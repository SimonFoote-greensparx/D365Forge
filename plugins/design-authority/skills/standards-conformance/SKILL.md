---
name: standards-conformance
description: Checks built Dynamics 365 CE components against project standards for naming, publisher prefix, solution layering, security and ALM, and reports each nonconformity as blocking or advisory. Use when reviewing solutions before deployment, auditing an environment for drift, onboarding a new partner, or gathering release evidence.
metadata:
  department: design-authority
  stages: Implement, Prepare, Operate
  modules: All
  status: draft
---

# Standards conformance

Standards are cheap to write and easy to ignore under deadline pressure. On Dynamics 365 CE the cost of drift shows up late: components created under the default publisher, unmanaged changes layered over managed solutions in production, security roles copied and edited until nobody knows which is authoritative, and flows owned by individuals who then leave. Each of these is quick to prevent and slow to unpick.

Standards conformance is the reviewer-class check that what was built follows the standards agreed for the programme. It is read-only: it inspects solutions, environments and pipelines and reports findings, and the building department makes the corrections.

## When to use

- Before a solution is deployed to test, UAT or production.
- Auditing an environment, especially production, for drift.
- Onboarding a new partner or team whose output must meet the same standards.
- Assembling conformance evidence for a release decision.

Not this skill: `platform-engineering:solution-layering` for designing the solution structure, `platform-engineering:deployment-pipelines` for building pipelines, `security-compliance:security-model-review` for an in-depth review of the security design, and `design-authority:design-review` for reviewing designs before build.

## Questions to ask first

1. Are the standards written down and agreed? You can only review against documented standards; anything else is opinion.
2. What is in scope: a solution, an environment, a release or a partner deliverable? Scope decides which checks apply.
3. Is the solution in source control, and can you see exactly what will be deployed? Reviewing a live environment alone misses what is about to arrive.
4. Has solution checker been run? Its results are a useful baseline, although it does not know the project's own standards.

## Approach

Run the checks in five groups and record each nonconformity with evidence (component, environment, what was expected, what was found).

1. Naming. Tables, columns, relationships, forms, views, flows, web resources, plug-in assemblies, security roles and environment variables follow the agreed conventions. Display names read well to business users; schema names are consistent and meaningful.
2. Publisher and prefix. Every component belongs to the project publisher with its agreed prefix, not the default publisher. ISV components stay in their own managed solutions and are not edited.
3. Solution layering. Downstream environments receive managed solutions only. Look for unmanaged layers over managed components in test and production, segmentation that matches the design, dependencies that are declared and minimal, and patches or upgrades used the way the ALM standard prescribes.
4. Security. Custom roles are built up from least privilege rather than copied from System Administrator. Integrations and automation run as application users. Field-level security profiles match the design. No individual user owns production flows or connections the business depends on.
5. ALM. Solutions are exported to source control, deployed by pipeline, use environment variables and connection references for environment-specific settings, and carry a version number that matches the release. Solution checker results have been reviewed and critical issues closed.

Classify each finding.

- Blocking: the nonconformity would make the release unsupportable, insecure or impossible to deploy cleanly, for example unmanaged customisations in production, components in the default publisher, hard-coded environment URLs, or integration identities with administrator rights. The release does not proceed until it is fixed.
- Advisory: issues such as naming inconsistencies that should be corrected in a planned clean-up.

Blocking findings are not overruled by the department under review. Disagreement escalates to the steering committee or executive sponsor, who may grant a time-bound exception that is recorded with an owner and a fix date.

Run conformance before every release to a downstream environment, and periodically against production to catch drift introduced outside the pipeline.

## Outputs

- Conformance report per release or environment, with findings classified as blocking or advisory.
- Exceptions register with owners and fix dates.
- Proposed clarifications to the standards in the `environment-and-alm-strategy` where a standard proved ambiguous.

## Scale notes

### SMB

The lead consultant plays this role, running a short checklist before each deployment: publisher prefix, managed solution, nothing in the default publisher, security roles, solution checker. A second pair of eyes from someone outside the delivery, even once before go-live, catches what the builder cannot see. Do not skip the managed solution and publisher checks; they are the hardest to undo later.

### Enterprise

Automate what can be automated (solution checker in the pipeline, naming rules, detection of unmanaged layers) and have the design authority sample the rest each release. Partners and internal teams work to the same standards, and conformance reports form part of the release evidence.

## Hand-offs

- Nonconformities return to the building department, typically `platform-engineering:solution-layering`, `platform-engineering:deployment-pipelines` or `platform-engineering:plugin-design`.
- Security findings are shared with `security-compliance:security-model-review`.
- `platform-administration:release-readiness` uses conformance results in release decisions.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Fix nonconformities directly in the environment under review.
- Pass a release to production that contains unmanaged customisations.
- Accept components built under the default publisher.
- Let the department under review downgrade a blocking finding.
