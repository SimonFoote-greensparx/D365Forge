# Templates

The project documents the `project-tailoring:document-pack` skill fills from an organisation profile and a role mapping,
then exports to Word (`docx`) or Excel (`xlsx`) in `output/`. Each template is Markdown with frontmatter, so it can be
reviewed in a pull request like any skill.

## Frontmatter

| Field | Meaning |
|---|---|
| `id` | Equals the file name. |
| `title` | The document title. |
| `format` | `docx` or `xlsx`. |
| `owner` | The `department:skill` that owns the content. |
| `tailored_from` | The profile sections and computed inputs used. |
| `status` | `draft`, `reviewed` or `stable`. |

## Placeholders

| Placeholder | Filled from |
|---|---|
| `{{organisation.name}}`, `{{goals.target_go_live}}` and other dotted paths | The organisation profile (`profiles/schema.json`). |
| `{{edition}}` | `project-tailoring:edition-selection`: SMB or Enterprise. |
| `{{modules_in_scope}}` | The modules with `in_scope: true`. |
| `{{roles.<role-id>}}` | The person or alias proposed for that role by `project-tailoring:role-mapping`. Role ids are in `data/role-catalogue.toml`. |
| `{{team_table}}`, `{{gaps_table}}` | Tables built by `project-tailoring:role-mapping` and `project-tailoring:skills-gap-analysis`. |
| `{{generated_on}}` | The date the pack was produced. |

Guidance for the person completing a document is in blockquotes starting `> Guidance:`; scale-specific notes start
`> SMB:` or `> Enterprise only:`. In `xlsx` templates, each `## Sheet: <name>` heading and the table under it becomes
a worksheet; example rows are there to be edited or deleted.

## Adding a template

Add the file, reference it from the owning skill's Outputs section, list it in `project-tailoring:document-pack`, then run
`bash scripts/build-all.sh`. `scripts/check-data.py` checks the frontmatter, the owner and every role placeholder.
