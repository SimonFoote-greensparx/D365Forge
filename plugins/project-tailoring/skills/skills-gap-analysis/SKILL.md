---
name: skills-gap-analysis
description: Lists the delivery roles the team cannot cover from declared skills and availability and recommends training, a contractor or a partner for each, with the reason and the stage by which it is needed. Use when role mapping shows gaps, when planning outside help or when deciding who will own the platform after go-live.
license: CC-BY-4.0
metadata:
  department: project-tailoring
  stages: Strategize, Initiate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Skills gap analysis

Every CRM project has gaps; the damage comes from finding them late. A missing data-migration-lead is cheap to solve in Initiate and expensive in Prepare. The second failure is filling every gap with a partner and going live with nobody inside the organisation able to run, support or change the platform.

This skill works from roles, not people. It says what a role needs and that nobody on the team has declared it at that level, or has the availability to take it on. It never describes an individual as weak and never assesses performance.

## When to use

- Role mapping has produced uncovered roles, partial matches or over-allocations.
- The project needs to decide what to train for, what to contract and what to buy from a partner.
- A budget or statement of work discussion needs a reasoned list of outside help.
- The organisation wants to know who will own the platform once the partner leaves.

Not this skill: `project-tailoring:role-mapping` to propose who holds each role, `change-adoption:role-based-training` for training end users, `programme-management:statement-of-work` to contract the partner.

## Questions to ask first

1. Which roles are uncovered, partly covered or over-allocated after role mapping? These are the inputs; this skill does not re-map people.
2. When is each role needed, and is it still needed after go-live? Durable roles favour building internal capability.
3. How deep is the need: enough to work alongside a partner, or enough to lead? Depth and lead time decide whether training is realistic.
4. What do the budget band and any existing partner arrangement allow? A partner already engaged changes the simplest route.
5. Which roles carry real risk if learned on the job (security, data migration, data protection)? Those need experienced hands even when training is also planned.

## Approach

Take each gap from the role mapping and choose a primary route and, where useful, a secondary one. Most good answers are combinations, such as a partner delivering while an internal person shadows.

1. Training suits roles the organisation must own after go-live, such as platform-administrator, support-lead, knowledge-manager, power-platform-maker and trainer, and gaps of one level where someone already declares the skill at working level. It takes time, so compare the realistic lead time with the stage when the role starts, and never plan training that ends after the role is needed.
2. A contractor suits a deep, time-bound need for one role, such as a data-migration-lead through the mock migrations or a deliverability-specialist while sending domains are set up, provided the organisation can direct an individual day to day.
3. A partner suits gaps that span a workstream or several linked roles (Field Service with scheduling and mobile, for example) or where accountability for delivery quality should sit with a firm under a statement of work.

Then apply the rules that outrank convenience and cost:

- Ownership roles stay inside. The executive-sponsor and process-owner roles cannot be contracted out. The data-protection-officer is whoever the organisation has appointed; a gap there is raised with leadership, not filled by the project.
- Durable roles held by a contractor or partner come with an internal successor route and a shadowing plan, so knowledge does not leave with them.
- Over-allocation is a capacity gap, not a skills gap. Backfill the person's day job or add capacity rather than recommending more training.
- Some gaps exist only because of the role combination rules, such as an independent reviewer for security design. These may need an outside reviewer simply because nobody inside is free of the conflict.

For training, name the capability and the form of learning (Microsoft Learn paths, partner-led workshops, shadowing) and check current Microsoft Learn for the present paths and certifications rather than quoting exam codes. Offer training to people who have declared interest or a related skill; the analysis never names anyone as needing remediation. Do not quote day rates, prices or market statistics. Describe cost relative to the profile's budget band and leave figures to the organisation and its partner.

## Outputs

- The `resource-and-skills-gap-plan`: role id, gap type, primary and secondary route, reason, needed-by stage and owner.
- Project team training needs for the `training-and-communications-plan`.
- Contractor and partner needs for the `delivery-plan`, and the related risks in the `raid-log`.

## Scale notes

### SMB

The partner usually covers most delivery roles, so the real question is who owns the system afterwards. Always name an internal platform owner route (often an office or IT administrator already declaring Power Platform skills at working level) and plan their training and shadowing. Keep the plan to a page.

### Enterprise

Group gaps by workstream and allow for procurement and onboarding lead times, including any vetting the organisation requires before contractors get access. Build a capability plan for the post-go-live team alongside the delivery gaps, and keep the plan under the same change control as the role mapping.

## Hand-offs

Partner scope goes to `programme-management:statement-of-work`, post-go-live ownership to `support-operations:support-model`, and the completed plan into `project-tailoring:document-pack`. No reviewer sign-off is needed; the project lead and executive sponsor approve spending on training, contractors and partners.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the role catalogue (`references/role-catalogue.json`) and the skills vocabulary (`references/skills-vocabulary.json`). In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`, with the TOML data files bundled as JSON.

## Never

- Describe an individual as weak, rank people or comment on anyone's performance.
- Invent day rates, prices, salaries or market statistics.
- Recommend a contractor or partner for the executive-sponsor or process-owner role.
- Plan training that finishes after the role is needed.
- Hand a durable platform role to a partner without an internal successor route.
