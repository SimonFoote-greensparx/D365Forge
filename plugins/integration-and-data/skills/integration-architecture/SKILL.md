---
name: integration-architecture
description: Designs how Dynamics 365 CE exchanges data with other systems, choosing the pattern, timing, identity and error handling for each interface. Use when building the integration inventory, choosing between Power Automate, Logic Apps, Service Bus, Functions or virtual tables, deciding sync or async, or planning retries, throttling and monitoring.
metadata:
  department: integration-and-data
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
---

# Integration architecture

Integrations are where CRM programmes quietly lose their schedule. Each interface looks small in a workshop, then turns out to need an owner on the other side, a test environment that does not exist yet, and an answer to what happens when the far end is down overnight. The usual failure is choosing the tool first (often whatever the team already knows) and discovering the volume, latency and error-handling needs after build.

The second failure is treating Dataverse like a database you can write to as fast as you like. It is a governed service with service protection limits, a security model and business logic that runs on every write. An integration that ignores those works in test and fails at month end.

## When to use

- Building or reviewing the inventory of interfaces in and out of Dataverse.
- Choosing a pattern and technology per interface, including whether it needs to be real-time at all.
- Designing identity, idempotency, retry, dead-lettering, replay and monitoring.
- Investigating throttling, duplicate records or silent failures caused by an integration.

Not this skill: `integration-and-data:erp-and-project-touchpoints` for what crosses the ERP boundary, `platform-engineering:power-automate-patterns` for building individual flows, `platform-engineering:plugin-design` for server-side logic inside Dataverse, `integration-and-data:migration-strategy` for one-off historic loads.

## Questions to ask first

1. Which system masters each shared entity and field, and is that agreed in writing? Two masters for one field is the root of most synchronisation defects.
2. What latency does the business actually need for each flow? Requests for real-time usually mean "before the user next looks", which is a different design.
3. What are the peak volumes and when do they occur (batch windows, month end, campaign sends)? Peaks decide tooling and whether service protection limits will bite.
4. What can the other system offer: an API, events, files, or only a database view? Its capabilities constrain the pattern more than Dataverse does.
5. Who supports each interface after go-live, and with what tooling? An interface without a named owner fails silently.

## Approach

Start with an inventory, not a diagram. For every interface record the source, target, tables, direction, trigger, frequency, peak volume, latency need, master system, owner on both sides and the business consequence of failure. This becomes the `integration-inventory`, and every later decision hangs off it.

Then choose a pattern per interface, defaulting to asynchronous:

1. Synchronous request-reply only when a user is waiting and cannot proceed without the answer, such as a credit check at order submission. Keep the outbound call out of long Dataverse transactions where possible, and design what the user sees when the far end times out.
2. Event-driven asynchronous for most outbound changes. Register a service endpoint so Dataverse posts the change to Azure Service Bus (queue or topic) or to a webhook, and let Azure Functions or Azure Logic Apps transform and deliver it. Users are then decoupled from the other system's availability.
3. Scheduled batch for high-volume, latency-tolerant feeds. Use Dataverse change tracking to pull only deltas, and bulk operations through the Dataverse Web API or the SDK for .NET rather than one request per row.
4. Virtual tables when users need to see external data in context but Dataverse does not need to own it, such as invoice history or stock levels. Check current Microsoft Learn documentation for provider options and the limits on query and write.
5. Power Automate for low-volume, business-owned flows. It is a sound choice for many interfaces, provided it runs in a solution, under a service principal or service account connection, with explicit error branches.

Design for failure on every interface. Make inbound writes idempotent by upserting on an alternate key that carries the source system's identifier, so a replayed message cannot create a duplicate. Retry transient errors with exponential backoff that honours the Retry-After value Dataverse returns when service protection limits are reached; check current Microsoft Learn documentation for the limit values rather than quoting them from memory. Route messages that keep failing to a dead-letter queue with enough context to replay them, and give a named team the job of draining it.

Authenticate each system integration as its own application user, backed by a Microsoft Entra app registration and a least-privilege security role. Never use a named person's account, and avoid one identity shared by every interface, because you lose both auditability and the ability to switch one off.

Decide monitoring before build: a correlation ID carried end to end, alerts on failure rates and dead-letter depth in Application Insights or Azure Monitor, and a daily count reconciliation for the interfaces the business cannot live without.

## Outputs

- `integration-inventory` with pattern, technology, master system, latency, volume and owner per interface.
- Pattern decisions and their reasons recorded in the `solution-blueprint`.
- Error-handling standard covering idempotency keys, retry policy, dead-letter handling and replay.
- Identity design listing application users and security roles per integration.
- Monitoring and alerting specification for operations.
- Integration risks and dependencies, such as other-system test environments and change windows, in the `raid-log`.

## Scale notes

### SMB

One consultant usually covers integration alongside configuration, and the estate is a handful of interfaces: an accounting package, a website form, perhaps a marketing list. Power Automate with standard connectors is often the right answer. Do not skip the inventory, the non-personal connection identity, the failure notification and a named owner; these are what stop a small team discovering failures from customers.

### Enterprise

An integration lead owns the inventory and the pattern catalogue, with developers per interface and a counterpart in each source system team. Expect an Azure integration layer (Service Bus, Functions, Logic Apps, often API Management) with its own environments, pipelines and on-call model. Interface contracts are versioned, pattern deviations go to design authority, and performance testing covers integration peaks running alongside user load.

## Hand-offs

- `platform-engineering:power-automate-patterns` and `platform-engineering:plugin-design` build the components.
- `testing-quality:system-integration-testing` plans end-to-end tests per interface; `testing-quality:performance-testing` covers peak load.
- `platform-administration:monitoring` takes over alerts and dashboards before go-live.
- Reviews: `design-authority:design-review` for pattern choices and deviations, and `security-compliance:security-model-review` for application user roles and data leaving the platform.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Connect an integration under a named person's account or one identity shared across every interface.
- Write to Dataverse in a tight loop without handling throttling responses and the Retry-After value.
- Build two-way synchronisation of the same field without an agreed master and conflict rule.
- Leave a dead-letter queue or failed-run history without an owner and an alert.
- Make a user wait on a synchronous call to a system with no agreed availability.
