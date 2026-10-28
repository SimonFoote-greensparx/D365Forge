---
id: cutover-and-hypercare-checklist
title: Cutover and hypercare checklist
format: xlsx
owner: support-operations:cutover-plan
tailored_from: organisation, goals, estate, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# Cutover and hypercare checklist

## How to use this template

The project manager ({{roles.project-manager}}) owns the cutover plan and the support lead ({{roles.support-lead}}) owns hypercare. Start the workbook early in Prepare so it can be tested in at least one full rehearsal before go-live, and refine it after each rehearsal using the timings actually achieved. During cutover, the runbook is the single source of truth: tasks are ticked off in it as they complete and every deviation is logged. Hypercare sheets stay in use until the exit criteria are met and support is handed over.

Target go-live: {{goals.target_go_live}}. Known change freezes: {{constraints.change_freezes}}.

> Guidance: Rehearse the cutover end to end in a non-production environment with the people who will do it on the night, and time every step. A cutover that has not been rehearsed is a guess. Agree the rollback point before cutover starts: the moment after which going back costs more than fixing forward.

> SMB: Cutover may take a single evening or weekend with the partner, the administrator and one process owner. Keep the go/no-go criteria and the rollback decision written down even when the same few people take every decision.

> Enterprise only: Run a cutover command centre with a published schedule of checkpoints, a named decision-maker at each go/no-go point, and separate runbooks per module or region if go-live is phased.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Legacy system being replaced | {{estate.current_crm}} |
| Generated on | {{generated_on}} |
| Time convention | T is go-live; T-5d is five days before, T+1d one day after |
| Status values | Not started, In progress, Done, Blocked, Not applicable |

## Sheet: Readiness

| ID | Readiness item | Area | Owner | Due | Evidence | Status |
|---|---|---|---|---|---|---|
| RD01 | UAT signed off for every process in scope | Testing | {{roles.process-owner}} | | Signed UAT sign-off forms | |
| RD02 | Final mock migration and reconciliation passed | Data | {{roles.data-migration-lead}} | | Reconciliation sheet signed by independent checker | |
| RD03 | Licences assigned and security roles mapped for every user | Access | {{roles.platform-administrator}} | | User and role export reviewed | |
| RD04 | Mailboxes approved and tested for server-side synchronisation | Email | {{roles.platform-administrator}} | | Mailbox test results | |
| RD05 | Production integrations configured with live endpoints and credentials | Integration | {{roles.integration-lead}} | | Connection test log | |
| RD06 | Users trained and quick-reference guides published | Change | {{roles.change-lead}} | | Training completion by team | |
| RD07 | Support model, hypercare rota and escalation routes agreed | Support | {{roles.support-lead}} | | Published rota | |
| RD08 | Cutover rehearsed and timings fit the agreed window | Cutover | {{roles.project-manager}} | | Rehearsal report | |

## Sheet: Cutover runbook

| ID | When | Task | Detail | Owner | Planned start | Planned duration | Depends on | Checkpoint | Status | Actual finish |
|---|---|---|---|---|---|---|---|---|---|---|
| CO01 | T-2d | Freeze data entry in {{estate.current_crm}} | Set legacy system to read-only; communicate to users | {{roles.process-owner}} | | | Go decision for cutover start | | | |
| CO02 | T-2d | Deploy final managed solutions to production | Through pipeline; record solution versions | {{roles.release-manager}} | | | CO01 | | | |
| CO03 | T-2d | Set environment variables, connection references and configuration data | Use production values from the ALM strategy | {{roles.platform-administrator}} | | | CO02 | | | |
| CO04 | T-1d | Extract and load final migration data | Follow load order in mapping workbook | {{roles.data-migration-lead}} | | | CO03 | | | |
| CO05 | T-1d | Reconcile migrated data | Counts and sample field checks by independent checker | {{roles.test-manager}} | | | CO04 | Go/no-go checkpoint 1 | | |
| CO06 | T-1d | Enable integrations and confirm first messages flow | Start with inbound reference data | {{roles.integration-lead}} | | | CO05 | | | |
| CO07 | T | Business smoke test with key users | Run agreed smoke scripts per module | {{roles.process-owner}} | | | CO06 | Go/no-go checkpoint 2 | | |
| CO08 | T | Open access to all users and send go-live communication | Enable security roles or app access | {{roles.platform-administrator}} | | | CO07 | | | |

