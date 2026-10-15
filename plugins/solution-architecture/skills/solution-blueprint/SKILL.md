---
name: solution-blueprint
description: Shapes the end-to-end solution blueprint for a Dynamics 365 CE programme, covering processes, data, integration, security, environments and ALM, and readies it for Success by Design reviews. Use when design starts after scoping, when a solution blueprint review is due, or when the blueprint has drifted from what is being built.
metadata:
  department: solution-architecture
  stages: Strategize, Initiate, Implement
  modules: All
  status: draft
---

# Solution blueprint

The solution blueprint is the one document that explains how the Dynamics 365 CE solution will deliver the outcomes the programme was funded for. It is what the Success by Design solution blueprint review examines, what the design authority holds the team to, and what a new joiner reads to understand why the system looks the way it does. Without it, each module workstream designs in isolation and the cross-module gaps only appear in system integration testing.

Blueprints usually fail in one of two ways. Some become a feature catalogue that restates product documentation and never says which business process each feature serves. Others are written well at the end of Initiate and then left alone, so by Prepare they describe a solution that no longer exists.

## When to use

- Design is starting after the charter and scope are agreed, and the team needs a structure for design decisions.
- A Success by Design solution blueprint review, or a later topic review, is approaching.
- A new module, phase or major integration is being added and the blueprint has to absorb it.
- The design authority has found that what is being built no longer matches the documented design.

Not this skill: `programme-management:project-charter` for business case and scope, `business-analysis:fit-gap-analysis` for requirement-level fit, `solution-architecture:cross-module-data-model` for the detailed data model, `solution-architecture:environment-strategy` for the environment landscape, and `integration-and-data:integration-architecture` for integration patterns.

## Questions to ask first

1. Which modules are in scope, in which phase and in what order? Phasing decides what the first baseline must settle and what can stay open.
2. Which outcomes and success measures did the charter commit to? Every blueprint chapter should trace back to at least one of them.
3. What is already fixed (licences bought, partner, ERP, Microsoft 365 tenant, telephony)? Fixed constraints are inputs to the design, not choices within it.
4. Who has authority to approve design decisions? Without a named approver or design authority, decisions get reopened every sprint.
5. Will the reviews be run with Microsoft FastTrack or led by the partner? This sets who facilitates each review and how much preparation time it needs.

## Approach

Write the blueprint as an argument, not an inventory. For each chapter, state the business need, the design chosen, the alternatives rejected and the reason. Descriptions of what a product feature does belong in links to Microsoft Learn, not in the document.

### 1. Build the skeleton from the review topics

Organise the blueprint around the areas a Success by Design review will probe, so the review becomes a walk through the document rather than a separate exercise: programme strategy and phasing, application landscape, end-to-end processes, data model, data migration, integration, security, reporting and AI, environments and ALM, testing, cutover and operations. Check the current Dynamics 365 Implementation Guide for the review topics in use.

### 2. Lead with end-to-end processes

Describe the processes that cross modules first: campaign response to qualified lead, lead to order, issue to resolution, service request to completed work order. For each, show which app owns each step, where records hand over between modules, and whether each step is standard, configured or extended. This is where cross-module gaps surface while they are still cheap to close.

### 3. Keep a decision log alongside the narrative

Record each significant decision with its context, options, choice, consequences, owner and date. The design authority reviews the log as well as the prose. Link open questions and assumptions to the `raid-log` so they are actively closed rather than forgotten.

### 4. Time the reviews deliberately

Hold the solution blueprint review once the design has real shape, typically early in Implement and before build commitments become hard to reverse. Plan topic reviews such as data, security, integration and performance as each area matures, and treat the go-live readiness review in Prepare as a test of whether the built solution still matches this document. Log every finding with an owner and a due date.

### 5. Baseline, then change through governance

Baseline the blueprint at the end of design and version it. From then on, changes go through the design authority with a short impact note, so the blueprint remains the single description of the solution through Operate.

## Outputs

- `solution-blueprint`, versioned and baselined at the end of design.
- An architecture decision log covering every significant choice and its rationale.
- An end-to-end process coverage matrix showing module ownership and fit (standard, configured, extended).
- Review findings, assumptions and open questions recorded in the `raid-log`.

## Scale notes

### SMB

One consultant often writes the blueprint while also configuring, so keep it short and focused on the decisions that matter: process coverage, data model, security model, environments and ALM. A single review with the partner and customer leads can replace a formal review board. Do not skip the security and ALM chapters because they look small; they are the ones that are most expensive to fix after go-live.

### Enterprise

Each module workstream contributes a chapter owned by its lead, while the solution architect owns the cross-module chapters and the decision log. The design authority approves the baseline and every later change. Expect several topic reviews with Microsoft or the partner, and reserve time in the delivery plan to respond to their findings.

## Hand-offs

Once the blueprint is baselined, `programme-management:delivery-plan` sequences the build, `solution-architecture:cross-module-data-model` and `solution-architecture:environment-strategy` detail their chapters, and `integration-and-data:integration-architecture` takes the integration chapter forward. Sign-off is needed from `design-authority:design-review`, with `security-compliance:security-model-review` for the security chapter.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Baseline a blueprint that lists features without tracing them to processes and outcomes.
- Treat the solution blueprint review as a one-off event the document never has to answer to again.
- Change a baselined design decision without recording it in the decision log.
- Present the blueprint as complete while the security, data migration or ALM chapters are placeholders.
