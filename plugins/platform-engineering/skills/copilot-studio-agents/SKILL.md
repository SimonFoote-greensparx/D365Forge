---
name: copilot-studio-agents
description: Guides building custom Copilot Studio agents grounded in Dataverse knowledge for Dynamics 365 CE, covering scope, knowledge selection, authentication, actions, orchestration, ALM and testing. Use when designing or building an agent over CRM data, adding agent actions that write to Dataverse, or preparing an agent for release.
metadata:
  department: platform-engineering
  stages: Implement, Prepare, Operate
  modules: All
  status: draft
---

# Copilot Studio agents

Copilot Studio makes it quick to build an agent that answers questions from Dataverse tables, knowledge articles and documents, and takes actions through flows and connectors. On a CRM project that puts agents very close to customer data, which is exactly why they need the same engineering discipline as any other component: scoped data, proper authentication, solutions, pipelines and tests.

Agents usually go wrong in three ways. They are pointed at whole tables and answer questions they should not, they run with the maker's credentials so every user sees what the maker sees, or they are built and edited directly in production with no record of what changed.

## When to use

- Building a custom agent that reads Dynamics 365 CE data or knowledge articles.
- Adding actions that create or update Dataverse records from an agent.
- Moving an agent from prototype to a governed, tested release.
- An agent gives wrong, ungrounded or over-sharing answers.

Not this skill: `data-and-ai:copilot-and-agent-enablement` for enabling Microsoft's built-in copilots and agents, `customer-service:service-agents-and-copilot` for Customer Service copilot features, `platform-administration:agent-governance` for maker policies and DLP, and `data-and-ai:responsible-ai-review` for the responsible AI assessment.

## Questions to ask first

1. Who will use the agent, staff or customers? Audience decides authentication, channels and how much data exposure is tolerable.
2. Which tables, columns and articles does it genuinely need? Narrow knowledge gives better answers and a smaller risk surface.
3. Should it only read, or also act? Write actions need validation, confirmation and least-privilege connections.
4. Which channels will it be published to, and is there a human hand-off? Teams, a public website and Dynamics 365 Contact Center each carry different requirements.
5. How will its consumption be paid for? Agent usage is billed differently from user licences; confirm with the Microsoft licensing guide or your partner.

## Approach

1. Define a narrow job. Write down the agent's purpose, audience, in-scope and out-of-scope questions, and success measures. Collect real example questions from the people who will use it.
2. Curate knowledge. Select Dataverse tables and columns deliberately rather than whole tables, and make sure table and column names and descriptions are meaningful, because the agent relies on them. Prefer published knowledge articles over raw notes or email bodies, and clean up duplicate or stale content before connecting it.
3. Authenticate as the user where data varies by user. End-user authentication lets Dataverse security roles decide what each person can see. Avoid maker-provided connections for data that should be filtered per user, and check current Microsoft Learn documentation for how each knowledge source and connector honours permissions.
4. Choose orchestration per path. Generative orchestration works well for open questions when topics, tools and knowledge sources have clear descriptions. Use explicit topics for regulated or transactional paths such as identity checks, complaints or refunds, where the steps must be predictable.
5. Wrap every action. Route writes through flows or custom APIs that validate inputs, ask the user to confirm before changing data and log what was done. Give each action only the privileges it needs.
6. Engineer the lifecycle. Build in a development environment inside a solution, with connection references and environment variables, and deploy through the same pipeline as the rest of the solution. Do not edit agents in production.
7. Test and measure. Keep a test set of questions with expected answers, including out-of-scope and adversarial prompts, and rerun it on every change. After release, review analytics for unanswered and escalated conversations and feed the gaps back into knowledge.

## Outputs

- An agent specification covering purpose, audience, knowledge sources, actions, channels and hand-off.
- A test question set with expected answers and results for each release.
- The agent's solution and deployment settings, recorded in the `environment-and-alm-strategy`.
- A submission pack for governance, security and responsible AI review.

## Scale notes

### SMB

Start with one internal agent over a small set of tables or articles, published to Teams, before anything faces customers. Do not skip end-user authentication or the test question set, even for a pilot.

### Enterprise

Run agents as products with a business owner, a backlog and a release cycle. Share common components (authentication, logging, hand-off topics) across agents, require security and responsible AI review before any external publication, and monitor consumption against the capacity bought.

## Hand-offs

`platform-administration:agent-governance` registers and governs the agent, `data-and-ai:responsible-ai-review` assesses it, `platform-engineering:deployment-pipelines` releases it, and `customer-service:knowledge-management` owns article quality. Reviewer sign-off: `security-compliance:security-model-review` for data access, and `design-authority:design-review` for agents that write data.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Publish an agent to customers without end-user authentication when it can reach personal or account data.
- Give an agent write actions without input validation and user confirmation.
- Point an agent at whole Dataverse tables without choosing which columns it may use.
- Build or edit agents directly in production outside a solution.
- Release an agent without a repeatable test set and a responsible AI review.
