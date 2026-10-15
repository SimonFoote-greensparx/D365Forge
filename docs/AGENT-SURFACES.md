# Agent surfaces

The write-surface map for this repository. Every file has exactly one owning agent, and no two agents claim the
same path. `scripts/check-surfaces.py` verifies both on every push.

The split is by exclusive write surface, not by topic. A topic split has no checkable boundary: two agents working on
"routing" and "SLAs" both end up editing the same skill. A surface split does.

## Classes

- **builder**: edits inside exactly one exclusive surface and never commits.
- **reviewer**: permanently read-only, holds no surface, and can always run in parallel.
- The **orchestrator** is neither: it owns no surface and is the sole committer.

People are separate from agents. Simon Foote builds and commits; Robert Peledie specifies, reviews and tests. See
`.github/CODEOWNERS` and `docs/DECISION-LOG.md` (D12).

## Roster

| id | class | status |
|---|---|---|
| `sales` | builder | installed |
| `marketing` | builder | installed |
| `customer-service` | builder | installed |
| `field-service` | builder | installed |
| `programme-management` | builder | installed |
| `business-analysis` | builder | installed |
| `solution-architecture` | builder | installed |
| `platform-engineering` | builder | installed |
| `integration-and-data` | builder | installed |
| `data-and-ai` | builder | installed |
| `testing-quality` | builder | installed |
| `change-adoption` | builder | installed |
| `platform-administration` | builder | installed |
| `support-operations` | builder | installed |
| `design-authority` | builder | installed |
| `security-compliance` | builder | installed |
| `project-tailoring` | builder | installed |
| `repo-meta` | builder | installed |
| `design-authority-review` | reviewer | installed |
| `security-compliance-review` | reviewer | installed |

Charters live in `.claude/agents/`, one per installed row. A row without a charter, or a charter without a row, fails
the check.

## Surfaces

### `sales`

```
plugins/sales/**
tests/triggers/sales.toml
editions/*/context/sales/**
```

### `marketing`

```
plugins/marketing/**
tests/triggers/marketing.toml
editions/*/context/marketing/**
```

### `customer-service`

```
plugins/customer-service/**
tests/triggers/customer-service.toml
editions/*/context/customer-service/**
```

### `field-service`

```
plugins/field-service/**
tests/triggers/field-service.toml
editions/*/context/field-service/**
```

### `programme-management`

```
plugins/programme-management/**
tests/triggers/programme-management.toml
editions/*/context/programme-management/**
```

### `business-analysis`

```
plugins/business-analysis/**
tests/triggers/business-analysis.toml
editions/*/context/business-analysis/**
```

### `solution-architecture`

```
plugins/solution-architecture/**
tests/triggers/solution-architecture.toml
editions/*/context/solution-architecture/**
```

### `platform-engineering`

```
plugins/platform-engineering/**
tests/triggers/platform-engineering.toml
editions/*/context/platform-engineering/**
```

### `integration-and-data`

```
plugins/integration-and-data/**
tests/triggers/integration-and-data.toml
editions/*/context/integration-and-data/**
```

### `data-and-ai`

```
plugins/data-and-ai/**
tests/triggers/data-and-ai.toml
editions/*/context/data-and-ai/**
```

### `testing-quality`

```
plugins/testing-quality/**
tests/triggers/testing-quality.toml
editions/*/context/testing-quality/**
```

### `change-adoption`

```
plugins/change-adoption/**
tests/triggers/change-adoption.toml
editions/*/context/change-adoption/**
```

### `platform-administration`

```
plugins/platform-administration/**
tests/triggers/platform-administration.toml
editions/*/context/platform-administration/**
```

### `support-operations`

```
plugins/support-operations/**
tests/triggers/support-operations.toml
editions/*/context/support-operations/**
```

### `design-authority`

```
plugins/design-authority/**
tests/triggers/design-authority.toml
editions/*/context/design-authority/**
```

### `security-compliance`

```
plugins/security-compliance/**
tests/triggers/security-compliance.toml
editions/*/context/security-compliance/**
```

### `project-tailoring`

```
plugins/project-tailoring/**
tests/triggers/project-tailoring.toml
editions/*/context/project-tailoring/**
```

### `repo-meta`

```
README.md
AGENTS.md
AUTHORS.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
LICENSE
.gitignore
.gitattributes
catalogue/**
data/**
profiles/**
templates/**
sources/**
scripts/**
docs/**
.github/**
.claude/**
.claude-plugin/**
.agents/**
editions/README.md
editions/*/edition.toml
tests/README.md
input/README.md
output/README.md
```

Reviewers declare no surface. That is structural rather than a promise: the check fails if a reviewer row has one.

## Reviewer independence

`design-authority` and `security-compliance` each appear twice on purpose. As departments they own their plugin
folders like any builder. As `design-authority-review` and `security-compliance-review` they are reviewer-class: they
review what other departments build, hold no surface in that capacity, and their blocking findings are not overruled by
the department under review. Disagreement escalates to the executive sponsor or steering committee.

## Rules

- One owner per path.
- A new department adds its catalogue entry, roster row, surface block and charter in the same change, or the check fails.
- Never remove a surface because it looks unused. Deprecate, announce, then remove.
- Cross-surface work moves as one coordinated change, never as two independent ones.
