---
name: inventory-and-purchasing
description: Designs Field Service inventory and purchasing, covering the system of record with ERP, product types, warehouses and van stock, usage recording, transfers and adjustments, purchase orders and receipts, and returns. Use when deciding how parts are tracked, ordered and returned, or how Field Service inventory relates to ERP.
metadata:
  department: field-service
  stages: Initiate, Implement, Prepare
  modules: Field Service
  status: draft
---

# Inventory and purchasing

Parts are one of the most common reasons a job is not fixed on the first visit, and parts usage is where field service meets finance. Field Service has long-established inventory and purchasing capabilities, but whether to use them is mostly decided by the ERP, not by Field Service.

Projects usually go wrong in the middle ground: both Field Service and ERP hold editable stock levels for the same items, and neither is right. Van stock is modelled as a warehouse but never counted, returns run on email and goodwill, and the product catalogue in Dynamics 365 drifts from item numbers and units in ERP.

## When to use

- Deciding which system masters items, stock, purchasing and costs.
- Classifying products and aligning them with ERP.
- Modelling warehouses, including vans, and how stock moves.
- Designing parts usage on work orders, purchasing for jobs and returns.
- Planning stock counts and opening balances at cutover.

Not this skill: `integration-and-data:erp-and-project-touchpoints` for the integration design with ERP, `sales:products-and-price-lists` for sales catalogue and pricing, `field-service:customer-assets-and-maintenance` for equipment installed at customer sites.

## Questions to ask first

1. Which system is the system of record for items, stock, purchasing and costs? This decides whether Field Service inventory is used at all.
2. Are vans stocked, and is van stock counted and replenished? Only counted stock can be modelled as a warehouse.
3. How do technicians get parts not on the van? This decides purchase orders, transfers or collection.
4. How are customer returns, faulty parts and supplier returns handled today? Returns need owners and statuses.
5. Are parts serial-numbered or installed as customer assets? This links inventory to the installed base.

## Approach

Field Service provides warehouses, inventory journals, transfers, adjustments, purchase orders with receipts and bills, and return processes. The first decision, recorded in the `integration-inventory` and the `solution-blueprint`, is which system masters each object.

1. Decide the system of record per object. Where an ERP is in place, it typically masters items, costs, warehouses, purchasing and financial postings, while Field Service consumes the product catalogue and records usage on work orders. Organisations without a capable ERP may run inventory and purchasing in Field Service. Avoid both systems holding editable stock for the same item and location. Agree the integration approach with `integration-and-data:erp-and-project-touchpoints`, and check current Microsoft Learn documentation for the supported options between Field Service and Microsoft ERP products.

2. Classify products. Product type (inventory, non-inventory or service) decides whether usage moves stock. Align item numbers, units of measure and price lists with ERP before loading.

3. Model warehouses. Model a van as a warehouse only if its stock is counted and replenished; otherwise usage figures cannot be trusted. Define central and regional warehouses to match how stock really moves.

4. Design usage recording. Technicians record parts used against the work order; estimated parts from the incident type become used when confirmed. Decide when usage reaches inventory and ERP: at completion, or after back-office review at posting.

5. Design purchasing for jobs. Decide where purchase orders are raised, who approves them, how receipts are recorded, and how special-order parts stay linked to the job that needs them. Keep ordering and receiving approvals with different people where financial controls require it.

6. Design returns. Customer returns, faulty parts back to suppliers and warranty claims each need an owner and a status path. The standard return processes only work if the warehouse team uses them every time.

7. Count and reconcile. Plan cycle counts for vans and warehouses, reconcile Field Service and ERP on a fixed cadence, and take opening balances from a stock count close to cutover.

## Outputs

- System-of-record decision per object in the `integration-inventory`.
- Warehouse, van and product model in the `solution-blueprint`.
- Product and opening stock data in the `data-migration-mapping`.
- Purchasing and returns process maps with owners.
- Stock count and opening balance steps in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Often there is only an accounting package. Either run simple inventory in Field Service with vans as warehouses, or skip inventory and record parts used for billing only. Do not skip the system-of-record decision or the van counting routine if vans are modelled.

### Enterprise

ERP usually masters inventory and purchasing across several legal entities, with serial numbers, warranty recovery and procurement approvals. Field Service focuses on usage and requests, the integration carries stock and cost, and segregation of duties for purchasing is reviewed by security-compliance.

## Hand-offs

- `integration-and-data:erp-and-project-touchpoints` designs the inventory, purchasing and costing integration.
- `integration-and-data:data-mapping-and-cleansing` aligns products and opening balances.
- `support-operations:cutover-plan` schedules the cutover stock count.
- Reviewer sign-off: `design-authority:design-review` for the system-of-record decision, and `security-compliance:security-model-review` for purchasing approvals and segregation of duties.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Hold editable stock levels for the same item and location in both Field Service and ERP.
- Model vans as warehouses without a counting and replenishment routine.
- Load products without aligning item numbers and units of measure with ERP.
- Go live without opening stock balances from a recent count.
