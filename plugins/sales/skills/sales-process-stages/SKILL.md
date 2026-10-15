---
name: sales-process-stages
description: Designs the opportunity sales process in Dynamics 365 Sales, covering business process flows, stage gates, required evidence, probability and close outcomes. Use when turning a sales methodology into stages, deciding gate rules, choosing between branches and separate flows, or fixing a pipeline that sellers and managers do not trust.
metadata:
  department: sales
  stages: Initiate, Implement, Operate
  modules: Sales
  status: draft
---

# Sales process stages

The sales process is what sellers see every day, and it shapes every pipeline report and forecast the business will run. In Dynamics 365 Sales it is usually expressed as a business process flow on the opportunity, backed by real fields such as sales stage, probability and forecast category.

Projects go wrong in two opposite ways. Some copy a ten-stage methodology slide straight into the system with mandatory fields at every step, so sellers update the record once a quarter. Others leave the default flow untouched, so stages mean different things to different teams and pipelines cannot be compared.

## When to use

- Translating an agreed sales methodology into stages, steps and exit criteria.
- Deciding which fields are mandatory at which gate, and how gates are enforced.
- Choosing between one flow with branches and several flows for different sales motions.
- Linking stage to probability, forecast category and close outcomes (won, lost, cancelled).
- Diagnosing why sellers skip stages or why pipeline reports disagree.

Not this skill: `sales:lead-to-opportunity` for qualification before the opportunity exists, `sales:forecasting` for rollups and forecast columns, `business-analysis:process-mapping` for mapping the current process before system design.

## Questions to ask first

1. How many genuinely different sales motions exist (new business, renewal, partner-led, tender)? Each motion with different exit criteria may justify a branch or a separate flow.
2. What evidence proves a deal has moved stage, and who checks it? Gates without evidence become a click, and gates nobody reviews get gamed.
3. Is probability set by stage, by the seller or by a model? This decides whether probability is derived from the stage or freely editable, and how forecasts weight the pipeline.
4. What must happen when a deal is won or lost? Won may trigger quotes, orders or ERP integration; lost should capture a reason and competitor for analysis.
5. Do other teams work the opportunity (presales, bid team, commercial approval)? Shared stages need ownership rules and possibly approvals.

## Approach

Begin with the business's own methodology, but compress it. Most B2B sales processes fit into four to six stages that a manager could explain in one sentence each; anything finer is better expressed as steps within a stage. Write exit criteria for every stage as facts the system can hold, then design the flow from those criteria rather than from the slide.

1. Use the business process flow as a guide, not as the database. The flow shows sellers where they are and what comes next; the facts belong in real fields on the opportunity so they can be reported, secured and read by forecasting and Copilot.
2. Gate sparingly. Make a step required only when its absence would make the next stage meaningless, such as an identified decision maker before a proposal. Everything else should be recommended, with a dashboard or view that shows the gaps.
3. Keep stage, probability and forecast category consistent. Decide whether moving stage sets a default probability and forecast category through a simple rule, and whether sellers may override it. Document the mapping in one table and test it.
4. Branch before you clone. Conditional branching inside one flow is easier to maintain than several flows on the same table, and it keeps pipelines comparable. Create a separate flow only when a sales motion has a different audience, different gates and different reporting. Check current Microsoft Learn documentation for the current limits on stages, steps and flows per table.
5. Design the close. Use the standard close opportunity experience with agreed status reasons for won, lost and cancelled, a competitor field where it matters, and a rule for what happens to open quotes and activities.
6. Make the flow role-aware. Use security roles to control which flows a team sees, and avoid hiding stages with form scripts, which is how unsupportable forms are born.

Pilot the stages with a handful of live opportunities before build is frozen. Watching sellers move real deals through the flow exposes ambiguous criteria faster than any workshop.

## Outputs

- Stage model with exit criteria, gate fields and owners, recorded in the `solution-blueprint`.
- Stage to probability and forecast category mapping table.
- Business process flow specification per sales motion, including branching rules.
- Close outcome design: status reasons, competitor capture and follow-on actions.
- Stage progression scenarios in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

One flow on the opportunity is nearly always enough, built by the consultant with the sales manager in the room. Start from the standard opportunity sales process and rename stages rather than building from scratch. Do not skip the written exit criteria; even a team of five needs to agree what each stage means before go-live.

### Enterprise

Expect a global core process with regional or business-unit variants, owned by sales operations. Variants should be branches or separate flows approved through `design-authority:design-review`, and changes to gates should be assessed through `design-authority:change-impact-assessment` because they shift forecast history. Coordinate with the data workstream so migrated opportunities land in a valid stage with consistent probability.

## Hand-offs

`sales:forecasting` builds on the stage and forecast category design, `sales:quotes-and-orders` picks up from the proposal stage onwards, and `data-and-ai:power-bi-on-dataverse` builds pipeline reporting. Custom code in or around the flow, such as plug-ins that enforce gates, goes through `design-authority:customisation-challenge`. Mapping migrated opportunities to stages belongs to `integration-and-data:data-mapping-and-cleansing`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Make every field in every stage mandatory.
- Hide or skip stages with form scripts instead of using branching or security roles.
- Change stage definitions mid-quarter without telling the forecasting and reporting owners.
- Create a separate business process flow for each team when a branch would do.
