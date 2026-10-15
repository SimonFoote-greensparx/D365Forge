---
name: sequences-and-sales-accelerator
description: Designs seller cadences with sales accelerator sequences, the work list, segments and assignment rules in Dynamics 365 Sales. Use when building outreach sequences for new leads or renewals, configuring the work list, automating lead and opportunity assignment, or deciding what belongs in a sequence rather than a marketing journey.
license: CC-BY-4.0
metadata:
  department: sales
  stages: Implement, Operate
  modules: Sales
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Sequences and sales accelerator

Sales accelerator turns a pipeline into a prioritised to-do list. Sequences define the steps a seller should take, segments group records that share a cadence, assignment rules distribute the work, and the work list shows each seller what to do next. Used well, it gives inside sales and business development teams a consistent rhythm without custom code.

Projects go wrong by treating sequences as a bulk email tool that duplicates marketing journeys, or by writing sequences so long and rigid that sellers mark steps complete without doing them. Assignment rules built on vague criteria cause the opposite problem: work lands with the wrong person and sits there.

## When to use

- Designing outreach cadences for new leads, inbound enquiries, renewals or dormant accounts.
- Configuring the work list, its filters and sort order.
- Setting up segments and assignment rules to route leads or opportunities to sellers and teams.
- Deciding whether a touchpoint belongs in a sales sequence or a marketing journey.

Not this skill: `marketing:journey-design` for automated one-to-many journeys, `marketing:segments-and-audiences` for marketing segments, `sales:copilot-in-sales` for AI assistance on records and in Outlook and Teams.

## Questions to ask first

1. Which seller teams work high volumes of similar records? Sequences pay off for inside sales, business development and renewals, far less for complex field sales.
2. What cadence works today, with which channels and timings? A sequence should encode a cadence that already works, not invent one.
3. How should work be distributed: territory, product, declared skills, capacity or round robin? Assignment rules need criteria that are held as data and kept current.
4. Which licences do the sellers hold? Sales accelerator capabilities vary by licence, so confirm with the Microsoft licensing guide or your partner.
5. Does marketing already contact these people, and on what consent basis? Seller emails in a sequence still have to respect opt-outs and the consent model, so check the position with the DPO.

## Approach

Design sequences from the seller's week, not from a marketing calendar. A good sequence has a clear entry condition, a small number of steps across email, call and task, realistic waits, and an exit when the customer responds or the record changes status.

1. Start with two or three sequences. Typical first candidates are inbound lead follow-up, post-event follow-up and renewal preparation. Prove that sellers complete steps before building more.
2. Write steps sellers will genuinely do. Use email templates that sellers personalise, call steps with short talking points, and waits that reflect real response times. Use conditional steps only where the branch changes what the seller does next.
3. Define entry and exit. Connect records to sequences through segments or manually, and make sure a record leaves the sequence when it is qualified, disqualified, replies or opts out. Overlapping sequences on one record confuse sellers and customers alike.
4. Build segments and assignment rules on data you maintain. Sales accelerator segments group records by criteria such as source, region or product interest, and assignment rules route them to sellers or teams. Base rules on territory, product, declared skills and capacity held in Dataverse, never on personal characteristics, and define a fallback owner for records no rule matches.
5. Configure the work list. Agree default filters and sort order with the sales manager so sellers open the app and see today's priorities. Add other record types only when sellers act on them.
6. Draw the line with marketing. One-to-many nurture belongs in a Customer Insights - Journeys journey; one-to-one seller outreach belongs in a sequence. A common pattern is a journey that creates or updates a lead, which then enters a sequence.
7. Measure at sequence level: steps completed and skipped, and how many records progressed. Review steps each quarter and retire what does not work.

Check current Microsoft Learn documentation for the current names and capabilities of the work list, sequence step types and assignment options, because this area has changed often.

## Outputs

- Sequence catalogue: purpose, entry and exit criteria, steps, templates and owner for each sequence.
- Segment and assignment rule design, including the fallback owner.
- Work list configuration and default views.
- Agreement with marketing on one-to-one and one-to-many contact boundaries and frequency.
- Seller guides for sequences and the work list in the `training-and-communications-plan`.

## Scale notes

### SMB

With a handful of sellers, start with one or two sequences and manual connection rather than automated segments, and assign by simple territory or round robin. A consultant can configure this in days. Do not skip exit conditions; small teams notice immediately when a customer who already replied gets another automated reminder.

### Enterprise

Expect sequences per team and region, a sales operations owner for the sequence catalogue and assignment rules, and a change process for new sequences. Agree contact frequency rules with marketing so customers are not reached by journeys and sequences in the same week, and route that agreement through `security-compliance:marketing-consent-compliance` where marketing consent is involved. Track licence assignment so only licensed sellers are placed in assignment rules; confirm with the Microsoft licensing guide or your partner.

## Hand-offs

`marketing:lead-scoring-and-sales-handoff` defines which leads arrive ready for a sequence, and `marketing:journey-design` owns automated nurture. `sales:copilot-in-sales` covers AI-drafted emails and summaries that sellers use within steps. `change-adoption:role-based-training` prepares sellers, and `security-compliance:marketing-consent-compliance` reviews sequence emails that could reach people who have opted out of marketing.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use sequences to send bulk marketing email to large lists.
- Base assignment rules on personal characteristics or rankings of individual sellers.
- Leave records in a sequence after the customer has replied, been qualified or opted out.
- Place sellers in sequences or assignment rules before confirming they are licensed for sales accelerator.
