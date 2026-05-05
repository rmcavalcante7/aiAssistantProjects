# Generate pyproject.toml

This runbook defines how to create and validate a correct `pyproject.toml` for a Python project.

The goal is to ensure:

- the project can be installed via `pip install`
- dependencies are accurate and minimal
- the project is reproducible
- no unnecessary or missing dependencies exist

This runbook applies to installable Python projects.

For pure automations or internal scripts that will not be packaged, this runbook is optional and only applies if the project explicitly needs a `pyproject.toml`.

---

# 🧠 Objective

Create a `pyproject.toml` that:

- reflects the real runtime requirements
- contains ONLY required dependencies
- supports packaging and distribution
- separates runtime and development dependencies

---

# 📌 When to use

Use this runbook when:

- creating a new project
- preparing a project for distribution
- fixing dependency issues
- cleaning an existing `pyproject.toml`

---

# ⚠️ CRITICAL RULE

Dependencies MUST include ONLY:

→ libraries that are directly required for the project to run

DO NOT include:

- unused libraries
- transitive dependencies (dependencies of dependencies)
- development tools (black, pytest, etc.)

---

# 🧱 Required structure

A valid `pyproject.toml` MUST include:

## 1. Build system

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## 2. Project metadata

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Short description"
readme = "README.md"
requires-python = ">=3.X,<3.Y"
```

---

## 3. Dependencies (CRITICAL SECTION)

```toml
dependencies = [
  "requests==X.Y.Z",
  "pandas==X.Y.Z"
]
```

Rules:

- include ONLY libraries used in the code
- pin versions (recommended for production)
- avoid unnecessary dependencies
- validate imports vs dependencies

---

## 4. Authors (optional but recommended)

```toml
[[project.authors]]
name = "Author Name"
```

---

## 5. License

```toml
[project.license]
text = "MIT"
```

---

## 6. Optional dependencies (dev tools)

```toml
[project.optional-dependencies]
dev = [
  "black",
  "mypy",
  "pytest"
]
```

Rules:

- dev tools MUST NOT be in main dependencies
- keep dev dependencies separate

---

## 7. Tool configuration (optional)

Example:

```toml
[tool.black]
line-length = 100

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

# 🔄 Dependency validation process (CRITICAL)

Before finalizing:

## Step 1 - Extract imports from code

Identify all imports:

- internal modules → ignore
- external libraries → must be listed

---

## Step 2 - Compare with dependencies

For each dependency:

- confirm it is actually used
- remove unused ones

---

## Step 3 - Detect missing dependencies

If code imports a library that is NOT in dependencies:

→ ADD IT

---

## Step 4 - Validate installability

Test:

```bash
pip install .
```

or:

```bash
pip install -e .
```

---

## Step 5 - Runtime validation

Run the project:

- no import errors
- no missing modules
- no hidden dependencies

---

# 🚫 Forbidden practices

- adding libraries "just in case"
- keeping unused dependencies
- mixing dev dependencies with runtime dependencies
- relying on globally installed packages
- skipping installation validation

---

# 🔍 Validation checklist

Before finalizing:

- all imports are covered
- no unused dependencies exist
- `pip install` works
- project runs in a clean environment
- dev tools are isolated

---

# 🧠 Key Principle

`pyproject.toml` is:

→ the installation contract of the project

If it is wrong:

→ the project is broken

---

END OF FILE
