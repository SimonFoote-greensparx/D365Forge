---
name: fit-gap-analysis
description: Classifies Dynamics 365 CE requirements as fit or gap and resolves each gap through a fixed hierarchy of adopt standard, configure, low-code, pro-code and third-party ISV, recording rationale, effort, risk and traceability to tests. Use when consolidating workshop outputs, estimating scope, or deciding how a particular gap should be closed.
license: CC-BY-4.0
metadata:
  department: business-analysis
  stages: Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Fit-gap analysis

The fit-gap register is where scope and long-term cost of ownership are actually decided. Every gap closed with custom code adds build effort now and, more importantly, regression testing on every release wave, upgrade risk, and a support burden for as long as the system runs. A register that records the decision and the reasoning lets the organisation see that cost before committing to it.

Fit-gap goes wrong when gaps are resolved by whoever writes the first solution, when configuration is treated as free, when an ISV is chosen from a demo without due diligence, and when the link from requirement to test is lost so nobody can prove the gap was closed.

## When to use

- After fit-to-standard workshops, to consolidate and classify their outputs.
- When estimating scope for a statement of work or a phase plan.
- When deciding how to close a specific gap, or revisiting a decision after a release wave.
- When building or auditing traceability from requirements to tests.

Not this skill: `business-analysis:fit-to-standard` for running the workshops, `solution-architecture:extend-or-configure` for the architectural design of a specific extension, `design-authority:customisation-challenge` for the formal challenge of a proposed customisation.

## Questions to ask first

1. What is the business reason for the gap, and what is it worth? A gap with no measurable value should be closed by adopting standard.
2. Could the process change instead of the system? This is the cheapest resolution and the one most often skipped.
3. How much custom code can the organisation support after go-live? An organisation with no in-house developers is buying a long partner dependency with every plug-in.
4. Does an upcoming release wave or an existing capability already close the gap? Check current Microsoft Learn documentation and the published release plans.
5. Who decides: the product owner, the design authority, or both? Decision rights should depend on the resolution level.

## Approach

Resolve every gap through the hierarchy in order, and record why each higher level was rejected before accepting a lower one.

1. Adopt standard. Change the process to fit the product. Cheapest to run, and the default unless the business reason is strong.
2. Configure. Forms, views, columns, business rules, business process flows, security roles, service levels and routing. Low risk, but not free: each item still needs testing, documentation and training.
3. Low-code. Power Automate cloud flows, Power Fx, custom pages and Copilot Studio agents. Needs ownership, ALM discipline and governance of connectors and run-as identities.
4. Pro-code. Plug-ins, PCF controls, custom APIs and Azure services. Needs development skills, pipelines and regression testing at every release wave.
5. Third-party ISV. An AppSource or partner solution. Adds a vendor dependency, so assess vendor viability, support terms, release wave compatibility, what data it stores and where (a question for the DPO), its security footprint, and its licence cost (confirm with the Microsoft licensing guide or your partner). Where a gap would otherwise mean rebuilding a commodity capability in pro-code, compare the two side by side.

For each gap record: identifier, process step, requirement, business reason, priority, resolution level, why higher levels were rejected, effort range, risk, owner, design authority decision, and linked stories and tests.

Work through the register in this sequence:

- Consolidate workshop outputs, remove duplicates and link each item to its process step identifier.
- Re-test every gap against standard behaviour with a consultant; many gaps turn out to be knowledge gaps.
- Apply the hierarchy and estimate each resolution as a range.
- Describe whole-life cost in words for every resolution from low-code onwards: build, test, release wave regression, support and licensing.
- Send low-code, pro-code and ISV resolutions to the design authority before they enter the backlog.
- Maintain a traceability matrix from requirement to gap decision, story, test case and UAT result, so that every requirement can be shown as delivered, deferred or withdrawn.

## Outputs

- A fit-gap register with resolution level and rationale for every gap.
- A requirements traceability matrix through to test cases, feeding the `test-strategy-and-uat-scripts`.
- A scope and effort summary for the `delivery-plan` and the statement of work.
- ISV assessment notes and inputs to the `solution-blueprint`.

## Scale notes

### SMB

Aim to close almost everything through adopt and configure, use low-code sparingly, and treat pro-code as an exception that needs a strong reason. A focused ISV can be pragmatic for one capability. One register, classified by the consultant and decided by the owner, is enough, but record the rationale even for small decisions.

### Enterprise

The design authority sets approval thresholds by resolution level and looks for reuse across workstreams, so one gap is not solved three ways. Global and local variants are tracked separately. ISVs go through procurement and security review, with data protection questions taken to the organisation's DPO, and traceability is held to audit standard.

## Hand-offs

- `business-analysis:user-stories` turns resolutions into backlog items.
- `solution-architecture:extend-or-configure`, `platform-engineering:power-automate-patterns` and `platform-engineering:plugin-design` design the extensions.
- `testing-quality:test-strategy` uses the traceability matrix.
- `programme-management:statement-of-work` takes the register as the scope basis.
- Reviewer sign-off: `design-authority:customisation-challenge` for low-code, pro-code and ISV resolutions; `security-compliance:security-model-review` for any ISV that reads or stores customer data.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Choose pro-code or an ISV without recording why standard, configuration and low-code were rejected.
- Treat configuration as free of testing, documentation and training effort.
- Install an ISV solution without checking its release wave support and how it handles customer data.
- Lose the trace from requirement to test.
