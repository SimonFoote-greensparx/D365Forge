---
name: licensing-and-capacity
description: Structures Dynamics 365 and Power Platform licensing and Dataverse capacity questions by persona, usage, environment and growth, and sets up ongoing licence and storage review. Use when estimating licences for a programme, checking whether capacity covers planned environments and data, or reviewing usage after go-live.
metadata:
  department: platform-administration
  stages: Strategize, Initiate, Prepare, Operate
  modules: All
  status: draft
---

# Licensing and capacity

Licensing and capacity decide what the programme costs to run and, sometimes, what it is allowed to build. The rules for Dynamics 365, Power Platform and Copilot Studio change regularly and contain subtleties (base and attach licences, lighter-use rights, access through other systems) that are easy to get wrong in a spreadsheet. Dataverse capacity is consumed by every environment, every copy and every attachment, and running over it blocks routine admin operations.

This skill structures the questions so the right facts reach the people who can answer them. It does not give licensing advice, and every conclusion it reaches must be confirmed with the Microsoft licensing guide or your partner.

## When to use

- Building the licence estimate for a business case or statement of work.
- Checking whether planned environments, copies and data volumes fit the capacity available.
- Considering an agent, integration or portal that changes who or what reaches Dataverse.
- Reviewing licence assignment and storage after go-live.

Not this skill: `platform-administration:environment-setup` for creating environments, `security-compliance:data-retention` for retention rules that reduce storage, and `programme-management:statement-of-work` for commercial terms with the partner.

## Questions to ask first

1. Which personas use which apps, tables and features, and how often? Licences follow what people do, not their job titles.
2. How many environments with Dataverse are planned, and which hold production copies? Each one consumes database capacity.
3. What data volumes, attachment growth and audit retention are expected? These drive database, file and log capacity.
4. What non-human access is planned (integrations, portals, agents, automated processes)? Indirect access and consumption-based services carry their own rules.
5. When do the licence agreements renew? Renewal is the practical moment to change the mix.

## Approach

1. Build the persona model. List personas from the role mapping with the apps, key tables and actions each needs, for example agents working cases all day versus managers who only read dashboards. Use declared roles and expected usage, never assessments of individuals. Map personas to licence types with the partner, noting where base and attach combinations or lighter-use licences might apply, and confirm with the Microsoft licensing guide or your partner.
2. Check indirect access. Reaching Dataverse through an integration, custom portal or another application does not usually remove the need for appropriate licences, because multiplexing rules look through the intermediary. Record each such pattern, then confirm with the Microsoft licensing guide or your partner.
3. Model capacity. Dataverse capacity is tracked as database, file and log, with entitlement pooled at tenant level from the licences held. Estimate each type per environment from row volumes, attachments and audit, include non-production copies, and project growth over several years. Move large documents to document management where it suits, and set retention so audit and log data do not grow without limit. For entitlements and add-on options, confirm with the Microsoft licensing guide or your partner.
4. Account for requests and AI consumption. Request entitlements, Copilot Studio and other consumption-based services, and pay-as-you-go options all affect cost. Capture expected volumes for each, and confirm with the Microsoft licensing guide or your partner.
5. Watch the consequences. Being over capacity restricts admin operations such as creating, copying or restoring environments, so monitor capacity in the Power Platform admin center and alert well before limits are reached.
6. Review regularly. After go-live, compare assigned licences with actual usage, reclaim unused ones and refresh the capacity forecast. Take the results into renewal discussions early.

## Outputs

- A persona-to-licence model with its assumptions, flagged for confirmation with the Microsoft licensing guide or your partner.
- A capacity forecast per environment and capacity type.
- A register of indirect access patterns and consumption-based services.
- Licensing and capacity risks added to the `raid-log`.

## Scale notes

### SMB

Keep the persona model short and work through it with the partner before signing. Capacity rarely binds early, but non-production copies and attachments can surprise, so set capacity alerts from day one. Do not skip the indirect access check for any portal or integration; confirm with the Microsoft licensing guide or your partner.

### Enterprise

A licensing owner, often procurement working with the platform team, holds the model, reconciles it against usage each quarter and plans true-ups. Capacity forecasting feeds the environment strategy and the retention policy. Large agreements may carry specific terms, so confirm with the Microsoft licensing guide or your partner.

## Hand-offs

`platform-administration:environment-setup` provisions within the confirmed capacity, `platform-administration:monitoring` alerts on capacity, and `programme-management:raid-log` tracks open licensing questions. No reviewer sign-off is mandated, but `design-authority:change-impact-assessment` should flag design changes that alter the licence mix.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Quote prices, licence entitlements or capacity limits from memory.
- Assume access through an integration, portal or agent removes the need for user licences.
- Create or copy environments without checking database capacity.
- Assign licences by job title without checking what each persona actually does.
- Present a licensing conclusion as final before it is confirmed with the Microsoft licensing guide or your partner.
