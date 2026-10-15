---
name: super-user-network
description: Designs and runs a super-user network for Dynamics 365 CE, covering the role, selection from declared skills and availability, agreed time commitment, enablement, and their part in testing, training, hypercare and release waves. Use when recruiting super users, defining their responsibilities, or keeping the network active after go-live.
metadata:
  department: change-adoption
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
---

# Super-user network

Super users multiply the programme's reach. They translate Dynamics 365 into local practice, catch design problems early, absorb the first wave of questions at go-live, and keep good habits alive long after the project team has gone. In practice, a healthy network is one of the strongest levers on adoption that a CRM programme controls.

Networks fail when super users are whoever could be spared, when the same few people are asked to do it on top of a full workload with no time protected, when they are trained no differently from everyone else, and when the network quietly dissolves at the end of hypercare. A network that only exists for go-live leaves nobody to absorb the next release wave.

## When to use

- At Initiate, to define the role and recruit the first super users, ideally from fit-to-standard participants.
- In Implement and Prepare, to involve super users in sprint reviews, UAT and train-the-trainer.
- At go-live and hypercare, to run floor support and feedback.
- In Operate, to keep the network active through release waves and staff changes.

Not this skill: `change-adoption:role-based-training` for curricula for all users, `support-operations:support-model` for the formal support tiers, `project-tailoring:role-mapping` for mapping the project team to delivery roles.

## Questions to ask first

1. How many sites, teams, roles and shifts need coverage? Coverage decides network size; let the organisation set the ratio.
2. How much time can line managers release, and for how long? Super-user time must be declared and agreed, not assumed.
3. Which tasks will super users take on: testing, training, floor support, feedback, release previews? The task list shapes selection and enablement.
4. How will the network connect to the support model and backlog after go-live? Without a route, feedback goes nowhere and the network loses heart.
5. What recognition can the organisation offer? Development opportunities and visible thanks sustain the network.

## Approach

1. Write the role description by stage. In Initiate, super users take part in fit-to-standard workshops. In Implement, they give feedback at sprint reviews and test early builds. In Prepare, they are UAT testers, trainee trainers and then local trainers. At go-live, they are floor-walkers and the first point of contact. In Operate, they collect feedback, preview release wave changes in a sandbox and welcome new joiners.
2. Plan coverage so that every site, team, shift and major role group has someone to turn to. Agree the ratio locally with sponsors rather than importing a standard figure.
3. Select from volunteers and nominations using declared skills (process knowledge, comfort with new tools, willingness to help colleagues) and declared availability, and agree each place with the line manager. Use the skills and availability recorded in the organisation profile where relevant. Do not use performance ratings or personal characteristics, and do not rank candidates against each other.
4. Agree the time commitment in writing for each stage, with figures set by the organisation and signed off by line managers. Revisit it before UAT and go-live, when demand peaks.
5. Enable them properly: earlier and deeper training, access to a sandbox in their real security role, a direct channel to the project team, previews of upcoming changes, and a short guide on triage and escalation.
6. Run a regular rhythm: a short network call, a Teams channel or community space, and a feedback log that feeds the backlog with visible outcomes.
7. After go-live, place the network inside the support model as the first local point of help, with a clear escalation route to the service desk.
8. Review network health in aggregate, such as coverage by site and role, questions resolved locally and feedback items raised, and refresh membership as people change jobs.

## Outputs

- A super-user role description by stage.
- A coverage map by site, team, role and shift.
- Selection criteria based on declared skills and availability, and written time agreements.
- A network charter, meeting rhythm and feedback log.

## Scale notes

### SMB

Two or three super users are often enough, frequently the key users who joined fit-to-standard. The consultant enables them directly. Even at this size, write the role down, agree their time with the owner and give them a route to raise problems after the consultant leaves.

### Enterprise

Appoint a network lead and regional coordinators, run a structured enablement programme, and integrate the network with the service desk tiers. Plan succession, because super users are often promoted or move roles, and keep the network engaged for every release wave.

## Hand-offs

- `change-adoption:role-based-training` uses super users as trainers.
- `testing-quality:user-acceptance-testing` draws testers from the network.
- `support-operations:hypercare` and `support-operations:support-model` place the network in the support routes.
- `support-operations:continuous-improvement` receives the feedback log.
- Reviewer sign-off: none required; super-user access in test environments follows `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Select or rank super users using performance ratings or personal characteristics.
- Give super users system administrator rights in production as a convenience.
- Assume super-user time without written agreement from their line managers.
- Let the network lapse at the end of hypercare.
