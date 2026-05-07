# Automation Simplicity And Stage Boundaries

## Status

Accepted

## Context

The repository guides AI-assisted engineering across automation projects, internal systems, integrations, and reusable Python packages.

The previous engineering guidance encouraged production-grade structure and SDK-style thinking. That is useful for quality, but it can lead the AI to overengineer automations by adding speculative layers, factories, interfaces, wrappers, or generic SDK extension points before there is a concrete design need.

At the same time, automations must not collapse into monolithic scripts. Business rules, external system boundaries, operational stages, and error reporting need enough structure to remain testable, observable, and maintainable.

## Decision

The AI must optimize for the simplest architecture that safely preserves business behavior, operational clarity, observability, and testability.

Automation code must use a semantic orchestration flow. The main entrypoint should coordinate meaningful process stages rather than mix extraction, transformation, integration, business rules, logging, and output generation in one procedural block.

Stages must be split when they cross different external systems. Stages should also be split when they represent different business activities, isolate critical business rules, isolate side effects, improve error reporting, or reduce meaningful complexity.

Stages may be intermediate rather than overly granular when operations are naturally cohesive and easier to understand as a single process block.

Abstractions are allowed when they solve concrete design pressure, such as:

- external integration boundaries;
- side-effect isolation;
- important domain contracts;
- critical business-rule testability;
- confirmed variation;
- meaningful duplication;
- separation between runtime wiring and business behavior;
- requirements from accepted context, specs, or decisions.

Abstractions must not be added only for hypothetical future reuse, generic architectural symmetry, or framework-style completeness.

When the explicit project goal is an SDK, framework, or reusable library, abstraction is allowed and expected. Even then, every abstraction must be justified by a concrete API contract, reuse scenario, extension point, integration boundary, or testability need.

## Alternatives Considered

- Keep SDK-style guidance as the default for every project: rejected because automations can become unnecessarily generic and harder to operate.
- Ban abstractions unless duplication already exists: rejected because valid design pressure can exist before duplication, especially around external systems, critical business rules, side effects, and domain contracts.
- Require every automation step to be granularly separated: rejected because it can create excessive fragmentation and make the main flow harder to understand.

## Consequences

Benefits:

- Reduces speculative architecture in automation projects.
- Keeps automations testable and observable without forcing framework-style structure.
- Preserves the ability to build SDKs and reusable libraries when the project explicitly requires it.
- Makes external system boundaries and business-rule boundaries explicit.

Risks:

- The AI must exercise judgment when deciding whether a process stage is cohesive or should be split.
- Under-structuring remains possible if semantic stages are ignored.
- Over-structuring remains possible if abstractions are justified weakly.

Maintenance impact:

- `.aiassistant/rules/AGENTS.md` must include anti-overengineering and automation flow design rules.
- Future specs and decisions should distinguish automation structure from SDK/library structure.
- Code review should challenge both monolithic automation scripts and speculative abstractions.

## Related Files

- [[CURRENT_CONTEXT]]
- [[rules/AGENTS|AGENTS rules]]
- [[REPOSITORY_GUIDELINES]]
- [[WIKILINK_RULES]]
- [[MAP]]
