#!/usr/bin/env python3
"""Emit an edition (smb or enterprise) as a standalone tree in dist/<edition>/, splicing context fragments into skills.

  python3 scripts/build-edition.py smb            emit dist/dynamics-365-ce-roster-smb/
  python3 scripts/build-edition.py --all --verify emit each edition to a temporary folder and validate it; keep nothing

Generation is one-way. dist/ is git-ignored and never hand-edited. A fragment at
editions/<edition>/context/<department>/<skill>.md is inserted immediately before the skill's "## Never" section.
A fragment for a skill that does not exist fails the build.
"""
import glob, os, re, shutil, subprocess, sys, tempfile, tomllib
from _common import ROOT, path, finish

args = sys.argv[1:]
verify = "--verify" in args
names = [a for a in args if not a.startswith("--")]
if "--all" in args:
    names = sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(path("editions", "*", "edition.toml")))
if not names:
    print(__doc__)
    sys.exit(2)
problems = []
COPY = ["plugins", "catalogue", "data", "profiles", "templates", "sources", "scripts", "tests", "docs",
        ".claude", ".claude-plugin", ".agents", "LICENSE", "LICENSE-CODE", "NOTICE.md", "CITATION.cff", "AGENTS.md", "README.md", "AUTHORS.md", "CONTRIBUTING.md"]
for name in names:
    cfg_path = path("editions", name, "edition.toml")
    if not os.path.exists(cfg_path):
        problems.append(f"no edition config at editions/{name}/edition.toml")
        continue
    cfg = tomllib.load(open(cfg_path, "rb"))["edition"]
    target_root = tempfile.mkdtemp() if verify else path("dist")
    target = os.path.join(target_root, f"dynamics-365-ce-roster-{name}")
    shutil.rmtree(target, ignore_errors=True)
    os.makedirs(target)
    for item in COPY:
        src = path(item)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(target, item), ignore=shutil.ignore_patterns("__pycache__"))
        elif os.path.exists(src):
            shutil.copy2(src, os.path.join(target, item))
    for d in cfg.get("exclude_departments", []):
        shutil.rmtree(os.path.join(target, "plugins", d), ignore_errors=True)
    spliced = 0
    for frag in sorted(glob.glob(path("editions", name, "context", "*", "*.md"))):
        dept, skill = frag.split(os.sep)[-2], os.path.splitext(os.path.basename(frag))[0]
        skill_file = os.path.join(target, "plugins", dept, "skills", skill, "SKILL.md")
        if not os.path.exists(skill_file):
            problems.append(f"{os.path.relpath(frag, ROOT)}: no skill {dept}:{skill} to extend")
            continue
        text = open(skill_file, encoding="utf-8").read()
        fragment = open(frag, encoding="utf-8").read().strip() + "\n\n"
        new, n = re.subn(r"^## Never\s*$", lambda m: fragment + m.group(0), text, count=1, flags=re.M)
        if n == 0:
            problems.append(f"{dept}:{skill}: no '## Never' section to splice before")
            continue
        open(skill_file, "w", encoding="utf-8").write(new)
        spliced += 1
    note = os.path.join(target, "EDITION.md")
    open(note, "w", encoding="utf-8").write(f"# {cfg['title']}\n\n{cfg['description']}\n\nEmitted from the core repository by "
                                            f"scripts/build-edition.py with {spliced} context fragments. Do not edit; change the core and re-emit.\n")
    if verify:
        r = subprocess.run([sys.executable, "scripts/validate-skills.py"], cwd=target, capture_output=True, text=True)
        if r.returncode != 0:
            problems.append(f"edition {name} fails skill validation:\n{r.stdout}")
        shutil.rmtree(target_root, ignore_errors=True)
        print(f"  {name}: verified ({spliced} fragments)")
    else:
        print(f"  {name}: emitted to {os.path.relpath(target, ROOT)} ({spliced} fragments)")
finish("editions", problems, len(names))
