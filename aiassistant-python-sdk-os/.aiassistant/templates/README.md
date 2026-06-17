# Templates

This directory stores reusable starter files for Python SDK projects.

Templates are scaffolding, not source of truth.

## Rules

- Adapt every template to the real SDK.
- Remove placeholders from finished files.
- Do not treat templates as active context.
- Do not copy PipeBridge-specific facts into a new SDK.
- Validate package metadata after using SDK project templates.
- Treat workflow templates as starter files, not production-ready CI.

## Available Templates

Governance:

- [[current-context-sdk-template]]
- [[decision-template]]
- [[checklist-template]]
- [[feedback-template]]
- [[roadmap-template]]
- [[spec-template]]
- [[prompt-template]]

SDK project:

- [[pyproject-template]]
- [[readme-sdk-template]]
- `sdk-project/pyproject-template.toml`
- `sdk-project/package-init-template.py`
- `sdk-project/facade-template.py`

Documentation:

- `docs/conf-template.py`
- `docs/index-template.rst`
- `docs/api-template.rst`

GitHub Actions:

- `github-workflows/ci.yml`
- `github-workflows/docs.yml`
- `github-workflows/publish.yml`
- `github-workflows/release.yml`

Process knowledge:

- [[process-knowledge-map-template]]
- [[process-index-template]]
- [[business-rule-template]]
- [[system-note-template]]

## Usage

1. Choose the closest template.
2. Copy it to the correct destination.
3. Replace placeholders with real SDK facts.
4. Remove unused sections.
5. Validate using the relevant runbook and checklist.

