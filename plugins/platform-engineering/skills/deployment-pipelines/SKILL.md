---
name: deployment-pipelines
description: Designs automated deployment of Dynamics 365 CE solutions with Pipelines in Power Platform, Azure DevOps with Power Platform Build Tools or GitHub Actions, covering source control, build, approvals, deployment settings and configuration data. Use when setting up ALM automation, choosing a tool, or fixing failed deployments.
license: CC-BY-4.0
metadata:
  department: platform-engineering
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Deployment pipelines

Manual export and import works for the first few weeks of a project and then becomes the biggest single source of deployment errors: the wrong solution version, a missing environment variable, a connection reference pointing at a developer's account, or reference data that never reached UAT. An automated pipeline makes every deployment repeatable and leaves a trail of what went where, when and with whose approval.

The choice of tool matters less than the discipline around it. Projects go wrong when the pipeline moves solutions but not the configuration data they need, when secrets live in pipeline definitions, or when urgent fixes bypass the pipeline and the next release silently overwrites them.

## When to use

- Setting up ALM automation at the start of build.
- Choosing between Pipelines in Power Platform, Azure DevOps and GitHub Actions.
- Deployments fail, differ between environments or depend on one person.
- Preparing the production deployment approach for go-live.

Not this skill: `platform-engineering:solution-layering` for solution structure and publishers, `solution-architecture:environment-strategy` for the environment path, `support-operations:cutover-plan` for the go-live runbook, and `testing-quality:regression-automation` for the automated test content.

## Questions to ask first

1. Who will run deployments: makers, professional developers or both? This drives the choice of tool.
2. Is Azure DevOps or GitHub already used and supported in the organisation? Reusing an established platform reduces cost and friction.
3. Which approvals are required before test, UAT and production? Approvals belong inside the pipeline, not in email threads.
4. What configuration data must move with the solutions? Queues, SLA settings, routing rules, incident types and price lists are records, not solution components, and need their own path.
5. Are the target environments Managed Environments? Some pipeline features depend on it; check current Microsoft Learn documentation.

## Approach

1. Choose the tool for the team. Pipelines in Power Platform suit maker-led projects that need simple, governed promotion with little set-up. Azure DevOps with Power Platform Build Tools, or GitHub Actions for Power Platform, suit projects with plug-ins, PCF controls, automated tests, branching and several solutions. The two can be combined; check current documentation for extensibility options.
2. Make source control the master. Export and unpack solutions from development into the repository on every meaningful change, review through pull requests, and treat the repository rather than the development environment as the truth.
3. Build once, deploy many. The build compiles plug-ins and code components, runs unit tests and solution checker, packs a managed solution with a stamped version and stores it as an artefact. That same artefact then moves through test, UAT and production.
4. Supply environment values at deploy time. Use a deployment settings file per environment for connection references and environment variables. Deploy with a service principal registered as an application user, and keep secrets in a key vault or the pipeline's secure store.
5. Move configuration data deliberately. Package reference and configuration records with the Configuration Migration tool or Package Deployer, keep record identifiers stable across environments and version the data packages alongside the solutions.
6. Gate and verify. Add approvals before UAT and production, take a manual backup before each production deployment, run smoke tests afterwards and confirm that flows and plug-in steps are active.
7. Plan for failure. Rolling back a managed solution is rarely simple, so favour a quick forward fix through the same pipeline, keep previous artefacts available and rehearse the production deployment in pre-production.
8. Route urgent fixes through the pipeline. Build them on a hotfix branch, deploy through the same gates and merge back so the next release does not overwrite them.

## Outputs

- ALM and pipeline section of the `environment-and-alm-strategy`.
- Pipeline definitions, deployment settings files and configuration data packages held in source control.
- Release notes per deployment showing version, approver and target environment.
- Production deployment steps referenced by the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Pipelines in Power Platform is often enough, with one solution and a simple path from development through test to production. Do not skip source control for anything containing code, deployment settings for connection references, or a backup before each production deployment.

### Enterprise

Use Azure DevOps or GitHub with a branching model per release, build validation on pull requests, automated regression after each test deployment, and segregation of duties so the person who builds a change cannot approve it into production. The pipeline becomes a controlled system with its own owner and change process.

## Hand-offs

`testing-quality:regression-automation` plugs tests into the pipeline, `support-operations:cutover-plan` uses the production deployment steps, and `platform-administration:environment-setup` creates the application users and connections. Reviewer sign-off: `design-authority:standards-conformance`, with `security-compliance:security-model-review` for service principal permissions.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Deploy to production by manual export and import from a developer's machine.
- Store client secrets or passwords in pipeline definitions or source control.
- Skip solution checker and post-deployment smoke tests for a production release.
- Rely on restoring a backup as the only rollback plan.
- Deploy unmanaged solutions beyond development.
