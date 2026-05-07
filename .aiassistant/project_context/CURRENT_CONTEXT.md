# Current Context

## 1. Project Overview

This repository defines an AI Repository Operating System for AI-assisted engineering.

Its purpose is to provide a reusable `.aiassistant` structure that makes an AI agent operate with explicit context, architectural decisions, repeatable runbooks, validation checklists, feedback, roadmap items, specs, prompts, templates, and repository rules.

The current evolution adds Obsidian-compatible wikilinks so the Markdown knowledge base can be navigated as a visual knowledge graph.

## 2. System Architecture

The system is documentation-first and repository-local.

Main layers:

- `.aiassistant/project_context/` stores the active runtime understanding.
- `.aiassistant/decisions/` stores accepted architectural constraints.
- `.aiassistant/runbooks/` stores executable procedures.
- `.aiassistant/checklists/` stores validation criteria.
- `.aiassistant/feedback/` stores structured real-world input.
- `.aiassistant/roadmap/` stores release-oriented planning.
- `.aiassistant/specs/` stores implementation design before coding.
- `.aiassistant/prompts/` stores reusable operational prompts.
- `.aiassistant/rules/` stores repository and agent behavior rules.
- `.aiassistant/tools/` stores repository-local support scripts.
- `.aiassistant/templates/` stores reusable starter artifacts.

The knowledge graph is a relationship layer over these existing Markdown artifacts. It must not create a parallel source of truth.

## 3. Integrations

There are no external runtime integrations in this repository.

Obsidian is an optional human-facing tool for visualizing Markdown wikilinks. The repository must remain useful without Obsidian.

## 4. Project Structure

Key directories:

- `.aiassistant/project_context/`: current system context and historical snapshots.
- `.aiassistant/decisions/`: accepted or proposed architectural decisions.
- `.aiassistant/runbooks/`: repeatable operational procedures.
- `.aiassistant/checklists/`: validation artifacts.
- `.aiassistant/feedback/`: structured improvement inputs.
- `.aiassistant/roadmap/`: planned delivery scope.
- `.aiassistant/specs/`: design documents for meaningful changes.
- `.aiassistant/prompts/`: reusable prompts for recurring AI workflows.
- `.aiassistant/rules/`: rules that govern repository and agent behavior.
- `.aiassistant/tools/`: executable support scripts for validation and derived outputs.
- `.aiassistant/templates/`: reusable scaffolding, not a source of truth.
- `.aiassistant/MAP.md`: Obsidian vault map for navigating major artifact relationships.

## 5. Core Flows

### Context bootstrap flow

- Input: explicit user-provided project definition.
- Processing: follow [[bootstrap-project-context]] and [[CONTEXT_TEMPLATE]].
- Output: `.aiassistant/project_context/CURRENT_CONTEXT.md`.

### Repository governance flow

- Input: change request or project evolution.
- Processing: evaluate whether the change affects context, decisions, runbooks, checklists, feedback, roadmap, specs, prompts, or rules.
- Output: updated `.aiassistant` artifacts aligned with [[REPOSITORY_GUIDELINES]].

### Knowledge graph flow

- Input: meaningful relationships between `.aiassistant` Markdown artifacts.
- Processing: navigate from [[MAP]], create Obsidian-compatible wikilinks according to [[WIKILINK_RULES]], validate them with [[validate-wikilinks]], and inspect them with [[use-obsidian-knowledge-graph]].
- Output: validated graph relationships visible in Obsidian and optionally exportable as JSON.

### Legacy migration flow

- Input: an older project that already uses `.aiassistant`.
- Processing: follow [[migrate-legacy-aiassistant-to-knowledge-graph]] without overwriting active project context.
- Output: migrated `.aiassistant` structure with wikilink policy, graph map, Obsidian workflow, and validation tooling.

## 6. Business Rules

- `CURRENT_CONTEXT.md` is the only active runtime context.
- Historical context files are not active context.
- Accepted decisions must be followed unless explicitly superseded.
- Runbooks define how repeatable procedures are executed.
- Checklists define what must be validated.
- Templates accelerate creation but are not a source of truth.
- Wikilinks must connect existing responsibility-specific artifacts and must not create duplicated documentation.
- Automation architecture must avoid speculative abstraction while preserving semantic stages, external system boundaries, and testable business rules.

## 7. Architectural Decisions Summary

- [[0001-knowledge-graph-wikilink-policy]]: the repository uses Obsidian-compatible wikilinks as a lightweight relationship layer across existing `.aiassistant` Markdown artifacts.
- [[0002-automation-simplicity-and-stage-boundaries]]: automation code must balance simplicity with clear process stages, external system boundaries, and testable business rules.

## 8. Known Risks / Limitations

- Excessive wikilinking can make the graph noisy and reduce its operational value.
- Broken wikilinks can create misleading relationships.
- Obsidian may not index `.aiassistant` when the project root is opened as a vault; opening `.aiassistant` itself as the vault is the preferred first-phase usage.
- Repository-root files are outside the `.aiassistant` Obsidian vault and do not appear as graph nodes unless the repository root is opened as the vault and dot-folder indexing is available.

## 9. Current State

- The base `.aiassistant` repository structure exists.
- The repository is a starter operating system, not a populated application project.
- Active context has been initialized for the repository itself.
- The knowledge graph increment defines policy, usage rules, Obsidian inspection, and automated wikilink validation.
- A migration changelog and runbook now describe how older `.aiassistant` projects should adopt the graph structure.
- Engineering guidance now includes anti-overengineering rules and automation flow stage boundaries.

## 10. Next Steps / Priorities

- Continue adding wikilinks incrementally to existing `.aiassistant` artifacts where relationships are meaningful.
- Use the validation script before accepting new graph relationships.
- Keep Obsidian as the primary visual graph tool for the first phase.

## Rules

- This file is the only valid runtime context.
- Keep this file concise and aligned with reality.
- Do not duplicate full decision, runbook, checklist, or rule content here.
- Update this file when the repository behavior materially changes.
