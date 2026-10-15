---
id: data-migration-mapping
title: Data migration mapping workbook
format: xlsx
owner: integration-and-data:data-mapping-and-cleansing
tailored_from: organisation, estate, modules_in_scope, roles, generated_on
status: draft
---

# Data migration mapping workbook

## How to use this template

The data migration lead ({{roles.data-migration-lead}}) owns this workbook. Start the entity list in Initiate once the data model is drafted, complete field and value mapping during Implement, and use the cleansing and reconciliation sheets in every mock migration through to cutover. Process owners ({{roles.process-owner}}) sign off what is migrated and the value mappings for their area, because those are business decisions, not technical ones.

Sources recorded in the profile: current CRM {{estate.current_crm}}, legacy systems {{estate.legacy_systems}}, other data sources {{estate.data_sources}}.

> Guidance: Migrate the least data that lets users do their job on day one. Each extra year of history adds mapping, cleansing and reconciliation effort and rarely gets used. Retention and deletion of personal data in source systems should be agreed with the DPO or legal adviser.

> SMB: One mock migration plus a full rehearsal is the minimum. Keep reconciliation even for small volumes; it is the evidence that the go-live data is complete.

> Enterprise only: Run several mock migrations with timed loads, keep the mapping under version control, and have reconciliation checked by someone other than the person who loaded the data.

## Sheet: Read me

| Item | Detail |
|---|---|
| Organisation | {{organisation.name}} |
| Modules in scope | {{modules_in_scope}} |
| Generated on | {{generated_on}} |
| Target column names | Use logical names from the target environment, checked against the latest solution |
| Mapping status values | Draft, Agreed with process owner, Built, Tested in mock, Signed off |
| Reconciliation rule | Every record in scope is either loaded or excluded by a documented rule |

## Sheet: Entity list and load order

| Load sequence | Source object | Source system | Target table | Migrate (yes, no, archive only) | Selection or cut-off rule | Depends on | Load method | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Users and teams | Not migrated | User, team | No: created from Microsoft Entra ID | Not applicable | None | Set up, not loaded | {{roles.platform-administrator}} | |
| 2 | Reference data (currencies, territories, subjects) | {{estate.current_crm}} | Various | Yes | All active | None | Configuration data package | {{roles.data-migration-lead}} | |
| 3 | Products and price lists | {{estate.erp}} | Product, price list, price list item | Yes | Active products only | Reference data | Integration initial load | {{roles.integration-lead}} | |
| 4 | Accounts | {{estate.current_crm}} | Account | Yes | Active customers plus recent prospects | Users, reference data | Migration tool | {{roles.data-migration-lead}} | |
| 5 | Contacts | {{estate.current_crm}} | Contact | Yes | Linked to migrated accounts | Accounts | Migration tool | {{roles.data-migration-lead}} | |
| 6 | Open opportunities | {{estate.current_crm}} | Opportunity | Yes | Open only | Accounts, contacts, products | Migration tool | {{roles.data-migration-lead}} | |
| 7 | Cases | {{estate.current_crm}} | Case | Yes | Open plus agreed history period | Accounts, contacts | Migration tool | {{roles.data-migration-lead}} | |
| 8 | Activities, notes and attachments | {{estate.current_crm}} | Activity tables, note | Archive only | Agree with process owner | Parent records | Archive or migration tool | {{roles.data-migration-lead}} | |

> Guidance: Add consent records (Marketing), customer assets and agreements (Field Service) where those modules are in scope. Parents load before children; self-referencing lookups such as parent account need a second pass.

## Sheet: Field mapping

