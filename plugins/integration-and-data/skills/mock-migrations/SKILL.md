---
name: mock-migrations
description: Plans and runs rehearsal migrations into non-production environments, recording timings, error rates and defects and tuning throughput until the load fits the cutover window. Use when scheduling mock loads, setting entry and exit criteria, investigating slow or failing loads, or preparing the dress rehearsal before go-live.
license: CC-BY-4.0
metadata:
  department: integration-and-data
  stages: Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Mock migrations

A migration that has not been rehearsed end to end at full volume will not fit its cutover window, and the team will find out on go-live weekend. Mock migrations turn the strategy and the mappings into a timed, repeatable procedure that someone tired can follow at three in the morning. Projects go wrong by running one trial load, by rehearsing with a sample instead of full volume, and by fixing defects by hand in the target so the next run repeats them.

## When to use

- Planning the number, timing and environments of mock migrations.
- Running a mock and recording timings, error rates and defects.
- Tuning throughput when loads are too slow or hit throttling.
- Preparing the dress rehearsal whose results feed the cutover runbook.

Not this skill: `integration-and-data:reconciliation` for checking results, `integration-and-data:data-mapping-and-cleansing` for fixing rules, `support-operations:cutover-plan` for the go-live runbook as a whole, `testing-quality:performance-testing` for user load.

## Questions to ask first

1. How long is the cutover window, and what else must happen inside it? The migration gets only part of the window, and timings are judged against that share.
2. Does the mock environment resemble production in solutions, plug-ins, flows and capacity? Timings from a stripped-down environment mislead.
3. Will each mock use a fresh full extract? Stale extracts hide source changes and new quality issues.
4. Who triages migration defects, and who can change mappings quickly? Without fast triage, mocks repeat the same failures.
5. Will business users validate each mock in the app? They find errors of meaning that counts never reveal.

## Approach

Plan a sequence of mocks with rising realism, and write entry and exit criteria for each before it starts.

1. Mock 1, technical. Proves the pipeline end to end on a full extract, with errors expected. Exit when every table loads and every error category is understood.
2. Mock 2, quality. Full volume with mapping and cleansing fixes applied, reconciliation run, and business users checking records in the app. Exit at the agreed error thresholds with no open critical defects.
3. Dress rehearsal. Full volume into a production-like environment, run strictly from the cutover runbook by the people who will run it for real, timed step by step. Include delta loads and post-load steps such as re-enabling plug-ins and flows, setting record states, sharing and security checks. Exit when the load fits the window with contingency and reconciliation is signed.

Add further mocks if exit criteria are not met. Do not lower the criteria to protect the date unless the steering committee records that decision and its risk.

Record the same things in every mock so results can be trended:

- Start and end time per table and step, with rows per minute, so the slowest steps are obvious.
- Error log per table: rows extracted, loaded and rejected, error message and root cause category (source data, mapping, target configuration, platform).
- Defect log: each defect with owner, fix, and the mock in which the fix is proven.
- Environment state: solution versions, which plug-ins, flows and duplicate detection rules were active, and any settings changed for the load.

When loads are too slow, tune in this order. First pre-resolve lookups to alternate keys or GUIDs in staging so the load does not query Dataverse row by row. Then use bulk operations and tuned parallelism, honouring the Retry-After value on throttling responses; check current Microsoft Learn documentation for service protection limits and throughput guidance rather than designing around them. Then decide which custom plug-ins, flows and duplicate detection to suspend or bypass, but only where the logic is not needed for historic data or can be safely replayed; check current Microsoft Learn documentation for the bypass options and privileges. Load attachments in a separate parallel stream, because they often dominate elapsed time. Agree with security-compliance whether auditing stays on during load, rather than switching it off quietly.

## Outputs

- Mock migration plan with schedule, environments, data sources, and entry and exit criteria.
- Timing log per mock, trended across mocks, feeding the cutover window estimate.
- Migration defect log with root cause, owner and verification mock.
- Final load runbook, proven at dress rehearsal and merged into the `cutover-and-hypercare-checklist`.
- Mock completion report for the go/no-go evidence pack.

## Scale notes

### SMB

Even a small migration needs a full trial load into a sandbox and a second clean run before go-live. The consultant runs it and the customer's administrator checks records in the app. Timings matter less, but the written runbook still matters, because the person running the final load may be working alone. Do not skip the clean second run.

### Enterprise

A migration lead runs mocks as scheduled events with daily defect triage across source system, ETL and CRM teams. Mocks are aligned with integration testing and user acceptance testing so testers work on migrated data, environment copies and refreshes are booked with platform administration, and dress rehearsal results are a formal input to the go/no-go decision.

## Hand-offs

- `integration-and-data:reconciliation` runs after every mock.
- `support-operations:cutover-plan` takes the rehearsed runbook and timings.
- `testing-quality:user-acceptance-testing` uses data from a recent mock.
- `programme-management:go-no-go` receives the mock completion evidence.
- `platform-administration:environment-setup` provides and refreshes mock environments.
- Review: `security-compliance:security-model-review` before real personal data is loaded into any non-production environment; whether that is permissible is a question for the organisation's DPO or legal adviser.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Treat a sample load as proof that full volume fits the cutover window.
- Fix migration defects by editing records in the target instead of fixing the rule and re-running.
- Lower exit criteria to keep the go-live date without a recorded steering decision.
- Load real customer personal data into non-production environments without an approved basis for doing so.
- Leave plug-ins, flows or auditing in a different state after load from the one the runbook specifies.
