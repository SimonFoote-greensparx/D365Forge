---
name: monitoring
description: Sets up operational monitoring for Dynamics 365 CE and Power Platform, covering service health, Message center, capacity, plug-in and flow failures, integration errors, telemetry, business heartbeats and alert routing. Use when preparing operations before go-live, deciding what to alert on and who receives it, or when users find failures first.
license: CC-BY-4.0
metadata:
  department: platform-administration
  stages: Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Monitoring

After go-live, the system's reputation depends on the support team finding problems before users do. Dynamics 365 CE fails in quiet ways: a support mailbox stops creating cases, a flow's connection expires, an integration queue backs up, system jobs pile up or capacity creeps towards its limit. None of these puts an error on a user's screen until the damage is done.

Most projects either monitor too little, relying on users to report issues, or too much, sending every alert to a mailbox nobody reads. Good monitoring is a short list of signals, each with an owner and a runbook.

## When to use

- Preparing operational readiness before go-live.
- Deciding which signals to alert on and where alerts go.
- Users are reporting failures that monitoring should have caught.
- Reviewing monitoring after a major change, a new integration or a new agent.

Not this skill: `support-operations:incident-management` for handling incidents once raised, `support-operations:support-model` for support tiers and hours, `customer-service:service-analytics` for business service reporting, and `solution-architecture:performance-by-design` for designing performance problems out.

## Questions to ask first

1. Who receives alerts, and during which hours? An alert without a reachable owner is noise.
2. Which business processes are critical enough to need end-to-end checks? These get heartbeat monitoring, not just error logs.
3. Which monitoring tools does the organisation already run (Azure Monitor, a security information and event management tool, an IT service management tool)? Feed existing tools rather than adding another console.
4. Which integrations and automations run unattended? Each needs its own failure signal.
5. What are the log and telemetry retention requirements? These decide where data is kept and for how long; where personal data is involved, check with the organisation's DPO or legal adviser.

## Approach

Monitor in layers, from Microsoft's service down to individual business processes, and route each signal to someone who can act on it.

1. Microsoft service. Subscribe the platform team to service health and Message center for the products in use. Message center posts often announce deprecations and behaviour changes well before they take effect.
2. Platform. Watch capacity, API request usage and throttling, environment operations and admin activity through the Power Platform admin center and its analytics, with capacity alerts set well short of limits.
3. Application. Send Dataverse, model-driven app and flow telemetry to Application Insights where supported, checking current Microsoft Learn documentation for what can be exported. Alert on plug-in exceptions, failed or stuck system jobs, flow failures and form performance regressions. Keep plug-in trace logging to exceptions in production.
4. Integration. Monitor dead-letter queues, failed messages and sync lag for each integration, at both the Dataverse end and the other system's end.
5. Business heartbeat. Define simple checks that prove critical processes still work: cases arriving from each support mailbox, server-side sync mailboxes healthy, work orders reaching technicians' devices, leads arriving from marketing forms. A missing heartbeat is often the first sign of a broken connection.
6. Security and audit. Feed audit and activity logs into the organisation's security monitoring, with the scope agreed with the security team.
7. Alert design. Every alert has a threshold, an owner, a severity and a runbook entry. Alerts go to monitored queues, shared channels or the service management tool, never to personal mailboxes. Review alert volumes monthly and retire alerts nobody acts on.

## Outputs

- A monitoring catalogue listing signal, source, threshold, owner, severity and runbook link.
- Dashboards for platform health, integrations and business heartbeats.
- Runbook entries handed to support and referenced by the `cutover-and-hypercare-checklist`.
- Monthly monitoring review notes feeding continuous improvement.

## Scale notes

### SMB

Start with service health and Message center subscriptions, capacity alerts, flow failure notifications to a shared mailbox or Teams channel, and one heartbeat for each critical inbound channel. That small set catches most real problems. Do not skip naming an owner for each signal.

### Enterprise

Integrate telemetry with the enterprise monitoring and service management tools, define severity levels aligned to the support model and run synthetic transactions for key journeys. A platform operations lead owns the catalogue, and hypercare uses the same signals with tighter thresholds.

## Hand-offs

`support-operations:incident-management` handles raised alerts, `support-operations:hypercare` uses the catalogue during hypercare, and `support-operations:continuous-improvement` acts on trends. Reviewer sign-off: `security-compliance:security-model-review` for the scope of audit and security monitoring.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Send platform alerts to an individual's mailbox instead of a monitored queue.
- Create an alert with no owner or runbook entry.
- Leave full plug-in trace logging switched on in production.
- Rely on users reporting failures as the main means of detection.
- Ignore Message center notices about deprecations that affect the solution.