| Source object | Source field | Source type | Target table | Target column (logical name) | Target type | Required in target | Transformation rule | Default if blank | Notes | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| Company | CompanyName | Text | account | name | Single line of text | Yes | Trim spaces; title case not applied | Reject record | | Draft |
| Company | LegacyId | Text | account | (custom legacy ID column) | Single line of text | No | Copy as is | None | Keeps traceability for reconciliation and integration | Draft |
| Company | OwnerLogin | Text | account | ownerid | Lookup (user or team) | Yes | Map via user mapping table | Default owner team | Inactive owners go to the default team | Draft |
| Company | Industry | Picklist | account | industrycode | Choice | No | Value mapping set VM01 | Blank | | Draft |
| Person | Email | Text | contact | emailaddress1 | Single line of text | No | Lower case; validate format | Blank | Invalid addresses flagged in cleansing | Draft |
| Ticket | Priority | Picklist | incident | prioritycode | Choice | Yes | Value mapping set VM02 | Normal | | Draft |

> Guidance: Example source fields are illustrative; replace them with the actual names from your source extract. Confirm every target logical name in the target environment rather than from memory.

## Sheet: Value mapping

| Mapping set | Source field | Source value | Target column | Target label | Target value (from target environment) | Agreed by |
|---|---|---|---|---|---|---|
| VM01 | Industry | Retail and wholesale | industrycode | Retail | | {{roles.process-owner}} |
| VM01 | Industry | Unknown | industrycode | (blank) | | {{roles.process-owner}} |
| VM02 | Priority | P1 | prioritycode | High | | {{roles.process-owner}} |
| VM02 | Priority | P3 | prioritycode | Normal | | {{roles.process-owner}} |
| VM03 | Case status | Waiting on customer | statuscode | Waiting for details | | {{roles.process-owner}} |

## Sheet: Cleansing rules

| Rule ID | Object | Problem | How detected | Fix (in source, in transformation, manual) | Owner | Acceptance threshold for go-live | Status |
|---|---|---|---|---|---|---|---|
| CL01 | Accounts | Duplicate companies | Match on name, postcode and VAT or company number | Merge in source before final extract | {{roles.process-owner}} | Agree with process owner | |
| CL02 | Contacts | Invalid or missing email | Format check | Flag; fix in source where possible | {{roles.process-owner}} | Agree with process owner | |
| CL03 | Accounts | Missing country or postcode | Null check | Default where safe; otherwise manual fix | {{roles.data-migration-lead}} | Agree with process owner | |
| CL04 | All | Records owned by leavers | Owner not in user mapping | Reassign to owner team | {{roles.data-migration-lead}} | None remaining | |
| CL05 | Contacts | Marketing consent unclear | No consent source or date | Do not migrate as consented; refer to DPO | {{roles.data-protection-officer}} | None remaining | |

## Sheet: Reconciliation

| Object | Mock or cutover run | Source count | Excluded by rule | Expected in target | Loaded in target | Difference | Explanation | Sample check done (fields compared) | Checked by |
|---|---|---|---|---|---|---|---|---|---|
| Accounts | Mock 1 | | | | | | | | |
| Contacts | Mock 1 | | | | | | | | |
| Open opportunities | Mock 1 | | | | | | | | |
| Cases | Mock 1 | | | | | | | | |

> Guidance: Expected equals source minus excluded; any difference needs an explanation before the next run. The person in "Checked by" should not be the person who ran the load ({{roles.test-manager}} or a nominated process owner).

## Sheet: Mock migration log

| Run | Date | Target environment | Scope | Elapsed load time | Errors | Lessons and changes | Ready for next run (yes or no) |
|---|---|---|---|---|---|---|---|
| Mock 1 | | Test or SIT | Core entities | | | | |
| Mock 2 | | Test or SIT | All entities | | | | |
| Cutover rehearsal | | Pre-production or UAT | Full, timed | | | | |

> Credit: Template from D365 CE Roster by Simon Foote and Robert Peledie (https://github.com/SimonFoote-greensparx/dynamics-365-ce-roster), licensed under CC BY 4.0. Keep this credit when you share or adapt the template; in your own completed document you may keep it as a footer or remove it.
