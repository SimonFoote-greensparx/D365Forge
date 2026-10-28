---
id: raci-matrix
title: Roles and responsibilities (RACI)
format: xlsx
owner: project-tailoring:role-mapping
tailored_from: organisation, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# Roles and responsibilities (RACI)

## How to use this template

The project manager ({{roles.project-manager}}) completes this workbook in Initiate, starting from the role mapping proposed from the organisation profile on {{generated_on}}. Walk through it with the sponsor, process owners and partner lead ({{constraints.partner}}) in one session, because most RACI disputes surface only when people see their name against a row. Review it at each stage gate and whenever someone joins, leaves or changes availability.

Each worksheet covers one Success by Design stage. Rows are project activities and columns are the main project roles, headed with the person or alias proposed for each role.

> Guidance: Use R (responsible: does the work), A (accountable: owns the outcome and signs it off), C (consulted before the work is finished) and I (informed afterwards). Every row has exactly one A. "A/R" is acceptable where one person both owns and does the work. Roles outside the main columns (module consultants, trainer, release manager, DPO, makers) go in the last column.

> SMB: Several columns will show the same person. That is expected; check the "Combination checks" sheet and record how any caution is mitigated.

> Enterprise only: Add a column per module workstream lead and repeat the Implement sheet per workstream if responsibilities differ.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Generated on | {{generated_on}} |
| Legend | R responsible, A accountable, C consulted, I informed |
| Rule | One A per row; nobody is accountable for approving their own testing or migration reconciliation |
| Basis of proposals | Declared skills and availability in the organisation profile only; confirm every assignment with the person |

## Sheet: Strategize

| Activity | Deliverable or decision | Executive sponsor ({{roles.executive-sponsor}}) | Project manager ({{roles.project-manager}}) | Business analyst ({{roles.business-analyst}}) | Process owner ({{roles.process-owner}}) | Solution architect ({{roles.solution-architect}}) | Design authority lead ({{roles.design-authority-lead}}) | Developer ({{roles.developer}}) | Integration lead ({{roles.integration-lead}}) | Data migration lead ({{roles.data-migration-lead}}) | Test manager ({{roles.test-manager}}) | Change lead ({{roles.change-lead}}) | Platform administrator ({{roles.platform-administrator}}) | Security lead ({{roles.security-lead}}) | Support lead ({{roles.support-lead}}) | Other roles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agree business outcomes and success measures | Charter outcomes table | A | R | C | C | C | | | | | | C | | | | |
| Approve business case and budget | Approved business case | A | R | | C | C | | | | | | | | | | Finance: C |
| Select partner and confirm edition | Signed statement of work | A | R | | C | C | | | | | | | | C | | Procurement: R |
| Assess licensing and capacity | Licence plan confirmed with the Microsoft licensing guide or partner | I | A | | C | C | | | | | | | R | | | |
| Initial stakeholder and change impact analysis | Stakeholder map | C | A | C | C | | | | | | | R | | | | |
| Confirm project roles from declared skills | Role mapping and skills-gap plan | C | A/R | | C | C | | | | | | C | | | C | Line managers: C |

## Sheet: Initiate

| Activity | Deliverable or decision | Executive sponsor ({{roles.executive-sponsor}}) | Project manager ({{roles.project-manager}}) | Business analyst ({{roles.business-analyst}}) | Process owner ({{roles.process-owner}}) | Solution architect ({{roles.solution-architect}}) | Design authority lead ({{roles.design-authority-lead}}) | Developer ({{roles.developer}}) | Integration lead ({{roles.integration-lead}}) | Data migration lead ({{roles.data-migration-lead}}) | Test manager ({{roles.test-manager}}) | Change lead ({{roles.change-lead}}) | Platform administrator ({{roles.platform-administrator}}) | Security lead ({{roles.security-lead}}) | Support lead ({{roles.support-lead}}) | Other roles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Run fit-to-standard workshops per module | Fit-to-standard outcomes | I | C | R | C | A | | | | | | | | | | Module consultants: R |
| Sign off to-be processes and backlog | Approved process maps and user stories | I | C | R | A | C | | | | | | I | | | | |
| Produce solution blueprint | Approved solution blueprint | I | C | C | C | R | A | C | C | C | C | | C | C | | |
| Define environment and ALM strategy | Environment and ALM strategy | | I | | | A | C | C | | | C | | R | C | | Release manager: R |
| Design security model | Security roles, business units, teams | | I | C | C | R | C | | | | | | C | A | | DPO: C |
| Agree integration and migration approach | Integration inventory, migration strategy | | I | | C | A | C | | R | R | C | | | C | | |
| Baseline delivery plan and RAID log | Delivery plan, RAID log | A | R | C | C | C | | | C | C | C | C | | | | |
| Agree test strategy | Test strategy | | C | C | C | C | | | | | A/R | | | | | |

## Sheet: Implement

