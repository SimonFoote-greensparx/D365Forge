---
name: delivery-plan
description: Builds the phased delivery plan for a Dynamics 365 CE programme, aligned to the Success by Design stages and the two Microsoft release waves a year, with sprints, milestones, exit criteria, test cycles and cutover windows. Use when planning phases and dates, sequencing modules, or checking whether a partner plan is realistic.
license: CC-BY-4.0
metadata:
  department: programme-management
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Delivery plan

Most CRM delivery plans are built backwards from a go-live date that was chosen before anyone understood the scope. The work that gets squeezed is always the work nobody sees in a demo: data migration rehearsals, integration testing, UAT, training and cutover preparation. Those are exactly the activities that decide whether go-live succeeds.

The other common failure is ignoring the platform's own rhythm. Dynamics 365 receives two major release waves a year plus regular service updates, so a plan that lands go-live in the same weeks a wave reaches production, with no regression window, is gambling. A good plan treats the release calendar, business peaks and change freezes as fixed anchors and plans the rest around them.

## When to use

- After the charter is approved and before the partner mobilises the build team.
- When a partner presents a plan and the organisation needs to test whether it is realistic.
- When a go-live date is under pressure or a phase has slipped and needs re-planning.
- When deciding the order in which modules, business units or regions go live.

Not this skill: `programme-management:project-charter` for why and what, `support-operations:cutover-plan` for the detailed cutover runbook, `testing-quality:test-strategy` for the test approach itself, `programme-management:go-no-go` for the go-live decision.

## Questions to ask first

1. Which constraint is fixed: date, budget or scope? The plan flexes the other two, and everyone needs to know which.
2. Which modules are in scope, and do they share core data such as accounts, contacts and products? Shared data decides sequence.
3. Which integrations and data migrations sit on the critical path? These have the longest lead times and the most external dependencies.
4. How much time have key users declared they can give, and when? Business availability, not partner capacity, is usually the real constraint.
5. When are the business peaks, year-end periods and change freezes? Go-live and UAT must avoid them.

## Approach

Structure the plan by Success by Design stage, so that every milestone has a recognisable purpose. Strategize produces the charter and partner selection. Initiate produces fit-to-standard outcomes, the backlog, the solution blueprint and the environment strategy. Implement is iterative build with mock migrations and SIT. Prepare covers UAT, performance testing, training, cutover rehearsal and the go/no-go decision. Operate covers hypercare, continuous improvement and the ongoing release wave cycle.

1. Place the anchors first: business peaks, change freezes and the release wave calendar. Check current Microsoft Learn documentation for this year's wave dates and early access window, and plan a regression cycle in a sandbox before each wave reaches production.
2. Work backwards from go-live through hypercare, cutover, go/no-go, final mock migration, UAT and SIT. Give each a duration based on evidence (volumes, number of scripts, number of integrations), not whatever time is left over.
3. Sequence modules around shared foundations. Security model, business units, accounts, contacts and products come first. Sales often goes first because it depends least on other modules; Field Service depends on assets, products and often ERP inventory; Marketing depends on clean contacts and consent data.
4. Run build in short sprints that each end with a demonstration to key users in a test environment, so that feedback arrives while it is still cheap to act on.
5. Plan more than one full mock migration, with the final one timed and run as a cutover rehearsal.
6. Give every milestone exit criteria, not just a date. A milestone is reached when its evidence exists.
7. Hold contingency explicitly at programme level rather than hiding it inside tasks, and report how much has been consumed.
8. Plan the Operate stage too: hypercare duration, the first release wave after go-live, and the backlog for the next phase.

Load key users against their declared availability from the organisation profile, and show where demand exceeds it. That gap belongs in the RAID log, not in an optimistic plan.

## Outputs

- `delivery-plan` with stages, phases, sprints, milestones and exit criteria.
- A release calendar overlay showing release waves, business peaks and change freezes.
- Key-user loading by stage against declared availability, feeding the `resource-and-skills-gap-plan`.
- A dependency and assumption list to load into the `raid-log`.

## Scale notes

### SMB

One phase, one plan on a page, a modest number of milestones, and the consultant usually acting as project manager. Mostly standard configuration means a short build, but UAT, at least one data migration rehearsal and role-based training must not be dropped to save time. Avoid go-live in the owner's busiest month.

### Enterprise

An integrated master plan rolls up workstream plans for each module, integration and data migration, with a PMO managing the critical path. Expect formal SIT and UAT cycles, multiple environments and deployment pipelines, phased rollout by region or business unit, and dependencies on ERP and telephony programmes with their own calendars. Design authority review points become stage gates in the plan.

## Hand-offs

- `programme-management:raid-log` and `programme-management:governance-cadence` take the dependencies and stage gates.
- `testing-quality:test-strategy` and `integration-and-data:migration-strategy` size their phases inside the plan.
- `support-operations:cutover-plan` and `platform-administration:release-readiness` work from the Prepare stage milestones.
- `project-tailoring:skills-gap-analysis` checks the plan against the declared skills of the team.
- Enterprise plans include `design-authority:design-review` checkpoints before build and before UAT.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Set go-live in the same window as a release wave reaching production or a business peak.
- Compress UAT, data migration rehearsals or training to protect a date.
- Plan key users at availability they have not declared.
- Publish a milestone without exit criteria.
