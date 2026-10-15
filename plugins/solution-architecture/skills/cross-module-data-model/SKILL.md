---
name: cross-module-data-model
description: Designs the shared Dataverse data model that Sales, Customer Service, Field Service and Customer Insights all build on, settling the customer spine, reuse of standard tables, column ownership and keys. Use when a module proposes new tables or shared columns, when a custom table may duplicate a standard one, or before a data model review.
metadata:
  department: solution-architecture
  stages: Initiate, Implement
  modules: All
  status: draft
---

# Cross-module data model

Every Dynamics 365 CE app writes to the same Dataverse tables. The account that sales qualifies is the account a case is raised against, the service account on a work order and the organisation a marketing journey targets. The data model is therefore a shared asset, and a decision made by one workstream constrains every other one, including modules that will not arrive until a later phase.

The usual failure is local optimisation. The service team adds a custom site table because functional locations looked unfamiliar, sales adds a customer tier column while marketing adds a segment column holding the same fact, and a phase one custom client table has to be migrated away from when Field Service arrives. Each choice looked reasonable alone; together they produce duplicate data, broken reporting and a costly rework.

## When to use

- A workstream proposes a new table, or a new column on a shared table such as account, contact or product.
- A second module is joining an existing Dataverse estate and must reuse what is already there.
- Customer Insights - Data or Customer Insights - Journeys is being added to an estate that already holds sales or service data.
- A data model review is due, or migration mapping keeps finding the same fact stored in two places.

Not this skill: `marketing:customer-profile-unification` for unification rules in Customer Insights - Data, `integration-and-data:data-mapping-and-cleansing` for source-to-target mapping, `security-compliance:business-units-and-teams` for ownership and access structure, and `solution-architecture:extend-or-configure` for whether a gap should be built at all.

## Questions to ask first

1. Which modules are in scope now and which are planned later? Designing for later modules now avoids reworking tables and migrations.
2. Is the business B2B, B2C or both? This decides whether account or contact anchors the model and how households or sites are represented.
3. Which system masters customers, products and installed assets? ERP often masters some of these, and Dataverse must not compete with it.
4. What volumes are expected per table over the life of the system? Volume affects ownership type, relationship behaviour and archival.
5. How is the organisation divided across countries, brands or business units? This shapes ownership, security and whether data is shared or partitioned.

## Approach

Start from the standard model and justify every departure from it. Standard tables carry behaviour that custom tables do not: timeline and activities, connections, Dataverse search, Copilot grounding, first-party app logic and whatever Microsoft adds next. A custom table that duplicates one of them gives all of that up permanently.

1. Fix the customer spine. Account and contact are shared by every app. Leads belong to sales and marketing, opportunities to sales, cases to service, and work orders and bookings to Field Service. Map each module's core tables to the spine (case to customer, work order to service account and billing account, customer asset to account and functional location) and confirm there is no second customer table anywhere. For B2C, model consumers as contacts; there is no separate person-account construct to fall back on.
2. Share the product catalogue. Sales quoting and Field Service parts and services draw on the same products, units and price lists. Agree one catalogue structure and one master system for it.
3. Give every shared column an owner. Keep a register of custom columns on account, contact and product with the owning workstream, purpose and master system. Before anyone creates a column, they search the register for something that already holds the fact. Use global choices for values that more than one module uses.
4. Decide ownership and relationship behaviour up front. A table's ownership type (user or team, or organisation) cannot be changed after the table is created. Set cascade behaviour on each relationship deliberately, because cascading assign or share across large account hierarchies is slow and quietly widens access.
5. Plan keys for integration and migration. Add alternate keys for external identifiers such as ERP customer numbers, and record which system masters each key.
6. Place Customer Insights correctly. Treat unified profiles in Customer Insights - Data as an enriched view that links back to contact and account, not as a replacement for them. Check current Microsoft Learn documentation for how profiles, segments and consent records surface in Dataverse.
7. Use the activity model. Record interactions as standard activities or custom activity tables so they appear on the timeline, in reporting and in Copilot summaries.

## Outputs

- Data model chapter of the `solution-blueprint`, with an entity relationship diagram covering every in-scope and planned module.
- A table and column register naming the owning workstream, purpose and master system for each component.
- Alternate key and master-system decisions that feed the `integration-inventory` and the `data-migration-mapping`.
- A log of approved exceptions where a custom table was justified, with the reason.

## Scale notes

### SMB

Usually one or two apps and one consultant. Keep the column register as a simple sheet, but keep it: the second module is when its absence hurts. The rule that must not be skipped is a single customer spine, because unwinding a duplicate customer table after go-live means migrating live data.

### Enterprise

A data architect owns the model across workstreams, and new tables or shared columns need design authority approval. Hold a data model review before each phase's build and a lightweight check each sprint that new components appear in the register. Involve the Customer Insights team early, because profile unification depends on consistently keyed account and contact data.

## Hand-offs

`integration-and-data:data-mapping-and-cleansing` and `integration-and-data:migration-strategy` use the model for mapping and load design, `platform-engineering:solution-layering` decides which solution owns each table, and `security-compliance:business-units-and-teams` builds access on the ownership choices. Sign-off comes from `design-authority:design-review`, with `security-compliance:security-model-review` wherever ownership or cascade behaviour changes access.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create a custom table that duplicates account, contact, lead, case, work order or customer asset.
- Let each module team add its own column for a fact another team already stores.
- Create a table before deciding whether it is user, team or organisation owned.
- Set cascade assign or share on large hierarchies without assessing the performance and access impact.
- Treat Customer Insights - Data profiles as a second customer master.
