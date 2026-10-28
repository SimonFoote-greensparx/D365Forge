---
name: role-based-training
description: Builds a role-based training plan for Dynamics 365 CE from security roles and future-state processes, defining curricula, formats, training environment, materials and schedule per role. Use when designing the training approach, preparing train-the-trainer, setting up a training environment, or planning training for new joiners and release waves.
license: CC-BY-4.0
metadata:
  department: change-adoption
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Role-based training

Feature tours do not change how people work. Users need to know how to do their own job in the new system: how a seller qualifies a lead and updates a forecast, how an agent picks up and resolves a case within its service level, how a technician completes a work order offline. Building training from security roles and future-state processes means each person learns exactly what they will see and do on day one.

Training goes wrong when it is delivered in a generic environment where everyone has full access, when it happens months before go-live and is forgotten, when materials are not updated after late UAT changes, and when nobody plans for the people who join after go-live or for the twice-yearly release waves.

## When to use

- During Implement, once security roles and future-state processes are stable enough to design curricula.
- In Prepare, to set up the training environment, train the trainers and schedule end-user sessions.
- In Operate, for new-joiner paths, refreshers and release wave updates.
- When a phased rollout needs training waves aligned to each go-live.

Not this skill: `change-adoption:super-user-network` for recruiting and running super users, `change-adoption:communications-plan` for messages and invitations, `testing-quality:user-acceptance-testing` for UAT itself.

## Questions to ask first

1. What are the final security roles, and which processes does each role carry out? These are the rows and columns of the curriculum.
2. How many users are in each role, and where, on which shifts and in which languages? This drives format, logistics and the number of sessions.
3. Is there a training environment with the go-live build and realistic, non-identifying data? Training in the wrong build creates confusion at go-live.
4. Who can deliver training, based on declared skills and availability? Internal trainers, super users and the partner each have different costs and credibility.
5. How will new joiners and release wave changes be handled after go-live? Without a plan, knowledge decays within months.

## Approach

1. Build a role-to-curriculum matrix. Rows are business roles aligned to security roles; columns are processes and modules; each cell names a learning module. Users with more than one role follow a combined path. Take role definitions from the agreed security model rather than inventing training-only roles.
2. Design each learning module around a scenario from the future-state process, reusing UAT scripts as the basis for exercises. A day-in-the-life exercise at the end of each curriculum ties the modules together.
3. Choose formats by impact. High-impact roles get hands-on, instructor-led sessions; low-impact roles get short recorded walkthroughs and quick reference guides. Microsoft Learn modules can provide background but do not replace training on the organisation's own processes. For in-product guidance options, check current Microsoft Learn documentation.
4. Specify the training environment: a copy of the UAT-approved build with synthetic or properly anonymised data, users signing in with their own accounts in their real security roles, and a reset routine between sessions. Loading production personal data needs the DPO's approval.
5. Train the trainers first, usually super users, once UAT is stable, and let them rehearse each session.
6. Schedule end-user training as close to go-live as logistics allow, completing before the go/no-go checkpoint, with a short refresher in the days before cutover.
7. Keep materials under version control and update them whenever late changes or UAT workarounds are agreed.
8. Track coverage and completion by role and team, and use any knowledge checks to improve the training, not to appraise people. Help-desk themes in hypercare show where to reinforce.
9. Plan Operate from the start: a new-joiner path, refreshers, and a short role-based update for each release wave.

Role specifics matter. Technicians should practise on the devices they will use, including offline scenarios in Field Service Mobile. Service agents should practise picking up work from queues in a test channel. Managers need dashboards, forecasting and coaching views, not only data entry.

## Outputs

- A role-to-curriculum matrix.
- The training section of the `training-and-communications-plan`, with schedule and logistics.
- A training environment specification and reset routine.
- Training materials, exercises and quick reference guides, plus a train-the-trainer plan.
- A coverage report by role for go/no-go.

## Scale notes

### SMB

The consultant trains a small group of super users or the owner, who then trains colleagues. A few hands-on sessions and a set of quick reference guides are usually enough, delivered in a sandbox copy of the build. Keep it role-based and hands-on even when the group is small.

### Enterprise

A training lead coordinates trainers, a learning management system, localisation and accessibility, and training waves aligned to a phased rollout. The training environment is refreshed through the deployment pipeline so it always matches the release being taught.

## Hand-offs

- `change-adoption:super-user-network` supplies trainers and floor support.
- `change-adoption:adoption-metrics` shows where reinforcement is needed after go-live.
- `platform-administration:environment-setup` provisions the training environment.
- `support-operations:support-model` takes the new-joiner and refresher paths into run.
- Reviewer sign-off: `security-compliance:security-model-review` confirms the roles used in training match production; data in the training environment needs DPO approval.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Train users with system administrator access instead of their real security role.
- Load unmasked production personal data into a training environment without DPO approval.
- Rank, appraise or report on individuals using training assessments.
- Schedule training so far ahead of go-live that users forget it before they need it.
