---
name: regression-automation
description: Builds and maintains a risk-based automated regression pack for Dynamics 365 CE so that release waves, service updates and project releases do not silently break working processes. Use when choosing test automation tooling, deciding what to automate, adding tests to pipelines, or testing in an early access sandbox.
metadata:
  department: testing-quality
  stages: Implement, Prepare, Operate
  modules: All
  status: draft
---

# Regression automation

Dynamics 365 CE changes continuously, with two major release waves a year and smaller service updates in between, while the project keeps shipping its own changes. Without a regression pack, every update becomes a manual retest that nobody has time for, so teams quietly stop testing and hear about breakages from users. Automation is the way out, but most teams over-reach: they try to automate everything through the user interface, tests break with every form change, and the pack is abandoned within months.

A sustainable regression pack is small, chosen by risk, owned by a named team and run on a schedule that matches Microsoft's release rhythm.

## When to use

- Choosing an automation approach for model-driven apps and Dataverse.
- Deciding which processes belong in the regression pack.
- Planning tests in an early access sandbox ahead of a release wave.
- Connecting automated tests to the deployment pipeline.
- Rescuing a regression pack that has become flaky or unmaintained.

Not this skill: `platform-administration:release-readiness` for planning the organisation's overall response to a release wave, `platform-engineering:deployment-pipelines` for building the pipeline itself, and `testing-quality:test-strategy` for deciding the overall test levels.

## Questions to ask first

1. Which processes would hurt most if they broke silently? Business risk, not ease of automation, decides what goes in the pack.
2. Who will maintain the tests after go-live, and what skills do they declare? A pack that only a developer can update will decay if the support team has none.
3. Is there a pipeline and a test environment whose data can be reset? Automated tests need known, stable data to give repeatable results.
4. What web test automation does the organisation already use? Building on existing skills and tooling beats adopting a new framework.

## Approach

1. Choose tooling with current information. The options have shifted over the years: EasyRepro (a Selenium-based library aimed at model-driven apps), Playwright-based frameworks built by the project team, and Power Apps Test Engine, among others. Check current Microsoft Learn documentation and each project's repository for status and support before committing, because the recommended path changes.
2. Automate in layers. Put business logic, plug-ins and custom APIs under API-level tests against Dataverse where you can; they are faster and far less brittle than UI tests. Reserve UI tests for a small set of end-to-end journeys per role, such as qualifying a lead, resolving a case, or scheduling and completing a work order.
3. Select by risk. Start with the few journeys whose failure would stop the business, plus the areas most exposed to platform change (heavily scripted forms, custom controls, integrations). Add tests when a defect escapes, not because a screen exists.
4. Design for stability. Use stable selectors and the framework's model-driven abstractions rather than screen positions. Create test data in setup and remove it afterwards. Keep credentials in a secret store, never in test code. Run under test accounts that hold the same security roles as real users; check whether these accounts need licences and confirm with the Microsoft licensing guide or your partner.
5. Wire into the pipeline. Run the pack after each deployment to the test environment and on a schedule against a production-like sandbox, and publish results where the team actually looks.
6. Use the early access window. When early access for a release wave opens, copy a sandbox, enable the updates there and run the pack. Sort failures into test fixes and genuine regressions, and raise genuine regressions with Microsoft through a support case while there is still time before the update reaches production.
7. Maintain continuously. Any change that alters a form, process or role updates the affected tests in the same piece of work. Retire tests that no longer protect anything.

Flaky tests are worse than no tests, because they teach the team to ignore failures. Quarantine and fix them quickly.

## Outputs

- Regression scope with risk rationale, recorded in `test-strategy-and-uat-scripts`.
- Automated test suite in source control alongside the solutions.
- Pipeline test stage, documented in the `environment-and-alm-strategy`.
- Release wave test report for each early access cycle.
- Maintenance ownership recorded in the support model.

## Scale notes

### SMB

A full automation framework may be more than the team can maintain. A short manual regression checklist run in an early access sandbox, plus a few automated journeys if someone can maintain them, is a reasonable start. What must not be skipped is checking each release wave in a sandbox before it reaches production.

### Enterprise

Expect a test automation engineer or team, packs per module plus cross-module journeys, scheduled runs in several environments, and results feeding release governance. Each workstream owns the tests for its area, and regression results form part of the evidence for every release decision.

## Hand-offs

- `platform-engineering:deployment-pipelines` adds the automated test stage.
- `platform-administration:release-readiness` uses release wave test results to plan updates.
- `support-operations:continuous-improvement` owns pack maintenance after go-live.
- `design-authority:standards-conformance` checks that automated regression is part of the agreed ALM standard; no separate reviewer sign-off is needed for the pack itself.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Automate everything through the user interface.
- Store test account passwords in test code or pipeline definitions.
- Wait for a release wave to arrive in production before running regression against it.
- Keep flaky tests in the pack without investigating them.
