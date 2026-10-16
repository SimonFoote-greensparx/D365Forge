"""Shared helpers for the build and check scripts. Standard library only (Python 3.11+)."""
from __future__ import annotations

import glob
import os
import re
import sys
import tomllib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPO_URL = "https://github.com/SimonFoote-greensparx/dynamics-365-ce-roster"
MARKETPLACE = "dynamics-365-ce-roster"
DISPLAY_NAME = "D365 CE Roster"
TAGLINE = ("Your Dynamics 365 CRM project team as installable AI agents: roles, skills and tailored templates "
           "for Sales, Marketing, Customer Service and Field Service, from SMB to enterprise.")
AUTHORS = [
    {"name": "Simon Foote", "slug": "simon-foote", "photo": "docs/assets/authors/simon-foote.jpg",
     "url": "https://www.linkedin.com/in/simonjayfoote/",
     "headline": "Microsoft AI and Power Platform Architect. Founder of greensparx and WaiFinder.",
     "project_role": "Builds the agents, skills, plugins, repository and website, and leads the data and development departments.",
     "bio": [
         "Simon has worked with Microsoft Dynamics CRM and Dynamics 365 for more than a decade. He started in 2014 as a "
         "technical consultant implementing Dynamics CRM for clients, then led the CRM and business intelligence teams at "
         "ISS Facility Services and Mitie. He was a Microsoft technical specialist and data engineer in IBM's UK Client "
         "Innovation Centre, and an architect, consultant and developer on Dynamics 365 CE and Power Apps at Zenzero. At "
         "Resonate he grew a small group of citizen developers into a multi-skilled Power Platform and Azure development "
         "department, introducing Scrum, DevOps and ALM. He went on to lead Power Platform Centre of Excellence work for "
         "central government at Hitachi Solutions and the Power Platform capability at Sharp UK.",
         "Today he is a Microsoft AI and Power Platform architect and the founder of greensparx. He helps organisations "
         "adopt Microsoft Copilot by finding the use cases that pay back, putting governance and responsible AI guardrails "
         "in place before scaling, and building Copilot Studio agents grounded in their own data. Through WaiFinder, which "
         "he founded in 2025, he gives managed service providers and consultancies a structured approach to AI adoption, "
         "compliance and governance.",
     ]},
    {"name": "Robert Peledie", "slug": "robert-peledie", "photo": "docs/assets/authors/robert-peledie.jpg",
     "url": "https://www.linkedin.com/in/robertpeledie/",
     "headline": "Solution and Enterprise Architect. TOGAF certified. Managing Director of 365Knowledge.",
     "project_role": "Designs the capabilities, specifies each department, reviews every skill and template, and leads testing.",
     "bio": [
         "Rob has designed and delivered Microsoft Dynamics CRM and Dynamics 365 solutions since 2008. He began as a CRM "
         "consultant on projects across the UK and Europe, led CRM delivery for more than 300 users across the UK, US and "
         "Asia-Pacific offices of GDS Group, and was development lead and Scrum Master for the Dynamics CRM and AX team at "
         "OVO Energy. As head of Dynamics CRM at Chorus he managed consultants, developers and support analysts serving "
         "more than 2,000 users.",
         "Since 2016 he has run 365Knowledge, an independent solution and enterprise architecture consultancy. Its clients "
         "have included the University of Bath, Hodge Bank, the Jersey Financial Services Commission, London Marathon "
         "Events, Walsall Council, Cycling UK, Barratt Developments and Unite Students, with work spanning sales, "
         "marketing, portals, chatbots, APIs and integration with product information and CPQ systems. He specialises in "
         "end-to-end architecture across CRM, ERP, analytics and custom applications, and in connecting systems through "
         "APIs, middleware and messaging. A TOGAF-certified enterprise architect and Certified Scrum Master, he has also "
         "written about Dynamics 365 for TechTarget since 2014.",
     ]},
]
AUTHOR_LINE = "Simon Foote and Robert Peledie"
# Licensing (D19): content under CC BY 4.0 in LICENSE, code under MIT in LICENSE-CODE. NOTICE.md says how to credit.
CONTENT_LICENCE = "CC-BY-4.0"
CODE_LICENCE = "MIT"
COPYRIGHT_HOLDER = "Simon Foote, Robert Peledie and the dynamics-365-ce-roster contributors"
CC_BY_URL = "https://creativecommons.org/licenses/by/4.0/"
CREDIT_LINE = (f'"D365 CE Roster" by Simon Foote and Robert Peledie ({REPO_URL}), licensed under CC BY 4.0 ({CC_BY_URL}).')
TEMPLATE_CREDIT = (f"> Credit: Template from D365 CE Roster by Simon Foote and Robert Peledie ({REPO_URL}), licensed under "
                   "CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you "
                   "may keep it as a footer or remove it.")
