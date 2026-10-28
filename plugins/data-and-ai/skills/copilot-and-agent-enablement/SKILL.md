---
name: copilot-and-agent-enablement
description: Plans the rollout of Copilot features and agents across the CE apps, covering data and knowledge readiness, security trimming, admin settings, licensing questions and pilots. Use when choosing which Copilot capabilities to switch on, preparing data for Copilot, or sequencing agents across Sales, Service, Field Service and Marketing.
license: CC-BY-4.0
metadata:
  department: data-and-ai
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Copilot and agent enablement

Copilot features in Dynamics 365 are easy to switch on and hard to make useful. They summarise, draft and answer from whatever is in Dataverse, in knowledge sources and in the user's context, so incomplete records, stale knowledge articles and loose security become visible to every user at once. Projects go wrong by enabling everything in one release with no pilot, no measure of value, and no answer to the licensing questions that arrive the following week.

Agents raise the stakes because they act rather than suggest. Treat each agent as a solution component with an owner, a scope and a review, not as a setting.

## When to use

- Deciding which Copilot features and prebuilt or custom agents to enable, in what order, for which roles.
- Preparing data, knowledge and security so Copilot output can be trusted.
- Coordinating the admin, regional and licensing prerequisites that enablement depends on.
- Designing pilots and measures of value, and keeping the plan current through release waves.

Not this skill: `sales:copilot-in-sales` and `customer-service:service-agents-and-copilot` for configuring module features, `platform-engineering:copilot-studio-agents` for building custom agents, `platform-administration:agent-governance` for operational governance of agents, `data-and-ai:responsible-ai-review` for the risk review of each use case.

## Questions to ask first

1. Which outcomes should Copilot move, for which roles? Without a target, enablement becomes a feature list nobody can judge.
2. How complete and current is the data Copilot will read: notes, tracked emails, case history, knowledge articles? Copilot output can only be as good as that data.
3. Do users' security roles grant only what they should see? Copilot does not widen access, but it surfaces whatever users can already reach far faster than they would find it themselves.
4. Where is the environment hosted, and do the features need data to move across geographies? Availability and admin consent vary by region, so check current Microsoft Learn documentation; whether cross-border data movement is acceptable is a question for the organisation's DPO or legal adviser.
5. Which features are included in the licences already held, and which need add-ons or consumption capacity? Confirm with the Microsoft licensing guide or your partner.

## Approach

1. Build an enablement catalogue. List candidate capabilities per app and role: record and meeting summaries and email drafting for sellers, case summaries and grounded reply drafts for service agents, work order summaries for field technicians and dispatchers, content and journey assistance for marketers, plus any prebuilt or custom agents. For each, record the outcome sought, users, data sources, prerequisites, licensing question, release status (generally available or preview, per current Microsoft Learn documentation) and decision.
2. Check data readiness per capability. Are the fields Copilot reads populated? Are emails and meetings tracked against the right records? Are knowledge articles current, owned and free of duplicates? Fix the data problems that matter for the first wave before enabling it, and log the rest.
3. Check security trimming. For Dataverse data, Copilot works within the user's privileges, so review roles with organisation-wide read access before enablement. External knowledge sources (SharePoint sites, websites, uploaded files) bring their own permission models, and some may not be trimmed per user; check each source and what an agent can return from it.
4. Configure prerequisites. Work through the Copilot settings in the Power Platform admin center and each app, data movement consent where needed, and audit or transcript settings. Keep preview features out of production unless a recorded decision accepts the risk.
5. Pilot with a small group per role. Capture a baseline first (time to wrap up a case, time to prepare for a customer meeting), run for long enough to see real use, collect feedback on wrong or unhelpful output, and judge results in aggregate. Expand only when the pilot shows value and no unresolved risk.
6. Govern agents separately. For each agent define its scope, its autonomy (suggest, act with approval, act alone), the actions and data it can reach, the identity it runs under, escalation to a person, and how it is switched off. Every agent goes through `data-and-ai:responsible-ai-review` before production.
7. Keep it current. Microsoft ships Copilot changes through release waves and more frequent updates, so review the catalogue each wave, re-run readiness for anything new, and track consumption where capabilities draw on capacity.

## Outputs

- Copilot and agent enablement catalogue with role, outcome, prerequisites, licensing question, status and decision.
- Readiness assessment covering data quality, knowledge, security and admin settings.
- Pilot plan with baseline, success measures and feedback route.
- Rollout plan and training input to the `training-and-communications-plan`.
- Licensing questions log, each answer confirmed with the Microsoft licensing guide or your partner.
- Risks such as preview dependencies, data quality and licensing in the `raid-log`.

## Scale notes

### SMB

One consultant usually leads, often with one app in scope. Enable a few capabilities with obvious value, such as summaries and email drafting, after a short data and security check, and pilot with a handful of willing users before everyone. Do not skip the licensing confirmation or the responsible AI review just because a feature is built in.

### Enterprise

An AI enablement lead coordinates module workstreams, the platform team and the organisation's AI governance function. Expect a catalogue under change control, staged enablement through environments, a responsible AI review per use case, agents with named business owners, and value measures reported to the steering committee each release wave.

## Hand-offs

- `sales:copilot-in-sales` and `customer-service:service-agents-and-copilot` configure module capabilities.
- `customer-service:knowledge-management` improves knowledge readiness.
- `platform-engineering:copilot-studio-agents` builds custom agents.
- `platform-administration:agent-governance` and `platform-administration:licensing-and-capacity` own operation and capacity.
- `change-adoption:role-based-training` and `change-adoption:adoption-metrics` support rollout.
- Reviews: `data-and-ai:responsible-ai-review` per use case, and `security-compliance:security-model-review` for over-broad access found during readiness.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Enable Copilot in production before checking that security roles do not over-share.
- Switch on preview features in production without a recorded decision.
- State that a capability is covered by current licences without confirming with the Microsoft licensing guide or your partner.
- Use Copilot usage or interaction data to assess or rank individual users.
- Deploy an agent that can change records without a named owner, a defined scope and a way to switch it off.
