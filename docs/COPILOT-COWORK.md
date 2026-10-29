# Using D365Forge with Microsoft Copilot Cowork

Copilot Cowork supports the open Agent Skills format, which is the format every D365Forge skill is written in. You
can add whole departments to Cowork as plugins, add a single skill on its own, set custom instructions so Cowork works
the way your project does, and build a tailored project pack whose Word and Excel documents land in your own OneDrive.

This guide covers what you do in Cowork. It is based on Microsoft's published guidance for customising Cowork and building
Cowork plugins (links at the end). Cowork changes regularly, so if a menu has moved, follow Microsoft's current guidance.

## Before you start

- **Access.** You need Copilot Cowork in your Microsoft 365 tenant, and your organisation must allow you to add your own
  plugins and skills. If **Upload plugin** or **Upload skill** is missing, ask your Microsoft 365 administrator.
- **Desktop or web.** Custom plugins are not supported in Cowork on mobile.
- **Information barriers.** Microsoft notes that tenants using Microsoft Purview Information Barriers cannot currently
  upload or share custom plugins and skills.
- **Trust.** A skill runs as instructions to the AI. Read what you upload; every skill in this repository is plain text.
- **Where to download.** The plugin archives and skills are on the project website (the **Downloads** page and each
  skill's page) and in the public GitHub repository, where anyone can download them without an account.
- **Status.** Every skill is marked `reviewed`. Check the `status` line at the top of
  each skill.

## Option 1: Add departments as plugins (recommended)

Each department is packaged as a ready-to-upload plugin archive in [`cowork/plugins/`](../cowork/plugins/). Each archive
holds the department's skills and their reference files, for example the sources list, or the role catalogue and
templates for `project-tailoring`.

1. Choose the departments for your project (see the table below).
2. Download its archive: from the **Downloads** page on the project website, or on GitHub by opening
   `cowork/plugins/<department>.zip` and selecting **Download raw file**.
3. Open Copilot Cowork, select **Customize** in the left navigation, then the **Plugins** tab.
4. Select **Upload plugin** and choose the archive. Cowork recognises it as a Claude-format plugin and converts it into
   a Cowork plugin, including its skills.
5. In the **Share** dialog, choose **Only you** to try it yourself, or **Specific users in your organisation** to share
   it with your project team.
6. The department appears under **Installed** on the **Plugins** tab with the `d365forge-` prefix (for example
   `sales.zip` installs as `d365forge-sales`), and its skills appear under **Your skills** under their own names.
7. Start a new conversation to use it.

Install only what your project needs. Cowork reads the name and description of every installed skill when it decides which
one to use, so a focused set gives sharper results.

| If your project is... | Upload |
|---|---|
| A small Sales and Customer Service rollout | `sales`, `customer-service`, `programme-management`, `solution-architecture`, `security-compliance` |
| A contact-centre or service transformation | `customer-service`, `integration-and-data`, `testing-quality`, `design-authority`, `security-compliance` |
| A Field Service rollout with ERP | `field-service`, `integration-and-data`, `solution-architecture`, `support-operations`, `design-authority` |
| A marketing launch on Customer Insights - Journeys | `marketing`, `security-compliance`, `data-and-ai`, `change-adoption` |
| Planning and staffing a project | `project-tailoring`, `programme-management` |

In a conversation, use the **Sources** picker to turn plugins on or off, so only the departments relevant to the
request are in play.

## Option 2: Add a single skill

To try one skill before installing its department:

1. Download the skill's `SKILL.md`: on the project website, open the skill's page and select **Download SKILL.md**; on
   GitHub, open the file, for example `plugins/customer-service/skills/queues-and-routing/SKILL.md`, and download it.
2. In Cowork, select **Customize** > **Skills**, select the arrow next to **Add**, then **Upload skill**, and choose the file.
3. Cowork validates it and saves it to your OneDrive. It appears under **Your skills** once it has synced.

A single `SKILL.md` does not include the skill's `references/` folder. That is fine for most skills, but use Option 1 for
`project-tailoring`, whose skills depend on their bundled role catalogue, rules and templates. If you upload a skill whose
name you already have, Cowork keeps both and adds a number to the new one, so remove the old version first.

## Set your custom instructions

Custom instructions tell Cowork how you work in every task. Copy the suggested text from
[`cowork/custom-instructions.md`](../cowork/custom-instructions.md) into **Customize** > **Preferences**, then fill in your
project's modules, scale and go-live date. In the instructions editor you can type `/` to reference a specific skill.

## Ask questions

Ask in plain language, as you would ask a colleague. The right skill loads when the request matches its description:

| You ask | What loads |
|---|---|
| "We keep getting duplicate cases from email replies. How should email-to-case be set up?" | `customer-service:email-to-case` |
| "Should this be a plug-in, a flow or configuration?" | `solution-architecture:extend-or-configure` |
| "Engineers lose notes when they are offline. What should the offline profile include?" | `field-service:mobile-and-offline` |
| "Can we email these trade contacts without consent?" | `security-compliance:marketing-consent-compliance` |

To use a specific lens, name the skill: "Use the scheduling optimisation skill to review this plan." Most skills will ask
two or three questions before they advise; answering them is what makes the advice fit your project.

## Build a tailored project pack

Cowork can create Word and Excel files in your OneDrive, which makes it a good place to run the tailoring department.

1. Upload the `project-tailoring` and `programme-management` plugins.
2. Create your organisation profile: use the profile builder on the project website, or start from a fictional sample in
   [`profiles/samples/`](../profiles/samples/). Use aliases ("Analyst A") instead of names if you prefer.
3. Save the profile in your own OneDrive, for example in a private project folder. Do not put it anywhere shared or public.
4. In a new conversation, attach the profile and ask: "Build our project pack from this profile."
5. Cowork validates the profile and asks for anything missing, recommends the SMB or Enterprise edition, and proposes who
   holds each project role, with a reason for each. Confirm or correct the role mapping before it continues.
6. It then writes the twelve documents (charter, RACI, skills-gap plan, delivery plan, RAID log, blueprint outline and the
   rest) as Word and Excel files in your Cowork output folder in OneDrive.
7. When the profile changes, ask: "Refresh our project pack." The refresh writes to a new dated folder and keeps your
   edited versions.

Role mapping uses only the skills and availability people declare. It never ranks people or comments on performance, and
its output is a proposal for the project lead to confirm.

## Roll out to your project team or organisation

- **To specific people.** Open the plugin's detail page, select **Share**, and add people by name or email. After you
  upload a newer version, select **Re-share** so everyone gets it.
- **To everyone, through your administrator.** Organisation-wide listing in Cowork's **Discover** section uses a
  Microsoft 365 app package. An administrator can convert a department with the Microsoft 365 Agents Toolkit, following
  Microsoft's "Build plugins for Copilot Cowork" guidance:

  ```
  atk import openplugin --path ./customer-service --output ./customer-service-cowork \
    --privacy-url https://d365forge.ai/privacy.html \
    --terms-url https://github.com/SimonFoote-greensparx/D365Forge/blob/main/NOTICE.md
  ```

  Here `./customer-service` is the unzipped plugin archive (or `plugins/customer-service` in a clone). Package the result
  with `atk package`, then upload it in the Microsoft 365 admin center under **Manage apps** > **Upload custom app**. The
  conversion generates placeholder icons; replace the colour icon with the 192 x 192 D365Forge icon,
  [`docs/assets/brand/d365forge-icon-192.png`](assets/brand/d365forge-icon-192.png), before packaging. The maintainers have not yet tested organisation-wide deployment, so try it in a
  test tenant first.

The plugins are free to share inside or outside your organisation. They are licensed under CC BY 4.0, so when you share
or adapt them, keep the credit to the authors, Simon Foote and Robert Peledie: it is in each department README, in each
skill's `license` and `authors` fields, and in [NOTICE.md](../NOTICE.md). Project documents you produce with them need
no credit.

## Keep up to date

The plugin archives are regenerated every time the skills change. To update a department:

1. Download the new archive from the website's **Downloads** page or `cowork/plugins/`.
2. Remove the old version from **Customize** > **Plugins**, then upload the new one.
3. **Re-share** it if you shared it with others, and start a new conversation.

**Plugins installed before 29 October 2026** have no prefix (for example `sales` rather than `d365forge-sales`). Cowork
treats the prefixed plugin as a different plugin, so remove the old, unprefixed one before uploading the new archive;
otherwise every skill in that department is installed twice.

Watch the repository, or check the [roadmap](ROADMAP.md), to see when departments move from `reviewed` to `stable`.

## What works differently from Claude Code

| Feature | Claude Code | Copilot Cowork |
|---|---|---|
| Skills load when a request matches | Yes | Yes |
| Reference files inside a skill (`references/`) | Yes | Yes, through plugin upload |
| Install from the marketplace (`/plugin install`) | Yes | No. Upload the archive from the **Downloads** page or `cowork/plugins/` instead |
| Delegate a whole department as a subagent (`.claude/agents/`) | Yes | Not supported in Cowork plugins yet |
| Run the repository's build and check scripts | Yes, in a clone | Not needed; they are for maintainers |
| Create Word and Excel files in OneDrive | Through other tools | Built in |

## Troubleshooting

| Problem | What to try |
|---|---|
| The skill you expected did not load | Start a new conversation, check the department is turned on in **Sources**, then name the skill in your request. If it still fails, open an issue with the prompt you used. |
| **Upload plugin** or **Upload skill** is missing | Your organisation may not allow custom plugins or skills. Ask your Microsoft 365 administrator. |
| The upload is rejected | Check you uploaded the `.zip` exactly as downloaded, without unzipping and re-zipping it. If it still fails, open an issue with the error message. |
| The upload fails with "File extension '.toml' is not supported" | You have a `project-tailoring` archive from before 16 October 2026, which bundled its role data as `.toml` files that Microsoft 365 Copilot does not accept. Download the archive again; the current one bundles that data as `.json`. |
| A new skill does not appear | Uploaded skills sync through OneDrive and can take a few moments. Refresh **Your skills**. |
| The project pack has gaps marked in the documents | That is deliberate: the tailoring skills mark what the profile did not tell them rather than invent it. Add the detail to the profile and refresh the pack. |

## Sources

- Microsoft Learn, "Customize Copilot Cowork": https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-customize
- Microsoft Learn, "Build plugins for Copilot Cowork": https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-plugin-development
