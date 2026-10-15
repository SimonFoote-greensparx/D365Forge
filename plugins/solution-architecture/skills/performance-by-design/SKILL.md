---
name: performance-by-design
description: Builds performance into the Dynamics 365 CE design before testing starts, covering form load, plug-in execution, service protection and request limits, integration throughput and large data volumes. Use when designing busy forms, high-volume tables or integrations, or when production slowness points to a design cause.
metadata:
  department: solution-architecture
  stages: Initiate, Implement, Prepare
  modules: All
  status: draft
---

# Performance by design

Performance problems in Dynamics 365 CE are almost always designed in. A case form with a dozen subgrids, a synchronous plug-in that calls an external service, an integration that hammers the Web API without retry logic, or an activity table that grows without an archival plan will each behave acceptably in a lightly used test environment and badly a few months after go-live.

Performance testing finds these problems late, when fixing them means redesign. This skill puts the questions on the table during design, while the cheapest fix is still available, and gives the performance tests something agreed to measure against.

## When to use

- Designing forms for high-use roles such as service agents, dispatchers or inside sales.
- Designing tables expected to hold very large volumes, such as activities, cases, bookings or telemetry.
- Designing integrations or batch jobs that move significant data in and out of Dataverse.
- Investigating slowness in production where the cause looks structural rather than a one-off.

Not this skill: `testing-quality:performance-testing` to plan and run load tests, `platform-engineering:plugin-design` for plug-in code detail, and `platform-administration:monitoring` for production telemetry and alerting.

## Questions to ask first

1. How many users work concurrently at peak, and where are they relative to the environment's region? Latency and concurrency shape both form and integration design.
2. How many rows will each major table hold at go-live and after several years? Growth decides indexing, archival and whether a standard table is the right home.
3. What are the integration volumes and peak windows? Batch loads and real-time feeds compete with users for the same limits.
4. Which screens do high-volume roles use all day? These deserve an agreed performance budget.
5. Do mobile or field users work on weak networks? This affects offline profiles and payload size.

## Approach

Agree performance budgets with the business for the critical scenarios (opening a case, saving an opportunity, loading the schedule board, syncing a technician's device), then design each layer to fit them. Do not invent targets on the business's behalf; agree them and record them in the blueprint.

### Forms and client

Load only what the user needs when the form opens. Put subgrids, quick view forms and timeline-heavy content in tabs that load when opened, keep onLoad scripts short and asynchronous, and avoid synchronous web requests. A few purposeful forms per role beat one form with every column. Use the Monitor tool in Power Apps to see what a form actually does.

### Server-side logic

Keep synchronous plug-ins lean: filtering attributes, minimal images, no external calls inside the transaction unless unavoidable, and asynchronous steps for anything the user does not need to see at once. Watch for chains where one save triggers several plug-ins and flows in turn.

### API limits and integrations

Service protection limits apply to every caller, and licence-based request entitlements sit alongside them. Design integrations to honour retry-after responses, use batch and bulk operations, and schedule heavy loads outside business hours. Check current Microsoft Learn documentation for the limits that apply; for request entitlements, confirm with the Microsoft licensing guide or your partner.

### Large data volumes

Plan retention and archival when a table is designed, not when it is full. Filter high-volume views on indexed columns, avoid leading wildcards and deep chains of linked tables, and keep audit scope deliberate. For very high-volume, append-heavy data, assess whether a standard table, an elastic table or a store outside Dataverse fits best, checking current documentation for elastic table behaviour. Keep large files in file columns or document management rather than notes where volumes are high.

### Security model

Heavy use of individual record sharing and very deep business unit hierarchies slow queries for every user. At scale, favour ownership and team-based access over individual shares.

Feed every budget and volume assumption into the performance test plan, and carry the same measures into production monitoring.

## Outputs

- Performance chapter of the `solution-blueprint`, including agreed budgets for the critical scenarios.
- A volume model per major table with growth, retention and archival assumptions.
- Integration load profiles recorded in the `integration-inventory`.
- Performance scenarios and targets for the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

Most SMB projects will not approach platform limits, so concentrate on forms and plug-ins, which is where small teams usually create problems. Still check integration retry handling and set an archival intent for activities and attachments. A short design checklist reviewed once per release is enough.

### Enterprise

The solution architect owns performance, with a named lead in each workstream. Include performance in every design authority review, run a dedicated performance environment and baseline key scenarios each release so regressions are visible. Large data migrations need their own throughput design and rehearsal.

## Hand-offs

`testing-quality:performance-testing` turns the budgets into tests, `platform-engineering:plugin-design` applies the server-side rules, `integration-and-data:integration-architecture` designs throughput, and `platform-administration:monitoring` carries the measures into production. Sign-off comes from `design-authority:design-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Call an external system synchronously from a high-volume plug-in step without a timeout and a failure path.
- Treat service protection limits as something to work around rather than design for.
- Rely on individual record sharing as the main access model at scale.
- Leave archival and retention design until production volumes cause problems.
- Load every subgrid, quick view and script when a form opens.
