---
name: project-charter
description: Drafts the project charter and business case for a Dynamics 365 CE programme, tying scope, sponsorship, budget and modules to measurable business outcomes with baselines and owners. Use when starting a CRM programme, seeking funding approval, restating the case after a major scope change, or when nobody can say what success looks like.
metadata:
  department: programme-management
  stages: Strategize, Initiate
  modules: All
  status: draft
---

# Project charter and business case

A Dynamics 365 CE programme is usually approved on a promise such as a single view of the customer or better service, and two years later nobody can show whether it was kept. The charter prevents this. It states why the organisation is investing, which outcomes it expects, how they will be measured, and who decides when scope, budget and date pull against each other. Every later argument about scope comes back to it, so it has to be specific enough to settle those arguments.

Charters go wrong in predictable ways. They list features instead of outcomes, quote benefits that were never baselined, name a sponsor with no authority over the business units affected, or are written by the implementation partner as a preface to its own proposal. A charter the customer did not write is rarely one the customer defends.

## When to use

- At Strategize, before partner selection, a statement of work or any design work begins.
- When funding approval needs a business case that finance will accept.
- When a phase has slipped or scope has changed enough that the original case no longer holds.
- When steering members describe the purpose of the programme differently from each other.

Not this skill: `programme-management:statement-of-work` for the contractual scope agreed with a partner, `programme-management:delivery-plan` for phases and dates, `project-tailoring:profile-intake` for capturing the organisation profile itself.

## Questions to ask first

1. Which business outcomes is the organisation paying for, and how are they measured today? Without a baseline taken before go-live, no benefit can be demonstrated afterwards.
2. Who is the executive sponsor, and which decisions can they make without referring upwards? A sponsor who cannot arbitrate between sales, service and IT cannot protect scope.
3. Which modules and user groups are in the first release, and which are deliberately deferred? This sets the edition, the cost profile and every downstream plan.
4. Of date, budget and scope, which one is fixed? Only one can be held firm, and the charter must say which of the others flexes.
5. What is already decided, such as partner, existing licences, compliance regime and change freezes? These narrow the options before any design starts.

## Approach

Start from the organisation profile if one exists, because its goals section (outcomes, success measures, target go-live, budget band) is the raw material for the charter. Where the profile is thin, run a short working session with the sponsor and the heads of each in-scope business area rather than drafting alone and circulating for comment.

1. Write outcomes, not features. Each outcome gets a measure, a current baseline, a target, a date and a named business owner. "Implement case management" is a feature. "Reduce time to first response on service cases from today's measured level to an agreed target within two quarters of go-live" is an outcome. If the legacy system cannot produce the baseline, sample it manually now rather than after go-live.
2. Connect outcomes to modules. Typical links are pipeline visibility and forecast reliability for Sales, lead conversion and consent coverage for Marketing, resolution time and repeat contact for Customer Service, and first-time fix and travel time for Field Service. A module with no outcome attached is a candidate for deferral.
3. Build the cost side honestly. Include licences and Dataverse capacity, partner fees, internal backfill for key users, data migration, integration, training, and the run cost after go-live: administration, support, and regression testing for the two Microsoft release waves each year. For licence costs and entitlements, confirm with the Microsoft licensing guide or your partner.
4. State benefits as the outcomes above, using the organisation's own figures and explicit assumptions. Do not borrow percentages from vendor case studies.
5. Draw the scope boundary at the level of processes, user groups, legacy systems to retire, integrations and headline data to migrate, with in scope, out of scope and deferred lists.
6. Name the governance roles: sponsor, product owner, programme manager, partner lead and, at enterprise scale, the design authority chair.
7. Copy every assumption and constraint the charter relies on into the RAID log, so that each one is tested rather than forgotten.
8. Have the sponsor sign it. From then on the charter is the baseline, and changes go through change control.

## Outputs

- `project-charter`, signed by the sponsor, covering purpose, outcomes, scope, governance, budget and constraints.
- A benefits register listing each outcome with measure, baseline, target, date and owner.
- A scope statement showing in scope, out of scope and deferred items.
- Initial assumptions and constraints, ready to load into the `raid-log`.

## Scale notes

### SMB

The charter can be two pages, drafted by the consultant with the owner or managing director, who is usually also the sponsor. Keep to three to five outcomes and a single release. Do not skip the baseline or the named sponsor; small projects lose their way through the same gaps as large ones, only faster.

### Enterprise

The business case goes through the organisation's investment approval process and needs finance sign-off on the cost model. Expect a programme charter with subordinate charters per phase or workstream, benefits owners in each business unit, and a benefits realisation plan that runs well beyond go-live. The PMO holds the baseline, and the charter names the stage gates the steering committee will use.

## Hand-offs

- `programme-management:delivery-plan` turns the scope and the fixed constraint into phases and milestones.
- `programme-management:governance-cadence` sets up the forums the charter names.
- `programme-management:raid-log` takes the assumptions and constraints.
- `project-tailoring:edition-selection` confirms SMB or enterprise treatment from the agreed scope.
- `change-adoption:adoption-metrics` reuses the outcome measures after go-live.
- No reviewer sign-off is required on the charter itself; check licence assumptions in the cost model through `platform-administration:licensing-and-capacity`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Sign off a charter whose outcomes have no baseline, target or owner.
- Quote licence prices or entitlements from memory; confirm with the Microsoft licensing guide or your partner.
- Present a feature list as the business case.
- Borrow benefit percentages from vendor case studies or other organisations.
- Let the implementation partner own the benefits register.
