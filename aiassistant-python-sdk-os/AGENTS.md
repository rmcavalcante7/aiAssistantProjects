# AGENTS.md

This file defines how AI agents must operate in this Python SDK operating
system.

It must be followed before any implementation, documentation, release,
packaging, repository-structure, or governance change.

## Mandatory Reading Order

1. `.aiassistant/project_context/CURRENT_CONTEXT.md`
2. `.aiassistant/decisions/`
3. `.aiassistant/runbooks/`
4. `.aiassistant/checklists/`
5. `.aiassistant/feedback/`
6. `.aiassistant/roadmap/`
7. `.aiassistant/specs/`
8. `.aiassistant/prompts/`
9. `.aiassistant/rules/CONTEXT_RULES.md`
10. `.aiassistant/rules/REPOSITORY_GUIDELINES.md`
11. `.aiassistant/rules/WIKILINK_RULES.md`
12. `.aiassistant/rules/PROCESS_KNOWLEDGE_RULES.md`
13. `.aiassistant/rules/AGENTS.md`

## Runtime Context

- `CURRENT_CONTEXT.md` is the only active context.
- Historical context files are not active context.
- Do not infer missing SDK scope, package name, public API, integrations, or
  release behavior.
- If context is missing or unclear, stop and ask for clarification.
- If the target repository has not been initialized yet, follow
  `.aiassistant/runbooks/bootstrap-python-sdk-context.md`.

## SDK Bias

This template is optimized for SDK and library development.

Default expectations:

- `src/` layout;
- `pyproject.toml` packaging;
- typed public API;
- stable facade or top-level entrypoint;
- semantic exception taxonomy;
- unit, functional, and integration tests;
- Sphinx-compatible docstrings;
- README suitable for GitHub and PyPI;
- release by Git tag when `setuptools_scm` is used.

Do not copy reference-project details as active facts. Package names, external
systems, environment variables, workflow names, and release URLs must come from
the target SDK context.

## Public API Rule

Before changing exported objects, method signatures, import paths, exception
types, result models, or documented behavior:

1. read the relevant spec or create one;
2. evaluate backward compatibility;
3. update docs and examples;
4. add or update tests;
5. apply the public API compatibility checklist.

Public API includes imports, facade/client methods, configuration objects,
result models, documented exceptions, README examples, and docs examples.

## Quality Gates

For SDK work, validate with the relevant commands from:

- `.aiassistant/runbooks/validate-sdk-quality-gates.md`
- `.aiassistant/runbooks/prepare-sdk-release.md`

Do not mark a release-ready change complete if formatting, typing, tests,
packaging, or docs are known to be broken.

When tooling cannot be run, state exactly which gates were not run and why.

## Root Delegation

The detailed engineering rules live in:

```text
.aiassistant/rules/AGENTS.md
```

This root file is the entrypoint. The internal file is the complete SDK
engineering standard.

## Final Rule

An SDK is a contract.

Treat public imports, documented behavior, package metadata, release workflow,
and examples as part of that contract.

