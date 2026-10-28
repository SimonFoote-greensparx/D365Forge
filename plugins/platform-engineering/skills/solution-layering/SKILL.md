---
name: solution-layering
description: Sets the publisher, solution segmentation and managed layering approach for Dynamics 365 CE customisations, including dependencies, upgrades, patches and removal of unmanaged layers. Use when structuring solutions at the start of build, splitting work across teams, or diagnosing why a deployed change is not taking effect.
license: CC-BY-4.0
metadata:
  department: platform-engineering
  stages: Initiate, Implement, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Solution layering

Every customisation in Dataverse lives in a layer. Microsoft's own apps are managed layers, ISV products add more, the project's solutions sit on top, and any unmanaged change made directly in an environment sits above all of them. How those layers stack decides which version of a form, column or flow users actually see, and whether the next deployment can change it.

Projects lose control of layering in familiar ways: building with the default publisher, making a quick fix directly in production that leaves an unmanaged layer the pipeline can never override, splitting into many solutions with tangled dependencies, or adding entire Microsoft tables to a solution when only one form changed.

## When to use

- Setting up the publisher and solution structure at the start of build.
- Several teams or workstreams need to deliver independently.
- A change deployed through the pipeline does not appear in an environment.
- Inheriting an estate with unmanaged customisations in production.

Not this skill: `platform-engineering:deployment-pipelines` for automating builds and deployments, `solution-architecture:environment-strategy` for the environment landscape, and `design-authority:standards-conformance` for checking components against standards.

## Questions to ask first

1. How many teams build in parallel, and do they release on the same cadence? Independent cadences may justify separate solutions; a shared cadence rarely does.
2. Which ISV or partner solutions are installed? Their managed layers sit beneath yours and constrain what you can change.
3. Does production already contain unmanaged customisations? Remediation must be planned before the first managed deployment.
4. Who owns the publisher? It should be the customer, unless the partner is shipping its own product.

## Approach

1. Use one customer publisher. Create a publisher that represents the organisation, with a short, meaningful prefix and a reserved choice value prefix, and use it for every project component. The default publisher and its prefix are not used for project work.
2. Go managed beyond development. Development environments hold the unmanaged source; every other environment receives managed solutions only. Source control, not an environment, holds the master copy of the unmanaged solution.
3. Segment only along real boundaries. Start with as few solutions as possible. Split when there is a genuine reason, such as different release cadences, a reusable core shared by several apps, code components or an integration package. Dependencies run one way, from module solutions to the core, never back.
4. Add only what changes. When customising a Microsoft table, add the table without all its components and then add only the forms, views and columns you change. Adding everything puts your layer over components you never meant to own and masks Microsoft's later changes to them.
5. Understand which layer wins. For most components the most recently installed managed layer takes effect, and an unmanaged layer overrides every managed layer beneath it. Use the solution layers view to see the stack for a component, and remove active unmanaged customisations once the managed version is correct.
6. Prefer upgrades to patches. A full solution upgrade removes components deleted in development, while patches add complexity and can leave the stack inconsistent. Use a staged upgrade where data must be moved between versions; check current Microsoft Learn documentation for the upgrade options.
7. Version consistently. Increment version numbers in the pipeline rather than by hand, so every build is traceable.
8. Remediate an inherited estate. Compare production with source, rebuild missing components in development, deploy them as managed and then remove the unmanaged layer component by component, testing as you go.

## Outputs

- Solution structure section of the `environment-and-alm-strategy`, covering publisher, solution list, dependencies and versioning.
- A component ownership map showing which solution owns each customised component.
- A remediation plan for unmanaged layers where an estate is inherited.

## Scale notes

### SMB

One publisher and usually one solution are enough, perhaps with a separate solution for code components. What must not be skipped is managed deployment to production and a rule that nobody customises production directly, even for a quick fix.

### Enterprise

Define a solution map with an owner per solution, enforce one-way dependencies with checks in the pipeline and audit layers regularly across test and production. Workstreams own their module solutions, a platform team owns the core, and the design authority approves any new solution.

## Hand-offs

`platform-engineering:deployment-pipelines` builds and moves the solutions, and `solution-architecture:environment-strategy` confirms where each is built and tested. Reviewer sign-off: `design-authority:standards-conformance`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Import unmanaged solutions into production.
- Customise directly in test, UAT or production environments.
- Use the default publisher or its prefix for project components.
- Add whole Microsoft tables with all their components when only a few are changing.
- Create circular dependencies between project solutions.
