---
name: user-stories
description: Writes and refines user stories for a Dynamics 365 CE backlog, derived from future-state process steps, written for real business roles, sized for a sprint and traced to processes, fit-gap decisions and tests. Use when building or grooming the backlog, splitting epics, or turning workshop notes into stories a configurator can deliver.
license: CC-BY-4.0
metadata:
  department: business-analysis
  stages: Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# User stories

On a CRM programme the backlog is the specification, so backlog quality sets the ceiling on build quality. A good story tells the build team who needs what and why, in words the business recognises, and it traces back to a process step and forward to a test.

Stories go wrong when they describe screens instead of needs ("add a field to the account form"), when the partner writes them without a business voice, when the role is simply "user", and when epics are so large they span several sprints. The quieter failure is non-functional work (security, data, integration, offline behaviour) that never becomes a story, so it is never estimated or tested.

## When to use

- After fit-to-standard, to turn decisions and future-state maps into a backlog.
- In backlog refinement, to split, rewrite or prioritise stories.
- When workshop notes, emails or legacy specifications need converting into deliverable work.
- When planning the minimum viable release for go-live.

Not this skill: `business-analysis:acceptance-criteria` for writing the Given/When/Then criteria on a story, `business-analysis:fit-gap-analysis` for deciding how a gap is resolved, `solution-architecture:extend-or-configure` for the architectural choice behind a story.

## Questions to ask first

1. Which future-state process step does the story serve? A story without a process step cannot be traced to a test or a training module.
2. Which business role needs it? Roles become security roles, so the role determines what the story must allow and prevent.
3. Has the underlying requirement been through fit-to-standard? If not, the story may specify a custom build for something the product already does.
4. Who is the product owner, and can they prioritise and accept without referring upwards? Stories stall without a decision-maker.
5. Where does the backlog live? The tool decides how traceability links are held.

## Approach

Use the familiar form: as a role, I want a capability, so that an outcome. The role is a real business role that will map to a security role, never "user" or "admin". The outcome should connect to a charter measure where possible. For example: as a service agent, I want to see the customer's active entitlements on the case form, so that I can apply the right service level without checking another system.

Organise the backlog as epics (a level 2 process or major capability), features (a level 3 process or module capability), stories (one deliverable change) and tasks.

1. Derive stories by walking each future-state step and asking what the role needs the system to do at that point. Tag each story with the step identifier.
2. Record the fit-gap classification on each story (standard, configure, low-code, pro-code or ISV). It drives estimation and decides which stories need design authority review.
3. Keep stories small, independent, valuable and testable. Split by process path (happy path first, exceptions next), by role, by record type, by channel or by data variation. Avoid splitting by technical layer (form, then view, then plug-in), which produces stories nobody can test on their own.
4. Write explicit non-functional stories: security role access, field-level security, auditing, retention, performance, integration behaviour, reporting, and offline behaviour for Field Service Mobile.
5. Agree a definition of ready: role, outcome, step identifier, fit-gap classification, acceptance criteria, data needs and dependencies known.
6. Agree a definition of done: built inside a solution in development, unit tested, deployed to test through the pipeline, acceptance criteria passed, and documentation and training notes updated.
7. Prioritise against charter outcomes, using MoSCoW or a similar method, and mark the minimum viable scope for go-live.
8. Refine weekly with the product owner and key users so that stories are ready two sprints ahead.

## Outputs

- A product backlog of epics, features and stories with step identifiers and fit-gap classification.
- Definitions of ready and done.
- A traceability matrix from process step to story to test, feeding the `test-strategy-and-uat-scripts`.
- The minimum viable release scope for go-live.

## Scale notes

### SMB

The consultant writes stories with the business owner, and the backlog may be a simple list. Many stories are pure configuration and can be grouped by process. Role, outcome and acceptance criteria are still required, because UAT and training are built from them.

### Enterprise

Each workstream keeps a backlog in a shared tool, with a product owner per module. Stories touching shared tables such as account and contact need cross-workstream agreement through the design authority. Non-functional stories are owned by architecture, and traceability is maintained to audit standard.

## Hand-offs

- `business-analysis:acceptance-criteria` completes each story before it is ready.
- `solution-architecture:extend-or-configure` and `platform-engineering:plugin-design` take stories that need extension.
- `testing-quality:system-integration-testing` plans tests from the trace.
- `change-adoption:role-based-training` builds curricula from stories grouped by role.
- Reviewer sign-off: stories classified as pro-code or ISV go to `design-authority:customisation-challenge` before they enter a sprint.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Write stories as instructions to add fields or screens with no role or outcome.
- Use a generic user or system administrator as the story role.
- Accept a story into a sprint without acceptance criteria and a process step reference.
- Leave security, data and integration needs in comments instead of stories.
