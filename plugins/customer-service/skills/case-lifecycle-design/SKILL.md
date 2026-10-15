---
name: case-lifecycle-design
description: Designs the Dynamics 365 case lifecycle, covering case types and categories, status reasons, resolution and reopening, parent and child cases, merging and business process flows. Use when deciding how a case moves from creation to closure, rationalising legacy statuses, or choosing between child cases and linked cases.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Initiate, Implement, Operate
  modules: Customer Service, Field Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Case lifecycle design

The case is the spine of a Customer Service implementation. Queues, SLAs, email-to-case, Copilot summaries, analytics and the hand-off to Field Service all read the case record and its status, so a muddled lifecycle quietly breaks everything built on top of it. When the lifecycle is right, routing and SLAs become configuration; when it is wrong, they become workarounds.

Projects usually go wrong in three ways. They carry the legacy system's long list of statuses straight into status reasons, so nobody can say which ones stop the SLA clock. They model every variation of request as a separate case type with its own form and process flow, multiplying build and test effort. And they never write down what resolved means or when a reply reopens a case, so reports count the same customer problem several times.

## When to use

- Defining case types or categories and what genuinely distinguishes them.
- Rationalising status reasons under the Active, Resolved and Cancelled states and agreeing what each one triggers.
- Agreeing resolution, cancellation and reopen rules.
- Deciding when to use parent and child cases, linked cases or merging.
- Shaping the case business process flow and the point where a case converts to a work order.

Not this skill: `customer-service:queues-and-routing` for who receives the case, `customer-service:slas-and-entitlements` for timers and entitlements, `customer-service:email-to-case` for how inbound email creates and updates cases, `field-service:work-order-design` for the work order once a case converts.

## Questions to ask first

1. What kinds of request does the service desk handle, and which genuinely differ in data, process or ownership? This decides whether you need several case types or one case with a category.
2. Which waiting states must be told apart by the customer, the agent and the SLA? Status reasons should exist to drive behaviour, not to describe every nuance.
3. What counts as resolved, who confirms it, and for how long can a customer reopen it? This fixes repeat-contact reporting and the email-to-case reopen rule.
4. Does one problem ever spawn coordinated work across teams or many customers, such as an outage? This decides whether parent and child cases are needed.
5. Do cases lead to site visits, returns or billing? This decides the conversion points and which fields must be complete before conversion.

## Approach

Start from standard. The case table with its three states, the case resolution record, parent and child case settings and the merge capability cover most service operations; the design work is choosing values and rules, not building new mechanics. Run the design through `business-analysis:fit-to-standard` workshops using real cases from the last few weeks, not invented ones.

1. Classify before you split. Use a short case type list or a category field (the subject tree, a custom category, or both) to drive routing and reporting. Give a type its own form or process flow only when the data captured or the stages genuinely differ. Most organisations need one main case form with conditional sections.

2. Design status reasons for behaviour. Build a status reason matrix: for each value, record whether it pauses the SLA, moves the case to another queue, notifies the customer or blocks resolution. If a value triggers nothing and no report uses it, drop it. Keep waiting on customer and waiting on third party separate, because their pause rules and follow-up automation usually differ.

3. Define resolution and cancellation. Decide the mandatory resolution data (resolution category, root cause where useful, a customer-facing summary) and whether open activities block resolution. Cancellation needs a reason too, otherwise it becomes a quiet way to hide breaches.

4. Write the reopen rule. A common pattern is to reactivate a resolved case if the customer replies within an agreed window, and otherwise raise a new case linked to the old one. Email-to-case, portals, Copilot and analytics all depend on this rule, so record it once and reuse it everywhere.

5. Use parent and child cases deliberately. They suit major incidents and multi-team work. Configure which fields children inherit and the closure rule (close children with the parent, or prevent parent closure while children are open) in the case settings, and test both. Use merge only for true duplicates and agree who may merge, since merged cases are cancelled.

6. Keep the business process flow short. A handful of stages, such as identify, research and resolve, with only the fields that gate progress. A flow that mirrors every status reason becomes a click tax. Check whether Copilot or agent features in scope read the standard case fields before customising them.

7. Plan the conversion points. For case to work order, agree which fields map across (account, contact, asset, incident type, priority), who converts, and whether the case stays open until the work order completes. Do the same for complaints, returns and escalations to product teams.

8. Prove it with scenarios. Walk real cases end to end, including a reopen, a merge, a parent with children and a cancellation, recording the expected status, SLA state and queue at each step. These walkthroughs become UAT scripts.

## Outputs

- Case lifecycle model (types or categories, states, status reasons, resolution, cancellation and reopen rules) in the `solution-blueprint`.
- Status reason matrix showing each value's effect on SLA, queue, notifications and resolution.
- Parent, child and merge rules, including who may perform each action.
- Business process flow stages with their gating fields.
- Case to work order field mapping, agreed with Field Service.
- Legacy status mapping for open cases, and where legacy ticket references that customers quote are kept, in the `data-migration-mapping`.
- End-to-end case scenarios in `test-strategy-and-uat-scripts`.
- Agent guidance on statuses and resolution in the `training-and-communications-plan`.

## Scale notes

### SMB

One consultant usually designs the lifecycle with the service manager in two or three workshops. Use a single case form, the standard process flow lightly adjusted and a short list of status reasons. Do not skip the status reason matrix or the written reopen rule; they are what keep SLAs and reports honest after go-live.

### Enterprise

Each service line will want its own lifecycle. The Customer Service workstream lead should own one shared model with controlled variations, and changes to states, status reasons or resolution categories go through design authority. Agree a common resolution taxonomy across business units so cross-line reporting works, align the case with the wider data model through `solution-architecture:cross-module-data-model`, and plan retention and archiving of closed cases early with `security-compliance:data-retention`.

## Hand-offs

- `customer-service:queues-and-routing` and `customer-service:slas-and-entitlements` build directly on the status model.
- `field-service:work-order-design` takes the case to work order mapping.
- `business-analysis:user-stories` turns the model into backlog items, and `testing-quality:user-acceptance-testing` uses the scenarios.
- Reviewer sign-off: `design-authority:design-review` for the lifecycle model, and `design-authority:customisation-challenge` for any custom case table, extra forms per type or custom status logic.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Copy the legacy status list into status reasons without mapping each value to a behaviour.
- Replace the standard case table with a custom table to model cases.
- Allow cases to be resolved or cancelled without a recorded reason.
- Delete cases to tidy queues or reports.
- Add a business process flow stage for every status reason.
