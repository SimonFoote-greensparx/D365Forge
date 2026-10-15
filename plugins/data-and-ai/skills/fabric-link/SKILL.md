---
name: fabric-link
description: Decides whether and how to replicate Dataverse data into an analytics platform, comparing Link to Microsoft Fabric with Azure Synapse Link for Dataverse, and designs table selection, lake security and curated layers. Use when CRM data must be combined with other sources, history outgrows direct reporting, or legacy exports need replacing.
license: CC-BY-4.0
metadata:
  department: data-and-ai
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Fabric link and Azure Synapse Link

Sooner or later someone wants CRM data next to ERP, web and telephony data, or wants years of history that would overwhelm a DirectQuery report. Microsoft's routes for this are the Link to Microsoft Fabric feature and Azure Synapse Link for Dataverse, which replaced older export services. Check current Microsoft Learn documentation for naming, options and limits before advising, because this area changes quickly.

Projects go wrong by enabling a link because the wizard makes it easy, then discovering that people in the analytics workspace can see rows the CRM security model hides, that storage consumption has grown, and that nobody owns the pipelines built on top.

## When to use

- Deciding whether CRM analytics needs a lake at all, and if so which link.
- Selecting tables, and designing curated layers and semantic models over linked data.
- Designing access to linked data, and deletion and retention in the lake.
- Replacing a legacy export to a database or data lake.

Not this skill: `data-and-ai:power-bi-on-dataverse` for reporting directly on Dataverse, `data-and-ai:reporting-strategy` for choosing the reporting tier, `marketing:customer-profile-unification` for unified customer profiles in Customer Insights - Data, `integration-and-data:integration-architecture` for operational interfaces.

## Questions to ask first

1. What need does this serve that Power BI on Dataverse cannot? If there is none, do not add a data platform.
2. Does the organisation already have Fabric capacity or an Azure data platform, in the same region as the Dataverse environment? Existing platforms and regional constraints usually decide the route.
3. Must the organisation own the storage and files, for example for its own tools, network controls or retention? That points toward Azure Synapse Link to its own storage account.
4. How fresh must analytical data be? Both routes are near real-time rather than instant; check current Microsoft Learn documentation for expected latency.
5. Who may see the data once it is outside the app? This is a security design question before it is a technical one.

## Approach

Choose the route.

1. Link to Microsoft Fabric. Dataverse maintains an analytics-ready copy of selected tables in Dataverse-managed storage and exposes it to a Fabric workspace through shortcuts, so there is no export pipeline to build. It consumes Dataverse storage capacity and needs Fabric capacity in a matching region. This is the default when Fabric is already the organisation's analytics platform. Check current Microsoft Learn documentation for prerequisites and for how many workspaces an environment can link to.
2. Azure Synapse Link for Dataverse. Dataverse exports continuously to the organisation's own Azure Data Lake Storage account, as CSV or in Delta format with a Spark pool, optionally attached to a Synapse workspace. Choose it when you need control of storage, network restrictions or non-Microsoft tools. You own the storage, the compute and their cost.
3. Neither. For modest volumes and CRM-only reporting, stay with Power BI on Dataverse.

Then design the link:

1. Tables. Linked tables need change tracking enabled. Choose tables from the report catalogue, not everything available, and review the list whenever new tables are added to the solution.
2. Layers. Treat linked tables as raw. Build curated tables that resolve choice labels and lookups, normalise currency and time zones, and handle deleted rows, then build reporting models on the curated layer. Reports should never query raw tables directly.
3. Security. Do not assume Dataverse security roles filter what workspace or storage users see; design access as if they do not. Restrict raw data to the data engineering team, publish curated data by role, exclude or mask columns that are field-secured or sensitive, and apply row-level security again in semantic models.
4. Deletion and retention. Understand how each route represents deleted rows and how long it keeps them. An erasure request or retention rule must reach the lake and every downstream copy, not only Dataverse; the organisation's DPO or legal adviser confirms which obligations apply.
5. Environments. Link each environment to its own workspace or storage. Never link a sandbox to a production analytics workspace. Solution deployments that change table schemas must be tested against downstream pipelines.
6. Operation. Monitor link status and table sync errors, Dataverse storage consumption, and Fabric or Azure cost, with a named owner for each.

## Outputs

- Analytics platform decision (Fabric link, Azure Synapse Link or neither) with reasons, in the `solution-blueprint`.
- Linked table list with change tracking settings and the reporting need each serves.
- Lake access design covering raw, curated and reporting layers.
- Curated layer and semantic model design.
- Capacity and cost forecast for Dataverse storage and Fabric or Azure.
- Link configuration per environment in the `environment-and-alm-strategy`.

## Scale notes

### SMB

Usually not needed at go-live; Power BI on Dataverse covers most needs. If the organisation already uses Fabric, the Fabric link is the lowest-effort route, but still choose tables deliberately and restrict workspace access. Do not skip the security design because the setup is a wizard.

### Enterprise

A data platform team typically owns Fabric or Azure, with the CRM programme as a supplier of data. Agree a contract for table schemas and change notice, shared curated layers with other domains, data governance through the organisation's catalogue and sensitivity labelling, and separate links per environment aligned with release management.

## Hand-offs

- `data-and-ai:power-bi-on-dataverse` builds semantic models and reports over curated data.
- `platform-administration:licensing-and-capacity` forecasts Dataverse storage and capacity.
- `platform-administration:monitoring` monitors link health.
- Reviews: `security-compliance:security-model-review` for lake access, `security-compliance:data-retention` for deletion and retention in the lake, and `design-authority:design-review` for the platform decision.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Enable a link to production before the lake access design has been reviewed by security-compliance.
- Grant broad workspace or storage access to raw linked tables for convenience.
- Link every available table and leave storage consumption unreviewed.
- Link a non-production environment to a production analytics workspace.
- Leave erasure and retention obligations unapplied to data copied into the lake.
