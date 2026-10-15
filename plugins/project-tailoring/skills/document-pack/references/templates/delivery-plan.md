---
id: delivery-plan
title: Delivery plan and milestones
format: xlsx
owner: programme-management:delivery-plan
tailored_from: organisation, goals, modules, estate, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# Delivery plan and milestones

## How to use this template

The project manager ({{roles.project-manager}}) builds this plan in Initiate with the partner ({{constraints.partner}}) and the solution architect, working back from the target go-live of {{goals.target_go_live}}. Baseline it when the solution blueprint is approved and report progress against that baseline at every steering meeting. Re-baseline only through change control, and keep the earlier baseline in the file so slippage stays visible.

The plan is organised by Success by Design stage. Workstreams are listed per module in scope ({{modules_in_scope}}) plus the cross-cutting streams every Dynamics 365 project needs.

> Guidance: Plan backwards from go-live as well as forwards from mobilisation. Fix the dates that are outside your control first (release waves, organisation change freezes, ERP releases, peak trading), then place UAT, training and cutover so none of them collides with those dates.

> SMB: Use one combined workstream for the apps in scope, two-week sprints and a short Prepare stage. Keep the stage gates; a small project still needs a documented go/no-go.

> Enterprise only: Give each module its own workstream lead and sprint backlog, add an integrated plan for SIT and UAT across modules, and decide early whether go-live is phased by module, region or business unit.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Target go-live | {{goals.target_go_live}} |
| Known change freezes | {{constraints.change_freezes}} |
| Generated on | {{generated_on}} |
| Status values | Not started, On track, At risk, Late, Complete |

## Sheet: Phases

| Stage | Phase | Objective | Exit criteria (stage gate) | Start | End | Owner | Status |
|---|---|---|---|---|---|---|---|
| Strategize | Vision and business case | Agree outcomes, scope, budget and partner | Charter drafted, statement of work signed | | | {{roles.executive-sponsor}} | |
| Initiate | Mobilise | Team, governance and environments in place | RACI agreed, sandboxes provisioned, backlog tool ready | | | {{roles.project-manager}} | |
| Initiate | Fit-to-standard and design | Test processes against standard apps, close gaps by design | Solution blueprint approved by design authority | | | {{roles.solution-architect}} | |
| Implement | Build sprints | Configure, extend and integrate in short iterations | All MVP backlog items accepted at sprint review | | | {{roles.project-manager}} | |
| Implement | System integration testing | Prove end-to-end processes across modules and integrations | SIT exit criteria met, final mock migration passed | | | {{roles.test-manager}} | |
| Prepare | UAT, performance and training | Business proves the solution and users are ready | UAT signed off, training delivered, performance accepted | | | {{roles.process-owner}} | |
| Prepare | Cutover readiness | Rehearse cutover and decide go/no-go | Rehearsal completed in agreed window, go decision recorded | | | {{roles.project-manager}} | |
| Operate | Go-live and hypercare | Stabilise and hand over to support | Hypercare exit criteria met | | {{goals.target_go_live}} plus hypercare | {{roles.support-lead}} | |

## Sheet: Workstreams

