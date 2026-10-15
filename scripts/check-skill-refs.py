#!/usr/bin/env python3
"""Every `department:skill` reference in skills, templates, docs, charters and tests resolves to a real skill."""
import glob, re
from _common import ROOT, path, skill_refs, department_ids, finish

refs = skill_refs()
depts = set(department_ids())
pattern = re.compile(r"`([a-z0-9-]+):([a-z0-9-]+)`")
files = (glob.glob(path("plugins", "*", "skills", "*", "SKILL.md")) + glob.glob(path("templates", "*.md"))
         + glob.glob(path("docs", "*.md")) + glob.glob(path(".claude", "agents", "*.md"))
         + glob.glob(path("editions", "**", "*.md"), recursive=True) + [path("README.md"), path("AGENTS.md")])
problems, checked = [], 0
for f in files:
    try:
        text = open(f, encoding="utf-8").read()
    except FileNotFoundError:
        continue
    for m in pattern.finditer(text):
        dept, skill = m.groups()
        if dept not in depts:
            continue  # not a skill reference (for example `owner:` style notes)
        checked += 1
        if f"{dept}:{skill}" not in refs:
            problems.append(f"{f.replace(ROOT + '/', '')}: unresolved reference {dept}:{skill}")
# Trigger tests name skills in the expected field.
for f in glob.glob(path("tests", "triggers", "*.toml")):
    for m in re.finditer(r'expected\s*=\s*"([a-z0-9-]+:[a-z0-9-]+)"', open(f, encoding="utf-8").read()):
        checked += 1
        if m.group(1) not in refs:
            problems.append(f"{f.replace(ROOT + '/', '')}: unresolved expected skill {m.group(1)}")
finish("skill references", problems, checked)
