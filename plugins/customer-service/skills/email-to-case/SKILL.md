---
name: email-to-case
description: Designs email-to-case in Dynamics 365 Customer Service, covering support mailboxes, server-side sync, queue mailboxes, automatic record creation and update rules, and the controls that stop reply chains creating duplicate cases. Use when turning shared support inboxes into cases or fixing duplicate, missing or junk email cases.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Initiate, Implement, Prepare
  modules: Customer Service
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Email-to-case

For many service desks email is still the busiest channel, and email-to-case is where the most visible defects appear in the first week after go-live. Duplicate cases from customer replies, cases raised by out-of-office messages and delivery failures, internal colleagues copied in who generate cases of their own, and a mailbox that silently stopped synchronising are all common, and all avoidable.

The root cause is usually that the project configured the record creation rule and tested it with a handful of tidy, single-message emails. Real support mail arrives as long threads, forwards, replies with edited subjects, and messages copied to several support addresses at once.

## When to use

- Connecting support mailboxes to Dynamics 365 and their queues.
- Designing automatic record creation and update rules for incoming email.
- Deciding how unknown senders, auto-replies, internal senders and spam are handled.
- Preventing duplicate cases from reply chains and multi-mailbox threads.
- Planning the switch of mail flow from a legacy helpdesk.

Not this skill: `customer-service:case-lifecycle-design` for the reopen rule and statuses, `customer-service:queues-and-routing` for what happens after the case lands in a queue, `sales:outlook-and-teams-integration` for users' own Outlook tracking and synchronisation.

## Questions to ask first

1. Which addresses receive support email, and who replies from them? Each becomes a queue mailbox, and replies must come from the case to keep threads linked.
2. Should every inbound email create a case, or only email from known customers? This shapes the rule conditions and the handling of unknown senders.
3. How do customers reply, forward and copy in other people? This decides which duplicate controls matter most.
4. What should a reply to a resolved case do? The answer must match the reopen rule from `customer-service:case-lifecycle-design`.
5. Do emails carry sensitive data or large attachments? This drives attachment limits, storage and retention decisions.

## Approach

Email-to-case has three layers, and problems are much easier to fix when you know which layer owns them. Mail flow is Exchange Online mailboxes synchronised into Dataverse through server-side synchronization, with each support mailbox linked to a queue. Record creation is the automatic record creation and update rule that turns an incoming email into a case or attaches it to an existing one. Handling is everything after that, covered by neighbouring skills.

1. Set up mailboxes properly. Use a dedicated mailbox per support queue, approve and test each one, and agree with the Microsoft 365 administrator who owns mailbox approval, permissions and alerts when synchronisation fails. A failed mailbox stops case creation without anyone noticing.

2. Decide which emails become cases. Configure conditions so that out-of-office replies, delivery failures, internal senders and known junk do not create cases. Decide whether unknown senders get a new contact and a case or go to a triage queue; on business-to-business desks, a triage queue usually avoids polluting contacts.

3. Stop duplicates from reply chains. Most duplicates are replies that the system failed to link to the original case. Keep tracking tokens or conversation correlation enabled (check current Microsoft Learn documentation for the matching options in your version), make sure agents reply from the case so outgoing mail carries the link, and set the rule so replies on an active case update it rather than raise a new one.

4. Handle resolved cases and shared threads. Configure what a reply to a resolved case does, in line with the agreed reopen window. When a customer copies two support addresses, both mailboxes receive the message, so decide which one owns the thread and test that only one case results.

5. Map the fields. Decide how sender, subject, body, keywords and attachments populate the case, and which values routing depends on. Keep parsing logic in the rule or a small flow rather than custom code unless volume or complexity demands it.

6. Protect the data. Attachments consume storage and may carry personal or sensitive data. Agree size limits, blocked file types and retention with `security-compliance:data-retention`, and take any question on lawful processing of email content to the organisation's DPO or legal adviser.

7. Test with real patterns, then switch over. Build a test pack of anonymised real emails (auto-replies, long threads, forwards, edited subjects, multiple recipients, large attachments) and run it through a test mailbox. Plan the cutover of mail flow, including how replies to old helpdesk ticket references are handled once the legacy system stops.

## Outputs

- Support mailbox and queue inventory in the `integration-inventory`.
- Record creation rule specification, including exclusions and unknown-sender handling.
- Duplicate-control decisions and the reply-to-resolved-case behaviour.
- Email test pack and expected results in `test-strategy-and-uat-scripts`.
- Mail flow switch-over steps and mailbox monitoring checks in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Usually one or two shared mailboxes feed one or two queues, with the consultant configuring the rule and the Microsoft 365 administrator approving mailboxes. Keep the rule simple. Do not skip auto-reply and internal-sender exclusions, duplicate testing with real threads, or an alert when synchronisation fails.

### Enterprise

Expect many regional or product mailboxes, an Exchange team with its own change process, and volumes that make duplicates expensive. Provision and approve mailboxes through a repeatable script or checklist, monitor mailbox health centrally, and agree legal hold and retention with the records management function. Route rule changes through change control, because a bad condition can flood queues within minutes.

## Hand-offs

- `customer-service:queues-and-routing` for routing the cases this creates.
- `platform-administration:monitoring` for mailbox synchronisation alerts.
- `support-operations:cutover-plan` for the mail flow switch-over.
- Reviewer sign-off: `security-compliance:data-retention` for email and attachment retention, and `security-compliance:security-model-review` for mailbox and queue access.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Create a case for every inbound email without excluding auto-replies, delivery failures and internal senders.
- Reply to customers on support threads from personal mailboxes outside the case.
- Go live without an alert for mailbox synchronisation failures.
- Switch live mail flow to Dynamics 365 before testing the rule against real reply chains.
