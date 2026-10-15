#!/usr/bin/env python3
"""Every skill has trigger tests: at least three prompts that should load it and one near miss that should not."""
import glob, os, tomllib
from _common import path, skills, finish

problems = []
by_dept = {}
for f in glob.glob(path("tests", "triggers", "*.toml")):
    dept = os.path.splitext(os.path.basename(f))[0]
    try:
        by_dept[dept] = {s["name"]: s for s in tomllib.load(open(f, "rb")).get("skill", [])}
    except tomllib.TOMLDecodeError as e:
        problems.append(f"tests/triggers/{dept}.toml: invalid TOML: {e}")
all_skills = skills()
for s in all_skills:
    t = by_dept.get(s["department"], {}).get(s["folder"])
    ref = f"{s['department']}:{s['folder']}"
    if not t:
        problems.append(f"{ref}: no trigger tests in tests/triggers/{s['department']}.toml")
        continue
    if len(t.get("should_trigger", [])) < 3:
        problems.append(f"{ref}: fewer than three should_trigger prompts")
    if len(t.get("should_not_trigger", [])) < 1:
        problems.append(f"{ref}: no should_not_trigger near miss")
names = {(s["department"], s["folder"]) for s in all_skills}
for dept, tests in by_dept.items():
    for name in tests:
        if (dept, name) not in names:
            problems.append(f"tests/triggers/{dept}.toml: tests for unknown skill {name!r}")
finish("trigger tests", problems, len(all_skills))
