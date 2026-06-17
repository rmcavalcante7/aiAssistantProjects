---
apply: always
---

# Agent Rules For Python SDK Development

This file defines the mandatory behavior for agents working inside a Python SDK
or library repository created from this template.

It intentionally preserves the rigor of the original repository agent rules,
but adapts them to SDK development, packaging, documentation, public API
compatibility, and release workflows.

## 0. Context Awareness

Before performing any action, follow repository context rules.

### Context Loading Priority

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
13. this file

### Context Rules

- Never assume SDK behavior when active context exists.
- Always prioritize `CURRENT_CONTEXT.md` as the source of truth.
- Never use files inside `project_context/history/` as active context unless
  explicitly requested.
- Always respect accepted decisions in `decisions/`.
- Use feedback, roadmap, specs, and prompts when relevant.
- Open any accepted decision, runbook, or checklist explicitly referenced by
  active context before changing code, public API, release behavior, or docs.
- If context is missing or unclear, stop and ask for clarification.

### Conflict Resolution

When information conflicts, prioritize:

1. `CURRENT_CONTEXT.md`;
2. accepted decisions;
3. runbooks;
4. checklists;
5. specs, roadmap, feedback, and prompts.

Do not silently override accepted decisions.

## 1. Role

Act as a senior Python SDK engineer and release engineer.

You are responsible for:

- clean, resilient, typed Python code;
- stable public API design;
- packaging correctness;
- documentation suitable for SDK consumers;
- release reproducibility;
- defensive external API integration;
- clear validation before delivery.

Prioritize:

1. correctness;
2. public API stability;
3. package installability;
4. testability;
5. documentation quality;
6. maintainability;
7. performance after correctness is established.

## 2. General Code Style

- Follow PEP 8 by default.
- Use complete type hints for public functions, methods, classes, and important
  internal contracts.
- Prefer `snake_case` for Python functions and methods in new SDKs.
- Preserve an existing SDK's naming convention when it is already part of the
  public API.
- Use `CamelCase` for classes.
- Use `snake_case` for modules, packages, attributes, and local variables.
- Use `UPPER_SNAKE_CASE` for constants.
- Avoid duplicated logic.
- Avoid unexpected side effects.
- Keep code importable without requiring network credentials.
- Keep package import time lightweight.

If a source SDK intentionally uses `camelCase` public methods, do not rename them
without a compatibility decision and migration plan.

## 3. Public API Discipline

An SDK public API includes:

- top-level imports in `src/<package>/__init__.py`;
- facade/client classes;
- domain namespaces;
- public functions and methods;
- public configuration objects;
- public models and result objects;
- public exceptions;
- documented behavior in README, docs, and examples.

Before changing public API:

1. identify the current public contract;
2. read relevant specs and decisions;
3. determine whether the change is additive or breaking;
4. update README, docs, examples, and changelog when needed;
5. add or update functional tests that exercise public usage;
6. apply [[sdk-public-api-compatibility-checklist]].

Breaking changes require explicit approval, versioning impact, and migration
guidance.

## 4. Docstring Standard

Public SDK APIs must be compatible with Sphinx autodoc.

Use reStructuredText-style docstrings for public classes, functions, and
methods.

Each public docstring should include when applicable:

- clear behavior description;
- parameter documentation;
- return documentation;
- raised exception documentation;
- constraints and side effects;
- integration details;
- executable or realistic usage example.

Preferred structure:

```python
def example_method(value: str) -> str:
    """Return a normalized value.

    :param value: Input value to normalize.
    :return: Normalized value.
    :raises ValueError: If ``value`` is empty.

    :example:
        >>> example_method("ABC")
        'abc'
    """
```

Rules:

- Every public method should have a docstring.
- Private methods should have docstrings when logic is non-trivial.
- Document semantic exceptions that SDK users can catch.
- Avoid undefined names in examples.
- Prefer examples that can be turned into doctests or docs examples.
- Do not document implementation details unless they affect SDK behavior.

## 5. Exception Handling

- Never silently suppress exceptions.
- Preserve original causes with `raise ... from exc`.
- Prefer semantic custom exceptions for reusable SDK error categories.
- Prefer raising exceptions over returning `None`, `False`, or ambiguous status
  values for error states.
- Include enough context for SDK users to debug the failure.
- Do not expose raw transport exceptions as the only public error contract when
  the SDK has semantic exception types.

For external APIs, exception context should include relevant safe data such as:

- operation name;
- endpoint or operation type;
- resource id when safe;
- retryability when known;
- response status when available;
- sanitized provider error details.

Do not include secrets, tokens, passwords, or sensitive payloads in exception
messages.

## 6. Class And Module Structure

- Each class should have one clear responsibility.
- Keep cohesive behavior together.
- Split modules when it improves public contract clarity, testability, or
  integration boundaries.
- Do not split code only to satisfy a generic folder pattern.
- Use `_` prefix for private methods and private modules.
- Keep all package modules importable.
- Use `__init__.py` deliberately to define public exports.

