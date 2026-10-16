#!/usr/bin/env python3
"""Sample profiles validate against profiles/schema.json, and their declared skills exist in the vocabulary.

Needs PyYAML (pip install pyyaml). Implements the subset of JSON Schema the profile schema uses, so no other dependency.
"""
import glob, json, re, sys
from _common import path, load_toml, finish, validate_schema as validate

try:
    import yaml
except ImportError:
    print("profiles: PyYAML not installed; skipped (pip install pyyaml)")
    sys.exit(0)

schema = json.load(open(path("profiles", "schema.json")))
vocab = {s["id"] for s in load_toml("data/skills-vocabulary.toml")["skill"]}
problems = []
samples = sorted(glob.glob(path("profiles", "samples", "*.yaml")))
for f in samples:
    name = f.split("/")[-1]
    data = yaml.safe_load(open(f, encoding="utf-8"))
    validate(data, schema, name, problems)
    for i, person in enumerate(data.get("team", [])):
        for s in person.get("skills", []):
            if s.get("skill") not in vocab:
                problems.append(f"{name}: team[{i}] declares unknown skill {s.get('skill')!r}")
finish("profiles", problems, len(samples))
