---
name: statement-of-work
description: Structures a statement of work with a Dynamics 365 CE implementation partner, weighing fixed price against time and materials and defining deliverables, customer obligations, acceptance and change requests. Use when reviewing a partner proposal, drafting an SOW, or handling a disputed change request. Not legal advice.
license: CC-BY-4.0
metadata:
  department: programme-management
  stages: Strategize, Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Statement of work with a partner

The statement of work decides who carries which risk. On CRM programmes it usually goes wrong in three places. Scope is described as a list of modules ("implement Customer Service") rather than processes, deliverables and volumes. The assumptions section quietly places obligations on the customer, such as data quality, key-user time and decision turnaround, that nobody on the customer side has read. And acceptance is left vague, so every deliverable becomes a negotiation.

This skill structures the commercial and delivery questions so the organisation can negotiate from a clear position. It is not legal advice. Contractual terms, liability, intellectual property and data processing clauses go to the organisation's legal adviser and DPO.

## When to use

- When choosing a commercial model for a new Dynamics 365 engagement.
- When reviewing a partner's proposal or draft statement of work before signature.
- When a change request is disputed and the parties disagree on what was in scope.
- When moving from a discovery phase to a build phase under a new statement of work.

Not this skill: `programme-management:project-charter` for the internal business case, `programme-management:governance-cadence` for who approves changes, `platform-administration:licensing-and-capacity` for licence and capacity questions.

## Questions to ask first

1. How well understood is the scope? Fixed price only works after fit-to-standard has produced a fit-gap list; before that, it buys a large risk premium.
2. What is the customer team committing to provide, and has it declared that availability? Customer obligations are where most change requests start.
3. How will each deliverable be accepted, by whom, and within what period? Undefined acceptance is the root of most disputes.
4. Who owns data migration, integration endpoints, ISV products and licence procurement? Gaps between parties become nobody's job.
5. Who signs contracts for the organisation, and when will legal review happen? Late legal review compresses negotiation into days.

## Approach

1. Match the commercial model to the uncertainty.
   - Fixed price suits a defined scope backed by a fit-gap list and process maps. The partner prices the risk in, so expect tight assumptions and a firm change process.
   - Time and materials suits discovery and an evolving backlog. The customer carries the risk, so it needs strong backlog ownership, burn reporting and a cap or review point.
   - A hybrid is often the most honest model for CRM: a fixed-price or capped discovery phase through Initiate that produces the backlog, blueprint and plan, then a separate build statement of work priced on that evidence.
2. Describe scope as processes and deliverables. List in-scope processes with their map references, modules, user groups and approximate user numbers, integrations from the `integration-inventory`, data objects and volumes to migrate, environments, reports, and training deliverables. Attach the fit-gap register and write an explicit out-of-scope list.
3. Make assumptions and dependencies two-way. Customer obligations (key users at stated availability, decision turnaround, data extracts, test data, UAT testers) and partner obligations (named roles, continuity, environments, documentation) should each state what happens if they are not met.
4. Define acceptance per deliverable: criteria, review period, who signs and how defects are classified. Link build acceptance to story acceptance criteria and UAT exit criteria.
5. Set out the change request process: request form, impact assessment covering cost, date, design, test and training, approval thresholds aligned to programme governance, and the rate card for change.
6. Tie fixed-price payment milestones to accepted deliverables rather than to dates.
7. Cover warranty, hypercare and handover: the defect correction period after go-live, the hypercare team and duration, and the transition to the support model.
8. Record the licence position, including who procures and when, and confirm with the Microsoft licensing guide or your partner.
9. List the questions for the legal adviser (liability, intellectual property, termination, any deemed-acceptance wording) and for the DPO (data processing terms, sub-processors, data location).

## Outputs

- A statement of work checklist and annotated review of the partner draft.
- A scope schedule built from processes, deliverables and the fit-gap register.
- A two-way assumptions and dependencies schedule.
- Acceptance and change request procedures.
- A question list for the legal adviser and DPO, and inputs to the `delivery-plan` and `raid-log`.

## Scale notes

### SMB

The partner's standard template or a packaged fixed-price offer is common. Read what the package excludes, especially data migration, integrations and training, and check the customer obligations against the one or two people who will actually do them. Keep legal review even when the contract is small.

### Enterprise

Expect a master services agreement with separate statements of work per phase, procurement involvement, and several partners (CRM, integration, ERP, managed service). Build a responsibilities matrix across partners, run commercial governance alongside steering, and ensure change requests flow through the programme's change control, not only the partner's.

## Hand-offs

- `business-analysis:fit-gap-analysis` and `business-analysis:process-mapping` supply the scope basis.
- `programme-management:delivery-plan` and `programme-management:raid-log` absorb milestones, assumptions and dependencies.
- `programme-management:governance-cadence` runs change control after signature.
- `support-operations:hypercare` and `support-operations:support-model` pick up warranty and handover terms.
- Contractual and legal matters go to the organisation's legal adviser; data processing terms go to the DPO.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Present this guidance as legal advice or recommend signing on its basis; contractual questions go to the organisation's legal adviser.
- Agree a fixed price for scope that has not been through fit-to-standard.
- Leave acceptance criteria to be agreed later.
- Commit the customer team to availability it has not declared.
