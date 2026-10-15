---
name: marketing-consent-compliance
description: Reviews marketing consent against UK GDPR and PECR, covering lawful basis, consent records, soft opt-in, preference centres, tracking and subject access across Customer Insights - Journeys and seller outreach, and classifies findings as blocking or advisory. Use when marketing is about to go live or consent is being migrated.
license: CC-BY-4.0
metadata:
  department: security-compliance
  stages: Initiate, Implement, Prepare, Operate
  modules: Marketing, Sales
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Marketing consent compliance

Marketing is where a CRM project meets data protection law most directly. Under UK GDPR the organisation needs a lawful basis for using personal data for marketing, and under PECR electronic marketing to individuals generally needs consent unless a narrow exception applies. Mistakes here are visible: complaints, regulator attention and a contact database nobody trusts.

Projects usually go wrong at migration and at the edges. Old opt-in flags are imported without evidence, service emails quietly carry promotions, sellers send sequences outside the journeys that check consent, and the preference centre updates one system while another keeps sending. This skill structures the review; it is not legal advice, and every legal judgement goes to the organisation's DPO or legal adviser.

## When to use

- Before the first journey, newsletter or SMS campaign goes live, and as a go-live input for Marketing.
- When migrating contacts and consent from a legacy email platform or CRM.
- When the organisation wants to rely on soft opt-in, legitimate interests or the corporate subscriber rules.
- When designing how subject access, erasure and objection requests are met across marketing data.

Not this skill: `marketing:consent-and-preference-centre` to configure consent and the preference centre, `marketing:email-deliverability` for inbox placement and sender reputation, `security-compliance:data-retention` for how long consent and interaction data are kept.

## Questions to ask first

1. Is the audience consumers and sole traders, or corporate subscribers? PECR treats them differently, while UK GDPR still applies to named individuals in both.
2. Which channels are in play (email, SMS, phone, post)? Each has its own rules, and live calls need screening against the preference services.
3. Which lawful basis does the organisation rely on for each marketing purpose, and has the DPO documented it? The configuration follows the documented basis; it does not decide it.
4. What consent evidence exists today, and where? This decides what can be migrated as consent and what cannot.
5. Is the organisation a business, a charity or a public body, and does it market outside the UK? Exemptions differ and have been changing, so check current ICO guidance.

## Approach

Map before configuring anything. List every message type by purpose (newsletter, event invitation, product promotion, renewal reminder, service notice), channel and audience, and mark each as marketing or service. Service messages do not need marketing consent but must not carry promotion, and mislabelling marketing as service is one of the most common findings.

1. Basis and rule. For each purpose, channel and audience, record the lawful basis, the PECR rule that applies and the evidence required. The DPO confirms the table.
2. Soft opt-in. Accept it only where the details were collected during a sale or negotiation for a sale, the marketing is for the organisation's own similar products or services, and the person was offered a simple way to refuse at collection and in every message since. It does not pass to group companies or to bought lists.
3. Consent records. Each record should show who, which contact point, which purpose or topic, when, how it was obtained, and the wording and version they saw. Withdrawal must be as easy as giving consent. Customer Insights - Journeys holds consent per contact point and purpose; check current Microsoft Learn documentation for how journeys enforce it and how they separate marketing from transactional messages.
4. Every sender. Sales sequences, seller emails from Outlook, other email platforms and SMS providers must honour the same preference and suppression data.
5. Migration. Import consent only where evidence exists; otherwise import as no consent. An email asking people to opt in is itself a marketing message under PECR, so the DPO approves any re-permission campaign.
6. Tracking and profiling. Open and click tracking, cookies on forms and pages, and unified profiles in Customer Insights - Data may need consent or an impact assessment; agree the approach with the DPO.
7. Rights. Document where marketing data lives (contacts, leads, activities, interaction data, segments, unified profiles, exports) and how a subject access, erasure or objection request is found and fulfilled within the statutory deadline. Keep a minimal suppression record so a person who objected is not re-imported.

A finding is blocking when electronic marketing would reach individuals without valid consent or a documented exemption, when consent cannot be evidenced, when any sender ignores an opt-out, or when no workable rights process exists. Wording, double opt-in and preference centre layout are usually advisory. Blocking findings are not overruled by the department under review; disagreement escalates to the executive sponsor or steering committee.

## Outputs

- Purpose, channel and audience matrix with lawful basis and PECR rule, approved by the DPO.
- Consent record specification and migration rules, feeding the `data-migration-mapping`.
- Rights request procedure covering every place marketing data is held.
- Findings log with blocking items in the `raid-log`, and consent test cases for the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

Small organisations often rely on soft opt-in and business contacts, and may have no formal DPO, in which case the person responsible for data protection or an external adviser takes that role here. The consultant who configured consent should not be the only reviewer. Never skip the evidence check on migrated consent or the unsubscribe test across every sending tool.

### Enterprise

Several brands or countries usually mean separate compliance profiles and preference centres, and marketing outside the UK needs local legal advice on top of this review. Where the catalogue's consent-and-privacy-lead role is held, it owns the consent model day to day, with the DPO deciding. Expect a consent change log, impact assessments for unified profiles and periodic audits of suppression across all senders.

## Hand-offs

Configuration fixes go to `marketing:consent-and-preference-centre` and `marketing:journey-design`, and seller outreach rules to `sales:sequences-and-sales-accelerator`. Consent migration rules go to `integration-and-data:data-mapping-and-cleansing`, profile unification to `marketing:customer-profile-unification`, and open blocking findings to `programme-management:go-no-go`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Import contacts as opted in without evidence of how and when consent was given.
- Send a re-permission email campaign without the DPO's approval.
- Label a promotional message as transactional to avoid consent checks.
- Let any sending system ignore the shared preference and suppression data.
- Present the review as legal advice or settle a lawful basis without the DPO or legal adviser.
