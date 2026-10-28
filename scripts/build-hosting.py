#!/usr/bin/env python3
"""Build the website as a self-contained static site for any web host (Hostinger, Azure Static Web Apps, IIS...).

    python3 scripts/build-hosting.py [--site-url https://d365forge.ai/] [--no-github-links]

Writes dist/website/ and dist/d365forge-website.zip (dist/ is git-ignored). Unzip the archive into the web
root, for example public_html on Hostinger. See docs/HOSTING.md.

Unlike the GitHub Pages site in docs/, which links to files on GitHub, this build renders every guide, department,
skill, agent charter and template as its own page and serves the Copilot Cowork plugin archives from a download
area, so the site works on its own. Everything else that refers to the repository links to it on GitHub, and a web
address written out in the text always links to that address (D23). --no-github-links (or GITHUB_LINKS = False in
scripts/_common.py) shows repository-only references as plain text instead.
Run `bash scripts/build-all.sh` first so the generated pages and archives are current.
"""
from __future__ import annotations

import argparse, html, json, os, posixpath, re, shutil, sys, zipfile
from _common import (ROOT, path, departments, skills, templates, finish, REPO_URL, SITE_URL,
                     DISPLAY_NAME, VERSION, GITHUB_LINKS, MARKETPLACE, site_page, unlinked_repo_mentions)
import _markdown as md

ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
ap.add_argument("--site-url", default=SITE_URL, help="Public address of the hosted site (default: SITE_URL in scripts/_common.py)")
ap.add_argument("--no-github-links", dest="github_links", action="store_false", default=GITHUB_LINKS,
                help="Show repository-only references as plain text instead of linking to GitHub")
ap.add_argument("--out", default=path("dist", "website"))
ap.add_argument("--zip", default=path("dist", "d365forge-website.zip"))
opts = ap.parse_args()
SITE = opts.site_url.rstrip("/") + "/" if opts.site_url else ""
OUT = opts.out
GEN = "scripts/build-hosting.py"
e = html.escape
problems: list[str] = []
depts, all_skills, tpls = departments(), skills(), templates()
dept_by_id = {d["id"]: d for d in depts}
FIXED = (2026, 1, 1, 0, 0, 0)

# ------------------------------------------------------------------ where each repository file lives on the site
GUIDES = {"docs/GETTING-STARTED.md": "guides/getting-started.html", "docs/COPILOT-COWORK.md": "guides/copilot-cowork.html",
          "docs/USE-CASES.md": "guides/use-cases.html", "docs/ROADMAP.md": "guides/roadmap.html",
          "docs/SOURCES.md": "guides/sources.html", "cowork/custom-instructions.md": "guides/custom-instructions.html",
          "NOTICE.md": "credit.html", "templates/README.md": "templates/placeholders.html"}
GUIDE_ACTIVE = {"docs/COPILOT-COWORK.md": "Copilot Cowork", "cowork/custom-instructions.md": "Copilot Cowork",
                "templates/README.md": "Templates"}
FIXED_MAP = {**GUIDES, "README.md": "index.html", "AUTHORS.md": "index.html#authors", "LICENSE": "LICENSE.txt",
             "LICENSE-CODE": "LICENSE-CODE.txt", "CITATION.cff": "downloads/CITATION.cff",
             "cowork/README.md": "downloads.html", "cowork/plugins": "downloads.html", "cowork": "downloads.html",
             "templates": "templates.html", "plugins": "catalogue.html",
             "profiles/schema.json": "downloads/profiles/schema.json", "profiles/samples": "downloads.html#profiles",
             "docs/index.html": "index.html", "docs/catalogue.html": "catalogue.html", "docs/templates.html": "templates.html",
             "docs/profile-builder.html": "profile-builder.html", "docs/privacy.html": "privacy.html",
             "docs/contributors.html": "contributors.html"}


