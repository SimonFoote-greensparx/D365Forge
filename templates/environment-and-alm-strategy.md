---
id: environment-and-alm-strategy
title: Environment and ALM strategy
format: docx
owner: solution-architecture:environment-strategy
tailored_from: organisation, estate, constraints, edition, modules_in_scope, roles, generated_on
status: draft
---

# Environment and ALM strategy

## How to use this template

The solution architect ({{roles.solution-architect}}) drafts this strategy in Initiate with the platform administrator ({{roles.platform-administrator}}) and, where one exists, the release manager ({{roles.release-manager}}). It must be approved before the first sprint, because environments, the solution publisher and the pipeline are expensive to change once build has started. Review it at each stage gate and after any change to licences or capacity.

> Guidance: The aim is simple: every change is made in development, held in source control, and reaches test and production only as a managed solution through a repeatable pipeline. Each section below should show how that holds for this project.

> SMB: Three environments (development, test, production) and a simple pipeline are usually enough. Keep source control and managed solutions even when the partner is the only developer.

> Enterprise only: Plan separate environments for SIT, UAT, training and pre-production, per-developer environments where the team is large, and pipeline approval gates owned by the release manager.

## Document control

| Version | Date | Author | Summary of change | Approved by |
|---|---|---|---|---|
| 0.1 | {{generated_on}} | {{roles.solution-architect}} | First draft generated from organisation profile | |

## 1. Context

{{organisation.name}} is delivering {{modules_in_scope}} as a {{edition}} project. Existing environments recorded in the profile: {{estate.environments}}. Licences recorded: {{estate.licences}}. Microsoft 365 tenant: {{estate.microsoft_365}}.

> Guidance: Note any existing Dataverse environments, Power Apps or flows already in the tenant, and who owns them. Unmanaged makers' work in the default environment is common and should be inventoried before the project's environments are created.

## 2. Principles

- Development happens only in development environments; nobody customises test, UAT or production directly.
- Downstream environments receive managed solutions only.
- One publisher and prefix for the project's own components, agreed before the first component is created.
- Everything that varies by environment is an environment variable or connection reference, never a hard-coded value.
- Source control is the record of what was built; an environment can be rebuilt from it.

## 3. Environment inventory

| Environment | Type | Purpose | Region | Security group | Owner | Data held | Refresh approach |
|---|---|---|---|---|---|---|---|
| Development | Sandbox | Configuration and build | | | {{roles.platform-administrator}} | Sample data only | Rebuilt from source as needed |
| Test or SIT | Sandbox | Integrated testing with test endpoints | | | {{roles.test-manager}} | Migrated test data | Refreshed before each test cycle |
| UAT | Sandbox | Business acceptance testing | | | {{roles.test-manager}} | Masked or synthetic data | Refreshed before UAT |
| Training | Sandbox | End-user training | | | {{roles.trainer}} | Training data set | Reset between sessions |
| Production | Production | Live service | | | {{roles.platform-administrator}} | Live data | Not applicable |

> Guidance: Choose the region to meet data residency needs for {{organisation.countries}} and any compliance constraints ({{constraints.compliance}}); confirm with the DPO or legal adviser where personal data is involved. Copying production into a sandbox brings live personal data with it, so agree masking or restricted access before doing so.

> Enterprise only: Add pre-production for cutover rehearsal and performance testing, and consider separate developer environments per developer or workstream.

## 4. Solution structure

| Solution | Contents | Publisher prefix | Depends on | Owner |
|---|---|---|---|---|
| Core | Shared tables, columns, security roles, base components | | None | {{roles.solution-architect}} |
| Module solution per workstream | Module-specific configuration | | Core | Module lead |
| Integration | Custom APIs, plugins, connection references | | Core | {{roles.integration-lead}} |

> Guidance: Fewer solutions are easier to manage. Split only where release cadence or ownership genuinely differs, and never let two solutions modify the same component without a clear layering plan.

## 5. Source control and branching

> Guidance: Name the repository, the branching model and who may merge. Solutions are exported and unpacked into source control on each change. Keep configuration data (for example queues, SLA settings, reference data) in source control too, packaged with the deployment.

## 6. Deployment pipeline

| Stage | From | To | Trigger | Approval required from | Automated checks |
|---|---|---|---|---|---|
| Build | Development | Artefact store | Merge to main branch | None | Solution checker, unit tests |
| Deploy to test | Artefact | Test or SIT | Successful build | {{roles.test-manager}} | Smoke tests |
| Deploy to UAT | Artefact | UAT | Test cycle passed | {{roles.process-owner}} | Smoke tests |
| Deploy to production | Artefact | Production | Release approved | {{roles.release-manager}} | Smoke tests, deployment log |

> Guidance: Options include Power Platform pipelines, Azure DevOps or GitHub with the Power Platform tooling. Check current Microsoft Learn documentation for capabilities and prerequisites before choosing.

## 7. Environment-specific settings

| Setting | Type | Development | Test | UAT | Production | Owner |
|---|---|---|---|---|---|---|
| ERP endpoint for {{estate.erp}} | Environment variable | | | | | {{roles.integration-lead}} |
| Mailbox server profile | Configuration | | | | | {{roles.platform-administrator}} |
| Sending domain (Marketing only) | Configuration | | | | | {{roles.journeys-consultant}} |

## 8. Governance and capacity

> Guidance: Describe data loss prevention policies for each environment, whether Managed Environments are used, who may create environments, and how the default environment is governed. Record storage capacity and how growth is monitored. Confirm licence and capacity entitlements with the Microsoft licensing guide or your partner; check current Microsoft Learn documentation for governance features.

## 9. Release waves and updates

> Guidance: Describe how each release wave is tested before it reaches production: which sandbox receives early access, who runs the regression pack, and who decides whether issues block. Note organisation change freezes ({{constraints.change_freezes}}).

## 10. Access and administration

| Activity | Who may perform it | Approval |
|---|---|---|
| Create or delete environments | {{roles.platform-administrator}} | {{roles.solution-architect}} |
| Assign system administrator role | {{roles.platform-administrator}} | {{roles.security-lead}} |
| Copy or reset an environment | {{roles.platform-administrator}} | Environment owner; DPO if production data is copied |
| Import solutions to production | Pipeline only | {{roles.release-manager}} |

## 11. Approval

| Name | Role | Decision | Date |
|---|---|---|---|
| {{roles.solution-architect}} | Solution architect | | |
| {{roles.design-authority-lead}} | Design authority lead | | |
| {{roles.platform-administrator}} | Platform administrator | | |
