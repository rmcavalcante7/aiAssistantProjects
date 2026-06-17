# Validate SDK Quality Gates

## Objective

Run the standard validation sequence for SDK implementation and release
readiness.

## When To Use

Use before:

- finishing public API changes;
- merging release-bound work;
- tagging a release;
- publishing package artifacts;
- declaring documentation-ready status.

## Preconditions

- Development dependencies are installed.
- Active context identifies package structure.
- Tests and docs paths are known.
- Integration-test credentials are configured when live validation is required.

## Inputs

- Source directory, usually `src`.
- Test directories.
- Examples directory if present.
- Docs directory if active.
- Optional integration-test environment variables.

## Standard Sequence

Run the applicable commands in this order:

```powershell
python -m black --check src tests examples
python -m mypy src
python -m pytest tests/unit tests/functional -v
python -m build
twine check dist/*
```

If documentation changed:

```powershell
sphinx-build -b html docs docs/_build/html
```

If live integration behavior changed and credentials are configured:

```powershell
python -m pytest tests/integration -v
```

## Validation Criteria

- Formatting passes.
- Typing passes or known exceptions are explicitly justified.
- Unit tests pass.
- Functional public API tests pass.
- Integration tests pass when required and available.
- Package builds.
- `twine check` passes.
- Docs build passes when docs changed.

## Integration Test Safety

Before running destructive integration tests, confirm:

- credentials point to the intended environment;
- tests use owned test data;
- reference fixtures are read-only;
- cleanup behavior is documented;
- explicit opt-in flags are required for mutation.

## Outputs

- Quality gate result.
- List of commands run.
- List of commands skipped and why.
- Residual risk when any gate cannot be run.

## Failure Scenarios

### Formatting Fails

Run `python -m black src tests examples` only when formatting changes are
acceptable for the current task.

### Typing Fails

Fix type contracts or explicitly document why strict typing cannot pass yet.
Do not hide public API typing problems.

### Build Fails

Check `pyproject.toml`, package discovery, README path, and versioning strategy.

### Docs Fail

Fix docstring/reStructuredText errors before release.

## Related Files

- [[sdk-implementation-checklist]]
- [[sdk-release-checklist]]
- [[prepare-sdk-release]]