def hosted(repo_path: str) -> str | None:
    """The site path for a repository path, or None if the site does not carry it."""
    p = repo_path.strip("/")
    if p in FIXED_MAP:
        return FIXED_MAP[p]
    m = re.fullmatch(r"plugins/([a-z0-9-]+)(/README\.md)?", p)
    if m and m.group(1) in dept_by_id:
        return f"departments/{m.group(1)}.html"
    m = re.fullmatch(r"plugins/([a-z0-9-]+)/skills/([a-z0-9-]+)(/SKILL\.md)?", p)
    if m:
        return f"skills/{m.group(1)}/{m.group(2)}.html"
    m = re.fullmatch(r"plugins/([a-z0-9-]+)/skills/([a-z0-9-]+)/references/sources\.md", p)
    if m:
        return f"skills/{m.group(1)}/{m.group(2)}.html#sources"
    m = re.fullmatch(r"\.claude/agents/([a-z0-9-]+)\.md", p)
    if m and m.group(1) in dept_by_id:
        return f"charters/{m.group(1)}.html"
    m = re.fullmatch(r"templates/([a-z0-9-]+)\.md", p)
    if m:
        return f"templates/{m.group(1)}.html"
    m = re.fullmatch(r"cowork/plugins/([a-z0-9-]+)\.zip", p)
    if m:
        return f"downloads/{m.group(1)}.zip"
    m = re.fullmatch(r"profiles/samples/([a-z0-9-]+\.yaml)", p)
    if m:
        return f"downloads/profiles/{m.group(1)}"
    return None


def site_rel(target: str, page: str) -> str:
    """Relative href from the page at site path `page` to site path `target` (which may carry a #fragment)."""
    t, _, frag = target.partition("#")
    rel = posixpath.relpath(t, posixpath.dirname(page) or ".") if t else posixpath.basename(page)
    return rel + ("#" + frag if frag else "")


def github(repo_path: str) -> str:
    kind = "blob" if "." in posixpath.basename(repo_path) else "tree"
    return f"{REPO_URL}/{kind}/main/{repo_path}".rstrip("/")


dropped: dict[str, int] = {}


def resolve(href: str, page: str, source: str | None) -> str | None:
    """Rewrite one link found on the site page `page`. `source` is the repository file it was rendered from, used to
    resolve relative Markdown links; None for links already in generated HTML."""
    if href.startswith(("#", "mailto:")):
        return href
    if isinstance(href, md.BareURL) and href.startswith(REPO_URL):
        # An address the reader can see opens that address, not a page that happens to show the same content.
        if opts.github_links:
            return str(href)
        dropped[str(href)] = dropped.get(str(href), 0) + 1
        return None
    if href.startswith(SITE_URL) and SITE:
        return SITE + href[len(SITE_URL):]
    repo_path = None
    for prefix in (REPO_URL + "/blob/main/", REPO_URL + "/tree/main/"):
        if href.startswith(prefix):
            repo_path = href[len(prefix):]
    if href.rstrip("/") == REPO_URL:
        if opts.github_links:
            return href
        dropped[href] = dropped.get(href, 0) + 1
        return None
    if repo_path is None and not re.match(r"^[a-z]+:", href):
        if source is None:
            return href  # a relative link inside generated HTML already points within the site
        base = posixpath.dirname(source)
        target, _, frag = href.partition("#")
        repo_path = posixpath.normpath(posixpath.join(base, target)) + ("#" + frag if frag else "")
    if repo_path is None:
        return href  # an outside link
    target, _, frag = repo_path.partition("#")
    site = hosted(target)
    if site is not None:
        if frag and "#" not in site:
            site += "#" + frag
        return site_rel(site, page)
    if opts.github_links:
        return github(target) + ("#" + frag if frag else "")
    dropped[target] = dropped.get(target, 0) + 1
    return None


A_TAG = re.compile(r'<a ([^>]*?)href="([^"]*)"([^>]*)>(.*?)</a>', re.S)


