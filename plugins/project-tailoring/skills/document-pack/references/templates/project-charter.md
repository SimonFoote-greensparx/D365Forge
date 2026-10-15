---
id: project-charter
title: Project charter and business case
format: docx
owner: programme-management:project-charter
tailored_from: organisation, goals, modules, estate, constraints, edition, modules_in_scope, roles, team_table, generated_on
status: draft
---

# Project charter and business case

## How to use this template

The project manager ({{roles.project-manager}}) drafts this charter with the executive sponsor ({{roles.executive-sponsor}}) during Strategize, before the partner statement of work is signed. The steering group approves it at the end of Initiate, once fit-to-standard workshops have tested the scope against the standard Dynamics 365 apps. After approval it changes only through change control: record every approved revision in the document control table and keep superseded versions.

Keep the charter short. It says why the project exists, what it must deliver, what it may spend and who decides. Detailed design belongs in the solution blueprint, and dates belong in the delivery plan.

> Guidance: Every section below was pre-filled from the organisation profile on {{generated_on}}. Treat each pre-filled value as a claim to confirm with its owner, not as an agreed fact.

## Document control

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | {{generated_on}} | {{roles.project-manager}} | First draft generated from the organisation profile | |
| | | | | |

## 1. Background and purpose

{{organisation.name}} is a {{organisation.sector}} organisation of {{organisation.size_staff}} staff operating in {{organisation.countries}}. Customer relationships are managed today in {{estate.current_crm}}, alongside {{estate.legacy_systems}}.

> Guidance: In two or three paragraphs, explain what is not working today, why it must be addressed now and what happens if nothing changes. Describe business problems (lost pipeline visibility, slow case resolution, double keying into the ERP), not software features. A sponsor should be able to read this section aloud at a board meeting.

## 2. Outcomes and success measures

Outcomes stated in the profile: {{goals.outcomes}}

Success measures stated in the profile: {{goals.success_measures}}

| Outcome | Success measure | Baseline today | Target | How and when measured | Benefit owner |
|---|---|---|---|---|---|
| | | Capture before Implement starts | | | {{roles.process-owner}} |
| | | | | | |

> Guidance: Each outcome needs at least one measure with a baseline taken from current systems before build starts; without it, nobody can show the benefit after go-live. Leave a target blank rather than writing a number nobody can evidence. Measures that only CRM data can produce (for example, time from case creation to first response) must be designed into the solution, so share this table with the solution architect.

## 3. Scope

### 3.1 Modules and users

Edition: {{edition}}. Modules in scope: {{modules_in_scope}}.

| Module | In scope | Users | Notes |
|---|---|---|---|
| Sales | {{modules.sales.in_scope}} | {{modules.sales.users}} | |
| Marketing (Customer Insights - Journeys) | {{modules.marketing.in_scope}} | {{modules.marketing.users}} | State whether Customer Insights - Data is included |
| Customer Service | {{modules.customer_service.in_scope}} | {{modules.customer_service.users}} | State which channels (email, chat, voice) are included |
| Field Service | {{modules.field_service.in_scope}} | {{modules.field_service.users}} office users, {{modules.field_service.technicians}} technicians | |

### 3.2 Processes in scope

> Guidance: List end-to-end processes, not screens: for example lead to opportunity, quote to order, case to resolution, work order to invoice. For each, name the process owner who will sign off design and UAT.

### 3.3 Out of scope

> Guidance: Write down what stakeholders might reasonably expect but will not get in this phase. An explicit exclusion list prevents more scope creep than any other paragraph in the charter.

### 3.4 Boundaries with other systems

| System | Current role | Relationship to Dynamics 365 | Decision needed by |
|---|---|---|---|
| {{estate.erp}} | ERP | Integrate, reference or out of scope | End of Initiate |
| {{estate.email_and_calendar}} | Email and calendar | Server-side synchronisation expected | End of Initiate |
| {{estate.telephony}} | Telephony | Integrate, replace or out of scope | End of Initiate |
| {{estate.integrations}} | Other integrations | Confirm each in the integration inventory | End of Initiate |

## 4. Delivery approach

The project follows the Success by Design stages: Strategize, Initiate, Implement, Prepare and Operate. Target go-live is {{goals.target_go_live}}. Implementation partner: {{constraints.partner}}.

