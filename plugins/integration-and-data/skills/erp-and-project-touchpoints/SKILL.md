---
name: erp-and-project-touchpoints
description: Defines, from the CRM side, what crosses between Dynamics 365 CE and the ERP or Project Operations, covering customers, products and pricing, orders, invoices, inventory and time. Use when agreeing master data ownership with finance, scoping quote to cash or time to billing, or deciding whether dual-write applies.
license: CC-BY-4.0
metadata:
  department: integration-and-data
  stages: Strategize, Initiate, Implement
  modules: Sales, Customer Service, Field Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# ERP and project touchpoints

The CRM and the ERP both believe they own the customer. Projects go wrong by letting sellers create accounts the ERP will not accept, by copying price lists that drift within weeks, and by replicating stock levels that are stale by the time anyone quotes from them. The CRM team often assumes finance will sort out the ERP side, and finance assumes the opposite, so the boundary is designed by nobody.

Dual-write tends to be mentioned in early workshops whatever the ERP is. It is specific to the Dynamics 365 finance and operations apps. With any other ERP, every touchpoint is an ordinary integration that has to be designed, built and supported.

## When to use

- Agreeing which system masters customers, products, prices, payment terms and credit, and when a CRM account becomes a trading customer.
- Scoping quote to cash: where quotes, orders and invoices are created and where their status is visible.
- Deciding how sellers, service agents and technicians see stock, credit status and invoices.
- Routing Field Service or Project Operations time, expenses and material usage to finance.

Not this skill: `integration-and-data:integration-architecture` for patterns and technology, `sales:quotes-and-orders` and `sales:products-and-price-lists` for the CRM configuration itself, `field-service:inventory-and-purchasing` for Field Service inventory design.

## Questions to ask first

1. Which ERP is it, and is it a Dynamics 365 finance and operations app? This decides whether dual-write and the native Field Service and Project Operations integrations are options at all.
2. At what point does a prospect become a trading customer, and who approves it? Credit control usually owns this, and the CRM process must hand over cleanly.
3. Where is price calculated: CRM price lists, the ERP pricing engine, or both? Discounts and trade agreements calculated in two places will disagree.
4. Where does an order originate: CRM, the ERP or an e-commerce channel? This sets the direction of flow and the master for order status.
5. What do CRM users need to see from the ERP, as opposed to act on? Seeing invoice history rarely justifies copying invoices into Dataverse.

## Approach

Work entity by entity from the CRM side. For each, write down the master, the event that makes data cross, the direction, and what CRM users may still edit afterwards. These defaults hold up on most projects:

1. Customers. CRM masters prospects and relationship data (contacts, activities, hierarchy, segmentation). The ERP masters trading customers, credit limits, payment terms and tax details. Create the ERP customer at a defined event (won opportunity, first order or credit approval), write the ERP account number back as an alternate key on the CRM account, and make the finance fields read-only in CRM from then on.
2. Products and pricing. The ERP is normally the product master. Push products, units and price lists into Dataverse so sellers can quote without leaving CRM, but agree whether CRM may add discounts or bundles and how often prices refresh. Where pricing logic is genuinely complex, call the ERP at quote time instead of rebuilding its rules in plug-ins.
3. Orders and invoices. Let quotes and draft orders start in CRM if sellers need them, but once submitted the order belongs to the ERP; return status, shipment and invoice summaries to CRM. Invoices suit a virtual table or embedded view better than a full copy.
4. Inventory. Look up availability on demand rather than replicating on-hand quantities for sellers. Field Service is different: technicians consume parts and warehouse movements must post back, so design that with the Field Service team.
5. Time and expenses. Field Service and Project Operations capture time, expenses and material usage that finance needs for billing, payroll and project accounting. Use approval as the trigger to cross, and treat the ERP as master once posted.

Then choose the mechanism. With finance and operations apps, evaluate dual-write and the native Field Service and Project Operations integration options, checking current Microsoft Learn documentation for supported table maps, initial synchronisation, prerequisites and which Project Operations deployment scenario applies. Dual-write couples the two systems closely, so test what users experience when either side is unavailable or a map is paused. With any other ERP, route each touchpoint through `integration-and-data:integration-architecture` like any other interface, using the ERP account number and product number as alternate keys so messages are idempotent.

Finally, walk the end-to-end process with both teams in the room: a prospect becoming a customer, a quote becoming an order and an invoice, a technician's time becoming a bill. Each hand-over point should name the status that triggers it and the team that fixes it when it fails.

## Outputs

- Master data ownership matrix by entity and field, signed by sales operations and finance.
- ERP touchpoint rows in the `integration-inventory`, one per entity and direction.
- Quote-to-cash and time-to-billing process flows showing where each status lives.
- Dual-write or native integration decision, where finance and operations apps are in scope, recorded in the `solution-blueprint`.
- Open ownership questions and ERP team dependencies in the `raid-log`.

## Scale notes

### SMB

Often a small accounting or ERP package and one person who knows it well. Keep crossing points few: customer creation, product and price refresh, and invoice visibility. Re-keying low volumes of orders can be acceptable if it is a deliberate, documented decision with a review date. Do not skip the master data ownership agreement; it takes an hour and prevents months of duplicate customers.

### Enterprise

CRM and ERP programmes often run on different calendars, so agree a joint integration backlog, shared test environments and one defect process. Expect a finance data owner per master entity, design authority review of any field mastered in two places, and integration testing that proves ERP posting, not just message delivery. Where finance and operations apps are in scope, environments for dual-write must be linked in step with the environment strategy.

## Hand-offs

- `integration-and-data:integration-architecture` for patterns, error handling and monitoring.
- `sales:products-and-price-lists`, `sales:quotes-and-orders` and `field-service:inventory-and-purchasing` configure the CRM side.
- `solution-architecture:cross-module-data-model` reflects the ownership decisions in the data model.
- `testing-quality:system-integration-testing` covers quote to cash and time to billing end to end.
- Reviews: `design-authority:design-review` for ownership and mechanism decisions, and `security-compliance:security-model-review` for financial data made visible in CRM.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Let CRM and the ERP both edit customer financial fields after the customer exists in the ERP.
- Replicate on-hand inventory into Dataverse for sellers to quote from.
- Propose dual-write for an ERP that is not a Dynamics 365 finance and operations app.
- Rebuild ERP pricing rules in CRM plug-ins or flows without the finance owner's agreement.
- Treat message delivery as proof that an order or time entry posted correctly in the ERP.