def rewrite_html(fragment: str, page: str) -> str:
    """Rewrite the links in generated HTML. A link to the repository home is removed outright while it is private."""
    def sub(m: re.Match) -> str:
        new = resolve(html.unescape(m.group(2)), page, None)
        if new is None:
            if m.group(2).rstrip("/") == REPO_URL:
                return ""
            return m.group(4)
        return f'<a {m.group(1)}href="{e(new)}"{m.group(3)}>{m.group(4)}</a>'
    out = A_TAG.sub(sub, fragment)
    if SITE:
        out = out.replace(SITE_URL, SITE)
    return out


def render_md(text: str, page: str, source: str) -> str:
    out = md.render(text, lambda h: resolve(h, page, source))
    return out.replace(SITE_URL, SITE) if SITE else out


def root_of(page: str) -> str:
    return "../" * page.count("/")


pages: dict[str, str] = {}


def add_page(site_path: str, title: str, body: str, active: str = "") -> None:
    pages[site_path] = site_page(title, body, active, root=root_of(site_path), hosted=True,
                                 github_links=opts.github_links, generator=GEN)


def read(rel: str) -> str:
    return open(path(rel), encoding="utf-8").read()


def chips(items: list[tuple[str, str]]) -> str:
    return '<dl class="facts">' + "".join(f"<dt>{e(k)}</dt><dd>{v}</dd>" for k, v in items) + "</dl>"


def cowork_link(did: str, page: str) -> str:
    return f'<a href="{site_rel(f"downloads/{did}.zip", page)}" download>{e(dept_by_id[did]["title"])} plugin for Copilot Cowork</a>'


# ------------------------------------------------------------------ the six generated pages, re-wrapped
for name in ("index.html", "catalogue.html", "templates.html", "profile-builder.html", "privacy.html", "contributors.html"):
    src = read(f"docs/{name}")
    title = re.search(r"<title>(.*?) \| ", src).group(1)
    act = re.search(r'class="active">([^<]+)</a>', src)
    body = src[src.index('<main class="wrap">\n') + len('<main class="wrap">\n'):src.rindex("\n</main>")]
    body = rewrite_html(body, name)
    if name == "privacy.html":
        old = ("The website is a set of static pages hosted on GitHub Pages. It sets no cookies of its own and has no "
               "analytics. GitHub, as the host, may log requests as described in GitHub's own privacy statement.")
        if old not in body:
            problems.append("privacy.html: hosting sentence changed in build-site.py; update build-hosting.py to match")
        body = body.replace(old, "The website is a set of static pages. It sets no cookies of its own and has no analytics. "
                                 "Our web hosting provider may log requests, such as IP addresses and browser details, "
                                 "to operate and secure the service.")
    if name == "index.html":
        body = body.replace("<code>cowork/plugins/</code>", "the downloads page")
        body = body.replace("> powers GitHub's <em>Cite this repository</em> button.",
                            "> holds the citation details.")
    pages[name] = site_page(html.unescape(title), body, act.group(1) if act else "", hosted=True,
                            github_links=opts.github_links, generator=GEN)

# ------------------------------------------------------------------ guides and the credit notice
GUIDE_TITLES = {}
for rel, site in GUIDES.items():
    front, text = md.strip_frontmatter(read(rel))
    m = re.search(r"^# (.+)$", text, re.M)
    GUIDE_TITLES[rel] = m.group(1) if m else rel
    body = render_md(text, site, rel)
    if rel == "docs/COPILOT-COWORK.md":
        body = (f'<div class="notice">Download the plugin archives from the <a href="{site_rel("downloads.html", site)}">'
                f'downloads page</a>. The steps below say where to upload them.</div>\n') + body
    add_page(site, re.sub(r"[`*]", "", GUIDE_TITLES[rel]), body, GUIDE_ACTIVE.get(rel, ""))

