---
name: field-level-security
description: Decides which Dataverse columns need column-level protection, designs field security profiles and checks that the protection holds in exports, reports and integrations, classifying findings as blocking or advisory. Use when values such as salary, bank details or vulnerability flags must be hidden from some users who can see the record.
license: CC-BY-4.0
metadata:
  department: security-compliance
  stages: Implement, Prepare, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Field-level security

Row-level security decides which records a user sees; field-level security decides which columns on those records they can read or change. It is the right tool when most of a record is shared widely but a few values are not: bank details on an account, a vulnerability flag on a case, a credit limit, a health note. Dataverse now describes this as column-level security with column security profiles, so check current Microsoft Learn documentation for the present naming and behaviour.

Projects go wrong in two directions. Some secure dozens of columns just in case, which makes forms confusing and testing expensive. Others secure the column on the form and forget that the same value leaves through Excel exports, lake exports, Power BI datasets and integrations running under accounts that see everything.

## When to use

- A requirement says some users may see a record but not certain values on it.
- Special category or financial data is being added to a table that many people use.
- Reports, exports or integrations are being designed for tables that hold secured columns.
- Before UAT or go-live, to confirm that column protection holds on every route.

Not this skill: `security-compliance:security-model-review` for access to whole records and tables, `security-compliance:data-retention` for how long the values are kept, `data-and-ai:power-bi-on-dataverse` for designing the reports themselves.

## Questions to ask first

1. Which columns are sensitive, and what makes each sensitive? The reason decides whether column security, a separate table or no control at all is right.
2. Who must read each column, and who must change it? Readers and writers are often different groups and need different profiles.
3. Where does the value travel after Dataverse (reports, lake or Fabric exports, integrations, Excel)? Protection that stops at the form is not protection.
4. Is the sensitivity about a few columns or a whole cluster of related data? Clusters are often better as their own table.
5. Which plug-ins, flows and integrations read or write these columns, and under which identity? Automation breaks quietly when it lacks the profile.

## Approach

Begin with a column register rather than with the settings. For each candidate record the table, the column, why it is sensitive, who reads it, who changes it and where it travels. Many candidates drop out here because they are not sensitive on their own, and the rest now have a stated reason that the review can test.

1. Choose the mechanism. Column security suits a few sensitive values on a table that many people use. When a cluster of sensitive data belongs together (support needs, safeguarding notes, financial assessments), a separate related table protected by its own role privileges is often cleaner, easier to audit and easier to report on.
2. Design profiles by need, usually a read-only and a read-write profile per sensitive group of columns. Assign them to teams, ideally Entra ID group teams, rather than to individuals.
3. Remember who bypasses it. Users holding System Administrator see secured values regardless of profile, so keep that role to a small named group.
4. Check indirect routes. Calculated and rollup columns, duplicate detection, search, document templates and email templates can surface a secured value indirectly. Check current Microsoft Learn documentation for how each behaves before relying on it.
5. Follow the data out. Lake and Fabric exports, Power BI import models and integration accounts may read secured values under a service identity. Treat every downstream copy as its own access decision and record who can see the value there.
6. Cover automation. Plug-ins, cloud flows and integrations that touch a secured column need an identity with the right profile, otherwise they fail or write blanks. Name each identity in the register.
7. Test negatively. Sign in as each persona and try the form, views, Advanced Find, export to Excel, the mobile app and the Web API. Newer masking options may exist; check current documentation before designing around them.

A finding is blocking when a sensitive value is readable by people outside its register entry through any route, when a process identity has wider column access than it needs, or when no negative test has been run. Unnecessary secured columns, inconsistent profile names and thin register entries are advisory. Blocking findings are not overruled by the department under review; disagreement escalates to the executive sponsor or steering committee. Whether a column holds special category data, and what that requires, is a question for the organisation's DPO or legal adviser.

## Outputs

- Column security register: table, column, reason, readers, writers, profile, downstream copies and process identities.
- Profile design with team assignments, referenced in the `solution-blueprint`.
- Negative test cases for the `test-strategy-and-uat-scripts`.
- Findings log, with blocking items mirrored in the `raid-log`.

## Scale notes

### SMB

Expect a few secured columns and one or two profiles. The trap on small projects is that the person administering the system is often the one person who should not see the value (salaries, for example), and System Administrator shows them everything. Resolve that before securing anything, and still check exports and the accounting integration.

### Enterprise

Keep the register under change control, with a data owner per sensitive group of columns and profiles per legal entity where rules differ. The data-and-ai-lead confirms how each downstream copy treats secured values. Recertify profile membership periodically and include column checks in automated regression tests.

## Hand-offs

The profile design goes to `security-compliance:security-model-review` so rows and columns are signed off together. Downstream treatment goes to `data-and-ai:fabric-link` and `data-and-ai:power-bi-on-dataverse`, process identities to `platform-engineering:plugin-design`, and negative tests to `testing-quality:user-acceptance-testing`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Rely on removing a column from a form as protection.
- Secure a column without a recorded reason, list of readers and list of writers.
- Assume a lake export or Power BI model enforces the same column rules as Dataverse.
- Give System Administrator to people who must not see the secured values.
- Decide whether data is special category without the DPO or legal adviser.
