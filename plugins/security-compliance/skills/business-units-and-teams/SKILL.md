---
name: business-units-and-teams
description: Designs and reviews the Dataverse business unit tree and the use of owner, access and Entra ID group teams, so that data is segregated only where it must be, and classifies findings as blocking or advisory. Use when deciding business units, choosing team types, planning a restructure or modelling several legal entities.
metadata:
  department: security-compliance
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
---

# Business units and teams

The business unit tree is the part of a Dataverse security model that is hardest to change once users and records sit in it. Projects usually go wrong by copying the organisation chart: every department becomes a unit, visibility breaks across units, and the fix is mass sharing that nobody can maintain. The opposite mistake is putting separate legal entities in one unit because it was quicker in the first sprint.

Treat business units as security boundaries and teams as the way people work across them. Like the rest of its department this skill is reviewer-class: findings are blocking or advisory, blocking findings are not overruled by the department under review, and disagreement escalates to the executive sponsor or steering committee.

## When to use

- Designing the business unit tree for a new environment, or reviewing one before build.
- Choosing between owner teams, access teams and Entra ID group teams for a collaboration pattern.
- Planning a reorganisation, merger or country rollout that will move users or records between units.
- Modelling several legal entities or brands that must not see each other's customers.

Not this skill: `security-compliance:security-model-review` for the full review of roles and privileges, `customer-service:queues-and-routing` for distributing work to agents, `solution-architecture:cross-module-data-model` for how tables relate across modules.

## Questions to ask first

1. Which groups of users must be prevented from seeing each other's records, and why? Only a real segregation need (legal entity, regulation, contract, commercial conflict) justifies a unit.
2. How do people collaborate across those boundaries? This decides between teams, matrix access and sharing.
3. Is Entra ID the source of truth for group membership, and who maintains it? Group teams are only as good as the directory behind them.
4. How often does the organisation restructure? Frequent change argues for a flat tree and attribute-based grouping.
5. Which modules work on the same records? Technicians, sellers and agents often need the same account across units.

## Approach

Start with the root unit only, and add a child unit when, and only when, one group must be stopped from seeing another group's records. Region, department and product line are normally attributes on the user or the record, used for views, dashboards and routing, not units. Keep the tree shallow: each extra level multiplies the cases where parent and child depth gives visibility nobody intended.

Check how the environment handles business units before drawing anything. Modernised business units let a user hold roles in units other than their own and let records be owned by a unit other than the owner's, which changes the design a great deal. Check current Microsoft Learn documentation for the present behaviour and the setting that controls it.

Then choose team types deliberately.

1. Owner teams own records collectively (a key account team, a regional service team) and can carry security roles. Use them where ownership genuinely belongs to a group.
2. Access teams give per-record collaboration through access team templates on tables such as account or opportunity, without a security role of their own. Use them where membership differs record by record.
3. Entra ID group teams take membership from a security group or Microsoft 365 group, so joiners, movers and leavers are handled in the directory. Prefer them for any team that maps to a real organisational group.
4. Decide whether team members should inherit the team's privileges for records they own personally, and check the current setting and its effect on Microsoft Learn before relying on it.

Avoid team sprawl. A team per record or per pair of people is a sign that access teams or a different unit design are needed. Write the joiner, mover and leaver procedure early: moving a user between units can affect their roles and the records they own, so check the current behaviour and script the move rather than doing it by hand in production.

Test with personas in at least two units, including one cross-unit scenario per module in scope. A finding is blocking when the design exposes data that must be segregated, or when the operating model only works through routine manual sharing. Naming, depth tidy-ups and documentation gaps are advisory. Where segregation is driven by a legal or regulatory duty, confirm the requirement with the organisation's DPO or legal adviser rather than inferring it from the organisation chart.

## Outputs

- Business unit diagram with the reason for each unit, recorded in the `solution-blueprint`.
- Team catalogue: team, type, purpose, owning unit, membership source, roles and owner.
- Joiner, mover and leaver procedure, including the scripted unit move.
- Findings log with blocking and advisory items; blocking items also go to the `raid-log`.

## Scale notes

### SMB

Most SMB projects need one business unit and a handful of owner teams. Resist adding units for departments or reporting, and use fields and views instead. What must not be skipped is the leaver procedure and one test as a non-administrator user, because a single unit makes it tempting to give everyone wide access.

### Enterprise

Several legal entities, countries or brands usually justify a unit each, with matrix access or group teams for shared services such as a central contact centre. The security-lead owns the design, the design authority approves changes to the tree, and Entra ID group owners are named in the team catalogue. Rehearse reorganisation moves in a sandbox copy with production-like volumes before doing them live.

## Hand-offs

The design goes to `security-compliance:security-model-review` for sign-off alongside the roles. Directory groups and environment access go to `platform-administration:environment-setup`, and record ownership for migrated data goes to `integration-and-data:migration-strategy`. Changes to an approved tree pass through `design-authority:change-impact-assessment` before they are built.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create a business unit only to mirror a department or to drive reporting.
- Rely on manual record sharing as the main way people collaborate.
- Move users or records between business units in production without a rehearsed, scripted procedure.
- Put entities that must be segregated into one unit for speed of delivery.
- Treat a segregation requirement as settled law without confirmation from the DPO or legal adviser.
