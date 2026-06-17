# SDK Release Checklist

## Objective

Validate release readiness before tagging or publishing.

## Scope And Version

- [ ] Release scope is confirmed.
- [ ] Versioning strategy is confirmed.
- [ ] Target tag or version is confirmed.
- [ ] Changelog is updated.
- [ ] Release branch or `main` state is intentional.

## Public API And Docs

- [ ] Public API changes have compatibility review.
- [ ] Breaking changes have explicit approval and migration guidance.
- [ ] README is updated.
- [ ] Docs are updated.
- [ ] Examples are updated.
- [ ] Changelog/release notes mention public impact.

## Local Validation

- [ ] `python -m black --check ...` passes.
- [ ] `python -m mypy src` passes or exceptions are justified.
- [ ] Unit tests pass.
- [ ] Functional tests pass.
- [ ] Required integration tests pass or are explicitly deferred.
- [ ] Destructive tests used owned data and explicit flags.
- [ ] `python -m build` passes.
- [ ] `twine check dist/*` passes.
- [ ] Sphinx docs build if docs changed.

## Package Metadata

- [ ] Package name is correct.
- [ ] README path is correct.
- [ ] Runtime dependencies are direct and minimal.
- [ ] Dev/docs dependencies are optional extras.
- [ ] Supported Python versions are correct.
- [ ] License and project URLs are correct.

## Publication

- [ ] PyPI/internal registry credentials are configured.
- [ ] GitHub release workflow is configured when applicable.
- [ ] Docs workflow is configured when applicable.
- [ ] Published package version will match the release tag.
- [ ] PyPI/registry README rendering assumptions are checked.
- [ ] No secrets or local artifacts are included.

## Post-Release

- [ ] Published package page was checked.
- [ ] GitHub Release was checked when applicable.
- [ ] Docs site was checked when applicable.
- [ ] Any incident was captured as feedback or runbook update.

## Related Files

- [[0004-sdk-release-publication-policy]]
- [[prepare-sdk-release]]
- [[validate-sdk-quality-gates]]
- [[python-sdk-release-prompt]]

