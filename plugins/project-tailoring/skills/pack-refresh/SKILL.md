---
name: pack-refresh
description: Re-runs the tailored pack after the organisation profile changes, re-checking edition, roles and gaps only where the change reaches, keeping earlier versions and reporting what moved. Use when scope, team, dates or estate change, when people join or leave the project, or before a stage gate that needs an up-to-date pack.
license: CC-BY-4.0
metadata:
  department: project-tailoring
  stages: Initiate, Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Pack refresh

Profiles go stale quickly: a module enters scope, the go-live date moves, two people leave, an integration is added. A pack that is never refreshed drifts away from the project, while a pack regenerated blindly overwrites edits the team has made and reshuffles roles people have already agreed to.

The refresh is therefore selective and open about what it did. It re-runs only what the change reaches, keeps the previous version, and tells the project lead in plain terms what moved and why.

## When to use

- The profile has changed: scope, users, team, availability, dates, estate or constraints.
- People have joined or left the project, or changed their declared availability.
- A stage gate or steering meeting needs a pack that matches the current position.
- Someone asks what difference a proposed change to the profile would make.

Not this skill: `project-tailoring:profile-intake` to update or validate the profile itself, `project-tailoring:document-pack` to produce a first pack, `design-authority:change-impact-assessment` for the solution impact of a scope change.

## Questions to ask first

1. Where is the previous pack and its manifest? Without the earlier snapshot there is nothing to compare, so produce a first pack instead.
2. What changed, and has the new profile passed validation? A refresh on an invalid profile spreads errors into twelve documents.
3. Which role assignments has the project lead already confirmed? Confirmed lines stay unless the change forces a review.
4. Have any generated documents been edited by hand since? Edited documents must never be overwritten.
5. Is the refresh for a stage gate? If so, the report leads with anything that affects the go-live decision.

## Approach

1. Compare the profiles. Diff the snapshot in the previous manifest against the current profile, key by key, and sort the changes into three groups: edition signals (modules, users, integrations, countries and legal entities, team size), people (members, declared skills, availability, internal status) and content only (goals, estate detail, constraints, dates).
2. Re-run only what the change reaches. Edition signals trigger edition selection, and if the recommendation changes, everything downstream runs. People changes trigger role mapping and the skills gap analysis. Content-only changes regenerate just the templates whose declared source keys changed.
3. Protect confirmed roles. Keep every confirmed assignment unless the person has left, their declared availability no longer covers the allocation, their declared skills changed, or a new combination rule now applies. In those cases mark the line for review with the reason. Never reassign a confirmed role silently.
4. Protect hand edits. Write the refreshed pack to a new dated folder in the same private output location and keep the previous one untouched. Where a regenerated section would replace text that was edited by hand, list it so the document owner can merge.
5. Report what moved, summary first. Cover the edition (unchanged or changed, with the signals that moved), roles newly uncovered, newly covered, over-allocated or in conflict, gaps opened or closed, each document with the sections that changed, placeholders added or resolved, and suggested entries for the raid-log. Date changes should call out collisions with change freezes and effects on the cutover checklist.
6. Close the loop. Ask the project lead to confirm any role lines marked for review, then update the manifest so the next refresh compares against the confirmed state.

The department's people rules apply unchanged: declared skills and availability only, aliases by default, no ranking or performance commentary, and nothing written into the repository. A person leaving is reported as a role that needs cover, never with a reason or comment about them.

## Outputs

- Refreshed pack in a new dated folder in the private output location, with the previous version kept.
- Change report: summary, edition, roles, gaps, documents and placeholders.
- Updated manifest, new risks and assumptions for the `raid-log`, and date effects on the `delivery-plan` and `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Refresh at each phase change or when someone joins or leaves; changes are usually small and one person reads the report. Keep the previous version even so, because small teams often edit documents directly and lose track of what the generator wrote.

### Enterprise

Tie refreshes to change control and run one before every stage gate. Send the change report to the PMO and workstream leads, who confirm role changes in their area. Scope changes that alter the design go to design authority before the refreshed blueprint is accepted.

## Hand-offs

Role lines marked for review go to `project-tailoring:role-mapping`, and new gaps to `project-tailoring:skills-gap-analysis`. Date and risk changes go to `programme-management:delivery-plan` and `programme-management:raid-log`, scope changes with design impact to `design-authority:change-impact-assessment`, and stage gate refreshes to `programme-management:go-no-go`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the role catalogue (`references/role-catalogue.json`) and the role combination rules (`references/role-combinations.json`). In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`, with the TOML data files bundled as JSON.

## Never

- Overwrite a previous pack or a hand-edited document without keeping the earlier version.
- Reassign a role the project lead confirmed without flagging it and asking.
- Write profile data, manifests or change reports into the repository.
- Report a change as having no impact without re-running the steps it reaches.
- Explain why a person left or comment on them; report only the role that needs cover.
