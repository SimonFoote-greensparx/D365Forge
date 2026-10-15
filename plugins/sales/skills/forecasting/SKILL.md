---
name: forecasting
description: Configures sales forecasting in Dynamics 365 Sales, including the forecast hierarchy, periods, columns, quotas, forecast categories, adjustments and permissions. Use when setting up forecasts for the first time, choosing between a manager or territory hierarchy, loading quotas, or working out why the forecast does not match the pipeline report.
metadata:
  department: sales
  stages: Implement, Prepare, Operate
  modules: Sales
  status: draft
---

# Forecasting

A forecast is only as good as the pipeline beneath it and the hierarchy it rolls up through. Dynamics 365 Sales provides forecast configuration that rolls opportunities up a hierarchy by period, with columns driven by forecast category and room for managers to adjust, but it assumes the underlying data and reporting lines are sound.

Projects usually go wrong by switching forecasting on before stages, close dates and forecast categories are used consistently, then losing the sales director's trust in the first week. The other common mistake is building the forecast on a hierarchy that does not match how the sales organisation actually reviews deals.

## When to use

- Setting up a forecast configuration: hierarchy, period, columns and permissions.
- Choosing between a manager hierarchy, a territory hierarchy or another structure.
- Loading and maintaining quotas.
- Defining forecast categories and how they relate to stage and probability.
- Reconciling the forecast with pipeline reports and finance targets.

Not this skill: `sales:sales-process-stages` for stage and probability design, `data-and-ai:power-bi-on-dataverse` for bespoke pipeline and forecast reporting, `security-compliance:business-units-and-teams` for the organisational security structure.

## Questions to ask first

1. How does the sales organisation review the forecast today, and how often? The configuration should mirror the real review meeting, not an idealised one.
2. Is the hierarchy based on reporting lines or on territories, and is that data maintained? A forecast rolls up only as well as the manager field or territory records it relies on.
3. Which fiscal calendar and forecast period apply? If they do not match finance, the numbers will never reconcile.
4. Who sets quotas, and how often do they change? Quota loading needs an owner and a repeatable method.
5. Are predictive or premium forecasting capabilities expected? Some capabilities depend on licence, so confirm with the Microsoft licensing guide or your partner.

## Approach

Fix the data before switching on the forecast. Check that open opportunities have a realistic estimated close date, an estimated revenue in the right currency and a forecast category that sellers actually maintain. If those are not true today, a forecast simply automates the arguments.

1. Agree the forecast categories. The standard opportunity forecast category separates pipeline, best case, committed, won, lost and omitted. Decide whether sellers set the category directly or whether it defaults from the stage, and write the rule down next to the stage mapping.
2. Choose the hierarchy. A manager hierarchy built on the user's manager field suits most organisations; a territory hierarchy suits those that manage by region or segment and keep territory records current. Check reporting lines in Dataverse before go-live, because a missing manager breaks the rollup without any warning to users.
3. Set the period and fiscal calendar to match finance, and decide how many periods ahead and behind are visible.
4. Configure columns that match the review conversation, typically quota, won, committed, best case and pipeline. Leave out columns nobody discusses in the meeting.
5. Load quotas with a repeatable method, usually a spreadsheet import per period, owned by sales operations rather than the CRM team.
6. Define adjustment rules. Managers can adjust rolled-up figures, so agree who may adjust, whether a note is required and how adjustments are reviewed, so the adjusted forecast stays explainable.
7. Set permissions so people see their own forecast and their team's rollup, consistent with the security model.
8. Use snapshots or forecast history to review trends and compare forecast with outcome. Check current Microsoft Learn documentation for the history and predictive features in your release; for what your licence includes, confirm with the Microsoft licensing guide or your partner.

Run at least one parallel cycle in which the existing spreadsheet forecast and the Dynamics 365 forecast are produced side by side. Reconcile the differences with sales operations, fix the data or configuration causes, and only then retire the spreadsheet.

## Outputs

- Forecast configuration design: hierarchy, periods, columns, categories, permissions and adjustment rules.
- Quota loading procedure with a named owner.
- Stage, probability and forecast category mapping, shared with the sales process design.
- Parallel run reconciliation record, plus forecast acceptance tests in the `test-strategy-and-uat-scripts`.
- Forecast review guidance for managers in the `training-and-communications-plan`.

## Scale notes

### SMB

One forecast on the manager hierarchy with quota, won, committed and pipeline columns is usually enough, configured by the consultant with the sales director. Quotas can be loaded each quarter from a spreadsheet. Do not skip the data quality check on close dates and forecast categories, because a small pipeline is swung by a handful of stale deals.

### Enterprise

Expect several forecast configurations (by region, product line or territory), a sales operations team that owns quotas and adjustments, and reconciliation with finance targets. Hierarchy data should be fed from HR or identity systems rather than maintained by hand, and changes to forecast categories or stage mappings should go through `design-authority:change-impact-assessment`. Bespoke analysis belongs in Power BI rather than in ever more forecast columns.

## Hand-offs

`sales:sales-process-stages` owns stage and category design, `data-and-ai:power-bi-on-dataverse` and `data-and-ai:reporting-strategy` own wider pipeline analytics, and `change-adoption:role-based-training` prepares managers for the forecast review. Forecast visibility across teams needs `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Switch on forecasting before close dates and forecast categories are maintained.
- Use the forecast grid to rank or appraise individual sellers; that is a management conversation outside this skill.
- Let managers adjust forecasts without a note or an audit trail.
- Promise predictive forecasting features without confirming licence and data readiness.
