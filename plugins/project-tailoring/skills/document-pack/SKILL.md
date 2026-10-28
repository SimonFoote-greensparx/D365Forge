---
name: document-pack
description: Fills the twelve project templates from the organisation profile, the edition decision and the confirmed role mapping, and writes Word and Excel drafts to the output folder in the user workspace, never into the repository. Use when a team wants its tailored charter, RACI, plans, logs and checklists produced as a first draft pack.
license: CC-BY-4.0
metadata:
  department: project-tailoring
  stages: Strategize, Initiate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Document pack

The pack turns the profile into twelve working drafts that the project's owners then finish. Its value is consistency: the same scope, dates, roles and assumptions appear in the charter, the plan, the RACI and the cutover checklist, instead of twelve documents written by different people at different times.

It goes wrong through false precision and leaked data. A generated document that invents a go-live date, a user count or a licence name looks authoritative and gets copied forward. A pack that writes team details back into the repository publishes personal data. So gaps stay visible, and everything is written to the user's own storage: output/ (git-ignored) in a clone of the repository, or the user's own OneDrive folder in Copilot Cowork.

## When to use

- A profile is validated, the edition is decided and the role mapping has a status on every line.
- The project wants its first set of tailored documents.
- Someone asks for one or more of the templates filled from their profile.

Not this skill: `project-tailoring:pack-refresh` to regenerate after the profile changes, or the owning skills, such as `programme-management:project-charter` and `solution-architecture:solution-blueprint`, to develop one document in depth.

## Questions to ask first

1. Is the profile validated and the edition decided? The pack is only as good as both.
2. Is the role mapping confirmed by the project lead, or still a proposal? Unconfirmed lines must show as proposed in every document.
3. Names or aliases? Follow the profile preference, which defaults to aliases.
4. Who will receive the pack? Wide circulation means declared skill levels stay in a restricted file.
5. Where will the pack be written? In a clone of the repository it must be output/, and output/ must be git-ignored; in Copilot Cowork or another assistant without the repository, it is the user's own storage (for example their Cowork folder in OneDrive), never a shared or public location. If neither is true, stop and fix that before writing anything.

## Approach

Check the preconditions before writing: a profile that passes validation, an edition with its reasons, a role mapping with a status on every line, and a private output location (a git-ignored output/ folder, or the user's own storage outside a repository). If any is missing, hand back to the skill that owns it rather than filling the gap.

Each template declares its id, its format (docx or xlsx), its owning skill and the profile keys it is tailored from. Treat that front matter as the authority and fill every placeholder from those keys, the edition and the role mapping. In outline:

- `project-charter`, `delivery-plan` and `raid-log` draw on organisation, goals, modules, constraints and the edition reasons; the raid-log also takes combination cautions, gaps and every open assumption.
- `raci-matrix` and `resource-and-skills-gap-plan` draw on the role mapping and the skills gap analysis.
- `solution-blueprint`, `environment-and-alm-strategy` and `integration-inventory` draw on modules, the estate and declared licences and environments.
- `data-migration-mapping` starts from the current CRM, legacy systems and data sources, at source level only.
- `test-strategy-and-uat-scripts`, `training-and-communications-plan` and `cutover-and-hypercare-checklist` draw on modules and users, integrations, change freezes, the go-live date and support roles.

Leave gaps visible. Where the profile is silent, write a clear To confirm placeholder naming the missing fact and the role that owns it, and add it to the raid-log. Never invent dates, numbers, costs or licence names; licences appear only as the profile declares them, and any licensing point in a document carries the note to confirm with the Microsoft licensing guide or your partner.

Shape by edition. Keep the template guidance marked for the chosen edition and drop the rest. SMB documents stay short with one owner across several; Enterprise documents add a section per module workstream, design authority checkpoints and SIT.

Write only to that private output location, in the formats the profile's output preference allows (Word, Excel, Markdown), following each template's declared format. Never write into templates/, profiles/, plugins/ or any other tracked or shared folder. Save a manifest alongside the documents with the generation date, a copy of the profile used, the edition and the mapping status, so a refresh can compare later. Mark every document as a generated first draft, naming its owning role by alias. Carry each template's closing Credit line into the document as a short closing line (a footer in Word, a note below the last table in Excel); tell the user it credits the template authors and may be kept or removed in their own documents.

People appear by alias unless the profile opts out. Declared skill levels appear only in the resource and skills-gap plan, which is marked for restricted circulation; every other document shows roles and aliases only.

## Outputs

- Twelve drafts in the private output location: `project-charter`, `raci-matrix`, `resource-and-skills-gap-plan`, `delivery-plan`, `raid-log`, `solution-blueprint`, `environment-and-alm-strategy`, `integration-inventory`, `data-migration-mapping`, `test-strategy-and-uat-scripts`, `training-and-communications-plan` and `cutover-and-hypercare-checklist`.
- A manifest recording the profile snapshot, edition, mapping status and generation date.
- A list of every To confirm placeholder, mirrored in the `raid-log`.

## Scale notes

### SMB

One person, usually the partner lead with the customer's project lead, can read the whole pack in a sitting, so keep each document tight. Do not drop the test strategy or the cutover checklist because they look heavy; shorten them instead. A single owner across several documents is fine if the RACI says so.

### Enterprise

Each document gets an owner from the confirmed mapping, and the pack becomes a baseline held under document control in the organisation's own document management, never in the repository. Generate per-workstream sections where the template allows, and expect the solution blueprint and environment strategy to go through design authority once developed.

## Hand-offs

Each draft goes to its owning skill: `programme-management:project-charter`, `programme-management:delivery-plan`, `programme-management:raid-log`, `solution-architecture:solution-blueprint`, `solution-architecture:environment-strategy`, `integration-and-data:integration-architecture`, `integration-and-data:data-mapping-and-cleansing`, `testing-quality:test-strategy`, `change-adoption:communications-plan` and `support-operations:cutover-plan`. The generated pack needs no reviewer sign-off, but the developed blueprint passes through `design-authority:design-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the twelve templates (`references/templates/`) and the role catalogue (`references/role-catalogue.json`) for role placeholders. In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`, with the TOML data files bundled as JSON.

## Never

- Write profile data, team details or generated documents into the repository.
- Invent dates, user numbers, costs or licence names to fill a template.
- Present proposed role assignments as confirmed.
- Use names when the profile asks for aliases.
- Put declared skill levels in any document other than the restricted resource and skills-gap plan.
