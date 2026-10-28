---
name: edition-selection
description: Recommends the SMB or Enterprise edition of D365Forge for a project from its modules, user numbers, integrations, legal entities and team size, giving the reason for each signal and explaining borderline cases. Use when tailoring starts, when someone asks whether their project is SMB or Enterprise, or when scope changes.
license: CC-BY-4.0
metadata:
  department: project-tailoring
  stages: Strategize, Initiate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# Edition selection

The edition decides how much structure the project carries. The SMB edition assumes one or two apps, a small partner-led team, one consultant covering several roles and mostly standard configuration. The Enterprise edition assumes several modules in parallel, a workstream per module, a design authority, multiple environments and pipelines, formal SIT and UAT, and benefits realisation. Choose too light and a complex programme runs without the controls it needs; choose too heavy and a small rollout drowns in documents nobody reads.

The edition is a delivery approach, not a Microsoft licence. Microsoft licence names can use similar words, so never infer licences from the edition or the edition from licences. For licensing questions, confirm with the Microsoft licensing guide or your partner.

## When to use

- A validated profile is ready and the pack needs an edition.
- Someone asks whether their project counts as SMB or Enterprise, or why D365Forge chose one.
- The profile sets an edition preference that may not match the signals.
- Scope, team or estate has changed enough to question the earlier choice.

Not this skill: `project-tailoring:profile-intake` to gather or fix the facts, `project-tailoring:role-mapping` to fill roles once the edition is known, `platform-administration:licensing-and-capacity` for licences and capacity.

## Questions to ask first

1. Which modules are in scope, and will they be delivered in parallel or in sequence? Parallel delivery is the strongest single signal.
2. How many users, in how many distinct populations, sites and countries? Training, testing and support scale with populations more than with headcount.
3. How many integrations, and do any need middleware, real-time exchange or more than one system of record? Integration complexity drives SIT and environments.
4. How many legal entities are involved? Use the profile value if present; otherwise infer from countries and the ERP set-up and ask if unclear.
5. How is the delivery team shaped: one partner consultant with customer staff, or several workstreams? Team shape decides whether one person can sensibly hold several roles.

## Approach

Read the profile and note the edition preference. If it is auto, the recommendation decides. If the user set smb or enterprise, honour the choice but still run the assessment and say plainly where the signals disagree.

Assess each signal as leaning SMB, leaning Enterprise or neutral, with a one-line reason drawn from the profile.

1. Modules. One or two apps delivered together lean SMB. Several modules in parallel, or a module that depends heavily on another (Field Service with Customer Service and ERP stock, for example), lean Enterprise.
2. Users. One population that can be trained in a single wave leans SMB. Several populations, shift patterns, sites or countries lean Enterprise.
3. Integrations. Standard connections such as Outlook, Teams and one scheduled ERP feed lean SMB. Middleware, real-time flows, several systems of record or anything that needs formal SIT leans Enterprise.
4. Legal entities. One entity leans SMB. Several entities with different processes, currencies, languages or regulators lean Enterprise, partly because of the security model they imply.
5. Team size. A partner consultant with a few customer staff leans SMB. A team large enough for a workstream per module, with dedicated test and release roles, leans Enterprise.

When the signals agree, recommend and move on. When they split, the project is borderline. Apply tie-breakers in this order: regulatory and compliance constraints, modules in parallel, then integration complexity, because missing controls in those areas are the most expensive to fix later. Do not invent numeric thresholds to make a borderline case look clear-cut; the reasons are the recommendation.

A borderline recommendation names the edition, lists the signals against it and names the practices to borrow from the other edition. A single-module rollout across several legal entities might stay SMB but borrow a light design authority and a UAT cycle per entity. A multi-module programme with a small team might take Enterprise governance while combining roles within the role combination rules.

Close with what would flip the decision, such as bringing Marketing into the first release, adding a second ERP or losing a key team member. That gives the project lead a clear trigger for a pack refresh.

## Outputs

- Edition recommendation with the reason for each of the five signals, recorded in the `project-charter`.
- Borderline note listing practices borrowed from the other edition, reflected in the `delivery-plan` and the `environment-and-alm-strategy`.
- Flip conditions, logged as assumptions in the `raid-log`.

## Scale notes

### SMB

When recommending SMB, also name what must not be dropped on a small project: a separate test environment, UAT with real users, a cutover checklist and an independent look at the security model. Small does not mean ungoverned. Keep the explanation short, because the audience is usually an owner or a single project lead.

### Enterprise

When recommending Enterprise, name the controls that switch on (design authority, workstream leads, environment pipeline, SIT, benefits tracking) and the roles that must be separate people. If the case was borderline, say which Enterprise controls can stay light so the project does not import ceremony it cannot staff.

## Hand-offs

The decision goes to `project-tailoring:role-mapping`, which uses it to select roles, and to `project-tailoring:document-pack`. Governance and environment consequences go to `programme-management:governance-cadence` and `solution-architecture:environment-strategy`. No reviewer sign-off is needed; the project lead or executive sponsor confirms the edition.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the role catalogue (`references/role-catalogue.json`), which records which roles each edition expects as separate seats. In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`, with the TOML data files bundled as JSON.

## Never

- Present the D365Forge edition as a Microsoft licence, or infer licences from it.
- Recommend an edition without stating the reason for each signal.
- Override an explicit edition preference silently, in either direction.
- Invent thresholds, statistics or costs to settle a borderline case.
- Drop UAT, a test environment or the security review because a project is SMB.
