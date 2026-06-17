# AI Repository Operating System For Python SDKs

This repository is a shareable AI-assisted engineering operating system focused
on Python SDK and library development.

It is derived from two sources:

- the current generic `.aiassistant` governance system;
- lessons learned from a real Pipefy SDK project reference.

The goal is to make AI-assisted SDK development safer, more reproducible, and
less dependent on chat history.

## What This Is

This is not an SDK implementation.

It is a repository template for building SDKs with:

- explicit runtime context;
- accepted architectural decisions;
- stable public API discipline;
- repeatable setup and release runbooks;
- quality gates for `black`, `mypy`, tests, build, docs, and packaging;
- PyPI publication rules;
- Sphinx documentation guidance;
- Obsidian-compatible wikilinks for governance navigation.

## Intended Use

Use this template when starting or evolving a Python SDK, client library, or
internal package that will expose a public API to other developers.

It is especially useful for SDKs that wrap:

- HTTP APIs;
- GraphQL APIs;
- SaaS platforms;
- integration systems;
- internal developer platforms.

## Core Ideas

- `CURRENT_CONTEXT.md` is the single active runtime context.
- Decisions define constraints that must not be changed casually.
- SDK public API changes require explicit compatibility review.
- `pyproject.toml` is the installability contract.
- Git tags drive package versions when `setuptools_scm` is adopted.
- CI must validate formatting, typing, and tests before release.
- PyPI must render the intended README, including public assets and badges.
- Documentation and examples are part of the SDK product.

## Main Directories

- `.aiassistant/project_context/`: active context for this SDK template.
- `.aiassistant/decisions/`: accepted governance and SDK lifecycle decisions.
- `.aiassistant/runbooks/`: executable procedures.
- `.aiassistant/checklists/`: validation criteria.
- `.aiassistant/rules/`: mandatory agent and repository rules.
- `.aiassistant/templates/`: starter files for SDK projects.
- `.aiassistant/tools/`: helper scripts, including wikilink validation.

## First Steps In A New SDK

1. Copy this repository into the new SDK workspace.
2. Read `AGENTS.md`.
3. Follow `.aiassistant/runbooks/bootstrap-python-sdk-context.md`.
4. Create the real SDK `CURRENT_CONTEXT.md`.
5. Use `.aiassistant/templates/sdk-project/pyproject-template.toml` as the
   starting point for packaging.
6. Use `.aiassistant/templates/github-workflows/` to configure CI, docs,
   PyPI publication, and GitHub releases.
7. Validate with `.aiassistant/runbooks/validate-sdk-quality-gates.md`.

## Reference Consolidation

The Pipefy/PipeBridge reference contributed these reusable lessons:

- keep a stable facade as the primary public entrypoint;
- separate transport, services, models, exceptions, and facade responsibilities;
- treat public API compatibility as a release gate;
- split tests into unit, functional, and integration scopes;
- use `black --check`, `mypy`, and `pytest` as release gates;
- use Sphinx for generated API docs;
- publish by Git tag;
- validate built artifacts before release;
- ensure the PyPI README renders the full product-facing README;
- document non-transactional and destructive integration behavior explicitly.

See `.aiassistant/specs/sdk-template-consolidation-from-pipebridge.md` for the
full consolidation notes.

