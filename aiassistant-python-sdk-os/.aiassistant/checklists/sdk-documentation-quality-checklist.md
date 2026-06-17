# SDK Documentation Quality Checklist

## Objective

Validate README, docs, examples, and public API documentation.

## README

- [ ] README package name matches `pyproject.toml`.
- [ ] Install command is correct.
- [ ] Quick start uses public API only.
- [ ] Authentication/configuration examples are safe.
- [ ] Public API summary matches actual exports.
- [ ] Examples avoid private internals.
- [ ] Documentation links are current.
- [ ] License and author information are current.

## PyPI / Registry Rendering

- [ ] `pyproject.toml` points to the intended README.
- [ ] PyPI-facing images use public URLs.
- [ ] Badges are intentional and render publicly.
- [ ] Relative local-only image paths are avoided for registry-facing assets.
- [ ] `twine check dist/*` passes when package artifacts are built.

## Sphinx / API Docs

- [ ] Sphinx docs build when docs are active.
- [ ] Public API docs prioritize public imports.
- [ ] Internal modules do not create duplicate object warnings.
- [ ] Examples do not reference undefined objects.
- [ ] Public docstrings render correctly.

## Examples And Changelog

- [ ] Examples are aligned with tests when practical.
- [ ] Examples do not require real secrets.
- [ ] Integration examples clearly mark live/destructive behavior.
- [ ] Changelog/release notes mention public behavior changes.

## Related Files

- [[0005-sdk-documentation-and-examples-policy]]
- [[generate-sdk-readme]]
- [[setup-sphinx-docs]]

