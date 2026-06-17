---
apply: always
---

# Context Management Rules

This file defines how project context must be created, updated, and maintained.

It must be followed before SDK implementation, packaging, documentation, release
workflow, or public API changes.

## Single Source Of Truth

There must be only one active context file:

```text
.aiassistant/project_context/CURRENT_CONTEXT.md
```

This file is the only valid runtime context.

Files in `project_context/history/` are historical snapshots only.

## Forbidden Behaviors

Do not:

- create multiple active context files;
- use historical snapshots as current context;
- append raw notes without refactoring;
- invent SDK package names, integrations, public APIs, release policies, or
  supported Python versions;
- treat templates as active context;
- preserve multiple competing context files;
- create `CURRENT_CONTEXT_v2.md`, `new-context.md`, or similar alternatives;
- copy PipeBridge reference context as if it were the new SDK context.

## Creating Context

When `CURRENT_CONTEXT.md` does not exist:

1. follow [[bootstrap-python-sdk-context]];
2. gather explicit SDK information from the user;
3. use [[SDK_CONTEXT_TEMPLATE]];
4. create the file only after enough real information exists.

Required minimum information:

- SDK purpose;
- package name;
- public entrypoint direction;
- target users;
- integration or wrapped system;
- supported Python versions;
- packaging/release intent;
- known compatibility constraints.

Do not ask every possible question at once if the project is still being
defined. Gather enough information to create a trustworthy first context and
record remaining unknowns as open questions.

## Updating Context

When new information changes the SDK reality:

- refactor the existing context;
- keep it concise;
- update the correct section;
- avoid log-style appendices.

Update context when:

- package identity changes;
- public API direction changes;
- integrations are added;
- release strategy changes;
- major architecture boundaries change;
- documentation or process knowledge becomes operationally important;
- supported Python version changes;
- CI/CD or publication target changes;
- integration-test boundaries change;
- public exception taxonomy changes.

## Context Vs Decisions

Use context for current behavior and project state.

Use decisions for binding constraints and accepted trade-offs.

Context must not override accepted decisions.

If a better approach conflicts with an accepted decision:

1. explain why the decision may be suboptimal;
2. explain risks of keeping it;
3. explain benefits of changing it;
4. ask for approval before changing behavior.

## Context Vs Specs

Use specs for planned implementation design.

Once a change is implemented and becomes current reality, update
`CURRENT_CONTEXT.md` if it materially affects:

- public API;
- architecture;
- release workflow;
- integrations;
- docs/publishing behavior.

Do not leave implemented reality only inside a spec.

## Context Cleanliness

The active context must remain:

- concise;
- coherent;
- non-redundant;
- aligned with the real SDK.

Do not append raw notes at the end. Refactor the relevant section.

## SDK-Specific Context Fields

A healthy SDK context should make these areas inspectable:

- package identity;
- public API surface;
- package architecture;
- external integrations;
- testing strategy;
- documentation strategy;
- release and versioning strategy;
- known compatibility risks;
- next priorities.

## Related Files

- [[CURRENT_CONTEXT]]
- [[SDK_CONTEXT_TEMPLATE]]
- [[bootstrap-python-sdk-context]]
- [[REPOSITORY_GUIDELINES]]

