---
name: cutover-plan
description: Plans the move from legacy systems to live Dynamics 365 CE as a timed, owned runbook with rehearsals, data freeze rules, decision checkpoints and rollback triggers. Use when building or rehearsing a cutover runbook, agreeing a data freeze, sequencing final migration and integration switch-on, or deciding the point of no return.
license: CC-BY-4.0
metadata:
  department: support-operations
  stages: Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Cutover plan

Cutover is the short window in which the organisation stops using its old system and starts using the new one. It touches every workstream at once: final data migration, integration switch-over, security, user access, communications and support readiness. It goes wrong when it is treated as a weekend task written up in the last fortnight, when the runbook has never been rehearsed, when the timings are guesses, and when nobody has decided the point after which rollback is no longer possible.

A good cutover plan is a timed, owned, rehearsed runbook with explicit decision points and a rollback route that has been thought through before anyone needs it.

## When to use

- Building the cutover runbook and its timings.
- Planning and reviewing cutover rehearsals.
- Agreeing data freeze rules and the handling of in-flight work.
- Defining rollback triggers and the point of no return.
- Sequencing integration switch-on and legacy shutdown.

Not this skill: `programme-management:go-no-go` for the release decision itself, `integration-and-data:mock-migrations` for migration rehearsal mechanics, `integration-and-data:reconciliation` for proving migrated data, and `support-operations:hypercare` for the period after go-live.

## Questions to ask first

1. Is the go-live a big bang, or phased by module, region or business unit? This decides how many cutovers there are and whether old and new systems run side by side.
2. How long does the final migration take, measured in a rehearsal? The freeze and outage window depend on measured timings, not estimates.
3. How much downtime and data freeze can the business tolerate? This sets the window and may force a delta load.
4. Can the legacy system be switched back on, and until when? Rollback is only real if the old system and its integrations can resume.
5. Are there change freezes, trading peaks or regulatory dates to avoid? These often constrain the date more than project readiness does.

## Approach

1. Build the runbook as a timed task list. Every line carries an ID, task, owner, dependency, planned start, duration, verification step and any communication it triggers. Cover pre-cutover work (production environment ready, solutions deployed as managed, business units, teams and security roles in place, licences assigned, integrations configured but disabled), the cutover itself (freeze, final extract, migration, reconciliation, integration switch-on, smoke test) and post-cutover (access opened, announcements, hypercare start).
2. Agree the data freeze. Define what stops in the legacy system and when, how in-flight work is handled (open cases, open opportunities, scheduled work orders, running marketing journeys), and whether a delta load is needed. Business owners sign the freeze rules, because they are the ones who must enforce them.
3. Rehearse more than once. The first rehearsal proves the sequence; a later one proves timings at production-like volume. Record actual durations, update the runbook, and treat every step that overran as a risk to be worked.
4. Build in decision points. Place explicit checkpoints in the runbook (before freeze, after migration and reconciliation, before opening to users), each with a named decision maker and written criteria.
5. Define rollback. State the triggers (reconciliation outside tolerance, a critical integration failing, smoke tests failing), the steps to restore legacy operation, and the point of no return after which the team fixes forward. Walk through the rollback steps in a rehearsal, even if only on paper.
6. Prepare the command centre. One channel, one runbook tracker, a cutover manager who calls each step, named contacts in every team including the partner and partner-system owners, and an agreed route for raising a Microsoft support case if the platform misbehaves.
7. Control access. Elevated access for migration and configuration is time-bound and removed when the runbook closes.

Smoke tests should be short scripted journeys per role, run by business representatives in production immediately before access opens to everyone.

## Outputs

- Cutover runbook within `cutover-and-hypercare-checklist`.
- Data freeze rules signed by business owners.
- Rehearsal reports with actual timings and lessons.
- Rollback plan and point-of-no-return statement.
- Command centre contact list and escalation path.
- Cutover risks recorded in the `raid-log`.

## Scale notes

### SMB

Cutover is often a single weekend, with the consultant running the runbook and a few business users smoke testing. Keep it written, timed and rehearsed at least once with a full data load. Rollback can be simple (for example, keeping the old system available until the business confirms on the first working day) but it must be decided in advance.

### Enterprise

Expect a cutover manager, a runbook spanning every workstream, several rehearsals, phased cutovers by region or module, and formal checkpoints. Coordinate with ERP, telephony and middleware change windows and with the organisation's change advisory board.

## Hand-offs

- `programme-management:go-no-go` owns the final decision and the checkpoint criteria.
- `integration-and-data:mock-migrations` and `integration-and-data:reconciliation` supply migration timings and reconciliation tolerances.
- `support-operations:hypercare` starts when the runbook closes.
- `security-compliance:security-model-review` confirms that temporary elevated access has been removed after cutover.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Go live on a runbook that has never been rehearsed with realistic data volumes.
- Leave rollback triggers and the point of no return to be decided during the cutover itself.
- Leave elevated migration or administrator access in place after cutover.
- Change the production solution during cutover outside the runbook.
