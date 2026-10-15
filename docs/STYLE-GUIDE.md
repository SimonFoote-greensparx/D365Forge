# Style guide

How a skill in this repository is written. Robert Peledie reviews against this guide; `scripts/validate-skills.py`
checks the parts a script can check.

## Anatomy

```
---
name: <identical to the folder name>
description: <120-450 characters. What it does, then "Use when ..." with concrete situations. No colons.>
license: CC-BY-4.0
metadata:
  department: <department id>
  stages: <subset of Strategize, Initiate, Implement, Prepare, Operate>
  modules: <subset of Sales, Marketing, Customer Service, Field Service, All>
  status: <draft | reviewed | stable>
  authors: Simon Foote, Robert Peledie
---

# Title in sentence case

Why this matters on a CRM project, and where projects usually go wrong.

## When to use
## Questions to ask first
## Approach
## Outputs
## Scale notes
### SMB
### Enterprise
## Hand-offs
## Sources
## Never
```

`license` and `metadata.authors` are fixed for every skill. They carry the credit to the original creators with the
skill wherever it is copied, so never remove or change them; outside contributors are credited in the git history and
`AUTHORS.md`. See `NOTICE.md`.

Edition fragments from `editions/<edition>/context/` are spliced in immediately before `## Never`, so every skill must
end with that section.

## Voice

- Write as an experienced CRM practitioner advising a colleague: opinionated, specific, practical.
- A skill asks the two to five questions that decide the answer before it advises. Those questions are the ones usually
  skipped, and skipping them is why the usual answer is wrong.
- A skill says what it cannot determine. One that answers everything confidently is the failure this library is built against.
- Paragraphs of two to five sentences. Bullets only for genuinely enumerable items. Bold sparingly; no emojis.

## Accuracy

- Durable judgement over version-specific detail. Dynamics 365 changes monthly; point to Microsoft Learn through
  `references/sources.md` rather than asserting how a feature currently behaves.
- Never invent statistics, prices, licence names or limits.
- Licensing questions end with the Microsoft licensing guide or a partner. Legal and data-protection questions end with
  the organisation's DPO or legal adviser.
- Use Microsoft's product and feature names exactly, for example Dynamics 365 Contact Center, Customer Insights -
  Journeys, Copilot Studio, server-side synchronization and the Power Platform admin center.

## Spelling

UK English by exact word form: organisation, customise, prioritise, optimise, analyse, behaviour, catalogue,
modelling, centre, licence (noun), programme (for projects), judgement. Microsoft product names keep Microsoft's spelling.
`python3 scripts/check-uk-english.py --fix` rewrites what it finds.

## People

Anything touching people (role mapping, training, adoption) uses declared skills and availability only. Skills never
assess performance, rank individuals or use personal characteristics.

## Reviewer-class skills

Each finding is classified as blocking or advisory, names the standard or risk behind it, and gives the specific fix.
Blocking findings are not overruled by the department under review; disagreement escalates to the executive sponsor or
steering committee.

## Cross-references

Refer to other skills as `department:skill` in backticks. `scripts/check-skill-refs.py` fails on any reference that does
not resolve.

## Trigger tests

Every skill has a block in `tests/triggers/<department>.toml` with at least three realistic prompts that should load it
and at least one near miss naming the skill that should catch it instead.
