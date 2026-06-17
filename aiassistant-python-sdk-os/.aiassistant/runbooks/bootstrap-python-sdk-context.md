# Bootstrap Python SDK Context

## Objective

Create the first active `CURRENT_CONTEXT.md` for a real Python SDK project.

This runbook prevents agents from inventing package identity, public API,
integrations, tests, documentation, or release behavior.

## When To Use

Use when:

- starting a new SDK from this template;
- `.aiassistant/project_context/CURRENT_CONTEXT.md` is missing;
- the user wants to initialize project context.

Do not use this to update an existing context.

## Preconditions

- The user has agreed to initialize SDK context.
- Enough explicit information exists to describe the SDK.

If information is missing, ask before writing.

## Minimum Inputs

Collect:

- SDK purpose;
- package name and import name;
- target users;
- public entrypoint direction;
- wrapped API or system;
- authentication model;
- supported Python versions;
- release target such as PyPI or internal registry;
- documentation target;
- known compatibility constraints.

## Optional Inputs

Collect when known:

- expected facade/client name;
- public domain namespaces;
- initial runtime dependencies;
- expected CI provider;
- versioning strategy;
- integration-test environment variables;
- destructive/live test constraints;
- branding or README asset requirements.

## Steps

1. Confirm whether `CURRENT_CONTEXT.md` exists.
2. If it exists, stop this runbook and update the existing file instead.
3. Classify the SDK:
   - public PyPI package;
   - private internal package;
   - API client;
   - integration SDK;
   - domain library.
4. Gather the minimum viable context.
5. Identify unknowns that block implementation or release.
6. Draft the context using [[SDK_CONTEXT_TEMPLATE]].
7. Remove all placeholders.
8. Validate that the context does not copy reference-project facts as current
   facts.
9. Identify follow-up decisions, specs, runbooks, or checklists.
10. Validate wikilinks if the context includes new links.

## Validation

- The active context exists.
- It describes the real SDK, not this template.
- Package identity and public API direction are clear.
- Unknowns are marked as open questions, not assumptions.
- Release and documentation intent are clear enough to guide setup.
- No historical or reference context is treated as current reality.

## Outputs

- `.aiassistant/project_context/CURRENT_CONTEXT.md`

Optional outputs:

- first roadmap;
- first spec;
- package/release decision;
- process knowledge map when the SDK wraps process-heavy behavior.

## Failure Scenarios

### Package Name Is Unknown

Do not create final context. Ask for package/import naming direction or record
the project as not ready for implementation.

### Public API Is Unknown

Create only high-level context if the SDK is exploratory. Do not invent facade
names, method names, or domain namespaces.

### Integration Scope Is Unknown

Ask whether the SDK wraps an external API, internal system, local domain logic,
or a combination.

### Release Strategy Is Unknown

Record release strategy as an open question and avoid creating publication
workflows as active behavior.

## Related Files

- [[SDK_CONTEXT_TEMPLATE]]
- [[CONTEXT_RULES]]
- [[setup-python-sdk-repository]]

