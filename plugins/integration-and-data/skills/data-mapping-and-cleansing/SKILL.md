---
name: data-mapping-and-cleansing
description: Produces the field-level mapping from legacy sources to Dataverse and the cleansing rules that make data loadable and trustworthy, covering deduplication, alternate keys, choice values, lookups and owners. Use when building the migration mapping, agreeing duplicate rules, or deciding how legacy codes map to choice columns.
license: CC-BY-4.0
metadata:
  department: integration-and-data
  stages: Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Data mapping and cleansing

The mapping is where migration effort really sits. Each row of it is a small decision about meaning, and every one deferred becomes a defect in a mock migration. Projects go wrong by mapping against a data model that is still changing, by treating cleansing as something the business will do later, and by loading duplicates on the assumption that duplicate detection will catch them afterwards.

Clean data also matters well beyond go-live. Copilot summaries, routing, segmentation and reporting all inherit whatever quality the migration delivers, so shortcuts here show up for years.

## When to use

- Building the field-level mapping from each source to the Dataverse model.
- Designing alternate keys, lookup resolution and owner mapping for loads.
- Mapping legacy codes to choice columns, and status values to state and status reason.
- Profiling source data and agreeing deduplication and cleansing rules with the business.

Not this skill: `integration-and-data:migration-strategy` for scope, tooling and load order, `solution-architecture:cross-module-data-model` for designing the target model, `integration-and-data:reconciliation` for proving what was loaded.

## Questions to ask first

1. Is the target data model stable enough to map against? Mapping against a moving model creates rework every sprint.
2. What identifiers exist in each source, and are they unique and stable? They become alternate keys and the basis for re-runnable loads.
3. Who in the business can decide which duplicate survives and what a legacy code means? Without a named decision-maker, cleansing stalls.
4. Which quality problems can be fixed in the source before extract? Fixing at source is cheaper and keeps systems consistent during any coexistence period.
5. What does good enough look like per table? Agreed quality thresholds give reconciliation something to test against.

## Approach

Map at field level in the `data-migration-mapping` template. Each row holds source system, table and column; target table and column by logical name; data type and length; transformation rule; default when blank; whether mandatory; cleansing rule; and the business owner who agreed it. Version the mapping and rebaseline it whenever the data model changes.

Keys and lookups:

1. Give every migrated table an alternate key holding the legacy identifier, or a composite of source system and legacy identifier where several sources feed one table. Upserting on that key makes loads re-runnable and lets lookups resolve without querying for GUIDs.
2. For each lookup, define the resolution key and the behaviour when the referenced row is missing: reject the row, link to a documented placeholder, or leave it blank and log it.
3. Map owners to users or teams with an explicit fallback, and keep the legacy owner value in staging for audit.

Choice columns: build an explicit value map from legacy codes to Dataverse choice values, with a rule for unmapped codes. Map to the integer value, never the label, because labels are translated and renamed. Use global choices where the same list appears on several tables. State and status reason need their own map, since only certain combinations are valid and closed states often have to be set after the row is created.

Cleansing:

1. Profile before writing rules: null rates, value distributions, invalid formats, orphaned children and suspected duplicates per table. Share the profile with the business so the scale of the problem is visible early.
2. Deduplicate in staging, before load, using match rules the business has agreed, such as normalised organisation name with postcode, or email address for contacts. Decide which record survives, which fields win, and how children of the losing record are reparented. Have a business user review a sample of proposed merges before any rule is applied in bulk.
3. Standardise formats: countries and regions to one list, phone numbers to one format, email addresses validated, addresses split into the structured columns.
4. Decide where each fix happens. Fix at source when only the business knows the answer, by rule in staging when it is repeatable, and after go-live only for low-value fields with a named owner and date.
5. Minimise. Drop columns no process uses, especially personal data.

Configure Dataverse duplicate detection rules for ongoing data entry after go-live; do not rely on them to clean a bulk load, and check current Microsoft Learn documentation for how they apply to API-based loads.

## Outputs

- Completed `data-migration-mapping` per table, with transformation and cleansing rules and their owners.
- Choice value maps and state and status reason maps.
- Alternate key definitions for each migrated table, passed to configuration.
- Data profiling report and cleansing log showing issue, rule, owner and status.
- Deduplication rules and survivorship decisions signed by the business data owner.
- Duplicate detection rules to configure for business-as-usual data entry.

## Scale notes

### SMB

The consultant usually maps and the customer's administrator or office manager makes the cleansing decisions. Spreadsheet sources are common, and fixing them at source before extract is often fastest. Keep the mapping in one workbook. Do not skip the legacy identifier on each record or the duplicate review; small databases are often the worst for duplicates.

### Enterprise

Data analysts own mappings per source, with a data quality lead and named business data owners per table. Expect several sources feeding one customer table, so matching and survivorship rules need formal agreement and possibly a master data management decision. Mappings go under change control, and changes to the data model trigger a mapping impact review.

## Hand-offs

- `integration-and-data:mock-migrations` runs the mappings at volume.
- `integration-and-data:reconciliation` tests the results against the agreed thresholds.
- `platform-engineering:solution-layering` carries alternate keys and duplicate detection rules into solutions.
- Reviews: `design-authority:standards-conformance` for key and naming conventions, and `security-compliance:data-retention` for personal data carried across.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Map choice values by label text instead of by value.
- Load rows without a stable legacy identifier stored on the target record.
- Merge duplicates in bulk on fuzzy matching without a business-approved rule and a sample review.
- Invent default values for mandatory columns without the business owner's agreement.
- Carry personal data columns into Dataverse that no process uses.
