---
name: plugin-design
description: Guides the design of Dataverse plug-ins, choosing synchronous or asynchronous execution and the right pipeline stage, and avoiding recursion, long-running work and fragile code. Use when a requirement needs server-side code, when registering or reviewing plug-in steps, or when plug-ins cause errors, loops or slow saves.
license: CC-BY-4.0
metadata:
  department: platform-engineering
  stages: Implement, Operate
  modules: All
  status: reviewed
  authors: Simon Foote, Robert Peledie
---

# Plug-in design

Plug-ins are the most powerful extension point in Dataverse and the easiest way to make a Dynamics 365 CE system slow and brittle. A plug-in runs inside the platform's event pipeline, often inside the database transaction, so a poorly placed step affects every user, integration and flow that touches the table.

The common mistakes are predictable: post-operation steps that update the record that triggered them and start a loop, update steps registered without filtering attributes so they fire on every save, external calls made inside synchronous steps, and plug-in classes that hold state between executions and fail only under load.

## When to use

- `solution-architecture:extend-or-configure` has concluded that server-side code is the right rung.
- Registering, reviewing or refactoring plug-in steps and custom APIs.
- Diagnosing plug-in errors, infinite loops, deadlocks or slow saves.

Not this skill: `solution-architecture:extend-or-configure` to decide whether code is needed at all, `platform-engineering:power-automate-patterns` for asynchronous low-code alternatives, and `solution-architecture:performance-by-design` for the wider performance budget.

## Questions to ask first

1. Must the logic block or change the save, or can it happen afterwards? This decides synchronous versus asynchronous and the stage.
2. Which message, table and columns should trigger it? Precise registration is the first performance control.
3. Will integrations, imports or bulk operations trigger it? Code that is fine for one user's save may not survive a nightly batch.
4. Does it need data or services outside Dataverse? External calls change the timeout and failure design.
5. Who maintains the code after go-live? Code with no owner in the run team becomes an upgrade risk.

## Approach

Choose the stage by what the logic needs to do, then keep each step small and single-purpose.

1. Pick the stage. Use pre-validation for cheap checks that should fail fast before the main work begins. Use pre-operation to set or correct values on the target, which avoids a second update call entirely. Use synchronous post-operation only when related records must change in the same transaction and the user must see the result. Use asynchronous post-operation for everything else: notifications, downstream updates and calls to other systems.
2. Register precisely. Every update step gets filtering attributes. Pre and post images include only the columns the code reads. Steps are registered in a solution, never by hand in each environment.
3. Design out recursion. The usual loop is a post-operation step updating its own record. Move the change to pre-operation, or update only when values actually differ. Treat the execution depth check as a safety net, not as the design.
4. Keep synchronous work short. Synchronous plug-ins run under a platform time limit and inside a transaction that holds locks. Avoid loops over large result sets and external calls, and push long or retry-prone work to asynchronous steps, to Azure through a service endpoint or webhook, or to a queue.
5. Write stateless code. Plug-in instances are cached and reused, so class fields must not hold per-execution data. Pass context through the execution context and shared variables.
6. Fail clearly. Throw an InvalidPluginExecutionException with a message a user can act on, write diagnostic detail to the tracing service, and send telemetry to Application Insights where it is configured (check current Microsoft Learn documentation for the integration).
7. Prefer custom APIs for callable logic. When client script, flows or integrations need to invoke server logic, expose it as a custom API rather than a dummy trigger column.
8. Configure, do not hard-code. Read URLs, thresholds and identifiers from environment variables, and keep secrets in Azure Key Vault or secure configuration.

Test with unit tests against a mocked execution context and with integration tests in a development environment, including bulk and concurrent scenarios.

## Outputs

- A design note per plug-in: message, table, stage, mode, filtering attributes, images and failure behaviour.
- Step registrations held in source control and in the solution, with conventions recorded in the `environment-and-alm-strategy`.
- Unit and integration tests that run in the build pipeline.
- Tracing and telemetry conventions handed to the support team.

## Scale notes

### SMB

Often one partner developer writes every plug-in. Insist on source in the customer's repository, a short design note per plug-in and filtering attributes on every update step. If the partner cannot support code long term, that is a reason to revisit the rung, not to skip documentation.

### Enterprise

Use a shared plug-in base library, code review for every change, static analysis and solution checker in the build, and a register of every step across all solutions. The design authority approves any new synchronous step on a high-volume table.

## Hand-offs

`platform-engineering:solution-layering` decides which solution holds the assembly, `platform-engineering:deployment-pipelines` builds and deploys it, and `testing-quality:regression-automation` covers it in regression. Reviewer sign-off: `design-authority:standards-conformance` for code standards, and `design-authority:customisation-challenge` for new synchronous steps on core tables.

## Sources

`references/sources.md` in this skill lists the outside authorities for the questions here, what each is authoritative for, and what you may do with it. Check the current Microsoft Learn documentation before stating how a feature behaves, because Dynamics 365 changes monthly, and cite what you used.

## Never

- Call an external service from a synchronous plug-in without a timeout and a failure path.
- Store per-execution state in plug-in class fields.
- Register an update step without filtering attributes.
- Rely on the execution depth check as the main defence against recursion.
- Hard-code record identifiers, URLs or credentials in plug-in code.
