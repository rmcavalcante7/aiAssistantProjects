# Prepare SDK Release

## Objective

Prepare, validate, tag, and publish a Python SDK release.

A release is a validated, installable, documented artifact. It is not only a
Git tag.

## When To Use

Use when a release is being prepared for:

- PyPI;
- an internal package registry;
- GitHub Release;
- a documented internal distribution.

## Preconditions

- Active context exists.
- Release scope is defined in roadmap or changelog.
- Public API changes have specs and compatibility review.
- README/docs/examples match public behavior.
- Required CI secrets are configured when publishing.
- Working tree is understood and release branch is intentional.

## Inputs

- Target version or Git tag.
- Changelog entries.
- Release branch or `main` state.
- PyPI/internal registry publication target.
- Documentation publication target.
- Required environment variables and CI secrets.

## Files To Review

Review when present:

- `README.md`;
- `pyproject.toml`;
- `CHANGELOG.md`;
- `src/<package>/__init__.py`;
- public facade/client modules;
- public models and exceptions;
- docs and examples;
- `.github/workflows/ci.yml`;
- `.github/workflows/publish.yml`;
- `.github/workflows/release.yml`;
- `.github/workflows/docs.yml`.

## Steps

1. Read [[sdk-release-checklist]].
2. Confirm release scope.
3. Confirm versioning strategy.
4. Confirm public API compatibility status.
5. Confirm docs/examples impact.
6. Run [[validate-sdk-quality-gates]].
7. Build docs if docs changed.
8. Confirm PyPI/registry README rules:
   - README source is intentional;
   - public images use public URLs;
   - badges render publicly;
   - release/version badge strategy is intentional.
9. Confirm no secrets or local artifacts are included.
10. Commit final release changes.
11. Push the release branch.
12. Create tag `vX.Y.Z` when using tag-driven releases.
13. Push the tag.
14. Monitor publish and release workflows.
15. Validate PyPI or registry page.
16. Validate GitHub Release.
17. Validate docs site when docs changed.
18. Record any incident as feedback or context update when the process changed.

## Recommended Local Validation

```powershell
python -m black --check src tests examples
python -m mypy src
python -m pytest tests/unit tests/functional -v
python -m build
twine check dist/*
```

If docs changed:

```powershell
sphinx-build -b html docs docs/_build/html
```

If release scope includes live provider behavior:

```powershell
python -m pytest tests/integration -v
```

## Tag-Driven Release Notes

When `setuptools_scm` is active:

- do not manually edit package versions for release;
- create semantic tags such as `vX.Y.Z`;
- ensure CI has Git history available;
- confirm published version matches the tag.

It is expected that separate PyPI publish and GitHub Release workflows may both
run from the same tag.

## Validation

- Git tag matches package version.
- Built artifacts pass metadata checks.
- Published package installs.
- README renders correctly on the registry.
- Docs remain reachable.
- Changelog matches the release.

## Failure Scenarios

### PyPI Upload Fails With Authentication Error

Check token scope, secret name, project ownership, and whether the version was
already published.

### Published README Renders Incorrectly

Fix README assets, badges, links, or `pyproject.toml` readme configuration and
release a corrected version.

### Tag Version Does Not Match Package Version

Check `setuptools_scm`, tag format, CI checkout depth, and local build output.

### Docs Workflow Fails

Fix docs before considering the release complete when docs changed.

## Outputs

- Published SDK release or a clear explanation of what blocked publication.
- Validation summary.
- Follow-up feedback/spec/runbook updates when release process gaps were found.

## Related Files

- [[0004-sdk-release-publication-policy]]
- [[sdk-release-checklist]]
- [[python-sdk-release-prompt]]

