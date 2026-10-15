---
name: queues-and-routing
description: Designs how cases and conversations reach the right agent in Dynamics 365 Customer Service, choosing between basic queues and unified routing and shaping workstreams, classification and assignment rules, capacity and presence. Use when setting up queues, choosing push or pick, or fixing stranded or misrouted work.
metadata:
  department: customer-service
  stages: Initiate, Implement, Operate
  modules: Customer Service
  status: draft
---

# Queues and routing

Routing is where the service design meets the way people actually work. Get it right and work arrives with the agent best placed to handle it, supervisors can see the backlog, and nothing waits unnoticed overnight. Get it wrong and agents cherry-pick easy cases, urgent items sit in a queue nobody watches, and supervisors spend their day reassigning by hand.

Projects usually go wrong by copying the org chart into queues, by switching on unified routing without agreeing capacity and presence with the floor managers, and by routing on data that is not reliably captured at intake. The other common failure is the missing fallback: rules that work in testing but leave unmatched items stranded in production.

## When to use

- Choosing basic queues or unified routing, and push or pick distribution.
- Designing the queue catalogue, membership and ownership.
- Designing workstreams, classification rules, route-to-queue rules and assignment methods.
- Setting capacity profiles, presence and skill-based routing.
- Designing overflow, out-of-hours and fallback behaviour, or diagnosing misrouted work.

Not this skill: `customer-service:digital-and-voice-channels` for configuring chat, messaging and voice channels, `customer-service:email-to-case` for turning email into cases, `customer-service:slas-and-entitlements` for timers and escalation deadlines, `security-compliance:business-units-and-teams` for record ownership and access.

## Questions to ask first

1. Do agents pick work from shared lists, or must the system push work to them? Push distribution needs unified routing; pure pick-from-queue can work well with basic queues.
2. Which channels are in scope now and in later releases? Mixing cases with real-time conversations is when capacity and presence start to matter.
3. What decides who should handle an item: product, language, customer tier, region or declared skill? Each becomes a routing attribute that must be populated at intake.
4. How are teams staffed, and do agents work across several queues? This shapes capacity profiles and whether skill-based routing repays its upkeep.
5. What should happen when nobody is available or a queue backs up? Overflow and fallback design is what keeps work from being stranded.

## Approach

The first decision is the routing engine. Basic queues let agents pick and supervisors assign manually, and remain a sound choice for a small back-office team that works cases in order. Unified routing pushes work to agents using rules, capacity and presence, and is the route for real-time channels, skill-based assignment and larger operations. Check current Microsoft Learn documentation for the status of legacy routing rule sets and for which features require unified routing; whether your licences cover it is a question to confirm with the Microsoft licensing guide or your partner.

### Structure

1. Design queues around work, not people. A queue is a pool of work that a group of agents can take interchangeably, such as billing enquiries in French. Avoid a queue per person and resist mirroring the org chart. Give every queue an owner, operating hours and a decision on whether it is public or private.

2. Separate classification from assignment. In unified routing, intake rules decide which workstream a record enters, the workstream sets the channel and distribution mode, classification rules enrich the item (priority, language, required skills), route-to-queue rules pick the queue and assignment rules pick the agent. Keeping these layers apart lets you change one without breaking the others.

3. Make routing data trustworthy. Every attribute a rule uses must be set at intake by the form, the channel, the email-to-case rule or a classification rule. If customer tier is unreliable in the data, do not route on it until it is fixed.

### Distribution

4. Choose assignment methods per queue. Highest capacity, round robin and custom prioritisation each suit different work. Start simple, usually round robin or highest capacity with priority ordering, and add custom rules only when a measured problem justifies them.

5. Agree capacity and presence with the floor. Capacity profiles define how much of each kind of work an agent can hold at once, and presence decides when work flows. Agree what each presence status means operationally, otherwise work piles up on someone who is in training.

6. Use skill-based routing only where skills are maintained. Skills and proficiency must be declared and kept current by a named owner from training and certification records. Exact-match rules on a neglected skill matrix strand work.

### Safety nets

7. Design overflow and fallbacks. Every queue needs out-of-hours behaviour, an overflow action and a fallback queue that someone monitors. Test the no-agent-available, agent-declines and nothing-matched paths explicitly.

8. Trace before go-live. Load a test environment with realistic volumes and agent rosters, use the routing diagnostics to explain each decision, and keep a short routing decision log so supervisors can answer why an item went where it did.

## Outputs

- Routing design (engine choice, workstreams, rules, overflow) in the `solution-blueprint`.
- Queue catalogue with owner, type, membership, operating hours and fallback queue.
- Routing rule matrix showing each attribute, where it is set, the rule and the target queue.
- Capacity profiles and presence definitions agreed with operations.
- Skill model structure and its owner, based on declared skills only.
- Routing scenarios, including no-match and out-of-hours paths, in `test-strategy-and-uat-scripts`.
- Supervisor guidance in the `training-and-communications-plan`.

## Scale notes

### SMB

Basic queues are often enough: a handful of queues, agents pick, a supervisor reassigns. If chat or voice brings in unified routing, keep one workstream per channel and a simple assignment method until evidence says otherwise. Do not skip queue ownership, out-of-hours behaviour and a daily check of unassigned work.

### Enterprise

Routing becomes an operational capability with a named owner, often a routing or workforce analyst in the service operation. Rule changes go through change control and are tested outside production with production-like data; check current Microsoft Learn documentation for which routing components travel in solutions, and script or document the rest as configuration steps. Align queue membership with business units and teams, and coordinate with any workforce management tool on schedules and adherence data.

## Hand-offs

- `customer-service:digital-and-voice-channels` adds channel workstreams on top of this design.
- `customer-service:service-analytics` takes queue and routing measures.
- `platform-engineering:deployment-pipelines` moves routing configuration between environments.
- Reviewer sign-off: `design-authority:design-review` for the routing design, and `security-compliance:business-units-and-teams` for queue membership and visibility.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create a queue per agent to imitate a personal work list.
- Route on attributes that are not reliably populated at intake.
- Use personal characteristics, or rankings of individual agents, to drive assignment.
- Go live without a monitored fallback queue and out-of-hours behaviour.
- Change production routing rules without testing them in another environment first.
