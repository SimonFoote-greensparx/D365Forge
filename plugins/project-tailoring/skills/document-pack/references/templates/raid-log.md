---
id: raid-log
title: RAID log
format: xlsx
owner: programme-management:raid-log
tailored_from: organisation, estate, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# RAID log

## How to use this template

The project manager ({{roles.project-manager}}) owns this log from Strategize to project closure; anyone on the project may raise an entry. Review open items at every weekly project meeting and bring the highest-rated risks and any issue needing a decision to each steering meeting. Close items rather than deleting them, so the history is available for the lessons-learned review.

The log is pre-populated with risks, assumptions, issues and dependencies that recur on Dynamics 365 Customer Engagement projects, plus the known risks from the organisation profile. Keep the rows that apply, rewrite them in your own terms and delete the rest.

> Guidance: Write each risk as cause, event and effect ("Because..., there is a risk that..., which would..."). A risk without a named owner and a dated action is only a worry. When a risk happens, close it and raise an issue that references it.

> SMB: A single sheet reviewed weekly by the partner and the sponsor is enough. Do not drop the Dependencies sheet; on small projects, delays usually come from third parties such as the ERP vendor or the telephony provider.

> Enterprise only: Keep a log per workstream, roll the top items up to a programme log, and record design authority and security findings as linked decisions.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Generated on | {{generated_on}} |
| Rating scale | Likelihood and impact rated High, Medium or Low against definitions agreed by the steering group |
| Response types | Avoid, Reduce, Transfer, Accept |
| Status values | Open, In progress, Closed, Realised (risk became an issue) |

## Sheet: Risks

| ID | Risk (cause, event, effect) | Category | Module | Likelihood | Impact | Response | Mitigation actions | Owner | Review by | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Because data in {{estate.current_crm}} has not been cleansed in years, there is a risk that duplicates and incomplete records are migrated, which would undermine user trust at go-live | Data | All | Assess | Assess | Reduce | Profile source data in Initiate; agree cleansing rules and owners; run at least two mock migrations | {{roles.data-migration-lead}} | | Open |
| R02 | Because users ask for the old system's screens to be replicated, there is a risk of excessive customisation, which would raise build, test and upgrade cost | Scope | All | Assess | Assess | Avoid | Fit-to-standard workshops; design authority challenges every extension | {{roles.design-authority-lead}} | | Open |
| R03 | Because process owners keep full business-as-usual duties, there is a risk that design sign-off and UAT slip | Resource | All | Assess | Assess | Reduce | Agree release from day job in writing; book UAT dates early | {{roles.executive-sponsor}} | | Open |
| R04 | Because the integration with {{estate.erp}} depends on another team's capacity, there is a risk that interfaces are not ready for SIT | Integration | Sales, Field Service | Assess | Assess | Reduce | Agree interface contracts and dates in Initiate; build against stubs | {{roles.integration-lead}} | | Open |
| R05 | Because release wave updates change platform behaviour, there is a risk that customisations or integrations break after an update | Technical | All | Assess | Assess | Reduce | Test in early access on a sandbox; maintain a regression pack | {{roles.platform-administrator}} | | Open |
| R06 | Because licence requirements are not confirmed per role, there is a risk of unbudgeted cost or users lacking capability at go-live | Commercial | All | Assess | Assess | Reduce | Confirm with the Microsoft licensing guide or your partner before budget approval | {{roles.project-manager}} | | Open |
| R07 | Because marketing consent history is held inconsistently, there is a risk that contacts are emailed without a valid basis | Compliance | Marketing | Assess | Assess | Avoid | Map consent sources; agree treatment with the DPO or legal adviser before migration | {{roles.data-protection-officer}} | | Open |
| R08 | Known risks from the profile: {{constraints.known_risks}} | | | Assess | Assess | | | | | Open |

## Sheet: Assumptions

| ID | Assumption | Area | Impact if wrong | How it will be validated | Owner | Validate by | Status |
|---|---|---|---|---|---|---|---|
| A01 | Standard Dynamics 365 tables are used for accounts, contacts, leads, opportunities and cases wherever they fit | Design | Data model rework and extra cost | Confirmed in fit-to-standard and blueprint review | {{roles.solution-architect}} | End of Initiate | Open |
| A02 | Process owners and super users are available for workshops and UAT as declared in the resource plan | Resource | Delayed sign-off | Written agreement from line managers | {{roles.project-manager}} | End of Strategize | Open |
| A03 | Mailboxes in {{estate.email_and_calendar}} can be approved for server-side synchronisation | Technical | Email tracking unavailable at go-live | Test with pilot mailboxes in a sandbox | {{roles.platform-administrator}} | Mid Implement | Open |
| A04 | {{estate.current_crm}} becomes read-only after cutover and is archived later | Cutover | Dual running and data divergence | Agreed in the cutover plan | {{roles.process-owner}} | Prepare | Open |
| A05 | Partner {{constraints.partner}} provides named consultants for the full delivery period | Commercial | Loss of knowledge mid-project | Named resources in the statement of work | {{roles.project-manager}} | Contract signature | Open |

## Sheet: Issues

| ID | Issue | Raised by | Date raised | Impact | Priority | Action | Owner | Due | Status | Escalated to |
|---|---|---|---|---|---|---|---|---|---|---|
| I01 | Sandbox for SIT not yet provisioned | | | Blocks SIT start | High | Request environment and capacity check | {{roles.platform-administrator}} | | Open | |
| I02 | Duplicate accounts found in source extract | | | Delays mock migration | Medium | Agree matching rules with process owner | {{roles.data-migration-lead}} | | Open | |
| I03 | To-be process for case escalation not signed off | | | Blocks configuration of routing | High | Decision workshop with process owner | {{roles.business-analyst}} | | Open | |

## Sheet: Dependencies

| ID | Dependency | Direction | Provider | Needed for | Needed by | Owner | Status | Notes |
|---|---|---|---|---|---|---|---|---|
| D01 | ERP interface specification and test endpoint | Inbound | {{estate.erp}} team | Integration build and SIT | | {{roles.integration-lead}} | Open | |
| D02 | Security groups and licence assignment in Microsoft Entra ID | Inbound | IT identity team | Environment access, UAT | | {{roles.platform-administrator}} | Open | |
| D03 | DNS records for the marketing sending domain | Inbound | IT network team | Customer Insights - Journeys email sending | | {{roles.journeys-consultant}} | Open | Marketing only |
| D04 | Telephony connector or contact centre integration | Inbound | {{estate.telephony}} provider | Voice channel and screen pop | | {{roles.integration-lead}} | Open | Customer Service only |
| D05 | Release wave and organisation change freeze dates | Inbound | Microsoft, internal change board | Cutover date | | {{roles.project-manager}} | Open | {{constraints.change_freezes}} |
| D06 | Final process sign-off | Outbound | Project to business | Training material completion | | {{roles.change-lead}} | Open | |

## Sheet: Decisions

| ID | Decision | Options considered | Rationale | Decided by | Date | Design authority or security finding reference |
|---|---|---|---|---|---|---|
| DEC01 | Use standard opportunity process with configured business process flow rather than a custom table | Custom table; standard with configuration | Lower upgrade risk, uses standard forecasting | {{roles.design-authority-lead}} | | |
| DEC02 | Migrate open cases and closed cases from a defined cut-off period only | All history; open only; open plus recent | Balances service context with migration effort; retention agreed with DPO | {{roles.process-owner}} | | |
| DEC03 | | | | | | |
