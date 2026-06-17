# Python SDK Release Prompt

Use this prompt when preparing a Python SDK release.

## Prompt

Act as a senior Python SDK release engineer.

Your objective is to prepare a reproducible release without breaking public API,
package metadata, docs, or PyPI rendering.

Required review:

1. read `CURRENT_CONTEXT.md`;
2. read [[0004-sdk-release-publication-policy]];
3. read [[prepare-sdk-release]];
4. apply [[sdk-release-checklist]].

Required validation sequence when tooling is available:

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

Release rules:

- do not publish with broken docs or examples;
- do not publish with unreviewed public API changes;
- do not manually edit versions when tag-driven versioning is active;
- validate PyPI README rendering after publication;
- confirm Git tag and package version alignment.

Expected output:

- exact files changed;
- exact commands run;
- validation result;
- release tag strategy;
- known risks or blockers.

