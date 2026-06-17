# Process Knowledge Documentation Lifecycle

## Status

Accepted

## Context

Most SDK changes concern developer-facing APIs. Some SDKs, however, wrap
business-heavy systems where the library exposes process stages, status
transitions, evidence rules, external-system contracts, or operational behavior.

When that happens, process knowledge must not live only in source code.

## Decision

Project-level process knowledge is optional, but mandatory when SDK development
changes business or operational behavior that needs to be understood outside
code.

Use `project_knowledge/` for:

- business rules;
- process stages;
- external system responsibilities;
- contracts;
- operational risks;
- evidence or audit requirements.

Do not use `project_knowledge/` as a replacement for `.aiassistant` governance.

Markdown remains the source of truth. Obsidian Canvas can be used only as visual
navigation.

## Alternatives Considered

- Store process knowledge inside `.aiassistant`: rejected because `.aiassistant`
  governs agents and repository evolution.
- Make process knowledge mandatory for every SDK: rejected because many SDKs
  only expose technical API contracts.
- Treat process knowledge as optional notes: rejected when behavior changes have
  operational impact.

## Consequences

Benefits:

- process-heavy SDKs remain explainable;
- agents can avoid changing business behavior blindly.

Risks:

- over-documentation can slow technical-only SDKs;
- process notes can drift if not maintained.

## Related Files

- [[PROCESS_KNOWLEDGE_RULES]]
- [[update-process-knowledge-documentation]]
- [[process-documentation-quality-checklist]]

