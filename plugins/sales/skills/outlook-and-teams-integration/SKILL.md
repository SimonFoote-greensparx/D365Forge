---
name: outlook-and-teams-integration
description: Designs server-side synchronisation, the Dynamics 365 App for Outlook and Teams collaboration for CRM users, covering mailbox setup, tracking rules, contact and appointment sync and record collaboration in Teams. Use when connecting mailboxes, deciding what gets tracked, or fixing sync errors and duplicate contacts.
metadata:
  department: sales
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: draft
---

# Outlook and Teams integration

Sellers live in Outlook and Teams, so the integration with Dynamics 365 decides whether customer conversations end up in CRM or stay in personal mailboxes. Server-side synchronisation connects Exchange mailboxes to Dataverse for email, appointments, contacts and tasks; the Dynamics 365 App for Outlook lets users track items and see CRM context; Teams integration links records to channels, chats and meetings.

Projects usually go wrong by connecting every mailbox with default settings and then finding thousands of personal contacts in CRM, or by leaving tracking entirely to users so almost nothing is captured. Mailbox approval and test failures also stall go-live more often than expected, because they depend on Exchange administrators outside the project team.

## When to use

- Planning server-side synchronisation for users and queues.
- Deciding tracking rules: which emails, appointments and contacts go into Dynamics 365.
- Deploying and configuring the Dynamics 365 App for Outlook.
- Setting up Teams collaboration around Dynamics 365 records.
- Troubleshooting mailbox errors, missing tracked items or duplicate contacts.

Not this skill: `customer-service:email-to-case` for shared mailboxes that create cases, `sales:copilot-in-sales` for Copilot experiences in Outlook and Teams, `platform-administration:environment-setup` for environment and tenant configuration.

## Questions to ask first

1. Is email on Exchange Online in the same tenant as Dynamics 365? Same-tenant Exchange Online is the straightforward path; anything else needs specialist design.
2. Who can approve mailboxes and deploy add-ins? Both usually need administrators outside the project, so book their time early.
3. What must be tracked automatically, and what is left to the user? This decides email processing settings and whether folder-level tracking is used.
4. Should contacts and appointments synchronise, and for whom? Unfiltered contact sync is the main way personal data floods into CRM.
5. How do sellers use Teams for customer work today? This decides whether linking records to channels and chats adds value or noise.

## Approach

Design the integration as a data capture policy first and a configuration task second. The real question is which customer interactions the organisation wants on record, within what privacy boundaries, and how much effort users should spend capturing them.

1. Set up server-side synchronisation per environment. Configure the email server profile for Exchange Online, set default mailbox settings for new users, and plan mailbox approval with the Exchange or global administrator. Test and enable mailboxes in batches and keep a register of failures and fixes. Copied or restored environments need their mailboxes re-tested and must not keep synchronising production mailboxes.
2. Choose the tracking model. Options range from users tracking individual items in the Outlook app, through folder-level tracking, to automatic rules in personal options. A sensible default is deliberate tracking by users, folder-level tracking for people who prefer filing, and email correlation so replies to tracked messages are captured.
3. Control contact synchronisation. Use synchronisation filters so only contacts that already exist in Dynamics 365 and belong to the user synchronise, rather than pushing whole address books into CRM. Agree how a contact first met in Outlook becomes a CRM contact, and who checks for duplicates.
4. Decide appointment and task sync. Two-way appointment sync helps sellers log meetings but can expose private calendar items, so set filters and teach users to mark items private.
5. Deploy the Dynamics 365 App for Outlook centrally through the Microsoft 365 admin center to the users who need it, and confirm it works in the Outlook clients they actually use.
6. Configure Teams collaboration where account and deal teams genuinely work in Teams, linking records to channels or chats, and agree naming and lifecycle rules so channels do not multiply. Check current Microsoft Learn documentation for the current collaboration and meeting features and their admin settings.
7. Monitor. Mailbox errors are invisible to users, so set up a regular mailbox status check and alerts for persistent failures.

Pilot with a small group of real users for at least a full working week before wider rollout, because sync problems surface only with real mail volumes and habits.

## Outputs

- Mailbox and synchronisation design: server profile, default settings, approval process and rollout batches.
- Tracking and data capture policy covering email, appointments, contacts and tasks.
- Outlook app deployment plan and supported client list.
- Teams collaboration conventions for channels, chats and meetings linked to records.
- Mailbox steps in the `cutover-and-hypercare-checklist`, and non-production mailbox rules in the `environment-and-alm-strategy`.

## Scale notes

### SMB

The consultant usually configures synchronisation with whoever administers Microsoft 365, often in a single session. Use default settings, deliberate tracking by users and contact sync filtered to owned contacts. Do not skip the pilot or the contact sync decision, because a few hundred personal contacts can pollute a small CRM within days.

### Enterprise

Expect separate Exchange and Dynamics 365 administration teams, change control for mailbox approval and add-in deployment, and mailbox rollout in waves aligned with training. Agree queue and shared mailbox rules with the service workstream, run mailbox health as an operational service, and document the privacy position on tracking and calendar sync with the DPO.

## Hand-offs

`platform-administration:environment-setup` owns environment configuration, and `platform-administration:monitoring` takes on mailbox health after go-live. Shared mailboxes for case creation go to `customer-service:email-to-case`. Who can see tracked email and synchronised contacts needs `security-compliance:security-model-review`, and user training goes to `change-adoption:role-based-training`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Synchronise entire Outlook address books into Dynamics 365.
- Let test or development environments process production mailboxes.
- Approve and enable all mailboxes at once without testing a pilot group first.
- Turn on automatic tracking of all email without agreeing the privacy position with the DPO.
