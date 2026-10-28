#!/usr/bin/env python3
"""No third-party licence text or copyright notices have found their way into content. All prose here is original."""
import glob, re
from _common import ROOT, path, finish

PATTERNS = [r"Licensed under the Apache License", r"GNU (Lesser )?General Public License", r"All rights reserved",
            r"Copyright \(c\) (?!20\d\d Simon Foote, Robert Peledie and the D365Forge contributors)", r"©\s*(Microsoft|\d{4})",
            r"Creative Commons Attribution-ShareAlike", r"Reproduced (with|by) (kind )?permission"]
rx = re.compile("|".join(PATTERNS), re.I)
files = [f for f in glob.glob(path("**", "*.*"), recursive=True)
         if f.endswith((".md", ".toml", ".yaml", ".json", ".html"))
         and "/dist/" not in f and not f.endswith("/LICENSE")]
problems = []
for f in files:
    for i, line in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
        if rx.search(line):
            problems.append(f"{f.replace(ROOT + '/', '')}:{i}: {line.strip()[:100]}")
finish("provenance", problems, len(files))
