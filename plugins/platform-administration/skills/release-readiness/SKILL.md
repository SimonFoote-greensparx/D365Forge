---
name: release-readiness
description: Prepares a Dynamics 365 CE estate for Microsoft updates, covering roadmap tracking on the AI at Work roadmap, release waves and early access, impact assessment, regression testing, feature enablement and user communication. Use when a major update approaches, early access opens, or a roadmap item or deprecation affects the solution.
license: CC-BY-4.0
metadata:
  department: platform-administration
  stages: Prepare, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Release readiness

Dynamics 365 and Power Platform are updated continuously. Most changes are welcome, but some alter screens users know, switch features on automatically, change behaviour that customisations rely on, or deprecate something the solution uses. Organisations that treat updates as Microsoft's business discover the impact in production on a Monday morning.

Release readiness is a rhythm, not a project. It needs someone watching what is coming, a way to judge impact, a sandbox to test in, a regression suite to prove the solution still works and a channel to tell users what has changed.

## When to use

- A major update or release wave is approaching and early access is available.
- A roadmap item, Message center post or deprecation notice may affect the solution.
- Setting up the post-go-live rhythm for tracking and adopting new features.
- Deciding whether to enable a new feature for users.

Not this skill: `testing-quality:regression-automation` for building the regression suite, `change-adoption:communications-plan` for user communications, `design-authority:change-impact-assessment` for formal assessment of significant changes, and `platform-administration:monitoring` for routing Message center posts.

## Questions to ask first

1. Which apps, features and customisations are in use? This is the surface every update is checked against.
2. Is there an automated regression suite, and how long does a full run take? It decides how quickly an update can be validated.
3. When are the business's change freezes and peak periods? Update timing and feature enablement should avoid them.
4. Who decides whether optional features are enabled? Without a named decision-maker, features either drift on by default or are never used.
5. Which ISV products are installed? Each vendor must confirm compatibility with the update.

## Approach

### Know where change is announced

Microsoft has long delivered major Dynamics 365 and Power Platform updates in two release waves a year, each with an early access period in which a sandbox can be switched to the upcoming changes before general deployment, plus smaller service updates in between. Microsoft has now moved roadmap content from the Dynamics 365 release plans to the AI at Work roadmap and publishes new capabilities as they are committed rather than in twice-yearly plan documents, while stating that update schedules themselves are unchanged. Check current Microsoft Learn documentation for the schedule and early access arrangements that apply, and repoint release plan bookmarks and internal pages to the AI at Work roadmap. Message center remains the tenant-specific source for changes and deprecations.

### Run a regular review

Hold a monthly or quarterly review of the AI at Work roadmap, filtered to the products in use, alongside a weekly triage of Message center. Classify each item as enabled automatically for users, enabled by administrators, opt-in, or deprecation, and record the decision and owner in a release readiness log.

### Test before it arrives

For each major update:

1. Copy production to a sandbox and switch it to early access where that is offered. Mask personal data in the copy as agreed with the organisation's DPO or legal adviser.
2. Run the regression suite and the critical UAT scripts, paying particular attention to client scripts, PCF controls, plug-ins on standard messages and ISV components.
3. Ask ISV vendors for compatibility statements.
4. Log defects, raise Microsoft support cases early for platform regressions and fix the solution wherever it relied on changed behaviour.

### Decide and communicate

Agree which optional features to enable, when and for whom, avoiding change freezes. Update training material and job aids, tell users what will look different before it changes, and brief the support team so they recognise update-related calls.

### Track deprecations

Keep a deprecation tracker with removal date, affected components, owner and remediation plan, and treat each deprecation as a backlog item with a deadline.

## Outputs

- A release readiness log of roadmap items and Message center posts with classification, decision and owner.
- Early access test results and a regression report for each major update.
- A deprecation tracker with remediation plans, linked to the `raid-log`.
- User-facing change notes and updated materials in the `training-and-communications-plan`.

## Scale notes

### SMB

Usually the partner or a single administrator handles this. A quarterly roadmap check, a regular read of Message center and a short manual test of critical processes in an early access sandbox are the minimum. Do not skip telling users before visible changes arrive.

### Enterprise

A release manager runs the rhythm with representatives from each workstream, automated regression runs in an early access sandbox and a release readiness board approves feature enablement. Significant changes go through formal change impact assessment, and communications follow the change and adoption plan.

## Hand-offs

`testing-quality:regression-automation` runs the suite, `change-adoption:communications-plan` and `change-adoption:role-based-training` prepare users, and `support-operations:continuous-improvement` picks up new features worth adopting. Reviewer sign-off: `design-authority:change-impact-assessment` for changes that alter the solution design.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Let the first test of a major update happen in production.
- Enable new features for users without assessing the impact and telling them first.
- Leave deprecation notices unactioned until the removal date.
- Treat old release plan bookmarks as the current source of roadmap information.
- Switch production to early access before the update has passed testing in a sandbox.
