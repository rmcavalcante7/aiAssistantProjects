# Checklists

This directory stores validation criteria.

Checklists define what must be verified before delivery, release, publication,
or process documentation completion.

They do not execute work. Use runbooks for execution.

## When To Create A Checklist

Create a checklist when:

- failure is costly;
- public API compatibility must be preserved;
- release readiness must be proven;
- documentation must meet publication quality;
- integration tests can mutate external systems;
- package metadata can break installation or PyPI rendering.

Do not create a checklist for:

- execution steps;
- architectural rationale;
- temporary debugging notes.

## Required Shape

Each checklist should include:

- objective;
- when to use;
- verifiable items;
- related files.

Each item must be concrete enough to answer yes/no.

## Execution Rule

When applying a checklist:

- evaluate every item;
- do not assume success;
- state which validations could not be run;
- explain residual risk.

## Common SDK Checklists

- [[sdk-implementation-checklist]]
- [[sdk-public-api-compatibility-checklist]]
- [[sdk-documentation-quality-checklist]]
- [[sdk-release-checklist]]
- [[process-documentation-quality-checklist]]

