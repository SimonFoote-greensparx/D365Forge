---
name: forms-and-events
description: Designs marketing forms and event management in Customer Insights - Journeys, covering form fields, contact and lead matching, consent capture, embedding, spam protection, registration, check-in and follow-up. Use when building sign-up or enquiry forms, running webinars or in-person events, or fixing duplicates created by form submissions.
metadata:
  department: marketing
  stages: Implement, Operate
  modules: Marketing
  status: draft
---

# Forms and events

Forms and events are where most new people enter the marketing database, so they shape data quality, consent evidence and the leads sales will see. Customer Insights - Journeys provides forms that create or update contacts and leads, and event management for registrations, sessions, check-in and online events.

Projects go wrong when every campaign builds its own form with different fields and consent wording, when submissions create duplicates because matching was never designed, or when event registrations run in a separate tool and never reach the CRM.

## When to use

- Designing marketing forms for subscriptions, enquiries, downloads and registrations.
- Setting contact and lead matching and update rules for submissions.
- Configuring consent capture and double opt-in on forms.
- Planning events: sessions, registration, capacity, reminders, check-in and follow-up.
- Embedding or hosting forms, and protecting them from spam.

Not this skill: `marketing:consent-and-preference-centre` for the consent model behind form checkboxes, `marketing:lead-scoring-and-sales-handoff` for what happens to leads from forms, `marketing:journey-design` for confirmation, reminder and follow-up journeys.

## Questions to ask first

1. Should a submission create or update a contact, a lead or both? This decides matching rules and what sales sees.
2. Which fields identify a person for matching? Email is the usual key, and a poor rule either creates duplicates or overwrites the wrong record.
3. What consent is captured, with what wording, and is double opt-in needed? Wording and evidence must be agreed with the DPO before forms go live.
4. Where will forms live: the corporate website, landing pages or hosted pages? This affects embedding, styling, cookies and who maintains the page.
5. What kind of events run: in-person, online or hybrid, single or multi-session? The event type decides sessions, capacity, check-in and online meeting integration.

## Approach

Standardise forms before multiplying them. Build a small set of form patterns, each with fixed core fields and consent elements, and let campaigns reuse them with different content. This keeps data consistent and cuts review effort.

1. Decide the record strategy. For subscriptions and newsletters, create or update contacts. For enquiries that need sales follow-up, create a lead linked to the contact, so sales sees intent without cluttering the contact table. Write down the matching rule and which fields a submission may overwrite.
2. Keep forms short. Ask only for what the next step needs; gathering detail across several interactions beats a long first form.
3. Capture consent properly. Use consent elements tied to the agreed purposes and topics, with wording approved by the DPO, and use double opt-in where the organisation's policy calls for stronger evidence. Do not pre-tick boxes.
4. Protect forms. Use the available bot protection, validate fields and watch submissions for spam patterns. Spam creates junk leads and harms deliverability when confirmation emails go to bad addresses.
5. Design events end to end. Set up the event, sessions and capacity, a registration form, confirmation and reminder messages through journeys, check-in, and follow-up for attendees and no-shows. For online events, check current Microsoft Learn documentation for the supported integration with Teams webinars or other platforms.
6. Feed sales. Registrations and attendance should be visible on the contact and, where relevant, update lead scores or raise tasks so sellers can follow up.
7. Test submissions end to end: a new person, an existing person, a changed email address, a spam attempt and a withdrawal of consent.

Check cookies and tracking on hosting pages with the website owner, because form analytics may depend on them, and take any cookie consent question to the DPO.

## Outputs

- Form pattern catalogue: purpose, fields, matching and update rules, consent elements.
- Event setup template: sessions, capacity, registration, reminders, check-in and follow-up.
- Consent wording log approved by the DPO.
- Form and event test cases in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

A small marketing team should start with one subscription form, one enquiry form and one event registration pattern, embedded on the website by whoever maintains it. Match on email and create leads only for enquiries. Do not skip the DPO review of consent wording or the end-to-end submission test.

### Enterprise

Expect forms across many sites, brands and languages, events with many sessions and venues, and a web team that controls embedding and cookies. Govern form patterns centrally, align matching rules with the data owner and any Customer Insights - Data unification, and route new consent wording through `security-compliance:marketing-consent-compliance`. Load-test registration for large events with `testing-quality:performance-testing`.

## Hand-offs

`marketing:consent-and-preference-centre` defines the consent elements, `marketing:lead-scoring-and-sales-handoff` takes leads from enquiry forms, and `marketing:journey-design` builds confirmation, reminder and follow-up journeys. Consent capture on forms needs `security-compliance:marketing-consent-compliance` sign-off, and retention of form and event data goes to `security-compliance:data-retention`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Pre-tick consent checkboxes or bundle marketing consent into terms and conditions.
- Let form submissions overwrite existing contact data without an agreed matching rule.
- Publish forms without bot protection and spam monitoring.
- Run event registration in a separate tool without a plan to bring registrations and attendance into Dynamics 365.
