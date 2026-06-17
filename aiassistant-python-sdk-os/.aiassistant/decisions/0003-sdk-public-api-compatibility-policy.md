# SDK Public API Compatibility Policy

## Status

Accepted

## Context

An SDK's value depends on stable public behavior. The PipeBridge reference
showed that a facade, public domain namespaces, semantic exceptions, result
models, and documented examples become part of the user contract.

Breaking a public import or method signature can be more damaging than changing
internal implementation.

## Decision

The public API must be explicitly identified and protected.

Public API includes:

- top-level imports from the package;
- facade classes and domain namespaces;
- public method names and signatures;
- public configuration objects;
- public models and result objects;
- documented exception types;
- documented behavior in README, docs, and examples.

Any public API change must:

- have a spec or explicit decision;
- document compatibility impact;
- update tests;
- update README/docs/examples;
- pass [[sdk-public-api-compatibility-checklist]].

Additive APIs are preferred. Breaking changes require an explicit versioning and
migration decision.

## Alternatives Considered

- Let public API evolve organically: rejected because downstream consumers need
  stability.
- Freeze all APIs immediately: rejected because early SDKs still need iterative
  design.
- Hide all internals without tests: rejected because internals still need unit
  coverage when they carry important behavior.

## Consequences

Benefits:

- fewer accidental breaking changes;
- clearer release notes;
- public examples remain trustworthy.

Risks:

- public API changes require more ceremony;
- poorly defined public/private boundaries can slow implementation until clarified.

## Related Files

- [[CURRENT_CONTEXT]]
- [[sdk-public-api-compatibility-checklist]]
- [[sdk-implementation-checklist]]
- [[specs/README|specs guidance]]
- [[python-sdk-implementation-prompt]]

