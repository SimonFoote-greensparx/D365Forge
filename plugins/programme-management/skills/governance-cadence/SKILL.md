---
name: governance-cadence
description: Designs the governance rhythm for a Dynamics 365 CE programme, covering steering committee, design authority, change control and team ceremonies, with terms of reference, decision rights and escalation scaled from SMB to enterprise. Use when setting up governance, when decisions stall, or when changes are bypassing control.
metadata:
  department: programme-management
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
---

# Governance cadence

Every CRM programme has meetings; fewer have governance. The difference is decision rights. Someone has to be able to approve a scope change, accept a deviation from standard Dynamics 365, release contingency and authorise go-live, and everyone has to know who that is and how quickly they will decide.

The usual failures are a steering committee that hears status reports and makes no decisions, design choices made in chat threads and never recorded, and change requests approved by the partner's project manager because nobody else was asked. Governance that is too heavy fails in a different way: sprints stall waiting for a monthly meeting, so teams quietly route around it.

## When to use

- At Initiate, to set up forums, terms of reference and the decision log.
- When decisions are stalling or being reopened.
- When changes are reaching the build without passing through change control.
- When moving into Operate and governance needs to shift from project to service.

Not this skill: `design-authority:design-review` for running a design review itself, `design-authority:change-impact-assessment` for assessing a specific change, `programme-management:raid-log` for the risk register the forums consume.

## Questions to ask first

1. Who holds budget and scope authority, and at what thresholds does a decision move up a level? Thresholds are what make delegation safe.
2. Is there a design authority, and does it have the power to block? Without blocking power it is an advisory panel.
3. How many workstreams, partners and vendors need coordinating? This sets the number of forums.
4. What corporate governance already exists, such as a PMO, architecture review board or change advisory board? Reuse it instead of duplicating it.
5. How quickly must decisions be made to keep sprints moving? The cadence has to be faster than the build.

## Approach

Design forums around the types of decision, then set the frequency each decision type needs. Every forum gets short terms of reference: purpose, chair, members, quorum, decision rights, inputs, outputs and frequency. Keep a decision log separate from the RAID log so that decisions can be found and are not reopened casually.

1. Steering committee. Chaired by the executive sponsor, typically monthly. Decides scope, budget, date, escalated risks, phase gates and go/no-go. Papers go out in advance and each agenda item ends with a decision or an explicit deferral.
2. Design authority. Chaired by the lead architect or an independent architect, weekly or fortnightly during Initiate and Implement. Owns design standards, deviations from standard, and the choice between configuration, low-code, pro-code and ISV. It classifies findings as blocking or advisory. Blocking findings are not overruled by the workstream under review; disagreement escalates to the steering committee or executive sponsor.
3. Change control. Assesses each change request against the charter and statement of work for cost, date, design, test, training and data impact. Design impact goes to the design authority, commercial impact goes to the statement of work process, and the decision is logged.
4. Team ceremonies. Daily stand-ups, sprint planning, sprint reviews with key users present, and retrospectives. Sprint reviews are where the business sees the system early, so protect them.
5. Operate governance. A change advisory route for production changes, a release wave readiness review twice a year, and a service review with the support team.

Set escalation in writing: team, then design authority or change control, then steering, then sponsor. Let the organisation set the effort and cost thresholds for each level; do not import someone else's numbers.

## Outputs

- Terms of reference for each forum.
- A governance calendar aligned to the sprint cadence and stage gates.
- A decision log and a change request form with its approval route.
- An escalation path with thresholds, and inputs to the `raci-matrix`.

## Scale notes

### SMB

Combine forums. A monthly steering meeting with the sponsor, consultant and project lead can also take design decisions, and change control can be a simple log approved by the sponsor. The consultant often acts as de facto design authority, so arrange an independent design review before build. Do not skip the written decision log or change control; small projects drift through informal "while you're in there" requests.

### Enterprise

Run the full structure: steering, a design authority with an independent chair and workstream leads, change control linked to the organisation's IT service management process, and commercial governance with each partner. After go-live, add a benefits realisation forum and a change advisory route for production. Multiple partners need a shared decision log and a single escalation path.

## Hand-offs

- `design-authority:design-review` and `design-authority:change-impact-assessment` operate inside this structure.
- `programme-management:statement-of-work` handles the commercial side of approved changes.
- `programme-management:raid-log` feeds the steering agenda.
- `project-tailoring:role-mapping` fills chair and member roles from the team's declared skills and availability.
- `support-operations:continuous-improvement` inherits governance at Operate.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Allow the department under review to overrule a blocking design-authority or security-compliance finding.
- Approve a change outside change control because it looks small.
- Run steering as a status meeting with no decisions recorded.
- Give the implementation partner sole approval of scope changes it will be paid to deliver.