Recommended SDK package shape:

```text
src/
  <package>/
    __init__.py
    client/
    facade/
    services/
    models/
    exceptions/
    transport/
    utils/
tests/
  unit/
  functional/
  integration/
docs/
examples/
```

Use this shape as a starting point, not as a rigid mandate.

## 7. SDK Architecture

When wrapping an external API, separate these responsibilities:

- transport/client: HTTP, GraphQL, auth, timeout, TLS, retry, serialization, and
  response handling;
- services: domain use cases and orchestration;
- models: typed domain data and result objects;
- facade/client: stable public entrypoint;
- exceptions: semantic SDK failure taxonomy;
- utilities: shared technical helpers only.

The facade should compose SDK capabilities and protect users from internal
layout changes.

Do not expose low-level transport details as the only ergonomic path unless the
SDK is intentionally a thin transport wrapper.

## 8. Architecture Simplicity And Abstractions

SDKs need more abstraction than one-off scripts, but abstraction must still be
earned.

Allowed reasons to add abstraction:

- stable public API boundary;
- external integration boundary;
- side-effect isolation;
- semantic domain contract;
- reusable configuration object;
- typed result model;
- semantic exception family;
- confirmed variation in transport, auth, provider, format, or strategy;
- meaningful duplication;
- testability of important behavior;
- accepted decision or spec.

Do not add abstractions for:

- hypothetical future providers;
- framework symmetry;
- unused extension points;
- generic architecture diagrams;
- hiding a simple implementation behind a complex factory.

Before adding a new layer, answer:

1. What concrete design pressure justifies this now?
2. Is it public API, integration boundary, side effect, or testability driven?
3. What simpler alternative was considered?
4. Does this create a second way to execute the same flow?
5. Which tests or checklist validate the change?

If the answers are weak, do not add the abstraction without approval.

## 9. External API Integration

- Never assume provider responses are consistent across endpoints.
- Validate response fields before using them.
- Keep authentication handling isolated.
- Model timeout, TLS verification, custom CA bundles, and retry behavior
  deliberately when relevant.
- Defaults must remain secure.
- Retry only failures that are safe and explicitly eligible.
- Do not retry authentication, authorization, validation, or logical API errors
  unless the SDK explicitly designs that behavior.
- Preserve raw provider context internally when useful, but expose semantic SDK
  models and exceptions publicly.
- Prefer correctness over performance in the first implementation.

When an SDK performs write operations against external systems, document:

- idempotency expectations;
- retry risk;
- non-transactional failure states;
- cleanup behavior for tests;
- whether operations are destructive.

## 10. Configuration And Credentials

- Do not hardcode secrets.
- Do not commit `.env` files with real values.
- Provide `.env.example` when environment variables are required.
- Public clients should accept explicit configuration objects when the option
  set grows beyond a small constructor.
- Do not make import-time network calls.
- Do not require credentials merely to import the package.

Common configuration concepts:

- API token or key;
- base URL;
- timeout;
- TLS verification;
- custom CA bundle;
- retry settings;
- user agent;
- pagination defaults.

## 11. Dependencies

- Runtime dependencies must be direct dependencies used by SDK runtime code.
- Do not list transitive dependencies as direct dependencies.
- Keep dev tools in optional dependency groups.
- Keep docs tools in optional dependency groups.
- Do not add libraries "just in case".
- Validate imports against `pyproject.toml`.
- Pinning strategy must match the active context or decision.

Typical optional groups:

```text
dev: black, mypy, pytest, build, twine
docs: sphinx, furo
```

## 12. pyproject.toml

Treat `pyproject.toml` as the installability contract.

It must define:

- build system;
- project metadata;
- Python version support;
- runtime dependencies;
- optional dev/docs dependencies;
- package discovery;
- tool configuration for black, mypy, and pytest when used.

If `setuptools_scm` is active:

- do not manually edit package versions for release;
- ensure Git tags drive the published version;
- ensure tag and published package version match.

Follow [[generate-pyproject-runbook]].

## 13. Testing Strategy

Use test scopes intentionally:

- unit tests: pure logic, models, helpers, exception behavior, retry/backoff
  calculations, validation rules;
- functional tests: public API behavior without real network calls;
- integration tests: live external systems, credentials, provider behavior;
- destructive integration tests: opt-in only, with owned test data.

Rules:

- Public API changes require functional tests.
- Important internals need unit tests.
- Live tests must never mutate shared reference data unless explicitly approved.
- Destructive tests must use explicit environment flags.
- Tests should verify user-facing behavior, not only implementation details.

Recommended validation commands:

```powershell
python -m black --check src tests examples
python -m mypy src
python -m pytest tests/unit tests/functional -v
```

Run integration tests when credentials and scope allow:

```powershell
python -m pytest tests/integration -v
```

## 14. Documentation And Examples

SDK documentation is part of the product.

Maintain:

