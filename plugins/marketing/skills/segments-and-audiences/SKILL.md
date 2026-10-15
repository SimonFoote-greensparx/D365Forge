---
name: segments-and-audiences
description: Designs segments and audiences for Customer Insights - Journeys, covering audience sources, attribute and behavioural conditions, inclusions, exclusions, suppression and refresh. Use when building a campaign audience, choosing between Dataverse contacts, leads or unified profiles, or fixing segments that include or miss the wrong people.
metadata:
  department: marketing
  stages: Implement, Operate
  modules: Marketing
  status: draft
---

# Segments and audiences

A segment decides who receives a message, so a wrong condition is a customer-facing error and an over-broad one is a consent risk. In Customer Insights - Journeys, segments can be built on Dataverse contacts and leads or, where Customer Insights - Data is in place, on unified profiles, using attributes, related records and engagement behaviour.

Projects usually go wrong when marketers build segments on fields nobody maintains, when the same logic is copied into dozens of near-identical segments, or when suppression is left to each journey to remember. The result is inconsistent audiences and regular sends to people who should have been excluded.

## When to use

- Building audiences for journeys, campaigns and events.
- Choosing the audience source: contacts, leads or unified profiles.
- Defining reusable conditions, exclusions and suppression segments.
- Checking segment size, membership and refresh before a send.
- Diagnosing segments that include or miss the wrong people.

Not this skill: `marketing:customer-profile-unification` for building unified profiles in Customer Insights - Data, `marketing:journey-design` for what happens once people are in the audience, `sales:sequences-and-sales-accelerator` for sales accelerator segments.

## Questions to ask first

1. Which table or profile represents the person you want to reach? Contacts, leads and unified profiles behave differently in segments and journeys.
2. Which fields does the segment rely on, and who maintains them? A condition on an unmaintained field quietly includes or excludes the wrong people.
3. Who must always be excluded? Staff, competitors, test records and customers in dispute belong in shared suppression segments.
4. Does the audience depend on behaviour such as email clicks or website visits? Behavioural conditions depend on tracking, consent and how long interaction data is kept; check current Microsoft Learn documentation.
5. How fresh must the audience be when a journey starts? This decides whether a segment is suitable or a trigger would serve better.

## Approach

Build a small library of well-named, reusable segments rather than a new segment for every send. Think in building blocks: a base audience, reusable inclusion conditions, and shared exclusions that every journey applies.

1. Pick the audience source per use case. Use contacts for known customers and subscribers, leads where marketing works prospects before qualification, and unified profiles when the audience depends on data that is not in Dataverse. Mixing sources in one programme needs a clear rule for which record receives the message.
2. Validate the data first. For each field a segment depends on, check completeness and ownership. A segment on industry is worthless if half the accounts have no industry.
3. Create shared exclusion segments. Maintain one for test and internal records and one for people the business has decided not to market to, such as accounts in dispute. Handle opt-outs through the consent model, not through segments.
4. Name and document consistently. Put purpose, source and owner in the name or description, and record the logic in plain language so a reviewer can check it without opening the builder.
5. Preview before use. Check segment size and a sample of members against expectations before attaching a segment to a journey, especially after data loads or field changes.
6. Treat AI-assisted segment building as a draft. Describing a segment in natural language can be a quick start, but review the generated conditions line by line before use, and check current Microsoft Learn documentation for what is available.
7. Review regularly. Retire unused segments, watch membership counts over time and investigate sudden jumps or drops.

Engagement-based segments, such as people who have interacted recently, help both relevance and deliverability. Agree one definition of engaged with the deliverability owner and use it consistently across journeys.

## Outputs

- Segment library: name, purpose, source, plain-language logic and owner for each segment.
- Shared exclusion and suppression segment design.
- Data quality findings for the fields segments depend on.
- Segment validation checks in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

The marketer usually builds segments, with consultant support for the first few. Start with contacts as the only source, a handful of reusable segments and one shared exclusion segment for test and internal records. Do not skip previewing segment members before the first live send.

### Enterprise

Expect several brands, regions and audience sources, a segment library owned by marketing operations and enforced naming standards. Segments on unified profiles need coordination with the Customer Insights - Data owner, and new audience sources or sensitive attributes go through `security-compliance:marketing-consent-compliance`. Where segments are very large, test refresh timing with `testing-quality:performance-testing` before campaign dates are fixed.

## Hand-offs

`marketing:journey-design` consumes segments, `marketing:customer-profile-unification` supplies unified profiles, and `marketing:consent-and-preference-centre` handles opt-outs. Data quality problems in segment fields go to `integration-and-data:data-mapping-and-cleansing`. Using new data sources or sensitive attributes for targeting needs `security-compliance:marketing-consent-compliance` sign-off.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Use segments as a substitute for the consent model when handling opt-outs.
- Build segments on fields nobody maintains.
- Target audiences using special category data without a basis approved by the DPO.
- Send to a segment whose size and members have not been previewed after a data change.
