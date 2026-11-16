# Roadmap

The plan runs for about 24 weeks of part-time effort by two people. Robert Peledie specified each department roughly a
phase ahead of the build and reviewed and tested it afterwards.

## Where we are

**Skills stable (16 November 2026).** All 100 skills are `status: stable` (D28), the release position for v1.0. Phase 4
is complete with the current edition fragments (D31). Microsoft Learn sources are now catalogued under Microsoft's
CC BY 4.0 licence (D30). Still to do before v1.0: the closed beta (Phase 6), the Microsoft 365 app packages (O4), and the
tagged release with the version set to 1.0.0 (Phase 7). The version stays at 0.1.0 until then.

## Phases

| Phase | Weeks | Objective | Exit criteria | Status |
|---|---|---|---|---|
| 0. Foundations | 1-2 | Agree scope, conventions and roles | Decisions D1-D16 recorded; repository protected with Rob as required reviewer | Complete. Rob as required reviewer superseded by D29 |
| 1. Walking skeleton | 3-4 | Prove build and install in both runtimes with `customer-service` | Skills install and trigger in Claude Code and ChatGPT or Codex; Rob's first review passed | Complete |
| 2. Sales and Customer Service | 5-9 | Review and harden the two most common modules and the core delivery disciplines | About 35 skills at `status: reviewed` | Complete (D25, D28) |
| 3. Marketing and Field Service | 8-12 | Review the remaining modules and their data and integration touchpoints | About 60 skills reviewed; hand-off scenarios pass Rob's tests | Complete (D25, D28) |
| 4. Reviewers, sources and editions | 11-15 | Governance, cited authorities and scale awareness | All skills reviewed; SMB and Enterprise fragments written; both editions verify | Complete (D31) |
| 5. Tailoring engine | 14-18 | Turn a profile into a tailored pack | Rob validates the SMB and enterprise sample packs against real practice | Complete; Rob's sign-off not required (D29) |
| 6. Website and beta | 17-21 | Make it usable by strangers | Public website; closed beta with 5-10 CRM practitioners; feedback triaged | In progress: website live; beta to run |
| 7. Launch | 22-24 | Release v1.0 and open to contributors | Tagged release, launch article, first external pull request reviewed | Not started |

## Milestones

| # | Milestone | Target | Evidence | Status |
|---|---|---|---|---|
| M1 | Repository live and first department installs in both runtimes | Week 4 | Recording of a skill triggering in each tool | Complete |
| M2 | Sales and Customer Service reviewed | Week 9 | About 35 skills at `status: reviewed` | Complete |
| M3 | Marketing and Field Service reviewed | Week 12 | About 60 skills reviewed; two cross-module scenarios pass | Complete |
| M4 | Reviewers, sources and editions live | Week 15 | Blocking review demonstrated; both editions verified in CI | Complete |
| M5 | Tailored pack generated from a sample profile | Week 18 | SMB and enterprise sample packs signed off by Rob | Complete; Rob's sign-off not required (D29) |
| M6 | Website live and beta complete | Week 21 | Public site; beta feedback log closed | In progress: site live; beta to run |
| M7 | v1.0 public release | Week 24 | Tagged release and launch post | Not started |

## After v1.0

- Industry packs emitted like editions (for example utilities field service, public sector case management).
- Finance and operations and Business Central touchpoints beyond the CRM side.
- A review sprint after each major Microsoft release, tracked against the AI at Work roadmap.

## Skill backlog suggested during drafting

Gaps the first draft worked around by pointing to the nearest existing skill. Each needs a capability specification
from Robert Peledie before it is built.

| Suggested skill | Department | Why |
|---|---|---|
| Benefits realisation | `programme-management` | Tracking outcomes after go-live, referenced by the charter and adoption metrics. |
| Partner selection and RFP | `programme-management` | Choosing an implementation partner before the statement of work. |
| Change control after sign-off | `programme-management` | Currently split between governance cadence and change impact assessment. |
| Self-service portal (Power Pages) | `customer-service` | Portals are mentioned by knowledge and case design but have no home. |
| Workforce management | `customer-service` | Forecasting, rostering and adherence for contact centres. |
| Data protection impact assessment | `security-compliance` | Needed by responsible AI review and new data processing. |
| Identity and access (Entra ID, conditional access) | `security-compliance` | Currently pointed at environment setup. |
| Subject access and erasure requests | `security-compliance` | Handling individual rights after go-live. |
| Data residency and sovereignty | `security-compliance` | Currently covered only through data retention. |
| Test data and masking | `testing-quality` | Safe use of production-like data in test environments. |
| Azure integration services build | `platform-engineering` | Service Bus, Functions and Logic Apps implementation detail. |
| Marketing and journey analytics | `marketing` | Currently pointed at reporting strategy. |