SITE_URL = "https://simonfoote-greensparx.github.io/dynamics-365-ce-roster/"
# The websites link every mention of the GitHub repository to it (D23). While the repository is private, only people
# who have been given access can open those links; others see GitHub's "page not found". Set to False, or build the
# hosted site with --no-github-links, to show repository-only references as plain text instead.
GITHUB_LINKS = True
REPO_RX = re.compile(r"https?://github\.com/SimonFoote-greensparx/dynamics-365-ce-roster[^\s<>()\[\]\"']*")


def linkify(text: str) -> str:
    """Escape text for HTML and turn every web address in it into a link that opens that address."""
    import html as _html
    out, last = [], 0
    for m in re.finditer(r"https?://[^\s<>()\[\]\"']+", text):
        url = m.group(0).rstrip(".,;:!?")
        out.append(_html.escape(text[last:m.start()]))
        out.append(f'<a href="{_html.escape(url)}">{_html.escape(url)}</a>')
        last = m.start() + len(url)
    out.append(_html.escape(text[last:]))
    return "".join(out)


def unlinked_repo_mentions(page: str) -> list[str]:
    """Web addresses of the repository that a reader sees on the page but cannot click. Commands in code blocks and
    data inside scripts are not counted: those are meant to be copied, not followed."""
    body = re.sub(r"<script\b.*?</script>|<pre\b.*?</pre>|<code\b.*?</code>|<textarea\b.*?</textarea>", "", page, flags=re.S)
    body = re.sub(r"<a\b[^>]*>.*?</a>", "", body, flags=re.S)
    body = re.sub(r"<[^>]+>", " ", body)
    return [m.group(0) for m in REPO_RX.finditer(body)]


