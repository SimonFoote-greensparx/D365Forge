# Tests

## Trigger tests

`tests/triggers/<department>.toml` holds, for every skill, at least three prompts that should load it and at least one
near miss that should load a different skill. Robert Peledie owns them. `scripts/check-triggers.py` checks they exist and
are well formed; running them is manual for now:

1. Install the department in Claude Code, and in ChatGPT or Codex.
2. Ask each `should_trigger` prompt in a fresh conversation and note which skill loads.
3. Ask each `should_not_trigger` prompt and confirm the `expected` skill loads instead.
4. Record failures as issues labelled `trigger`.

## Scenario tests

The cross-module situations in `docs/USE-CASES.md` are run end to end before a department moves to `status: reviewed`.

## Placeholders

- `tests/scenarios/`: scripted versions of the use cases, once the manual runs settle.
- `tests/packs/`: expected outputs for the two sample profiles, once the tailoring engine is reviewed.
