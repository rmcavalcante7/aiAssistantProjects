# Setup Sphinx Docs

## Objective

Create or validate Sphinx documentation for a Python SDK.

## When To Use

Use when:

- the SDK has a stable public API;
- docs are published to GitHub Pages or another docs site;
- public API documentation changes;
- docstrings or generated API docs need validation.

## Preconditions

- Package imports locally.
- Optional docs dependencies are configured.
- README and public API direction exist.
- Public modules to document are known.

## Inputs

- Package name.
- Docs title.
- Repository URL.
- Documentation URL.
- Logo path or URL.
- Public API modules to document.
- Internal modules that should be hidden or marked `:no-index:`.

## Steps

1. Create `docs/`.
2. Start from `templates/docs/conf-template.py`.
3. Create `index.rst`, `quickstart.rst`, `api.rst`, and `development.rst` as
   needed.
4. Document public API first.
5. Keep examples aligned with README and tests.
6. Mark internal modules with `:no-index:` when autodoc duplicates public API
   exports.
7. Build docs locally.
8. If publishing with GitHub Pages, configure the docs workflow template.

## Validation

Run when tooling is available:

```powershell
python -m pip install -e .[docs]
sphinx-build -b html docs docs/_build/html
```

Confirm:

- build exits successfully;
- public imports render correctly;
- examples do not reference undefined objects;
- internal modules do not create duplicate object warnings;
- docs link to the correct repository and package version.

## Failure Scenarios

### Duplicate Object Warnings

Check whether public exports and internal modules are both documented. Use
`:no-index:` for internal pages when appropriate.

### Import Errors During Docs Build

Check editable install, `sys.path`, package discovery, and missing optional
dependencies.

### Broken Examples

Fix examples or move them out of published docs until they are valid.

## Outputs

- Buildable SDK documentation.

## Related Files

- [[0005-sdk-documentation-and-examples-policy]]
- [[sdk-documentation-quality-checklist]]

