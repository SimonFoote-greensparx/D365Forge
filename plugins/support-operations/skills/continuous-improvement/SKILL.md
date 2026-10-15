---
name: continuous-improvement
description: Runs the post-go-live improvement cycle for Dynamics 365 CE with one prioritised backlog, a release cadence aligned to Microsoft release waves, adoption feedback loops and value reporting to the sponsor. Use when setting up the backlog after hypercare, agreeing a release rhythm, or deciding what to improve next.
metadata:
  department: support-operations
  stages: Operate
  modules: All
  status: draft
---

# Continuous improvement

Go-live is the start of the system's working life, not the end of its value. Deferred scope, user requests, hypercare findings, adoption problems and new Microsoft capabilities all compete for attention. Without a structure the system either freezes, so nothing changes and users drift away, or sprawls, so every request is built, technical debt grows and release waves start breaking things.

Continuous improvement gives the service owner a steady rhythm: one backlog, prioritisation tied to business outcomes, a predictable release cadence, and feedback loops from users and from Microsoft's roadmap.

## When to use

- Setting up the improvement backlog as hypercare ends.
- Agreeing how requests are prioritised and by whom.
- Setting a release cadence that fits Microsoft's release waves.
- Deciding which customisations to retire as standard features arrive.
- Reporting value delivered to the sponsor.

Not this skill: `change-adoption:adoption-metrics` for defining and measuring adoption, `platform-administration:release-readiness` for preparing each Microsoft release wave, `design-authority:change-impact-assessment` for assessing a specific change, and `support-operations:incident-management` for live issues.

## Questions to ask first

1. Who owns the backlog and decides priorities after go-live? Without a product owner with authority, the loudest request wins.
2. What capacity is funded for improvement, internal or partner? The cadence must match the capacity, not the wish list.
3. Which business outcomes and success measures were set at the start? Prioritisation should tie back to them.
4. How do users give feedback today? If the only channel is the incident queue, improvement ideas get lost among faults.

## Approach

1. Create one backlog. Bring together deferred scope, change requests from hypercare, problem fixes, user ideas, technical debt and items arising from release waves. Each item carries a short case: the outcome it supports, who benefits, and a rough size.
2. Prioritise in the open. Use a simple published method (value against effort, with compliance and supportability items first) and review priorities with business representatives on a fixed rhythm. People accept a declined request far more readily when they can see why.
3. Set a release cadence. A predictable rhythm (for example monthly) lets the business plan around changes. Every release goes through the pipeline with regression testing and release notes. Leave room around Microsoft's twice-yearly release waves for early access testing and for adopting features that replace custom work.
4. Retire customisation. Each release wave review should ask which custom components are now covered by standard features. Removing customisation counts as improvement, and it shrinks future regression effort.
5. Close the feedback loop. Gather feedback through super-users, in-app channels and usage data. Compare adoption with the outcomes in the original business case, and treat low use of a feature as a backlog item (redesign, retrain or remove), not only as a training problem.
6. Govern change. Changes that alter the data model, security, integrations or signed-off design go through `design-authority:change-impact-assessment` before they enter a release.
7. Report value. Give the sponsor a short regular report: what was released, what it changed for users, adoption trends, and what comes next. This is what keeps improvement funded.

Keep the backlog honest. Items that have sat untouched for several review cycles should be closed with a reason, so the list reflects real intent.

## Outputs

- Prioritised improvement backlog with outcome-based cases.
- Release calendar aligned to Microsoft release waves.
- Release notes and user communications, drawing on the `training-and-communications-plan`.
- Customisation retirement list.
- Value and adoption report for the sponsor.

## Scale notes

### SMB

The backlog is often a simple list owned by the business system owner, with the partner delivering small releases on a regular schedule under a support or retainer contract. Do not skip the release wave review; small teams are the most exposed to features changing underneath them.

### Enterprise

Expect product owners per module, design authority review of significant change, a release train across modules with shared regression, benefits realisation tracked against the original business case, and prioritisation alongside other Power Platform workloads at portfolio level.

## Hand-offs

- `design-authority:change-impact-assessment` reviews significant changes before they are scheduled.
- `business-analysis:user-stories` refines backlog items ready for build.
- `testing-quality:regression-automation` keeps the regression pack current with each release.
- `platform-administration:release-readiness` aligns the cadence with each release wave; `change-adoption:adoption-metrics` and `change-adoption:communications-plan` support feedback and release communications.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Build every user request without prioritising it against business outcomes.
- Release changes outside the pipeline or without regression testing.
- Ignore new standard features that could replace existing customisation.
- Let the backlog become a private list held only by the partner.
