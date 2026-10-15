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
    {"name": "Simon Foote", "role": "Builder and maintainer (data and development)",
     "url": "https://www.linkedin.com/in/simonjayfoote/"},
    {"name": "Robert Peledie", "role": "CRM Architect (capability design, review and testing)",
     "url": "https://www.linkedin.com/in/robertpeledie/"},
]
AUTHOR_LINE = "Simon Foote and Robert Peledie"
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
