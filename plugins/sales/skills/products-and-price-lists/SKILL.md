---
name: products-and-price-lists
description: Designs the product catalogue in Dynamics 365 Sales, including product families, bundles, unit groups, price lists, discount lists and currencies, and decides whether CRM or ERP owns products and pricing. Use when structuring products, setting up price lists per market, or planning catalogue synchronisation with an ERP.
license: CC-BY-4.0
metadata:
  department: sales
  stages: Initiate, Implement, Prepare
  modules: Sales, Field Service
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Products and price lists

The product catalogue sits underneath opportunities, quotes, orders and, in Field Service, work orders, so a weak structure leaks into every downstream process. It is also the area where CRM and ERP most often disagree about who is the master, which turns a configuration task into an integration decision.

Projects usually go wrong by importing the full ERP item master into Dataverse, thousands of codes nobody sells directly, or by building a pricing engine in CRM that duplicates rules finance already maintains. The catalogue should hold what sellers need to shape a deal, and no more.

## When to use

- Structuring product families, products, bundles, properties and product relationships.
- Designing unit groups, units and default units.
- Setting up price lists by market, channel or customer tier, with discount lists and currencies.
- Deciding whether Dynamics 365 calculates prices or receives them from an ERP.
- Planning the initial catalogue load and ongoing synchronisation.

Not this skill: `sales:quotes-and-orders` for the documents that use the catalogue, `integration-and-data:erp-and-project-touchpoints` for building the ERP integration, `field-service:inventory-and-purchasing` for stock, warehouses and purchasing.

## Questions to ask first

1. Which system is the master for products and prices today, and will that change? This decides whether the catalogue is maintained in Dynamics 365 or arrives read-only through integration.
2. How many sellable items are there, and how often do prices change? Volume and rate of change decide between manual upkeep, imports or integration.
3. Are prices fixed by list, negotiated per deal or set by customer agreement? Negotiated pricing needs discount controls and approvals; agreements may need customer-specific price lists.
4. Which currencies and units of measure do sellers quote in? Currencies and unit groups are structural and expensive to change once transactions exist.
5. Do Field Service or Customer Service use the same products? A shared catalogue needs one owner and agreed product types.

## Approach

Treat the catalogue as something to design, not a table to fill. Start from how sellers describe what they sell in a customer conversation, then map that to the ERP item master, rather than the other way round.

1. Decide the master first. If an ERP owns items and prices, Dynamics 365 receives a curated subset through integration and sellers cannot edit it. If the CRM owns the sales catalogue, finance must accept it as the source for quoting. Record the decision in the `integration-inventory` before any product is created.
2. Use families for structure and properties for variation. Families group products for navigation and reporting and let child products inherit properties such as size or service level. Avoid creating a separate product for every combination when a property on the quote line would do.
3. Use bundles for items sold together, and treat product kits as a legacy construct; check current Microsoft Learn documentation before relying on them. Product relationships (up-sell, cross-sell, accessory, substitute) are cheap to set up and help sellers and suggestion features alike.
4. Keep unit groups simple. Create one unit group per genuine measurement family (each, box, pallet; hour, day) and resist one unit group per product.
5. Design price lists around how prices really differ, usually by currency, market or channel. Choose the pricing method for price list items deliberately, use discount lists for volume breaks rather than extra products, and set default price lists by territory where the business allows it.
6. Decide where calculation happens. The standard system pricing calculation suits list-based selling. When an ERP holds complex pricing, either bring prices in through integration or replace the calculation with custom pricing logic, which is a design authority decision because it changes upgrade and support risk.
7. Plan the publish and retire lifecycle. Products are normally created in draft and published before sellers can use them, and retiring rather than deleting keeps transaction history intact.

Load the catalogue into a test environment first and build a sample quote for each major product family before anyone signs off the structure.

## Outputs

- Catalogue design covering families, product types, properties, bundles and relationships, recorded in the `solution-blueprint`.
- Unit group and currency register.
- Price list and discount list matrix by market, channel or tier.
- Master data ownership decision for products and prices in the `integration-inventory`.
- Product and price list entries in the `data-migration-mapping`.

## Scale notes

### SMB

A small business often has a few dozen products and one price list, maintained by the sales manager directly in Dynamics 365. Keep to one currency unless there is genuine cross-border selling, one or two unit groups and no custom pricing. Do not skip naming who maintains prices after go-live, because an unowned catalogue goes stale quickly.

### Enterprise

Expect ERP ownership, several currencies and regional price lists, with a product data steward and a formal change process for catalogue updates. Synchronisation should be designed and tested with `integration-and-data:erp-and-project-touchpoints`, and any custom pricing logic needs `design-authority:customisation-challenge`. Coordinate with Field Service so service products, parts and labour share product types and units with sales.

## Hand-offs

`sales:quotes-and-orders` uses the catalogue for quoting and order capture. ERP synchronisation of items and prices goes to `integration-and-data:erp-and-project-touchpoints`, and the initial catalogue load to `integration-and-data:data-mapping-and-cleansing`. Who may edit products and price lists is a `security-compliance:security-model-review` question, and custom pricing logic needs sign-off from `design-authority:customisation-challenge`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Import the whole ERP item master when sellers only quote a subset.
- Let sellers edit prices in Dynamics 365 when an ERP is the agreed pricing master.
- Delete products or price lists that have been used on transactions; retire them instead.
- Replace the system pricing calculation without a design authority decision.
