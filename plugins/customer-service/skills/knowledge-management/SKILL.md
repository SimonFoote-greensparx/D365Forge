---
name: knowledge-management
description: Designs the knowledge article lifecycle in Dynamics 365 Customer Service, covering templates, authoring ownership, review and approval, publishing, expiry, translation and feedback. Use when setting up knowledge for agents, portals or Copilot, migrating existing articles, or fixing stale and duplicated content.
license: CC-BY-4.0
metadata:
  department: customer-service
  stages: Initiate, Implement, Prepare, Operate
  modules: Customer Service
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Knowledge management

Knowledge is the asset that new agents, customer self-service and Copilot all depend on. A good knowledge base shortens handling time and makes answers consistent; a poor one spreads wrong answers faster, especially once generative features start quoting it.

Projects usually go wrong by treating knowledge as a migration task: everything in the old wiki or SharePoint library is moved across unchanged, nobody owns it, and articles written as policy documents sit next to duplicates and outdated fixes. The technology is rarely the problem. Ownership, review discipline and writing for answers are.

## When to use

- Setting up the knowledge article lifecycle, templates and approval workflow.
- Assigning authoring and review ownership by subject.
- Deciding what to migrate, rewrite or retire from existing knowledge sources.
- Planning translations, internal versus external visibility and portal use.
- Fixing a knowledge base that agents or customers no longer trust.

Not this skill: `customer-service:service-agents-and-copilot` for which AI features use the knowledge, `customer-service:case-lifecycle-design` for the case process itself, `change-adoption:role-based-training` for training agents.

## Questions to ask first

1. Who will own, write and review articles day to day? Without named owners by subject, content decays as soon as the project team leaves.
2. Who reads the articles: agents, customers through a portal, AI features, or all three? Audience decides tone, visibility and how strict approval must be.
3. Where does knowledge live today and how much of it is current? This decides how much is migrated, rewritten or left in place.
4. Which languages and regions need content? Translation adds versions, reviewers and effort.
5. Do any articles carry regulatory, contractual or safety statements? Those need a formal approval step and a named approver.

## Approach

Dynamics 365 knowledge articles have a long-established lifecycle with drafting, review and approval, scheduled or immediate publishing, expiry and archiving, plus versions and translations. The project's job is to put people and rules around that lifecycle, then connect it to daily case work.

1. Set ownership by subject. Assign each knowledge category to an owning team, with roles for subject owner, author and reviewer, and a knowledge manager who holds standards and the backlog. Authors should be the people who resolve the cases. Record the roles in the `raci-matrix`.

2. Design for answers. Create a few article templates, such as how-to, troubleshooting, known issue and policy summary, each with a consistent structure: the question or symptom, who it applies to, the steps, and what to do if they fail. Short single-purpose articles serve agents, portal search and Copilot far better than long manuals.

3. Define the workflow. Decide which articles need formal approval (customer-facing, regulated or policy content) and which trusted authors may publish directly. Give every article a review date and route expiring articles back to their owners.

4. Curate before migrating. Inventory existing content and decide for each item whether to keep, rewrite, merge or retire it, then migrate only what survives. Map category, product, language, audience and keywords in the `data-migration-mapping`. If a large body of content must stay in another repository, check current Microsoft Learn documentation on external search options rather than duplicating it.

5. Close the loop with cases. Link articles to the cases they helped resolve, capture feedback, and make it easy to draft a new article from a resolved case. Agents should be able to flag a gap without leaving the case.

6. Prepare for Copilot and self-service. Ambiguous, contradictory or internal-only content will surface in generated answers. Set internal and external visibility deliberately, remove duplicates, and agree permitted sources with `customer-service:service-agents-and-copilot`.

7. Measure health. Track articles past their review date, searches with no useful result, article use on resolved cases and feedback trends, and review them monthly with subject owners.

## Outputs

- Knowledge governance model with roles recorded in the `raci-matrix`.
- Article templates and a short writing guide.
- Lifecycle, approval and review rules in the `solution-blueprint`.
- Content inventory with keep, rewrite, merge or retire decisions, and the migration map in the `data-migration-mapping`.
- Author and reviewer training in the `training-and-communications-plan`.
- Knowledge health measures and a review cadence.

## Scale notes

### SMB

The service manager often doubles as knowledge manager, with a few experienced agents as authors. Allow trusted authors to publish internal articles without formal approval. Do not skip the content cull before migration or review dates on every article.

### Enterprise

Expect a knowledge council or owner per product line, formal approval for customer-facing and regulated content, translation workflows and portal publishing. Agree standards for templates and metadata across business units, and report knowledge health by category so owning teams can see where reviews are overdue.

## Hand-offs

- `customer-service:service-agents-and-copilot` once content is ready to ground AI features.
- `integration-and-data:data-mapping-and-cleansing` for the content migration.
- `change-adoption:role-based-training` for author and reviewer training.
- Reviewer sign-off: `security-compliance:security-model-review` for internal versus external visibility, with `data-and-ai:responsible-ai-review` where content grounds generated answers.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Bulk-migrate legacy knowledge without reviewing and retiring stale content.
- Publish articles with no owner and no review date.
- Expose internal-only articles to portals or AI grounding without checking visibility.
- Put customer personal data in knowledge articles.
