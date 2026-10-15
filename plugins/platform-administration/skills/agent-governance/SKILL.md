---
name: agent-governance
description: Governs who can build, share and publish Copilot Studio agents, flows and apps across the tenant, using DLP policies, environment zoning, Managed Environments controls, the CoE Starter Kit and an agent approval path. Use when setting maker policies, approving an agent for wider release, or tracking down ungoverned agents.
license: CC-BY-4.0
metadata:
  department: platform-administration
  stages: Initiate, Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Agent governance

Copilot Studio and Power Platform let anyone with the right licence build an agent or automation that reaches CRM data and talks to customers or colleagues. That is a real benefit and a real exposure: an agent built in the default environment with a broad connector and published to a public channel can leak data faster than any report.

Governance fails at both extremes. Locking everything down pushes makers towards unofficial tools, while leaving everything open produces a sprawl of unowned agents and flows that nobody can inventory. The aim is a clear path that makes the safe route the easy one.

## When to use

- Setting or reviewing tenant policies for makers, connectors and agents.
- An agent is ready to move from a team pilot to a wider or external audience.
- Inventorying agents, flows and apps, or dealing with orphaned ones.
- Rolling out Copilot Studio to makers beyond the project team.

Not this skill: `platform-engineering:copilot-studio-agents` for how to build an agent, `data-and-ai:responsible-ai-review` for the responsible AI assessment, `data-and-ai:copilot-and-agent-enablement` for enabling Microsoft's own copilots, and `security-compliance:security-model-review` for Dataverse security roles.

## Questions to ask first

1. Who should be able to build agents: the project team, approved makers or everyone? This sets the zone model and which licences makers need, so confirm with the Microsoft licensing guide or your partner.
2. Which data classes may agents use, and which must never leave the organisation? Regulated or personal data needs a decision from the organisation's DPO or legal adviser.
3. Which channels are allowed (Teams only, internal sites, public websites, Dynamics 365 Contact Center)? External channels carry the greatest risk.
4. What governance already exists in the tenant (DLP policies, Managed Environments, the CoE Starter Kit)? Build on it rather than duplicating it.
5. Who owns an agent when its maker moves on? Ownership must survive staff changes.

## Approach

1. Zone the environments. Define a personal zone for individual productivity (restricted connectors, no external channels, sharing only with small groups), a team zone for departmental solutions with a named owner, and a managed zone for business-critical and customer-facing agents built under full ALM. Route new makers into their own developer environments where the tenant supports it, checking current Microsoft Learn documentation for the options.
2. Set DLP policies. Classify connectors as business, non-business or blocked, with a tenant-wide baseline and environment-level policies per zone. Data policies also govern Copilot Studio capabilities such as knowledge sources, channels and HTTP requests; check current documentation for the controls available, and test policy changes against existing agents and flows before enforcing them.
3. Use Managed Environments controls. Apply sharing limits, maker welcome content that explains the rules, solution checker enforcement and usage insights in the team and managed zones.
4. Inventory continuously. Install and run the Center of Excellence (CoE) Starter Kit, or equivalent admin reporting, to inventory agents, flows, apps and makers, spot orphaned resources and drive compliance follow-up. The kit needs its own set-up and upkeep, and some components need premium licences; confirm with the Microsoft licensing guide or your partner.
5. Define the approval path. Before an agent moves to a wider audience or an external channel, require a registered business owner, a description of the data used and actions taken, the authentication method, a responsible AI review, a security review and a test record. Approved agents move into the managed zone.
6. Manage the lifecycle. Run periodic ownership attestation, quarantine or disable agents whose owners have left or which are no longer used, and remove maker access as people change roles.
7. Monitor use. Review usage analytics and audit logs for agents and connectors, and feed what you find into the next policy review.

## Outputs

- An agent and maker governance policy, including the zone model and approval path.
- A DLP policy design per zone, with the connector classification register.
- An agent inventory recording owner, audience, data, channels and review status.
- Governance findings and policy exceptions recorded in the `raid-log`.

## Scale notes

### SMB

Often there is no central IT governance at all. Start with a tenant-wide DLP baseline, a restricted default environment, a separate governed environment for anything customer-facing and a simple list of agents and owners. Do not skip the approval step before any agent faces customers.

### Enterprise

A platform governance team owns the policies and the CoE Starter Kit, with a regular maker forum bringing makers, security and data protection together. Agent approval follows a defined workflow with security and responsible AI sign-off, and governance measures are reported to the steering committee.

## Hand-offs

`data-and-ai:responsible-ai-review` assesses agents in the approval path, `platform-engineering:copilot-studio-agents` builds managed-zone agents, and `platform-administration:monitoring` takes agent usage signals into operations. Reviewer sign-off: `security-compliance:security-model-review` for data access before any external publication.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Let makers publish agents to external channels from the default environment.
- Allow agents to use connectors the DLP policy has not classified.
- Approve an agent for wider release without a named business owner.
- Disable DLP enforcement to unblock a single maker or project.
- Publish a customer-facing agent without a responsible AI review.
