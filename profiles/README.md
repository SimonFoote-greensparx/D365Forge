# Organisation profiles

An organisation describes itself once, in YAML, so the `project-tailoring` department can produce a tailored pack.

| File | Purpose |
|---|---|
| `schema.json` | The JSON Schema every profile is validated against. |
| `samples/smb-sample.yaml` | A fictional 85-person services firm implementing Sales, Customer Service and Field Service with a partner. |
| `samples/enterprise-sample.yaml` | A fictional 4,200-person group consolidating three legacy CRMs across all four modules. |

**Real profiles never belong here.** Copy a sample into `input/` (git-ignored), edit it there, and point the agent at it.
Use aliases ("Analyst A") instead of names if you prefer; set `preferences.use_aliases: true`.

## Sections

| Section | What to describe |
|---|---|
| `organisation` | Name or alias, sector, staff, countries, legal entities, regulatory context. |
| `goals` | Outcomes, success measures, target go-live (YYYY-MM), budget band. |
| `modules` | For Sales, Marketing, Customer Service and Field Service: in scope, users, and module extras (contacts, channels, technicians). |
| `estate` | Current CRM, legacy systems, ERP, email, telephony, data sources, integrations, licences, environments. |
| `team` | Each person: alias, optional name, current role, availability, and declared skills from `data/skills-vocabulary.toml` with a level (awareness, working, advanced, expert). |
| `constraints` | Partner scope, compliance, change freezes, known risks. |
| `preferences` | Aliases, edition (auto, smb, enterprise), output formats. |

Validate a profile with `python3 scripts/check-profiles.py` (samples) or ask the agent to run `project-tailoring:profile-intake`.
