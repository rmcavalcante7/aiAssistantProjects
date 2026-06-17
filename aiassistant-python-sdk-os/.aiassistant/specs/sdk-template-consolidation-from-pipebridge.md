# SDK Template Consolidation From PipeBridge

## Status

Implemented in this template.

## Objective

Analyze the extracted PipeBridge `.aiassistant` reference and generalize the
useful SDK-development practices into this Python SDK operating system.

## Source Reference

The reference archive contained a local `.aiassistant` workspace for a Python
SDK originally built around Pipefy and later consolidated as PipeBridge.

It included:

- project context snapshots;
- feedback entries;
- roadmap;
- specs;
- playbooks;
- release prompt;
- local agent rules.

## Useful Patterns Retained

### Stable Facade

The reference protected a main public facade and domain namespaces.

Generalized rule:

- each SDK should explicitly identify its public entrypoint and exported
  domains;
- facade and top-level imports are compatibility contracts.

Related:

- [[0003-sdk-public-api-compatibility-policy]]
- [[sdk-public-api-compatibility-checklist]]

### Layered SDK Architecture

The reference separated:

- client/transport;
- services;
- models;
- exceptions;
- facade;
- workflow/policies where needed.

Generalized rule:

- use clear boundaries when they protect integration behavior, public contracts,
  or testability;
- avoid project-specific service names in this template.

Related:

- [[0002-python-sdk-lifecycle-policy]]
- [[rules/AGENTS|AGENTS rules]]

### Transport Configuration

The reference captured practical enterprise needs:

- timeout configuration;
- TLS verification control;
- custom CA bundle;
- retry for transient transport failures.

Generalized rule:

- API clients should model transport configuration explicitly;
- defaults must remain secure;
- retries must avoid auth and logical API errors unless explicitly designed.

### Public Escape Hatches

The reference used a conditional raw update path only after validating that
high-level behavior was insufficient.

Generalized rule:

- low-level escape hatches must be explicit, additive, documented, and tested;
- they must not weaken the safe high-level path.

### Tests By Scope

The reference separated:

- unit tests for internals;
- functional tests for public API without live network;
- integration tests for real external systems.

Generalized rule:

- SDKs should test public behavior separately from internals;
- destructive live tests require explicit flags and owned test data.

Related:

- [[validate-sdk-quality-gates]]
- [[sdk-implementation-checklist]]

### Release Flow

The reference used:

- `black --check`;
- `mypy`;
- `pytest`;
- `python -m build`;
- `twine check`;
- tag-driven publication;
- separate GitHub Actions for CI, docs, PyPI, and GitHub Release.

Generalized rule:

- release is a validated artifact flow, not just a Git tag.

Related:

- [[0004-sdk-release-publication-policy]]
- [[prepare-sdk-release]]
- [[sdk-release-checklist]]

### PyPI README Non-Regression

The reference captured important PyPI lessons:

- use the canonical README when intended;
- use public URLs for PyPI-visible assets;
- do not rely on local relative image paths for published rendering;
- verify README rendering after publication.

Generalized rule:

- README rendering is part of release validation.

Related:

- [[0005-sdk-documentation-and-examples-policy]]
- [[sdk-documentation-quality-checklist]]

### Sphinx Docs

The reference used Sphinx and documented a real issue with duplicate autodoc
entries.

Generalized rule:

- generated docs must build cleanly;
- internal modules may need `:no-index:` when also exported publicly.

Related:

- [[setup-sphinx-docs]]

## Patterns Not Copied As Universal

The following were intentionally not copied as active context:

- package name `pipebridge`;
- Pipefy-specific domains such as cards, pipes, phases, files, and connectors;
- Pipefy tenant IDs, card IDs, environment variable names, and live validation
  data;
- exact public methods such as `createSafely` or `moveSafely`;
- project-specific branding assets;
- old local context snapshot policy that created timestamped active context
  files.

These remain reference evidence only, not constraints for future SDKs.

## Consolidated Output

The lessons above were converted into:

- SDK lifecycle decisions;
- release and documentation policies;
- runbooks for setup, pyproject, Sphinx, quality gates, and release;
- checklists for implementation, public API, docs, and release;
- SDK-focused prompts;
- package, workflow, and documentation templates.

