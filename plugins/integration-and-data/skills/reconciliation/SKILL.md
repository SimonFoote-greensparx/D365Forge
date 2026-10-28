---
name: reconciliation
description: Proves that migrated or integrated data arrived complete and correct, using record counts, financial and quantity totals, relationship checks and business sample reviews, ending in signed acceptance. Use when defining reconciliation checks, investigating count mismatches after a load, or gathering migration sign-off for go/no-go.
license: CC-BY-4.0
metadata:
  department: integration-and-data
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Reconciliation

Reconciliation is how a migration earns trust. Without it, the first week of go-live is spent arguing about whether a missing opportunity was ever there. Projects go wrong by reconciling only total row counts, which hide offsetting errors, by agreeing tolerances after seeing the results, and by letting the project team sign off on data it does not own.

Integrations need the same discipline on a recurring basis. An interface that has quietly dropped one message a day for a month is a reconciliation failure, not a monitoring one.

## When to use

- Defining the checks, queries, tolerances and owners for migration acceptance.
- Running reconciliation after a mock or the production load, and explaining variances.
- Collecting signed acceptance from business data owners for go/no-go.
- Setting up recurring reconciliation between Dataverse and another system after go-live.

Not this skill: `integration-and-data:mock-migrations` for running the loads, `integration-and-data:data-mapping-and-cleansing` for fixing the rules behind a variance, `testing-quality:user-acceptance-testing` for testing processes rather than data.

## Questions to ask first

1. Who is the business data owner for each table, with authority to accept it? Sign-off by the project team is not sign-off.
2. What tolerance is acceptable per table and measure? Tolerances agreed after the results are known invite argument.
3. What figures can the source produce reliably, and as at what time? Reconciling against a moving source makes variances impossible to explain.
4. Which records carry financial or contractual weight? Those need exact totals, not samples.
5. Is this a one-off migration or an ongoing integration? Integrations need automated recurring checks, not a single report.

## Approach

Work in four layers, and script every check so it runs identically after each mock and the production load.

1. Completeness. Count rows per table at every stage: extracted, transformed, rejected, deliberately excluded and loaded. Extracted must equal loaded plus rejected plus excluded, so every row is accounted for. Break counts down by meaningful slices (state, status reason, owner, business unit, source system, record type), because a correct total can hide two errors that cancel out.
2. Value accuracy. Compare control totals on money and quantity columns, such as open pipeline value, order and contract values, entitlement terms and stock quantities, by currency and by status. Compare key text columns between staging and target with checksums where the tooling allows. Check dates carefully: Dataverse stores date and time values in UTC and displays them in the user's time zone, so a date-only value loaded into a user-local column can appear a day out. Confirm each date column's behaviour against the mapping.
3. Integrity. Confirm there are no orphaned children, that lookups point to the right parents, that closed records carry the right status reason, that owners match the mapping, and that attachments exist and open.
4. Business sample review. Business users open a sample of records in the app against a short checklist. Choose the sample deliberately: largest customers, oldest records, records with many children, merged duplicates, and anything that caused a defect in an earlier mock. Agree the sample size with the data owner.

Query the target through the Dataverse Web API, FetchXML aggregates or the read-only TDS endpoint rather than counting rows in views. Aggregate queries have row limits on large tables, so check current Microsoft Learn documentation and count in partitions where needed.

Every variance gets a row in an exceptions log with root cause, decision (fix and re-run, or accept) and approver. Accepted variances need the data owner's name against them.

Sign-off happens per table. The data owner signs a short statement that the data is accepted, listing accepted exceptions. These statements go into the go/no-go evidence pack.

For integrations, agree a small set of daily or weekly counts and totals between Dataverse and the other system, automate them, and alert on breaches. Make them part of the support model.

## Outputs

- Reconciliation specification per table, with checks, queries, tolerances and owners, linked to the `data-migration-mapping`.
- Reconciliation report per mock and for the production load, with variances explained.
- Exceptions log with root cause, decision and approver.
- Signed acceptance from each business data owner, filed for go/no-go.
- Reconciliation steps and the sign-off gate in the `cutover-and-hypercare-checklist`.
- Recurring integration reconciliation checks for operations.

## Scale notes

### SMB

Counts by table and status, a few control totals and a business user clicking through a chosen sample is usually enough. The consultant prepares it and the customer's owner signs. Do not skip written sign-off, even if it is an email, because it settles questions about missing data after go-live.

### Enterprise

Reconciliation is scripted, runs automatically after every mock and the production load, and reports against tolerances fixed in the mock plan. Each business data owner signs per table, finance or internal audit may require evidence for financial records, and reconciliation status is a formal go/no-go criterion. Recurring integration checks feed operational monitoring and service reporting.

## Hand-offs

- `programme-management:go-no-go` receives signed acceptance and open exceptions.
- `support-operations:cutover-plan` includes reconciliation as a gate in the cutover runbook.
- `integration-and-data:data-mapping-and-cleansing` fixes rules behind unexplained variances.
- `platform-administration:monitoring` and `support-operations:support-model` take on recurring integration checks.
- Review: `security-compliance:data-retention` if reconciliation finds data that should not have been migrated.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Accept a matching total row count as proof that a migration is correct.
- Agree tolerances after the results are known.
- Let the project team sign acceptance on behalf of business data owners.
- Close a variance as explained without a recorded root cause and approver.
- Reconcile against a source that is still changing without a recorded as-at time.
