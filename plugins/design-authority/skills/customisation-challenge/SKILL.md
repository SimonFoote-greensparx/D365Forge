---
name: customisation-challenge
description: Challenges proposed customisations of Dynamics 365 CE by walking them down the gap resolution hierarchy (adopt standard, configure, low-code, pro-code, ISV) and testing supportability over time. Use when a team proposes custom code, a new custom table, a PCF control, an ISV product or any departure from standard behaviour.
license: CC-BY-4.0
metadata:
  department: design-authority
  stages: Initiate, Implement
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Customisation challenge

Every customisation is a long-term cost. It has to be tested against each release wave, documented, supported, and eventually retired or rebuilt when Microsoft ships something better. Projects over-customise because each request seems reasonable on its own, because users want the old system's behaviour back, or because developers would rather build than configure. A few years later the organisation owns a bespoke CRM sitting on a platform it pays to keep standard.

This reviewer-class skill is the formal challenge. Before a gap is filled with anything beyond configuration, someone outside the build team asks whether it needs filling at all and, if so, at the lowest rung of the hierarchy that works. It is read-only: it reviews the proposal and reports findings, and the proposing department owns the decision record and the build.

## When to use

- A team proposes a plug-in, custom API, PCF control or client script.
- A new custom table duplicates something a standard table could hold.
- An ISV product is proposed to fill a gap.
- Users ask for the legacy system's behaviour to be recreated.
- A low-code solution is growing into something that needs pro-code support.

Not this skill: `business-analysis:fit-gap-analysis` for identifying the gaps, `solution-architecture:extend-or-configure` for the architect's own design choice, `design-authority:design-review` for reviewing a whole design, and `design-authority:standards-conformance` for checking a built component.

## Questions to ask first

1. What business outcome does the gap serve, and what happens if it is not filled? Many gaps turn out to be preferences rather than requirements.
2. Has the standard process been shown to the business, and why was it rejected? Familiarity with the old system is not a reason to customise.
3. Who will support the component after go-live, and with what declared skills? Pro-code without a maintainer becomes an orphan.
4. Does the proposal depend on a preview feature or a roadmap item? Check current Microsoft Learn documentation; preview features are not a production foundation.

## Approach

Walk each proposal down the hierarchy and stop at the first rung that meets the need.

1. Adopt standard. Can the business change its process to fit standard behaviour? This is the cheapest option and is often dismissed too quickly. Ask the process owner, not only the requester.
2. Configure. Can standard configuration (columns, forms, views, business rules, business process flows, security roles, SLAs, routing rules) meet the need? Configuration survives upgrades and can be maintained by administrators.
3. Low-code. Can Power Automate, Power Fx or a Copilot Studio agent meet it? Low-code is cheaper to change but still needs ALM, ownership and error handling; it is not free.
4. Pro-code. Plug-ins, custom APIs, PCF controls and client scripts are justified when transactional integrity, performance or user experience demand them. Require unit tests, source control and a named maintainer.
5. ISV. A third-party product may beat building, but challenge vendor viability, the vendor's record of keeping pace with release waves, data residency, the exit route and licensing (ask the vendor for its terms, and for Microsoft licences confirm with the Microsoft licensing guide or your partner).

For every proposal, test supportability over time. How will it behave through the next few release waves? Does it rely on unsupported techniques such as direct manipulation of the page structure or undocumented APIs? Who maintains it, and what would removing it later cost? Does it overlap with something on Microsoft's published release plans?

Record each finding with its classification.

- Blocking: the proposal uses unsupported techniques, has no maintainer, skips a lower rung that clearly meets the need, or creates risk the blueprint does not allow. It cannot proceed until resolved.
- Advisory: a lower rung might work, or supportability could be improved; the department records its decision and may proceed.

Blocking findings are not overruled by the department under review. Where it disagrees, the matter escalates to the steering committee or executive sponsor, who may accept the customisation and its long-term cost explicitly.

## Outputs

- Challenge record per proposal, stating the rung chosen and the rationale.
- Findings classified as blocking or advisory.
- Customisation register (what was built, why, owner, next review date) kept alongside the `solution-blueprint`.
- Accepted technical debt recorded in the `raid-log`.

## Scale notes

### SMB

The lead consultant plays this role and is often challenging their own team's proposals, so a second-pair-of-eyes review from someone outside the delivery is worth arranging for anything pro-code or ISV. SMB organisations rarely have developers to maintain custom code, so the bar for pro-code should be higher, not lower.

### Enterprise

The design authority board runs the challenge with a defined submission template, and the customisation register is reviewed at every release wave. Expect pressure from workstreams with tight deadlines; the hierarchy protects the long-term estate and must be applied consistently across modules.

## Hand-offs

- Proposals that pass go to `solution-architecture:extend-or-configure` for design, then to `platform-engineering:plugin-design`, `platform-engineering:pcf-controls`, `platform-engineering:power-automate-patterns` or `platform-engineering:copilot-studio-agents` to build.
- Built components are checked by `design-authority:standards-conformance`.
- Escalations reach the steering committee through `programme-management:governance-cadence`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Approve pro-code where configuration or a process change meets the need.
- Accept customisations that rely on unsupported techniques or undocumented APIs.
- Approve an ISV product without assessing vendor viability, licensing and exit route.
- Let the proposing department overrule a blocking finding.
