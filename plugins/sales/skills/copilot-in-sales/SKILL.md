---
name: copilot-in-sales
description: Plans Copilot enablement for sellers in Dynamics 365 Sales and in Outlook and Teams, covering use cases, data readiness, security, admin settings, piloting and measuring value. Use when a customer wants Copilot for the sales team, asks why summaries or drafts are poor, or needs a readiness check before AI features are switched on.
license: CC-BY-4.0
metadata:
  department: sales
  stages: Strategize, Implement, Prepare, Operate
  modules: Sales
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Copilot in Sales

Copilot features for sellers summarise records, draft emails, prepare for meetings and highlight what changed in the pipeline. They are only as useful as the data and security model they read from: a Copilot asked to summarise an opportunity with no notes, stale close dates and duplicate contacts will produce confident, unhelpful answers.

Projects go wrong by treating Copilot as a switch at the end of the project, with no data readiness work and no agreement on what sellers should use it for, or by enabling everything for everyone at once and spreading a weak first impression across the whole team. Product names and packaging in this area change often, so always check current Microsoft Learn documentation.

## When to use

- Assessing whether a Dynamics 365 Sales environment is ready for Copilot for sellers.
- Planning which Copilot capabilities to enable, for whom and in what order.
- Connecting the seller Copilot experience in Outlook and Teams to CRM data.
- Diagnosing poor summaries, drafts or suggestions.
- Defining how the sales team will measure value from Copilot.

Not this skill: `data-and-ai:copilot-and-agent-enablement` for the organisation-wide Copilot and agent programme, `platform-engineering:copilot-studio-agents` for building custom agents, `sales:outlook-and-teams-integration` for email and calendar synchronisation itself.

## Questions to ask first

1. Which seller tasks should Copilot help with first? A short list of named use cases, such as meeting preparation, email drafting and record summaries, makes enablement and measurement possible.
2. How good is the data sellers rely on? Notes, activities, contacts and opportunity fields are what Copilot reads, so poor data produces poor output.
3. Is the security model sound? Copilot works within each user's permissions, so oversharing in the security model becomes oversharing in answers.
4. What do the organisation's AI policy and data residency position require? Some features may involve settings or data movement that need an explicit, recorded decision with the DPO.
5. Which licences do sellers hold, and which capabilities do they include? Confirm with the Microsoft licensing guide or your partner.

## Approach

Treat Copilot for sellers as an outcome-led rollout rather than a feature toggle. Agree three to five use cases with sales leadership, check the data each one depends on, enable for a pilot group, and extend only when the pilot shows value.

1. Run a data readiness check. For the pilot's accounts and opportunities, look at email and meeting tracking from Outlook, completeness of key opportunity fields, duplicate accounts and contacts, and whether notes live in the system or in personal documents. Fix the worst gaps first; often that means getting tracking working properly.
2. Review the security model. Confirm business units, teams and sharing give sellers what they need and nothing more. Field-level security on sensitive fields matters more once a summary can surface them in a sentence.
3. Settle governance. Record the AI policy position, data residency choices and any settings that move data across geographies, take them through `data-and-ai:responsible-ai-review`, and check them with the DPO. Decide who may switch on new Copilot features as they arrive in release waves.
4. Configure the experiences. In the Sales app, enable the capabilities agreed for the pilot through the admin and app settings; in Outlook and Teams, connect the seller experience to Dynamics 365 and decide which fields it may show and update. Check current Microsoft Learn documentation for the current admin locations and defaults, which move between releases.
5. Pilot with willing sellers. Choose a group with reasonable data and a manager who will use the output in pipeline reviews. Collect examples of good and poor output and trace each poor one back to a data or configuration cause.
6. Measure value at team level. Use usage telemetry, time saved on the agreed tasks and seller feedback, aggregated by team, with measures agreed with sales leadership before the pilot starts.
7. Extend in waves, refreshing guidance with real examples from the pilot.

Keep a short register of what is enabled, for whom and why, and review it every release wave, because Microsoft adds and renames Copilot capabilities frequently.

## Outputs

- Copilot use case list with success measures agreed with sales leadership.
- Data readiness assessment and remediation actions for the pilot scope.
- Enablement register: capabilities enabled, user groups, settings and decision owners.
- Responsible AI and data residency decisions, logged in the `raid-log`.
- Seller guidance with worked examples in the `training-and-communications-plan`.

## Scale notes

### SMB

A small sales team can pilot with everyone, but the readiness check still matters: switch on email tracking and tidy duplicates before enabling Copilot. The consultant usually configures the settings with the business owner in one session. Do not skip the AI policy conversation; even a small organisation needs a recorded decision on data residency and acceptable use, checked with whoever acts as DPO.

### Enterprise

Expect Copilot for sellers to sit inside a wider AI programme with a central governance board, so align with `data-and-ai:copilot-and-agent-enablement` and `platform-administration:agent-governance`. Run pilots per region or segment, track settings per environment, and include Copilot behaviour in regression testing after each release wave. Agree team-level measures with works councils or employee representatives where they exist.

## Hand-offs

`data-and-ai:copilot-and-agent-enablement` owns the organisation-wide approach, `data-and-ai:responsible-ai-review` reviews use cases and risks, and `platform-administration:agent-governance` manages settings across environments. `security-compliance:security-model-review` must confirm access before rollout. Custom agents for sellers go to `platform-engineering:copilot-studio-agents`, and seller training to `change-adoption:role-based-training`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Enable Copilot for all sellers before a data readiness check and a pilot.
- Use Copilot usage data to assess or rank individual sellers.
- Switch on features that move data across geographies without a recorded decision and DPO input.
- Promise specific Copilot capabilities or licence entitlements without checking current Microsoft Learn documentation and the Microsoft licensing guide.
