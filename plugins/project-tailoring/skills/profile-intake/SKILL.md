---
name: profile-intake
description: Builds or validates the organisation profile that drives a tailored D365Forge pack, checking a YAML file against the schema or interviewing the user, and asks only for what is missing while defaulting to aliases for people. Use when tailoring starts, when a profile fails validation or when someone wants to describe their organisation.
license: CC-BY-4.0
metadata:
  department: project-tailoring
  stages: Strategize, Initiate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Profile intake

Everything the tailoring department produces depends on the profile: the edition, the role mapping, the skills gaps and the twelve documents. A thin or wrong profile produces confident-looking documents built on guesses, and those guesses get copied forward into plans and contracts.

Intake usually goes wrong in one of two ways. Either it asks too much, and a long questionnaire is abandoned halfway, or it collects more about team members than the pack needs. This skill keeps the intake short, asks in the order that decides the most, and stays minimal about people: aliases by default, declared skills and availability only.

## When to use

- A user supplies a profile file and wants it checked before tailoring.
- A user wants a tailored pack but has no profile, so the facts need gathering in conversation.
- A profile has failed validation and the user needs to know what to fix.
- A profile needs completing before edition selection or role mapping can run.

Not this skill: `project-tailoring:edition-selection` to decide SMB or Enterprise once the profile is ready, `project-tailoring:role-mapping` to propose who holds each role, `project-tailoring:pack-refresh` to re-run an existing pack after the profile changes.

## Questions to ask first

1. Is there a profile file already, or does this start from conversation? It decides between validating and interviewing.
2. Which modules are in scope, with roughly how many users each? These facts decide the edition and most of the pack.
3. Who is on the team, with which declared skills, levels and availability? Role mapping cannot start without them.
4. Should people appear by alias or by name? Aliases are the default and suit packs that circulate widely.
5. What is already fixed (target go-live, partner, change freezes, compliance obligations)? Fixed constraints shape the plan more than preferences do.

## Approach

When a file is supplied, validate first and ask second. Check it against the profile schema and report each error in plain language with its path, for example that a level under team skills must be awareness, working, advanced or expert, or that a skill id is not in the skills vocabulary. Then run the consistency checks a schema cannot express:

- a module in scope with no user count, or Field Service in scope without a technician count;
- a target go-live that falls inside a declared change freeze;
- integrations whose systems do not appear anywhere else in the estate;
- a team where nobody declares any Dynamics 365 or Power Platform skill;
- a person with no skills listed, or with an availability that looks implausible for their declared role;
- legal entities missing when several countries are listed, since edition selection needs it.

Marketing in scope with UK GDPR or PECR in the regulatory context is not an error, but note it so the consent review is planned early.

When there is no file, interview. Ask three to five questions at a time, in this order: modules and users; team, skills and availability; estate and integrations; constraints; goals and success measures. Each batch decides more of the pack than the next, so a user who stops early still gets a usable profile. Accept "not known yet" and record it as an open point; open points become visible placeholders in the pack and entries in the raid-log.

Ask only for what is missing or inconsistent, and never re-ask a fact that is already present and valid. When a value is valid but surprising, such as a large user count with a two-person team, ask once and record the answer.

Treat people data with care. Set use_aliases to true unless the user explicitly chooses names. For each person collect only the alias, current role, whether they are internal, availability percentage and skills with levels, as declared by the person or the project lead. Explain the four levels in a line each so declarations are consistent. Do not infer skills or levels from job titles, and never ask for performance ratings, age, health or any other personal characteristic. If the organisation wants real names in the pack, suggest it checks that use with its DPO.

In a clone of the repository, save the profile to input/, which is git-ignored, after confirming the ignore rule is in place; in Copilot Cowork or another assistant without the repository, save it to the user's own storage, such as a private OneDrive folder. Never write a real profile into profiles/samples/ or anywhere else in the repository. Finish with a short summary: what was captured, what is still open, which assumptions were made and whether the profile is ready for edition selection.

## Outputs

- A validated profile file in input/ or the user's own storage, never in the repository.
- A validation report listing schema errors, consistency warnings and open points.
- An intake summary for the project lead, with assumptions and unknowns that will appear as placeholders in the `project-charter` and as entries in the `raid-log`.

## Scale notes

### SMB

Intake for a small organisation is usually one sitting with the customer's project lead and the partner consultant. The team list is short, so take care over availability: small teams over-commit, and a managing director at a tenth of their time is a real constraint. Do not skip the estate section, because even one accounting integration shapes the plan.

### Enterprise

Several people supply parts of the profile (workstream leads, IT, procurement), so prefer an edited file over a long conversation and validate it each time it changes. Name a profile owner. Multiple countries and regulatory contexts need checking against legal entities, and later changes flow through a pack refresh rather than an edited pack.

## Hand-offs

A ready profile goes to `project-tailoring:edition-selection`, then `project-tailoring:role-mapping`. Open points about scope or goals go to `programme-management:project-charter`. No reviewer sign-off is needed for the profile itself.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the profile schema (`references/profile-schema.json`), the skills vocabulary (`references/skills-vocabulary.json`) and two fictional sample profiles (`references/sample-smb-profile.yaml`, `references/sample-enterprise-profile.yaml`). In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`, with the TOML data files bundled as JSON.

## Never

- Ask for or record performance ratings, personal characteristics or anything about people beyond role, internal status, declared skills and availability.
- Write a real organisation profile into the repository, including profiles/samples/.
- Fill a missing value with a guess without marking it as an assumption.
- Use real names unless the user has explicitly turned aliases off.
- Re-ask questions the profile already answers validly.
