---
name: scheduling-optimisation
description: Decides whether and how to automate Field Service scheduling with Resource Scheduling Optimization or newer AI scheduling capabilities, covering readiness, scope, goals, constraints and objectives, operating rhythm and rollout. Use when manual dispatch no longer scales, travel time is too high, or automated scheduling is proposed.
metadata:
  department: field-service
  stages: Strategize, Implement, Operate
  modules: Field Service
  status: draft
---

# Scheduling optimisation

Automated scheduling promises less travel, more jobs per day and dispatchers freed from building routes by hand. It also amplifies whatever is wrong with the data: wrong durations, missing locations and over-specified skills produce confident, unworkable schedules at machine speed.

Projects usually go wrong by buying optimisation before manual scheduling is stable and measured, by trying to optimise every territory and every rule at once, and by leaving dispatchers out of the design. When dispatchers do not trust the output, they quietly override it and the investment delivers nothing.

## When to use

- Deciding whether automated scheduling is worth it, and when.
- Choosing between Resource Scheduling Optimization and newer Microsoft scheduling capabilities.
- Designing optimisation scope, goals, constraints and objectives.
- Planning pilot, parallel running and rollout.
- Diagnosing poor or distrusted optimisation results.

Not this skill: `field-service:schedule-board-setup` for resources, territories and manual dispatch, `field-service:incident-types-and-service-tasks` for job durations and required skills, `platform-administration:licensing-and-capacity` for licence management.

## Questions to ask first

1. Is manual scheduling really the bottleneck? If durations or data are wrong, optimisation will not fix the problem.
2. Are durations, locations, working hours and characteristics accurate? The optimiser trusts every input it is given.
3. What should the schedule favour: travel, utilisation, priority, promised windows or continuity with a preferred technician? These become the goal's objectives.
4. When should schedules be fixed: overnight for the coming days, or continuously through the day? This decides run timing and booking locks.
5. Which engine and licence are in play? Options and packaging change, so confirm with the Microsoft licensing guide or your partner.

## Approach

Resource Scheduling Optimization has long been the Microsoft add-in for automated Field Service scheduling, and Microsoft has also been introducing Copilot and agent-based scheduling assistance. Names, capabilities and availability in this area change, so check current Microsoft Learn documentation for what exists today and which option fits. The method below applies whichever engine you choose.

1. Prove the manual baseline. Run manual scheduling with the schedule assistant for a period and measure travel time, jobs per resource per day, first-time fix and adherence to promised windows. Without a baseline nobody can show the optimiser helped.

2. Fix the inputs. Validate durations against actual bookings, geocode every service account and resource start location, confirm working hours and time off, and check required characteristics against declared resource skills.

3. Define a narrow first scope. Start with one territory or service line with enough volume to matter and dispatchers willing to pilot. Decide which resources, requirements and time horizon are in scope.

4. Express goals as constraints and objectives. Constraints are rules every schedule must respect, such as matching skills, working hours, territory and time windows. Objectives are what to maximise or minimise, such as travel time, working hours used or high-priority work served. Keep the first goal simple and add constraints only when a real scheduling error proves the need.

5. Decide the operating rhythm. Choose when runs happen, which bookings are locked, how emergencies are inserted and what dispatchers may override. Record overrides so they can inform tuning.

6. Run in parallel before trusting. Compare optimiser output with dispatcher schedules for the pilot scope, review differences with dispatchers, and tune. Publish automatically only when dispatchers agree the output is workable.

7. Scale and monitor. Extend scope territory by territory, watch run outcomes and unscheduled requirements, and keep a named owner for goals and scope.

Dispatchers move from building schedules to managing exceptions, which is a real role change. Involve them from the start and plan the change with `change-adoption:role-based-training`.

## Outputs

- Business case and baseline measures linked to the `project-charter` success measures.
- Input data quality report covering durations, locations, hours and characteristics.
- Optimisation scope and goal design in the `solution-blueprint`.
- Pilot and rollout plan in the `delivery-plan`.
- Parallel run comparison and tuning log.
- Dispatcher role change content in the `training-and-communications-plan`.

## Scale notes

### SMB

Often not needed yet: a single dispatcher with the schedule assistant handles modest volumes well. If adopted, use one scope and one simple goal. Do not skip the baseline or the clean-up of inputs.

### Enterprise

Expect several scopes with regional goals, integration with workforce management, attention to run duration and timing, and goal changes governed like any other production change. Where optimisation changes working patterns, involve HR and, where required, employee representatives early. If an AI scheduling capability is used, put it through responsible AI review.

## Hand-offs

- `field-service:schedule-board-setup` keeps the resource data the optimiser depends on.
- `platform-administration:licensing-and-capacity` tracks entitlement to the chosen engine; for the licence itself, confirm with the Microsoft licensing guide or your partner.
- `data-and-ai:responsible-ai-review` for any AI-based scheduling capability.
- Reviewer sign-off: `design-authority:design-review` for the optimisation design, and `design-authority:change-impact-assessment` for changes to live goals or scope.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Switch on automated scheduling before durations, locations and working hours are validated.
- Optimise every territory at once on the first run.
- Publish optimiser schedules automatically before a parallel run with dispatchers.
- Use optimisation results to rank individual technicians.
- Assume a scheduling capability is available in your region or covered by your licence; check current Microsoft Learn documentation, and for licensing confirm with the Microsoft licensing guide or your partner.