# ------------------------------------------------------------------ departments and agent charters
for d in depts:
    did = d["id"]
    site = f"departments/{did}.html"
    _, text = md.strip_frontmatter(read(f"plugins/{did}/README.md"))
    box = (f'<div class="callout"><strong>Use it in Copilot Cowork:</strong> download the {cowork_link(did, site)} '
           f'and upload it in Cowork under <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em>. '
           f'<a href="{site_rel("guides/copilot-cowork.html", site)}">How to install</a>.</div>')
    crumbs = f'<p class="crumbs"><a href="{site_rel("catalogue.html", site)}">Catalogue</a> &rsaquo; {e(d["title"])}</p>'
    add_page(site, d["title"], crumbs + render_md(text, site, f"plugins/{did}/README.md").replace("</h1>", "</h1>\n" + box, 1),
             "Catalogue")

    charter_rel = f".claude/agents/{did}.md"
    if os.path.exists(path(charter_rel)):
        site = f"charters/{did}.html"
        front, text = md.strip_frontmatter(read(charter_rel))
        crumbs = (f'<p class="crumbs"><a href="{site_rel("catalogue.html", site)}">Catalogue</a> &rsaquo; '
                  f'<a href="{site_rel(f"departments/{did}.html", site)}">{e(d["title"])}</a> &rsaquo; Agent charter</p>')
        if not re.search(r"^# ", text, re.M):
            text = f"# {d['title']} agent charter\n\n" + text
        add_page(site, f"{d['title']} agent charter", crumbs + render_md(text, site, charter_rel), "Catalogue")

# ------------------------------------------------------------------ skills
for s in all_skills:
    did, name = s["department"], s["folder"]
    site = f"skills/{did}/{name}.html"
    rel = s["path"]
    _, text = md.strip_frontmatter(read(rel))
    meta = s["meta"]
    facts = chips([
        ("Department", f'<a href="{site_rel(f"departments/{did}.html", site)}">{e(dept_by_id[did]["title"])}</a>'),
        ("Stages", e(meta.get("stages", ""))), ("Modules", e(meta.get("modules", ""))),
        ("Status", f'<span class="status {e(meta.get("status", ""))}">{e(meta.get("status", ""))}</span>'),
        ("Copilot Cowork", f"{cowork_link(did, site)}, or this skill on its own: "
                           f'<a href="{site_rel(f"downloads/skills/{did}/{name}/SKILL.md", site)}" download>Download SKILL.md</a>'),
        ("Claude Code", f"<code>/plugin install {e(did)}@{MARKETPLACE}</code>"),
        ("Licence", f'<a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, by {e(str(meta.get("authors", "")))}'),
    ])
    crumbs = (f'<p class="crumbs"><a href="{site_rel("catalogue.html", site)}">Catalogue</a> &rsaquo; '
              f'<a href="{site_rel(f"departments/{did}.html", site)}">{e(dept_by_id[did]["title"])}</a> &rsaquo; {e(name)}</p>')
    body = render_md(text, site, rel)
    body = body.replace("</h1>", "</h1>\n" + facts, 1)
    sources_rel = rel.replace("SKILL.md", "references/sources.md")
    if os.path.exists(path(sources_rel)):
        _, stext = md.strip_frontmatter(read(sources_rel))
        stext = re.sub(r"^# .*\n", "", stext, count=1)
        stext = re.sub(r"^Generated by .*\n", "", stext, flags=re.M)
        stext = re.sub(r"^## ", "### ", stext, flags=re.M)
        body += f'\n<section id="sources" class="sources"><h2>Sources for this skill</h2>{render_md(stext, site, sources_rel)}</section>'
    add_page(site, f"{name} ({dept_by_id[did]['title']})", crumbs + body, "Catalogue")

# ------------------------------------------------------------------ templates
for t in tpls:
    tid = t["front"].get("id", "")
    site = f"templates/{tid}.html"
    owner = t["front"].get("owner", "")
    od, _, oskill = owner.partition(":")
    facts = chips([
        ("Format", "Word (docx)" if t["front"].get("format") == "docx" else "Excel (xlsx)"),
        ("Owning skill", f'<a href="{site_rel(f"skills/{od}/{oskill}.html", site)}"><code>{e(owner)}</code></a>'),
        ("Tailored from", e(t["front"].get("tailored_from", ""))),
        ("Status", e(t["front"].get("status", ""))),
    ])
    crumbs = f'<p class="crumbs"><a href="{site_rel("templates.html", site)}">Templates</a> &rsaquo; {e(t["front"].get("title", tid))}</p>'
    body = render_md(t["body"], site, t["path"]).replace("</h1>", "</h1>\n" + facts, 1)
    add_page(site, t["front"].get("title", tid), crumbs + body, "Templates")