def site_page(title: str, body: str, active: str, *, root: str = "", hosted: bool = False,
              github_links: bool = GITHUB_LINKS, generator: str = "scripts/build-site.py") -> str:
    """The shared page shell for the website. `root` is the relative path from the page back to the site root.

    GitHub Pages (hosted=False) links guides and files to GitHub. The hosted build (hosted=True) links to its own
    rendered pages and download area, and to GitHub for everything else unless github_links is off."""
    import html as _html
    blob = REPO_URL + "/blob/main/"
    if hosted:
        nav = [("index.html", "Home"), ("catalogue.html", "Catalogue"), ("templates.html", "Templates"),
               ("profile-builder.html", "Profile builder"), ("guides/copilot-cowork.html", "Copilot Cowork"),
               ("downloads.html", "Downloads")]
        if github_links:
            nav.append((REPO_URL, "GitHub"))
        credit = "credit.html"
    else:
        nav = [("index.html", "Home"), ("catalogue.html", "Catalogue"), ("templates.html", "Templates"),
               ("profile-builder.html", "Profile builder"), (blob + "docs/COPILOT-COWORK.md", "Copilot Cowork"),
               (REPO_URL, "GitHub")]
        credit = blob + "NOTICE.md"

    def href(h: str) -> str:
        return h if h.startswith("http") else root + h

    links = "".join(f'<a href="{href(h)}"{" class=\"active\"" if t == active else ""}>{t}</a>' for h, t in nav)
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{_html.escape(title)} | {DISPLAY_NAME}</title>
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<!-- Generated by {generator}. Do not edit by hand. -->
<header class="top"><div class="wrap"><a class="brand" href="{root}index.html">{DISPLAY_NAME}</a><nav>{links}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap">Created by Simon Foote and Robert Peledie. Content licensed under <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, code under MIT. <a href="{href(credit)}">How to credit</a> · <a href="{root}privacy.html">Privacy</a><br>An independent community project, not affiliated with or endorsed by Microsoft.</div></footer>
</body>
</html>
"""
VERSION = "0.1.0"
STAGES = ["Strategize", "Initiate", "Implement", "Prepare", "Operate"]
MODULES = ["Sales", "Marketing", "Customer Service", "Field Service", "All"]
STATUSES = ["draft", "reviewed", "stable"]
LAYERS = {"module": "Module", "delivery": "Delivery", "reviewer": "Reviewer", "tailoring": "Tailoring"}


def path(*parts: str) -> str:
    return os.path.join(ROOT, *parts)


def load_toml(rel: str) -> dict:
    with open(path(rel), "rb") as fh:
        return tomllib.load(fh)


def departments() -> list[dict]:
    return load_toml("catalogue/departments.toml")["department"]


def department_ids() -> list[str]:
    return [d["id"] for d in departments()]


FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def parse_frontmatter(text: str) -> tuple[dict, str] | tuple[None, str]:
    """Parse the small YAML subset skills and templates use: scalars plus one nested mapping level."""
    m = FRONT.match(text)
    if not m:
        return None, text
    data: dict = {}
    current = None
    for raw in m.group(1).splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")) and current is not None:
            key, _, value = raw.strip().partition(":")
            data[current][key.strip()] = value.strip().strip('"')
            continue
        key, _, value = raw.partition(":")
        key, value = key.strip(), value.strip()
        if value == "":
            data[key] = {}
            current = key
        else:
            data[key] = value.strip('"')
            current = None
    return data, text[m.end():]


def skills() -> list[dict]:
    """Every skill on disk, with its parsed frontmatter, body and title."""
    found = []
    for p in sorted(glob.glob(path("plugins", "*", "skills", "*", "SKILL.md"))):
        dept = p.split(os.sep)[-4]
        folder = p.split(os.sep)[-2]
        text = open(p, encoding="utf-8").read()
        front, body = parse_frontmatter(text)
        title = re.search(r"^# (.+)$", body, re.M)
        found.append({
            "path": os.path.relpath(p, ROOT), "department": dept, "folder": folder,
            "front": front or {}, "body": body, "text": text,
            "name": (front or {}).get("name", ""), "description": (front or {}).get("description", ""),
            "meta": (front or {}).get("metadata", {}) if isinstance((front or {}).get("metadata"), dict) else {},
            "title": title.group(1).strip() if title else folder,
        })
    return found


def skill_refs() -> set[str]:
    return {f"{s['department']}:{s['folder']}" for s in skills()}


def sources() -> list[dict]:
    items = []
    for p in sorted(glob.glob(path("sources", "*.toml"))):
        with open(p, "rb") as fh:
            for s in tomllib.load(fh).get("source", []):
                s["_file"] = os.path.relpath(p, ROOT)
                items.append(s)
    return items


def templates() -> list[dict]:
    items = []
    for p in sorted(glob.glob(path("templates", "*.md"))):
        if os.path.basename(p).upper() == "README.MD":
            continue
        text = open(p, encoding="utf-8").read()
        front, body = parse_frontmatter(text)
        items.append({"path": os.path.relpath(p, ROOT), "front": front or {}, "body": body, "text": text})
    return items


def write_or_check(rel: str, content: str, check: bool, problems: list[str]) -> None:
    """Write a generated file, or in --check mode report it as stale instead."""
    target = path(rel)
    current = open(target, encoding="utf-8").read() if os.path.exists(target) else None
    if current == content:
        return
    if check:
        problems.append(f"{rel} is out of date; run the generator")
        return
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)


def finish(label: str, problems: list[str], count: int | None = None) -> None:
    for p in problems:
        print(f"  {p}")
    suffix = f"{count} checked, " if count is not None else ""
    print(f"{label}: {suffix}{len(problems)} problems")
    sys.exit(1 if problems else 0)


def check_flag() -> bool:
    return "--check" in sys.argv[1:]


def write_or_check_bytes(rel: str, content: bytes, check: bool, problems: list[str]) -> None:
    """Binary twin of write_or_check, for generated archives."""
    target = path(rel)
    current = open(target, "rb").read() if os.path.exists(target) else None
    if current == content:
        return
    if check:
        problems.append(f"{rel} is out of date; run the generator")
        return
    os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
    with open(target, "wb") as fh:
        fh.write(content)


# ---------------------------------------------------------------- profile schema (the subset of JSON Schema it uses)
TYPES = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool}


def validate_schema(value, sch, where, problems):
    t = sch.get("type")
    if t and not (isinstance(value, TYPES[t]) and not (t == "integer" and isinstance(value, bool))):
        problems.append(f"{where}: expected {t}"); return
    if "enum" in sch and value not in sch["enum"]:
        problems.append(f"{where}: {value!r} not in {sch['enum']}")
    if "pattern" in sch and isinstance(value, str) and not re.search(sch["pattern"], value):
        problems.append(f"{where}: {value!r} does not match {sch['pattern']}")
    if "minimum" in sch and isinstance(value, int) and value < sch["minimum"]:
        problems.append(f"{where}: below minimum {sch['minimum']}")
    if "maximum" in sch and isinstance(value, int) and value > sch["maximum"]:
        problems.append(f"{where}: above maximum {sch['maximum']}")
    if t == "object":
        for req in sch.get("required", []):
            if req not in value:
                problems.append(f"{where}: missing {req}")
        props = sch.get("properties", {})
        for k, v in value.items():
            if k in props:
                validate_schema(v, props[k], f"{where}.{k}", problems)
            elif sch.get("additionalProperties") is False:
                problems.append(f"{where}: unexpected key {k!r}")
    if t == "array":
        if len(value) < sch.get("minItems", 0):
            problems.append(f"{where}: needs at least {sch['minItems']} items")
        for i, item in enumerate(value):
            validate_schema(item, sch.get("items", {}), f"{where}[{i}]", problems)
