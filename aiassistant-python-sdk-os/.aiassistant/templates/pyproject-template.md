# pyproject Template

Use `sdk-project/pyproject-template.toml` as the starting point for a Python SDK
`pyproject.toml`.

Apply [[generate-pyproject-runbook]] after copying it.

Key rules:

- use direct runtime dependencies only;
- keep dev and docs tools in optional extras;
- choose versioning strategy deliberately;
- validate with `python -m build` and `twine check dist/*`;
- align README and package metadata.

