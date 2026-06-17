# SDK Implementation Checklist

## Objective

Validate SDK implementation work before delivery.

Use this checklist for feature work, bug fixes, integration changes, public API
changes, packaging changes, and documentation-impacting changes.

## Context And Scope

- [ ] Active context was read.
- [ ] Relevant accepted decisions were read.
- [ ] Relevant runbooks/checklists were identified.
- [ ] Relevant spec or roadmap item was read or created.
- [ ] The change scope is clear.
- [ ] Unrelated refactors were avoided.

## Public API

- [ ] Public API impact was identified.
- [ ] Backward compatibility impact was identified.
- [ ] Additive vs breaking nature was stated.
- [ ] Public imports remain stable unless explicitly changed.
- [ ] Public examples still use valid APIs.
- [ ] [[sdk-public-api-compatibility-checklist]] was applied when needed.

## Code Quality

- [ ] Code is typed.
- [ ] Public behavior has Sphinx-compatible docstrings.
- [ ] Exceptions preserve causes where applicable.
- [ ] No broad exception handling hides root causes.
- [ ] New abstractions solve a concrete SDK design pressure.
- [ ] Runtime dependencies were not added without direct need.

## Integration Behavior

- [ ] Transport/auth/timeout/TLS/retry behavior was considered when relevant.
- [ ] External API responses are validated defensively.
- [ ] Write operations document retry/idempotency risk when relevant.
- [ ] Secrets are not logged or committed.

## Tests And Docs

- [ ] Unit tests cover important internal behavior.
- [ ] Functional tests cover public behavior changes.
- [ ] Integration tests were added or updated when live behavior changed.
- [ ] Destructive tests use owned data and explicit flags.
- [ ] README/docs/examples were updated when public behavior changed.
- [ ] Changelog/release note impact was considered.

## Validation

- [ ] Formatting was checked.
- [ ] Typing was checked.
- [ ] Unit and functional tests were run or skipped with reason.
- [ ] Build/package validation was run when packaging changed.
- [ ] Docs build was run when docs changed.
- [ ] Residual risk is documented.

## Related Files

- [[0002-python-sdk-lifecycle-policy]]
- [[0003-sdk-public-api-compatibility-policy]]
- [[validate-sdk-quality-gates]]

