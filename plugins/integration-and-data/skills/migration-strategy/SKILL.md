---
name: migration-strategy
description: Sets the overall approach for moving legacy CRM, spreadsheet and mailbox data into Dataverse, covering scope, history cut-off, load order, owners and users, tooling and cutover approach. Use when deciding what to migrate, choosing migration tools, sequencing loads around lookups, or estimating the migration workstream.
license: CC-BY-4.0
metadata:
  department: integration-and-data
  stages: Initiate, Implement, Prepare
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Migration strategy

Data migration is the most under-planned workstream on CRM projects, because it looks like a technical task for the final month. In practice it is a business decision about what history is worth keeping, followed by months of iteration as quality problems surface. Programmes go wrong by promising to migrate everything, by starting extracts too late to find the problems in time, and by leaving owners and users until the end, when every single record needs one.

Good migrations are smaller than the customer first asks for. Every year of history kept means more mapping, more cleansing and more reconciliation, and much of it is never opened again once the new system is live.

## When to use

- Deciding scope: which tables, which records, how much history, and what stays in an archive.
- Choosing tools and the migration environment, and estimating effort.
- Sequencing loads so lookups resolve, and planning owners, users and teams.
- Choosing between a single cutover load and a phased or delta approach.

Not this skill: `integration-and-data:data-mapping-and-cleansing` for field-level rules, `integration-and-data:mock-migrations` for rehearsals, `integration-and-data:reconciliation` for proving the result, `support-operations:cutover-plan` for the go-live runbook.

## Questions to ask first

1. What will users actually do with migrated history in the first year? The answer sets the cut-off better than any rule of thumb.
2. What are the sources, the volumes per table and the size of attachments? Volumes decide tooling and load windows; attachments drive storage capacity.
3. Will the legacy system stay readable after go-live, and for how long? A read-only archive makes a short history cut-off much easier to agree.
4. How long is the cutover window, and can the business keep working in the legacy system during it? This decides between one load and a bulk-plus-delta approach.
5. Are there retention or deletion obligations on the legacy data? Migrating data that should already have been deleted moves the liability into Dataverse; the organisation's DPO or legal adviser decides what applies.

## Approach

1. Agree scope per table. For each table decide: migrate all, migrate filtered (open records plus closed records inside a cut-off), archive only, or leave behind. A common starting point is open opportunities, cases and work orders in full, recent closed records, and older activities archived. The business owner of each table signs its scope, not the project team.
2. Order loads by dependency. Reference and configuration data first (currencies, business units, teams, subjects, units, products, price lists), then users and owning teams, then accounts and contacts, then the transactional tables that look them up, and activities, notes and attachments last. Self-referencing lookups such as parent account need a second pass. Set state and status at the end of each table's load, because closed or inactive records resist later updates.
3. Settle owners and users early. Every record needs an owner. Map legacy users to Dataverse users or teams, decide where records owned by leavers go, and make sure users exist with the right business unit and roles before transactional loads start. Where original creation dates matter, load them into the overridden created on column; check current Microsoft Learn documentation for how it behaves.
4. Choose tooling by volume and repeatability. The Configuration Migration tool suits configuration and reference data moved between environments. Dataflows and the import wizard suit small, simple loads. Azure Data Factory, third-party ETL toolkits with Dataverse connectors, or custom loaders using the bulk operations of the Dataverse Web API or SDK for .NET suit large or complex loads that will be rehearsed many times. Choose on upsert support, logging, re-runnability and team skills, not on an existing vendor relationship.
5. Stage the data. Extract into a staging database where transformation, cleansing and reconciliation queries run, so every run is repeatable and auditable and the source is not hit repeatedly.
6. Plan throughput and business logic. Bulk loads fire plug-ins, flows, duplicate detection, rollups and auditing. Decide per table what is suspended during load, how it is re-enabled, and whether anything must be replayed afterwards. Check current Microsoft Learn documentation for the options to bypass custom business logic and the privileges they need.
7. Pick the cutover approach. A single load suits modest volumes and a weekend window. Large volumes usually need a bulk load of history ahead of cutover and a delta load of changes inside the window, which requires reliable change dates in the source.

## Outputs

- Migration strategy covering scope, cut-off, tooling, environments, load order and cutover approach.
- Table scope list signed by business data owners, carried into the `data-migration-mapping`.
- Load sequence and dependency diagram, including second-pass lookups.
- User and owner mapping approach, including leavers.
- Migration effort, mock schedule and milestones feeding the `delivery-plan`.
- Migration risks (source access, data quality, volumes, storage capacity) in the `raid-log`.

## Scale notes

### SMB

Usually a consultant working with the customer's administrator, migrating from spreadsheets, a mailbox or a small legacy CRM. Dataflows or the import wizard may be enough, and a short cut-off keeps the work manageable. Do not skip owner mapping, a full trial load into a non-production environment, or the business sign-off on scope.

### Enterprise

A migration lead, ETL developers, data analysts per source and named business data owners per table. Expect several sources holding conflicting versions of the same customer, a migration environment sized for production volumes, an ETL platform with its own deployment pipeline, and several mock migrations. Storage capacity needs forecasting early, and phased go-lives need coexistence rules and delta loads between waves.

## Hand-offs

- `integration-and-data:data-mapping-and-cleansing` produces field mappings and cleansing rules.
- `integration-and-data:mock-migrations` rehearses; `integration-and-data:reconciliation` proves the result.
- `platform-administration:licensing-and-capacity` forecasts storage capacity.
- `support-operations:cutover-plan` takes the final load into the runbook.
- Reviews: `security-compliance:data-retention` for what may be migrated and how long it is kept, and `design-authority:design-review` for the strategy.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Promise to migrate all history before the business has said what it will use.
- Load transactional records before their owners, users and referenced records exist.
- Migrate personal data that retention rules say should already have been deleted.
- Run the first full load as the production cutover.
- Choose a migration tool because of a vendor relationship rather than the load requirements.
