# Process Knowledge Documentation Lifecycle

## Status

Accepted

## Context

The repository already defines how AI agents must work with context, decisions,
runbooks, checklists, specs, prompts, and wikilinks. It also defines that
automation code must preserve business behavior, expose meaningful process
stages, and keep business rules testable when possible.

Development work can change more than code. It can change how a process works,
which business rule is applied, which external system is involved, which input
or output contract is expected, or how operational failures must be handled.
When those changes are only captured in source code, agents and humans lose the
process-level map needed for onboarding, debugging, validation, and safe
evolution.

The user wants process and business-rule documentation to evolve together with
the development work performed by agents.

## Decision

Business-rule and process documentation is part of the development lifecycle.

When an agent changes behavior that affects a business process, business rule,
automation stage, external system interaction, input/output contract, evidence
requirement, error handling rule, status transition, or operational boundary,
the agent must update the related process knowledge documentation in the same
development flow.

The recommended project-level documentation root is `project_knowledge/`.
That directory is for operational and business-process knowledge, not for AI
repository governance.

The `.aiassistant` directory remains the source of truth for AI governance:
context, decisions, rules, runbooks, checklists, specs, prompts, and templates.
Project process documentation must not replace `.aiassistant` context or
accepted decisions.

Markdown remains the source of truth for process knowledge. Obsidian Canvas may
be used as a curated visual map, but it must not become the only place where a
business rule or process contract is documented.

Agents must follow [[PROCESS_KNOWLEDGE_RULES]] and validate process knowledge
with [[process-documentation-quality-checklist]] when the change affects process
or business behavior.

## Alternatives Considered

- Keep business-rule documentation optional: rejected because documentation
  drift is likely when agents evolve automations or apps without updating the
  process map.
- Store process knowledge inside `.aiassistant`: rejected because `.aiassistant`
  is repository governance, while process knowledge belongs to the project being
  built.
- Use Obsidian Canvas as the source of truth: rejected because canvas files are
  best used as visual navigation, while Markdown is easier to review, diff,
  validate, and link.
- Require process documentation for every small code change: rejected because
  purely internal refactors that do not change behavior or contracts should not
  create documentation noise.

## Consequences

Benefits:

- Business rules evolve visibly with implementation.
- Onboarding can start from a process map instead of scattered code.
- External system boundaries and contracts become easier to inspect.
- Agents have clearer context before changing process behavior.
- Wikilinks and Obsidian can show how stages, rules, systems, risks, and
  contracts relate.

Risks:

- Agents may over-document implementation details instead of business behavior.
- Process notes can become stale if the lifecycle rule is ignored.
- The repository must distinguish clearly between `.aiassistant` governance and
  project-level process knowledge.

Maintenance impact:

- Add process knowledge rules to the mandatory agent reading path.
- Add templates for process maps, process indexes, business rules, and system
  notes.
- Add a runbook and checklist for updating process knowledge during
  development.
- Extend wikilink validation so project-level process vaults using relative
  links can be checked without external dependencies.

## Related Files

- [[CURRENT_CONTEXT]]
- [[PROCESS_KNOWLEDGE_RULES]]
- [[REPOSITORY_GUIDELINES]]
- [[WIKILINK_RULES]]
- [[update-process-knowledge-documentation]]
- [[process-documentation-quality-checklist]]
- [[process-knowledge-map-template]]
- [[process-index-template]]
- [[business-rule-template]]
- [[system-note-template]]
- [[0002-automation-simplicity-and-stage-boundaries]]
