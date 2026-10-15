---
name: digital-and-voice-channels
description: Plans digital messaging and voice channels for customer service with Dynamics 365 Contact Center and the Customer Service workspace, covering chat, SMS and social messaging, telephony provider choice, and call recording and retention as a compliance gate. Use when adding chat or voice or choosing a telephony route.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Strategize, Initiate, Implement, Prepare
  modules: Customer Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Digital and voice channels

Real-time channels change the service operating model. The customer is waiting, agents may handle several conversations at once, presence and capacity suddenly matter, and a bad configuration is felt immediately rather than in tomorrow's backlog. Voice adds carriers, numbers, call flows and recording, each with its own lead times and rules.

Projects usually go wrong by treating channels as a technical add-on switched on late in the build. The telephony route is chosen after number porting lead times have already slipped, recording is enabled because it is available, and the security review then blocks go-live because nobody can say how long recordings are kept or who can play them back.

## When to use

- Deciding which digital and voice channels to offer, and in what order.
- Choosing a telephony route and planning numbers, carriers and call flows.
- Designing the agent experience in the Customer Service workspace for conversations.
- Designing pre-conversation questions, customer identification and conversation-to-case rules.
- Preparing recording, transcription and retention decisions for security sign-off.

Not this skill: `customer-service:queues-and-routing` for workstreams, capacity and assignment, `customer-service:service-agents-and-copilot` for AI assistance and autonomous agents, `platform-engineering:copilot-studio-agents` for building bots, `security-compliance:data-retention` for setting the retention policy itself.

## Questions to ask first

1. Which channels do customers use today, at what times and volumes? This sets channel priority, staffing and the order of rollout.
2. What telephony estate exists: carrier contracts, an incumbent contact centre platform, numbers to port, an IVR? This decides between Microsoft-provided numbers, your own carrier or integrating another platform.
3. Must calls or chats be recorded or transcribed, and for how long kept? Recording is a security-compliance gate, not a toggle.
4. Must customers be authenticated or matched to existing contacts and cases? This shapes pre-chat design and identity matching.
5. Is the contact centre being bought alongside Dynamics 365 Customer Service or with another CRM? This affects the agent workspace, the data model and the licences needed; confirm with the Microsoft licensing guide or your partner.

## Approach

Microsoft's real-time service channels have evolved from Omnichannel for Customer Service into Dynamics 365 Contact Center, with agents working in the Customer Service workspace. Channel lists, regional availability, telephony options and packaging change often, so check current Microsoft Learn documentation before committing to a design, and treat which licences you need as a question to confirm with the Microsoft licensing guide or your partner.

1. Start from the contact reasons. For each reason, decide which channels to offer, whether a bot handles it first, and when it escalates to a person with context. Add channels in waves; one well-staffed chat channel serves customers better than several thinly staffed ones.

2. Choose the telephony route early. The usual options are Microsoft-provided numbers through Azure Communication Services, bringing an existing carrier, or keeping an established contact centre platform and integrating it with the agent workspace. Weigh number porting lead times, carrier contracts, existing IVR investment, regional availability and who supports voice after go-live. Record the decision and its reasons.

3. Design the agent experience. Agree what the agent sees when a conversation arrives (customer, open cases, recent conversations), which productivity tools are on the screen, and when a conversation creates or links to a case, following `customer-service:case-lifecycle-design`.

4. Design pre-conversation and identity. Keep pre-chat questions few and useful for routing. Decide how authenticated customers are identified and how unknown customers are matched to contacts without creating duplicates.

5. Settle routing first. Real-time channels depend on unified routing, presence and capacity; agree them with `customer-service:queues-and-routing` before building channels.

6. Treat recording and transcription as a gate. Recordings, transcripts, sentiment and generated summaries are stored personal data. Before go-live, document what is captured, how callers are told, where it is stored, who can access it, how long it is kept and how it is deleted. This needs sign-off from `security-compliance:data-retention` and `security-compliance:security-model-review`; the lawful basis and caller notice wording go to the organisation's DPO or legal adviser.

7. Plan operations and load. Define operating hours, out-of-hours messages, overflow to callback or voicemail where supported, supervisor monitoring and the support route for telephony faults. Load test with realistic concurrency before launch.

## Outputs

- Channel strategy and rollout waves in the `delivery-plan`.
- Telephony decision record and channel design in the `solution-blueprint`.
- Carrier, telephony and messaging platform connections in the `integration-inventory`.
- Recording, transcription and retention specification submitted for security sign-off.
- Channel and load test scenarios in `test-strategy-and-uat-scripts`.
- Number porting and channel launch steps in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Start with one digital channel, usually chat, and add voice only if the team can staff it. Keep any bot to a few clear intents with an easy route to a person. Do not skip the recording and retention decision or out-of-hours behaviour, and for the licences each channel needs, confirm with the Microsoft licensing guide or your partner.

### Enterprise

Expect several regions, carrier contracts, number porting schedules, IVR migration and a separate telephony support team. Workforce management, quality monitoring and regulated recording requirements usually apply. Run formal load and failover tests, plan channel launches by region, and keep a joint runbook with the telephony provider for incidents.

## Hand-offs

- `customer-service:queues-and-routing` for channel workstreams and capacity.
- `integration-and-data:integration-architecture` where a third-party telephony or contact centre platform is integrated.
- `testing-quality:performance-testing` for concurrency and load tests.
- Reviewer sign-off: `security-compliance:data-retention` and `security-compliance:security-model-review` must clear recording and transcription before go-live, and `design-authority:design-review` reviews the telephony route.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Enable call or chat recording before retention and access have security-compliance sign-off.
- Choose a telephony route without checking porting lead times, carrier contracts and regional availability.
- Launch a channel without staffed hours, out-of-hours behaviour and overflow.
- Assume a channel, region or carrier is supported without checking current Microsoft Learn documentation.
