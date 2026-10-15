---
name: slas-and-entitlements
description: Designs service level agreements and entitlements in Dynamics 365 Customer Service, covering SLA KPIs, applicable and success conditions, business hours, pause rules, warning and failure actions, and entitlement terms. Use when turning contract commitments into timers or deciding what support a customer is owed.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Initiate, Implement, Operate
  modules: Customer Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# SLAs and entitlements

SLAs are where a commercial promise becomes a timer an agent can see. They drive escalations, supervisor attention, customer communication and, in many contracts, service credits, so a badly built SLA is both an operational and a commercial problem. Entitlements answer a related question: what support this customer has actually bought.

Projects usually go wrong by configuring SLAs straight from contract wording without agreeing exactly what starts, pauses and stops each clock. Business hours and holidays are set up late or for the wrong region, pause statuses multiply until breach figures mean nothing, and warning emails go to everyone and are ignored by all. Entitlements are often configured because they exist, then left unchecked by agents and unrenewed by anyone.

## When to use

- Translating contract or policy commitments into SLA KPIs and targets.
- Defining applicable and success conditions, business hours, holiday schedules and time zones.
- Deciding which status reasons pause and resume timers.
- Designing warning and failure actions and who acts on them.
- Deciding whether to use entitlements, and designing allocation, channels and renewal.

Not this skill: `customer-service:case-lifecycle-design` for the status model itself, `customer-service:queues-and-routing` for escalation queues and assignment, `customer-service:service-analytics` for SLA compliance reporting, `field-service:agreements-and-recurring-work` for contracted site visits.

## Questions to ask first

1. What exactly is promised, to whom, and where is it written? Contractual SLAs, internal targets and aspirations need different treatment, and only the first is customer-visible.
2. What event starts, pauses and stops each clock? Without exact events the KPI cannot be built, tested or defended in a dispute.
3. Which business hours, holidays and time zone apply to each customer group? Calendars drive every deadline and are the most common cause of disputed breaches.
4. How is a customer's support allowance decided: contract, product, tier, number of cases or hours? This decides whether entitlements earn their place.
5. What should happen at warning and at breach, and who will act? Actions without an owner are just noise.

## Approach

Treat SLA design as translation, from contract language into precise and testable events. Build SLAs with SLA KPIs in the current model managed through the Customer Service admin center. Older SLA types are deprecated or being retired; if you inherit them, check current Microsoft Learn documentation and plan a migration rather than extending them.

### SLAs

1. Build a KPI catalogue first. List each measure (typically first response and resolution, sometimes update frequency or callback), the event that starts it, the event that satisfies it, and the target per priority or tier. Each measure becomes an SLA KPI, and the target matrix becomes SLA items.

2. Write conditions in plain language before configuring. Applicable conditions choose which SLA item applies (priority, case type, customer tier); success conditions decide when the KPI is met. Base them on stable fields. If priority can change mid-case, decide whether the target recalculates and test it.

3. Get time right. Define customer service schedules and holiday calendars per region, and decide whose time zone governs the deadline. A round-the-clock premium tier and a business-hours standard tier need separate schedules. Test deadlines across weekends, public holidays and clock changes.

4. Pause sparingly and visibly. Pause and resume are driven by status reasons, set organisation-wide in the service configuration settings or, where supported, per SLA KPI (check current Microsoft Learn documentation), so this step depends on the status reason matrix from `customer-service:case-lifecycle-design`. Pause only for genuine waits outside the organisation's control, confirm the contract allows it, and make sure the customer is told when the clock stops.

5. Give every action an owner. Warning and failure actions run as Power Automate flows: notify the owner, alert a team lead, raise priority or move the case to an escalation queue. Each action needs a named recipient role and a reason someone will act on it.

6. Make it visible and auditable. Show the SLA timer on the case form, keep the SLA KPI instance records for reporting, and agree whether a breach can be waived, by whom, and with what recorded reason.

### Entitlements

7. Decide whether entitlements earn their place. They record what a customer may receive, by number of cases or hours, through which channels and for which products, and can carry a specific SLA. They pay off when support is sold in packages or out-of-entitlement work must be refused or charged. If every customer gets the same service, a default SLA by tier is simpler.

8. If you use them, design the operation. Decide whether allocation decreases on case creation or resolution, who creates and renews entitlements, how a default entitlement applies, whether case creation is restricted once terms run out, and exactly what an agent does when an entitlement is exhausted.

Finally, settle how in-flight cases are treated at cutover: migrated open cases need a clear rule on whether timers start fresh or honour original dates.

## Outputs

- SLA KPI catalogue and target matrix by priority and tier, in the `solution-blueprint`.
- Business hours, holiday calendar and time zone definitions by region.
- Pause matrix linking status reasons to timer behaviour.
- Warning and failure action design with an owner for each action.
- Entitlement model (allocation, channels, products, renewal, exhausted-entitlement procedure), or a recorded decision not to use entitlements.
- SLA test scenarios across weekends, holidays and priority changes in `test-strategy-and-uat-scripts`.
- Cutover rule for timers on migrated open cases in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

One or two SLAs, first response and resolution KPIs, and one business-hours calendar usually cover it. Skip entitlements unless support is sold in packages. Do not skip writing down the start, pause and stop events, loading the holiday calendar, or testing a deadline that crosses a weekend.

### Enterprise

SLAs are often contractual and multi-region, so involve the commercial owner of each contract and keep the KPI catalogue under change control. Expect regional calendars, several tiers and service credits, and design reporting of SLA compliance by contract from the start. Changes to live SLAs affect customers and open cases, so route them through design authority, and check timer and flow load at volume with `solution-architecture:performance-by-design`.

## Hand-offs

- `customer-service:service-analytics` builds SLA compliance and breach reporting.
- `platform-engineering:power-automate-patterns` builds and hardens the warning and failure flows.
- `integration-and-data:migration-strategy` applies the cutover rule for open cases.
- Reviewer sign-off: `design-authority:design-review` for the SLA and entitlement design, and `design-authority:change-impact-assessment` for any change to a live SLA.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Configure an SLA from contract wording without written start, pause and stop events.
- Add pause statuses to improve breach figures.
- Build new SLAs on deprecated SLA types.
- Send warning or failure notifications to a distribution list with no owner who acts.
- Promise customers targets that have not been tested against real rosters and business hours.
