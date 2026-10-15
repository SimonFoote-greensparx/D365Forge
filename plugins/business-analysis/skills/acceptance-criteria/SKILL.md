---
name: acceptance-criteria
description: Writes testable acceptance criteria for Dynamics 365 CE user stories in Given/When/Then form, covering security roles, starting data, negative paths and automation outcomes, and links each criterion to test cases. Use when a story lacks criteria, when UAT scripts must be derived from stories, or when story-level acceptance is disputed.
license: CC-BY-4.0
metadata:
  department: business-analysis
  stages: Initiate, Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Acceptance criteria

Acceptance criteria are the agreement between the business and the build team at story level, and the bridge from the backlog into SIT and UAT. When they are precise, the developer knows when to stop, the tester knows what to check, and the product owner can accept without a meeting.

On Dynamics 365 projects criteria most often fail on security and data. A story is demonstrated by a consultant with system administrator rights against hand-picked records, it passes, and then it fails in UAT for a real agent in a real business unit. Other common faults are criteria that simply restate the story, criteria that cover only the happy path, and vague words such as quick or intuitive that nobody can test.

## When to use

- During refinement, before a story is accepted as ready for a sprint.
- When deriving SIT and UAT scripts from the backlog.
- When the business and build team disagree about whether a story is done.
- When automation, integration or security behaviour needs a precise, testable statement.

Not this skill: `business-analysis:user-stories` for writing and splitting the story itself, `testing-quality:user-acceptance-testing` for planning and running UAT, `programme-management:statement-of-work` for contractual acceptance of partner deliverables.

## Questions to ask first

1. Which security role performs the action, in which business unit? Access is where Dynamics 365 criteria fail most often.
2. What state is the data in before the action? Record status, ownership and related records change the outcome.
3. What are the exception and negative paths? Validation, duplicates and missing access are where defects hide.
4. Is there a measurable non-functional expectation, and where is it agreed? Thresholds must come from agreed requirements, not from the analyst.
5. How will the criterion be tested, manually or by automated regression? Criteria intended for automation need stable, explicit data.

## Approach

Write each criterion as a short scenario. Given sets the role and starting data. When is a single action or event. Then states the observable outcome, including anything that must not happen.

A service example:

- Given a user in the service agent security role, and a case for an account with an active entitlement
- When the agent sets the case priority to high and saves
- Then the service level from the entitlement is applied and the first response timer shows on the case

A negative example: given a user in the sales security role with no service access, when they open the same case, then they can read it but cannot edit it.

Working rules that keep criteria testable:

1. Keep to a handful of scenarios per story. If a story needs many more, split the story.
2. Test one behaviour per scenario.
3. Include at least one negative path for access, validation or duplicate handling.
4. Name the security role and business unit; never use a system administrator as the actor.
5. Specify the data, and list the sample records in the test data set.
6. Use measurable terms only. Take any performance threshold from the agreed non-functional requirements.
7. State automation outcomes explicitly: which flow runs, which records are created or updated, which email or notification is sent, and which integration message is produced.
8. For Field Service Mobile, state the connectivity condition, because online and offline behaviour can differ.
9. Give each criterion an identifier and link it to its test case. UAT scripts then combine criteria into end-to-end scenarios that follow the future-state process maps.

Review criteria in refinement with three perspectives present: the product owner for business meaning, a tester for testability, and a builder for feasibility.

## Outputs

- Given/When/Then criteria on each story, including negative and security scenarios.
- Criterion-to-test links in the traceability matrix.
- Test data requirements for each scenario.
- Inputs to the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

The consultant and business owner write criteria together during refinement. They can be brief, but role, starting data and one negative path are always required. UAT scripts can often be assembled directly from the criteria.

### Enterprise

The test lead reviews criteria before a story is marked ready, and candidates for regression automation are tagged. Criteria for shared components, such as account and contact behaviour, are agreed across workstreams. Traceability from criterion to test result is kept for audit.

## Hand-offs

- `testing-quality:system-integration-testing` and `testing-quality:user-acceptance-testing` build scripts from the criteria.
- `testing-quality:regression-automation` takes the tagged scenarios.
- Reviewer sign-off: criteria involving column-level access or sharing are checked by `security-compliance:field-level-security` or `security-compliance:security-model-review`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Write criteria that can only pass when tested as a system administrator.
- Use unmeasurable words such as fast, easy or intuitive as a pass condition.
- Invent performance thresholds instead of taking them from agreed non-functional requirements.
- Accept a story with only happy-path criteria.