| Workstream | Module | Lead | Key deliverables | Depends on | Peak stage | Include? |
|---|---|---|---|---|---|---|
| Sales | Sales ({{modules.sales.users}} users) | {{roles.sales-consultant}} | Lead to opportunity, products and price lists, quotes, forecasting | Product and customer data from {{estate.erp}} | Implement | {{modules.sales.in_scope}} |
| Marketing | Customer Insights - Journeys | {{roles.journeys-consultant}} | Journeys, segments, consent and preference centre, sending domain set-up | DNS changes, consent history from current systems | Implement | {{modules.marketing.in_scope}} |
| Customer Service | Customer Service ({{modules.customer_service.users}} users) | {{roles.customer-service-consultant}} | Case lifecycle, queues and unified routing, SLAs, knowledge, channels | {{estate.telephony}} | Implement | {{modules.customer_service.in_scope}} |
| Field Service | Field Service ({{modules.field_service.technicians}} technicians) | {{roles.field-service-consultant}} | Work orders, incident types, schedule board, Field Service Mobile, inventory | Inventory and invoicing in {{estate.erp}} | Implement | {{modules.field_service.in_scope}} |
| Integration and data | All | {{roles.integration-lead}} | Integrations, migration mapping, mock migrations, reconciliation | Source system owners | Implement to Prepare | Yes |
| Platform and ALM | All | {{roles.platform-administrator}} | Environments, pipelines, security roles, monitoring | Tenant and identity teams | Initiate onwards | Yes |
| Testing | All | {{roles.test-manager}} | Test strategy, SIT, UAT, regression pack | Stable test environments | Implement to Prepare | Yes |
| Change and training | All | {{roles.change-lead}} | Stakeholder plan, communications, role-based training, super users | Process sign-off | Prepare | Yes |

> Guidance: Delete workstream rows for modules marked out of scope.

## Sheet: Milestones

| ID | Milestone | Stage | Baseline date | Forecast date | Owner | Evidence of completion | Status |
|---|---|---|---|---|---|---|---|
| M01 | Charter and business case approved | Initiate | | | {{roles.executive-sponsor}} | Signed approval page | |
| M02 | Solution blueprint approved | Initiate | | | {{roles.design-authority-lead}} | Design authority minutes, no open blocking findings | |
| M03 | Build complete | Implement | | | {{roles.solution-architect}} | Final sprint review accepted | |
| M04 | SIT exit | Implement | | | {{roles.test-manager}} | SIT exit report | |
| M05 | UAT signed off | Prepare | | | {{roles.process-owner}} | UAT sign-off form per process | |
| M06 | Go/no-go decision | Prepare | | | {{roles.executive-sponsor}} | Signed go/no-go record | |
| M07 | Go-live | Operate | {{goals.target_go_live}} | | {{roles.project-manager}} | Production smoke test passed | |
| M08 | Hypercare exit | Operate | | | {{roles.support-lead}} | Exit criteria met, handover signed | |

## Sheet: Sprint plan

| Sprint | Start | End | Sprint goal | Workstreams | Review date | Status |
|---|---|---|---|---|---|---|
| 1 | | | Core data model, accounts and contacts, base security roles | Platform, all modules | | |
| 2 | | | Lead to opportunity and first integration stub | Sales, Integration | | |
| 3 | | | Case creation, queues and routing rules | Customer Service | | |

## Sheet: Release waves and freezes

| Item | Why it matters | Date | Where to check | Action | Owner |
|---|---|---|---|---|---|
| Release plans for the next wave published | Shows new and changed features for in-scope modules | Check current release plans | Microsoft Learn release planning pages | Review features and deprecations for in-scope modules | {{roles.solution-architect}} |
| Early access window for the next wave | Allows regression testing in a sandbox before updates are applied | Check current dates | Power Platform admin center and Microsoft Learn | Enable on a sandbox copy and run the regression pack | {{roles.platform-administrator}} |
| Wave updates applied to production | Platform changes arrive in production | Check current dates | Microsoft 365 admin center Message center | Avoid go-live and cutover in the same window | {{roles.platform-administrator}} |
| Deprecation announcements | Features in the design may be withdrawn | Check before blueprint approval | Microsoft Learn deprecation notices | Log affected items in the RAID log | {{roles.solution-architect}} |
| Organisation change freezes | {{constraints.change_freezes}} | | Internal calendar | Keep cutover and training outside freeze periods | {{roles.project-manager}} |
| ERP and telephony vendor releases | Interfaces may change | | {{estate.erp}} and {{estate.telephony}} owners | Agree interface freeze from SIT to hypercare exit | {{roles.integration-lead}} |

> Guidance: Never type release dates from memory. Check the current Microsoft Learn release planning pages and the Power Platform admin center each time the plan is re-baselined.
