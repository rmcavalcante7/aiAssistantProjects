# Setup Python SDK Repository

## Objective

Create or validate the baseline repository structure for a Python SDK.

The result should be installable, testable, documented, and ready for controlled
public API evolution.

## When To Use

Use when:

- starting a new SDK;
- normalizing an existing library into a package;
- preparing a project for publication;
- adding missing SDK repository structure.

## Preconditions

- Active context exists.
- Package name and import name are known.
- Supported Python versions are known.
- Public API direction is at least minimally defined.
- Release target is known or explicitly undecided.

## Inputs

- Package name.
- Import name.
- Runtime dependencies.
- Dev/docs dependency preferences.
- GitHub/PyPI/internal publication intent.
- Docs publication intent.
- Test strategy.

## Recommended Structure

```text
.
  README.md
  CHANGELOG.md
  pyproject.toml
  src/
    <package>/
      __init__.py
  tests/
    unit/
    functional/
    integration/
  docs/
  examples/
  .github/
    workflows/
```

Use only directories that are relevant to the real SDK. Do not create empty
structure that implies behavior the project does not have.

## Steps

1. Create `src/<package_name>/`.
2. Define initial public exports in `src/<package_name>/__init__.py`.
3. Create a facade/client module only when the public API direction supports it.
4. Create `tests/unit`, `tests/functional`, and `tests/integration` when each
   scope is relevant.
5. Create `docs/` if Sphinx docs are planned.
6. Create `examples/` or `use_cases/` for public usage examples.
7. Generate `pyproject.toml` by following [[generate-pyproject-runbook]].
8. Create a README by following [[generate-sdk-readme]].
9. Add GitHub workflow files from `templates/github-workflows/` only after
   project metadata and validation commands are real.
10. Add `.env.example` for required integration-test environment variables.
11. Confirm `.gitignore` excludes virtual environments, build artifacts, local
   IDE files, and secrets.
12. Apply [[sdk-implementation-checklist]].

## Validation

- Package imports from `src/`.
- `pip install -e .[dev]` works when dependencies are available.
- Tests can be discovered.
- README and pyproject agree on package identity.
- Public exports are intentional.
- No secrets or local-only files are required for import.
- Workflow templates were customized before use.

## Outputs

- SDK repository skeleton ready for implementation.

## Failure Scenarios

### Package Does Not Import

Check `src/` layout, package discovery, `__init__.py`, and editable install.

### Workflow Fails Immediately

Check whether optional directories such as `examples/` or `docs/` exist and
whether workflow commands were customized.

### Tests Need Live Credentials

Move live coverage to `tests/integration` and require explicit environment
variables.

### Public API Direction Is Too Vague

Create only package scaffolding and context. Defer facade/domain namespaces
until public behavior is agreed.

## Related Files

- [[0002-python-sdk-lifecycle-policy]]
- [[generate-pyproject-runbook]]
- [[generate-sdk-readme]]
- [[validate-sdk-quality-gates]]

