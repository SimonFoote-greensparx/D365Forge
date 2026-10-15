---
id: solution-blueprint
title: Solution blueprint outline
format: docx
owner: solution-architecture:solution-blueprint
tailored_from: organisation, goals, modules, estate, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# Solution blueprint outline

## How to use this template

The solution architect ({{roles.solution-architect}}) writes the blueprint during Initiate, drawing on fit-to-standard workshop outcomes, the approved process maps and the integration and migration workbooks. The design authority ({{roles.design-authority-lead}}) reviews it before build starts, and blocking findings must be resolved before approval. After approval, update the blueprint whenever a design decision changes, and record the change in the decisions log so the design and the built system never drift apart.

The blueprint is the single description of what will be built and why. It links out to the detailed workbooks rather than repeating them.

> Guidance: Write for two audiences: a process owner who needs to recognise their process, and a developer who joins in month four and needs to understand the design principles. Diagrams help both; export them from the source tool and keep the source file with the project records.

> SMB: Sections 5 to 11 can be a few paragraphs each. Do not skip the security model or the customisation register; both are hard to retrofit.

> Enterprise only: Keep an overarching blueprint plus one annex per module workstream, each reviewed separately by the design authority.

## Document control

| Version | Date | Author | Summary of change | Reviewed by |
|---|---|---|---|---|
| 0.1 | {{generated_on}} | {{roles.solution-architect}} | Outline generated from organisation profile | |

## 1. Purpose and scope

This blueprint describes the Dynamics 365 Customer Engagement solution for {{organisation.name}}, covering {{modules_in_scope}} on Dataverse and Power Platform, delivered as a {{edition}} project with {{constraints.partner}}.

> Guidance: State the release this blueprint covers (MVP or a named phase) and list the documents it depends on: project charter, process maps, integration inventory, data migration mapping workbook, environment and ALM strategy.

## 2. Business context and outcomes

Outcomes: {{goals.outcomes}}. Success measures: {{goals.success_measures}}.

> Guidance: For each success measure, name the data the solution must capture to report it. If the solution cannot capture it, change the design or the measure now.

## 3. Design principles

> Guidance: Agree five to eight principles with the design authority and apply them to every decision. Typical principles for a Dynamics 365 project are listed below; keep, change or delete them.

- Use standard tables, forms and processes before configuration, and configuration before code.
- One customer record across Sales, Marketing, Customer Service and Field Service; no duplicate customer tables per module.
- Every extension has a named business owner and a recorded justification in the customisation register.
- Business logic sits server-side where it must always run, regardless of the client used.
- Security is designed in from the first sprint, not added before UAT.
- All changes reach test and production as managed solutions through a pipeline.

## 4. Solution overview

| Module | Apps and capabilities used | Users | Fit-to-standard summary |
|---|---|---|---|
| Sales | | {{modules.sales.users}} | |
| Marketing | Customer Insights - Journeys; Customer Insights - Data if unified profiles are in scope | {{modules.marketing.users}} | |
| Customer Service | Case management, queues, unified routing, knowledge; channels to confirm | {{modules.customer_service.users}} | |
| Field Service | Work orders, scheduling, Field Service Mobile, inventory | {{modules.field_service.technicians}} technicians | |

> Guidance: Delete rows for modules not in scope. Include a context diagram showing Dynamics 365, {{estate.erp}}, {{estate.email_and_calendar}}, {{estate.telephony}} and other systems in {{estate.integrations}}.

## 5. Process scope by module

| Process | Module | Process owner | Fit-to-standard outcome (standard, configure, extend, out of scope) | Backlog reference |
|---|---|---|---|---|
| Lead to opportunity | Sales | {{roles.process-owner}} | | |
| Quote to order | Sales | | | |
| Campaign to qualified lead | Marketing | | | |
| Case to resolution | Customer Service | | | |
| Work order to invoice | Field Service | | | |

## 6. Data model

> Guidance: Show the core standard tables used (account, contact, lead, opportunity, case, work order, customer asset and so on) and any custom tables, with their relationships. For each custom table, state why no standard table fits. Note the system of record for each shared entity, especially customers and products shared with {{estate.erp}}.

| Table | Standard or custom | Purpose | Owner type (user or organisation) | System of record | Notes |
|---|---|---|---|---|---|
| Account | Standard | Customer organisations | User | | |
| Contact | Standard | People at customers | User | | |
| | | | | | |

## 7. Security model

> Guidance: Describe business units, owner teams and Microsoft Entra ID group teams, security roles by persona, field-level security and any record sharing rules. Keep the business unit structure as flat as the access requirements allow. Regulatory context to consider: {{organisation.regulatory_context}}. Questions on personal data go to the organisation's DPO or legal adviser. Review with {{roles.security-lead}}.

| Persona | Security role(s) | Business unit | Teams | Field security profiles | Notes |
|---|---|---|---|---|---|
| Salesperson | | | | | |
| Service agent | | | | | |
| | | | | | |

## 8. Integration overview

> Guidance: Summarise the integration pattern for each interface and refer to the integration inventory for detail. Integrations in the profile: {{estate.integrations}}.

## 9. Data migration overview

> Guidance: Summarise what is migrated from {{estate.current_crm}} and {{estate.legacy_systems}}, the history cut-off and the load approach. Refer to the data migration mapping workbook for detail.

## 10. Environments, ALM and release

> Guidance: Summarise the environment and ALM strategy: environments, solution structure, publisher prefix, pipeline and how release waves are tested.

## 11. Reporting, analytics and AI

> Guidance: State which needs are met by standard dashboards and views, which by Power BI, and whether data is exported to an analytics platform. List Copilot or agent features proposed, each with a responsible AI review owner ({{roles.data-and-ai-lead}}). Check current Microsoft Learn documentation for availability and licensing; confirm licensing with the Microsoft licensing guide or your partner.

## 12. Non-functional requirements

| Area | Requirement | How it will be verified |
|---|---|---|
| Performance | Agreed response expectations for key forms and views | Performance testing in Prepare |
| Availability and continuity | | |
| Data residency | Environment region to match {{organisation.countries}} and compliance needs | |
| Retention and deletion | Agreed with DPO | |
| Accessibility | | |
| Offline and mobile | Field Service Mobile offline needs, if in scope | |

## 13. Customisation register

| ID | Extension | Type (plugin, PCF, flow, custom table, JavaScript) | Business justification | Alternative considered | Owner | Design authority status |
|---|---|---|---|---|---|---|
| CX01 | | | | | | |

## 14. Design decisions

| ID | Decision | Options considered | Rationale | Date | Approved by |
|---|---|---|---|---|---|
| DD01 | | | | | {{roles.design-authority-lead}} |

## 15. Open questions

| ID | Question | Owner | Needed by |
|---|---|---|---|
| Q01 | | | |

## 16. Approval

| Name | Role | Decision (approved, approved with advisory findings, not approved) | Date |
|---|---|---|---|
| {{roles.design-authority-lead}} | Design authority lead | | |
| {{roles.security-lead}} | Security lead | | |
| {{roles.process-owner}} | Process owner | | |

> Guidance: Design authority and security findings are classified as blocking or advisory. Blocking findings are not overruled by the delivery team; disagreements go to the executive sponsor ({{roles.executive-sponsor}}) or steering committee.
