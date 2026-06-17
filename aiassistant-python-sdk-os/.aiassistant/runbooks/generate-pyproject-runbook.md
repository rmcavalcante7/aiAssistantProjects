# Generate pyproject.toml

## Objective

Create or validate the SDK `pyproject.toml` so the package can be installed,
tested, built, and published reproducibly.

`pyproject.toml` is the installability contract of a Python SDK.

## When To Use

Use when:

- starting a new SDK;
- changing dependencies;
- changing supported Python versions;
- changing package metadata;
- preparing publication;
- fixing install/build failures.

## Preconditions

- Active context exists.
- Package name and import name are known.
- Supported Python versions are known.
- Runtime dependencies are known or can be extracted from imports.
- Versioning strategy is known or explicitly undecided.

## Inputs

- Package name.
- Import/package directory.
- Description.
- Authors.
- License.
- Python version range.
- Direct runtime dependencies.
- Optional dev/docs dependencies.
- README path.
- Repository, docs, and issue URLs.
- Versioning strategy.

## Required Sections

The file should define:

- `[build-system]`;
- `[project]`;
- `[project.optional-dependencies]`;
- `[project.urls]`;
- package discovery under `src/`;
- versioning configuration when applicable;
- `black`, `mypy`, and `pytest` configuration when used.

## Steps

1. Start from [[pyproject-template]] or
   `templates/sdk-project/pyproject-template.toml`.
2. Fill real package metadata.
3. Choose versioning:
   - `setuptools_scm` for tag-driven releases;
   - static version only when explicitly chosen.
4. Set `requires-python` to the real supported range.
5. List direct runtime dependencies only.
6. Put `black`, `mypy`, `pytest`, `build`, `twine`, Sphinx, and docs tools in
   optional extras.
7. Configure package discovery for `src/`.
8. Configure `black`.
9. Configure `mypy`.
10. Configure `pytest`.
11. Validate dependency coverage against imports.
12. Confirm README path exists and is the intended registry long description.

## Dependency Validation

Review imports in SDK runtime code:

- ignore standard-library imports;
- ignore internal package imports;
- map external imports to direct dependencies;
- remove unused dependencies;
- keep transitive dependencies out unless directly imported or required by a
  public extra.

Development and docs tools must not be runtime dependencies.

## Validation Commands

Run when tooling is available:

```powershell
python -m pip install -e .[dev]
python -m pip install -e .[docs]
python -m build
twine check dist/*
```

Also validate:

- package imports after editable install;
- README referenced by `readme` exists;
- metadata renders without errors;
- version produced by build matches the active strategy.

## Outputs

- Valid `pyproject.toml`.
- Known dependency/runtime assumptions.

## Failure Scenarios

### Import Works Locally But Fails After Install

Check package discovery, `src/` layout, missing `__init__.py`, and editable
install behavior.

### Version Does Not Match Tag

Check `setuptools_scm` configuration, tag name, and whether Git history is
available in CI.

### PyPI README Fails

Check `readme`, content type, relative images, and `twine check` output.

### Dependency Missing At Runtime

Add the direct runtime dependency and rerun install/build validation.

## Related Files

- [[0002-python-sdk-lifecycle-policy]]
- [[0004-sdk-release-publication-policy]]
- [[prepare-sdk-release]]

