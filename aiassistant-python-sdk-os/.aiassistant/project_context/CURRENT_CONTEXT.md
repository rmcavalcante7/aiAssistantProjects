# Current Context

## 1. Project Overview

This repository is a Python SDK-focused variant of the AI Repository Operating
System.

Its purpose is to provide a reusable `.aiassistant` structure for building,
documenting, validating, and releasing Python SDKs or client libraries with AI
assistance.

The current version consolidates:

- the governance model from the existing generic AI Repository Operating System;
- release, documentation, testing, packaging, and public API lessons from a real
  Pipefy SDK project reference.

## 2. System Architecture

The system is documentation-first and repository-local.

Main layers:

- `.aiassistant/project_context/` stores active runtime understanding.
- `.aiassistant/decisions/` stores accepted architectural and lifecycle rules.
- `.aiassistant/runbooks/` stores executable procedures.
- `.aiassistant/checklists/` stores validation criteria.
- `.aiassistant/feedback/` stores structured real-world input.
- `.aiassistant/roadmap/` stores release planning.
- `.aiassistant/specs/` stores design before implementation.
- `.aiassistant/prompts/` stores reusable operational prompts.
- `.aiassistant/rules/` stores repository and agent behavior rules.
- `.aiassistant/templates/` stores reusable SDK scaffolding.
- `.aiassistant/tools/` stores helper scripts.
- `project_knowledge/` is optional and only for business or operational process
  documentation when an SDK wraps a process-heavy domain.

## 3. SDK Development Model

The target SDK structure is expected to use:

- `src/` package layout;
- `pyproject.toml` as the installability contract;
- typed public APIs;
- a stable facade or top-level public entrypoint;
- separated transport, service, model, exception, and facade responsibilities
  when the SDK integrates with an external API;
- unit, functional, and integration tests;
- Sphinx-compatible documentation;
- GitHub Actions for CI, docs, PyPI publish, and GitHub release when applicable;
- tag-driven versioning when `setuptools_scm` is adopted.

## 4. Integrations

There are no runtime integrations in this template.

The template provides optional starter files for:

- GitHub Actions;
- PyPI publication;
- GitHub Releases;
- Sphinx documentation;
- Obsidian graph navigation.

## 5. Core Flows

### SDK Context Bootstrap

- Input: explicit SDK definition from the user.
- Processing: follow [[bootstrap-python-sdk-context]] and [[SDK_CONTEXT_TEMPLATE]].
- Output: `.aiassistant/project_context/CURRENT_CONTEXT.md` for the real SDK.

### SDK Repository Setup

- Input: package name, public API direction, supported Python versions, and
  integration scope.
- Processing: follow [[setup-python-sdk-repository]].
- Output: `src/`, `tests/`, `docs/`, `pyproject.toml`, and starter workflows.

### SDK Implementation

- Input: approved spec, feedback, or roadmap item.
- Processing: preserve public API compatibility, implement narrowly, update
  tests/docs/examples, and apply [[sdk-implementation-checklist]].
- Output: SDK change aligned with current context and decisions.

### SDK Release

- Input: release-ready changes.
- Processing: follow [[prepare-sdk-release]] and [[sdk-release-checklist]].
- Output: validated package, Git tag, PyPI publication, GitHub Release, and
  updated docs when applicable.

### Knowledge Graph

- Input: meaningful relationships between `.aiassistant` Markdown artifacts.
- Processing: follow [[WIKILINK_RULES]] and validate with [[validate-wikilinks]].
- Output: a navigable Obsidian-compatible graph.

## 6. Business Rules

- `CURRENT_CONTEXT.md` is the only active runtime context.
- Accepted decisions must be followed unless explicitly superseded.
- Public API changes require compatibility review.
- `pyproject.toml` must reflect direct runtime dependencies only.
- Release validation must include formatting, typing, tests, build, and package
  metadata checks.
- Docs and examples must be updated when public behavior changes.
- PyPI-facing README behavior must not regress after publication.
- Git tag and published package version must stay aligned when tag-driven
  versioning is used.
- Integration tests that mutate external systems must isolate owned test data
  and document cleanup behavior.

## 7. Architectural Decisions Summary

- [[0001-knowledge-graph-wikilink-policy]]: wikilinks are the relationship
  layer across governance artifacts.
- [[0002-python-sdk-lifecycle-policy]]: SDK development must preserve package,
  public API, testing, docs, and release discipline.
- [[0003-sdk-public-api-compatibility-policy]]: public imports and behavior are
  compatibility contracts.
- [[0004-sdk-release-publication-policy]]: release is tag-driven and validated
  before PyPI/GitHub publication when configured.
- [[0005-sdk-documentation-and-examples-policy]]: README, docs, examples, and
  Sphinx output are part of the SDK product.
- [[0006-process-knowledge-documentation-lifecycle]]: process knowledge evolves
  with business/process behavior when relevant.

## 8. Known Risks / Limitations

- This is a template, not an initialized SDK.
- The target SDK must still define its real package name, public API, supported
  Python versions, integrations, and release policy.
- Over-copying PipeBridge-specific details would create false constraints.
- Public API compatibility can be missed if specs and checklists are skipped.
- PyPI rendering can regress if README assets use local-only paths.

## 9. Current State

- A new standalone SDK-focused `.aiassistant` structure exists.
- The original generic project has not been overwritten.
- PipeBridge reference lessons have been generalized into SDK governance,
  runbooks, checklists, prompts, and templates.

## 10. Next Steps / Priorities

- Use this folder as the starting point for a new Python SDK repository.
- Bootstrap the real SDK context before implementation.
- Customize package metadata, supported Python versions, and workflow templates.
- Validate wikilinks after any documentation relationship changes.

## Rules

- This file is the only valid runtime context for this template.
- Do not use PipeBridge as active context for a future SDK.
- Treat PipeBridge only as a reference source already consolidated into this
  template.

