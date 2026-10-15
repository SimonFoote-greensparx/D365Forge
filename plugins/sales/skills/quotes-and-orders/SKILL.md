---
name: quotes-and-orders
description: Designs the quote to order to invoice flow in Dynamics 365 Sales, covering quote revisions, discount approvals, document output, order capture and the point where an ERP takes over pricing, fulfilment or invoicing. Use when building quoting, deciding what CRM and ERP each own, or designing quote approval and generation.
license: CC-BY-4.0
metadata:
  department: sales
  stages: Initiate, Implement, Prepare
  modules: Sales
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Quotes and orders

Quoting is where the CRM touches money, which makes it the most sensitive process in the sales design. Dynamics 365 Sales can carry a deal from quote through order to invoice, but in most organisations the order and invoice belong to an ERP, and the hand-over point is the single most important decision in this area.

Projects go wrong when they build the full quote, order and invoice chain in CRM because the tables exist, then discover finance will never accept a CRM invoice. The opposite failure is just as common: quoting is left in spreadsheets outside the system, so the pipeline never shows what was actually offered.

## When to use

- Designing quote creation, revisions, activation and closing.
- Defining discount limits and approval routes for quotes.
- Producing customer-facing quote documents.
- Deciding whether orders and invoices are created in Dynamics 365, in an ERP, or both.
- Designing what happens when a deal is won: order creation, ERP hand-off and status feedback.

Not this skill: `sales:products-and-price-lists` for the catalogue and pricing structure, `integration-and-data:erp-and-project-touchpoints` for building the ERP integration, `sales:sales-process-stages` for where quoting sits in the opportunity flow.

## Questions to ask first

1. Which system issues the binding order and the invoice? This fixes the end of the CRM process and the direction of status updates.
2. Who can discount, by how much, and who approves exceptions? Approval rules are the main source of quoting customisation, so pin them down early.
3. How complex are quotes: simple line lists, configured solutions or recurring services? Complexity decides between the standard quote, a configure-price-quote add-on or a partner solution.
4. What must the customer receive, in which format and languages? Document generation choices depend on branding, signature and translation needs.
5. Do sellers and service teams need to see order, delivery and invoice status in CRM? Visibility without ownership shapes the return integration.

## Approach

Draw the line between CRM and ERP before configuring anything. A durable pattern is that Dynamics 365 owns the opportunity and the quote, the won quote creates an order that is sent to the ERP, and the ERP owns fulfilment, invoicing and payment while sending status back for visibility. Vary it only for a clear reason, and record the decision in the `integration-inventory`.

1. Use the standard quote lifecycle. Quotes move from draft to active, when they are locked for sending, and changes after that create a revision rather than editing what the customer saw. Closing a quote as won or lost keeps the history clean. Resist redesigning this; sellers and auditors understand it.
2. Keep quote pricing honest. Quote lines should come from the price list, with write-in products allowed only where the business accepts them. Line and quote discounts should respect agreed limits, enforced by a simple rule or an approval.
3. Build approvals with low-code first. A Power Automate approval raised when a quote exceeds a threshold, with thresholds and approvers held in a configuration table rather than hard-coded, covers most needs. Move to plug-ins only when an approval must block a transaction synchronously.
4. Generate documents with standard tools where you can. Word templates cover many quote documents; where branding, clauses or e-signature are demanding, assess a document generation add-on and test it with real multi-page quotes.
5. Decide the order's role. If the ERP is the order master, the CRM order is a request: create it from the won quote, lock its pricing, submit it through integration and make it read-only once accepted. If there is no ERP, Dynamics 365 orders and invoices can serve a small business, but agree that with finance in writing.
6. Bring status back. Account and opportunity views should show order, delivery and invoice state from the ERP, synchronised or surfaced virtually, so sellers stop phoning finance.

Microsoft offers standard integrations between Dynamics 365 Sales and its own ERP products. Check current Microsoft Learn documentation for what they synchronise today before designing anything custom.

## Outputs

- CRM and ERP ownership decision for quote, order and invoice, recorded in the `integration-inventory`.
- Quote lifecycle and approval design, including discount thresholds and approvers.
- Quote document templates and a sample output pack.
- Order hand-off specification with status feedback fields and the route for rejected orders.
- Quote to cash scenarios in the `test-strategy-and-uat-scripts`, run end to end with the ERP during SIT.

## Scale notes

### SMB

A small business with a simple accounts package can quote in Dynamics 365 and invoice in the accounts package, with a manual or lightly automated hand-off. Use the standard quote, one Word template and a single approval threshold. Do not skip agreeing where the invoice is raised with whoever runs finance, even if that is one person.

### Enterprise

Expect ERP ownership of orders and invoices, multi-entity and multi-currency quoting, and formal approval matrices. Run joint design sessions with the ERP team and `integration-and-data:erp-and-project-touchpoints`, prove quote to cash in `testing-quality:system-integration-testing`, and treat any configure-price-quote add-on as a separate decision through `design-authority:design-review`. Financial controls may require audit sign-off on who can change an approved quote.

## Hand-offs

`integration-and-data:erp-and-project-touchpoints` builds the order and status integration, with `integration-and-data:integration-architecture` choosing the pattern. Approval flows go to `platform-engineering:power-automate-patterns`. Custom pricing or approval plug-ins need `design-authority:customisation-challenge`, and restricting who can see or change discount and approval fields needs `security-compliance:field-level-security`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Raise invoices in Dynamics 365 when finance has not agreed it is the invoicing system.
- Let sellers edit an activated quote instead of revising it.
- Hard-code discount thresholds or approver names in flows or plug-ins.
- Send orders to the ERP without a defined path for rejected or failed orders.
