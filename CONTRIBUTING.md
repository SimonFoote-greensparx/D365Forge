# Contributing

Thank you for helping. D365Forge gets better when practitioners tell us where a skill gives the wrong answer, fails
to load, or misses how real CRM projects work.

## The most useful contributions

1. **A situation the library handles badly.** Open an issue with the question you asked, what loaded, and what a good
   practitioner would have said. A skill that exists but fails to trigger, or triggers and answers the wrong question, is
   more common than a missing skill.
2. **A correction** where a skill is wrong, out of date or too generic.
3. **A source** that settles a question the skills currently answer from judgement alone.
4. **A new skill or department**, after discussing it in an issue first.

## How work flows

| Stage | Who | What happens |
|---|---|---|
| Specified | Robert Peledie | A capability specification (`docs/CAPABILITY-SPEC-TEMPLATE.md`) says what the skill must cover and how it will be tested. |
| Building | Simon Foote or a contributor | The skill, its trigger tests and any source entries are written on a short-lived branch. |
| In review | Robert Peledie | Content review, trigger tests run in at least one tool, reviewer-class gates checked. |
| Done | Maintainers | Merged once `bash scripts/check-all.sh` passes and the review is approved. |

## Writing a skill

Read `docs/STYLE-GUIDE.md` first. In short:

- One folder per skill: `plugins/<department>/skills/<skill>/SKILL.md`. The frontmatter `name` equals the folder name.
- The frontmatter carries `license: CC-BY-4.0` and `metadata.authors: Simon Foote, Robert Peledie`, unchanged.
- Files inside a skill folder use types Microsoft 365 Copilot accepts, such as `.md`, `.json`, `.yaml` or `.csv`, not
  `.toml`. `scripts/build-cowork.py` lists them and fails the checks otherwise.
- The description says what the skill does and when to use it, in 120-450 characters, with no colons.
- Sections in order: When to use, Questions to ask first, Approach, Outputs, Scale notes (SMB and Enterprise), Hand-offs,
  Sources, Never.
- UK English, original prose, durable judgement rather than version-specific claims, and no invented statistics.
- Add at least three should-trigger prompts and one near miss to `tests/triggers/<department>.toml`.

Then regenerate and check:

```
bash scripts/build-all.sh
```

## Adding a department

In one change: add it to `catalogue/departments.toml`, add a roster row and surface block to `docs/AGENT-SURFACES.md`,
add a charter at `.claude/agents/<id>.md`, create `plugins/<id>/skills/`, and run `bash scripts/build-all.sh`. The
surface check fails if any part is missing.

## Ground rules

- No client or employer material, names or data. Write from general practice.
- No copied text from Microsoft Learn or any other publisher. Cite through `sources/`.
- Licensing, legal and data-protection questions are structured, not answered: skills point to the Microsoft licensing
  guide, a partner, the DPO or a legal adviser.
- Be kind. See `CODE_OF_CONDUCT.md`.

By contributing you agree that your contribution is licensed under the same terms as the rest of the repository:
content under CC BY 4.0 ([LICENSE](LICENSE)) and code under MIT ([LICENSE-CODE](LICENSE-CODE)). You also confirm that
you have the right to submit it; if you wrote it as part of your job, check that your employer agrees. Contributors
are credited in the git history and, for substantial contributions, in [AUTHORS.md](AUTHORS.md). Do not remove or
change the credit to the original creators, Simon Foote and Robert Peledie, in skill frontmatter, templates,
[NOTICE.md](NOTICE.md) or [CITATION.cff](CITATION.cff).
