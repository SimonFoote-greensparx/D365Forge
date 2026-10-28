---
name: power-bi-on-dataverse
description: Designs Power BI reporting over Dataverse, choosing the connector, import or DirectQuery, the semantic model shape and row-level security that matches Dataverse access, plus embedding and release. Use when connecting Power BI to CRM data, reports are slow or show rows users should not see, or reports are embedded in model-driven apps.
license: CC-BY-4.0
metadata:
  department: data-and-ai
  stages: Implement, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Power BI on Dataverse

Power BI over Dataverse looks easy because the connector finds every table in seconds. The trouble starts later: models that import whole tables with hundreds of columns, refreshes that time out, and above all reports that show managers rows the CRM security model would hide. Projects go wrong by assuming Power BI inherits Dataverse security, which depends entirely on how the model connects, and by building a new model for every report.

## When to use

- Choosing how Power BI connects to Dataverse and which storage mode to use.
- Designing semantic models over CRM tables, including choices, lookups, currency and dates.
- Designing row-level security that respects the Dataverse security model.
- Embedding Power BI in model-driven apps, or diagnosing slow or over-exposed reports.

Not this skill: `data-and-ai:reporting-strategy` for deciding whether Power BI is the right tier, `data-and-ai:fabric-link` for reporting over a lake copy, `security-compliance:security-model-review` for the Dataverse security model itself.

## Questions to ask first

1. Do all report viewers have Dataverse access, or will some see reports without being CRM users? Passing the viewer's identity to Dataverse only works for people Dataverse knows.
2. How complex is the security the reports must respect: business units, teams, sharing, hierarchy, field security? Simple rules can be mirrored in a model; complex ones push toward DirectQuery or a simplified reporting rule.
3. How fresh must the data be, and how large are the tables? Freshness favours DirectQuery; volume and history favour import or a lake.
4. Will reports be embedded in the app, published as Power BI apps, or both? This shapes filtering, navigation and who needs access.
5. What Power BI licensing and capacity do authors and viewers hold? Confirm with the Microsoft licensing guide or your partner.

## Approach

Choose the connection route. The Dataverse connector reads through the TDS endpoint, which must be enabled for the environment, and supports import and DirectQuery; it is the default for CRM reporting. The older Common Data Service (Legacy) connector reads through the Web API and still has uses for very large result sets and some data types. Where a Fabric link or Azure Synapse Link exists, large and historical models read the lake instead of Dataverse. Check current Microsoft Learn documentation for each route's limits, because they change.

Choose the storage mode per model, knowing what it does to security:

1. Import gives fast visuals and full modelling, refreshed on a schedule. Data is read with the credentials configured on the semantic model, so viewers do not get Dataverse security; row-level security must be built in the model.
2. DirectQuery with the Dataverse connector queries at view time. When configured to pass the viewer's identity, Dataverse applies that user's security roles, so rows are trimmed as in the app. The costs are slower visuals, modelling restrictions and query load on Dataverse. It suits operational reports embedded in the app; check current Microsoft Learn documentation for the setting and its constraints.

For import models, design row-level security deliberately. Do not try to reproduce every business unit, team, share and hierarchy rule. Agree a reporting security rule with security-compliance, such as by business unit, owning team or territory, then implement it by matching the signed-in user's principal name to the Dataverse user and its business unit or team membership tables. Test each role with real users from each business unit, not only the view-as feature. Leave out columns protected by field-level security unless the model protects them equivalently.

Shape the model as a star schema: facts such as opportunities, cases, work orders and activities; dimensions such as account, product, owner, territory and date. Select only the columns needed and filter out inactive rows where appropriate. Filter on choice value columns and display the label columns, since resolving labels costs query time. Use base-currency columns for totals across currencies. Decide time-zone handling explicitly, because Dataverse stores date and time values in UTC. Use incremental refresh on modified date for large import tables.

When embedding, remember that embedding changes navigation, not security: viewers still need access to the report and the model's own security still applies. Check current Microsoft Learn documentation for the environment setting that allows Power BI in model-driven apps.

Release through separate development, test and production workspaces, parameterise the environment URL, and promote with Power BI deployment pipelines or source control. Certify shared semantic models and build reports on them rather than duplicating models.

## Outputs

- Connection route and storage mode decision per model, with reasons.
- Semantic model design: tables, relationships, measures, refresh and incremental refresh settings.
- Row-level security design mapped to Dataverse security, with test evidence per role.
- Reports, dashboards and embedding configuration per report catalogue entry.
- Workspace and promotion approach aligned with the `environment-and-alm-strategy`.

## Scale notes

### SMB

Often one consultant or a report-literate power user builds a few reports on one shared model. DirectQuery can be the simpler route when everyone is a CRM user and volumes are modest, because Dataverse security then does the trimming. Do not skip a security test with a non-administrator account; administrators see everything and hide the problem.

### Enterprise

A BI team owns certified semantic models, workspaces, deployment pipelines and capacity. Expect a reporting security rule agreed with security-compliance, automated tests for row-level security, capacity monitoring, and design authority review of models that bypass Dataverse security. Large models usually read from the lake rather than Dataverse.

## Hand-offs

- `data-and-ai:fabric-link` when volume or history outgrows direct connection.
- `platform-administration:licensing-and-capacity` for Power BI capacity and licence questions; confirm with the Microsoft licensing guide or your partner.
- `testing-quality:performance-testing` for DirectQuery load on production Dataverse.
- Reviews: `security-compliance:security-model-review` for row-level security and field-level security handling, and `design-authority:design-review` for shared model design.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Assume an import-mode model inherits Dataverse security.
- Publish a model containing field-secured columns without equivalent protection in the model.
- Test row-level security only with an administrator account.
- Run heavy DirectQuery reports against production Dataverse without performance testing.
- Connect production reports with a named person's credentials or from a personal workspace.
