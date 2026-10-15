---
name: schedule-board-setup
description: Sets up Field Service resources and the schedule board, covering bookable resource types, characteristics, roles, territories, working hours, start locations, requirements, board tabs and the schedule assistant. Use when onboarding technicians as resources, designing territories, or configuring how dispatchers schedule and reschedule jobs.
license: CC-BY-4.0
metadata:
  department: field-service
  stages: Implement, Prepare, Operate
  modules: Field Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Schedule board setup

Dispatchers live in the schedule board, and technicians feel every decision made there. The board can only be as good as the resource data underneath it: a technician without working hours, a start location or the right characteristics is invisible or wrongly offered, however well the board is configured.

Projects usually go wrong by configuring board tabs before the resource data is complete, by copying sales territories into dispatch, and by building one enormous board that every dispatcher filters differently. Contractors, crews and equipment are often an afterthought, then forced into the wrong resource type late in testing.

## When to use

- Modelling technicians, contractors, crews, equipment and facilities as bookable resources.
- Designing territories and assigning resources and service accounts to them.
- Setting working hours, time off, time zones and start locations.
- Configuring board tabs, filters and views for each dispatcher.
- Teaching dispatchers to use the schedule assistant and rehearsing a dispatch day.

Not this skill: `field-service:scheduling-optimisation` for automated scheduling, `field-service:incident-types-and-service-tasks` for what each job requires, `security-compliance:business-units-and-teams` for record access by region.

## Questions to ask first

1. Who and what is scheduled: employees, contractors, crews, equipment or facilities? Each maps to a different resource type with different behaviour.
2. How is the patch divided, and does each dispatcher own an area? This shapes territories and board tabs.
3. Where do technicians start and end their day? Start locations drive travel time and every availability calculation.
4. Which skills and certifications must match, and who maintains them? Characteristics are only as reliable as their owner.
5. How far ahead and how do dispatchers schedule today? This decides how much to lean on the schedule assistant and whether optimisation follows.

## Approach

Before configuring a single board tab, make sure every bookable resource has the right type, working hours, time zone, start and end location, territory, roles and characteristics. Board configuration is quick; resource data is where the effort goes.

1. Model resources by type. Employees are usually user resources; contractors may be set up differently depending on whether they use the app; crews group resources that travel together; equipment and facilities are booked where they constrain the job. Check current Microsoft Learn documentation for how each type behaves with the mobile app, and for which licences each type needs, confirm with the Microsoft licensing guide or your partner.

2. Maintain characteristics as declared skills. Characteristics and their rating values record certifications and proficiency a resource holds, maintained by a named owner from training and certification records. They are not performance scores and must not be used as such.

3. Design territories for dispatch. Territories should reflect how work is dispatched and travelled, not how sales are organised. Assign resources and service accounts to them, and decide whether resources may work across territories.

4. Set working hours and locations. Working hours, breaks, time off and start locations drive availability and travel time. Agree who maintains time off and how. If a start location is a technician's home address, treat it as personal data and limit who can see it.

5. Configure the board per dispatcher. Create tabs by territory or service line with the filters, views and requirement lists each dispatcher needs. Keep shared tabs under control so one person's changes do not break another's. Check current Microsoft Learn documentation for board settings in your release.

6. Use the schedule assistant. Teach dispatchers to search for availability from the requirement, which respects characteristics, territory, working hours and travel, rather than dragging blindly onto the board. This habit is also the foundation for `field-service:scheduling-optimisation`.

7. Load resources repeatably. Resources, characteristics, territories and working hours are reference data; load them by template or script and reconcile before go-live.

8. Rehearse a dispatch day. With production-like resource data, have dispatchers schedule a realistic day, including emergencies, cancellations and sickness, before go-live.

## Outputs

- Resource model and territory design in the `solution-blueprint`.
- Resource, characteristic and working hours load in the `data-migration-mapping`.
- Board tab configuration for each dispatcher role.
- Dispatch day rehearsal scripts in `test-strategy-and-uat-scripts`.
- Dispatcher training in the `training-and-communications-plan`.

## Scale notes

### SMB

One dispatcher, one board and perhaps no territories at all. Manual scheduling with the schedule assistant is usually enough. Do not skip working hours, time zones, start locations and characteristics for every resource.

### Enterprise

Expect several dispatch centres, contractors, crews and working time rules that may be set by agreements or law; take questions on those rules to the organisation's legal adviser. Resource data often comes from an HR system through integration, territories form a hierarchy, and board configuration needs an owner and change control.

## Hand-offs

- `field-service:scheduling-optimisation` once manual scheduling is stable and measured.
- `field-service:mobile-and-offline` for what technicians see of their bookings.
- `integration-and-data:integration-architecture` where resource and time-off data come from HR systems.
- Reviewer sign-off: `security-compliance:security-model-review` for access to resource personal data such as home start locations, and `security-compliance:business-units-and-teams` for regional visibility.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use characteristic ratings to score or rank technicians' performance.
- Copy sales territories into Field Service without checking they suit dispatch.
- Go live with resources missing working hours, time zones or start locations.
- Expose technicians' home addresses beyond the people who need them for dispatch.
