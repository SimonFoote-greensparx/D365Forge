---
name: incident-management
description: Defines how Dynamics 365 CE incidents are classified, escalated, communicated and closed, including severity definitions, major incident handling, escalation to Microsoft and post-incident review. Use when writing severity definitions, handling a live outage or serious defect, or setting up post-incident and problem reviews.
metadata:
  department: support-operations
  stages: Prepare, Operate
  modules: All
  status: draft
---

# Incident management

When a CRM system fails, the business feels it at once: agents cannot work cases, technicians cannot see their jobs, sellers cannot quote. The cause may be a Microsoft service issue, a failed integration, a bad deployment or a data problem, and the first hour is often lost working out which. Organisations without agreed severity definitions argue about priority while users wait, and those without a communication routine leave users guessing.

Incident management for Dynamics 365 CE should sit inside the organisation's existing IT service management practice, with additions for a cloud platform the organisation does not operate itself.

## When to use

- Writing or revising severity definitions and response targets.
- Handling a live incident, especially one that may be a Microsoft service issue.
- Setting up major incident communication.
- Running post-incident reviews and feeding problem management.

Not this skill: `support-operations:support-model` for who sits in which tier, `platform-administration:monitoring` for alerts and telemetry, `support-operations:hypercare` for the weeks straight after go-live, and `support-operations:continuous-improvement` for scheduling permanent fixes.

## Questions to ask first

1. What severity scale does the organisation's service desk already use? Align with it rather than inventing a CRM-only scale.
2. Which business processes are critical, and during which hours? Severity follows business impact, so this list drives classification.
3. Who can raise and escalate Microsoft support cases, and at which severities? Check the organisation's Microsoft agreement, and for anything tied to licences confirm with the Microsoft licensing guide or your partner.
4. Is there a major incident process and communication channel already? A CRM outage should use it, not a parallel one.

## Approach

1. Define severity by business impact. A workable four-level scale:
   - Severity 1: a critical process is unavailable for many users with no workaround (agents cannot open cases, the schedule board will not load, the mobile app cannot sync).
   - Severity 2: a critical process is degraded or unavailable for a group of users, or the workaround is costly.
   - Severity 3: a non-critical function fails, or a reasonable workaround exists.
   - Severity 4: cosmetic issues and questions.
   Attach response and resolution targets from the support agreement to each level, and state who may declare and who may downgrade a Severity 1.
2. Triage fast. Check Microsoft service health and Message center in the Microsoft 365 admin center, recent deployments, and failures in integrations and flows. Recent change is the most common cause, so know how to roll back the last deployment.
3. Escalate to Microsoft well. Raise the support case through the Power Platform admin center with the environment ID and URL, timestamps with time zone, any correlation or activity IDs shown in error messages, steps to reproduce, business impact and why the severity is justified. Good evidence shortens resolution more than chasing does.
4. Run a major incident routine. For Severity 1, appoint an incident lead, open a bridge with the right technical owners (including partner, middleware and telephony where relevant), publish user updates at a fixed interval even when there is no news, and keep the timeline as you go.
5. Treat data incidents differently. If an incident exposes or loses personal data (records shared too widely, a mistaken bulk update or delete, a misdirected marketing send), follow the organisation's breach process and involve the DPO or legal adviser immediately, because notification obligations may apply.
6. Close and learn. Hold a blameless post-incident review for Severity 1 and 2 covering timeline, root cause, contributing factors and actions. Open a problem record for recurring incidents and feed permanent fixes into the backlog.

## Outputs

- Severity definitions with response and resolution targets.
- Incident and major incident procedure, including a Microsoft escalation checklist.
- Incident communication templates for users and stakeholders.
- Post-incident review records and a problem log.
- Go-live incident procedure within the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Keep it simple: a one-page severity table, a named person who can raise Microsoft cases, a partner contact for out-of-hours, and a template message for users. A common trap is that only the partner can raise cases with Microsoft; make sure an internal administrator can as well.

### Enterprise

Incidents live in the enterprise service management tool with CRM-specific categories, on-call rotas per tier, alert integration, a major incident manager, and post-incident reviews reported to service governance. Coordinate with telephony, ERP and middleware teams, since many CRM incidents start somewhere else.

## Hand-offs

- `support-operations:continuous-improvement` schedules permanent fixes and problem actions.
- `platform-administration:monitoring` adds alerts for failure modes found in reviews.
- Emergency fixes that change signed-off design are assessed after the event by `design-authority:change-impact-assessment`.
- Incidents involving access to or exposure of data also go to `security-compliance:security-model-review`, alongside the DPO or legal adviser.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Set severity by who is complaining rather than by business impact.
- Hold back a Microsoft support case on a Severity 1 while internal investigation continues.
- Handle a personal data exposure as a routine defect without involving the DPO or legal adviser.
- Assign blame to individuals in post-incident reviews.
