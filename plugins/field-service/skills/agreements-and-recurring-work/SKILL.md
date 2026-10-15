---
name: agreements-and-recurring-work
description: Designs Field Service agreements for contracted and recurring work, covering booking setups and recurrence, generated work orders and bookings, agreement incidents, products and tasks, invoice setups, lifecycle and renewals. Use when contracts promise scheduled visits, preventive maintenance or recurring billing.
license: CC-BY-4.0
metadata:
  department: field-service
  stages: Initiate, Implement, Operate
  modules: Field Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Agreements and recurring work

Agreements turn service contracts into generated work. They are how a promise of quarterly inspections or an annual service becomes work orders on the right dates, with the right tasks and parts, against the right assets. When they work, recurring revenue and recurring work stay in step.

Projects usually go wrong on timing and money. Agreements generate work orders too far ahead and fill the schedule board with work that will change, or migration creates a backlog of past-dated jobs on day one. Contracts are billed both from agreements and from ERP, and renewals depend on someone remembering.

## When to use

- Mapping service contracts onto agreements and booking setups.
- Designing recurrence, generation timing and automatic bookings.
- Deciding whether agreements raise invoices or ERP bills contracts.
- Defining the agreement lifecycle, mid-term changes and renewals.
- Migrating live contracts without creating backlogs.

Not this skill: `field-service:customer-assets-and-maintenance` for the asset model that maintenance protects, `customer-service:slas-and-entitlements` for reactive support entitlements and SLAs, `integration-and-data:erp-and-project-touchpoints` for contract billing integration.

## Questions to ask first

1. What do contracts promise: visit frequency, tasks, included parts, response times? This defines agreement content.
2. How far ahead must work be visible for planning and parts? This sets generation timing.
3. Should bookings be created automatically or left to dispatch? This depends on how fixed the visits and technicians are.
4. Which system bills contracts? This decides whether invoice setups are used at all.
5. How are agreements renewed, changed mid-term or cancelled? Lifecycle rules prevent orphaned or duplicated work.

## Approach

An agreement holds the commercial terms (service account, price list, dates and status) and one or more booking setups that generate work orders on a recurrence, plus optional invoice setups that generate recurring invoices. Agreements are long-established in Field Service; design them around how contracts are sold and delivered.

1. Map contracts to agreements. Decide whether an agreement represents a contract, a site or a group of assets. One agreement per contract is usually easiest to bill and renew, with several booking setups for different visit types or sites.

2. Design booking setups. Each booking setup defines the recurrence, work order type, priority and the incident types, products, services and tasks to include. Link setups to customer assets where maintenance is asset-specific, so history builds on the asset.

3. Choose generation timing. Work orders are generated a set number of days ahead, and bookings can be created automatically or left for dispatch. Generate far enough ahead for planning and parts, not so far that the board fills with work that will move. Automatic bookings suit fixed-route, fixed-technician visits; leave flexible visits to dispatchers or optimisation.

4. Decide billing. Invoice setups generate recurring invoices in Dynamics 365. If ERP bills contracts, use agreements for service delivery only and pass contract information to ERP through `integration-and-data:erp-and-project-touchpoints`.

5. Define the lifecycle. Agreements move from estimate to active and then expire or are cancelled. Agree who activates, how mid-term changes are made, what happens to already generated work orders on cancellation, and how renewals are prompted before expiry.

6. Align with reactive service. If the contract also covers reactive support, align entitlements and SLAs with the agreement so agents and dispatchers see one consistent picture of what the customer has bought.

7. Migrate live contracts carefully. Set start dates and the next due visit so generation does not create past-dated work orders on day one, and rehearse the load in mock migrations.

Test generation with time-shifted data: confirm the right work orders appear on the right dates across month ends, leap years and public holidays.

## Outputs

- Contract to agreement mapping and agreement model in the `solution-blueprint`.
- Booking setup and invoice setup standards.
- Live contract migration rules, including next due dates, in the `data-migration-mapping`.
- Generation test scenarios in `test-strategy-and-uat-scripts`.
- Renewal process with an owner and reminder lead time.
- Treatment of in-flight contracts in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

One agreement per contract with simple recurrences is usually enough, and invoices often stay in the accounting system. Do not skip testing generation dates or setting next due visits when migrating contracts.

### Enterprise

Expect large contract portfolios with price escalation, multi-site agreements, ERP contract billing and generation jobs that need monitoring. Put agreement templates and generation settings under change control, and monitor that generation runs completed as expected.

## Hand-offs

- `field-service:customer-assets-and-maintenance` for asset-linked maintenance.
- `field-service:scheduling-optimisation` where generated work is scheduled automatically.
- `integration-and-data:mock-migrations` to rehearse loading live contracts.
- Reviewer sign-off: `design-authority:design-review` for the agreement and billing design.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Generate work orders so far ahead that the schedule board fills with work that will change.
- Bill the same contract through both agreement invoices and ERP.
- Migrate live contracts without setting next due dates.
- Leave renewals without an owner or a reminder.
