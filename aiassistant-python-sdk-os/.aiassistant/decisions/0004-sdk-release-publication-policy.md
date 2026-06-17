# SDK Release And Publication Policy

## Status

Accepted

## Context

The PipeBridge reference established a robust release pattern:

- CI validates formatting, typing, and tests;
- documentation is generated when public docs change;
- package artifacts are built and checked before publication;
- publication is driven by Git tags;
- GitHub Release and PyPI publication can be separate workflows triggered by the
  same tag.

These practices are reusable for Python SDKs.

## Decision

SDK releases must be validated before publication.

Default release policy:

- use semantic versioning;
- prefer tag-driven versioning with `setuptools_scm` when the project is
  release-managed through Git tags;
- run `black --check`, `mypy`, and `pytest` before release;
- build artifacts with `python -m build`;
- validate artifacts with `twine check dist/*`;
- publish to PyPI only from release tags when configured;
- create GitHub Releases from the same tag when configured;
- confirm PyPI package version matches the Git tag;
- confirm PyPI README rendering after publication.

Manual versioning is allowed only when the project explicitly chooses it in
context or decision.

## Alternatives Considered

- Publish manually from local machines: rejected as the default because it is
  less reproducible.
- Require tag-driven releases for every project: rejected because private
  internal packages may use different release controls.
- Skip PyPI rendering checks: rejected because README rendering issues are common
  and user-facing.

## Consequences

Benefits:

- releases become reproducible;
- package metadata failures are caught before upload;
- version drift is reduced.

Risks:

- workflow secrets and PyPI tokens must be configured correctly;
- tag-triggered workflows can appear duplicated when publish and release jobs
  run separately.

## Related Files

- [[prepare-sdk-release]]
- [[sdk-release-checklist]]
- [[generate-pyproject-runbook]]
- [[python-sdk-release-prompt]]

