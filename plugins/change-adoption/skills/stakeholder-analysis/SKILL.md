---
name: stakeholder-analysis
description: Identifies stakeholder groups for a Dynamics 365 CE rollout and assesses change impact by role across process, system, data, reporting and ways of working, to size the change effort and target engagement. Use when starting change planning, assessing how ready a business unit is, or building a change impact assessment for a phase or module.
license: CC-BY-4.0
metadata:
  department: change-adoption
  stages: Strategize, Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Stakeholder analysis and change impact

Most CRM programmes that fail do so on adoption rather than technology. The system goes live, sellers keep their spreadsheets, agents keep working from the shared inbox, and the data that was meant to power forecasting and service reporting never arrives. Knowing which roles experience the biggest change, and in what way, tells the programme where to spend its change effort.

Analysis goes wrong when the stakeholder map becomes a list of names with opinions about who is resistant, when impact is assessed by module rather than by role, and when managers are forgotten even though their reporting, coaching and pipeline reviews often change the most. It also goes wrong when it is done too late to influence design.

## When to use

- At Strategize or Initiate, to identify stakeholder groups and plan engagement.
- After future-state processes are mapped, to assess impact by role.
- Before each phase or wave, to check readiness and change saturation in the affected groups.
- When a business unit is pushing back and the programme needs to understand why.

Not this skill: `change-adoption:communications-plan` for planning messages and channels, `change-adoption:role-based-training` for training design, `design-authority:change-impact-assessment` for the technical impact of a design change.

## Questions to ask first

1. Which roles touch the in-scope processes, and roughly how many people are in each? Group size drives the scale and format of every intervention.
2. What changes for each role in process, system, data entry, reporting and measures? The kind of change decides the kind of support needed.
3. What else is changing for these groups at the same time? Change saturation is a common hidden reason for low adoption.
4. Are there works councils, unions or consultation obligations? These affect timing and content; take advice from HR and the organisation's legal adviser.
5. Who sponsors the change inside each business unit? Local sponsorship matters more than central announcements.

## Approach

Work with groups and roles throughout. The aim is to understand how the change lands on each kind of job, not to profile individuals.

1. List stakeholder groups by role and business unit: executives, line managers, front-line roles per module (sellers, marketers, service agents, dispatchers, technicians), back-office teams, IT support, partners and, where portals or communications change, customers. Use the organisation profile and the role catalogue to keep role names consistent.
2. Map each group's interest and influence, and identify the sponsor role for each.
3. Assess impact per role on five dimensions: process, system, data, reporting and measures, and organisation. Rate each as low, medium or high, with a one-line description of the change from today to tomorrow. Typical examples: sales managers moving forecast reviews from spreadsheets to Dynamics 365 forecasts and dashboards; service agents moving from a shared mailbox to queues and service levels; technicians moving from paper or a legacy app to Field Service Mobile with offline use; marketers adopting consent-driven segments.
4. Assess readiness at group level only, using anonymous and aggregated pulse surveys or structured conversations with sponsors.
5. Build a change saturation calendar showing other initiatives, peaks and freezes for each group.
6. Derive interventions from impact: high-impact roles get early involvement (fit-to-standard participants, super users, sprint reviews), hands-on training and manager briefings; low-impact roles need awareness and quick guides.
7. Feed risks into the RAID log and refresh the assessment at each stage gate.

Stakeholder registers that contain names are personal data. Keep them minimal, restrict access to the project team, and send data protection questions to the organisation's DPO.

## Outputs

- A stakeholder group register with interest, influence and sponsor role.
- A change impact assessment by role, presented as a heat map.
- A change saturation calendar.
- Aggregated readiness findings, and inputs to the `training-and-communications-plan` and `raid-log`.

## Scale notes

### SMB

The owner and consultant can do this in one working session, producing a short table of roles and what changes for each. Even with few roles, identify what changes for managers and avoid the busiest trading periods. Keep in mind that in very small teams a role can be one person, so discuss impact as a role, not as a verdict on that person.

### Enterprise

Appoint a change lead per workstream, assess impact by business unit and country, and coordinate with HR on consultation obligations. Readiness is assessed formally at stage gates, and saturation is managed with the organisation's portfolio office.

## Hand-offs

- `change-adoption:communications-plan` uses the impact and sponsor roles.
- `change-adoption:role-based-training` sizes training from the impact ratings.
- `change-adoption:super-user-network` plans coverage for high-impact groups.
- `programme-management:raid-log` takes adoption risks.
- No reviewer sign-off is required; data protection questions about stakeholder records go to the DPO.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Rate named individuals on resistance, attitude, performance or personal characteristics.
- Assess impact by module instead of by role.
- Keep stakeholder personal data beyond what the plan needs.
- Leave line managers out of the impact assessment.
