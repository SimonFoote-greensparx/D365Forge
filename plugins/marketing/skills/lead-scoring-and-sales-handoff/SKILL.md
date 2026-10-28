---
name: lead-scoring-and-sales-handoff
description: Designs lead scoring in Customer Insights - Journeys and the hand-off of sales-ready leads to Dynamics 365 Sales with journey context, covering fit and interest signals, thresholds, assignment, follow-up expectations and feedback. Use when defining marketing qualified leads, building a scoring model, or fixing leads that sellers ignore.
license: CC-BY-4.0
metadata:
  department: marketing
  stages: Initiate, Implement, Operate
  modules: Marketing, Sales
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Lead scoring and sales hand-off

Lead scoring is the agreement between marketing and sales about which people are worth a seller's time, expressed as rules the system can apply. The hand-off is where that agreement is tested: the lead must reach the right seller quickly, with enough context about what the person did to make the first conversation relevant.

Projects go wrong when marketing builds a scoring model alone and sales never trusts it, when thresholds are set without looking at real outcomes, or when leads land in Dynamics 365 Sales with no explanation of why they are there. Without a feedback loop the model never improves.

## When to use

- Defining marketing qualified and sales-ready criteria jointly with sales.
- Building lead scoring models in Customer Insights - Journeys.
- Designing how scored leads are created, assigned and presented to sellers.
- Passing journey context (forms, events, emails, score) to sales.
- Reviewing scoring against outcomes and adjusting it.

Not this skill: `sales:lead-to-opportunity` for qualification and conversion once sales has the lead, `sales:sequences-and-sales-accelerator` for seller follow-up cadences, `marketing:journey-design` for the nurture journeys that build the score.

## Questions to ask first

1. What does sales consider a good lead, and which past leads actually converted? Thresholds should come from evidence, not guesses.
2. Which signals are available: profile fit, form submissions, event attendance, email and web engagement? Scoring can only use data that is captured and that the organisation may lawfully use for this purpose, which is a question for the DPO.
3. Who receives sales-ready leads, and how quickly must they follow up? Assignment and follow-up time define the hand-off service.
4. Is predictive lead scoring in Dynamics 365 Sales in use or planned? Two scores on one lead confuse sellers unless their roles are clear.
5. What will sales tell marketing about lead outcomes? The feedback loop is what keeps the model honest.

## Approach

Make lead scoring a joint marketing and sales design, signed off by both leaders. Start with a short workshop using recent real leads and their outcomes, and agree definitions before anyone opens the scoring designer.

1. Separate fit from interest. Fit comes from profile data such as role, industry, organisation size and region; interest comes from behaviour such as form submissions, event attendance, email clicks and visits to key pages. A lead needs both to be sales-ready; strong interest from a poor fit belongs in nurture, not with a seller.
2. Build a simple model first. A handful of weighted conditions with decay for old activity is easier to explain and adjust than an elaborate one. Set the sales-ready threshold from past conversion where data exists, or start conservatively and adjust after the first month of outcomes.
3. Define the hand-off event. When a lead crosses the threshold, decide whether to create or update the lead, change its status, notify the owner, add it to a sales sequence or raise a task. One clear action beats several.
4. Carry journey context. Sellers need to see why the lead is here: the score and its main contributors, recent form submissions, event registrations and attendance, journey interactions, consent state and source campaign. Put this on the lead form in the Sales app, not in a marketing screen sellers will never open.
5. Assign and set expectations. Route leads by territory, product or declared skills, agree a follow-up time with sales leadership, and monitor it at team level.
6. Close the loop. Use lead status and disqualify reasons from sales to review the model monthly at first, then quarterly, and change weights and thresholds through a small, recorded change process.
7. Align with predictive scoring. If predictive lead scoring in Dynamics 365 Sales is used, decide which score drives the hand-off and which is advisory, and explain it to sellers. Predictive features depend on licence and data volume; confirm with the Microsoft licensing guide or your partner.

Check current Microsoft Learn documentation for the scoring capabilities available in your release of Customer Insights - Journeys.

## Outputs

- Joint lead definition: fit criteria, interest signals and sales-ready threshold, signed by marketing and sales leads.
- Scoring model specification with weights, decay and review cadence.
- Hand-off design: lead creation, assignment, notification and follow-up time.
- Seller lead view showing journey context and score contributors.
- Hand-off scenarios in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

Often one marketer and one sales manager agree the model in a single session, and the consultant configures a simple score with a few conditions. Hand off by assigning the lead to its owner and raising a task. Do not skip the monthly outcome review with sales; small teams can adjust quickly and should.

### Enterprise

Expect several scoring models by business unit, product or region, a marketing operations owner, and a follow-up service level agreed at leadership level. Lead routing must work with sales territories and sales accelerator assignment, and hand-off performance is reported at team level. Scoring changes that shift lead volumes go through `design-authority:change-impact-assessment`, and use of behavioural tracking data goes through `security-compliance:marketing-consent-compliance`.

## Hand-offs

`sales:lead-to-opportunity` takes the lead through qualification, and `sales:sequences-and-sales-accelerator` runs follow-up cadences. `data-and-ai:reporting-strategy` defines funnel reporting across marketing and sales. Use of engagement data in scoring needs `security-compliance:marketing-consent-compliance` sign-off.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Set the sales-ready threshold without input from sales.
- Send leads to sellers without the context that explains the score.
- Score on data collected without a consent or lawful basis for that use.
- Use lead follow-up data to rank or appraise individual sellers.
