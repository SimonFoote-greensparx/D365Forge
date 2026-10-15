#!/usr/bin/env python3
"""The role catalogue, role combinations, skills vocabulary and templates are consistent with each other."""
import re
from _common import load_toml, department_ids, skill_refs, templates, TEMPLATE_CREDIT, finish

problems = []
depts, refs = set(department_ids()), skill_refs()
vocab = {s["id"] for s in load_toml("data/skills-vocabulary.toml")["skill"]}
roles = load_toml("data/role-catalogue.toml")["role"]
role_ids = [r["id"] for r in roles]
if len(role_ids) != len(set(role_ids)):
    problems.append("data/role-catalogue.toml: duplicate role ids")
for r in roles:
    if r["department"] not in depts:
        problems.append(f"role {r['id']}: unknown department {r['department']!r}")
    for s in r.get("requires", []) + r.get("desirable", []):
        if s not in vocab:
            problems.append(f"role {r['id']}: skill {s!r} is not in data/skills-vocabulary.toml")
    for ed in r.get("editions", []):
        if ed not in ("smb", "enterprise"):
            problems.append(f"role {r['id']}: unknown edition {ed!r}")
for rule in load_toml("data/role-combinations.toml")["rule"]:
    for rid in rule["roles"]:
        if rid not in role_ids:
            problems.append(f"role combination names unknown role {rid!r}")
    if rule.get("severity") not in ("unsafe", "caution"):
        problems.append(f"role combination {rule['roles']}: severity must be unsafe or caution")
tpls = templates()
for t in tpls:
    f, where = t["front"], t["path"]
    for key in ("id", "title", "format", "owner", "tailored_from", "status"):
        if not f.get(key):
            problems.append(f"{where}: missing {key}")
    if f.get("id") and not where.endswith(f"/{f['id']}.md"):
        problems.append(f"{where}: id {f['id']!r} does not match the file name")
    if f.get("format") not in ("docx", "xlsx"):
        problems.append(f"{where}: format must be docx or xlsx")
    if f.get("owner") and f["owner"] not in refs:
        problems.append(f"{where}: owner {f['owner']!r} is not a skill")
    if f.get("format") == "xlsx" and "## Sheet:" not in t["body"]:
        problems.append(f"{where}: xlsx templates define worksheets with '## Sheet:' headings")
    if not t["text"].rstrip().endswith(TEMPLATE_CREDIT):
        problems.append(f"{where}: must end with the credit line from NOTICE.md (TEMPLATE_CREDIT in scripts/_common.py)")
    for m in re.finditer(r"\{\{\s*roles\.([a-z0-9-]+)\s*\}\}", t["text"]):
        if m.group(1) not in role_ids:
            problems.append(f"{where}: placeholder roles.{m.group(1)} is not in the role catalogue")
finish("data and templates", problems, len(roles) + len(tpls))
