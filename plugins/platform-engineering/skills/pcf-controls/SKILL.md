---
name: pcf-controls
description: Guides when and how to build Power Apps component framework code components for Dynamics 365 CE forms and views, covering justification, design, accessibility, mobile and offline use, packaging and versioning. Use when an interface need goes beyond standard controls, or when reviewing or adopting a community or vendor control.
license: CC-BY-4.0
metadata:
  department: platform-engineering
  stages: Implement, Operate
  modules: All
  status: draft
  authors: Simon Foote, Robert Peledie
---

# PCF controls

Code components built with the Power Apps component framework let a model-driven app present data in ways standard controls cannot: a visual timeline, a signature pad on a technician's device, an inline map or a richer editable grid. They render inside the app's own lifecycle, so a well-built control feels native and a poorly built one slows every form it sits on.

Projects get into trouble when controls are built for cosmetic preference, when business validation lives in a control and nowhere else, or when community controls are imported without anyone reading the code. Another frequent problem is releasing a change without incrementing the control's version, so users keep running the old one.

## When to use

- An interface requirement cannot be met by standard controls, configuration or a custom page.
- A control is needed on Field Service Mobile or must work offline.
- A community, AppSource or partner-built control is proposed.
- An existing control is slow, inaccessible or behaves differently across devices.

Not this skill: `solution-architecture:extend-or-configure` to decide whether a control is justified, `field-service:mobile-and-offline` for the offline profile and mobile app set-up, and `platform-engineering:plugin-design` for server-side rules a control must never replace.

## Questions to ask first

1. What exactly can standard controls not do, and what does the user lose if one is used? This keeps controls to genuine needs.
2. Where will the control run (main forms, views, custom pages, mobile, offline)? Each context changes which APIs and data are available.
3. Is it bound to a column or a dataset, or does it fetch its own data? This decides the control type and its performance profile.
4. Which accessibility standard must the organisation meet? It sets the testing bar before release.
5. Who in the run team can maintain TypeScript and the build toolchain? Without that skill the control becomes an orphan.

## Approach

Treat a code component as a small product with its own source, tests, version history and owner.

1. Justify it and look for existing options. Check standard controls, Microsoft-provided components and reputable published controls first. If adopting a third-party control, review the source and maintenance history, be ready to own a fork, and refer its licence terms to the organisation's DPO or legal adviser where they are unclear.
2. Choose the type. Field components bind to a column and suit input or display of a single value. Dataset components bind to a view or subgrid and suit alternative list or grid presentations. Keep components that fetch extra data through the Web API to a minimum, because each adds calls to every form load.
3. Keep logic in the right place. The control presents and captures data. Rules that must always hold belong in Dataverse (business rules, plug-ins, column validation), because data also arrives through imports, flows and integrations that never render the control.
4. Build for performance. Keep bundles small, use the platform-provided React and Fluent UI libraries where supported (check current Microsoft Learn documentation), avoid heavy work on every update cycle and debounce user input before writing values back.
5. Build for everyone. Support keyboard navigation, screen readers, high contrast and the app theme. Test on the devices and form factors users actually have, including Field Service Mobile and offline mode where relevant.
6. Package properly. Initialise the project with the Power Platform CLI, keep source in the repository, build in the pipeline and ship controls in a component solution under the organisation's publisher. Increment the manifest version on every release so clients pick up the change.
7. Test. Unit test the logic, use the test harness during development and check the control in a real app, on real devices, before release.

## Outputs

- A control specification covering purpose, binding, contexts, accessibility and performance expectations.
- Source repository and build steps for the control, recorded in the `environment-and-alm-strategy`.
- A component solution under the organisation's publisher.
- Review notes for any third-party control adopted.

## Scale notes

### SMB

Prefer existing controls or configuration, because a bespoke control is a significant support commitment for a small team. If one is essential, make sure the customer owns the source and a partner support arrangement covers it. Accessibility testing must not be dropped to save time.

### Enterprise

Maintain a catalogue of approved controls with named owners, a shared component library aligned to the organisation's design system, automated accessibility checks in the build and design authority approval for each new control.

## Hand-offs

`platform-engineering:solution-layering` places the control in a solution, `platform-engineering:deployment-pipelines` builds and releases it, and `testing-quality:regression-automation` keeps it covered. Reviewer sign-off: `design-authority:customisation-challenge` before build and `design-authority:standards-conformance` before release.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Import community or vendor controls into production without reviewing source, licence terms and maintainer.
- Enforce a business rule only inside a PCF control.
- Release a control that has not been tested with keyboard and screen reader.
- Ship a changed control without incrementing its manifest version.
- Build a code component where a standard control or configuration meets the need.
