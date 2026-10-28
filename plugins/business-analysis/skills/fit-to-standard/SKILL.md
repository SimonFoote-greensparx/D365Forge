---
name: fit-to-standard
description: Plans and runs fit-to-standard workshops that demonstrate standard Dynamics 365 CE behaviour first, using realistic scenarios from the business, and record only differences backed by a business reason. Use when preparing Initiate workshops, when a partner proposes open requirement-gathering, or when stakeholders ask to rebuild the old system.
license: CC-BY-4.0
metadata:
  department: business-analysis
  stages: Strategize, Initiate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Fit-to-standard workshops

Traditional requirements gathering asks people what they want, and they describe the system they already have. Fit-to-standard reverses the order. The team shows how standard Dynamics 365 handles the process, using the organisation's own scenarios, and then asks what would stop the business working that way. What remains is a much shorter list of genuine differences, each with a reason.

The method fails when demonstrations run in an empty trial with no recognisable data, when the facilitator cannot configure the system live, when gaps are recorded because a user prefers the old screen, or when nobody in the room has authority to accept the standard process. It also fails when the workshop drifts into designing custom solutions on the whiteboard.

## When to use

- At Initiate, after the process catalogue exists and before the backlog is written.
- When a partner proposes requirement-gathering sessions that start from a blank page.
- When stakeholders ask for the legacy CRM or spreadsheets to be replicated.
- When a new module or business unit joins an existing Dynamics 365 estate.

Not this skill: `business-analysis:fit-gap-analysis` for classifying and resolving the gaps the workshops produce, `business-analysis:process-mapping` for drawing the processes, `design-authority:customisation-challenge` for formally challenging a proposed customisation.

## Questions to ask first

1. Which processes and modules are in scope, and in what order should they be covered? This sets the workshop schedule and the demo build.
2. Who can make process decisions in the room? Without process owners present, every difference is recorded as a gap.
3. Is there a sandbox with representative configuration and sample data? Users judge the product by what looks familiar.
4. Which current behaviours are required by regulation or contract, and which are habit? Only the first kind justifies a gap by itself.
5. Which apps does the organisation expect to license? Demos must not rely on capabilities that will not be bought; confirm with the Microsoft licensing guide or your partner.

## Approach

1. Prepare a sandbox with light configuration in the organisation's language: a few business units, sample accounts and contacts, a handful of products, realistic cases or work orders, and the standard model-driven apps for the modules in scope. Avoid heavy pre-configuration, which turns the demo into a design proposal.
2. Schedule by process, not by module screen. Typical workshops cover lead to opportunity, quote to order, case intake to resolution, work order scheduling to completion, and campaign to qualified lead.
3. Run each workshop to a fixed shape. Restate the outcomes the process must deliver, walk the standard process end to end in the system using the organisation's scenario, and pause at each step to ask whether the business could work this way.
4. Record each step as fit, fit with configuration, or gap, with the business reason in the owner's words. A gap needs a reason tied to an outcome, a regulation, a customer commitment or a measurable cost. "That is how we do it today" is not a reason; ask what would happen if the business adopted the standard step.
5. Park solution design. When someone starts designing a fix, log the need and move on; resolution belongs to fit-gap analysis and the design authority.
6. Play back decisions within a few days and have the process owner confirm them in writing.
7. Feed the results into the future-state maps, the fit-gap register and candidate stories.
8. Before closing a gap as permanent, check the published release plans for upcoming capabilities (check current Microsoft Learn documentation), and revisit open gaps when each release wave lands.

Staff each workshop with a functional consultant who can configure live, an analyst who captures decisions, the process owner who decides, and key users who do the work. Bring an architect when the process crosses modules or systems.

## Outputs

- A workshop schedule, scenarios and demo scripts per process.
- A decision log per workshop, confirmed by the process owner.
- A candidate fit-gap list with business reasons.
- Updated future-state process maps and playback summaries.

## Scale notes

### SMB

The consultant runs and captures each workshop, often one per process, with the owner deciding in the room. Standard apps usually fit well at this scale, so resist customising on the first day and let users live with standard behaviour through the first sprints before deciding.

### Enterprise

Run a global template series first, then shorter local variance workshops per business unit or country that may only challenge the template with a documented reason. Keep a single decision log format across workstreams, and have the design authority attend workshops where processes cross modules.

## Hand-offs

- `business-analysis:fit-gap-analysis` classifies and resolves the gaps.
- `business-analysis:process-mapping` updates the future-state maps.
- `business-analysis:user-stories` turns confirmed fits and configurations into backlog items.
- `solution-architecture:solution-blueprint` takes cross-module decisions into the design.
- Reviewer sign-off: any gap proposing customisation goes to `design-authority:customisation-challenge`.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Ask users for requirements before showing them standard Dynamics 365.
- Record a gap whose only reason is that the current system works that way.
- Design custom solutions inside the workshop.
- Demonstrate preview features as though they were committed scope.
