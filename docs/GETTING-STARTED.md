# Getting started

D365 CE Roster is a library of CRM delivery expertise packaged as 17 independently installable departments. Install the
ones your project needs, and the relevant specialist loads when you ask something in its territory. It runs in Claude
Code and in ChatGPT and Codex from the same files.

Nothing here changes your Dynamics 365 environment. Installing a department adds skills to your AI assistant; it does not
connect to Dataverse, write to your tenant or run anything on its own.

## Install

### Claude Code

Add the marketplace once, then install departments one at a time:

```
/plugin marketplace add SimonFoote-greensparx/dynamics-365-ce-roster
/plugin install customer-service@dynamics-365-ce-roster
/plugin install solution-architecture@dynamics-365-ce-roster
```

`/plugin` on its own opens the plugin menu to review and manage what is installed.

### ChatGPT and Codex

Add the repository as a plugin marketplace (the manifest is `.agents/plugins/marketplace.json`), or copy the department
folders you want into `.agents/skills/` in your own project. Skill descriptions share a limited context budget there, so
installing a handful of departments works better than installing all of them.

## Which departments to install first

Start from the project you are running, not from the org chart.

| If your project is... | Start with |
|---|---|
| A small Sales and Customer Service rollout | `sales`, `customer-service`, `programme-management`, `solution-architecture`, `security-compliance` |
| A contact-centre or service transformation | `customer-service`, `integration-and-data`, `testing-quality`, `design-authority`, `security-compliance` |
| A Field Service rollout with ERP | `field-service`, `integration-and-data`, `solution-architecture`, `support-operations`, `design-authority` |
| A marketing launch on Customer Insights - Journeys | `marketing`, `security-compliance`, `data-and-ai`, `change-adoption` |
| A multi-module enterprise programme | All four module departments, `programme-management`, `solution-architecture`, `platform-engineering`, `platform-administration`, both reviewer departments |
| Planning a project and staffing it | `project-tailoring`, `programme-management` |

Install the two reviewer departments, `design-authority` and `security-compliance`, early regardless. They are the ones
that tell you something you did not want to hear, which is the reason to have them.

## Three ways to use it

1. **Just ask.** Skills load themselves when a request matches: "We keep getting duplicate cases from email replies; how
   should email-to-case be set up?"
2. **Name the skill** for a specific lens: `/customer-service:email-to-case` in Claude Code, or "use the email-to-case
   skill" elsewhere.
3. **Delegate a department.** Each department has an agent charter in `.claude/agents/`, so it can be handed a body of
   work as a subagent with its own write surface.

## Get a tailored project pack

1. Copy a sample from `profiles/samples/` into `input/` (or build one with the profile builder on the website).
2. Describe your organisation: modules and users, goals, current estate, and your team with their declared skills and
   availability. Use aliases instead of names if you prefer.
3. Install `project-tailoring` and ask: "Build our project pack from input/our-profile.yaml."
4. The agent recommends an edition, proposes who holds each role, flags gaps and unsafe combinations, and writes the
   Word and Excel templates to `output/`.

`input/` and `output/` are git-ignored, so your organisation's data never reaches the repository. The role mapping is a
proposal for the project lead to confirm; it never ranks people or assesses performance.

## What to expect back

A skill is not a form that fills itself in. Most will start by asking the two or three things that decide the answer:
which modules, how many users, whether there is an ERP, whether technicians work offline. Expect to be told what the
library cannot determine, and where a question belongs with Microsoft's documentation, a licensing specialist, your DPO
or a legal adviser.

## Reviewer-class departments behave differently

`design-authority` and `security-compliance` review what other departments propose. Their blocking findings are not
overruled by the department under review. In practice: when a design customises something standard Dynamics 365 already
does, or a marketing journey has no lawful basis for a segment, that is not a trade-off against the go-live date. The
date moves or the design changes.

## Getting help

Questions and ideas belong in GitHub Discussions; defects and gaps in Issues. A situation the library handles badly is
the most useful thing you can report.
