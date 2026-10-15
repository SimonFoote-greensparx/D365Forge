---
name: email-deliverability
description: Plans email deliverability for Customer Insights - Journeys, covering sending domain strategy, domain authentication with SPF, DKIM and DMARC, warm-up, list hygiene and sender reputation monitoring. Use when authenticating domains, planning the first sends from a new platform, or investigating marketing email landing in spam or bouncing.
license: CC-BY-4.0
metadata:
  department: marketing
  stages: Implement, Prepare, Operate
  modules: Marketing
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Email deliverability

Deliverability is whether marketing email reaches the inbox rather than the spam folder or nowhere at all. It depends on authenticated domains, a sending reputation built up gradually, and lists of people who want the email. Mailbox providers have become stricter with bulk senders, so a project that ignores this can go live with a working journey whose messages nobody sees.

Projects usually go wrong by leaving domain authentication until go-live week, because DNS changes need IT and sometimes an external host, or by migrating years of unengaged contacts and mailing all of them on day one. Both damage reputation in ways that take weeks to repair.

## When to use

- Authenticating sending domains for Customer Insights - Journeys.
- Choosing sending domains and subdomains for marketing.
- Planning warm-up for a new domain or platform.
- Setting list hygiene rules for bounces, unengaged contacts and suppression.
- Investigating falling engagement, spam placement or blocklisting.

Not this skill: `marketing:email-and-sms-channels` for templates and content, `marketing:consent-and-preference-centre` for consent and unsubscribe design, `customer-service:email-to-case` for service mailbox configuration.

## Questions to ask first

1. Who controls DNS for the sending domains, and how long do changes take? Authentication depends on DNS records that IT or an external provider must publish.
2. Does the organisation's domain already have a DMARC policy? A strict policy without the new sending service aligned can block marketing email entirely.
3. How large and how engaged is the list being migrated? Mailing old, unengaged addresses is the fastest way to damage a new reputation.
4. What volumes and frequency are planned for the first months? Warm-up has to match the real sending plan.
5. Will marketing share a domain with corporate email or other senders? Shared domains share reputation and DMARC policy.

## Approach

Treat deliverability as an infrastructure workstream with its own plan, owner and lead times, not as a marketing afterthought.

1. Choose sending domains. Many organisations send marketing from a dedicated subdomain (for example news.example.co.uk), which keeps marketing reputation and policy apart from corporate email while the brand still looks familiar. Agree this with IT and the brand owner before templates are built.
2. Authenticate. Add each sending domain in Customer Insights - Journeys and publish the DNS records it supplies for DKIM, make sure SPF covers the sending service where needed, and confirm alignment so DMARC passes. Check current Microsoft Learn documentation for the exact records and steps, then test with real sends to the major mailbox providers.
3. Introduce DMARC carefully. If there is no DMARC policy yet, start in monitoring mode, read the reports, and move towards quarantine and then reject only once every legitimate sender is aligned. If a strict policy already exists, align the new service before the first send.
4. Clean the list before migration. Remove hard bounces and known invalid addresses, apply the organisation's policy on role addresses, and hold back long-term unengaged contacts from early sends. Agree what engaged and unengaged mean with marketing.
5. Warm up. Start with the most engaged recipients at modest volumes and increase gradually while watching bounces and complaints. Avoid large sends to cold segments early on. If dedicated sending IPs are offered for your volume, they need their own warm-up; check current Microsoft Learn documentation.
6. Meet mailbox provider expectations. Major providers expect authenticated mail, easy one-click unsubscribe and low complaint rates from bulk senders. Read their current published guidance rather than relying on memory.
7. Monitor continuously. Track bounce, complaint and unsubscribe trends, register for mailbox provider postmaster tools where they exist, act on blocklist alerts, and suppress repeated bounces automatically.

Deliverability is never finished. Build a monthly review into marketing operations, and revisit warm-up whenever volumes or domains change.

## Outputs

- Sending domain strategy and DNS change request, with owners and lead times in the `raid-log`.
- Authentication checklist for SPF, DKIM and DMARC per domain.
- Warm-up plan aligned to the launch send schedule.
- List hygiene and suppression rules.
- Deliverability checks in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

The consultant usually guides whoever manages DNS, often an external IT provider, through authentication in one session. Use one marketing subdomain, a simple warm-up across the first few sends and strict removal of hard bounces. Do not skip authentication, and do not mail the whole legacy list on day one.

### Enterprise

Expect several brands and domains, an existing DMARC policy owned by the security team, and a central email team that coordinates every sender. Plan DNS changes through change control, align all sending services before tightening DMARC, and give deliverability a named owner in marketing operations. Sending domain strategy across brands should go through `design-authority:design-review`, and incidents should follow `support-operations:incident-management`.

## Hand-offs

`marketing:email-and-sms-channels` builds content on the authenticated domains, `marketing:segments-and-audiences` applies engagement-based suppression, and `platform-administration:monitoring` takes over reputation monitoring after go-live. List cleansing and suppression decisions that touch consent need `security-compliance:marketing-consent-compliance` sign-off.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Send production marketing volume from an unauthenticated domain.
- Move DMARC straight to reject without reviewing monitoring reports first.
- Mail the full migrated list in the first week on a new domain.
- Buy or rent email lists.
