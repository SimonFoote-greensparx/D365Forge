---
name: security-model-review
description: Reviews a Dataverse security model as an independent reviewer, covering security roles, privilege depth, teams, hierarchy security, record sharing and Entra ID access, and classifies every finding as blocking or advisory. Use when a role matrix needs sign-off, before UAT or go-live, or when users see records they should not.
license: CC-BY-4.0
metadata:
  department: security-compliance
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Security model review

Few CRM security failures are dramatic. Most are quiet: a seller who can read every account because someone widened read depth to make a lookup work, an integration account running as System Administrator, or a service team that shares records by hand until the sharing table slows every view. Each shortcut made sense under deadline pressure, and none was reviewed against the whole model.

This skill is the independent check on the model as designed and as deployed. It is reviewer-class: every finding is classified as blocking or advisory, and blocking findings are not overruled by the department under review. Disagreement escalates to the executive sponsor or steering committee, never back to the team that built the model.

## When to use

- A role matrix or persona design is ready for sign-off.
- Before UAT starts, and again as an input to the go-live decision.
- After go-live, when someone reports seeing records they should not (or missing records they need), or before a release adds a module.
- When an organisation inherits an environment and needs to know what access it actually grants.

Not this skill: `security-compliance:business-units-and-teams` to design the business unit tree and team types, `security-compliance:field-level-security` to protect individual columns, `platform-administration:environment-setup` to configure environments and admin settings.

## Questions to ask first

1. Which personas exist, and what must each read, create, change and delete? Without a persona-by-table view there is nothing to review against.
2. Which data is personal, special category or commercially restricted? This sets how hard to push on depth and sharing.
3. Is the business unit structure settled? Privilege depth only has meaning relative to it.
4. Which non-human identities exist (application users, integration accounts, flows owned by service accounts)? Excess privilege usually hides here.
5. Who owns Entra ID groups and conditional access? Usually not the CRM team, so findings there need a named owner outside the project.

## Approach

Review evidence, not intentions. Ask for the role matrix (persona, table, privilege, depth), an export of the custom roles from the target environment, the application users with their roles, and the team list. Compare the design with what is deployed; drift between the two is a finding in its own right.

1. Roles. Check that custom roles are copies or built from scratch rather than edits to out-of-box roles, which platform updates can change. Favour a small base role that every user holds plus additive functional roles over one large role per job title. Challenge every organisation-wide read, write or delete on a table holding personal data and ask for the business reason.
2. Quiet privileges. Assign, Share, Append To and delete are where leakage and data loss begin. Share lets one user widen access for everyone downstream, so it should be rare. Customisation privileges in production belong to administrators only.
3. Teams and hierarchy. Confirm that owner teams carry shared ownership, access teams handle per-record collaboration, and Entra ID group teams keep membership in step with the directory. If hierarchy security is on, check which model (manager or position) and depth were chosen and whether anyone has tested it at realistic volumes.
4. Sharing and cascades. Heavy manual sharing, and cascading share or assign across parent and child records, grow the access table quickly and slow queries. Ask how much sharing the design expects; if nobody knows, record it.
5. Identity. Application users need a role scoped to what the integration touches. At a high level, confirm that conditional access covers the environment (multi-factor authentication, device rules for mobile and offline use) and that an environment security group limits who can be given access.
6. Testing. Ask for evidence of tests run while signed in as each persona, including negative tests. Hiding a form, view or button is not a control.

Log each finding with an id, area, evidence, classification and required action. A finding is blocking when data is exposed beyond need-to-know, a privilege escalation path exists, or persona testing has not happened; the rest are advisory. Where a finding raises a legal question, such as whether a persona may lawfully see special category data, frame the question and refer it to the organisation's DPO or legal adviser.

## Outputs

- Security findings log (id, area, evidence, blocking or advisory, action, owner, due date), with blocking items copied to the `raid-log`.
- Annotated role matrix recording what was approved and on what conditions.
- Persona test checklist for inclusion in the `test-strategy-and-uat-scripts`.
- Sign-off statement naming the reviewer, the scope, the environment reviewed and any open blocking findings.

## Scale notes

### SMB

One consultant often designs and builds the whole model, so the review must come from someone else: a partner colleague, the customer's IT lead or an external reviewer for a day. Keep the review to the essentials: persona tests, application users, organisation-wide depth on personal data and the Share privilege. Two or three custom roles are usually enough, and a smaller model is easier to keep right.

### Enterprise

Review at design, before UAT, before go-live and after every major release. The security-lead owns the model and the reviewer must be someone else, as the role combination rules expect. Look for a role naming standard, a persona-to-role register under change control, automated checks in the pipeline where feasible, and periodic access recertification after go-live with the Entra ID owners involved.

## Hand-offs

Blocking findings return to the builders, usually through `platform-engineering:solution-layering` for role packaging and `platform-administration:environment-setup` for environment access. Persona tests go to `testing-quality:user-acceptance-testing`, and open blocking findings are an input to `programme-management:go-no-go`. Changes to an approved model come back through `design-authority:change-impact-assessment` and then through this review again.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Approve a model that nobody has tested by signing in as each persona.
- Accept System Administrator on an application user or integration account for convenience.
- Treat hidden forms, views or buttons as a security control.
- Let the department under review downgrade or close its own blocking finding.
- Give a view on whether access is lawful instead of referring it to the DPO or legal adviser.
