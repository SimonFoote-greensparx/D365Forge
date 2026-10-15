#!/usr/bin/env python3
"""UK English by exact word form in prose (D3). Microsoft product names keep Microsoft's spelling.

Run with --fix to rewrite the flagged words in place. URLs, inline code and code blocks are left alone.
"""
import glob, re, sys
from _common import ROOT, path, finish

US_TO_UK = {
    "organization": "organisation", "organizations": "organisations", "organizational": "organisational",
    "organize": "organise", "organized": "organised", "organizing": "organising",
    "customize": "customise", "customized": "customised", "customizing": "customising",
    "customization": "customisation", "customizations": "customisations",
    "prioritize": "prioritise", "prioritized": "prioritised", "prioritizing": "prioritising", "prioritization": "prioritisation",
    "optimize": "optimise", "optimized": "optimised", "optimizing": "optimising", "optimization": "optimisation",
    "analyze": "analyse", "analyzed": "analysed", "analyzing": "analysing",
    "utilize": "utilise", "utilized": "utilised", "utilization": "utilisation",
    "standardize": "standardise", "standardized": "standardised", "standardization": "standardisation",
    "minimize": "minimise", "minimized": "minimised", "maximize": "maximise", "maximized": "maximised",
    "recognize": "recognise", "recognized": "recognised", "summarize": "summarise", "summarized": "summarised",
    "authorize": "authorise", "authorized": "authorised", "authorization": "authorisation",
    "synchronize": "synchronise", "synchronized": "synchronised", "synchronization": "synchronisation",
    "normalize": "normalise", "normalized": "normalised", "visualize": "visualise", "visualization": "visualisation",
    "behavior": "behaviour", "behaviors": "behaviours", "favor": "favour", "favorite": "favourite",
    "labor": "labour", "honor": "honour", "catalog": "catalogue", "catalogs": "catalogues",
    "modeling": "modelling", "modeled": "modelled", "labeled": "labelled", "labeling": "labelling",
    "canceled": "cancelled", "canceling": "cancelling", "traveled": "travelled", "fulfill": "fulfil",
    "enrollment": "enrolment", "judgment": "judgement", "center": "centre", "centers": "centres",
    "defense": "defence", "offense": "offence",
}
# Proper nouns that keep Microsoft's (or another publisher's) spelling.
ALLOW = [
    "Contact Center", "admin center", "Admin Center", "Center of Excellence", "Microsoft 365 admin center",
    "Resource Scheduling Optimization", "Customer Service admin center", "Power Platform admin center",
    "Copilot Service admin center", "Search Engine Optimization", "Data Center", "Microsoft Defender",
    "Experience Center", "Trust Center", "Customize", "server-side synchronization", "Server-side synchronization",
    "Resource Scheduling Optimization (RSO)", "Contact Center", "Sales Accelerator", "Message center", "Message Center", "Security Center",
]
FILES = (glob.glob(path("plugins", "*", "skills", "*", "SKILL.md")) + glob.glob(path("plugins", "*", "README.md"))
         + glob.glob(path("templates", "*.md")) + glob.glob(path("docs", "*.md")) + glob.glob(path("editions", "**", "*.md"), recursive=True)
         + glob.glob(path(".claude", "agents", "*.md")) + glob.glob(path("cowork", "*.md")) + glob.glob(path("*.md")) + glob.glob(path("data", "*.toml")))
STRIP = re.compile(r"```.*?```|`[^`\n]*`|https?://\S+|\]\([^)]*\)", re.S)
WORD = re.compile(r"\b(" + "|".join(sorted(US_TO_UK, key=len, reverse=True)) + r")\b", re.I)

fix = "--fix" in sys.argv[1:]
problems = []
for f in FILES:
    text = open(f, encoding="utf-8").read()
    masked = STRIP.sub(lambda m: " " * len(m.group(0)), text)
    for allowed in ALLOW:
        masked = re.sub(re.escape(allowed), lambda m: " " * len(m.group(0)), masked)
    hits = list(WORD.finditer(masked))
    if not hits:
        continue
    if fix:
        out, last = [], 0
        for h in hits:
            us = h.group(0)
            uk = US_TO_UK[us.lower()]
            uk = uk.capitalize() if us[0].isupper() else uk
            out.append(text[last:h.start()]); out.append(uk); last = h.end()
        out.append(text[last:])
        open(f, "w", encoding="utf-8").write("".join(out))
        continue
    for h in hits:
        line = text.count("\n", 0, h.start()) + 1
        problems.append(f"{f.replace(ROOT + '/', '')}:{line}: {h.group(0)!r} -> {US_TO_UK[h.group(0).lower()]!r}")
finish("UK English", problems, len(FILES))
