# Generic Python Package Publish

This runbook defines the standard process to prepare, validate, and publish a Python project.

It ensures:

- reproducible builds
- clean dependency management
- consistent releases
- safe publication (Git and optionally PyPI)

This runbook applies only to publishable Python packages, libraries, and SDKs.

It does NOT apply by default to pure automations, RPAs, or internal scripts that are not released as packages.

---

# 🧠 Objective

Provide a repeatable, production-grade process to:

- prepare the project
- validate correctness
- build artifacts
- publish safely

---

# 📌 When to use

Use this runbook when:

- releasing a new version
- publishing a package to PyPI
- tagging a production-ready version
- validating a project for distribution

---

# 🧱 Step 1 - Validate project structure

Ensure the project contains:

- `README.md`
- `pyproject.toml`
- source directory (e.g. `src/` or package root)
- tests

---

# 🧱 Step 2 - Validate README

- README must follow project type (product or operational)
- Quick Start must work
- no outdated information
- links must be valid

---

# 🧱 Step 3 - Validate pyproject.toml

- dependencies include ONLY required libraries
- dev dependencies are separated
- Python version is correct
- metadata is complete

Test installation:

```bash
pip install -e .
```

---

# 🧱 Step 4 - Code quality

Run:

```bash
black .
mypy <package_or_src_path>
```

Rules:

- no formatting issues
- no type errors

---

# 🧱 Step 5 - Run tests

```bash
pytest -v
```

Rules:

- all tests must pass
- no flaky tests

---

# 🧱 Step 6 - Build artifacts

```bash
python -m build
```

This generates:

- `dist/*.whl`
- `dist/*.tar.gz`

---

# 🧱 Step 7 - Validate build

Install built package in a clean environment:

```bash
pip install dist/*.whl
```

Test basic usage:

- import works
- no missing dependencies

---

# 🧱 Step 8 - Git validation

Before publishing:

- ensure correct branch (usually `main`)
- commit all changes
- no debug code
- no temporary files

---

# 🧱 Step 9 - Versioning

Update version in:

- `pyproject.toml`

Follow semantic versioning:

- patch → bug fix
- minor → backward-compatible feature
- major → breaking change

---

# 🧱 Step 10 - Tag release

```bash
git tag vX.Y.Z
git push origin main --tags
```

---

# 🧱 Step 11 - Publish to PyPI (optional)

```bash
pip install twine
twine upload dist/*
```

Rules:

- do not overwrite existing versions
- validate credentials
- confirm package page

---

# 🧱 Step 12 - Post-release validation

- verify PyPI page
- verify installation works
- verify documentation links

---

# 🚫 Forbidden practices

- publishing without tests
- publishing with broken README
- including unused dependencies
- skipping build validation
- releasing without version control

---

# 🔍 Final checklist

- README validated
- pyproject validated
- code formatted
- types checked
- tests passed
- build successful
- install tested
- version updated
- tag created

---

# 🧠 Key Principle

A release is not just code.

It is a **validated, installable, reproducible artifact**.

---

END OF FILE
