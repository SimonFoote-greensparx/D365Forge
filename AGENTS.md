# AGENTS.md

D365 CE Roster is an agent organisation for delivering Microsoft Dynamics 365 Customer Engagement projects: 17
departments, each installable on its own. This file describes the repository to an agent working **on** it. The skills
under `plugins/` are a different thing: they describe how to do the work of a delivery function, and they load when a
request matches their description.

## Installing, in either tool

The skills are identical. Only the manifests differ, and both are generated from `catalogue/departments.toml`, so a skill
fixed once is fixed for both.

| Tool | Manifests |
|---|---|
| Claude Code | `plugins/<department>/.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` |
| ChatGPT and Codex | `plugins/<department>/.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` |
| Microsoft Copilot Cowork | `cowork/plugins/<department>.zip`, uploaded through Customize > Plugins (see `docs/COPILOT-COWORK.md`) |

## Before you open a pull request

```
bash scripts/check-all.sh
```

Every check CI runs, in one script. The workflow calls this same file, so the two cannot drift. Scripts use the Python
standard library (3.11 or later); profile validation also needs PyYAML.

## Rules that are enforced rather than suggested

- **One owner per path.** `docs/AGENT-SURFACES.md` maps every file to exactly one agent. A new department adds its
  catalogue entry, roster row, surface block and charter in the same change.
- **Generated files are never hand-edited.** The README, both sets of manifests, each department README, each skill's
  `references/sources.md`, `docs/SOURCES.md` and the website catalogue are emitted by scripts and verified with `--check`.
  So are the Copilot Cowork archives in `cowork/plugins/` and the bundled files in each `project-tailoring` skill's
  `references/`. Change the source and run `bash scripts/build-all.sh`.
- **Skill anatomy.** Every `SKILL.md` has `name` (equal to its folder), `description` (120-450 characters, no colons),
  `license: CC-BY-4.0` and `metadata` (`department`, `stages`, `modules`, `status`, `authors`), then the sections in
  `docs/STYLE-GUIDE.md`.
- **Credit stays.** Content is CC BY 4.0 (`LICENSE`) and code is MIT (`LICENSE-CODE`). The credit to the creators, Simon
  Foote and Robert Peledie, lives in `NOTICE.md`, `CITATION.cff`, each skill's `license` and `metadata.authors`, and the
  closing credit line of each template. Never remove or change it; the checks fail if a skill or template loses it.
- **Sources are references, never copies.** `sources/*.toml` maps outside authorities to departments; the `licence` field
  decides whether an agent may quote or only cite. When torn, take the more restrictive class.
- **UK English**, by exact word form, except Microsoft product names. `python3 scripts/check-uk-english.py --fix` rewrites.
- **Trigger tests.** Every skill has at least three prompts that should load it and one near miss in `tests/triggers/`.
- **No organisation data in the repository.** Real profiles go in `input/` and generated packs in `output/`; both are
  git-ignored. Samples in `profiles/samples/` are fictional.
- **No third-party content.** All prose is original; `scripts/check-provenance.py` is the backstop.

## Departments

| Layer | Departments |
|---|---|
| Module | `sales`, `marketing`, `customer-service`, `field-service` |
| Delivery | `programme-management`, `business-analysis`, `solution-architecture`, `platform-engineering`, `integration-and-data`, `data-and-ai`, `testing-quality`, `change-adoption`, `platform-administration`, `support-operations` |
| Reviewer | `design-authority`, `security-compliance` |
| Tailoring | `project-tailoring` |
