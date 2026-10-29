#!/usr/bin/env python3
"""Package each department as a plugin archive for Microsoft Copilot Cowork. --check verifies.

Writes cowork/plugins/<department>.zip and cowork/README.md. Each archive is a Claude-format plugin
(.claude-plugin/plugin.json plus skills/), which Copilot Cowork's Upload plugin converts on import.
Archives are stored uncompressed with fixed timestamps so the same tree always produces the same bytes,
which is what lets --check prove they are current.
Inside each archive the plugin.json names the plugin d365forge-<department> and starts its description with
"D365Forge <Title>.", so Cowork lists the plugins under the D365Forge prefix (D27). The archive file names stay
<department>.zip, because the website's downloads and the GitHub links use them.
"""
import glob, io, json, os, zipfile
from _common import (departments, skills, path, write_or_check, write_or_check_bytes, check_flag, finish, REPO_URL,
                     DISPLAY_NAME, VERSION, cowork_plugin_name)

check, problems = check_flag(), []
FIXED = (2026, 1, 1, 0, 0, 0)
# File types Microsoft 365 Copilot accepts in a skill folder, from Microsoft Learn, "Custom skills in declarative
# agents", Supported file and script types. A skill folder holding any other type (for example .toml) is rejected on
# upload with "File extension '.toml' is not supported" (D21).
ALLOWED = {".md", ".txt", ".json", ".xml", ".yaml", ".yml", ".ini", ".config", ".utf8", ".log", ".csv", ".tsv", ".html",
           ".htm", ".pdf", ".rtf", ".docx", ".doc", ".docm", ".pptx", ".ppt", ".ppsm", ".xlsx", ".xls", ".xlsm", ".png",
           ".jpg", ".jpeg", ".gif", ".bmp", ".py", ".js", ".mjs", ".cjs", ".ts", ".mts", ".sh", ".bash"}
SAFE_NAME = __import__("re").compile(r"^[A-Za-z0-9._ !-]+$")
KEBAB = __import__("re").compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MANIFEST = os.path.join(".claude-plugin", "plugin.json")


def cowork_manifest(root: str, d: dict) -> bytes:
    """The department's Claude Code manifest, renamed with the D365Forge prefix for Copilot Cowork (D27)."""
    manifest = json.load(open(os.path.join(root, MANIFEST), encoding="utf-8"))
    manifest["name"] = cowork_plugin_name(d["id"])
    manifest["description"] = f"{DISPLAY_NAME} {d['title']}. {manifest['description']}"
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")

all_skills = skills()
rows = []
for d in departments():
    did = d["id"]
    root = path("plugins", did)
    members = [os.path.join(".claude-plugin", "plugin.json"), "README.md"]
    for f in sorted(glob.glob(os.path.join(root, "skills", "**", "*"), recursive=True)):
        if os.path.isfile(f):
            members.append(os.path.relpath(f, root))
    # Copilot Cowork limits: 20 skills per plugin; per skill, at most 20 companion files of supported types with safe
    # names, none hidden, each up to 5 MB and 10 MB in total.
    mine = [s for s in all_skills if s["department"] == did]
    name = cowork_plugin_name(did)
    if not KEBAB.match(name) or len(name) > 64:
        problems.append(f"{did}: Cowork plugin name {name} must be lowercase with single hyphens, at most 64 characters")
    if len(mine) > 20:
        problems.append(f"{did}: {len(mine)} skills; Copilot Cowork accepts at most 20 per plugin")
    for s in mine:
        folder = os.path.join(root, "skills", s["folder"])
        companions = [f for f in glob.glob(os.path.join(folder, "**", "*"), recursive=True)
                      if os.path.isfile(f) and os.path.basename(f) != "SKILL.md"]
        if len(companions) > 20:
            problems.append(f"{did}:{s['folder']}: {len(companions)} companion files; the limit is 20")
        sizes = [os.path.getsize(c) for c in companions]
        if any(n > 5 * 1024 * 1024 for n in sizes) or sum(sizes) > 10 * 1024 * 1024:
            problems.append(f"{did}:{s['folder']}: companion files exceed 5 MB each or 10 MB in total")
        for c in companions:
            rel = os.path.relpath(c, folder)
            if any(part.startswith(".") for part in rel.split(os.sep)):
                problems.append(f"{did}:{s['folder']}: hidden companion file {rel}")
            ext = os.path.splitext(c)[1].lower()
            if ext not in ALLOWED:
                problems.append(f"{did}:{s['folder']}: {rel} has a file type ({ext or 'none'}) that Microsoft 365 Copilot "
                                "rejects in a skill folder")
            if not all(SAFE_NAME.match(part) for part in rel.split(os.sep)):
                problems.append(f"{did}:{s['folder']}: {rel} has characters Copilot Cowork does not allow in file names")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_STORED) as z:
        for m in members:
            info = zipfile.ZipInfo(m.replace(os.sep, "/"), date_time=FIXED)
            info.external_attr = 0o644 << 16
            content = cowork_manifest(root, d) if m == MANIFEST else open(os.path.join(root, m), "rb").read()
            z.writestr(info, content)
    data = buf.getvalue()
    write_or_check_bytes(f"cowork/plugins/{did}.zip", data, check, problems)
    rows.append(f"| [{d['title']}](plugins/{did}.zip) | `{name}` | {len(mine)} | {len(data) // 1024} KB |")

readme = [f"# {DISPLAY_NAME} for Microsoft Copilot Cowork", "",
          "<!-- Generated by scripts/build-cowork.py. Do not edit by hand. -->", "",
          f"One plugin archive per department, version {VERSION}. Upload the ones your project needs in Copilot Cowork:",
          "**Customize** > **Plugins** > **Upload plugin**. Cowork converts each archive into a Cowork plugin, including its skills.", "",
          "The full guide, including single skills, custom instructions, tailored project packs and organisation-wide rollout, is",
          "[docs/COPILOT-COWORK.md](../docs/COPILOT-COWORK.md). Suggested custom instructions are in",
          "[custom-instructions.md](custom-instructions.md).", "",
          "Every plugin name in Cowork starts with `d365forge-`, so D365Forge sits clearly alongside other skill libraries. The",
          "archive files keep the department name (for example `sales.zip`), and the skills keep their own names.", "",
          "| Department | Plugin name | Skills | Size |", "|---|---|---|---|"] + rows + ["",
          "To download an archive from GitHub, open it and select **Download raw file**. The archives are regenerated from the",
          "skills by `python3 scripts/build-cowork.py`; never edit them by hand.", "",
          "## Credit", "",
          "The plugins were created by Simon Foote and Robert Peledie and are licensed under CC BY 4.0. Share them freely inside",
          "or outside your organisation; when you share or adapt them, keep the credit in each department README and in each",
          "skill's `license` and `authors` fields. [NOTICE.md](../NOTICE.md) gives the wording.", ""]
write_or_check("cowork/README.md", "\n".join(readme), check, problems)
finish("Copilot Cowork packages", problems, len(rows))
