---
name: mobile-and-offline
description: Designs the Field Service Mobile experience for technicians, covering mobile forms and navigation, offline profiles and sync scope, media capture, device security, and testing in poor connectivity. Use when configuring the technician app, deciding what data works offline, or diagnosing slow sync and missing records in the field.
license: CC-BY-4.0
metadata:
  department: field-service
  stages: Implement, Prepare, Operate
  modules: Field Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Mobile and offline

For technicians, the mobile app is the whole project. If it is slow to sync, cluttered with desktop fields or missing the asset history they need in a plant room with no signal, they will go back to paper and phone calls, and every downstream benefit disappears.

Projects usually go wrong by putting desktop forms on a phone, by scoping offline data too widely (first sync takes an age and background sync drains batteries) or too narrowly (records missing on site), and by testing only on office Wi-Fi. Device management and lost-device procedures are often left until a security review asks for them.

## When to use

- Designing mobile forms, views and navigation around the technician's day.
- Defining the mobile offline profile, sync filters and media handling.
- Making customisations work offline or degrade safely.
- Agreeing device ownership, management and security.
- Planning field pilots and connectivity testing, or diagnosing sync problems.

Not this skill: `field-service:work-order-design` for the work order lifecycle itself, `platform-engineering:pcf-controls` for building custom controls, `change-adoption:role-based-training` for technician training.

## Questions to ask first

1. Where do technicians work, and how reliable is connectivity there? This decides how far the design must assume offline working.
2. Which devices are used, who owns them, and are they managed? This drives security, deployment and lost-device handling.
3. What does a technician need on site: job history, asset details, knowledge, parts? This sets the offline scope.
4. What must be captured: photos, signatures, readings, time? Media volume is often the biggest sync load.
5. Do contractors or partner technicians use the app? This affects security and licences; confirm with the Microsoft licensing guide or your partner.

## Approach

Field Service Mobile runs on the Power Apps mobile platform, with offline capability governed by a mobile offline profile that defines which tables and rows are downloaded to the device. The design work is deciding what a technician genuinely needs, making it usable on a phone, and proving it in the places technicians actually work. Check current Microsoft Learn documentation for current offline behaviour and limits before finalising.

1. Design for the job, not the record. Start from the technician's day: see bookings, travel, start work, complete tasks and inspections, record parts and time, capture a signature, finish. Build mobile-specific forms and views with only what each step needs, and keep key actions easy to reach one-handed.

2. Scope offline data tightly. Start from the default Field Service offline profile and adjust it. Include the technician's own bookings and related work orders, customer assets, service tasks, products they may use and recent history for the sites they visit. Filter bookings to a short window around today, and avoid downloading whole tables of accounts, products or articles. Every extra table and row lengthens sync.

3. Plan media. Photos and signatures are often the largest data on the device. Decide image resolution, where files are stored and when they upload.

4. Handle customisations with care. Client scripts, custom controls and flows must work offline or degrade safely. Server-side logic such as plug-ins and real-time flows runs only after sync, so design validation that tolerates delay.

5. Secure the device. Agree device ownership, mobile device management, app protection policies and the lost-device procedure with `security-compliance:security-model-review`.

6. Test where technicians work. Measure first sync with realistic data volume, then work in aeroplane mode, weak signal and while switching networks. Include conflicts, such as a dispatcher changing a booking while the technician is offline. Use real devices, including the oldest supported model.

7. Pilot in the field. Run a pilot with a few technicians in different areas before rollout, fix friction quickly, and give technicians a clear support route for sync problems.

## Outputs

- Mobile form and navigation design.
- Offline profile specification with tables, filters and rationale in the `solution-blueprint`.
- Device and security standard.
- Connectivity and sync test scripts in `test-strategy-and-uat-scripts`.
- Technician quick guides in the `training-and-communications-plan`.
- Mobile support and sync troubleshooting steps in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Use the default offline profile with small adjustments and company-managed phones if possible. The consultant should spend a day in the field with a technician testing real jobs. Do not skip testing in poor connectivity or a lost-device procedure.

### Enterprise

Expect a managed device fleet, rollout waves by region, contractors, several languages and accessibility needs. Offline profiles may differ by role and need change control, sync performance needs monitoring, and app updates need a release process coordinated with device management.

## Hand-offs

- `field-service:incident-types-and-service-tasks` for the tasks and inspections technicians complete.
- `testing-quality:performance-testing` for sync volume and timing tests.
- `change-adoption:role-based-training` for technician training and floor support.
- Reviewer sign-off: `security-compliance:security-model-review` for device security and data held offline.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Put desktop forms on the mobile app unchanged.
- Download whole tables to devices in case they are needed.
- Sign off the app after testing only on office Wi-Fi.
- Rely on server-side logic for validation technicians need while offline.
- Allow unmanaged devices to hold customer data offline without security-compliance sign-off.
