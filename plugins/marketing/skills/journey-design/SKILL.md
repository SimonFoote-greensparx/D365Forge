---
name: journey-design
description: Designs real-time journeys in Customer Insights - Journeys, covering trigger and segment entry, custom triggers, branching, waits, goals, exit and re-entry rules, testing and go-live. Use when planning a welcome, nurture, onboarding, renewal or event journey, choosing triggers, or moving journeys off older outbound marketing.
license: CC-BY-4.0
metadata:
  department: marketing
  stages: Initiate, Implement, Operate
  modules: Marketing
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Journey design

Journeys are where marketing intent becomes automated customer contact, so design errors reach customers directly and at scale. Customer Insights - Journeys uses real-time journeys as its current approach: a journey starts from a trigger (something a customer or system did) or from a segment, then moves each person through messages, waits and branches. Older outbound marketing journeys work differently; check current Microsoft Learn documentation for their status before designing anything on them.

Projects go wrong by drawing ambitious journey diagrams before the triggers, data and consent model exist, or by building many overlapping journeys that contact the same person several times a week. A journey should have one purpose, one audience and a measurable goal.

## When to use

- Designing a new journey: welcome, onboarding, nurture, renewal, event or re-engagement.
- Choosing between trigger-based and segment-based entry, and defining custom triggers.
- Setting branches, waits, exits, goals and re-entry rules.
- Planning journey testing, approval and go-live.
- Moving journeys from outbound marketing to real-time journeys.

Not this skill: `marketing:segments-and-audiences` for building the audience, `marketing:email-and-sms-channels` for message content and channel setup, `sales:sequences-and-sales-accelerator` for one-to-one seller cadences.

## Questions to ask first

1. What is the journey's business goal, and how will success be measured? The goal decides the exit rule and stops journeys running on autopilot.
2. What starts the journey: a customer action, a system event or membership of a segment? This decides between a built-in trigger, a custom trigger from Dataverse or another system, and a segment.
3. Which consent purpose applies to each message? Messages that part of the audience cannot receive change the shape of the journey.
4. What other journeys or sales activity could reach the same people? Overlap needs frequency rules or exclusions.
5. Who approves a journey before it goes live? Testing and approval must be agreed before the first journey is built.

## Approach

Design on paper before the canvas. Write a one-page journey brief for each journey covering purpose, audience, entry, messages, decisions, exit, goal and the consent purpose each message relies on. Most design flaws show up when that brief is reviewed with sales and the data owner.

1. Choose the entry deliberately. Use a trigger when timing matters, such as a form submission, a purchase recorded in Dataverse or an event registration. Use a segment when the audience is defined by attributes and the timing is a campaign decision. Custom triggers let other systems or Power Automate start journeys, but each needs an owner and a documented payload.
2. Keep the canvas shallow. Use attribute branches and waits only for genuinely different paths, and split long programmes into linked journeys. A journey that has to be zoomed out to be read will not be maintained.
3. Set exit and goal rules. Exit people when they reach the goal, become sales-ready, unsubscribe or stop being eligible, and decide whether and when they may re-enter.
4. Coordinate contact frequency. Agree with other journey owners and sales how many marketing messages a person may receive in a period, then use the platform's frequency and quiet-time controls where they exist; check current Microsoft Learn documentation for what applies to your release.
5. Hand over to sales inside the journey. Where a journey detects buying interest, update a score, create or update a lead or raise a task for the owner rather than sending yet another email, and make sure the journey context is visible to the seller.
6. Test with realistic data outside production. Use test contacts that cover each branch, consent state and language, and confirm triggers fire from the real source system. Then run a controlled live test with internal recipients.
7. Govern after launch. Review journey analytics against the goal, retire journeys that no longer serve it, and keep a register of live journeys and their owners.

When moving from outbound marketing, redesign rather than copy. The trigger-led model often replaces several scheduled journeys with one.

## Outputs

- Journey brief for each journey: purpose, audience, entry, steps, consent purpose, exit and goal.
- Trigger catalogue with owners, sources and payloads.
- Contact frequency rules agreed across marketing and sales.
- Journey test scenarios in the `test-strategy-and-uat-scripts`.
- Live journey register with owners and review dates.

## Scale notes

### SMB

A small marketing team, often one marketer with part-time consultant help, should start with two or three journeys such as welcome, event follow-up and re-engagement. Use built-in triggers and simple segments, and keep approval to one named reviewer. Do not skip the consent check and the internal live test before each journey goes live.

### Enterprise

Expect journey standards owned by marketing operations, shared trigger and content conventions, approval workflows, and several brands or regions. Custom triggers from other systems need integration design and testing, and journey templates should be reused across regions. Any journey that introduces a new consent purpose or audience source goes through `security-compliance:marketing-consent-compliance` before launch.

## Hand-offs

`marketing:segments-and-audiences` provides audiences, `marketing:email-and-sms-channels` supplies messages, and `marketing:lead-scoring-and-sales-handoff` defines when a journey passes a person to sales. Custom triggers raised from flows go to `platform-engineering:power-automate-patterns`, and acceptance testing to `testing-quality:user-acceptance-testing`. Journeys need `security-compliance:marketing-consent-compliance` sign-off before going live.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Launch a journey without a defined goal, exit rule and owner.
- Copy outbound marketing journeys step for step into real-time journeys.
- Send marketing messages from a journey without checking the consent purpose for each message.
- Sign off a journey tested only with internal records that bypass the real triggers and consent states.
