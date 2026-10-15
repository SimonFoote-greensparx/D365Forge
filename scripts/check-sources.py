#!/usr/bin/env python3
"""The source catalogue is well formed and every department or skill it names exists."""
import re
from _common import sources, department_ids, skill_refs, finish

REQUIRED = ["id", "title", "publisher", "url", "licence", "jurisdiction", "authoritative_for", "departments", "checked"]
LICENCES = {"cite-only", "check-terms", "ogl-v3", "cc-by-4.0", "public-domain"}
problems, seen = [], set()
depts, refs = set(department_ids()), skill_refs()
items = sources()
for s in items:
    where = f"{s['_file']}:{s.get('id', '?')}"
    for key in REQUIRED:
        if key not in s or s[key] in ("", []):
            problems.append(f"{where}: missing {key}")
    if s.get("id") in seen:
        problems.append(f"{where}: duplicate id")
    seen.add(s.get("id"))
    if s.get("licence") not in LICENCES:
        problems.append(f"{where}: licence {s.get('licence')!r} is not one of {sorted(LICENCES)}")
    if not str(s.get("url", "")).startswith("https://"):
        problems.append(f"{where}: url must be https")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(s.get("checked", ""))):
        problems.append(f"{where}: checked must be YYYY-MM-DD")
    for d in s.get("departments", []):
        if d not in depts:
            problems.append(f"{where}: unknown department {d!r}")
    for r in s.get("skills", []):
        if r not in refs:
            problems.append(f"{where}: unknown skill {r!r}")
finish("source catalogue", problems, len(items))