# ------------------------------------------------------------------ downloads
site = "downloads.html"
rows = []
for d in depts:
    did = d["id"]
    z = path("cowork", "plugins", f"{did}.zip")
    if not os.path.exists(z):
        problems.append(f"cowork/plugins/{did}.zip missing; run bash scripts/build-all.sh")
        continue
    count = sum(1 for s in all_skills if s["department"] == did)
    rows.append(f'<tr><td><a href="departments/{did}.html">{e(d["title"])}</a></td><td>{count}</td>'
                f'<td>{os.path.getsize(z) // 1024} KB</td><td><a href="downloads/{did}.zip" download>{did}.zip</a></td></tr>')
samples = sorted(f for f in os.listdir(path("profiles", "samples")) if f.endswith(".yaml"))
downloads = f"""<h1>Downloads</h1>
<p class="lead">Everything you need to use {DISPLAY_NAME} in Microsoft Copilot Cowork, version {VERSION}. Each department is
one plugin archive; download only the ones your project needs.</p>
<h2>Copilot Cowork plugins</h2>
<p>In Copilot Cowork, select <em>Customize</em> &gt; <em>Plugins</em> &gt; <em>Upload plugin</em> and choose an archive. Cowork
converts it into a plugin with its skills. The <a href="guides/copilot-cowork.html">Copilot Cowork guide</a> covers single
skills, sharing with your team and updates, and the <a href="guides/custom-instructions.html">suggested custom instructions</a>
help Cowork use the skills well.</p>
<div class="table-wrap"><table class="grid"><thead><tr><th>Department</th><th>Skills</th><th>Size</th><th>Download</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div>
<h2 id="profiles">Organisation profiles</h2>
<p>The project-tailoring department turns an organisation profile into named roles, a skills-gap view and project templates.
Build one with the <a href="profile-builder.html">profile builder</a>, or start from a fictional sample:</p>
<ul>{"".join(f'<li><a href="downloads/profiles/{e(f)}" download>{e(f)}</a></li>' for f in samples)}
<li><a href="downloads/profiles/schema.json" download>schema.json</a> (the profile format)</li></ul>
<h2>Credit and citation</h2>
<p>The plugins, skills and templates are licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
(<a href="LICENSE.txt">licence text</a>); the code under MIT (<a href="LICENSE-CODE.txt">licence text</a>). When you share or
adapt them, credit Simon Foote and Robert Peledie as described on the <a href="credit.html">credit page</a>.
<a href="downloads/CITATION.cff" download>CITATION.cff</a> holds the citation details.</p>"""
add_page(site, "Downloads", downloads, "Downloads")

# ------------------------------------------------------------------ not found page (root-relative, served at any depth)
notfound = site_page("Page not found", f"""<h1>Page not found</h1>
<p class="lead">That page does not exist or has moved.</p>
<p>Try the <a href="/catalogue.html">catalogue</a>, the <a href="/templates.html">templates</a> or the
<a href="/downloads.html">downloads</a>, or go back to the <a href="/index.html">home page</a>.</p>""",
                     "", root="/", hosted=True, github_links=opts.github_links, generator=GEN)
pages["404.html"] = notfound.replace('href="/http', 'href="http')

# ------------------------------------------------------------------ write the site
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)


def put(rel: str, data: bytes | str) -> None:
    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "wb") as fh:
        fh.write(data.encode("utf-8") if isinstance(data, str) else data)


for rel, content in pages.items():
    put(rel, content)
for dirpath, _, files in os.walk(path("docs", "assets")):
    for f in files:
        full = os.path.join(dirpath, f)
        put(os.path.relpath(full, path("docs")).replace(os.sep, "/"), open(full, "rb").read())
