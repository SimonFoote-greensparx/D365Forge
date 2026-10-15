---
name: extend-or-configure
description: Makes the architectural build decision for a specific gap or proposed extension, climbing a ladder from standard behaviour and configuration through low-code and Dataverse code to ISV products and Azure services, judged on cost of ownership. Use when someone proposes custom code, a PCF control, an AppSource product or an Azure component.
license: CC-BY-4.0
metadata:
  department: solution-architecture
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Extend or configure

Every extension is a liability the organisation carries for the life of the system. It must be tested against each Microsoft update, understood by the support team and kept compatible with features Microsoft adds later. The question is never whether something can be built, because almost anything can, but which is the lowest rung of the ladder that meets the need acceptably.

Projects go wrong when the build approach follows the skills of whoever picks up the story. A developer writes a plug-in for what a business rule would do, a maker builds a flow for logic that must run inside the transaction, or an ISV product is bought for one feature. Each choice is defensible alone; together they produce an estate nobody can upgrade with confidence.

## When to use

- A gap from the fit-gap register needs an architectural build decision.
- Someone proposes a plug-in, PCF control, custom page, ISV product or Azure component.
- The design authority asks why a requirement was not met with standard features.
- A post-go-live enhancement request needs a consistent sizing of build approach and run cost.

Not this skill: `business-analysis:fit-gap-analysis` to classify and record the gap register, `business-analysis:fit-to-standard` to challenge the process first, `design-authority:customisation-challenge` for the independent challenge, and `platform-engineering:plugin-design`, `platform-engineering:pcf-controls` or `platform-engineering:power-automate-patterns` for the build itself.

## Questions to ask first

1. What business outcome does the requirement serve, and what is lost if standard behaviour is used instead? This tests whether the gap is real or a preference.
2. Must the logic run inside the save, or can it run afterwards? This alone rules whole rungs in or out.
3. How often does it run, and at what volume? High-volume logic is a poor fit for some low-code tools.
4. Who will maintain it after go-live, and with which skills? A solution the run team cannot support is not a solution.
5. Does it depend on premium connectors, ISV subscriptions or Azure consumption? These add running costs; confirm with the Microsoft licensing guide or your partner.

## Approach

Climb the ladder one rung at a time and record why each lower rung was not enough. From lowest to highest cost of ownership:

1. Adopt the standard. Change the process to fit the product where the difference adds no business value. This is the cheapest option and the one most often skipped.
2. Configure. Columns, forms, views, business rules, business process flows, SLAs, routing rules, schedule board settings and app settings. Configuration moves with the product and needs no code skills to maintain.
3. Low-code. Power Fx formula columns, cloud flows, custom pages and similar tools. A good fit for logic that can run asynchronously or is owned by makers, within the limits set out in `platform-engineering:power-automate-patterns`.
4. Pro-code inside Dataverse. Plug-ins, custom APIs, client scripts and PCF controls. Right for synchronous, transactional or high-volume logic and for interface needs configuration cannot meet, but it needs developer skills in the run team.
5. ISV or AppSource product. Sensible for a substantial, well-bounded capability such as document generation, address validation or mapping that a vendor maintains. Check the vendor's record of keeping pace with Microsoft updates, its support model and how you would exit.
6. External services. Azure Functions, Logic Apps or Service Bus for heavy processing, long-running work or integration patterns that do not belong in Dataverse.

Score each candidate against the same criteria: fit to the requirement, run cost, upgrade exposure, test burden, skills needed to maintain it, and licensing. Prefer the lowest rung that scores acceptably, even when a higher rung would be more elegant.

Unsupported techniques sit off the ladder altogether. Manipulating the page DOM, calling undocumented endpoints or changing data outside the platform's APIs can break without warning on any update, and no business case justifies them.

Record each decision in the blueprint's decision log with the rung chosen, the rungs rejected and why. Gap types repeat, so once the design authority agrees an answer for one type, reuse it as a pattern rather than arguing it again.

## Outputs

- A build decision for each gap or proposal, recorded in the decision log of the `solution-blueprint`.
- A customisation register listing every extension, its rung, owner and upgrade risk.
- Assessment notes for any ISV product proposed.
- Entries in the `raid-log` where a decision carries upgrade or support risk.

## Scale notes

### SMB

Stay on the bottom three rungs wherever possible, because the support team is small and may not include a developer. When code is unavoidable, make sure the partner hands over source, documentation and a support arrangement. Do not skip recording the decision; it is the only defence when the next consultant asks why something was built.

### Enterprise

Standardise answers to recurring gap types in a pattern catalogue owned by the design authority. Workstreams propose, the solution architect applies the ladder, and anything at rung four or above goes to independent challenge. Track the size and risk of the customisation register as a programme measure.

## Hand-offs

`platform-engineering:plugin-design`, `platform-engineering:pcf-controls` or `platform-engineering:power-automate-patterns` build the chosen approach, and `integration-and-data:integration-architecture` picks up rung six when the need is an integration. `design-authority:customisation-challenge` must clear anything at rung four or above before build starts.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use unsupported customisation techniques such as DOM manipulation or undocumented endpoints.
- Write custom code for a requirement that standard configuration meets acceptably.
- Choose a build approach the run team cannot maintain.
- Recommend an ISV product without checking its update record, support model and exit path.
- Climb a rung without recording why the lower rungs were rejected.
