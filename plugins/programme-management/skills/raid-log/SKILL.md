---
name: raid-log
description: Sets up and runs the risks, assumptions, issues and dependencies log for a Dynamics 365 CE programme, seeded with CRM-typical risks such as data quality, integration, key-user availability and licensing, with owners, scoring and escalation. Use when starting the log, preparing for steering, or deciding whether to escalate a risk.
license: CC-BY-4.0
metadata:
  department: programme-management
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# RAID log

On many CRM programmes the RAID log is written once at kick-off and then left alone. Risks are owned by the project rather than by a person, nobody updates the scores, and the issues that eventually derail go-live were sitting in the log as assumptions all along. The value of a RAID log comes from a short, live list with named owners and dated actions, reviewed on a fixed rhythm, with a clear threshold for escalation.

The good news is that CRM risks are predictable. Data quality, integration readiness, key-user availability and licensing appear on almost every Dynamics 365 programme, so the log should start seeded with them rather than waiting for them to happen.

## When to use

- At Initiate, to set up the log and its review rhythm.
- Before each steering committee, to decide what to escalate and what to ask for.
- When an assumption in the charter or statement of work turns out to be false.
- When a dependency on another team, vendor or programme is at risk.

Not this skill: `programme-management:governance-cadence` for the forums where RAID items are decided, `design-authority:change-impact-assessment` for assessing a proposed design change, `support-operations:incident-management` for live incidents after go-live.

## Questions to ask first

1. Who owns the log, and how often is it reviewed? An unowned log decays within weeks.
2. What threshold sends an item to the steering committee? Without one, either everything escalates or nothing does.
3. Does the organisation already have a risk scoring scale? Use it, so programme risks can roll into corporate risk reporting.
4. Which assumptions did the charter and statement of work rely on? Broken assumptions are the usual source of change requests.
5. Which external parties hold dependencies, such as the ERP team, telephony vendor, ISVs or Microsoft support? Their dates are outside the programme's control.

## Approach

Keep one register with four item types and a consistent set of fields: identifier, type, description, named owner, probability and impact on the organisation's scale, proximity, response, actions with dates, status, and links to the workstream and plan milestone. Write risks in cause, event and effect form ("because the legacy data has no enforced account hierarchy, migration may create duplicate accounts, which would undermine user trust at go-live") so the response targets the cause.

1. Seed the CRM-typical risks on day one and let workstream leads remove those that do not apply.
   - Data quality: duplicates, missing mandatory values and inconsistent option values in legacy data.
   - Integration: availability of the ERP or telephony team, unclear interface ownership, and Dataverse service protection limits (check current Microsoft Learn documentation for the values).
   - Key-user availability: business experts pulled back into day-to-day work, slowing decisions and testing.
   - Licensing and capacity: the wrong licence mix or storage capacity for the design; confirm with the Microsoft licensing guide or your partner.
   - Release waves: a platform update changing behaviour during build or UAT.
   - Over-customisation: requirements drifting towards pro-code without design authority approval.
   - Consent and data protection for marketing data, which needs the DPO's input.
2. Give every assumption a validation date and an owner. When it proves false, convert it to an issue or a risk the same week.
3. Record dependencies in both directions, with the other party's named contact and date.
4. Choose a response for every risk (avoid, reduce, transfer or accept) and make acceptance an explicit decision by the sponsor, not a default.
5. Review weekly in workstreams and roll up before each steering meeting. Take the top risks to steering with a specific ask, not just a status colour.
6. Close items only with evidence that the response worked, and keep closed items for audit.

Record key-user availability as a gap between planned demand and declared availability. The log is a programme document that many people read, so it must not contain judgements about named individuals.

## Outputs

- `raid-log` with seeded CRM risks, owners, scores, responses and actions.
- A top-risks summary with asks for each steering committee.
- An assumption validation schedule.
- A dependency map across teams, vendors and programmes.

## Scale notes

### SMB

A shared list maintained by the consultant or project manager is enough, reviewed with the sponsor every two weeks. Keep it short. Do not skip the data quality and key-user availability risks, because on small projects the same few people run the business and test the system.

### Enterprise

Each workstream keeps its own RAID log, rolling up into a programme log owned by the PMO and aligned to the corporate risk framework. Dependencies on ERP, identity and telephony programmes need cross-programme review. Risks that require a design change link to design authority decisions, and the full history is kept for audit.

## Hand-offs

- `programme-management:governance-cadence` takes escalated items to steering.
- `design-authority:change-impact-assessment` assesses mitigations that change the design.
- `integration-and-data:data-mapping-and-cleansing` owns responses to data quality risks.
- `platform-administration:licensing-and-capacity` owns licensing and capacity risks.
- `security-compliance:marketing-consent-compliance` and `security-compliance:data-retention` advise on data protection risks, alongside the DPO.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Record opinions about the performance, reliability or attitude of named individuals.
- Assign a risk to the project, a team or a partner instead of a named owner.
- Close a risk without evidence that the response worked.
- Downgrade a score to keep an item off the steering agenda.
