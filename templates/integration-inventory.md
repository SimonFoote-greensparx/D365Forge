---
id: integration-inventory
title: Integration inventory
format: xlsx
owner: integration-and-data:integration-architecture
tailored_from: organisation, estate, edition, modules_in_scope, roles, generated_on
status: draft
---

# Integration inventory

## How to use this template

The integration lead ({{roles.integration-lead}}) starts this inventory in Initiate, from the systems listed in the organisation profile and the fit-to-standard workshops, and the solution architect ({{roles.solution-architect}}) approves it as part of the solution blueprint. Each interface then carries its status through build, SIT and go-live. Update it whenever an interface is added, its pattern changes or a source system owner changes their API.

> Guidance: The commonest integration failure on CRM projects is not technical: it is discovering late that nobody agreed which system owns the customer or product record. Complete the "Data ownership" sheet before designing any interface.

> SMB: Favour standard connectors and simple scheduled or event-driven flows. Keep the inventory even if there are only three interfaces; it becomes the support team's map after go-live.

> Enterprise only: Add middleware design references, interface contracts with version numbers, non-functional targets agreed with each system owner, and a separate SIT scenario per interface.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Edition | {{edition}} |
| Modules in scope | {{modules_in_scope}} |
| Systems listed in profile | ERP {{estate.erp}}; email and calendar {{estate.email_and_calendar}}; telephony {{estate.telephony}}; other {{estate.integrations}} |
| Generated on | {{generated_on}} |
| Direction values | Inbound to Dynamics 365, Outbound from Dynamics 365, Bidirectional |
| Status values | Identified, Designed, Built, SIT passed, Live, Retired |

## Sheet: Systems

| System | Business owner | Technical contact | System of record for | Hosting | Integration options available | Change or release cycle | Notes |
|---|---|---|---|---|---|---|---|
| {{estate.current_crm}} | | | Current customer data (until cutover) | | Export or API | Frozen after cutover | Source for migration, not an ongoing interface unless dual running |
| {{estate.erp}} | | | Customers for billing, products, prices, orders, invoices | | | | |
| {{estate.email_and_calendar}} | | | Email, appointments | | Server-side synchronisation | | |
| {{estate.telephony}} | | | Calls | | | | Customer Service only |
| Microsoft Entra ID | | | Users and groups | Cloud | Group teams, licence assignment | | |
| {{estate.data_sources}} | | | | | | | |

## Sheet: Interfaces

| ID | Interface | Source | Target | Business purpose | Data objects | Direction | Trigger | Pattern | Volume and frequency (to measure) | Error handling | CRM owner | Module | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| INT01 | Customer master sync | {{estate.erp}} | Dataverse | Keep billing accounts aligned | Account, contact, address | Bidirectional | Event | Middleware or connector | | Retry, then alert support queue | {{roles.integration-lead}} | Sales, Field Service | MVP | Identified |
| INT02 | Products and price lists | {{estate.erp}} | Dataverse | Sellers quote from current catalogue | Product, unit, price list item | Inbound | Scheduled | Middleware or connector | | Log and alert | {{roles.integration-lead}} | Sales | MVP | Identified |
| INT03 | Orders to ERP | Dataverse | {{estate.erp}} | Fulfil and invoice won business | Order, order line | Outbound | Event | Middleware or API | | Retry, then manual queue | {{roles.integration-lead}} | Sales | MVP | Identified |
| INT04 | Email and calendar | {{estate.email_and_calendar}} | Dataverse | Track email and appointments | Email, appointment | Bidirectional | Real-time | Server-side synchronisation | | Mailbox alerts | {{roles.platform-administrator}} | All | MVP | Identified |
| INT05 | Telephony and screen pop | {{estate.telephony}} | Dataverse | Identify caller, log calls | Phone call, conversation | Inbound | Real-time | Vendor connector or Dynamics 365 Contact Center | | Vendor monitoring | {{roles.integration-lead}} | Customer Service | Confirm | Identified |
| INT06 | Website forms | Website | Dataverse | Capture enquiries and consent | Lead, contact, consent | Inbound | Event | Customer Insights - Journeys forms | | Form submission monitoring | {{roles.journeys-consultant}} | Marketing | Confirm | Identified |
| INT07 | Parts and stock | {{estate.erp}} | Dataverse | Technicians see stock and use parts | Product, warehouse, inventory | Bidirectional | Scheduled | Middleware or connector | | Log and alert | {{roles.integration-lead}} | Field Service | Confirm | Identified |
| INT08 | Analytics export | Dataverse | Analytics platform | Reporting across systems | Selected tables | Outbound | Scheduled | Platform export feature | | Pipeline monitoring | {{roles.data-and-ai-lead}} | All | Later | Identified |

> Guidance: Delete rows that do not apply and add one per interface in {{estate.integrations}}. Record measured volumes, not guesses, and check current Microsoft Learn documentation for service protection limits before designing high-volume loads.

## Sheet: Data ownership

| Data object | System of record | Role of Dynamics 365 (master, copy, reference) | Who may edit in Dynamics 365 | Sync direction | Conflict rule | Agreed by |
|---|---|---|---|---|---|---|
| Customer (account) | | | | | | {{roles.process-owner}} |
| Contact | | | | | | |
| Product and price | {{estate.erp}} | Copy | Nobody; read-only | Inbound | ERP wins | |
| Order | | | | | | |
| Invoice | {{estate.erp}} | Reference | Nobody | Inbound | ERP wins | |
| Customer asset | | | | | | |

## Sheet: Non-functional and support

| Interface ID | Peak volume | Latency needed | Retry approach | Alerting and monitoring | Authentication | Support owner after go-live | Runbook reference |
|---|---|---|---|---|---|---|---|
| INT01 | | | | | Service principal or app registration | {{roles.support-lead}} | |
| INT03 | | | | | | | |
| INT04 | | | | Mailbox status alerts | | {{roles.platform-administrator}} | |

> Guidance: Every interface needs a named support owner and a documented way to replay failed messages before it goes live.

## Sheet: Test coverage

| Interface ID | SIT scenario | Test data required | Environment pairing | Negative tests (failure, duplicates, late arrival) | Result | Tested by |
|---|---|---|---|---|---|---|
| INT01 | New customer created in ERP appears in Dynamics 365 | Test customer set | SIT with ERP test | ERP unavailable; duplicate key | | |
| INT03 | Won opportunity creates order in ERP | Priced products | SIT with ERP test | Missing product in ERP | | |
| INT04 | Tracked email appears on contact timeline | Pilot mailboxes | SIT | Mailbox not approved | | |
