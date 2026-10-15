---
name: process-mapping
description: Maps current and future state business processes for Dynamics 365 CE as BPMN-lite swimlanes at a consistent level of detail, annotated with roles, Dataverse records and systems to drive fit-to-standard, stories and tests. Use when capturing how sales, service, field or marketing work happens today, or designing how it will run in Dynamics 365.
metadata:
  department: business-analysis
  stages: Strategize, Initiate, Implement
  modules: All
  status: draft
---

# Process mapping

Process maps are the spine of a CRM programme. User stories, fit-gap decisions, test scenarios, security roles and training curricula all hang off them, so a weak set of maps weakens everything downstream. A good map shows who does what, in which order, using which record, and where the decisions and handoffs are.

Projects usually go wrong in one of three ways. Teams spend weeks perfecting current-state maps of processes that are about to be replaced. Future-state maps turn out to be the old process with "Dynamics 365" written in the boxes. Or the maps mix levels of detail, so a single diagram jumps from strategy to button clicks and nobody can use it.

## When to use

- At Strategize or early Initiate, to build the process catalogue and agree scope.
- Before fit-to-standard workshops, to give each workshop a process to walk through.
- When designing the future state after fit-to-standard decisions are made.
- When a process changes after sign-off and downstream stories, tests and training need updating.

Not this skill: `business-analysis:fit-to-standard` for running the workshops that compare processes with standard Dynamics 365, `sales:sales-process-stages` for configuring sales stages and business process flows, `customer-service:case-lifecycle-design` for designing case states and transitions.

## Questions to ask first

1. Which end-to-end processes deliver the outcomes in the charter? This keeps mapping effort on what matters.
2. How much will each process change? Processes being redesigned need only a light current state; stable ones need more detail.
3. Who does the work, and who can describe the exceptions? Process owners describe the intended process; the people doing it describe the real one.
4. Which other systems touch the process, such as ERP, telephony, email, portals or document management? Each touchpoint is a potential integration.
5. What will the maps feed: workshops, stories, tests or training? That decides the lowest level of detail you need.

## Approach

Use a level hierarchy and keep each diagram at one level. Level 1 is a value chain such as lead to cash, issue to resolution, request to completed work order, or campaign to qualified lead. Level 2 breaks each chain into end-to-end processes. Level 3 is the swimlane map of a single process. Level 4, task detail, is drawn only where a story or work instruction needs it.

Keep the notation BPMN-lite: start and end events, tasks, exclusive decisions, swimlanes by role (never by person), message flows to other systems, and the key records each step creates or updates. Business users must be able to read the maps without training in notation.

1. Build the process catalogue at levels 1 and 2 from the charter outcomes, and agree an owner for each level 2 process.
2. Capture current state lightly: one session per level 2 process, recording pain points, volumes, exceptions, handoffs and any baseline measures. Stop once the pain points are clear.
3. Draw the future state against standard Dynamics 365 behaviour. Use the standard records (lead, opportunity, quote, order; case, queue, entitlement; work order, booking; journey, segment) and standard stage names wherever they fit, and mark where a business process flow will guide the user.
4. Annotate each future-state step with the role (which later becomes a security role), the Dataverse table, any other system, automation candidates, the decision rule, and the pain point it resolves.
5. Give every step an identifier (for example SVC-02.07) so stories, gaps and tests can trace back to it.
6. Walk each map through with the people who do the work, not only the owner.
7. Version the maps and route changes after sign-off through change control, because each change ripples into stories, tests and training.

Use whatever drawing tool the organisation can maintain after the partner leaves, and store maps with the project documentation rather than in personal files.

## Outputs

- A process catalogue at levels 1 and 2 with named owners.
- Current-state notes or maps with pain points and baselines.
- Future-state swimlane maps annotated with roles, Dataverse tables, systems and step identifiers.
- Inputs to the `solution-blueprint` and to role design for the security model.

## Scale notes

### SMB

The consultant maps with the owner or the lead user, usually covering levels 1 to 3 for a handful of processes. Current state can be a pain-point list rather than diagrams. A future-state map for every in-scope process is still required, because training and testing depend on it.

### Enterprise

Process owners are appointed per value chain, and a process architecture standard fixes notation, levels and naming. A global template is mapped first, with local variants justified per business unit or country. Maps live in a shared repository under version control, and future-state maps are reviewed by the design authority before build.

## Hand-offs

- `business-analysis:fit-to-standard` uses the maps as workshop scripts.
- `business-analysis:user-stories` derives stories from future-state steps.
- `solution-architecture:solution-blueprint` takes the future state into the overall design.
- `change-adoption:stakeholder-analysis` assesses impact by role from the swimlanes.
- `testing-quality:test-strategy` builds end-to-end scenarios from the maps.
- Enterprise future-state maps go to `design-authority:design-review` before build.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Spend weeks perfecting current-state maps of processes that will be replaced.
- Draw the future state by adding Dynamics 365 labels to the old process.
- Name individuals in swimlanes; use roles.
- Design custom automation into the future state before checking standard behaviour.
