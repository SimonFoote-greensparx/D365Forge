---
name: role-mapping
description: Proposes who holds each delivery role by matching declared skills and availability against the role catalogue, gives a one-line reason per role, flags uncovered, over-allocated and unsafe role combinations, and never ranks people. Use when a profile lists the team and the project lead needs a first role assignment to confirm.
metadata:
  department: project-tailoring
  stages: Strategize, Initiate
  modules: All
  status: draft
---

# Role mapping

A Dynamics 365 CE project fails quietly when a role nobody holds turns out to matter: no one owns data migration until the first mock load fails, or the only developer ends up signing off their own testing. Mapping roles early makes those gaps visible while there is still time to train, contract or bring in a partner.

The mapping is a proposal built from what people have declared about their own skills and availability. It does not assess anyone's performance, rank people against each other or use personal characteristics, and it is not final until the project lead confirms it.

## When to use

- A validated profile lists the team and the edition is decided.
- The project lead wants a first view of who could hold each role, and which roles nobody covers.
- Someone asks whether one person can safely hold two roles.
- The team changes and the mapping needs a fresh proposal.

Not this skill: `project-tailoring:skills-gap-analysis` to decide how uncovered roles are filled, `project-tailoring:edition-selection` for the edition that decides which roles need separate seats, `programme-management:governance-cadence` for steering and decision forums.

## Questions to ask first

1. Which edition and which modules are in scope? Together they decide which catalogue roles are needed and which can be combined.
2. What has each person declared: skills, levels, availability and whether they are internal? These are the only evidence the mapping uses.
3. How much of each role's time does this project need? Without an estimate over-allocation cannot be checked, so ask the project lead where the catalogue gives none.
4. Which roles will the partner hold? Partner roles still need a named alias and still obey the combination rules.
5. Should people appear by alias or by name? Aliases are the default.

## Approach

1. Select the roles. The role catalogue is the authority for which roles exist, the skills each requires and desires, the module that makes it relevant and the editions that expect it as a separate seat. Include every role whose module is all or is in scope. In the SMB edition, roles not expected as separate seats are still responsibilities; use the catalogue's SMB note to fold them into another role (a business analyst combined with the module consultant, for example).
2. Match declared skills. For each role, list the people whose declared skills cover its required skills. The catalogue lists skills without levels, so apply one stated rule: advanced or expert covers a lead role, working covers it with support, awareness does not cover it. Mark anyone who meets the rule only partly as a partial match. Do not infer skills from current role or job title.
3. Propose a holder. Choose a match who has availability, preferring the option that avoids combination conflicts and spreads load. Give a one-line reason quoting declared facts only, such as declares security-design at advanced, 40 percent available, 15 percent allocated here. List other matching people alphabetically by alias, without scores, so the project lead can choose differently.
4. Check allocation. Add up each person's allocations and compare them with their declared availability. Flag every over-allocation rather than quietly trimming roles.
5. Apply the combination rules. Check every rule in the role combination rules. An unsafe pairing, such as a developer who would also sign off testing, is never proposed. A caution pairing, such as the security-lead also being the design-authority-lead, may be proposed with its reason stated and its mitigation named, for example an independent review of the security design.
6. Keep ownership roles with the organisation. The executive-sponsor and process-owner roles belong to internal people. The data-protection-officer role maps to whoever the organisation has already appointed, internal or external; the project does not appoint one.
7. Flag gaps. List uncovered roles and partial matches separately, ready for the skills gap analysis.

Present the result as a proposal with a status on every line: proposed, confirmed, partial, uncovered or conflict. The project lead confirms or changes each line, ideally after checking with the person concerned, and only confirmed lines flow into the RACI as settled.

## Outputs

- Role mapping table: role id, proposed holder by alias, one-line reason, allocation and status.
- Over-allocation and combination list with the rule, its severity and the proposed alternative or mitigation.
- Uncovered roles and partial matches for the skills gap analysis.
- The confirmed mapping, which feeds the `raci-matrix` and the `resource-and-skills-gap-plan`.

## Scale notes

### SMB

One consultant covering several roles is normal and expected, so most attention goes to the combination rules and to availability. A managing director at a tenth of their time can sponsor but cannot also be the process owner for three processes. Make sure the person who builds is never the one who accepts the testing, even if that means a process owner signs off UAT with partner support.

### Enterprise

Expect a holder per role and per module workstream, with the security-lead and design-authority-lead separate from the people building. Map at workstream level, refresh the mapping at each stage gate, and involve line managers in confirming availability. The mapping holds declared skill levels, so share it with the project leadership only.

## Hand-offs

Uncovered and partial roles go to `project-tailoring:skills-gap-analysis`, and the confirmed mapping to `project-tailoring:document-pack`. Named sponsors and owners appear in `programme-management:project-charter`. If the mapping leaves security design without an independent reviewer, raise it with `security-compliance:security-model-review` before build starts.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

The shared files this skill reads are bundled with it, so it works wherever the department is installed, including Copilot Cowork: the role catalogue (`references/role-catalogue.toml`), the role combination rules (`references/role-combinations.toml`) and the skills vocabulary (`references/skills-vocabulary.toml`). In a clone of the repository the originals are in `data/`, `templates/` and `profiles/`; the bundled copies are regenerated from them by `scripts/build-bundles.py`.

## Never

- Rank people, score them against each other or comment on anyone's performance.
- Use age, gender, health or any other personal characteristic, or infer skills from a job title.
- Present the mapping as final before the project lead has confirmed it.
- Propose a pairing that the role combination rules mark as unsafe.
- Show real names when the profile asks for aliases.
