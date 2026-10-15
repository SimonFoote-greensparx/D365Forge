---
name: customer-assets-and-maintenance
description: Designs customer assets in Field Service, covering asset hierarchies, functional locations, asset data and properties, installed base migration, and preventive maintenance driven by time, usage or condition. Use when modelling equipment at customer sites, migrating an installed base, or planning maintenance against assets.
metadata:
  department: field-service
  stages: Initiate, Implement, Operate
  modules: Field Service, Customer Service
  status: draft
---

# Customer assets and maintenance

The installed base is where field service builds long-term value: knowing exactly what is installed where, its history and its condition makes first-time fixes, warranty decisions and preventive maintenance possible. Agents handling cases benefit too, because they can see the equipment the customer is calling about.

Projects usually go wrong by migrating a messy installed base unchanged, by building asset hierarchies many levels deep, and by recording every small part as an asset. Then nobody owns keeping the records current after each visit, and preventive maintenance plans are disconnected from the assets they are meant to protect.

## When to use

- Deciding what counts as a customer asset and what data to hold for it.
- Designing asset hierarchies and functional locations for customer sites.
- Planning installed base cleansing and migration.
- Designing preventive maintenance triggers by time, usage or condition.
- Making asset history visible to technicians and service agents.

Not this skill: `field-service:agreements-and-recurring-work` for the contracts that generate maintenance visits, `field-service:inventory-and-purchasing` for parts held in stock, `integration-and-data:mock-migrations` for rehearsing the data load.

## Questions to ask first

1. What equipment is serviced, and what must be known about each item, such as serial number, model, install date and warranty? This sets the asset data model.
2. Do assets sit in structured sites such as buildings, floors or production lines? This decides whether functional locations are needed.
3. Where is the installed base held today, and how reliable is it? This sizes the cleansing effort.
4. Is maintenance driven by time, usage or condition? Each needs a different trigger and data feed.
5. Who updates asset records after work: technicians, back office or automation? Without an owner the installed base decays.

## Approach

Customer assets represent equipment the organisation services at customer sites. They can be arranged in hierarchies, with a parent unit and its components, and placed in functional locations that describe the site structure. Work orders, cases and agreements can all reference an asset, which is what makes service history meaningful.

1. Decide what is an asset. Track as an asset anything you service, warrant, inspect or report on individually. Consumables and low-value parts do not need asset records. Decide whether parts installed during a job should become component assets automatically, and set that behaviour deliberately.

2. Keep hierarchies shallow. Two or three levels usually suffice; deeper trees slow technicians down and complicate reporting. Use functional locations for site structure (site, building, floor, room or line) and place top-level assets in them, rather than building location into the asset tree.

3. Define asset data. Agree a core set of fields such as category, product, serial number, install date and warranty end. For category-specific attributes and readings, check current Microsoft Learn documentation for asset property capabilities in your release before adding custom fields.

4. Cleanse before migrating. Legacy installed base data is often duplicated, mislocated or stale. Profile it, deduplicate by serial number and site, agree a cut-off for retired equipment, and map it in the `data-migration-mapping` with `integration-and-data:data-mapping-and-cleansing`.

5. Design maintenance triggers. Time-based maintenance is usually modelled through agreements generating recurring work orders against assets, see `field-service:agreements-and-recurring-work`. Usage- or condition-based maintenance needs readings, captured on inspections, fed from customer systems, or sent from connected devices; check current Microsoft Learn documentation for the supported IoT options before committing.

6. Keep records live. Make asset updates part of completing the job: technicians confirm serial numbers and record replacements and readings. Give the back office ownership of corrections.

7. Expose history. Show asset service history on the work order and the case, so technicians and agents can spot repeat failures.

## Outputs

- Asset and functional location model in the `solution-blueprint`.
- Installed base cleansing rules and migration map in the `data-migration-mapping`.
- Maintenance trigger design by asset category.
- Device or monitoring data feeds in the `integration-inventory`, where in scope.
- Technician asset update procedure in the `training-and-communications-plan`.

## Scale notes

### SMB

A flat list of assets per customer site with a few core fields, and time-based maintenance through agreements, usually covers the need. Do not skip deduplicating the installed base before loading it.

### Enterprise

Expect complex sites such as hospitals, campuses or plants, functional location hierarchies, connected devices, regulated inspection history and a large migration rehearsed through several mock runs. Keep customer assets distinct from the organisation's own fixed assets in ERP, and agree the retention of inspection and asset history.

## Hand-offs

- `field-service:agreements-and-recurring-work` for time-based maintenance generation.
- `integration-and-data:mock-migrations` to rehearse the installed base load.
- `integration-and-data:integration-architecture` for device and monitoring data feeds.
- Reviewer sign-off: `design-authority:design-review` for the asset model, and `security-compliance:data-retention` for retaining asset and inspection history.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Migrate the installed base without deduplicating by serial number and site.
- Create asset records for consumables or every small part.
- Build site structure into deep asset hierarchies instead of functional locations.
- Commit to condition-based maintenance before confirming the data feed and current platform support.
