---
name: environment-strategy
description: Decides which Dataverse environments a Dynamics 365 CE programme needs, with their purpose, type, region, Managed Environments status and data copy rules, and how data residency is handled. Use when planning the environment landscape, adding workstreams or phases, or answering where customer data will be stored.
license: CC-BY-4.0
metadata:
  department: solution-architecture
  stages: Initiate, Implement
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Environment strategy

The environment landscape is the physical shape of the ALM process. It decides where people build, where testing happens, how close test data is to production and where customer data physically resides. It is cheap to get right at the start and expensive to change later, because the region is chosen when an environment is created and every integration and pipeline is wired to specific environments.

The common failures are building in the default environment, sharing one sandbox for development and UAT so testers trip over half-finished work, and discovering late that the capacity bought cannot support the copies the test plan assumed. Another is forgetting the post-go-live shape, so the first urgent fix has nowhere safe to be built.

## When to use

- In Initiate, when the environment list and the ALM path are first defined.
- A new workstream, phase or module needs its own space to build or test.
- Data residency, sovereignty or regulatory questions are raised about where data sits.
- Post-go-live support needs a hotfix lane alongside the next release.

Not this skill: `platform-administration:environment-setup` to create and configure the environments, `platform-engineering:deployment-pipelines` to automate movement between them, and `platform-administration:licensing-and-capacity` for the capacity they consume.

## Questions to ask first

1. How many teams build in parallel, and how often will they release? This sets the number of development environments and whether a hotfix lane is needed.
2. What data residency or regulatory obligations apply? Region is fixed at creation, and the answer must come from the organisation's DPO or legal adviser.
3. How much Dataverse capacity is available? Every environment and every copy consumes it.
4. Which external systems need non-production counterparts? Without matching test endpoints, integration testing drifts towards production.
5. Does testing need production-like data? This determines the copy, masking and refresh approach.

## Approach

Design the landscape as the path a change travels, then add only the environments that path genuinely needs.

1. Define the core path. A typical CE path is development, test (system and integration testing), UAT and production. Add a build environment where several developers need a clean place to assemble solutions, and a training environment if training runs alongside UAT. Use the sandbox type for everything except production, and Developer environments for individual makers and short experiments.
2. Separate building from testing. Unmanaged work happens only in development. Every downstream environment receives managed solutions through a pipeline, so test results reflect exactly what production will receive.
3. Plan the post-go-live shape now. After go-live, a support lane (its own development and test) runs alongside the project lane, with a clear rule for merging fixes back. Projects that skip this end up patching production directly.
4. Decide on Managed Environments. Managed Environments add governance controls such as sharing limits, usage insights and solution checker enforcement, and some deployment features depend on them. Enable them at least for production and for every environment a pipeline deploys into, and check current Microsoft Learn documentation for the feature set. Managed Environments carry licensing conditions, so confirm with the Microsoft licensing guide or your partner.
5. Settle region and residency. Choose the geography deliberately and record the reason. Moving an environment between geographies is not a routine admin action. Residency, sovereignty and cross-border transfer questions go to the organisation's DPO or legal adviser.
6. Define data handling. State which environments may hold production copies, how personal data is masked or minimised, who approves a copy and how often environments are refreshed. Raise the lawful basis for test copies with the organisation's DPO or legal adviser rather than assuming copies are acceptable.
7. Pair integrations and name things. Map each environment to its integration endpoints, security group and owner, and apply a naming convention that makes the purpose obvious in the Power Platform admin center.

## Outputs

- Environment chapter of the `solution-blueprint` and the environment section of the `environment-and-alm-strategy`.
- An environment register listing purpose, type, region, Managed Environments status, security group, owner and integration pairings.
- Data copy, masking and refresh rules for non-production environments.
- A capacity estimate per environment handed to licensing.

## Scale notes

### SMB

Three environments (development, a combined test and UAT, and production) are often enough for a single app with mostly standard configuration, plus a Developer environment for experiments. What must not be skipped is keeping development separate from production and moving managed solutions between them. If capacity forces a compromise, combine test with UAT, never development with UAT.

### Enterprise

Expect development environments per workstream or per developer, a shared build environment, separate SIT, UAT, performance, training and pre-production environments, and the support lane. Environment groups and rules can help apply policies consistently; check current Microsoft Learn documentation for what they cover. New environment requests go through the design authority, and the platform team owns the register.

## Hand-offs

`platform-administration:environment-setup` provisions the register, `platform-engineering:deployment-pipelines` wires the path, and `platform-administration:licensing-and-capacity` confirms the capacity. Sign-off comes from `design-authority:design-review`, with `security-compliance:data-retention` for the rules on production copies and `security-compliance:security-model-review` for access to each environment.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Build or customise solutions in the default environment.
- Use one environment for both development and UAT.
- Copy production personal data into non-production without masking and agreement from the DPO.
- Choose an environment region before data residency requirements are confirmed.
- Make production the first environment to receive a managed solution.
