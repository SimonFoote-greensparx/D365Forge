---
name: performance-testing
description: Plans and runs performance testing of Dynamics 365 CE forms, plug-ins, integrations and concurrent users against realistic data volumes and agreed targets. Use when deciding whether a performance test is needed, defining load scenarios and response targets, choosing tools, or chasing slow forms and timeouts before go-live.
license: CC-BY-4.0
metadata:
  department: testing-quality
  stages: Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Performance testing

Performance problems in Dynamics 365 CE rarely come from the platform alone. They come from what the project added: forms with many fields, tabs and subgrids loading at once, synchronous plug-ins chaining into each other, flows firing on every update, and integrations that call the API one record at a time. None of this shows in a development environment with a few hundred records and one user, and all of it shows at go-live when the full data set and the full user base arrive together.

Performance testing is the cheapest place to find these problems, but only if the test environment holds realistic data volumes and the scenarios reflect real peaks.

## When to use

- Deciding whether the project needs a formal performance test or targeted checks.
- Defining scenarios, user loads and response targets.
- Testing integrations with high volumes or tight timing.
- Investigating slow forms, timeouts or throttling seen in SIT or UAT.

Not this skill: `solution-architecture:performance-by-design` for designing for performance up front, `platform-administration:monitoring` for production telemetry, and `platform-administration:licensing-and-capacity` for API entitlements and storage capacity.

## Questions to ask first

1. What are the peaks? A contact centre on Monday morning, technicians syncing at shift start, a large marketing send and a nightly ERP batch each need a different test.
2. How many users are concurrent at peak, by role? Concurrency per role shapes the load model far more than the total number of named users.
3. What data volume will exist at go-live and after a year of use? A test against a near-empty database proves very little.
4. Which interfaces carry high volumes or time-critical messages? Batch windows and API throttling are common failure points.
5. Has the business agreed response targets? Without targets, results cannot pass or fail.

## Approach

1. Scope by risk. Not every project needs a full load test. A single-module deployment with mostly standard forms may need only targeted checks of the heaviest forms and interfaces. High concurrency, heavy pro-code, large data volumes or time-critical integrations justify a planned performance test.
2. Prepare the environment. Use a sandbox with production-like volume, ideally loaded by a mock migration, carrying the same solutions, security roles and integrations as production. If that volume is a copy of real personal data, the DPO or legal adviser decision from the test strategy applies. Sandbox behaviour can differ from production, so check current Microsoft Learn documentation and treat results as strong indicators rather than guarantees.
3. Test forms one at a time first. Measure load times for the main forms per role with browser developer tools and the Monitor tool in Power Apps. Count controls, tabs, subgrids, web resources and on-load scripts; slow forms are almost always overloaded forms.
4. Test server-side logic. Exercise plug-ins and synchronous automation with realistic payloads, reading the plug-in trace log for execution times. Look for synchronous chains, unfiltered queries, and logic that fires on every field change rather than the fields that matter.
5. Test integrations under volume. Run batch interfaces at expected peak plus headroom and watch for service protection limits and throttling responses. Confirm the integration honours retry-after responses and batches requests where sensible. API entitlements depend on licences; confirm with the Microsoft licensing guide or your partner.
6. Test concurrency. Use a load tool (JMeter-based scripts or Azure Load Testing are common choices; check current tooling) to simulate concurrent users per role running their main journeys, ramping up to the agreed peak. Check current Microsoft guidance on load testing Dataverse environments before running large tests.
7. Report and remediate. Compare results with targets, rank the worst offenders, fix, and retest. Keep the final figures as a baseline that production monitoring can compare against.

## Outputs

- Performance test plan and results within `test-strategy-and-uat-scripts`.
- Load model by role and peak scenario.
- Form, plug-in and interface findings with remediation owners.
- Baseline figures handed to production monitoring.
- Performance risks recorded in the `raid-log`.

## Scale notes

### SMB

A formal load test is often unnecessary. Do check the main forms per role with realistic data, review plug-ins and flows for synchronous chains, and run any bulk integration at full volume. The consultant can do this in a few days; skipping it entirely is the mistake.

### Enterprise

Expect a performance test lead, a dedicated environment, scripted load tests per module and joint tests with middleware and partner systems. Performance targets become SIT exit criteria or a separate gate before go-live, and results feed capacity planning.

## Hand-offs

- `solution-architecture:performance-by-design` for design changes; `platform-engineering:plugin-design` and `platform-engineering:power-automate-patterns` for code and flow fixes.
- `integration-and-data:integration-architecture` for interface redesign.
- `platform-administration:monitoring` takes the baseline into production alerting.
- `programme-management:go-no-go` receives the results; remediation that changes signed-off design needs `design-authority:change-impact-assessment`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Run load tests against production.
- Declare performance acceptable from a test against a near-empty environment.
- Report pass or fail without response targets agreed with the business.
- Hide slow processing by raising timeouts instead of removing the load.