> SMB: One partner consultant commonly covers several roles and the sponsor makes decisions directly. Favour standard configuration and a single go-live; state that principle here so later requests for customisation have to argue against it.

> Enterprise only: Describe the workstream structure (one per module plus integration and data, testing, and change), the design authority, the steering committee cadence and whether go-live is phased by module, region or business unit.

## 5. Business case

### 5.1 Options considered

| Option | Description | Benefits | Costs and risks | Recommended |
|---|---|---|---|---|
| A | Continue with {{estate.current_crm}} | No migration effort | Problems in section 1 remain | |
| B | Dynamics 365 using standard capability, minimal customisation | Faster delivery, easier upgrades through release waves | Some process change for users | |
| C | Dynamics 365 with significant extension | Closer fit to current ways of working | Higher build, test and upgrade cost | |

### 5.2 Costs

Budget band from the profile: {{goals.budget_band}}.

| Cost category | One-off | Recurring per year | Source of estimate | Confidence |
|---|---|---|---|---|
| Licences and capacity | | | Confirm with the Microsoft licensing guide or your partner | |
| Partner services | | | Statement of work | |
| Internal team time and backfill | | | Resource and skills-gap plan | |
| Integration and middleware | | | Integration inventory | |
| Data migration and cleansing | | | Data migration mapping workbook | |
| Training and change | | | Training and communications plan | |
| Hypercare and ongoing support | | | Support model | |
| Contingency | | | Risk-based, agreed with sponsor | |

> Guidance: Do not quote licence prices or edition names from memory. Licensing questions must be confirmed with the Microsoft licensing guide or your partner, and the confirmation recorded here.

### 5.3 Benefits

| Benefit | Type (cash, efficiency, risk, customer experience) | Linked success measure | Owner | Expected from |
|---|---|---|---|---|
| | | | | |

> Enterprise only: Add a benefits realisation schedule with review points after go-live, owned by the sponsor and reported to the steering committee.

## 6. Governance and roles

| Role | Proposed | Accountability in this project |
|---|---|---|
| Executive sponsor | {{roles.executive-sponsor}} | Owns the business case, chairs decisions, resolves escalations |
| Project manager | {{roles.project-manager}} | Plan, budget, RAID, reporting |
| Process owner | {{roles.process-owner}} | Signs off processes, designs and UAT |
| Solution architect | {{roles.solution-architect}} | End-to-end design and technical decisions |
| Design authority lead | {{roles.design-authority-lead}} | Independent design review; blocking findings stand |
| Data protection officer | {{roles.data-protection-officer}} | Advice on personal data, consent and retention |

Proposed team from the profile:

{{team_table}}

> Guidance: Role proposals are based on declared skills and availability only. Confirm each with the person and their line manager before the charter is approved. Escalations go to the sponsor or steering committee.

## 7. Constraints, assumptions and dependencies

Regulatory context: {{organisation.regulatory_context}}. Compliance constraints: {{constraints.compliance}}. Change freezes: {{constraints.change_freezes}}.

> Guidance: List the assumptions the budget and dates depend on (for example, process owners available as declared, ERP team able to expose the interfaces needed). Copy each into the RAID log so it is tracked. Data protection and legal questions go to the DPO or legal adviser.

## 8. Key risks

Known risks from the profile: {{constraints.known_risks}}

| Risk | Impact on outcomes | Response | Owner |
|---|---|---|---|
| | | | |

## 9. Key milestones

| Milestone | Stage | Target date | Decision owner |
|---|---|---|---|
| Charter approved | Initiate | | {{roles.executive-sponsor}} |
| Solution blueprint approved | Initiate | | {{roles.design-authority-lead}} |
| UAT signed off | Prepare | | {{roles.process-owner}} |
| Go/no-go decision | Prepare | | {{roles.executive-sponsor}} |
| Go-live | Operate | {{goals.target_go_live}} | {{roles.executive-sponsor}} |
| Hypercare exit | Operate | | {{roles.support-lead}} |

## 10. Approval

| Name | Role | Decision (approve, approve with conditions, reject) | Date |
|---|---|---|---|
| {{roles.executive-sponsor}} | Executive sponsor | | |
| | Finance representative | | |
| | Partner lead ({{constraints.partner}}) | | |

> Credit: Template from D365 CE Roster by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/dynamics-365-ce-roster), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
