---
name: test-strategy
description: Sets the overall test approach for a Dynamics 365 CE programme, covering test levels, environments, test data, defect handling and traceability. Use when planning which test phases a project needs, who runs them and where, or agreeing entry and exit criteria before build starts.
license: CC-BY-4.0
metadata:
  department: testing-quality
  stages: Initiate, Implement
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Test strategy

Testing on a CRM project is usually planned late and squeezed hardest, because build overruns eat into the weeks set aside for SIT and UAT. The consequences are predictable: business users find configuration defects that a functional test should have caught, integration faults surface in front of the business, and nobody can say with confidence which requirements have actually been proved.

A test strategy prevents this by deciding early which test levels the project needs, who runs each one, where they run, with what data, and what evidence closes each phase. On Dynamics 365 CE it also has to plan for a platform that keeps changing after go-live, so the strategy should outlive the project.

## When to use

- At Initiate, when the delivery plan needs test phases, durations and environments.
- When a statement of work or partner proposal must say who tests what.
- When test environments, test data or defect tooling have not been agreed.
- When scope, modules or integrations change enough that the existing strategy no longer fits.

Not this skill: `testing-quality:system-integration-testing` for running integration cycles, `testing-quality:user-acceptance-testing` for business acceptance, `business-analysis:acceptance-criteria` for writing the criteria that tests prove, and `platform-administration:environment-setup` for provisioning environments.

## Questions to ask first

1. Which modules, integrations and migrated data sets are in scope? Each one adds test levels or cycles, and integrations drive most of the SIT effort.
2. Who will test, and how much of their time is declared as available? Business testers with no backfill are the most common reason UAT slips.
3. How many non-production environments exist or are planned? Sharing one environment between SIT and UAT forces the phases to run in series.
4. May production or legacy personal data be used for testing? This is a data-protection decision; take it to the organisation's DPO or legal adviser before planning test data.
5. Is a defect and test management tool already in use? Reusing a tool the organisation knows (Azure DevOps, Jira) beats introducing a new one mid-project.

## Approach

Write the strategy as a short, decision-heavy document, not a testing textbook. Every section should answer who, where, with what, and how we know it is done.

1. Define the test levels. For Dynamics 365 CE the useful set is: unit tests for pro-code (plug-ins, custom APIs, PCF controls) written by developers; functional tests of configured features against user stories, run by consultants or testers; system integration testing across interfaces and cross-module flows; user acceptance testing by business users; performance testing where volume or concurrency is a risk; and regression testing, automated where it pays back. Drop levels that do not apply, but say so explicitly.
2. Map levels to environments. A typical pattern is development, a test or SIT environment deployed from the pipeline with managed solutions, a UAT environment that mirrors production security and data shape, then production. Note where connected services (Customer Insights - Journeys, Dynamics 365 Contact Center channels, Field Service Mobile) need their own setup per environment, because these are often forgotten until UAT.
3. Plan test data. Decide per level whether data is synthetic, masked, or loaded through the migration tooling. Using mock migration output in UAT lets business users test against data that looks like theirs and tests the migration at the same time.
4. Set entry and exit criteria per level. Entry criteria stop a phase starting on an unready build. Exit criteria are written in terms of scripts executed, requirements covered and open defects by severity, never elapsed time.
5. Agree defect management. One tool, one severity scale used by every phase, a named triage owner and a turnaround expectation per severity. Agreeing severities here means SIT, UAT and hypercare speak the same language.
6. Build traceability. Each user story links to acceptance criteria, each criterion to at least one test, and each test to its results. This lets a go/no-go board see coverage rather than opinion.
7. Plan for life after go-live. Name the regression pack, its owner, and how it will run against each Microsoft release wave.

Test with real security roles from the functional level onwards. Testing as System Administrator hides most of the defects users will hit on the first day.

## Outputs

- Test strategy section of `test-strategy-and-uat-scripts`, covering levels, environments, data, criteria and defect process.
- Test phase timeline feeding the `delivery-plan`.
- Environment-to-phase map aligned with the `environment-and-alm-strategy`.
- Defect severity definitions shared by SIT, UAT and hypercare.
- Requirements-to-test traceability matrix.
- Testing risks (tester availability, environment readiness, test data approval) raised in the `raid-log`.

## Scale notes

### SMB

The lead consultant usually writes a strategy of a few pages and runs functional testing personally. SIT and UAT can share an environment if budget demands it, but keep at least one environment separate from development. Do not skip UAT entry and exit criteria or testing with real security roles; both are cheap and catch the defects that damage go-live.

### Enterprise

A test manager owns the strategy, with test leads per workstream and a central defect triage board. Expect several SIT cycles, a dedicated performance test, automated regression in the pipeline and formal phase sign-offs kept for audit. Coordinate test data across modules so that a case in Customer Service and a work order in Field Service refer to the same accounts and assets.

## Hand-offs

- `testing-quality:system-integration-testing`, `testing-quality:user-acceptance-testing`, `testing-quality:performance-testing` and `testing-quality:regression-automation` pick up each level.
- `platform-administration:environment-setup` provisions the environments the strategy names.
- `integration-and-data:mock-migrations` supplies migrated test data.
- `design-authority:design-review` confirms the strategy covers the architecture's risk points (integrations, pro-code, high-volume processes).

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Plan UAT as the first time business processes are tested end to end.
- Copy production personal data into test environments without a decision from the DPO or legal adviser.
- Close a test phase on its calendar date when its exit criteria are not met.
- Test only as System Administrator.
