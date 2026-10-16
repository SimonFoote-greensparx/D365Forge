#!/usr/bin/env python3
"""The website's profile builder produces profiles that match profiles/schema.json.

Runs the builder's own functions (docs/assets/profile-builder.js) in Node.js against a set of form states, including
the one that exposed the nested-integrations bug, then parses the YAML they produce with PyYAML and validates it with
the same checker as the sample profiles. Also checks that the builder's in-browser checks flag what they should.
Needs Node.js and PyYAML; skipped with a note if either is missing.
"""
import json, os, re, shutil, subprocess, sys
from _common import path, load_toml, finish, validate_schema

try:
    import yaml
except ImportError:
    print("profile builder: PyYAML not installed; skipped (pip install pyyaml)")
    sys.exit(0)
node = shutil.which("node")
if not node:
    print("profile builder: Node.js not installed; skipped")
    sys.exit(0)

schema = json.load(open(path("profiles", "schema.json"), encoding="utf-8"))
vocab = [s["id"] for s in load_toml("data/skills-vocabulary.toml")["skill"]]


def state(**over):
    base = {
        "org": {"name": "Org A", "sector": "", "staff": "100", "entities": "1", "countries": "United Kingdom", "regulatory": "UK GDPR, PECR"},
        "goals": {"outcomes": "One view of every customer", "measures": "", "goLive": "2027-06", "budget": "not-shared"},
        "modules": {"sales": {"on": True, "users": "20"}, "marketing": {"on": False, "users": "0", "contacts": ""},
                    "customer_service": {"on": False, "users": "0", "channels": []},
                    "field_service": {"on": False, "users": "0", "technicians": "0"}},
        "estate": {"crm": "", "erp": "", "telephony": "", "email": "Microsoft 365", "m365": True, "dataSources": "",
                   "licences": "", "environments": "development, test, production", "legacy": [], "integrations": []},
        "team": [{"alias": "Analyst A", "name": "", "role": "Business analyst", "availability": "60", "internal": True,
                  "skills": [{"skill": vocab[0], "level": "working"}]}],
        "constraints": {"partner": True, "partnerScope": "build, data migration", "compliance": "", "freezes": "", "risks": "Key users stretched"},
        "prefs": {"aliases": True, "edition": "auto", "formats": ["docx", "xlsx"]},
    }
    for key, value in over.items():
        base[key] = {**base[key], **value} if isinstance(value, dict) else value
    return base


CASES = {
    # The profile that failed: one integration with only a system name, a full name as an alias, a typo in the
    # organisation name, an ERP named differently from the integration, no partner and no known risks.
    "reported": state(
        org={"name": "WOrkwell", "regulatory": "UK GDPR"},
        modules={"sales": {"on": True, "users": "15"}, "marketing": {"on": True, "users": "3", "contacts": ""},
                 "customer_service": {"on": False, "users": "0", "channels": []}, "field_service": {"on": False, "users": "0", "technicians": "0"}},
        estate={"erp": "Fin Ops", "integrations": [{"system": "Finance", "direction": "", "frequency": "", "purpose": ""}]},
        team=[{"alias": "Simon Foote", "name": "", "role": "CRM AI Solutions Contractor", "availability": "40", "internal": False,
               "skills": [{"skill": vocab[0], "level": "advanced"}, {"skill": vocab[1], "level": "expert"}]}],
        constraints={"partner": False, "partnerScope": "", "risks": ""}),
    # Every field the builder offers, names instead of aliases, and characters YAML treats specially.
    "complete": state(
        org={"name": "Café & Co: \"North\" #1", "sector": "Housing", "entities": "2", "countries": "United Kingdom, Ireland"},
        goals={"outcomes": "Faster case handling\nOne customer record", "measures": "First-contact resolution 75%", "goLive": "2027-04", "budget": "250k-1m"},
        modules={"sales": {"on": True, "users": "40"}, "marketing": {"on": True, "users": "5", "contacts": "120000"},
                 "customer_service": {"on": True, "users": "60", "channels": ["email", "phone", "web-portal"]},
                 "field_service": {"on": True, "users": "8", "technicians": "35"}},
        estate={"crm": "Dynamics CRM 2016", "erp": "Dynamics 365 Finance", "telephony": "Teams Phone", "m365": True,
                "dataSources": "Spreadsheets, Web forms", "licences": "Dynamics 365 Sales Enterprise", "environments": "dev, test, uat, prod",
                "legacy": [{"name": "Old Case System", "purpose": "Cases", "records": "250000", "retire": True}],
                "integrations": [{"system": "Dynamics 365 Finance", "direction": "both", "frequency": "near-real-time", "purpose": "Customers and invoices"},
                                 {"system": "Teams Phone", "direction": "inbound", "frequency": "real-time", "purpose": "Screen pop"}]},
        team=[{"alias": "Analyst A", "name": "Alex Example", "role": "BA", "availability": "100", "internal": True,
               "skills": [{"skill": vocab[0], "level": "expert"}]},
              {"alias": "Developer B", "name": "Sam Sample", "role": "Developer", "availability": "150", "internal": False,
               "skills": [{"skill": vocab[2], "level": "working"}]}],
        constraints={"partner": True, "partnerScope": "build", "compliance": "ISO 27001", "freezes": "December", "risks": "Data quality\nKey users"},
        prefs={"aliases": False, "edition": "enterprise", "formats": ["docx", "xlsx", "md"]}),
    # Nothing filled in that matters: the builder must say what is missing rather than invent it.
    "empty": state(goals={"outcomes": "", "measures": "", "goLive": "", "budget": "not-shared"},
                   modules={"sales": {"on": False, "users": "0"}}, team=[], prefs={"aliases": True, "edition": "auto", "formats": []}),
}

