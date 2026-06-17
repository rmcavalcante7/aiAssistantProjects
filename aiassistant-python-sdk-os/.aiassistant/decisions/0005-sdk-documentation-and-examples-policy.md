# SDK Documentation And Examples Policy

## Status

Accepted

## Context

For an SDK, documentation is part of the product surface. The PipeBridge
reference showed that README rendering on GitHub and PyPI, Sphinx docs, public
examples, logo URLs, badges, and API docs can all affect adoption and release
quality.

## Decision

SDK documentation must evolve with public behavior.

Required documentation layers:

- README for product overview, installation, quick start, public API summary,
  links, and release status;
- Sphinx docs for deeper API and usage documentation when the SDK is stable
  enough to publish docs;
- examples or use cases that exercise public API paths;
- changelog or release notes for published changes.

README files intended for PyPI must use assets that render publicly. Local-only
relative image paths should not be used for PyPI-facing logos or badges.

Public API changes must update docs and examples before release.

## Alternatives Considered

- Keep only code docstrings: rejected because SDK users need onboarding and
  examples.
- Maintain a reduced PyPI README by default: rejected because it can drift from
  the canonical product README.
- Generate docs only after release: rejected because docs build failures should
  be caught before publication.

## Consequences

Benefits:

- users can adopt the SDK faster;
- PyPI and GitHub stay aligned;
- public behavior changes are visible.

Risks:

- documentation can become stale if treated as optional;
- generated docs may require Sphinx-specific maintenance.

## Related Files

- [[generate-sdk-readme]]
- [[setup-sphinx-docs]]
- [[sdk-documentation-quality-checklist]]
- [[prepare-sdk-release]]

