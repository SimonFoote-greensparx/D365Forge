# Data

Shared reference data the skills and the tailoring engine read. Owned by Robert Peledie (content) and Simon Foote
(format). Everything here is generic: no organisation's data belongs in this folder.

| File | What it holds | Used by |
|---|---|---|
| `role-catalogue.toml` | Every project role: title, department, the module that makes it relevant, which editions expect it as a separate seat, SMB and Enterprise descriptions, required and desirable skills. | `project-tailoring:role-mapping`, `project-tailoring:skills-gap-analysis`, templates (`{{roles.<id>}}`) |
| `role-combinations.toml` | Pairs of roles one person should not hold (`unsafe`) or may hold with a stated reason (`caution`). | `project-tailoring:role-mapping` |
| `skills-vocabulary.toml` | The skill ids people declare in an organisation profile, so declared skills and role requirements match. | Profiles, the role catalogue, `scripts/check-profiles.py` |

`scripts/check-data.py` verifies that every role's skills are in the vocabulary, every combination names real roles, and
every template placeholder names a real role.

## Placeholders for more data

Planned additions, each to be specified by Robert Peledie before it is built:

- `effort-benchmarks.toml`: indicative effort ranges by module and edition, for planning conversations only.
- `risk-library.toml`: typical CRM risks by module, to pre-populate the RAID log.
- `release-calendar.toml`: the organisation's own review rhythm against the AI at Work roadmap.