harness = """
const pb = require(process.argv[1]);
const cases = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const out = {};
for (const [name, c] of Object.entries(cases.states)) {
  const profile = pb.buildProfile(c);
  out[name] = { yaml: pb.toYaml(profile), review: pb.review(profile, cases.vocab), errors: pb.validate(profile, cases.schema) };
}
process.stdout.write(JSON.stringify(out));
"""
res = subprocess.run([node, "-e", harness, path("docs", "assets", "profile-builder.js")],
                     input=json.dumps({"states": CASES, "vocab": vocab, "schema": schema}), capture_output=True, text=True, timeout=60)
problems = []
if res.returncode != 0:
    problems.append(f"the builder script failed in Node.js: {res.stderr.strip()[:400]}")
    finish("profile builder", problems, 0)
out = json.loads(res.stdout)

for name in ("reported", "complete"):
    r = out[name]
    if re.search(r"^\s*-\s+-\s", r["yaml"], re.M):
        problems.append(f"{name}: the YAML contains a list inside a list")
    data = yaml.safe_load(r["yaml"])
    schema_problems = []
    validate_schema(data, schema, name, schema_problems)
    problems += schema_problems
    if r["errors"]:
        problems.append(f"{name}: the builder's own check reports {r['errors']} for a valid profile")
    if r["review"]["problems"]:
        problems.append(f"{name}: the builder blocks a usable profile: {r['review']['problems']}")

rep = yaml.safe_load(out["reported"]["yaml"])
if rep["estate"]["integrations"] != [{"system": "Finance"}]:
    problems.append(f"reported: integrations came out as {rep['estate']['integrations']!r}")
if "name" in rep["team"][0]:
    problems.append("reported: a name was written although aliases are on")
checks = " ".join(out["reported"]["review"]["checks"])
for expected in ("looks like a person's name", "spelling of \"WOrkwell\"", "does not match any system", "no direction, frequency or purpose",
                 "No known risks"):
    if expected not in checks:
        problems.append(f"reported: the builder did not warn about: {expected}")

full = yaml.safe_load(out["complete"]["yaml"])
if full["organisation"]["name"] != CASES["complete"]["org"]["name"]:
    problems.append("complete: special characters in the organisation name did not survive the YAML")
if [t.get("name") for t in full["team"]] != ["Alex Example", "Sam Sample"]:
    problems.append("complete: names were not written although aliases are off")
if full["team"][1]["availability_percent"] != 100:
    problems.append("complete: availability above 100% was not capped")
if full["estate"]["integrations"][0] != {"system": "Dynamics 365 Finance", "direction": "both", "frequency": "near-real-time", "purpose": "Customers and invoices"}:
    problems.append("complete: an integration lost its direction, frequency or purpose")
if out["complete"]["review"]["checks"]:
    problems.append(f"complete: unexpected warnings {out['complete']['review']['checks']}")

empty = out["empty"]
for expected in ("outcome", "person", "module", "output format"):
    if not any(expected in p for p in empty["review"]["problems"]):
        problems.append(f"empty: the builder did not flag a missing {expected}")
if not empty["errors"]:
    problems.append("empty: the builder's schema check passed a profile with no team and no outcomes")

finish("profile builder", problems, len(CASES))
