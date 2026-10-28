---
name: work-order-design
description: Designs the Field Service work order lifecycle, covering work order types, priorities, system statuses and substatuses, booking statuses, creation routes including case conversion, and completion, review and posting. Use when shaping how jobs flow from request to invoice or mapping legacy job statuses onto Field Service.
license: CC-BY-4.0
metadata:
  department: field-service
  stages: Initiate, Implement
  modules: Field Service, Customer Service
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Work order design

The work order is the job itself: what needs doing, where, for whom, by when, and what was used to do it. Scheduling, the mobile app, inventory, billing and service history all hang off it, so its lifecycle has to be clear to dispatchers, technicians and the back office alike.

Projects usually go wrong by fighting the standard model. Teams replace system statuses with their own, confuse the work order status with the booking status, create a work order type for every product line, and leave the difference between completed and posted undefined. The billing integration then surprises everyone, because nobody agreed which system raises the invoice.

## When to use

- Mapping the job journey from request through scheduling and completion to billing.
- Defining work order types, priorities and substatuses.
- Mapping legacy job statuses onto system statuses and substatuses.
- Designing how work orders are created, including from cases and agreements.
- Agreeing completion, review and posting, and what posting triggers downstream.

Not this skill: `field-service:incident-types-and-service-tasks` for the content of a job, `field-service:schedule-board-setup` for resources and dispatch, `field-service:agreements-and-recurring-work` for generated recurring jobs, `customer-service:case-lifecycle-design` for the case side of a case to work order conversion.

## Questions to ask first

1. How do jobs originate: cases, agreements, sales orders, monitoring alerts or phone calls? Each route needs its own mandatory data and owner.
2. Which kinds of work differ in process, billing or data, such as break-fix, installation or inspection? These become work order types.
3. Who confirms a job is complete, and who approves it for billing? This separates Completed from Posted.
4. Which system raises invoices, Dynamics 365 or ERP? This decides what posting does and how billing integrates.
5. Do jobs need several visits, crews or more than one technician? This shapes requirements and booking design.

## Approach

Work orders carry a fixed set of system statuses (Unscheduled, Scheduled, In Progress, Completed, Posted and Cancelled) that drive Field Service logic, and bookings carry their own statuses that roll up to the work order. Design within this model: put business detail in substatuses and never rename or repurpose the system statuses.

1. Map the job journey. Walk real jobs from request to invoice and mark each step against the system statuses. Note what the dispatcher, technician, back office and customer see and do at each step.

2. Define work order types that change something. A type earns its place if it changes the price list or billing approach, whether an incident type is required, default duration or reporting. Installation, break-fix, inspection and preventive maintenance are common; resist one type per product line.

3. Use substatuses for business detail. Map each legacy job status to a system status plus a substatus, such as Scheduled with an awaiting-parts substatus. This mapping also drives the migration of open jobs in the `data-migration-mapping`.

4. Separate booking from work order status. Technicians update the booking on the mobile app (travelling, in progress, completed) and the work order follows. Add custom booking statuses only where dispatch needs them, each mapped to a Field Service status.

5. Set priorities and promised windows. Keep a short list of priorities with clear scheduling meaning, and decide whether customers are given time windows or promised arrival times. These feed `field-service:schedule-board-setup` and `field-service:scheduling-optimisation`.

6. Design creation routes. For case to work order, agree with `customer-service:case-lifecycle-design` which fields map across (account, contact, asset, incident type, priority, description), who converts, and whether the case stays open until the job completes.

7. Define completion, review and posting. Completed means the field work is done; Posted means the back office has reviewed products, services and time and approved them for billing. Decide who reviews, what they check and what posting triggers. If ERP raises invoices, design the hand-over with `integration-and-data:erp-and-project-touchpoints` and do not run in-app invoicing for the same jobs.

8. Capture what reporting needs. Make sure resolution, time and parts used are recorded as data on the job, not hidden in free-text notes.

## Outputs

- Work order lifecycle model, status and substatus map and booking status map in the `solution-blueprint`.
- Work order type and priority catalogue.
- Legacy job status mapping for open jobs in the `data-migration-mapping`.
- Case to work order field mapping, agreed with Customer Service.
- Posting-to-billing interface in the `integration-inventory`.
- End-to-end job scenarios in `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

One or two work order types, a few substatuses and a single dispatcher usually suffice. Posting may be a simple office check before invoicing in the accounting system. Do not skip the legacy status map or the written rule separating completed from posted.

### Enterprise

Expect several service lines and regions, ERP billing, contractor technicians, multi-visit and crew jobs. Hold one shared work order model with controlled regional variations, put types and substatuses under change control, and agree posting rules with finance so revenue and cost recognition match the ERP.

## Hand-offs

- `field-service:incident-types-and-service-tasks` defines what each job contains.
- `field-service:schedule-board-setup` takes priorities and promised windows into dispatch.
- `integration-and-data:erp-and-project-touchpoints` designs the posting-to-billing integration.
- Reviewer sign-off: `design-authority:design-review` for the lifecycle model, and `design-authority:customisation-challenge` for any custom status logic.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Rename, repurpose or bypass the work order system statuses.
- Create a work order type for every product, customer or region.
- Invoice the same jobs from both Field Service and ERP.
- Let work orders be completed without recorded parts, time and resolution.
