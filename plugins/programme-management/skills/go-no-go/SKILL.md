---
name: go-no-go
description: Defines the go/no-go criteria, evidence and decision procedure for a Dynamics 365 CE go-live, covering test exit, data reconciliation, cutover and rollback rehearsal, training coverage, support readiness and open reviewer findings. Use when preparing the go-live decision, writing readiness criteria, or when a go-live date is under pressure.
metadata:
  department: programme-management
  stages: Prepare
  modules: All
  status: draft
---

# Go/no-go decision

The go-live decision is the most pressured decision in a CRM programme. Criteria written in the final week tend to be shaped by the evidence that happens to exist, and a programme that has announced a date finds reasons to keep it. The remedy is to agree the criteria, thresholds and evidence owners early in the Prepare stage, so the go/no-go meeting checks evidence against a standard set when nobody was under pressure.

Typical failures are criteria such as "UAT complete" with no defect thresholds, a rollback plan that exists on paper but was never rehearsed, a support team that has not seen the system, and no clear statement of who actually makes the decision.

## When to use

- At the start of Prepare, to define and approve the criteria.
- Before each readiness checkpoint leading up to cutover.
- When a go-live date is under pressure and the steering committee needs a structured decision.
- For each wave of a phased rollout.

Not this skill: `support-operations:cutover-plan` for the cutover runbook, `platform-administration:release-readiness` for platform and environment readiness checks, `testing-quality:user-acceptance-testing` for planning and running UAT.

## Questions to ask first

1. Who makes the decision, and who can block it? The sponsor decides, but open blocking findings from design authority or security compliance must be resolved or escalated, never waived by the delivery team.
2. What is the rollback position, and where is the point of no return? A plan without a rehearsed rollback is a one-way door.
3. What defect severities will the business accept at go-live, and with what workarounds? Agree the severity definitions before UAT, not after.
4. Which business events constrain the timing? Month-end, peak season and campaigns limit when cutover and hypercare can happen.
5. What evidence will each workstream bring, and from which source? Evidence must be verifiable, not a verbal assurance.

## Approach

Write each criterion with a measure, a threshold, the evidence required, an owner and a status of met, met with conditions, or not met. Get steering approval for the set early in Prepare, and change it afterwards only through change control.

1. Solution and testing. SIT and UAT exit criteria met; no open defects above the agreed severity; accepted defects have documented and trained workarounds; performance testing passed; regression run after the most recent platform update.
2. Data. Final mock migration completed within the cutover window; reconciliation signed off by the business data owners; the approach for delta loads tested.
3. Integration. Production endpoints, credentials and monitoring in place and tested end to end.
4. Security and compliance. Security roles tested by real users in their own roles; no open blocking findings from security compliance review; for Marketing, consent data verified before any journey sends.
5. People. Training coverage by role complete, super users in place, go-live communications sent, managers briefed. Report coverage by role, not individual scores.
6. Support. Support model live, hypercare rota staffed, incident routes and known errors published.
7. Platform. Production environment configured, capacity checked, licences assigned (confirm with the Microsoft licensing guide or your partner).
8. Cutover. Rehearsed with timings, rollback rehearsed, point of no return defined, business contingency agreed for the cutover window.

Run the decision in stages: an early readiness checkpoint that leaves time to fix gaps, the formal go/no-go shortly before cutover starts, and a confirmation at the point of no return. If a Success by Design go-live readiness review is run by Microsoft FastTrack or your partner, schedule it early enough for its findings to be addressed.

The decision has three possible results: go; go with conditions, each condition with an owner and a deadline; or no-go with a re-plan. Record the decision, the evidence reviewed and the reasoning.

## Outputs

- Approved go/no-go criteria with thresholds, evidence and owners.
- A readiness scorecard for each checkpoint.
- A decision record with conditions, owners and deadlines.
- Inputs to the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

One checklist and one meeting with the sponsor, consultant and lead key user. Keep the criteria few, but never drop UAT sign-off, data reconciliation, trained users, a rollback position and a named support contact. A short dress rehearsal of cutover is worth more than another round of review.

### Enterprise

Each workstream brings a readiness report, design authority and security compliance confirm there are no open blocking findings, and the organisation's change advisory process approves the production change. Phased rollouts need criteria per wave, plus a check that lessons from the previous wave have been applied. Business continuity owners sign off the cutover window.

## Hand-offs

- `support-operations:cutover-plan` and `support-operations:hypercare` execute after a go decision.
- `platform-administration:release-readiness` and `integration-and-data:reconciliation` supply evidence.
- `testing-quality:user-acceptance-testing` supplies UAT exit evidence.
- Reviewer sign-off: `design-authority:design-review` and `security-compliance:security-model-review` must report no open blocking findings. Disagreement escalates to the steering committee or executive sponsor.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Rewrite the criteria in the final week to fit the evidence available.
- Go live with an open blocking design-authority or security-compliance finding waived by the delivery team.
- Go live without a rehearsed rollback and a defined point of no return.
- Use individual training scores as go-live evidence.
