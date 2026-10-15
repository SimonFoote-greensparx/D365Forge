#!/usr/bin/env python3
"""Sample profiles validate against profiles/schema.json, and their declared skills exist in the vocabulary.

Needs PyYAML (pip install pyyaml). Implements the subset of JSON Schema the profile schema uses, so no other dependency.
"""
import glob, json, re, sys
from _common import path, load_toml, finish

try:
    import yaml
except ImportError:
    print("profiles: PyYAML not installed; skipped (pip install pyyaml)")
    sys.exit(0)

schema = json.load(open(path("profiles", "schema.json")))
vocab = {s["id"] for s in load_toml("data/skills-vocabulary.toml")["skill"]}
TYPES = {"object": dict, "array": list, "string": str, "integer": int, "boolean": bool}


def validate(value, sch, where, problems):
    t = sch.get("type")
    if t and not (isinstance(value, TYPES[t]) and not (t == "integer" and isinstance(value, bool))):
        problems.append(f"{where}: expected {t}"); return
    if "enum" in sch and value not in sch["enum"]:
        problems.append(f"{where}: {value!r} not in {sch['enum']}")
    if "pattern" in sch and isinstance(value, str) and not re.search(sch["pattern"], value):
        problems.append(f"{where}: {value!r} does not match {sch['pattern']}")
    if "minimum" in sch and isinstance(value, int) and value < sch["minimum"]:
        problems.append(f"{where}: below minimum {sch['minimum']}")
    if "maximum" in sch and isinstance(value, int) and value > sch["maximum"]:
        problems.append(f"{where}: above maximum {sch['maximum']}")
    if t == "object":
        for req in sch.get("required", []):
            if req not in value:
                problems.append(f"{where}: missing {req}")
        props = sch.get("properties", {})
        for k, v in value.items():
            if k in props:
                validate(v, props[k], f"{where}.{k}", problems)
            elif sch.get("additionalProperties") is False:
                problems.append(f"{where}: unexpected key {k!r}")
    if t == "array":
        if len(value) < sch.get("minItems", 0):
            problems.append(f"{where}: needs at least {sch['minItems']} items")
        for i, item in enumerate(value):
            validate(item, sch.get("items", {}), f"{where}[{i}]", problems)


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
