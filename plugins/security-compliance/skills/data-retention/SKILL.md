---
name: data-retention
description: Designs and reviews how long CRM data is kept and how it is deleted, anonymised or retained, covering bulk deletion, Dataverse long-term retention, audit logs, call recordings and downstream copies, and classifies findings as blocking or advisory. Use when setting retention rules, planning deletion jobs or handling erasure requests.
license: CC-BY-4.0
metadata:
  department: security-compliance
  stages: Initiate, Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Data retention

A CRM system collects personal data faster than almost any other: tracked emails, case notes, attachments, marketing interactions, call recordings and transcripts. UK GDPR expects the organisation to keep personal data no longer than it needs, yet many projects go live with no deletion at all because retention was left for later. Later arrives as a storage bill, a subject access request that surfaces notes from years ago, or an erasure request nobody can carry out.

The other common failure is deleting in Dataverse and assuming the job is done while copies remain in the lake, in Power BI, in mailboxes and in the ERP. This skill structures retention design and review. It does not set retention periods; those come from the organisation's retention schedule and are confirmed by its DPO or legal adviser.

## When to use

- Turning a retention schedule into rules for each table, file type and recording.
- Choosing between deletion, anonymisation and long-term retention for a type of record.
- Setting call recording and transcript retention for Dynamics 365 Contact Center.
- Designing how erasure requests and legal holds work, or reviewing retention before go-live or a migration.

Not this skill: `security-compliance:marketing-consent-compliance` for the lawful basis and consent records themselves, `integration-and-data:migration-strategy` for deciding what to migrate, `platform-administration:licensing-and-capacity` for storage capacity.

## Questions to ask first

1. Does the organisation have a retention schedule, and who owns it? Periods come from the schedule, never from the project team.
2. What starts the clock for each record type (case resolved, contract ended, last interaction)? A period without a trigger cannot be automated.
3. What must survive the period: nothing, anonymised statistics or a read-only record? This decides delete, anonymise or retain.
4. Where are the copies (lake or Fabric exports, Power BI, ERP, SharePoint document locations, mailboxes, recordings, backups)? Deletion only counts if every copy is covered.
5. Are there legal holds or sector obligations that override deletion? Every job needs a way to leave held records alone.

## Approach

Turn the schedule into a retention matrix with one row per table, file type or recording type: purpose, trigger, period from the schedule, action (delete, anonymise or retain read-only), mechanism, owner and evidence. Include the data people forget: notes and attachments, email bodies, audit history, marketing interaction data, unified profiles in Customer Insights - Data, and call recordings and transcripts.

1. Pick the mechanism for each row. Bulk delete jobs are the long-standing way to remove records matching a query on a recurring schedule. Anonymisation (blanking or replacing personal columns while keeping the record for reporting) usually needs a scheduled cloud flow or plug-in. Dataverse long-term retention can move inactive records into read-only retained storage; check current Microsoft Learn documentation for what it supports, how retained data is queried and how it is eventually deleted.
2. Respect relationships. Deleting a parent can cascade to its children or be blocked by a restrict rule. Decide per relationship whether children are deleted, reassigned or anonymised, and test in a sandbox with production-like volumes before any live run.
3. Cover recordings and logs. Contact Center recordings and transcripts, audit log retention and marketing interaction data each have their own settings. Check current Microsoft Learn documentation for each and align them with the schedule.
4. Follow every copy. Deleting in Dataverse does not touch lake or Fabric exports, Power BI imports, ERP records, tracked emails still in mailboxes or SharePoint documents. Give each copy its own rule and owner.
5. Plan for backups and restores. Deleted data persists in backups until they expire, so agree with the DPO how erasures are re-applied if a backup is ever restored.
6. Holds and erasure. Provide a flag or query that excludes held records from every job, and a documented route for individual erasure requests that also updates the marketing suppression list.
7. Evidence. Log each run (job, date, records affected, failures), alert on failures and review the matrix whenever the schedule changes.

Retention choices can change storage consumption and therefore cost. For capacity and licence questions, confirm with the Microsoft licensing guide or your partner.

A finding is blocking when personal data goes live with no retention owner or rule, when a migration brings in data already past its period without a documented reason, when a deletion would cascade unintentionally, or when an erasure request cannot be carried out end to end. Gaps in evidence logging and tidy-ups are advisory. Blocking findings are not overruled by the department under review; disagreement escalates to the executive sponsor or steering committee. Retention periods and legal holds are for the organisation's DPO or legal adviser to confirm.

## Outputs

- Retention matrix per table, file type and recording type, approved by the schedule owner.
- Deletion and anonymisation job specifications, with sandbox test evidence.
- Erasure and legal hold procedures for the support team.
- Retention rules applied before migration, recorded in the `data-migration-mapping`, and retention checks in the `cutover-and-hypercare-checklist`.

## Scale notes

### SMB

Smaller organisations often have no written schedule. Help them frame the questions for their DPO or adviser instead of inventing periods, then implement the minimum: recurring bulk delete jobs for the obvious record types, a recording retention setting if voice is in scope, and an erasure procedure. Do not skip mailbox and export copies just because there are few of them.

### Enterprise

Expect a records manager, schedules that differ by country or legal entity, and legal holds raised by a central function. Long-term retention, lake exports and recordings each need a named owner, the matrix sits under change control, and the DPO receives regular evidence that jobs ran. Test deletion performance at full volume and schedule jobs outside business hours.

## Hand-offs

Running the jobs after go-live belongs to `support-operations:support-model`, with failure alerts through `platform-administration:monitoring`. Migration applies the rules via `integration-and-data:migration-strategy`, downstream copies are handled with `data-and-ai:fabric-link`, and recording settings with `customer-service:digital-and-voice-channels`. Changes to an approved matrix pass through `design-authority:change-impact-assessment`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Invent a retention period instead of taking it from the organisation's schedule.
- Run a bulk delete in production that has not been tested against production-like data in a sandbox.
- Treat deletion in Dataverse as complete while downstream copies remain.
- Migrate data already past its retention period without a documented reason.
- Delete or anonymise records that are under a legal hold.
