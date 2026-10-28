---
name: customer-profile-unification
description: Designs unified customer profiles in Customer Insights - Data, covering source selection, source mapping, deduplication, match rules, merge policies and use of profiles in journeys and Dynamics 365 apps. Use when combining customer data from several systems, tuning match rules, or deciding whether Customer Insights - Data is needed at all.
license: CC-BY-4.0
metadata:
  department: marketing
  stages: Strategize, Initiate, Implement, Operate
  modules: Marketing, Sales, Customer Service
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Customer profile unification

Customer Insights - Data brings customer records from several systems into one unified profile, so marketing, sales and service can target and personalise using the whole relationship rather than one system's view. Unification is a chain of decisions: which sources to bring in, how to map them, how to remove duplicates within each source, how to match across sources and how to merge fields into a single profile.

Projects go wrong by loading every available source on the theory that more data is better, by accepting default matching without testing it against known customers, or by buying the product when customer data already lives almost entirely in Dataverse. Poor matching stays invisible until two different people receive each other's personalised email.

## When to use

- Deciding whether Customer Insights - Data is needed beyond Dataverse contacts.
- Selecting and preparing data sources for unification.
- Designing source mapping, deduplication, match rules and merge policies.
- Testing and tuning match quality.
- Making unified profiles available to Customer Insights - Journeys and Dynamics 365 apps.

Not this skill: `marketing:segments-and-audiences` for building audiences on profiles, `integration-and-data:data-mapping-and-cleansing` for cleansing data in source systems, `data-and-ai:fabric-link` for analytics on Dataverse data in Microsoft Fabric.

## Questions to ask first

1. Which use cases need data that is not already in Dataverse? If there are none, unified profiles may add cost without value.
2. Which sources hold customer data, and which identifiers do they share? Shared identifiers decide how reliable matching will be.
3. How good are names, emails, phone numbers and addresses in each source? Normalisation and fuzzy matching only partly make up for poor data.
4. Which source is most trusted for each field? Merge precedence depends on it.
5. What lawful basis and purposes allow these sources to be combined? Combining data for profiling raises data protection questions for the DPO, and licensing and capacity should be confirmed with the Microsoft licensing guide or your partner.

## Approach

Start from use cases, not sources. List the decisions unified profiles will improve (a segment, a personalisation, a measure, a service view) and the data each one needs. Bring in only the sources those use cases require, and add more when a new use case justifies them.

1. Prepare sources. Connect each source through a supported connector or data lake, and fix obvious quality problems at source where you can. Check current Microsoft Learn documentation for supported source types and refresh options.
2. Map sources. For each table, identify the primary key, the fields used for matching and the meaning of key fields such as email, phone and name. Leave out fields nobody needs; they slow unification and widen the data protection footprint.
3. Deduplicate within each source first. Define rules that collapse duplicates inside a source and decide which record wins, usually the most recently updated or the most complete.
4. Design match rules across sources. Order sources from most to least reliable, start with exact matches on strong identifiers such as customer number or verified email, then add normalised or fuzzy rules on name and address for what remains. Each extra rule should earn its place through a measured gain.
5. Test match quality. Build a sample of known customers with expected outcomes, including awkward cases such as shared household emails, company switchboard numbers and name changes. Review false and missed matches, then tune. False matches are usually worse than missed ones, because they mix two people's data.
6. Define merge policies. For each unified field choose the winning rule, such as most trusted source or most recent value, and decide which fields are combined rather than chosen.
7. Publish and use. Make profiles available to Customer Insights - Journeys segments and, where useful, to sellers and service agents in Dynamics 365 apps, on refresh schedules that suit the use cases.

Document every rule and the reason for it. Unification decisions are hard to reverse once journeys and reports depend on them.

## Outputs

- Use case to source matrix justifying each data source.
- Source mapping, deduplication, match and merge design, recorded in the `solution-blueprint`.
- Match quality test set and results.
- Source entries with refresh schedules in the `integration-inventory`.
- Data protection questions for the DPO, tracked in the `raid-log`.

## Scale notes

### SMB

Many small organisations do not need Customer Insights - Data; if customer data lives mainly in Dataverse, segments on contacts are enough. Where it is justified, keep to two or three sources and exact matching on email or customer number. Do not skip the match quality test or the DPO check on combining sources.

### Enterprise

Expect many sources, a data platform team, a data steward per domain and a formal process for adding sources. Match rules and merge policies should be reviewed through `design-authority:design-review` and aligned with the wider analytics estate. Run unification and refresh monitoring as an operational service, and ask the DPO early whether a data protection impact assessment is needed.

## Hand-offs

`marketing:segments-and-audiences` and `marketing:journey-design` use the profiles, `integration-and-data:integration-architecture` and `integration-and-data:data-mapping-and-cleansing` prepare the sources, and `data-and-ai:fabric-link` aligns profiles with the wider analytics estate. Combining sources for marketing needs `security-compliance:marketing-consent-compliance` sign-off, and retention of profile data goes to `security-compliance:data-retention`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Load every available source without a use case for it.
- Accept match rules without testing them against known customers.
- Write merged profile values back into source systems without an agreed master data decision.
- Combine data sources for profiling without a lawful basis and purpose approved by the DPO.
