---
name: email-and-sms-channels
description: Designs the email and text message channels in Customer Insights - Journeys, covering templates, content blocks, personalisation, sender identity, SMS providers and numbers, opt-out keywords and message testing. Use when setting up email or SMS for the first time, building a template set, or deciding which messages belong on which channel.
metadata:
  department: marketing
  stages: Implement, Prepare, Operate
  modules: Marketing
  status: draft
---

# Email and SMS channels

Email and text messages are the main ways a journey reaches people, and each brings its own setup, content standards and compliance rules. In Customer Insights - Journeys, email is designed in the built-in editor with reusable content and personalisation, while text messages need a supported SMS provider, sender numbers and keyword handling.

Projects go wrong by treating channel setup as a creative task only and leaving sender identity, SMS provider contracts and opt-out handling to the final week. Another common failure is personalisation that breaks: a missing first name, the wrong language or a dynamic field that renders blank in front of thousands of customers.

## When to use

- Setting up email templates, content blocks, brand settings and personalisation.
- Choosing an SMS provider, sender numbers or short codes, and opt-out keywords.
- Deciding which message types use email, SMS or both.
- Designing message testing and approval.
- Fixing rendering, personalisation or SMS delivery problems.

Not this skill: `marketing:email-deliverability` for domain authentication and sender reputation, `marketing:consent-and-preference-centre` for consent and subscription design, `customer-service:digital-and-voice-channels` for SMS and messaging in customer service.

## Questions to ask first

1. Which message types go on which channel, and are any transactional rather than marketing? The purpose decides the consent rules and footer requirements.
2. Which sending domains and sender names represent the brand? Sender identity must be agreed with IT and the brand owner before templates are built.
3. Which countries and languages are in scope? Languages, character sets, time zones and SMS rules vary by country.
4. Which SMS providers and number types are available in the target countries? Provisioning can take weeks; check current Microsoft Learn documentation for supported providers.
5. Who approves content before it is sent? Brand, legal and compliance approval needs a defined route.

## Approach

Set up the channel foundation once, then make content creation repeatable. The foundation is sender identity, templates, reusable blocks and compliance elements; content is what marketers change every week.

1. Agree sender identity. Choose sending domains and from names with IT and the brand owner, and make sure domain authentication is under way before the first real send.
2. Build a small template set. A few templates covering newsletter, event, service notice and simple announcement are easier to maintain than one per campaign. Put the footer, postal address, unsubscribe and preference centre links in reusable content blocks so they cannot be forgotten.
3. Design personalisation defensively. Give every dynamic field a fallback value, test conditional content with records that are missing data, and personalise only with fields that are maintained.
4. Plan languages early. Decide whether languages are handled by separate messages, conditional content or language-specific journeys, and where preferred language is held on the contact.
5. Set up SMS properly. Contract with a supported provider, provision sender numbers or short codes for each country, configure opt-out and help keywords, and agree quiet hours. Keep messages short, identify the sender and include the opt-out instruction wherever it is required.
6. Separate transactional from marketing. Service notices such as booking confirmations may follow different consent rules from marketing. Make the distinction visible in the template set and in the consent purpose each message uses, and let the DPO decide borderline cases.
7. Test every message. Preview and send tests across major email clients and devices, check links and tracking, and send SMS tests to real handsets in each country. Record approval before scheduling.

Editor features, AI-assisted content and channel options change frequently, so check current Microsoft Learn documentation before promising a capability. Message volumes may count against tenant entitlements; confirm with the Microsoft licensing guide or your partner.

## Outputs

- Channel setup record: sending domains, from names, SMS provider, numbers and keywords by country.
- Template and content block library with owners.
- Personalisation standards, including fallback values and language handling.
- Message approval route, captured in the `raci-matrix`.
- Message test cases in the `test-strategy-and-uat-scripts`.

## Scale notes

### SMB

One marketer and a consultant can set up email in days: one sending domain, three or four templates and a footer block. Add SMS only when there is a clear use case and a provider in place. Do not skip test sends to real inboxes and the unsubscribe check before the first campaign.

### Enterprise

Expect several brands, sending domains, languages and countries, each with its own SMS registration and provider arrangements. Use a content governance model with brand and legal approval, shared template libraries and design standards, and track provisioning lead times in the `raid-log`. Country-specific SMS rules and transactional messaging should be reviewed through `security-compliance:marketing-consent-compliance`.

## Hand-offs

`marketing:email-deliverability` owns authentication and reputation, `marketing:consent-and-preference-centre` owns consent purposes and preference links, and `marketing:journey-design` places messages in journeys. Message volume against entitlements is a `platform-administration:licensing-and-capacity` question; confirm with the Microsoft licensing guide or your partner. Content and channel compliance needs `security-compliance:marketing-consent-compliance` sign-off.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Send personalised content without fallback values for missing fields.
- Send marketing text messages without opt-out keyword handling and sender identification.
- Remove or hide the unsubscribe and preference centre links in marketing templates.
- Label a marketing message as transactional to get round consent.
