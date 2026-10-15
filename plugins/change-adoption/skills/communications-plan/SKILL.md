---
name: communications-plan
description: Plans change communications for a Dynamics 365 CE rollout by audience, message, sender, channel and timing, from early awareness through go-live and hypercare into release waves, with a feedback loop. Use when drafting the communications calendar, writing go-live announcements, or deciding who should send which message to which group.
metadata:
  department: change-adoption
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
---

# Communications plan

Users decide whether a new CRM is worth their time long before they sit in a training room. If the first thing they hear is a launch email in go-live week, sent by IT and describing an exciting new system, the programme has already lost the argument. A communications plan makes sure each group hears why the change matters to them, what will change in their working day, and when, from someone they trust.

Typical failures are generic messages that could describe any system, every message coming from the project team rather than business leaders, no route for questions, and silence after go-live just when users most need reassurance that their feedback is being acted on.

## When to use

- At Initiate, to set up the plan and the first awareness messages.
- Through Implement and Prepare, to schedule role-specific messages, training invitations and cutover notices.
- At go-live and during hypercare, for launch, help and known-issue updates.
- In Operate, for release wave changes and adoption follow-up.

Not this skill: `change-adoption:stakeholder-analysis` for who is affected and how, `change-adoption:role-based-training` for training content and scheduling, `support-operations:hypercare` for the hypercare operating model.

## Questions to ask first

1. What does each audience gain and lose? The message comes from the impact assessment, not from the feature list.
2. Whom do people in each group trust to hear from? Business change lands better from sponsors and line managers than from the project.
3. Which channels actually reach front-line roles, such as technicians away from a desk or agents on shifts? Email alone rarely reaches them.
4. Which dates are fixed: go-live, training windows, data cut-off, legacy read-only date? Users need the dates that change their behaviour.
5. How will questions and feedback be collected and answered? A one-way plan misses resistance until it is too late.

## Approach

Plan by phase, so that the content matures as the system does.

1. Awareness, during Strategize and Initiate. Why the organisation is changing, which outcomes it expects, and what this means at a high level. Sent by the sponsor.
2. Understanding, during Implement. What changes for each role, shown with real screens from sprint reviews as early as possible. Delivered largely through line managers.
3. Readiness, during Prepare. Training invitations, requests to tidy legacy data, cutover dates, when the legacy system becomes read-only, and where to get help.
4. Go-live. Launch message, help routes, super-user contacts and a daily known-issues update during hypercare.
5. Reinforcement, in Operate. Early wins, practical tips, aggregate adoption progress, responses to feedback, and what each release wave changes by role.

For each item record audience, objective, key message, sender, channel, date, owner, feedback mechanism and status. Brief line managers before their teams hear anything, with a short pack that includes likely questions and answers.

Make messages specific. "From the go-live date, new service requests are logged as cases in Dynamics 365, and the old system becomes read-only for reference" tells people what to do; "an exciting new platform is coming" does not. Repeat key dates across several channels.

Build two-way routes in from the start: a Teams channel or community space, a maintained FAQ, questions collected through super users, and short pulse surveys reported in aggregate. Close the loop by publishing what changed because of feedback.

Where customers are affected, for example a new portal, changed email footers or updated privacy and consent wording, coordinate with marketing and have the DPO or legal adviser approve the wording.

Keep the communications calendar and the training schedule in one combined plan so that invitations, reminders and cutover notices never contradict each other.

## Outputs

- The communications section of the `training-and-communications-plan`, with calendar.
- A message framework by audience and phase.
- Manager briefing packs and an FAQ.
- Go-live and hypercare announcements, and a feedback log.

## Scale notes

### SMB

One owner, often the sponsor, with consultant support. A few well-timed messages and team meetings are usually enough. The minimum is why the change is happening, what changes for each role, the key dates and where to get help.

### Enterprise

A change or communications lead works with internal communications, with localisation and translation where needed. Channels are planned per audience, messages go through an approval route, and reach is measured in aggregate. Phased rollouts need a separate message sequence per wave.

## Hand-offs

- `change-adoption:role-based-training` aligns training invitations with the calendar.
- `change-adoption:super-user-network` relays messages and collects questions.
- `support-operations:hypercare` supplies known-issue updates after go-live.
- `programme-management:go-no-go` checks communications readiness as a criterion.
- Reviewer sign-off: customer-facing consent or privacy wording goes to `security-compliance:marketing-consent-compliance` and the DPO.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Send the first meaningful message in go-live week.
- Promise features or dates that the delivery plan has not confirmed.
- Use message read or engagement data to single out individuals.
- Change customer-facing privacy or consent wording without the DPO or legal adviser.
