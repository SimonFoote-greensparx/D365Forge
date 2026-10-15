---
id: resource-and-skills-gap-plan
title: Resource and skills-gap plan
format: xlsx
owner: project-tailoring:skills-gap-analysis
tailored_from: organisation, team, constraints, edition, modules_in_scope, roles, team_table, gaps_table, generated_on
status: draft
---

# Resource and skills-gap plan

## How to use this template

The project manager ({{roles.project-manager}}) owns this workbook and completes it in Strategize with the sponsor and the partner lead ({{constraints.partner}}). It compares the roles a {{edition}} project for {{modules_in_scope}} needs with the skills and availability people have declared, then records how each gap will be closed. Revisit it at every stage gate, when someone's availability changes and before the partner contract is extended.

The generator fills the "Team supply" and "Skills gaps" sheets from the organisation profile; the example rows shown below are replaced by the computed tables. Everything else is for the project to complete.

> Guidance: Work only from skills and availability that people have declared themselves. This plan is not a performance review: do not rate, rank or compare individuals, and do not record personal characteristics. If a declared level looks optimistic, agree a short practical exercise or pairing arrangement with the person rather than overriding their declaration.

> SMB: Expect most gaps to be closed by the partner, with one or two internal people trained to take over administration and first-line support after go-live. Do not skip the administrator and support rows; they are what keeps the system healthy once the partner leaves.

> Enterprise only: Plan demand per workstream and per stage, include backfill for business staff seconded to the project, and agree a knowledge transfer plan for every partner-filled role.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Generated on | {{generated_on}} |
| Skill levels | awareness, working, advanced, expert (as declared by each person) |
| Closing options | train, pair with partner, hire, contract, partner-delivered, combine with another role |
| Data handling | Contains names and availability; store with restricted access and delete personal rows after project closure |

## Sheet: Role demand

| Role id | Role | Stages needed | Expected effort (to estimate) | Required skills | Proposed | Coverage status |
|---|---|---|---|---|---|---|
| project-manager | Project manager | All | Confirm with partner | project-management | {{roles.project-manager}} | Proposed |
| solution-architect | Solution architect | Initiate to Prepare | Heavier in Initiate | solution-architecture, dataverse-data-modelling | {{roles.solution-architect}} | Proposed |
| process-owner | Process owner | All | Regular workshops and UAT | process-ownership | {{roles.process-owner}} | Confirm release from day job |
| data-migration-lead | Data migration lead | Initiate to Operate | Peaks at mock migrations and cutover | data-migration, data-quality | {{roles.data-migration-lead}} | Gap |
| test-manager | Test manager | Initiate to Prepare | Peaks at SIT and UAT | testing | {{roles.test-manager}} | Gap |
| platform-administrator | Platform administrator | Initiate onwards | Continues after go-live | power-platform-administration | {{roles.platform-administrator}} | Proposed |
| trainer | Trainer | Implement to Operate | Peaks before go-live | training-delivery | {{roles.trainer}} | Proposed |
| support-lead | Support lead | Prepare onwards | Continues after go-live | service-management | {{roles.support-lead}} | Proposed |

> Guidance: Add module roles only for modules in scope: sales-consultant, journeys-consultant, customer-service-consultant, field-service-consultant. Express effort as a pattern (for example "two days a week in Implement") once estimated with the partner; do not copy figures from another project.

## Sheet: Team supply

| Alias | Name | Current role | Availability % (declared) | Declared skills and levels | Proposed project roles | Confirmed with person and line manager |
|---|---|---|---|---|---|---|
| sales-ops-01 | | Sales operations manager | From profile | sales-operations (advanced), process-mapping (working) | process-owner | |
| it-admin-01 | | IT systems administrator | From profile | entra-id (advanced), power-platform-administration (working) | platform-administrator | |
| svc-lead-01 | | Service desk team leader | From profile | service-management (advanced), knowledge-management (working) | support-lead, process-owner | |

> Guidance: The generator replaces the example rows above with {{team_table}}. Use aliases if the profile sets preferences.use_aliases to true.

## Sheet: Skills gaps

| Role | Required skill | Required level | Best declared level on team | Gap | Impact if not closed | Closing option | Owner | Close by |
|---|---|---|---|---|---|---|---|---|
| solution-architect | dataverse-data-modelling | advanced | working | One level | Data model rework after build starts | Pair with partner architect, then train | {{roles.project-manager}} | End of Initiate |
| data-migration-lead | data-migration | advanced | none declared | Not covered | Poor quality data at go-live | Partner-delivered with internal shadow | {{roles.project-manager}} | Start of Implement |
| test-manager | testing | working | awareness | One level | Weak UAT scripts and exit criteria | Train and pair | {{roles.project-manager}} | Before SIT |
| security-lead | security-design | advanced | working | One level | Over-permissive security roles | Partner review plus training | {{roles.project-manager}} | Before blueprint approval |
| platform-administrator | alm-and-devops | working | awareness | One level | Unmanaged changes reaching production | Train before first deployment | {{roles.platform-administrator}} | Mid Implement |

> Guidance: The generator replaces the example rows above with {{gaps_table}}. A gap in a role that continues after go-live (administrator, support lead, trainer) should usually be closed by training an internal person, not by the partner alone.

## Sheet: Closing actions

| Action id | Gap addressed | Action | Type | Person or role | Provider | Start | End | Cost (to estimate) | Status |
|---|---|---|---|---|---|---|---|---|---|
| GA-01 | dataverse-data-modelling | Shadow partner architect through blueprint workshops | Pairing | {{roles.solution-architect}} | {{constraints.partner}} | | | | Not started |
| GA-02 | power-platform-administration | Complete Microsoft Learn administrator learning paths | Training | {{roles.platform-administrator}} | Microsoft Learn | | | | Not started |
| GA-03 | data-migration | Add migration specialist to statement of work | Partner | {{roles.data-migration-lead}} | {{constraints.partner}} | | | | Not started |
| GA-04 | testing | Agree test manager secondment from another programme | Internal move | {{roles.test-manager}} | Internal | | | | Not started |

## Sheet: Availability by stage

| Person or role | Strategize | Initiate | Implement | Prepare | Operate | Known absences or change freezes |
|---|---|---|---|---|---|---|
| {{roles.executive-sponsor}} | Confirm | Confirm | Confirm | Confirm | Confirm | {{constraints.change_freezes}} |
| {{roles.process-owner}} | Confirm | Confirm | Confirm | Confirm | Confirm | |
| {{roles.platform-administrator}} | Confirm | Confirm | Confirm | Confirm | Confirm | |
| {{roles.support-lead}} | Confirm | Confirm | Confirm | Confirm | Confirm | |

> Guidance: Enter the percentage each person can give in each stage, as agreed with them and their line manager. Business peaks (year end, seasonal demand) are the usual cause of UAT slipping, so mark them here.

## Sheet: Backfill and handover

| Role | Filled by (internal, partner, contractor) | Business-as-usual work released | Backfill arrangement | Knowledge transfer needed before partner exit | Approved by |
|---|---|---|---|---|---|
| process-owner | Internal | Day-to-day team management | | Not applicable | {{roles.executive-sponsor}} |
| solution-architect | Partner | Not applicable | Not applicable | Design decisions log, data model walkthrough | {{roles.executive-sponsor}} |
| platform-administrator | Internal | Desktop support duties | | Environment and ALM runbooks | {{roles.executive-sponsor}} |

> Credit: Template from D365 CE Roster by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/dynamics-365-ce-roster), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
