# Editions

An edition is the core library made specific to one scale. `scripts/build-edition.py` reads an edition's config and
emits a standalone tree into `dist/` (git-ignored): the whole core, with context fragments spliced into the skills they
extend.

```
python3 scripts/build-edition.py smb               emit dist/dynamics-365-ce-roster-smb/
python3 scripts/build-edition.py --all --verify    emit each edition to a temporary folder, validate it, keep nothing (CI runs this)
```

## Layout

```
editions/<edition>/edition.toml                      what the edition is
editions/<edition>/context/<department>/<skill>.md   extends that core skill
```

A fragment carries its own `##` heading and is spliced immediately before the skill's `## Never` section. A fragment for
a skill that does not exist fails the build. An edition may also drop departments it has no use for with
`exclude_departments`.

## The rule

Generation is one-way. The emitted tree is never hand-edited; an edit made downstream is lost on the next emit. A core
skill that is wrong for every scale is fixed in the core.

## Status

Both editions are placeholders with one example fragment each. Every core skill already carries SMB and Enterprise notes;
fragments are for detail that would clutter the core, and will be written during Phase 4 of the roadmap.