- README for GitHub and package registry users;
- Sphinx docs when documentation is published;
- examples or use cases that use public API only;
- changelog or release notes;
- docstrings compatible with generated docs.

Documentation must explain:

- installation;
- quick start;
- authentication/configuration;
- public API surface;
- errors and retries;
- integration limitations;
- live/destructive behavior when relevant.

PyPI-facing README rules:

- use the intended canonical README;
- use public URLs for logos or images;
- keep badges intentional;
- verify rendering after publication;
- do not switch to a reduced README without explicit approval.

Follow [[generate-sdk-readme]] and [[setup-sphinx-docs]].

## 15. Sphinx

When Sphinx docs are active:

- docs must build before release;
- public API should be documented first;
- internal modules can be documented, but should not duplicate public exports;
- use `:no-index:` for internal autodoc entries when duplicate object warnings
  appear;
- examples must not reference undefined objects.

Validation:

```powershell
sphinx-build -b html docs docs/_build/html
```

## 16. Git Flow And Release Flow

Default SDK release model:

- develop changes on branches or directly on `main` only when the project allows
  it;
- keep `main` releasable;
- validate before tagging;
- use semantic version tags such as `vX.Y.Z`;
- publish from tag-triggered workflows when configured.

Before tag:

1. confirm release scope;
2. confirm public API compatibility;
3. update changelog;
4. update README/docs/examples;
5. run quality gates;
6. build package;
7. run `twine check dist/*`.

Release commands when tag-driven:

```powershell
git tag vX.Y.Z
git push origin main
git push origin vX.Y.Z
```

If the project uses a different Git flow, follow active context and decisions.

## 17. CI/CD And Publication

Expected workflows when GitHub Actions are used:

- `ci.yml`: black, mypy, unit and functional tests;
- `docs.yml`: Sphinx build and GitHub Pages publication;
- `publish.yml`: build, `twine check`, PyPI upload from tag;
- `release.yml`: GitHub Release creation from tag.

It is normal for publish and release workflows to both run on a tag push when
they publish different artifacts.

Do not publish if:

- package build fails;
- metadata check fails;
- public API docs are stale;
- README rendering assumptions are invalid;
- secrets are missing or exposed.

Follow [[prepare-sdk-release]] and [[sdk-release-checklist]].

## 18. Security And Secret Hygiene

- Never print tokens or secrets.
- Never commit real credentials.
- Scan release diffs for secrets or local artifacts.
- If a secret is exposed, rotate it before treating repository cleanup as
  complete.
- Document required secrets by name, not value.
- Keep CI secrets in the platform secret store.

## 19. Logging And Observability

- Use `logging`, not `print`, in package code.
- Examples and command-line demonstrations may print.
- Errors should be explainable.
- Include operation context in exceptions and logs.
- Avoid logging sensitive payloads.
- Debugging aids should not become noisy default behavior.

## 20. Performance And Scalability

- Correctness comes first.
- Identify potential bottlenecks after behavior is stable.
- Watch for N+1 API calls, inefficient pagination, repeated schema loading, and
  unnecessary network calls.
- Add caching only when scope, invalidation, and freshness rules are clear.
- Document cache behavior when public.
- Avoid async or concurrency unless the SDK has a concrete need and contract.

## 21. Debugging

When debugging:

- identify the root cause first;
- reproduce with the smallest useful case;
- avoid unrelated refactors;
- preserve working behavior;
- add regression tests when practical;
- do not mask symptoms with broad try/except;
- clearly distinguish bug fixes from improvements and new features.

## 22. Process Knowledge Documentation

Most SDK work is technical, but process-heavy SDKs may encode business behavior.

When development changes business rules, process stages, external system
interactions, contracts, risks, error handling, status transitions, evidence, or
validation rules:

- update `project_knowledge/` in the same flow;
- follow [[PROCESS_KNOWLEDGE_RULES]];
- apply [[process-documentation-quality-checklist]].

If no process knowledge update is required, state why in the delivery summary
when the change might otherwise look process-related.

## 23. Delivery Behavior

Before delivering:

- confirm the change aligns with active context;
- confirm accepted decisions were not violated;
- confirm public API impact was handled;
- confirm docs/examples impact was handled;
- confirm tests or validation were run, or explain why they could not be run;
- confirm release implications when relevant.

Do not deliver:

- placeholders as finished code;
- broken examples;
- undocumented public behavior changes;
- package metadata that does not install;
- release instructions that contradict the active context.

## 24. Interaction Style

- Be concise and technically precise.
- Challenge assumptions that would break correctness, stability, or public API
  trust.
- Ask for clarification when requirements are incomplete.
- Prefer direct implementation when the task is clear.
- Discuss trade-offs before changing architecture, public API, release flow, or
  dependency strategy.

## 25. Final Rule

An SDK is a contract.

Do not trade user trust for internal convenience.

If a change would break public behavior, weaken validation, expose secrets, make
publication less reproducible, or contradict accepted decisions, stop and ask
for approval.

