---
name: reporting-strategy
description: Decides where each reporting need is met, across in-app views, charts and dashboards, built-in app analytics, Power BI and analytics workspaces, and maintains the report catalogue and KPI definitions. Use when legacy reports need rationalising, users ask for dashboards, or the team must choose between in-app reporting and Power BI.
license: CC-BY-4.0
metadata:
  department: data-and-ai
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Reporting strategy

Every CRM project inherits a long list of legacy reports, and the worst response is to rebuild all of them. Many were workarounds for a system that could not show a filtered list, which a model-driven view now does in minutes. Projects go wrong in two opposite directions: pushing everything into Power BI so users leave the app to see their own work, or forcing management analytics into in-app charts that cannot combine tables, history or other systems.

A reporting strategy is a decision about audience, freshness and data scope, made per need and written down so each thing is built once, in the right place.

## When to use

- Triaging the legacy report list at the start of a project.
- Deciding whether a need belongs in a view, a dashboard, built-in analytics, Power BI or an analytics workspace.
- Agreeing KPI definitions and who owns them.
- Sequencing reporting delivery around go-live.

Not this skill: `data-and-ai:power-bi-on-dataverse` for building Power BI content, `data-and-ai:fabric-link` for the analytics platform, `customer-service:service-analytics` and `sales:forecasting` for module-specific analytics, `change-adoption:adoption-metrics` for measuring system adoption.

## Questions to ask first

1. Who uses each report, and what decision do they make with it? Reports without a decision are candidates to retire.
2. How fresh must the data be? Needs measured in seconds belong in the app; daily is fine for most management reporting.
3. Does the need combine CRM data with other systems or long history? That takes it beyond in-app reporting.
4. Is there an existing Power BI or Fabric estate with its own governance? Reuse its workspaces and standards rather than starting a parallel one.
5. What Power BI and Fabric licensing do authors and viewers hold? It shapes who can see shared content; confirm with the Microsoft licensing guide or your partner.

## Approach

Use four tiers and a default for each.

1. In the app. Views, charts, dashboards and, in Customer Service, interactive dashboards. They are live, security-trimmed and need no data movement. This is the default for anything a user acts on: my open cases, my opportunities closing this month, today's work orders.
2. Built-in analytics. The CE apps ship analytics and insights features for sales, service and field service. Check current Microsoft Learn documentation for what is included and evaluate it before building custom equivalents.
3. Power BI on Dataverse. Cross-table, trend and KPI reporting for managers and leadership, embedded in model-driven apps where users need it in context, or published as Power BI apps.
4. Analytics workspace. Fabric or Azure Synapse fed by a Dataverse link, for combining CRM with ERP, web, telephony or survey data, for long history, or where reporting load would strain Dataverse.

Then work through the needs:

1. Collect needs as decisions, not layouts: who, which decision, how often, how fresh, which data.
2. Triage every legacy report: retire, replace with a view, replace with built-in analytics, rebuild in Power BI, or move to the analytics workspace. Use legacy usage data where it exists; reports nobody opened last quarter are rarely missed.
3. Record each surviving need in a report catalogue with audience, decision, tier, sources, freshness, owner, security approach and status.
4. Define measures once. Agree what won, open case, first-time fix, response time and similar terms mean, who owns each definition, and which certified semantic model carries it. Two reports defining the same KPI differently will undermine trust faster than any defect.
5. Design security per tier. In-app reporting inherits Dataverse security. Power BI and lake data need explicit design, which `data-and-ai:power-bi-on-dataverse` and `data-and-ai:fabric-link` cover.
6. Sequence delivery. Operational views and dashboards are go-live scope because users cannot work without them. Most management analytics follow once a few weeks of data exist in the new processes, so plan them as a post-go-live release rather than a go-live risk.

## Outputs

- Report catalogue covering audience, decision, tier, source, freshness, owner, security and status.
- Legacy report triage list with the decision for each report.
- KPI and measure definitions agreed with business owners.
- Reporting architecture section in the `solution-blueprint`.
- Go-live and post-go-live reporting backlog feeding the `delivery-plan`.

## Scale notes

### SMB

The consultant usually covers reporting. In-app views and dashboards plus a handful of Power BI reports often meet every need, so do not stand up an analytics workspace without a clear reason. Do not skip KPI definitions; small teams argue about numbers as much as large ones.

### Enterprise

A reporting lead or central BI team owns the catalogue and the certified semantic models, often alongside an enterprise data platform shared with other programmes. Module workstreams own their operational views; the BI team owns cross-module analytics. Expect data governance involvement in KPI definitions, a certification process for shared models, and design authority review of the reporting architecture.

## Hand-offs

- `data-and-ai:power-bi-on-dataverse` builds Power BI models and reports.
- `data-and-ai:fabric-link` sets up the analytics platform when tier four is needed.
- `customer-service:service-analytics` and `sales:forecasting` configure module analytics.
- `change-adoption:adoption-metrics` covers adoption reporting.
- Reviews: `design-authority:design-review` for the reporting architecture, and `security-compliance:security-model-review` for any data reported outside Dataverse security.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Rebuild every legacy report without asking what decision it supports.
- Send users to Power BI for lists they need to act on inside the app.
- Publish two reports that define the same KPI differently.
- Report CRM data outside the app without a designed security approach.
- Stand up an analytics workspace when in-app reporting or Power BI on Dataverse meets the need.
