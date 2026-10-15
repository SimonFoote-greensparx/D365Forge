---
name: adoption-metrics
description: Defines adoption metrics for Dynamics 365 CE across usage, data quality and process outcomes, with baselines, targets, sources and review rhythm, reported by team or role and never used to monitor individual performance. Use when setting adoption KPIs, specifying an adoption dashboard, or diagnosing low usage after go-live.
metadata:
  department: change-adoption
  stages: Prepare, Operate
  modules: All
  status: draft
---

# Adoption metrics

Login counts say very little about whether a CRM is working. People can sign in every day and still keep the real pipeline in a spreadsheet, or close cases with no resolution recorded. Useful adoption measurement looks at three layers together: whether people use the system for the processes it was built for, whether the data they enter is good enough to rely on, and whether the business outcomes in the charter are moving.

Measurement goes wrong when the dashboard is all logins and record counts, when there is no baseline so nothing can be compared, and when metrics are turned against individuals. Once users believe the data is being used to judge them personally, they enter whatever keeps the numbers green, and the data becomes useless for the purposes the programme was funded for.

## When to use

- In Prepare, to define metrics and take baselines before go-live.
- During hypercare, to spot where usage or data quality is lagging.
- In Operate, to report adoption to steering and feed benefits tracking.
- When usage is lower than expected and the programme needs to understand why.

Not this skill: `programme-management:project-charter` for defining the business outcomes themselves, `customer-service:service-analytics` for operational service KPIs, `data-and-ai:reporting-strategy` for the wider reporting landscape, `platform-administration:monitoring` for platform health.

## Questions to ask first

1. Which charter outcomes must adoption evidence support? Metrics that do not connect to outcomes become vanity numbers.
2. What baseline exists from the legacy system or manual sampling? Without one, improvement cannot be shown.
3. Which data sources are available, such as Dataverse records, audit data and platform usage analytics? Check current Microsoft Learn documentation for what the Power Platform admin center reports today.
4. At what level of aggregation will HR, any works council and the DPO accept reporting? Agree this before building anything.
5. Who will act on the metrics, and how often? A metric nobody acts on should be dropped.

## Approach

Define a small set of measures in each of three layers, by role.

1. Usage. Active users by role and team against assigned licences (for licence assignment questions, confirm with the Microsoft licensing guide or your partner); records created through the intended process, such as opportunities progressed through stages, cases created from queues, and work orders completed on mobile; use of key capabilities such as forecasts, queues or the schedule board; and signs that legacy tools or shadow spreadsheets are still in use.
2. Data quality. Completeness of the fields that reporting depends on, duplicate trends, opportunities with no recent activity, cases closed without a resolution category, work orders without completion notes, and contacts without a recorded consent status.
3. Process outcomes. The charter measures themselves, such as pipeline coverage, forecast reliability, case resolution time, first-time fix and lead conversion, compared with baseline.

For each metric record the definition and formula, source, aggregation level, owner, baseline, target set by the business owner, and review frequency.

- Aggregate by team, role, business unit or site, and agree with the DPO a minimum group size below which results are not shown, so individuals cannot be identified.
- Prefer Dataverse data reported through Power BI and the organisation's existing reporting tools. Do not track keystrokes, screen time or time spent in the app.
- Take baselines before go-live and agree targets with business owners, not the project team.
- Review weekly during hypercare and monthly afterwards. Actions are supportive: targeted refresher training, process fixes, backlog items, data clean-up, or better guidance. They are never disciplinary.
- During hypercare, add leading indicators: help requests by theme and feedback from super users.
- Hand the metric set to the business owners and support team at the end of hypercare, so measurement continues into benefits tracking.

## Outputs

- An adoption metrics catalogue with definitions, sources, owners, baselines and targets.
- A dashboard specification at agreed aggregation levels.
- A pre-go-live baseline report.
- Hypercare and monthly adoption review packs with an action log.

## Scale notes

### SMB

A handful of measures on a single dashboard, reviewed monthly by the owner, is enough. In small teams even role-level results can identify a person, so report at team level or not at all, and check the approach with the organisation's DPO or legal adviser.

### Enterprise

Adoption dashboards per business unit feed a benefits realisation forum. Definitions are held centrally so regions report the same thing, works council agreements set the reporting levels, and retention of usage data follows the organisation's retention policy.

## Hand-offs

- `data-and-ai:power-bi-on-dataverse` builds the dashboards.
- `change-adoption:role-based-training` acts on gaps the metrics reveal.
- `support-operations:continuous-improvement` turns findings into backlog items.
- `programme-management:governance-cadence` takes adoption reporting to steering.
- Reviewer sign-off: `security-compliance:data-retention` for retention of usage data; data protection questions go to the DPO.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use adoption data to monitor, rank or discipline individual users.
- Report login counts as evidence of adoption on their own.
- Publish results at a level where individuals in a small team can be identified.
- Set targets without a baseline.
