---
name: lead-to-opportunity
description: Designs how leads are captured, qualified, disqualified and converted into accounts, contacts and opportunities in Dynamics 365 Sales. Use when deciding whether to use leads at all, defining qualification evidence, setting what qualify creates and how duplicates are caught, or tidying lead ownership and disqualify reasons.
license: CC-BY-4.0
metadata:
  department: sales
  stages: Initiate, Implement, Operate
  modules: Sales
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Lead to opportunity

The lead table is where marketing effort turns into sales pipeline, and it is the first place a Dynamics 365 Sales design shows whether the business has agreed what qualified means. Get it wrong and sellers either skip leads entirely and create opportunities from nothing, or the lead list becomes a pile of untouched records that nobody trusts.

Most projects go wrong by copying the old CRM's statuses, letting qualification create duplicate accounts and contacts, and leaving disqualify reasons as free text. The result is a funnel that cannot be reported on and a marketing team that never learns which leads were good.

## When to use

- Deciding whether a business needs leads at all, or should start sales work at the opportunity.
- Defining qualification evidence, lead statuses and disqualify reasons.
- Designing what happens on qualify: which records are created, matched or reused.
- Setting lead ownership, assignment and follow-up rules, and lead source tracking.
- Planning which open leads move across from a legacy CRM.

Not this skill: `marketing:lead-scoring-and-sales-handoff` for scoring models and the marketing to sales threshold, `sales:sales-process-stages` for the stages after qualification, `sales:sequences-and-sales-accelerator` for seller cadences on new leads.

## Questions to ask first

1. Where do leads come from (web forms, events, partners, inbound calls, bought data) and in what volumes? The mix decides whether leads earn a separate table or are just noise in front of opportunities.
2. Who qualifies: marketing, an inside sales or business development team, or the account owner? This sets ownership, security and the point at which the hand-off is measured.
3. What does qualified mean in this business, written as checkable facts? Without an agreed definition, conversion rates mean nothing and every seller applies private rules.
4. Is the business mostly selling to new organisations or growing existing accounts? Existing-customer selling often bypasses leads and needs strong account matching instead.
5. Is Customer Insights - Journeys in scope now or later? If so, lead creation, matching and scoring must be designed together with marketing.

## Approach

Start by deciding whether leads earn their place. Where nearly every enquiry comes through an existing account relationship, forcing a lead first adds clicks and teaches people to work around the system. Where volume comes from forms, events and campaigns, the lead is valuable because it keeps unqualified people out of the account and contact tables. Make the decision per route to market, not once for the whole company.

1. Define qualification as evidence. Replace adjectives with fields a seller can complete: budget understood, decision maker identified, need confirmed, timescale within an agreed horizon, or whatever framework sales leadership already uses. Put those fields on the lead form and in the first stage of the lead business process flow so qualification is visible rather than remembered.
2. Design the qualify action deliberately. Qualifying a lead can create an account, a contact and an opportunity. Decide which of the three are created in each scenario, and make sure duplicate detection prompts the seller to link to an existing account or contact rather than creating a second one. Check current Microsoft Learn documentation for the settings that control what qualify creates and when duplicates are checked.
3. Map lead fields forward. Use the relationship mappings so source, campaign, product interest and qualification notes travel to the opportunity. A field that does not map is lost to reporting at the exact point the funnel is measured.
4. Make disqualification a reportable outcome. Replace free text with a short, agreed list of status reasons (no budget, no response, lost to competitor, not a fit, duplicate) and share the totals with marketing every month.
5. Fix ownership and assignment. Decide whether leads land in a team or queue first and are then assigned, and what happens to leads nobody touches within the agreed time. Assignment should use territory, product and declared skills, never personal characteristics.
6. Agree a rule for stale leads. Open leads that sit for ever distort every report, so agree when an untouched lead is closed and how long disqualified leads are kept, and take the retention question to `security-compliance:data-retention`.

Migrate only open leads with recent activity and a clear owner. Old disqualified leads rarely justify the cleansing effort, and they often carry consent questions that marketing and the DPO should answer first.

## Outputs

- Lead lifecycle definition: sources, statuses, status reasons, qualification evidence and conversion outcomes.
- Qualify behaviour specification: records created per scenario, duplicate detection rules and field mappings.
- Lead assignment and follow-up rules, including the route for untouched leads.
- Lead entries in the `data-migration-mapping` for open leads moving from the legacy CRM.
- Lead to opportunity scenarios in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

One consultant usually designs this with the sales manager in a single workshop. Keep the standard lead form, add only the qualification fields the manager will actually check, and use simple territory or round-robin assignment. Do not skip duplicate detection on qualify; small teams that share every account feel duplicate records first.

### Enterprise

Expect several routes to market with different rules, so document one lead lifecycle per route around a shared core of statuses and reasons. A sales operations owner should hold the definition of qualified, and changes should go through `design-authority:change-impact-assessment` because they move forecast and marketing measures. Plan lead queues and assignment volumes alongside the marketing and service workstreams so routing rules do not collide.

## Hand-offs

Upstream, `marketing:lead-scoring-and-sales-handoff` defines when a marketing lead is sales-ready and what journey context travels with it. Downstream, `sales:sales-process-stages` picks up the opportunity and `sales:sequences-and-sales-accelerator` handles follow-up cadences. Lead migration goes to `integration-and-data:data-mapping-and-cleansing`. Lead visibility across teams needs `security-compliance:security-model-review`, and custom qualify logic beyond configuration goes through `design-authority:customisation-challenge`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Auto-qualify leads without an agreed, documented qualification rule.
- Let qualify create new accounts and contacts with duplicate detection switched off.
- Record disqualify reasons as free text only.
- Migrate the full legacy lead history without checking its consent basis with marketing and the DPO.
