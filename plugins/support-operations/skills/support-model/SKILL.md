---
name: support-model
description: Designs the business-as-usual support model for Dynamics 365 CE, covering support tiers, partner versus internal responsibilities, Microsoft support cases, the service owner role and support access to production. Use when deciding who supports the system after go-live, scoping a partner support contract, or defining routes to Microsoft.
license: CC-BY-4.0
metadata:
  department: support-operations
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Support model

A CRM system needs an owner and a support structure for as long as it runs, yet that structure is usually designed in a hurry just before go-live. The results are familiar: users email the consultant who built the system, the partner receives tickets it is not contracted for, nobody holds the relationship with Microsoft, and the system drifts because no one is accountable for it.

The support model decides who does what once the project team has gone: first-line help, configuration changes, code fixes, platform administration and escalation to Microsoft, with a named service owner accountable for the whole.

## When to use

- Deciding the support tiers and who staffs each one.
- Splitting responsibilities between internal teams and a partner.
- Scoping the partner support contract.
- Deciding who raises and manages Microsoft support cases.
- Setting rules for support and partner access to production.

Not this skill: `support-operations:incident-management` for severity definitions and incident handling, `support-operations:hypercare` for the period straight after go-live, `platform-administration:monitoring` for alerts and telemetry, and `programme-management:statement-of-work` for the contractual terms of partner work.

## Questions to ask first

1. Does the organisation have, or plan to build, an internal CRM team, and what skills do its members declare? This decides what stays in-house and what goes to a partner.
2. Is there an existing IT service desk and service management tool? Plugging into it avoids a parallel support channel.
3. What support arrangement does the organisation have with Microsoft, directly or through a partner? It decides who can raise cases and how quickly they are handled; check the organisation's Microsoft agreement, and for anything tied to licences confirm with the Microsoft licensing guide or your partner.
4. Who will be the service owner, and do they hold budget authority? A service owner without budget cannot prioritise anything.
5. What hours and locations must support cover? Field technicians and contact centres often work outside office hours.

## Approach

1. Define the tiers. A common shape for Dynamics 365 CE:
   - Tier 0: self-help through knowledge articles, in-app guidance and super-users.
   - Tier 1: the IT service desk logs every issue, resolves access and how-to questions, and routes the rest.
   - Tier 2: the internal CRM team or partner application support handles configuration, data fixes, security role changes and analysis.
   - Tier 3: developers, internal or partner, fix code, integrations and complex defects.
   - Microsoft: platform defects and service issues, raised as support cases through the Power Platform admin center by named administrators.
2. Split partner and internal work. For each tier and type of work, decide who owns it, using the declared skills and availability of the internal team rather than judgements about individuals. Make the partner scope explicit: response targets per severity, hours of cover, and how change work is estimated and approved. Avoid any arrangement in which the organisation cannot run its own system without the partner.
3. Name the roles. A service owner accountable for health, cost and roadmap; a product owner who manages the backlog; platform administrators; and super-users as the bridge into the business. One person may hold several roles in a small organisation, but every accountability needs a name.
4. Control support access. Support staff and partners get least-privilege roles in production. Elevated access is time-bound and logged, partner accounts are reviewed on a schedule, and they are removed when a contract ends.
5. Write the operating documents. The support process, routing rules, a knowledge base for the support team, runbooks for routine tasks (adding a user, changing a queue, rerunning a failed integration) and a contact list.
6. Prove it before go-live. The support team takes part in UAT and hypercare and handles real tickets under supervision, and the service desk tool has categories and routing configured before the first day.

## Outputs

- Support model document with tiers, routing and hours of cover.
- Support responsibilities as a `raci-matrix` across internal teams, partner and Microsoft.
- Partner support scope ready for contracting.
- Support access policy and review schedule.
- Support runbooks and contacts, referenced from the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Often there is no internal CRM team: a business system owner, a few trained super-users and a partner support contract. Make sure someone inside the organisation holds administrator access to the tenant and environments and can raise Microsoft cases, and that system knowledge is written down rather than living only with the partner.

### Enterprise

Expect a service owner, a platform team, application support per module, integration with the enterprise service management tool, contracted partner support with service levels, and a formal route to Microsoft. Coordinate with the organisation's Power Platform centre of excellence, where one exists, so that shared platform support is not duplicated.

## Hand-offs

- `support-operations:incident-management` defines severities and incident handling within the tiers.
- `support-operations:continuous-improvement` runs the backlog and release cadence the service owner controls.
- `platform-administration:monitoring` feeds alerts into the support queue.
- `security-compliance:security-model-review` signs off support and partner access to production.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Leave the organisation without its own administrator access to its tenant and environments.
- Give partner or support accounts standing System Administrator access in production.
- Route users directly to individual consultants instead of the support channel.
- Allocate support duties from assessments of individual performance rather than declared skills and availability.
