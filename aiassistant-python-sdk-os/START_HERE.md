# Start Here

Use this folder as the starting point for a new Python SDK or client library.

## 1. Read First

Read in this order:

1. `AGENTS.md`
2. `.aiassistant/project_context/CURRENT_CONTEXT.md`
3. `.aiassistant/rules/AGENTS.md`
4. `.aiassistant/runbooks/bootstrap-python-sdk-context.md`

## 2. Initialize The Real SDK Context

Before creating code, replace the template context with the real SDK context.

Follow:

```text
.aiassistant/runbooks/bootstrap-python-sdk-context.md
```

Do not copy PipeBridge/Pipefy facts into the new SDK. They were used only as
reference material for this template.

## 3. Create The SDK Structure

Follow:

```text
.aiassistant/runbooks/setup-python-sdk-repository.md
```

Use templates from:

```text
.aiassistant/templates/sdk-project/
.aiassistant/templates/github-workflows/
.aiassistant/templates/docs/
```

## 4. Package And Validate

Create `pyproject.toml` with:

```text
.aiassistant/runbooks/generate-pyproject-runbook.md
```

Validate with:

```text
.aiassistant/runbooks/validate-sdk-quality-gates.md
```

## 5. Release

When the SDK is ready to publish, follow:

```text
.aiassistant/runbooks/prepare-sdk-release.md
```

## Non-Negotiable Rules

- `CURRENT_CONTEXT.md` is the only active runtime context.
- Public API is a contract.
- `pyproject.toml` is the installability contract.
- README, docs, examples, tests, and release workflows are part of the SDK
  product.
- Do not publish without validating formatting, typing, tests, build artifacts,
  and package metadata.

