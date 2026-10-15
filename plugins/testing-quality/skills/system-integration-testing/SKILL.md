---
name: system-integration-testing
description: Plans and runs system integration testing for Dynamics 365 CE, proving interfaces with ERP, telephony, email and other systems plus end-to-end flows that cross modules. Use when preparing SIT cycles, designing integration test scenarios, deciding on stubs and failure-path tests, or judging whether SIT can exit.
metadata:
  department: testing-quality
  stages: Implement, Prepare
  modules: All
  status: draft
---

# System integration testing

Integrations are where CRM projects lose the most time late in delivery. Each interface works in a developer's hands, then fails when real data, real volumes, real security and a real partner system meet in the same cycle. The classic mistake is treating SIT as one pass at the end of build, so integration defects appear in UAT in front of business users, or worse, at cutover.

SIT on Dynamics 365 CE has two jobs. It proves each interface against its specification, including the unhappy paths, and it proves the business flows that cross module and system boundaries, such as lead to order to invoice, or case to work order to billing.

## When to use

- Planning the number, length and content of SIT cycles.
- Turning the integration inventory into test scenarios.
- Deciding when to use stubs and when to wait for connected partner systems.
- Running defect triage that involves other system owners.
- Judging whether SIT exit criteria are met.

Not this skill: `integration-and-data:integration-architecture` for designing the interfaces, `integration-and-data:mock-migrations` for migration rehearsals, `testing-quality:performance-testing` for volume and concurrency, and `testing-quality:user-acceptance-testing` for business acceptance.

## Questions to ask first

1. Is the integration inventory complete, with direction, trigger, frequency and owner for every interface? SIT scenarios are derived from it, so gaps there become gaps in coverage.
2. Do partner systems have test environments that can be connected, and who owns them? Availability of the ERP or telephony test system often sets the SIT dates.
3. Which flows cross modules or systems end to end? These carry the highest business risk and need scenario tests, not only interface tests.
4. Is reference data (products, price lists, territories, resources, skills) aligned across systems in the SIT environment? Mismatched keys cause most first-cycle failures.

## Approach

1. Derive scenarios from the integration inventory and the process maps. For each interface, test the happy path, validation failures, duplicate messages, the partner system being unavailable, retries and replay, and record ownership conflicts (which system wins when both update the same field). Then layer end-to-end scenarios on top, following one business object through every system it touches.
2. Prepare an SIT environment deployed from the pipeline with managed solutions, never patched by hand. Connect it to partner test systems where they exist. Use stubs only where they do not, and record each stub as an untested risk with a date for closing it in a later cycle.
3. Align the data. Load reference data consistently across systems and agree a small set of named test accounts, contacts, products and assets that every team uses. Seed with mock migration output where the data-protection decision in the test strategy allows it.
4. Run in cycles. A first cycle proves connectivity and basic mapping, a second runs the full scenario set, and a third retests fixes and runs regression. Freeze configuration during a cycle except for agreed fixes, or results become impossible to interpret.
5. Check both ends. A test passes only when the record is right in Dataverse and in the partner system, and when the logs show what you expected. Read plug-in trace logs, flow run history and middleware logs, not just the screen.
6. Test security in the flow. Integration identities should run as application users with least-privilege roles. Test that an interface fails cleanly and visibly when a permission is missing, so production faults can be diagnosed quickly.
7. Triage jointly. During cycles, hold a daily defect call with every system owner present, because many integration defects live in the gap between teams.

Cross-module flows deserve particular attention when Sales, Customer Service and Field Service are built by different workstreams. Each team tests its own module, and nobody tests the handover between them unless SIT makes it explicit.

## Outputs

- SIT scenarios and scripts within `test-strategy-and-uat-scripts`.
- Interface-to-scenario coverage traced back to the `integration-inventory`.
- Stub register with closure dates.
- SIT cycle reports with defects by severity and by system.
- SIT exit report supporting the UAT entry decision.

## Scale notes

### SMB

Integrations are usually few (email, an accounting package, perhaps a telephony connector), so one full cycle followed by a retest is often enough. The consultant who built an integration should not be its only tester; borrow a second person for the end-to-end scenarios. Never drop the failure-path tests to save time.

### Enterprise

Expect an SIT lead, cycle plans agreed with each partner system owner, and environment bookings for systems shared with other programmes. Middleware, ERP and CRM workstreams each assign testers. Integration defects are triaged centrally with clear ownership, and SIT exit is a formal gate signed by the test manager.

## Hand-offs

- `testing-quality:user-acceptance-testing` starts when SIT exit criteria are met.
- `testing-quality:performance-testing` takes interfaces with volume or timing risk.
- Interface design defects return to `integration-and-data:integration-architecture`; data alignment issues go to `integration-and-data:data-mapping-and-cleansing`.
- Fixes that change a signed-off interface need `design-authority:change-impact-assessment`; integration identities and their roles are confirmed by `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Pass an interface test by checking only the Dynamics 365 side.
- Run SIT in an environment patched by hand instead of deployed from the pipeline.
- Use a System Administrator account as the integration identity to get tests passing.
- Leave stubs in place without recording the untested risk.