for d in depts:
    z = path("cowork", "plugins", f"{d['id']}.zip")
    if os.path.exists(z):
        put(f"downloads/{d['id']}.zip", open(z, "rb").read())
for f in samples:
    put(f"downloads/profiles/{f}", open(path("profiles", "samples", f), "rb").read())
put("downloads/profiles/schema.json", open(path("profiles", "schema.json"), "rb").read())
for s in all_skills:
    put(f"downloads/skills/{s['department']}/{s['folder']}/SKILL.md", open(path(s["path"]), "rb").read())
put("downloads/CITATION.cff", open(path("CITATION.cff"), "rb").read())
put("LICENSE.txt", open(path("LICENSE"), "rb").read())
put("LICENSE-CODE.txt", open(path("LICENSE-CODE"), "rb").read())

put(".htaccess", f"""# {DISPLAY_NAME} website. Generated by {GEN}. Static files only; works on Apache and LiteSpeed (Hostinger).
Options -Indexes
DirectoryIndex index.html
ErrorDocument 404 /404.html
AddDefaultCharset utf-8
AddType application/zip .zip
AddType text/plain .cff .yaml
AddType text/markdown .md
<IfModule mod_headers.c>
  <FilesMatch "\\.(zip|cff|yaml|md)$">
    Header set Content-Disposition attachment
  </FilesMatch>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set X-Frame-Options "SAMEORIGIN"
</IfModule>
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/html "access plus 0 seconds"
  ExpiresByType text/css "access plus 7 days"
  ExpiresByType image/jpeg "access plus 30 days"
</IfModule>
""")
robots = "User-agent: *\nAllow: /\n"
if SITE:
    robots += f"Sitemap: {SITE}sitemap.xml\n"
    urls = sorted(p for p in pages if p != "404.html")
    put("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{e(SITE + ('' if p == 'index.html' else p))}</loc></url>\n" for p in urls) + "</urlset>\n")
put("robots.txt", robots)

# ------------------------------------------------------------------ check every local link and image resolves
for rel in pages:
    if rel == "404.html":
        continue
    for m in re.finditer(r'(?:href|src)="([^"]+)"', pages[rel]):
        h = html.unescape(m.group(1))
        if re.match(r"^[a-z]+:", h) or h.startswith(("#", "/")):
            continue
        target = posixpath.normpath(posixpath.join(posixpath.dirname(rel), h.partition("#")[0]))
        if not os.path.exists(os.path.join(OUT, target)):
            problems.append(f"{rel}: broken link {h}")
for rel, content in pages.items():
    if f'href="{REPO_URL}' in content and not opts.github_links:
        problems.append(f"{rel}: links to GitHub although GitHub links are off")
    if opts.github_links:
        for url in unlinked_repo_mentions(content):
            problems.append(f"{rel}: the repository address {url} is shown but not linked")

# ------------------------------------------------------------------ zip, files at the top level
os.makedirs(os.path.dirname(opts.zip), exist_ok=True)
names = []
for dirpath, _, files in os.walk(OUT):
    for f in files:
        names.append(os.path.relpath(os.path.join(dirpath, f), OUT).replace(os.sep, "/"))
with zipfile.ZipFile(opts.zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for n in sorted(names):
        info = zipfile.ZipInfo(n, date_time=FIXED)
        info.external_attr = 0o644 << 16
        info.compress_type = zipfile.ZIP_DEFLATED
        z.writestr(info, open(os.path.join(OUT, n), "rb").read())
print(f"  {len(pages)} pages, {len(names)} files, {os.path.getsize(opts.zip) // 1024} KB -> {os.path.relpath(opts.zip, ROOT)}")
if dropped:
    print(f"  {sum(dropped.values())} references to repository-only files shown as plain text (GitHub links are off): "
          + ", ".join(sorted(dropped)[:8]) + ("..." if len(dropped) > 8 else ""))
finish("hosted website", problems, len(pages))
