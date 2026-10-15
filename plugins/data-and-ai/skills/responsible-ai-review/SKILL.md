---
name: responsible-ai-review
description: Reviews each Copilot or agent use case against the Microsoft responsible AI principles, covering human oversight, customer transparency, failure handling and data protection hand-offs. Use when an AI feature or agent is heading for production, an agent will talk to customers, or AI will process personal data.
license: CC-BY-4.0
metadata:
  department: data-and-ai
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Responsible AI review

AI in a CRM touches customers directly. It drafts the email they receive, answers them in chat, summarises their complaint for the next agent and scores their enquiry. A responsible AI review asks, before go-live, who could be harmed if it gets something wrong and what stops that happening. Projects skip it because the features come from Microsoft, but the use case, the data, the configuration and the process around it are the organisation's choices, and so is the accountability.

The review should be proportionate. A summary a seller reads before a call needs a short check; an agent that answers customers or changes records needs a full one.

## When to use

- Before a Copilot feature or agent reaches production, and whenever its scope, data or autonomy changes.
- When an AI system will interact with customers or prepare decisions about them.
- When AI processes personal data, special category data or data about customers in vulnerable circumstances.

Not this skill: `data-and-ai:copilot-and-agent-enablement` for rollout planning, `platform-administration:agent-governance` for governing agents in operation, `security-compliance:security-model-review` for access controls and data protection review.

## Questions to ask first

1. Does the AI suggest to a user, draft for approval, or act and reply without a person? Autonomy sets the depth of the review.
2. Who is affected if output is wrong, biased or inappropriate, and how badly? Customer-facing and decision-shaping uses carry more risk than internal summaries.
3. What data does it read and produce, and does that include personal or sensitive data? This decides whether a data protection impact assessment may be needed, which the organisation's DPO or legal adviser determines.
4. Will customers know when they are dealing with AI or AI-drafted content? Expectations and, in some jurisdictions, obligations apply; confirm with the organisation's DPO or legal adviser.
5. Who owns the use case and can switch it off? Accountability needs a named role, not a project team.

## Approach

Review each use case against the six Microsoft responsible AI principles and record a finding against each.

1. Fairness. Could outputs treat groups of customers differently, for example in scoring, prioritisation, routing or the tone of drafted replies? Look at which inputs drive the output, test with varied realistic samples, and remove inputs that act as proxies for personal characteristics.
2. Reliability and safety. Test with realistic, awkward and adversarial inputs: out-of-scope questions, missing data, and instructions hidden in customer-supplied text such as emails and chat messages. Define what happens on failure, such as handing to a person or giving a safe default response.
3. Privacy and security. Confirm data minimisation, security trimming of every knowledge source, retention of prompts, transcripts and generated content, and any data movement across geographies. Pass these to security-compliance rather than concluding on them here.
4. Inclusiveness. Check accessibility of AI-driven experiences, language coverage, and that customers who do not want to deal with an agent can reach a person easily.
5. Transparency. Tell customers when they are talking to an AI agent and how to reach a person. Make it clear to staff which content is AI-generated and, where the feature allows, which sources it drew on.
6. Accountability. Name the business owner, the oversight model, the change control route, the monitoring of quality and complaints, and the switch-off procedure.

Design human oversight explicitly. For each use case choose one of three modes: a person reviews every output before it reaches a customer (the default for new customer-facing drafting), a person samples outputs after the fact, or the agent acts alone with monitoring and escalation. Move to a less supervised mode only on evidence from the more supervised one. Make review real rather than a rubber stamp: show sources, make editing easy, and watch aggregate edit and override rates.

Record an outcome per use case: ready, ready with conditions, or not ready, with conditions tracked to closure. This skill frames the review; findings that fall to security-compliance follow that department's blocking and advisory rules, and residual risk is accepted by the executive sponsor or steering committee, not by the delivery team.

Re-review when Microsoft changes the underlying feature in a release wave, when new data sources or actions are added, when the audience widens, and after any incident.

## Outputs

- Responsible AI review record per use case: description, autonomy, findings by principle, conditions, owner and outcome.
- Human oversight design per use case.
- Customer transparency wording and disclosure points, for review by the DPO or legal adviser where required.
- Test evidence for reliability, safety and fairness checks.
- Data protection hand-off note to security-compliance.
- Residual risks and owners in the `raid-log`.

## Scale notes

### SMB

Usually the consultant and the customer's business owner, using a one-page record per use case. Most SMB uses are internal suggestions with a person in the loop, which keeps the review short. Do not skip it for any customer-facing agent or AI-drafted customer communication, and still ask the data protection question.

### Enterprise

An AI governance or responsible AI function usually exists or is forming, and this review feeds it rather than replacing it. Expect a use case register, standard test packs, DPO and legal involvement for customer-facing and decision-shaping uses, sign-off by a review board, and periodic re-review tied to release waves.

## Hand-offs

- `security-compliance:security-model-review` takes the data protection items, including whether an impact assessment is needed; the conclusion belongs to the organisation's DPO or legal adviser.
- `security-compliance:data-retention` sets retention for prompts, transcripts and generated content.
- `platform-administration:agent-governance` monitors agents and owns switch-off in operation.
- `customer-service:service-agents-and-copilot` and `customer-service:digital-and-voice-channels` implement disclosure and hand-to-person routes.
- `programme-management:governance-cadence` brings residual risk to the steering committee.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Deploy a customer-facing agent without telling customers it is AI and offering a route to a person.
- Let an agent take irreversible actions on customer records without a human approval step.
- Treat Microsoft's own responsible AI commitments as a substitute for reviewing the organisation's use case.
- Use AI outputs to assess, rank or discipline individual employees.
- Give a legal or data protection conclusion instead of routing the question to the DPO or legal adviser.
