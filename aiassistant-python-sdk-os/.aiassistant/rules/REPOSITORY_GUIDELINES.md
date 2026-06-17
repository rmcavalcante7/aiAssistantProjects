---
apply: always
---

# Repository Guidelines

This file defines how the SDK operating system repository must evolve.

## Purpose

The repository supports context-aware Python SDK development with explicit
governance, repeatable release flows, and validation gates.

It is a structured operating system, not a loose documentation folder.

Each artifact has one responsibility. Do not mix context, decisions, execution,
validation, and templates in the same file.

## Component Responsibilities

### `project_context/`

Stores the active runtime understanding.

- `CURRENT_CONTEXT.md`: current system state.
- `history/`: historical snapshots only.

### `decisions/`

Stores accepted constraints and trade-offs.

Use it for:

- public API compatibility policy;
- package and versioning strategy;
- release workflow;
- documentation policy;
- external integration boundaries;
- dependency/versioning policy;
- compatibility promises;
- security and credential handling;
- long-lived testing boundaries.

### `runbooks/`

Stores executable procedures.

Use it for:

- bootstrapping SDK context;
- setting up package structure;
- generating README and pyproject;
- configuring docs;
- preparing releases;
- validating docs;
- validating package metadata;
- publishing safely.

### `checklists/`

Stores validation criteria.

Use it for:

- implementation readiness;
- public API compatibility;
- documentation completeness;
- release readiness;
- PyPI README rendering;
- integration-test safety.

### `feedback/`

Stores real-world product input.

Feedback may generate specs, roadmap items, or decisions.

Feedback must describe the problem and impact. It is not a place for raw task
notes or implementation logs.

### `roadmap/`

Stores release-oriented planning.

Roadmaps define what will be built, in what order, and under which constraints.
They do not replace specs or decisions.

### `specs/`

Stores design before implementation.

Create a spec before public API changes, architecture changes, or complex SDK
behavior changes.

Specs must record compatibility, tests, and documentation impact.

### `prompts/`

Stores reusable operational prompts.

Prompts standardize agent behavior for recurring tasks. They must not become
the only place where a rule exists.

### `rules/`

Stores mandatory governance and agent behavior.

### `templates/`

Stores scaffolding for SDK projects.

Templates are not source of truth and must be adapted.

Generated files must remove placeholders before they are considered complete.

### `tools/`

Stores executable helper scripts.

Tools support governance but do not replace context, decisions, runbooks, or
checklists.

### `project_knowledge/`

Optional root for process and business-rule documentation when an SDK wraps
process-heavy systems.

Do not use it as an alternative `.aiassistant`.

## When To Update Each Component

Update `CURRENT_CONTEXT.md` when current SDK reality changes.

Create a decision when a constraint must be preserved.

Create a runbook when a process must be repeated.

Create a checklist when validation must be explicit.

Create feedback when a real issue or product gap appears.

Create a roadmap when release scope must be organized.

Create a spec before non-trivial implementation.

Update prompts when repeated agent behavior must be standardized.

Use templates only as starting points.

Update `project_knowledge/` when SDK behavior changes business or operational
process behavior.

## SDK Artifact Governance

For real SDK repositories, these files are operationally important:

- `pyproject.toml`;
- `README.md`;
- `CHANGELOG.md`;
- `src/<package>/__init__.py`;
- public facade/client modules;
- public models and exceptions;
- `tests/`;
- `docs/`;
- `.github/workflows/`.

Changes to these files should be reviewed for public API, packaging,
documentation, and release impact.

## pyproject Rules

- Runtime dependencies must be direct dependencies.
- Development tools must live in optional extras.
- Documentation tools must live in optional extras.
- Python version support must match active context.
- Versioning strategy must be explicit.
- `readme` must point to the intended package-registry README.

## Public API Rules

Create or update a spec when changing:

- top-level imports;
- facade/client signatures;
- public configuration objects;
- public result models;
- public exceptions;
- documented behavior;
- import paths used by consumers.

Apply [[sdk-public-api-compatibility-checklist]].

## Release Rules

Release changes must use [[prepare-sdk-release]] and
[[sdk-release-checklist]].

Do not publish if:

- quality gates are failing;
- package metadata is invalid;
- README rendering assumptions are unresolved;
- tag/version alignment is unclear;
- secrets are missing or exposed.

## Forbidden Practices

Do not:

- mix active context with decisions;
- store execution procedures in context;
- create duplicate sources of truth;
- publish without validating package artifacts;
- hide public API breaking changes inside internal refactors;
- add dependencies without validating direct usage;
- copy PipeBridge-specific facts into a new SDK as if they were universal;
- keep outdated generated artifacts active;
- bypass runbooks when they exist;
- treat workflow templates as production-ready without customization.

## Evolution Rules

Prefer incremental evolution over rewrites.

For significant changes:

1. define or update a decision when the constraint is long-lived;
2. create or update a spec when implementation design is needed;
3. update context after reality changes;
4. update runbooks/checklists when procedure or validation changes;
5. validate wikilinks when documentation relationships change.

## Related Files

- [[CURRENT_CONTEXT]]
- [[0002-python-sdk-lifecycle-policy]]
- [[0003-sdk-public-api-compatibility-policy]]
- [[0004-sdk-release-publication-policy]]
- [[0005-sdk-documentation-and-examples-policy]]
- [[WIKILINK_RULES]]
- [[PROCESS_KNOWLEDGE_RULES]]
