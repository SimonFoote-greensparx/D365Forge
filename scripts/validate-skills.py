#!/usr/bin/env python3
"""Every SKILL.md has valid frontmatter, a name matching its folder, a usable description and the standard sections."""
import collections
from _common import skills, department_ids, STAGES, MODULES, STATUSES, finish

REQUIRED_SECTIONS = ["## When to use", "## Questions to ask first", "## Approach", "## Outputs",
                     "## Scale notes", "### SMB", "### Enterprise", "## Hand-offs", "## Sources", "## Never"]
problems, names = [], collections.defaultdict(list)
depts = set(department_ids())
all_skills = skills()
for s in all_skills:
    p, front, meta = s["path"], s["front"], s["meta"]
    if not front:
        problems.append(f"{p}: no frontmatter")
        continue
    if s["department"] not in depts:
        problems.append(f"{p}: department folder {s['department']!r} is not in catalogue/departments.toml")
    name, desc = s["name"], s["description"]
    if name != s["folder"]:
        problems.append(f"{p}: name {name!r} does not match folder {s['folder']!r}")
    if not name or not all(part.isalnum() and part.islower() for part in name.split("-")):
        problems.append(f"{p}: name {name!r} is not lowercase-hyphenated")
    if not (120 <= len(desc) <= 450):
        problems.append(f"{p}: description is {len(desc)} characters (keep it 120-450 so it triggers well and fits the budget)")
    if meta.get("department") != s["department"]:
        problems.append(f"{p}: metadata.department should be {s['department']!r}")
    for st in [x.strip() for x in meta.get("stages", "").split(",") if x.strip()] or ["(missing)"]:
        if st not in STAGES:
            problems.append(f"{p}: unknown stage {st!r}")
    for mo in [x.strip() for x in meta.get("modules", "").split(",") if x.strip()] or ["(missing)"]:
        if mo not in MODULES:
            problems.append(f"{p}: unknown module {mo!r}")
    if meta.get("status") not in STATUSES:
        problems.append(f"{p}: status must be one of {STATUSES}")
    for section in REQUIRED_SECTIONS:
        if f"\n{section}\n" not in s["body"] and not s["body"].startswith(section):
            problems.append(f"{p}: missing section {section!r}")
    if s["body"].rstrip().endswith("## Never"):
        problems.append(f"{p}: empty Never section")
    names[name].append(p)
for name, paths in names.items():
    if len(paths) > 1:
        problems.append(f"duplicate skill name {name!r}: {', '.join(paths)}")
finish("skills", problems, len(all_skills))