| Activity | Deliverable or decision | Executive sponsor ({{roles.executive-sponsor}}) | Project manager ({{roles.project-manager}}) | Business analyst ({{roles.business-analyst}}) | Process owner ({{roles.process-owner}}) | Solution architect ({{roles.solution-architect}}) | Design authority lead ({{roles.design-authority-lead}}) | Developer ({{roles.developer}}) | Integration lead ({{roles.integration-lead}}) | Data migration lead ({{roles.data-migration-lead}}) | Test manager ({{roles.test-manager}}) | Change lead ({{roles.change-lead}}) | Platform administrator ({{roles.platform-administrator}}) | Security lead ({{roles.security-lead}}) | Support lead ({{roles.support-lead}}) | Other roles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Configure and build backlog items | Configured solution in development | | I | C | C | A | | R | | | | | | | | Makers and module consultants: R |
| Review customisations against standards | Design review findings (blocking or advisory) | | I | | | R | A | C | C | | | | | C | | |
| Build and unit test integrations | Integrations deployed to test | | I | | | A | C | R | R | | C | | | C | | |
| Run mock data migrations | Mock migration and reconciliation report | | I | | C | C | | | | A/R | C | | | | | |
| Execute system integration testing | SIT exit report | | I | | | C | | R | R | R | A | | | | | |
| Promote solutions between environments | Release notes and deployment log | | I | | | C | | C | | | C | | R | | | Release manager: A |
| Develop training materials | Role-based training materials | | I | C | C | | | | | | | A | | | | Trainer: R |
| Sprint reviews and demos | Accepted backlog items | I | A | R | C | C | | R | | | | I | | | | |

## Sheet: Prepare

| Activity | Deliverable or decision | Executive sponsor ({{roles.executive-sponsor}}) | Project manager ({{roles.project-manager}}) | Business analyst ({{roles.business-analyst}}) | Process owner ({{roles.process-owner}}) | Solution architect ({{roles.solution-architect}}) | Design authority lead ({{roles.design-authority-lead}}) | Developer ({{roles.developer}}) | Integration lead ({{roles.integration-lead}}) | Data migration lead ({{roles.data-migration-lead}}) | Test manager ({{roles.test-manager}}) | Change lead ({{roles.change-lead}}) | Platform administrator ({{roles.platform-administrator}}) | Security lead ({{roles.security-lead}}) | Support lead ({{roles.support-lead}}) | Other roles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Execute UAT and sign off | UAT sign-off per process | I | C | R | A | C | | C | | | R | C | | | | Super users: R |
| Run performance and security testing | Performance and security test reports | | I | | | C | | R | C | | A | | C | R | | |
| Deliver end-user training | Training completion records | I | C | | C | | | | | | | A | | | | Trainer: R |
| Plan and rehearse cutover | Cutover runbook and rehearsal report | | A | | C | C | | C | R | R | C | | R | | C | |
| Prepare production environment and access | Production ready, roles assigned | | I | | | C | | | | | | | A/R | C | | |
| Set up support model and hypercare rota | Support model | | C | | C | | | | | | | | C | | A/R | |
| Go/no-go decision | Signed go/no-go record | A | R | | C | C | C | | | | C | C | C | C | C | DPO: C |

## Sheet: Operate

| Activity | Deliverable or decision | Executive sponsor ({{roles.executive-sponsor}}) | Project manager ({{roles.project-manager}}) | Business analyst ({{roles.business-analyst}}) | Process owner ({{roles.process-owner}}) | Solution architect ({{roles.solution-architect}}) | Design authority lead ({{roles.design-authority-lead}}) | Developer ({{roles.developer}}) | Integration lead ({{roles.integration-lead}}) | Data migration lead ({{roles.data-migration-lead}}) | Test manager ({{roles.test-manager}}) | Change lead ({{roles.change-lead}}) | Platform administrator ({{roles.platform-administrator}}) | Security lead ({{roles.security-lead}}) | Support lead ({{roles.support-lead}}) | Other roles |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Execute cutover and go-live | Production live | I | A | | C | C | | R | R | R | | | R | | C | |
| Hypercare triage and fixes | Hypercare log | I | C | | C | C | | R | R | | | | R | | A | |
| Track adoption against success measures | Adoption report | I | C | | R | | | | | | | A | | | C | |
| Benefits realisation review | Benefits report | A | R | | R | | | | | | | C | | | | |
| Prepare for each release wave | Regression results and release readiness note | | I | | C | C | C | | | | R | | A | | C | |
| Manage the continuous improvement backlog | Prioritised backlog | I | | R | A | C | C | | | | | | | | R | |
| Close the project and hand over to business as usual | Closure report | A | R | | C | | | | | | | | C | | R | |

## Sheet: Combination checks

| Roles held by one person | Severity | Why it matters | Mitigation if combined | Applies on this project (Y/N) |
|---|---|---|---|---|
| Developer and test manager | Unsafe | The person who builds a change should not sign off its testing | Assign a separate test manager | |
| Data migration lead and test manager | Unsafe | Reconciliation must be checked by someone other than the person who loaded the data | Assign an independent reconciler | |
| Solution architect and design authority lead | Caution | Normal at SMB scale, but designs are then self-reviewed | Arrange a second-pair-of-eyes review outside the delivery | |
| Release manager and developer | Caution | Without automated pipelines one person both changes and promotes code | Use pipelines with approval gates | |
| Executive sponsor and project manager | Caution | Removes the escalation route | Keep a steering group in place | |
| Security lead and data protection officer | Caution | The DPO's advice should stay independent of control design | Record DPO advice separately | |

> Guidance: Unsafe combinations must not appear in the final matrix. Cautions may stand if the mitigation is written down and agreed by the sponsor.

> Credit: Template from D365Forge by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/D365Forge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
