---
name: service-analytics
description: Defines the service metrics that matter and how Dynamics 365 Customer Service reports them, using built-in historical and real-time analytics, Power BI and Dataverse data. Use when choosing service KPIs, designing supervisor and leadership dashboards, or working out why service figures disagree between reports.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Initiate, Implement, Operate
  modules: Customer Service
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Service analytics

A service operation is run on its numbers: supervisors move people between queues, leaders justify headcount, and the business case for the project is judged on them. If the metrics are poorly chosen or inconsistently defined, the operation optimises for the wrong thing and nobody trusts the dashboards.

Projects usually go wrong in two ways. They leave analytics until after go-live, then discover the fields needed for first contact resolution or contact reason were never captured. Or they publish a long list of speed measures with no quality counterweight, and teams learn to close cases quickly and watch them reopen.

## When to use

- Choosing a balanced set of service KPIs and writing their definitions.
- Deciding what built-in analytics cover and where Power BI is needed.
- Designing dashboards for agents, supervisors, service leaders and executives.
- Reconciling figures that differ between built-in reports, Power BI and spreadsheets.
- Linking service measures to the project's success measures.

Not this skill: `data-and-ai:reporting-strategy` for the organisation-wide reporting approach, `data-and-ai:fabric-link` for analytics data platform choices, `change-adoption:adoption-metrics` for measuring system adoption, `customer-service:slas-and-entitlements` for configuring the SLA timers that feed compliance figures.

## Questions to ask first

1. What decisions will each metric inform, and who makes them? A metric with no decision owner is decoration.
2. Which channels and record types are in scope? Case metrics and conversation metrics come from different data and different built-in reports.
3. Does the case and conversation design capture what the metrics need? Contact reason, resolution category, origin and reopen tracking must be designed in, not reported around.
4. Is there an existing reporting platform and data team? This decides how far to rely on built-in analytics versus Power BI.
5. Who may see what level of detail? Team-level operational views are routine; individual-level data raises people and privacy questions.

## Approach

Pick a small, balanced set of measures that pull against each other, so improving one at the expense of another becomes visible. A sensible core for most service desks covers five areas:

- Demand: new cases and conversations by channel and contact reason.
- Speed: first response and resolution time against SLA.
- Quality: first contact resolution, reopen rate and customer satisfaction.
- Flow: backlog size and age, transfers, and abandonment on real-time channels.
- Knowledge and AI: knowledge use on resolved cases and self-service with a confirmed outcome.

1. Write definitions before building. For each metric state the numerator, denominator, inclusions and exclusions (merged, cancelled and test cases), time basis and time zone. Built-in analytics, Power BI and supervisors' spreadsheets must share the same definitions or the figures will never reconcile.

2. Design the data into the lifecycle. Check that `customer-service:case-lifecycle-design` captures contact reason, resolution category, origin channel and a way to detect reopens, before build completes.

3. Use built-in analytics first. Customer Service provides historical and real-time analytics for cases, conversations and knowledge; check current Microsoft Learn documentation for the current reports, how they are enabled and how often data refreshes. They are a fast win for supervisors.

4. Extend with Power BI where needed. Cross-module views, telephony or ERP data, and long-history trends belong in a governed Power BI model over Dataverse, built with `data-and-ai:power-bi-on-dataverse`.

5. Build one view per audience. Agents need their queue and SLA timers, supervisors need real-time flow and backlog, service leaders need trends and outcomes, executives need a handful of outcome measures. Keep each view small.

6. Keep metrics about the operation. Report at queue, team and channel level. Do not design league tables or rankings of individual agents; any use of individual data is a matter for the organisation's HR policy, and privacy questions go to the organisation's DPO or legal adviser.

7. Reconcile, then review. During UAT compare built-in figures, Power BI and a manual count for a sample period. After go-live, review the metric set each quarter and retire measures nobody uses.

## Outputs

- Metric catalogue with definitions and owners, referenced from the `solution-blueprint`.
- Dashboard set per audience.
- Data capture requirements fed back to the case and conversation design.
- Reconciliation tests in `test-strategy-and-uat-scripts`.
- Service measures linked to the success measures in the `project-charter`.
- Hypercare dashboard in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Built-in dashboards plus a few views usually suffice, defined by the consultant with the service manager. Do not skip written metric definitions or the case fields that feed them, because they cannot be added retrospectively to history.

### Enterprise

Expect a governed semantic model owned by the data team, analytics data in a lakehouse via `data-and-ai:fabric-link`, regional comparisons that need common definitions, and benefits tracking against the business case. Any reporting that exposes individual agent data needs a privacy review and agreement with HR before release.

## Hand-offs

- `data-and-ai:power-bi-on-dataverse` builds the Power BI models and reports.
- `support-operations:continuous-improvement` uses the metrics after go-live.
- `change-adoption:adoption-metrics` complements service measures with adoption measures.
- Reviewer sign-off: `security-compliance:security-model-review` for who can see which service data, and `design-authority:standards-conformance` for metric and model standards.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Publish a metric without a written definition shared by every report that shows it.
- Build league tables or rankings of individual agents.
- Track speed metrics without a balancing quality metric.
- Leave analytics design until after go-live, when the fields it needs were never captured.
