---
name: power-automate-patterns
description: Sets patterns for Power Automate cloud flows on Dataverse, covering triggers, error handling, connection references, environment variables, ownership and safe reruns, and when not to use a flow. Use when designing or reviewing flows, when flows fail silently, or when choosing between a flow and a plug-in for high-volume logic.
license: CC-BY-4.0
metadata:
  department: platform-engineering
  stages: Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Power Automate patterns

Cloud flows are the default automation tool on most Dynamics 365 CE projects because makers can build them quickly. That speed is also the risk. Flows built outside solutions, owned by whoever created them, with hard-coded URLs and no error handling, work in development and fail quietly in production.

The other recurring mistake is using flows for the wrong job. Dataverse-triggered cloud flows run asynchronously, so they cannot block a save or guarantee a value is set before the user sees the record, and they are a poor home for logic that runs on every save of a busy table.

## When to use

- Designing a new flow, or reviewing flows before they move to test or production.
- Standardising error handling, logging and ownership across a programme.
- Deciding whether a requirement belongs in a flow, a plug-in or an Azure service.
- Investigating flows that fail, run twice or run under a person who has left.

Not this skill: `platform-engineering:plugin-design` for synchronous or transactional server logic, `integration-and-data:integration-architecture` for system-to-system integration design, and `platform-administration:agent-governance` for DLP policies and maker governance.

## Questions to ask first

1. Must the outcome exist before the user's save completes? If so, a cloud flow is the wrong tool.
2. How many times a day will it run, and in what bursts? Volume drives trigger filtering, concurrency and the choice of tool.
3. Which connectors does it use, and does the DLP policy allow them together? A flow that breaks policy will not run in a governed environment.
4. Who owns it and its connections in production? Ownership by an individual is a support incident waiting to happen.
5. What happens if a run fails halfway? This decides retries, compensation and how reruns behave.

## Approach

1. Build inside solutions from the start. Every flow that will reach production lives in a solution, uses connection references for its connections and reads environment-specific values (URLs, record identifiers, recipients, thresholds) from environment variables. The deployment pipeline supplies those values per environment.
2. Trigger narrowly. Use the Dataverse trigger with the right change type, selected columns and a row filter so the flow wakes only when relevant data changes, and add trigger conditions where needed. A flow that fires on every save and then exits still consumes requests.
3. Handle errors explicitly. Put the main actions in a try scope, follow it with a catch scope configured to run after failure or time-out, and add a finally scope for clean-up. In the catch, log the run's details to a Dataverse error table or Application Insights and notify a monitored support queue. Set retry policies deliberately on actions that call external services.
4. Make runs safe to repeat. Flows get retried and resubmitted. Check whether the work has already been done before creating records or sending messages.
5. Keep flows small. Use child flows for reusable steps, limit apply-to-each loops over large sets, set concurrency deliberately and handle paging.
6. Own flows as a service. Production flows run under a service account or application user rather than a person, with connections created by the platform team. Check current Microsoft Learn documentation for which ownership models each connector supports.
7. Know when to step up. High-volume synchronous logic, validation that must block a save, heavy data transformation and near-instant responses belong in plug-ins, custom APIs, Azure Functions or Logic Apps instead.
8. Mind the cost. Premium connectors, per-flow or process licences and request limits all affect running cost; confirm with the Microsoft licensing guide or your partner.

## Outputs

- Flow standards for naming, error handling, logging and ownership, recorded in the `environment-and-alm-strategy`.
- A flow inventory with trigger, purpose, owner, connectors and expected volume.
- Environment variable and connection reference lists per solution, ready for deployment settings.
- An error log table or telemetry design handed to support.

## Scale notes

### SMB

Flows are often the main automation tool and may be built by a power user. Keep them simple, but do not skip solutions, a shared service account and a basic try and catch pattern with an alert. Those three prevent most production surprises.

### Enterprise

Publish templates for the standard patterns, require peer review before promotion, run solution checker and naming checks in the pipeline, and route every flow failure into central monitoring and the incident process. The design authority approves any flow on a high-volume table.

## Hand-offs

`platform-engineering:deployment-pipelines` supplies environment variables and connection references, `platform-administration:monitoring` takes flow failures into operations, and `platform-administration:agent-governance` confirms the DLP fit. Reviewer sign-off: `design-authority:standards-conformance`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use a cloud flow for validation that must block a record save.
- Leave production flows or their connections owned by an individual maker.
- Hard-code environment URLs, record identifiers or recipients in a flow.
- Build a flow destined for production outside a solution.
- Let a flow swallow errors without logging and alerting.
