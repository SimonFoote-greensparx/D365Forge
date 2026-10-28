---
id: test-strategy-and-uat-scripts
title: Test strategy and UAT script pack
format: docx
owner: testing-quality:test-strategy
tailored_from: organisation, goals, estate, modules_in_scope, roles, generated_on
status: draft
---

# Test strategy and UAT script pack

## How to use this template

The test manager ({{roles.test-manager}}) writes the strategy in Initiate and agrees it with the solution architect and the process owners before the first sprint, so that testing is planned into the build rather than bolted on at the end. Process owners ({{roles.process-owner}}) and super users write the UAT scripts during Implement from the signed-off process maps and user stories, and execute them in Prepare. Update the strategy when scope, environments or the release plan change, and keep the UAT script pack as the regression baseline for future release waves.

> Guidance: Test what the business depends on, not every setting. Prioritise end-to-end processes, security roles, integrations and migrated data; Microsoft already tests the standard platform.

> SMB: Combine SIT and UAT into one business-led cycle if the solution is mostly standard configuration, but keep separate exit criteria and a written UAT sign-off.

> Enterprise only: Run distinct SIT and UAT cycles across modules, add performance testing, automated regression and a test tool with traceability from requirement to test to defect.

## Document control

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | {{generated_on}} | {{roles.test-manager}} | First draft generated from organisation profile | |

## 1. Scope and objectives

Scope covers {{modules_in_scope}} for {{organisation.name}}, including integrations with {{estate.integrations}} and data migrated from {{estate.current_crm}}.

> Guidance: State the objectives in business terms, linked to the success measures ({{goals.success_measures}}). List explicitly what will not be tested (for example, standard platform features used without change).

## 2. Test levels

| Level | Purpose | Performed by | Environment | Entry criteria | Exit criteria |
|---|---|---|---|---|---|
| Unit and component | Each configuration item or extension works as designed | {{roles.developer}}, consultants | Development | Story built | Acceptance criteria met |
| System integration testing (SIT) | End-to-end processes across modules and integrations | {{roles.test-manager}} | Test or SIT | Build complete, interfaces deployed | No open critical or high defects |
| Data migration validation | Migrated data is complete and usable | {{roles.data-migration-lead}} with independent checker | Test or SIT | Mock migration loaded | Reconciliation signed off |
| Security and role testing | Each persona sees and does only what it should | {{roles.security-lead}} | Test or SIT | Security roles built | All persona tests passed |
| Performance | Key forms, views and integrations meet agreed expectations | {{roles.test-manager}} | Pre-production or UAT | Representative data volumes | Agreed expectations met |
| User acceptance testing (UAT) | The business confirms it can run its processes | {{roles.process-owner}} | UAT | SIT exit, UAT scripts approved, testers trained | Signed UAT sign-off per process |
| Regression | Changes and release waves do not break working processes | {{roles.test-manager}} | Sandbox on early access | Regression pack current | Pack passed or issues accepted |

## 3. Environments and test data

> Guidance: Describe the test data set for each level. Do not copy production personal data into test or UAT without masking or an approval agreed with the DPO or legal adviser ({{roles.data-protection-officer}}). Test users must hold the same security roles as the real personas; testing as a system administrator hides most security defects.

## 4. Defect management

| Severity | Definition | Expected response |
|---|---|---|
| Critical | A core process cannot be completed and there is no workaround | Fix before the cycle continues |
| High | A core process is impaired; a workaround exists but is not acceptable for go-live | Fix before exit |
| Medium | A secondary function is impaired; acceptable workaround exists | Fix or defer by agreement |
| Low | Cosmetic or minor inconvenience | Defer to backlog |

> Guidance: Agree who triages defects, how often, and who may defer a defect. A process owner, not the delivery team, decides whether a workaround is acceptable for go-live.

## 5. Roles

| Role | Responsibility |
|---|---|
| {{roles.test-manager}} | Strategy, planning, defect triage, exit reports |
| {{roles.process-owner}} | UAT scope, script approval, sign-off |
| Super users and testers | Execute UAT scripts and record evidence |
| {{roles.developer}} and consultants | Fix defects, unit test |

> Guidance: The person who built a change should not be the one who signs off its testing.

## 6. Release wave regression

> Guidance: Describe how the UAT pack is reduced to a regression pack, which sandbox is used for early access testing, and who decides whether a release wave issue blocks the update. Check current Microsoft Learn documentation for release wave dates. Consider automating the most-used processes.

## 7. UAT approach

UAT runs in Prepare, before the go/no-go decision and ahead of the target go-live of {{goals.target_go_live}}.

> Guidance: Plan UAT as scenarios that follow a real piece of work from start to finish across teams (for example, an enquiry becoming an opportunity, a quote and an order). Give testers short training first, run UAT in a room or channel with the consultants available, and hold a daily triage. Allow time for a retest cycle.

## 8. UAT script format

Each script follows a process from start to finish under one persona. Record evidence (screenshots or record references) for every step marked as a checkpoint.

| Script ID | Module | Process | Scenario | Persona and security role | Preconditions | Step | Action | Test data | Expected result | Actual result | Pass or fail | Defect reference | Tester | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| UAT-SAL-01 | Sales | Lead to opportunity | Qualify an inbound web lead | Salesperson | Lead exists, assigned to tester | 1 | Open the lead and complete qualification fields | Test lead A | Business process flow advances to the next stage | | | | | |
| UAT-SAL-01 | Sales | Lead to opportunity | Qualify an inbound web lead | Salesperson | | 2 | Qualify the lead | | Account, contact and opportunity created and linked; no duplicate account | | | | | |
| UAT-CS-01 | Customer Service | Case to resolution | Customer emails the support address | Service agent | Mailbox and email-to-case configured | 1 | Send an email from a test customer address | Test contact B | Case created, linked to the contact and routed to the correct queue | | | | | |
| UAT-CS-01 | Customer Service | Case to resolution | Customer emails the support address | Service agent | | 2 | Pick the case, reply and resolve it | | Reply on timeline; SLA timer stops; case resolved | | | | | |
| UAT-FS-01 | Field Service | Work order to completion | Reactive repair visit | Dispatcher, then technician | Customer asset and incident type exist | 1 | Create a work order and schedule it on the schedule board | Test asset C | Booking created for an available technician | | | | | |
| UAT-FS-01 | Field Service | Work order to completion | Reactive repair visit | Technician | Field Service Mobile signed in | 2 | Complete tasks, record parts used and close the booking | | Work order status updated; product usage recorded | | | | | |
| UAT-MKT-01 | Marketing | Campaign to lead | Prospect submits a marketing form | Marketing user | Form published on test page | 1 | Submit the form with consent ticked | Test prospect D | Contact or lead created with consent recorded and journey started | | | | | |

> Guidance: Delete rows for modules not in scope and write one script per process variant that matters to the business. Each expected result must be checkable by a business tester without technical knowledge.

## 9. UAT sign-off

| Process | Scripts executed | Passed | Open defects (by severity) | Workarounds accepted | Decision (accept, accept with conditions, reject) | Process owner | Date |
|---|---|---|---|---|---|---|---|
| | | | | | | {{roles.process-owner}} | |

## 10. Approval of this strategy

| Name | Role | Decision | Date |
|---|---|---|---|
| {{roles.test-manager}} | Test manager | | |
| {{roles.solution-architect}} | Solution architect | | |
| {{roles.process-owner}} | Process owner | | |

> Credit: Template from D365Forge by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/D365Forge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
