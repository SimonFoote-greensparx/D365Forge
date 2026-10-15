---
name: user-acceptance-testing
description: Organises user acceptance testing run by business users, with scripts derived from acceptance criteria, entry and exit criteria, a shared defect severity scale and formal sign-off. Use when preparing UAT scripts, selecting and briefing business testers, running UAT triage, or deciding whether the business can accept the solution.
license: CC-BY-4.0
metadata:
  department: testing-quality
  stages: Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# User acceptance testing

UAT is the business confirming that the solution supports the way it will actually work. It is not a training course, a demonstration or the first time anyone has tested the system, although on many CRM projects it ends up being all three. When UAT turns into discovery, change requests flood in, dates slip, and acceptance is given under pressure rather than on evidence.

Good UAT is short, scripted and run by the people who will use the system, logged in with their real security roles, against data that looks like their own. The scripts come from the acceptance criteria agreed when the user stories were written, so the business is checking what it asked for.

## When to use

- Writing UAT scripts and the UAT plan.
- Setting UAT entry and exit criteria.
- Choosing business testers by role coverage and declared availability, and briefing them.
- Running daily UAT triage and separating defects from change requests.
- Preparing UAT sign-off for the go-live decision.

Not this skill: `business-analysis:acceptance-criteria` for writing the criteria, `testing-quality:system-integration-testing` for technical end-to-end proving, `change-adoption:role-based-training` for training end users, and `programme-management:go-no-go` for the release decision.

## Questions to ask first

1. Are acceptance criteria written and agreed for the stories in scope? Without them, scripts become opinions and sign-off becomes a negotiation.
2. Which business roles must accept, and which testers have declared availability for the UAT window? Choose testers for role coverage and availability, never on assessments of individuals.
3. Has SIT exited, and is the UAT environment deployed from the pipeline with migrated data? Starting early wastes testers' time on known defects.
4. Who has authority to sign off each process area? Sign-off from someone without that authority will be reopened after go-live.
5. Do testers hold the licences needed to use the UAT environment? Confirm with the Microsoft licensing guide or your partner.

## Approach

1. Derive scripts from acceptance criteria. Each script follows a business scenario in business language (a day in the life of a role), cites the stories and criteria it proves, and states the expected outcome. Keep scripts at the level of what the user does and sees rather than field-by-field click paths, so testers notice when the process feels wrong.
2. Set entry criteria. SIT has exited with no open critical defects; the UAT environment is deployed with managed solutions; security roles, teams and queues are configured as for production; migrated data is loaded; testers have had a short navigation briefing and know how to log defects; process owners have reviewed the scripts. Whether real customer data may sit in UAT is a decision for the organisation's DPO or legal adviser.
3. Set exit criteria. All scripts executed; no open critical or high defects unless each has an accepted workaround recorded; medium defects carry a fix plan; each process owner has signed off.
4. Use one severity scale, the one agreed in the test strategy. A workable scale is: critical (a core process cannot be completed and there is no workaround), high (a process is seriously impaired or the workaround is costly), medium (wrong but workable), low (cosmetic). Separate change requests from defects: a defect is the system failing an agreed criterion, and anything else is a change request routed to change control.
5. Run UAT as a managed event. Hold a short daily stand-up and triage, keep a visible tracker of scripts executed and defects by severity, have consultants on hand to reproduce issues, and plan a fix-and-retest window into the schedule rather than hoping for one.
6. Close formally. Record what was tested, by which roles, with what outcome, and which defects are carried into go-live with owners and dates.

Test as real users. Business-unit and team-based access, field-level security and queue membership produce exactly the defects that administrator testing hides. For Field Service, technicians should test on Field Service Mobile with their actual devices; for Contact Center channels, include live agent sessions with real routing.

## Outputs

- UAT plan, scripts and tracker within `test-strategy-and-uat-scripts`.
- UAT entry and exit checklist.
- Defect log with severity and disposition, plus a change request list routed to change control.
- UAT sign-off record per process area, feeding `programme-management:go-no-go`.

## Scale notes

### SMB

A handful of business testers over a short window is normal, with the consultant preparing scripts and running triage. Keep sign-off formal even when the sponsor is also a tester. Do not let UAT double as end-user training; if testers are meeting the system for the first time, run a short orientation before scripts start.

### Enterprise

UAT runs per workstream and then end to end across modules, with a UAT manager, test leads and process owners who sign off. Plan tester backfill with line managers well ahead, run a dedicated triage board, expect more than one round, and keep an audit trail of sign-offs. Languages, currencies, time zones and accessibility need their own scripts.

## Hand-offs

- `programme-management:go-no-go` receives the UAT exit report and the list of carried defects.
- `support-operations:cutover-plan` takes the accepted build into cutover; `support-operations:hypercare` inherits carried defects.
- `change-adoption:role-based-training` reuses UAT scenarios as a basis for training.
- Change requests raised in UAT go to `design-authority:change-impact-assessment`; access findings go to `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Let consultants or developers execute UAT scripts on behalf of business testers.
- Run UAT logged in as System Administrator.
- Accept sign-off from someone without authority for that process area.
- Relabel change requests as defects to get them built before go-live.
- Rate or rank individual testers in UAT reports.
