---
name: incident-types-and-service-tasks
description: Designs Field Service incident types as reusable job templates, with service tasks, inspections, products, services, required characteristics, estimated durations and resolutions. Use when standardising what technicians do for each kind of job, building the incident type catalogue, or setting realistic job durations.
metadata:
  department: field-service
  stages: Initiate, Implement, Operate
  modules: Field Service
  status: draft
---

# Incident types and service tasks

Incident types are where Field Service turns the knowledge in experienced technicians' heads into a repeatable job definition. When a work order receives an incident type, its tasks, parts, labour, skills and duration flow onto the job, so the quality of the catalogue sets the quality of scheduling, execution and billing.

Projects usually go wrong at the extremes. Some build an incident type per symptom and end up with a catalogue nobody can navigate; others build one generic type and lose the benefit entirely. Durations are guessed, inspections turn into long forms nobody can complete on a phone, and products on incident types drift away from the real product catalogue.

## When to use

- Designing the incident type catalogue and its granularity.
- Defining service tasks, task types and inspections.
- Attaching products, services and required characteristics to incident types.
- Setting and recalibrating estimated durations.
- Defining resolution codes for first-time-fix and repeat-visit reporting.

Not this skill: `field-service:work-order-design` for the work order lifecycle and types, `field-service:schedule-board-setup` for maintaining resources and their characteristics, `field-service:agreements-and-recurring-work` for recurring maintenance visits.

## Questions to ask first

1. What are the recurring kinds of job, and how do they differ in tasks, skills and parts? This sets the catalogue's granularity.
2. Are actual job durations known from history? Durations drive scheduling quality more than any other single input.
3. Which jobs need structured evidence such as readings, pass or fail checks, photos or signatures? This decides where inspections are needed.
4. Is the product and service catalogue clean, and who owns it? Incident types can only reference what the catalogue holds.
5. Do jobs vary by asset category or region? This decides whether incident types are generic or specialised.

## Approach

An incident type bundles the default content of a job: service tasks, products, services, required characteristics, estimated duration and possible resolutions. The design aim is a catalogue that covers most job volume with a manageable number of well-maintained types.

1. Set the granularity. Aim for one incident type per distinct job method, not per symptom or customer. A useful test is whether a technician would do materially different work, need different skills or take a different time. If not, it is the same incident type with different notes.

2. Write service tasks as steps a technician confirms. Keep task names short and verifiable. Use service task types with inspections where structured evidence matters, and keep inspections short enough to complete on a phone on site. Check current Microsoft Learn documentation for inspection capabilities and how responses are stored for reporting.

3. Attach products and services from a clean catalogue. Products on incident types are the parts usually needed, held as estimates until used; services represent labour or fees for billing. Agree with `field-service:inventory-and-purchasing` how products are classified before loading.

4. Set required characteristics deliberately. Characteristics on an incident type become requirements used by scheduling. Use only skills and certifications that resources hold in their declared profiles; an over-specified requirement leaves jobs unschedulable.

5. Estimate durations from evidence. Use historical job times where available, agree defaults with field supervisors, and plan to recalibrate after go-live from actual booking durations. Duration errors compound across a day's route.

6. Define resolutions. A short list of resolution codes per incident type makes first-time-fix and repeat-visit reporting possible.

7. Govern the catalogue. Name an owner, usually a service operations or technical lead, with a change process and a review after the first months of live use. Load incident types as configuration data by a repeatable method so test and production stay aligned.

## Outputs

- Incident type catalogue covering tasks, inspections, products, services, characteristics, durations and resolutions.
- Inspection templates for jobs that need structured evidence.
- Configuration data deployment approach in the `environment-and-alm-strategy`.
- Duration baseline and recalibration plan.
- Technician task guidance in the `training-and-communications-plan`.

## Scale notes

### SMB

A handful of incident types usually covers most job volume, owned by the service manager or lead technician. Add inspections only where regulation or customers require evidence. Do not skip realistic durations or required characteristics, because scheduling depends on both.

### Enterprise

Expect a catalogue per service line with central standards, multiple languages, regulated inspection evidence and multi-resource jobs; check current Microsoft Learn documentation for how incident types express multi-resource requirements. Treat the catalogue as configuration data moved through pipelines, and review durations regularly using actual booking data.

## Hand-offs

- `field-service:work-order-design` applies incident types to the work order lifecycle.
- `field-service:schedule-board-setup` aligns characteristics with resource profiles.
- `platform-engineering:deployment-pipelines` moves incident type configuration data between environments.
- Reviewer sign-off: `design-authority:standards-conformance` for catalogue standards, and `security-compliance:data-retention` where inspection evidence must be retained for regulatory reasons.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create an incident type per symptom, customer or technician.
- Set required characteristics that no available resource holds.
- Leave estimated durations as guesses with no plan to recalibrate them from actual bookings.
- Hand-key incident types separately in each environment.
