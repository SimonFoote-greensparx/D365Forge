---
name: consent-and-preference-centre
description: Designs the consent model and preference centre for Customer Insights - Journeys, mapping UK GDPR and PECR questions, including soft opt-in, onto contact point consent, purposes, topics and compliance profiles. Use when setting up consent, migrating legacy opt-ins, building a preference centre, or checking whether a message may be sent.
license: CC-BY-4.0
metadata:
  department: marketing
  stages: Strategize, Initiate, Implement, Prepare, Operate
  modules: Marketing
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Consent and preference centre

Consent decides whether a marketing message may be sent at all, so this is the part of marketing design where a configuration mistake becomes a regulatory problem. Customer Insights - Journeys records consent against each contact point (an email address or phone number) for purposes and topics, grouped in compliance profiles, and checks it when messages go out. Check current Microsoft Learn documentation for how the model behaves in your release.

Projects go wrong by migrating old opt-in flags without evidence, by treating every message as transactional, or by building a preference centre that offers choices the system cannot honour. This skill structures the questions; it is not legal advice, and the final call belongs to the organisation's DPO or legal adviser.

## When to use

- Designing purposes, topics and compliance profiles for marketing.
- Working out the consent approach for each audience, channel and purpose.
- Considering soft opt-in for existing customers.
- Migrating consent from a legacy CRM or marketing tool.
- Building or reviewing a preference centre and unsubscribe flow.

Not this skill: `security-compliance:marketing-consent-compliance` for the independent compliance review, `marketing:forms-and-events` for capturing consent on forms, `marketing:email-and-sms-channels` for footer and opt-out content.

## Questions to ask first

1. Which channels, audiences and countries are in scope? UK GDPR and PECR treat individuals, sole traders and corporate subscribers differently, and other countries add their own rules.
2. What lawful basis and form of permission does the organisation rely on for each purpose? This decides whether explicit opt-in, soft opt-in or another basis is even on the table, and the DPO makes that decision.
3. What evidence exists behind current consent records? Without source, date and wording, legacy opt-ins may not be usable.
4. Which messages are genuinely transactional or service messages? Marketing dressed up as service messaging is a common compliance failure.
5. What choices should the preference centre offer? Every choice offered must map to a purpose or topic the system can enforce.

## Approach

Build the consent model from the organisation's privacy position, agreed with the DPO, and only then configure it. Start with a consent matrix: one row per purpose (for example newsletters, product offers, event invitations, service notices), columns for channel and audience type, and in each cell the basis relied on, the permission type, the evidence required and how withdrawal works.

1. Separate purposes from topics. Purposes reflect why the organisation contacts people, such as commercial marketing as opposed to transactional notices; topics let people choose subjects within a purpose. Keep both lists short and stable.
2. Treat PECR as a separate test from UK GDPR. Electronic marketing by email and text has its own rules on top of the lawful basis question. Soft opt-in may let an organisation market its own similar products and services to existing customers whose details it gathered during a sale or negotiation, provided a simple opt-out was offered then and is offered in every message. Whether it applies to a given audience, and whether recent changes to UK law affect the position, is for the DPO or legal adviser to decide.
3. Configure compliance profiles to match the matrix. Set up purposes, topics, double opt-in where required and the preference centre for each profile, and record which profile each journey and message uses.
4. Migrate with evidence. Bring legacy consent across only where source, date and wording are known, and keep that evidence with the record. Where evidence is missing, agree with the DPO whether to treat records as not consented or to run a permission refresh campaign.
5. Design the preference centre for people. Offer clear choices that map exactly to topics and purposes, a single way to unsubscribe from all marketing, and a confirmation. Test that each choice actually stops the right messages.
6. Keep consent consistent across systems. If sales, service or other tools capture opt-outs, design how they reach Customer Insights - Journeys promptly and which system holds the record of truth.
7. Prove it works. Write test cases for each cell of the matrix, including withdrawal, and keep the results as evidence.

All of this is design support, not legal advice. Take the matrix and every open question to the organisation's DPO or legal adviser.

## Outputs

- Consent matrix by purpose, channel and audience, approved by the DPO.
- Compliance profile, purpose and topic configuration design.
- Legacy consent migration rules and evidence mapping in the `data-migration-mapping`.
- Preference centre design and unsubscribe flow.
- Consent test cases and evidence in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

In a small organisation the marketer and consultant draft the consent matrix and whoever acts as DPO approves it. One compliance profile with a few topics and a simple preference centre is often enough. Do not skip the evidence check on migrated opt-ins or the DPO approval, because small organisations face the same rules as large ones.

### Enterprise

Expect several brands, countries and compliance profiles, a formal privacy team and records of processing to update. Consent flowing between Customer Insights - Journeys, sales, service and external systems needs an integration design and a single record of truth. Every change to purposes, topics or consent wording goes through `security-compliance:marketing-consent-compliance`, whose blocking findings the marketing team cannot overrule.

## Hand-offs

`security-compliance:marketing-consent-compliance` must sign off the consent model before go-live, and `security-compliance:data-retention` sets how long consent evidence and unengaged contacts are kept. `marketing:forms-and-events` and `marketing:email-and-sms-channels` implement capture and opt-out, and `integration-and-data:migration-strategy` plans the movement of legacy consent. Open legal questions go to the organisation's DPO or legal adviser.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Migrate legacy opt-ins without source, date and wording evidence.
- Treat marketing messages as transactional to avoid consent checks.
- Offer preference centre choices that the system does not enforce.
- Present this design as legal advice, or settle the lawful basis without the DPO or legal adviser.
