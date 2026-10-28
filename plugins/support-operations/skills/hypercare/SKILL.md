---
name: hypercare
description: Runs the hypercare period after a Dynamics 365 CE go-live, setting scope, planned duration, staffing, daily triage, fix cadence and exit criteria for handing over to business-as-usual support. Use when planning hypercare, running triage in the first weeks after go-live, or deciding whether to extend or exit hypercare.
license: CC-BY-4.0
metadata:
  department: support-operations
  stages: Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Hypercare

The first weeks after go-live decide whether users trust the new system. Small problems, such as a missing queue membership, a view that hides records a team expects to see, or an email that does not become a case, feel large to people who have just lost the system they knew. Hypercare is the period of intensified support that absorbs this, fixes what matters quickly and hands over cleanly to the support model.

It usually goes wrong in one of two ways. Either hypercare has no defined end and quietly becomes the project team doing support indefinitely, or it ends on a calendar date while serious issues are still open.

## When to use

- Planning hypercare scope, duration, rota and exit criteria.
- Running daily triage after go-live.
- Deciding how fixes reach production during hypercare.
- Deciding whether to extend hypercare or exit to business-as-usual support.

Not this skill: `support-operations:support-model` for steady-state support, `support-operations:incident-management` for severity definitions and major incidents, `support-operations:cutover-plan` for the go-live itself, and `change-adoption:adoption-metrics` for measuring adoption.

## Questions to ask first

1. What is in scope: only the new solution, or also integrations, data, devices and access? Users do not draw these lines, so a narrow scope needs clear routing for everything else.
2. Who staffs hypercare from the project, the partner and the future support team, and with what declared availability? The support team should work inside hypercare, not wait at the end of it.
3. Which defects and workarounds were carried from UAT? They shape the first days and the first communications.
4. Does a business peak (month-end, a seasonal rush, a campaign launch) fall in the window? Plan extra cover or adjust the duration.

## Approach

1. Plan duration, decide exit by criteria. Set a planned duration long enough to cover at least one occurrence of every critical business cycle (month-end, a billing run, a planned maintenance round for field service). The plan sets expectations; the exit criteria decide when it ends.
2. Agree exit criteria up front. No open critical or high incidents; incident volume falling and within what the support team can absorb; known defects with owners and dates; knowledge articles and runbooks handed over; the support team running triage itself; monitoring and alerting live.
3. Staff with a blend. Consultants who built the solution, partner developers for fixes, super-users on the floor, and the support team alongside them. Build the rota from declared skills and availability, not from judgements about individuals.
4. Run daily triage. A short fixed meeting each morning covering new issues, severity, owner, fix or workaround, and what to tell users. Sort issues into defects, training needs, data problems, access problems and change requests, and send change requests to the backlog instead of building them in hypercare.
5. Control fixes. Fixes go through the pipeline to production as managed solutions after a regression check, on an agreed release rhythm, with an emergency route for critical issues. Nothing is edited directly in production.
6. Communicate. Publish known issues and workarounds, what was fixed, and how to get help. Super-users are the fastest channel into each team.
7. Watch the right signals. Track sign-ins and usage alongside incident volume. Low usage with few incidents usually means people have drifted back to spreadsheets, not that all is well.
8. Exit formally. Review the criteria at a hypercare exit meeting, hand open items to the support model with named owners, and move deferred enhancements to the improvement backlog.

## Outputs

- Hypercare plan, rota and exit criteria within `cutover-and-hypercare-checklist`.
- Contact routes for users and super-users.
- Daily triage log with categories, owners and status.
- Known issues and workarounds list for users.
- Hypercare exit report and handover list.

## Scale notes

### SMB

Hypercare is usually short, with the consultant on call and a super-user in each team. Keep daily triage even if it is a brief call. Do not skip exit criteria, and make sure the post-hypercare support arrangement (often a partner contract) is signed before hypercare ends, because an SMB without an internal CRM team has nowhere else to turn.

### Enterprise

Expect a hypercare manager, a command centre for the first days, triage per workstream feeding a central board, floor-walkers or super-users at each site, and phased exits by module or region. Hypercare status goes to the steering committee, and exit is a formal decision.

## Hand-offs

- `support-operations:support-model` takes over at exit, and `support-operations:incident-management` processes apply from the first day.
- `support-operations:continuous-improvement` receives deferred enhancements and change requests.
- `change-adoption:adoption-metrics` and `change-adoption:super-user-network` use hypercare signals to target adoption work.
- Fixes that change signed-off design need `design-authority:change-impact-assessment`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- End hypercare on its calendar date while critical or high issues remain open.
- Edit configuration directly in production to fix hypercare issues.
- Build change requests as hypercare fixes.
- Use hypercare data to rate or rank individual users or staff.
