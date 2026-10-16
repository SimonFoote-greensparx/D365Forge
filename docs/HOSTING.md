# Hosting the website

The website can be published in two ways.

| | GitHub Pages | Any web host (for example Hostinger) |
|---|---|---|
| Built by | `scripts/build-site.py`, into `docs/` | `scripts/build-hosting.py`, into `dist/` |
| Guides, skills and templates | Linked to their files on GitHub | Rendered as pages on the site |
| Copilot Cowork plugins | Downloaded from GitHub | Served from the site's Downloads page |
| Needs the repository to be public | Yes, or a paid GitHub plan | No |

## Build the hosted site

```
bash scripts/build-all.sh
python3 scripts/build-hosting.py --site-url https://your-domain.example/
```

This writes `dist/website/` and `dist/d365-ce-roster-website.zip`. `dist/` is git-ignored, so the archive is never
committed. `--site-url` is optional; when given, the build adds a `sitemap.xml` and uses that address wherever the
guides name the website. The script checks that every link and image on every page resolves, and fails if one does not.

The hosted site contains:

- the home, catalogue, templates, profile builder and privacy pages;
- a page for every guide, department, agent charter, skill and template, and the credit notice;
- a Downloads page with the 17 Copilot Cowork plugin archives, every skill's `SKILL.md`, the sample organisation
  profiles and the profile schema;
- the licence texts, a `404.html` page, `robots.txt` and an `.htaccess` file for Apache and LiteSpeed servers.

While the repository is private, links to files that only exist in the repository are shown as plain text, and the
GitHub links are left out. When the repository is made public, set `REPO_PUBLIC = True` in `scripts/_common.py` (or
pass `--repo-public`) and rebuild.

## Upload to Hostinger

1. In hPanel, open the website and go to **File Manager**.
2. Open `public_html`. If it holds a placeholder page, such as `default.php`, delete it.
3. Upload `d365-ce-roster-website.zip` into `public_html`.
4. Right-click the archive, select **Extract**, and extract it into `public_html` itself, not a new folder. The archive
   holds the site files at its top level, so `index.html` ends up directly in `public_html`.
5. Delete the archive once it has been extracted.
6. Turn on SSL for the domain in hPanel, and force HTTPS, if the domain does not have it already.
7. Open the site and check the home page, a skill page and a download.

The site is plain HTML and CSS with two small scripts (the catalogue search and the profile builder). It needs no PHP,
no database and no build step on the server. It also works in a subfolder, except that the 404 page loses its styling
there because the server can show it at any address.

## Update the hosted site

Rebuild, then upload and extract the new archive over the old files. Extracting replaces the files that changed. If
pages have been removed or renamed, delete the old folders in `public_html` first (or empty `public_html`) so that
stale pages do not linger.

## Privacy

The hosted privacy page says the site sets no cookies and has no analytics, and that the web host may log requests.
If you add analytics, a cookie banner or a contact form, update the privacy page in `scripts/build-site.py` and the
hosted wording in `scripts/build-hosting.py` first.
