---
name: service-agents-and-copilot
description: Plans Copilot and AI service agents in Dynamics 365 Customer Service, starting with knowledge readiness, then agent-assist features, then narrowly scoped autonomous agents with human hand-off and governance. Use when choosing which Copilot features to enable, preparing knowledge sources, or scoping an autonomous service agent.
metadata:
  department: customer-service
  stages: Strategize, Implement, Operate
  modules: Customer Service
  status: draft
---

# Service agents and Copilot

Copilot features and service agents can only ever be as good as the knowledge and data they read. Grounded on current, well-owned knowledge, they shorten handling time and after-contact work; grounded on a stale or contradictory knowledge base, they give confident wrong answers at scale.

Projects usually go wrong by switching features on because they are included, then measuring success by how many agents have them rather than by what changed. The riskier failure is deploying an autonomous agent that can update or close cases without a defined boundary, an owner or a clean route to a human.

## When to use

- Deciding which Copilot capabilities to enable for service agents and supervisors, and in what order.
- Assessing whether knowledge is ready to ground AI features.
- Scoping an autonomous service agent or a custom agent built in Copilot Studio.
- Designing human review, escalation and governance for AI in service.
- Measuring whether AI features are delivering value.

Not this skill: `customer-service:knowledge-management` for the article lifecycle itself, `data-and-ai:copilot-and-agent-enablement` for the cross-module AI enablement plan, `platform-engineering:copilot-studio-agents` for building custom agents, `data-and-ai:responsible-ai-review` for the formal AI assessment.

## Questions to ask first

1. Is the knowledge base current, owned and free of contradictions? Generated answers repeat whatever the sources say.
2. Which tasks cost agents the most time today? Features should target measured pain such as summaries, drafting or finding answers.
3. Is the goal to assist people or to let an agent act on its own? Autonomy changes the risk, the governance and the testing needed.
4. What data may AI features read, where is it processed, and who reviews output? Data location and human review are design decisions, not defaults.
5. Which licences or consumption charges apply to the features in scope? Packaging changes often, so confirm with the Microsoft licensing guide or your partner.

## Approach

Sequence matters more than features: knowledge first, then assistive features for people, then autonomous agents for narrow, well-understood tasks. Microsoft adds and renames Copilot capabilities and service agents frequently, so check current Microsoft Learn documentation for what is available, in which regions, and whether it is generally available or in preview before promising anything.

1. Make knowledge ready. Work with `customer-service:knowledge-management` to retire stale articles, resolve contradictions, set internal and external visibility, and agree which sources AI features may use. Then run a set of real customer questions against those sources and record whether a good answer exists. Where none exists, no feature will invent a reliable one.

2. Start with assistive features. Typical candidates are case and conversation summaries, drafted replies, and question answering grounded in knowledge. Enable them for a pilot group, agree what good output looks like, and collect feedback inside the tool.

3. Keep people accountable. Agents review generated content before it reaches a customer. Train agents on how output can be wrong and what to do about it, and decide whether generated content is labelled or logged.

4. Scope autonomous agents narrowly. Pick one task with clear rules and low harm if wrong, such as enriching and triaging new cases or answering a defined set of questions. Define exactly which records and fields the agent may change, what it must never do, and how it hands over to a person with full context. Build custom agents with `platform-engineering:copilot-studio-agents`.

5. Govern before scaling. Every agent needs an owner, a statement of its permissions, a way to switch it off, monitoring and a review cadence, set up with `platform-administration:agent-governance`. Submit each agent and significant feature to `data-and-ai:responsible-ai-review` before production.

6. Measure outcomes at team level. Agree before-and-after measures with `customer-service:service-analytics`, such as handling and after-contact time, first contact resolution, deflection with a confirmed outcome and agent feedback. Use them to expand, adjust or switch off features.

Generated summaries and transcripts are new stored records containing personal data. Agree their retention and access with `security-compliance:data-retention`, and take questions of lawful basis or cross-border processing to the organisation's DPO or legal adviser.

## Outputs

- Knowledge readiness assessment with the evaluation question set and results.
- AI feature enablement and pilot plan in the `delivery-plan`.
- Agent scope definitions (purpose, permissions, boundaries, escalation, owner) in the `solution-blueprint`.
- Responsible AI review submission.
- Evaluation and hand-off test scenarios in `test-strategy-and-uat-scripts`.
- Agent guidance on reviewing AI output in the `training-and-communications-plan`.

## Scale notes

### SMB

Enable a small set of assistive features after a knowledge clean-up, with one named person watching feedback. Leave autonomous agents until assistive features have shown value. Do not skip knowledge readiness, human review of customer-facing output, or a proportionate responsible AI review.

### Enterprise

Expect a central AI or CoE function, staged rollout by queue or region, formal evaluation sets re-run after each Microsoft release, and data location reviews per region. Where AI changes how agents work, involve HR and, where required, employee representatives early. Agent permissions and changes go through the same change control as other production configuration.

## Hand-offs

- `data-and-ai:copilot-and-agent-enablement` for the programme-wide AI enablement plan.
- `platform-administration:agent-governance` for agent ownership, monitoring and switch-off.
- `change-adoption:role-based-training` for agent and supervisor training.
- Reviewer sign-off: `security-compliance:security-model-review` for agent permissions and data access, and `security-compliance:data-retention` for transcripts and generated content.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Enable generative features over knowledge that has not been reviewed for accuracy and visibility.
- Let an autonomous agent change or close cases without a defined boundary, an owner and a human escalation path.
- Use Copilot interaction data to rank or assess individual agents.
- Promise availability or regional support for an AI feature without checking current Microsoft Learn documentation, or quote its price instead of advising people to confirm with the Microsoft licensing guide or your partner.
