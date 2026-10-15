# Source catalogue

The outside authorities that settle questions the skills cannot settle on their own: Microsoft's own documentation
for how a feature behaves, Microsoft's licensing resources for what is licensed, and regulators for what the law
requires. `scripts/build-sources.py` emits a `references/sources.md` into every skill whose department a source
serves, and an index at `docs/SOURCES.md`.

**References, never copies.** The catalogue holds a pointer, who publishes it, what it is authoritative for and what
you may do with it. Nothing here reproduces source text. A pointer stays current when Microsoft changes the product;
a copy is out of date the next month.

## Fields

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique, lowercase, hyphenated. |
| `title` | yes | The document's own title. |
| `publisher` | yes | Who publishes it. |
| `url` | yes | Where to read it. Checked weekly by `.github/workflows/links.yml`. |
| `licence` | yes | One of the values below. Decides whether an agent may quote or only cite. |
| `jurisdiction` | yes | `Global`, `UK`, `EU` and so on. |
| `authoritative_for` | yes | One sentence: what question this source settles. |
| `departments` | yes | Department ids whose skills should read this source. |
| `skills` | no | Extra `department:skill` references outside those departments. |
| `checked` | yes | Date the entry was last verified (YYYY-MM-DD). |

## The licence field

| `licence` | Meaning | What an agent may do |
|---|---|---|
| `cite-only` | Free to read, not licensed for reuse here | Name it, link it, summarise in your own words. Do not reproduce text. |
| `check-terms` | Reuse terms not yet confirmed by the maintainers | Treat as `cite-only` until confirmed. |
| `ogl-v3` | UK Open Government Licence v3.0 | Quote and reuse with the required attribution. |
| `cc-by-4.0` | Creative Commons Attribution 4.0 | Quote and reuse with attribution. |
| `public-domain` | No copyright restriction | Quote and reuse freely. |

When in doubt between two classes, choose the more restrictive one. Upgrading an entry from `check-terms` to a reuse
licence needs a decision-log entry citing the publisher's terms.

## Adding a source

1. Add a `[[source]]` block to the most relevant file in this folder.
2. Run `python3 scripts/build-sources.py` to regenerate the per-skill lists and `docs/SOURCES.md`.
3. Run `bash scripts/check-all.sh`.
