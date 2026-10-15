#!/usr/bin/env python3
"""docs/AGENT-SURFACES.md is coherent: every roster row has a charter, builders have a surface, reviewers have none,
and every file in the repository has exactly one owning agent."""
import glob, os, re
from _common import ROOT, path, finish

text = open(path("docs", "AGENT-SURFACES.md"), encoding="utf-8").read()
roster = {}
for m in re.finditer(r"^\|\s*`?([a-z0-9-]+)`?\s*\|\s*(builder|reviewer)\s*\|\s*(installed|planned)\s*\|", text, re.M):
    roster[m.group(1)] = (m.group(2), m.group(3))
surfaces = {}
for m in re.finditer(r"^### `?([a-z0-9-]+)`?\s*\n+```\n(.*?)\n```", text, re.M | re.S):
    surfaces[m.group(1)] = [line.strip() for line in m.group(2).splitlines() if line.strip()]
problems = []
charters = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(path(".claude", "agents", "*.md"))}
for agent, (cls, status) in roster.items():
    if status == "installed" and agent not in charters:
        problems.append(f"{agent}: installed but has no charter in .claude/agents/")
    if cls == "builder" and agent not in surfaces:
        problems.append(f"{agent}: builder with no surface block")
    if cls == "reviewer" and agent in surfaces:
        problems.append(f"{agent}: reviewers hold no write surface")
for c in charters - set(roster):
    problems.append(f".claude/agents/{c}.md: charter with no roster row")
for agent in surfaces:
    if agent not in roster:
        problems.append(f"{agent}: surface block with no roster row")


def to_regex(pattern: str) -> re.Pattern:
    out = ""
    i = 0
    while i < len(pattern):
        if pattern.startswith("**", i):
            out += ".*"; i += 2
        elif pattern[i] == "*":
            out += "[^/]*"; i += 1
        else:
            out += re.escape(pattern[i]); i += 1
    return re.compile(out + "$")


compiled = [(agent, p, to_regex(p)) for agent, pats in surfaces.items() for p in pats]
SKIP_DIRS = {".git", "dist", "__pycache__", "node_modules"}
files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for f in filenames:
        rel = os.path.relpath(os.path.join(dirpath, f), ROOT).replace(os.sep, "/")
        if rel.startswith(("input/", "output/")) and not rel.endswith(("README.md", ".gitkeep")):
            continue  # user data, git-ignored
        if rel.endswith(".pyc"):
            continue
        files.append(rel)
for rel in files:
    owners = sorted({agent for agent, _, rx in compiled if rx.match(rel)})
    if not owners:
        problems.append(f"{rel}: no owning agent")
    elif len(owners) > 1:
        problems.append(f"{rel}: claimed by {', '.join(owners)}")
finish("surface map", problems, len(files))