> Guidance: The rows above are typical anchor tasks; a real runbook often has many more. Add module-specific steps (for example, activating SLAs, routing rules and queues for Customer Service, or enabling the schedule board and mobile sync for Field Service).

## Sheet: Go-no-go criteria

| Criterion | Measure | Threshold agreed | Evidence | Owner | Result (go or no-go) |
|---|---|---|---|---|---|
| No open critical defects | Defect log | None open | Defect report | {{roles.test-manager}} | |
| Data reconciliation complete | Reconciliation sheet | Every difference explained | Signed reconciliation | {{roles.data-migration-lead}} | |
| Integrations working | First messages processed | Agree per interface | Integration monitoring | {{roles.integration-lead}} | |
| Users can sign in with correct access | Smoke test by persona | All personas pass | Smoke test log | {{roles.security-lead}} | |
| Support ready | Rota staffed, channels live | In place | Published rota | {{roles.support-lead}} | |

> Guidance: The executive sponsor ({{roles.executive-sponsor}}) takes the final decision on the evidence above and records it.

## Sheet: Rollback plan

| Trigger | Decision point | Rollback steps | Owner | Latest time to decide | Communication |
|---|---|---|---|---|---|
| Reconciliation fails and cannot be fixed in the window | Checkpoint 1 | Keep legacy system live; reopen data entry; disable production access | {{roles.project-manager}} | | Users told to continue in {{estate.current_crm}} |
| Critical process fails in smoke test | Checkpoint 2 | As above; log defects; replan cutover | {{roles.project-manager}} | | Sponsor briefing, user notice |
| Integration failure affecting orders or billing | Checkpoint 2 | Suspend interface; agree manual workaround or roll back | {{roles.integration-lead}} | | {{estate.erp}} owners informed |

## Sheet: Hypercare daily checks

| Check | Frequency | Owner | Where to look | Escalate when |
|---|---|---|---|---|
| Integration errors and failed messages | Several times daily | {{roles.integration-lead}} | Middleware or flow run history | Any failure on an order or billing interface |
| Failed background processes and plug-in errors | Daily | {{roles.platform-administrator}} | System jobs and plug-in trace log | Repeated failures on the same process |
| Mailbox synchronisation errors | Daily | {{roles.platform-administrator}} | Mailbox status and alerts | Any mailbox failing to sync |
| Case routing and queue backlog | Daily | {{roles.customer-service-consultant}} | Queues and routing diagnostics | Work not reaching agents |
| Schedule board and mobile sync issues | Daily | {{roles.field-service-consultant}} | Technician reports, sync errors | Technicians unable to complete jobs |
| Access and security requests | Daily | {{roles.security-lead}} | Support queue | Any request for elevated access |
| Usage of key processes by team | Weekly | {{roles.change-lead}} | Adoption reports (aggregated) | A team not using a core process |

## Sheet: Hypercare log

| ID | Date | Reported by (team) | Module | Description | Severity | Workaround | Owner | Fix target | Status |
|---|---|---|---|---|---|---|---|---|---|
| HC01 | | | | | | | | | |
| HC02 | | | | | | | | | |
| HC03 | | | | | | | | | |

## Sheet: Hypercare exit

| Criterion | Agreed target | Current position | Evidence | Approved by |
|---|---|---|---|---|
| No open critical or high hypercare issues | None open | | Hypercare log | {{roles.support-lead}} |
| Support team handling incidents without project help | Agreed with support lead | | Support tickets | {{roles.support-lead}} |
| Runbooks, known errors and admin documentation handed over | Complete | | Handover checklist | {{roles.platform-administrator}} |
| Adoption tracking in place against success measures | Reporting live | | Adoption report | {{roles.change-lead}} |
| Legacy system decommissioning or archive plan agreed | Plan approved | | Plan document | {{roles.process-owner}} |

> Credit: Template from D365Forge by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/D365Forge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
