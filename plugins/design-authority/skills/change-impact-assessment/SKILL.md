---
name: change-impact-assessment
description: Assesses proposed changes to a signed-off Dynamics 365 CE design for impact on data model, automation, security, integrations, migration, testing, training, cost and timeline, recording findings as blocking or advisory. Use when a change request arrives after design sign-off, during UAT or cutover, or after go-live.
license: CC-BY-4.0
metadata:
  department: design-authority
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Change impact assessment

Once a design is signed off, every change has a ripple. A new mandatory column breaks an integration that creates records, a change to case ownership invalidates queue routing and reports, a new status reason alters an SLA calculation, and a small security change breaks test scripts and training material. Change requests are usually sized on build effort alone, and the ripples are discovered in UAT or in production.

Change impact assessment is the reviewer-class check that every change after sign-off is understood before it is approved. It is read-only: it assesses and reports, the requesting department owns the change, and the change board or steering committee makes the decision.

## When to use

- A change request arrives after design sign-off.
- UAT produces requests that are not defects.
- A change is proposed during cutover or hypercare.
- A post-go-live backlog item would alter the data model, security, integrations or signed-off design.

Not this skill: `programme-management:raid-log` for logging risks and decisions, `programme-management:governance-cadence` for the rhythm of the change board, `design-authority:design-review` for reviewing a new design, and `support-operations:continuous-improvement` for prioritising the post-go-live backlog.

## Questions to ask first

1. What is the change, who requested it, and which business outcome does it serve? A change without an outcome should not go further.
2. What was signed off, and where is it recorded? The baseline decides what counts as a change.
3. What stage is the project in? The same change costs far more during UAT or cutover than during build.
4. Is there a deadline or regulatory driver? This affects whether to accept risk now or defer.

## Approach

1. Establish the baseline. Identify the signed-off artefacts the change touches: blueprint sections, data mapping, integration specifications, security model, test scripts and training material.
2. Trace the impact through a fixed checklist, so nothing is assessed from memory.
   - Data model: tables, columns, relationships, calculated and rollup columns.
   - Process and automation: business process flows, plug-ins, flows, business rules, SLAs and routing.
   - Integrations: payloads, mappings and partner system changes.
   - Data migration: mapping changes, reruns and reconciliation.
   - Security and data protection: roles, field-level security, sharing; where personal data processing changes, refer to the DPO or legal adviser.
   - Reporting and analytics.
   - Testing: affected scripts, regression scope and retest of signed-off areas.
   - Training and communications.
   - Licensing and capacity: confirm with the Microsoft licensing guide or your partner.
   - Cost, timeline and dependencies on other workstreams.
3. Assess options. Offer alternatives where they exist, such as adopting standard behaviour, deferring to a later release, or a reduced version, applying the same hierarchy as `design-authority:customisation-challenge`.
4. Record findings with their classification.
   - Blocking: the change cannot proceed as proposed because it breaks the blueprint, a standard or a dependency, or because its impact is not yet understood (for example an affected integration owner has not been consulted).
   - Advisory: risks or costs the decision makers should weigh, which do not prevent approval.
5. Recommend. Approve, approve with conditions, defer or reject, with the assessment attached. The change board or steering committee decides; the design authority supplies the assessment.
6. Update the baseline. Once a change is approved, confirm that the affected artefacts are updated and the change is traceable from request to release.

Blocking findings are not overruled by the department under review, which includes the department that requested the change. If it disagrees, the matter escalates to the steering committee or executive sponsor, who may accept the risk explicitly and have it recorded.

Watch cumulative change. Many small approved changes can add up to a redesign that nobody ever reviewed as a whole.

## Outputs

- Impact assessment per change request, with findings classified as blocking or advisory.
- Recommendation for the change board.
- Updates to the `delivery-plan` and `raid-log` for approved changes.
- List of baseline artefacts to update, such as the `solution-blueprint`, `data-migration-mapping`, `integration-inventory`, `test-strategy-and-uat-scripts` and `training-and-communications-plan`.

## Scale notes

### SMB

The lead consultant plays this role and often assesses a change the same day, using the checklist as a quick scan. A short written assessment is enough for small changes, but the whole checklist still has to be walked; integrations and migration are the usual misses. For changes touching pro-code or integrations, a second-pair-of-eyes review from someone outside the delivery is worth arranging.

### Enterprise

Change requests go through formal change control with a change board, impact input from each affected workstream consolidated by the design authority, and thresholds that decide which changes need steering committee approval. Track cumulative change across the programme and report it at each governance cycle.

## Hand-offs

- Approved changes return to the requesting department and update `programme-management:delivery-plan` and `programme-management:raid-log`.
- `testing-quality:test-strategy` adjusts regression and retest scope.
- `change-adoption:communications-plan` updates what users are told.
- Changes with security impact also need `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Size a change on build effort alone.
- Make the approval decision on behalf of the change board or steering committee.
- Let the requesting department overrule a blocking finding.
- Assess a change during UAT or cutover without considering retest and rollback impact.
