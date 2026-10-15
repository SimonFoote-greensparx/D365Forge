---
name: environment-setup
description: Provisions and configures Dynamics 365 CE environments to the agreed strategy, covering type, region, base currency and language, security groups, admin roles, application users and baseline settings. Use when creating or configuring an environment, restricting who can open it, or setting up service identities for integrations and pipelines.
license: CC-BY-4.0
metadata:
  department: platform-administration
  stages: Initiate, Implement, Prepare
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Environment setup

Environment setup turns the environment strategy into real, configured environments. Several choices made at creation cannot be undone without rebuilding, and a misconfigured setting (an open security group, missing audit settings, an integration running as a person) becomes a production problem that nobody notices until an audit or an outage.

Typical failures are a production environment created with the wrong base currency, environments that anyone in the tenant can open, integration identities holding the System Administrator role, and Dynamics 365 app versions that differ between UAT and production, so a solution that imported cleanly in testing fails on go-live night.

## When to use

- Creating environments from the approved environment register.
- Restricting access to an environment or appointing its administrators.
- Creating application users for integrations, pipelines or agents.
- Establishing or checking the baseline configuration of an environment.

Not this skill: `solution-architecture:environment-strategy` for deciding which environments exist, `platform-administration:licensing-and-capacity` for licences and capacity, `security-compliance:security-model-review` for the business security model, and `security-compliance:business-units-and-teams` for business unit and team design.

## Questions to ask first

1. Is the environment on the approved register with its type, region and purpose? Setup follows the strategy; it does not invent environments.
2. Which base currency and base language will it use? Both are fixed when the environment is created.
3. Which Microsoft Entra security group gates access? Without one, every user in the tenant with a suitable licence can reach it.
4. Which Dynamics 365 apps, at which versions, are needed? Mismatched app versions cause solution import failures.
5. Is there enough capacity? Creation and copy operations can be blocked when the tenant is over capacity, so for entitlements, confirm with the Microsoft licensing guide or your partner.

## Approach

Script what you can and record everything else, so any environment can be rebuilt to the same baseline.

1. Create to the register. Use the agreed name, type, region and purpose. Confirm base currency and base language with the business before creating production, and add the Dynamics 365 apps at creation where the set-up flow allows it.
2. Gate access. Assign a dedicated security group to each environment, with membership managed by the identity team. Use group-based licence assignment where the organisation already works that way.
3. Separate admin roles. Keep tenant-level Power Platform administrator roles to a small named group, give the System Administrator security role only to those who need it in each environment, and agree a break-glass account process with security.
4. Create application users properly. Each integration, pipeline and agent connection gets its own app registration and application user with a custom security role scoped to its job. Record the owner, purpose and secret or certificate expiry date for each.
5. Apply the baseline settings. Turn on auditing at environment and table level as agreed with security, set plug-in trace logging (fuller in development and test, exceptions only in production), configure server-side sync and mailboxes, document management, and session and inactivity timeouts, and enable Managed Environments where the strategy calls for it. Keep these in a checklist and, where possible, apply them with the Power Platform CLI or PowerShell so they are repeatable.
6. Align app versions. Before deploying solutions, check that installed Dynamics 365 apps and their versions match along the path, updating lower environments first.
7. Tidy the default environment. Rename it so its purpose is clear, restrict what can be built there and make sure a DLP policy covers it.
8. Protect before change. Confirm system backups are in place and take a manual backup before major changes or deployments.

## Outputs

- Completed environment register entries (name, URL, type, region, currency, language, security group, admin owner), recorded in the `environment-and-alm-strategy`.
- A baseline configuration checklist per environment.
- An application user register with owners and credential expiry dates.
- Set-up scripts held in source control.

## Scale notes

### SMB

A partner consultant usually sets up a handful of environments directly in the Power Platform admin center. Do not skip security groups, a non-personal integration identity, or confirmation of base currency and language before production is created. A simple checklist is enough to record the baseline.

### Enterprise

A platform team owns setup, working from requests approved against the register. Scripts create and configure environments, a regular review checks admin role membership and application user credentials, and changes to production settings go through change control.

## Hand-offs

`platform-administration:monitoring` takes the environments into operational monitoring, `platform-engineering:deployment-pipelines` uses the application users, and `security-compliance:business-units-and-teams` builds the security structure inside each environment. Reviewer sign-off: `security-compliance:security-model-review` for admin roles and application user permissions.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create a production environment before base currency and base language are confirmed.
- Leave an environment without a security group restricting access.
- Give integration or pipeline application users the System Administrator role by default.
- Run integrations or pipelines under a named person's account.
- Deploy solutions while Dynamics 365 app versions differ between source and target environments.
