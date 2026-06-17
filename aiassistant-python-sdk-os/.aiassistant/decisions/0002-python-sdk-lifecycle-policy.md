# Python SDK Lifecycle Policy

## Status

Accepted

## Context

This template is intended for Python SDKs and libraries. SDKs differ from
internal scripts because public imports, package metadata, documentation,
examples, and release artifacts become contracts for downstream users.

The PipeBridge reference showed that successful SDK work requires more than
working code: public facade stability, packaging, CI, docs, PyPI rendering, and
release workflows all need explicit governance.

## Decision

Python SDK projects using this template must treat the full SDK lifecycle as
part of the product:

- project context must define package identity and public API direction;
- `src/` layout is the default package structure;
- `pyproject.toml` is the installability contract;
- runtime dependencies must be direct and minimal;
- public API behavior must be covered by tests and documentation;
- docs and examples must evolve with public behavior;
- release validation must cover formatting, typing, tests, build, and package
  metadata.

## Alternatives Considered

- Treat the SDK like an internal script: rejected because package consumers need
  stable contracts.
- Start with packaging later: rejected because packaging decisions affect imports,
  docs, tests, and CI from the beginning.
- Require one rigid architecture for all SDKs: rejected because APIs vary, but
  lifecycle gates remain consistent.

## Consequences

Benefits:

- new SDKs start with release discipline;
- packaging issues surface early;
- agents have clear validation paths.

Risks:

- small experimental libraries may feel heavier;
- users must customize templates instead of copying them blindly.

## Related Files

- [[CURRENT_CONTEXT]]
- [[setup-python-sdk-repository]]
- [[generate-pyproject-runbook]]
- [[validate-sdk-quality-gates]]
- [[sdk-implementation-checklist]]

