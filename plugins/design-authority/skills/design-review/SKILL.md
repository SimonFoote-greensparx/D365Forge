---
name: design-review
description: Reviews Dynamics 365 CE solution designs against the approved blueprint, architecture principles and project standards, and records each finding as blocking or advisory. Use when a workstream submits a design for approval at a gate or before build, or when a design appears to depart from the blueprint or clash with another workstream.
license: CC-BY-4.0
metadata:
  department: design-authority
  stages: Initiate, Implement
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Design review

On a CRM programme, a design decision made in one workstream quietly constrains all the others. Sales adds its own account hierarchy, Customer Service builds separate contact matching, Field Service introduces a parallel asset model, and by the time anyone notices, the data model has split and the integrations have doubled. Design review is the checkpoint that keeps each design consistent with the blueprint and with every other design.

This is a reviewer-class skill and it is read-only. It reads designs, compares them with the blueprint and standards, and reports findings. It does not rewrite the design; the department under review owns the fix.

## When to use

- A design is submitted for approval at a design gate or before build starts.
- A workstream proposes a change to the data model, security model or integration pattern before sign-off.
- A design seems to conflict with the blueprint or with another workstream's design.
- A design summary is needed for the steering committee.

Not this skill: `design-authority:customisation-challenge` for challenging a single proposed customisation, `design-authority:standards-conformance` for checking built components, `design-authority:change-impact-assessment` for changes after sign-off, `solution-architecture:solution-blueprint` for writing the blueprint, and `security-compliance:security-model-review` for the security design.

## Questions to ask first

1. Is there an approved blueprint and set of standards to review against? Without a baseline, review becomes personal preference.
2. What exactly is submitted, and what decision is requested? Scope the review to that design and that gate.
3. Which other workstreams does the design touch? Shared tables, shared integrations and shared security are where review adds most value.
4. Has the requirement been through fit-to-standard and fit-gap analysis? A design for a gap that standard functionality covers should not have reached review.

## Approach

1. Prepare. Read the design, the related user stories, the relevant blueprint sections and the standards. List the decisions the design makes and the assumptions it relies on.
2. Review against the blueprint. Check that the design uses the agreed data model, favouring standard tables (account, contact, opportunity, case, work order) over new custom ones, and follows the agreed integration patterns and ALM approach. Flag every new table, relationship or interface that the blueprint does not contain.
3. Review cross-cutting concerns. Security (business units, teams, roles, field-level security), performance at expected volume, supportability through release waves, reporting needs, data migration impact, and licensing implications (confirm with the Microsoft licensing guide or your partner).
4. Review consistency across workstreams. Look for duplicated entities, conflicting ownership of the same data, and overlapping automation on shared tables.
5. Record findings. Each finding states what was found, the principle or standard it relates to, the evidence, a recommended remedy and its classification.
   - Blocking: the design cannot proceed to build or release until this is resolved, because it breaks the blueprint, a standard or a non-negotiable requirement, or creates unacceptable risk.
   - Advisory: an improvement the department should consider; it records its decision and may proceed.
6. Communicate the outcome: approved, approved with advisory findings, or not approved pending blocking findings. Blocking findings are not overruled by the department under review. If that department disagrees, the matter escalates to the steering committee or executive sponsor, who may accept the risk explicitly and have it recorded.
7. Track to closure. Revisit blocking findings when the design is resubmitted, and keep a design decision log so later reviews can see why choices were made.

Keep reviews proportionate. A small configuration design needs a short check; a new integration or a data model change needs the full review.

## Outputs

- Design review record with findings classified as blocking or advisory.
- Gate outcome: approved, approved with advisories, or not approved.
- Entries in the design decision log kept alongside the `solution-blueprint`.
- Escalations and explicitly accepted risks recorded in the `raid-log`.

## Scale notes

### SMB

The lead consultant usually plays the design authority, which means reviewing designs they may have written themselves. Ideally arrange a second-pair-of-eyes review by someone outside the delivery (another senior consultant at the partner, or the customer's IT lead) for the blueprint and for any pro-code or integration design. Keep the record light, but still classify every finding as blocking or advisory.

### Enterprise

Design authority is a standing board with a chair, architects for each domain, and security and integration representation, meeting on a fixed cadence with a defined submission process. Findings are tracked formally, design gates appear in the delivery plan, and the steering committee is the escalation route.

## Hand-offs

- Findings return to the department under review, for example `solution-architecture:solution-blueprint`, `integration-and-data:integration-architecture` or `platform-engineering:plugin-design`.
- Security aspects are passed to `security-compliance:security-model-review`.
- Escalations reach the steering committee through `programme-management:governance-cadence`.
- Built components are checked later by `design-authority:standards-conformance`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Edit the design under review instead of reporting findings.
- Allow the department under review to overrule or downgrade a blocking finding.
- Approve a design when no approved blueprint or standards exist, without stating that gap in the outcome.
- Raise findings from personal preference rather than a principle, standard or evidenced risk.
