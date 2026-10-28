---
id: training-and-communications-plan
title: Training and communications plan
format: docx
owner: change-adoption:role-based-training
tailored_from: organisation, goals, modules, constraints, modules_in_scope, roles, generated_on
status: draft
---

# Training and communications plan

## How to use this template

The change lead ({{roles.change-lead}}) owns this plan, with the trainer ({{roles.trainer}}) responsible for the curriculum and materials. Draft the audience analysis and communication timeline in Initiate, build the curriculum during Implement once processes are signed off, and deliver training in Prepare as close to go-live as practical. Keep the plan live through hypercare: update it as feedback arrives and for each release wave that changes what users see.

> Guidance: People adopt a CRM system when it helps them do their own job, so train by role and by process, using the organisation's own data and scenarios rather than generic feature tours. Training records show readiness; they are not used to assess, rank or compare individuals.

> SMB: The partner often trains a small group of super users who then train colleagues. Make sure the super users have time released for it, and keep a short quick-reference guide per role.

> Enterprise only: Use a full train-the-trainer model, a dedicated training environment refreshed between cohorts, a learning management system for scheduling and completion tracking, and a formal super-user network per region or business unit.

## Document control

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | {{generated_on}} | {{roles.change-lead}} | First draft generated from organisation profile | |

## 1. Purpose and scope

This plan prepares users at {{organisation.name}} to use {{modules_in_scope}} from the target go-live of {{goals.target_go_live}}, and keeps them informed through the change.

> Guidance: Link the plan to the outcomes it supports ({{goals.outcomes}}) and state which success measures depend on adoption.

## 2. Audiences

| Audience | Module | Approximate number | Security role(s) | What changes for them | Change impact (high, medium, low) | Super user |
|---|---|---|---|---|---|---|
| Salespeople and sales managers | Sales | {{modules.sales.users}} | | | | |
| Marketing team | Marketing | {{modules.marketing.users}} | | | | |
| Service agents and supervisors | Customer Service | {{modules.customer_service.users}} | | | | |
| Dispatchers | Field Service | {{modules.field_service.users}} | | | | |
| Field technicians | Field Service | {{modules.field_service.technicians}} | | | | |
| Administrators and support team | All | | | | | Not applicable |
| Leaders and managers | All | | | Reports and dashboards they will use | | |

> Guidance: Delete rows for modules not in scope. Describe what changes in terms of daily work (for example, "cases arrive in a queue rather than a shared mailbox"), drawn from the stakeholder analysis and process maps.

## 3. Training approach

> Guidance: Describe the mix of instructor-led sessions, short videos, quick-reference guides and in-app guidance, and why it suits each audience. Field technicians usually need hands-on practice on the device they will use, including offline working on Field Service Mobile if in scope. Schedule training in the weeks just before go-live; training given months ahead is largely forgotten.

## 4. Curriculum

| Course | Audience | Module | Format | Duration (to estimate) | Prerequisites | Trainer | Materials | Scheduled |
|---|---|---|---|---|---|---|---|---|
| Navigating Dynamics 365 and personal settings | All users | All | Short video plus live Q&A | | Account and licence assigned | {{roles.trainer}} | Video, quick-reference guide | |
| Managing leads and opportunities | Salespeople | Sales | Instructor-led, hands-on | | Navigation course | {{roles.trainer}} | Exercises with sample data | |
| Working cases from queues | Service agents | Customer Service | Instructor-led, hands-on | | Navigation course | {{roles.trainer}} | Exercises, knowledge article guide | |
| Scheduling work orders | Dispatchers | Field Service | Instructor-led | | Navigation course | {{roles.trainer}} | Schedule board exercises | |
| Completing jobs on mobile | Technicians | Field Service | Hands-on with device | | Device enrolled | {{roles.trainer}} | Device guide | |
| Building journeys and segments | Marketing team | Marketing | Instructor-led | | Consent rules briefing | {{roles.trainer}} | Exercises | |
| Administration and support | Administrators, support team | All | Workshop and handover | | Environment access | {{roles.platform-administrator}} | Runbooks | |

## 5. Training environment and data

> Guidance: Name the training environment and how it is reset between sessions. Use realistic but non-personal data; agree any use of real customer data with the DPO or legal adviser ({{roles.data-protection-officer}}). Each trainee needs a user account with the same security role they will have in production.

## 6. Super-user network

> Guidance: List super users per team, the time released for them, their duties (testing, peer support, feedback) and how they meet with the project. Choose super users from those who volunteer or are nominated by their manager based on role coverage, not on any assessment of individuals.

| Team or location | Super user | Time released | Supported audience |
|---|---|---|---|
| | | | |

## 7. Communications plan

| When (relative to go-live) | Audience | Key message | Channel | Sender | Owner | Status |
|---|---|---|---|---|---|---|
| Initiate | All affected staff | Why we are changing and what will stay the same | Leadership briefing, intranet | {{roles.executive-sponsor}} | {{roles.change-lead}} | |
| During Implement | Affected teams | What the new process looks like; sprint demo highlights | Team meetings, short demo recordings | Process owners | {{roles.change-lead}} | |
| Before UAT | Testers and their managers | UAT dates, time needed, how to log defects | Email, calendar invitations | {{roles.test-manager}} | {{roles.change-lead}} | |
| Before training | All users | How to book training, what to bring | Email, Teams | {{roles.trainer}} | {{roles.change-lead}} | |
| Week before go-live | All users | Cutover dates, what to stop doing in the old system, where to get help | Email, team briefings | {{roles.executive-sponsor}} | {{roles.change-lead}} | |
| Go-live day | All users | We are live; hypercare contacts and channels | Email, Teams, floor walkers | {{roles.support-lead}} | {{roles.change-lead}} | |
| Hypercare | All users | Known issues, fixes released, tips | Weekly update | {{roles.support-lead}} | {{roles.change-lead}} | |

> Guidance: Avoid sending go-live communications during organisation change freezes or peak periods ({{constraints.change_freezes}}). Leaders should hear the message before their teams do.

## 8. Feedback and adoption measures

> Guidance: Define how feedback is gathered (surveys, super-user reports, support tickets) and which adoption measures are tracked at team level, such as active use of key processes. Report aggregated results only; do not use adoption data to assess individual performance.

## 9. After go-live

> Guidance: Plan refresher sessions, onboarding for new joiners, and communications for each release wave that changes the user interface or processes.

## 10. Approval

| Name | Role | Decision | Date |
|---|---|---|---|
| {{roles.change-lead}} | Change lead | | |
| {{roles.process-owner}} | Process owner | | |
| {{roles.executive-sponsor}} | Executive sponsor | | |

> Credit: Template from D365Forge by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/D365Forge), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
