# Knowledge Graph Wikilink Policy

## Status

Accepted

## Context

The repository is organized as a structured `.aiassistant` operating system for AI-assisted engineering. Its artifacts already have defined responsibilities: context describes current behavior, decisions explain why constraints exist, runbooks define execution, checklists define validation, and other directories support evolution.

The user wants to visualize relationships between these Markdown artifacts using Obsidian Graph View. This requires a consistent wikilink policy so links remain useful, stable, and aligned with repository governance.

## Decision

The repository will use Obsidian-compatible wikilinks as a lightweight relationship layer across existing `.aiassistant` Markdown artifacts.

Wikilinks must:

- connect artifacts that have a meaningful operational or architectural relationship;
- point to Markdown file stems by default, without `.md`;
- use explicit Obsidian paths only when file stems are duplicated;
- preserve each directory's existing responsibility;
- avoid creating a separate wiki or duplicate source of truth;
- remain useful even when Obsidian is not being used.

Obsidian is the primary visualization tool for the first phase. The preferred usage is to open `.aiassistant` itself as the Obsidian vault. A lightweight Python validator may be used to detect broken links and optionally export graph JSON. A custom HTML graph generator is deferred.

## Alternatives Considered

- Create a separate `wiki/` or `knowledge/` directory: rejected because it would encourage duplicated explanations and a parallel source of truth.
- Generate an HTML graph immediately: deferred because Obsidian already provides the first visualization layer and the immediate need is governance.
- Avoid wikilinks and rely only on normal Markdown links: rejected because Obsidian wikilinks provide direct graph compatibility with minimal syntax.

## Consequences

Benefits:

- The documentation structure becomes navigable as a graph.
- Relationships between context, decisions, runbooks, specs, checklists, feedback, roadmap, prompts, and rules become explicit.
- Obsidian can visualize the repository without additional dependencies.

Risks:

- Over-linking can make the graph noisy.
- Broken links can mislead readers and agents.
- Link rules must be followed consistently to avoid documentation drift.

Maintenance impact:

- New or changed `.aiassistant` Markdown artifacts should consider whether meaningful wikilinks are needed.
- The Python validator should remain dependency-free unless a future decision accepts a dependency.

## Related Files

- [[CURRENT_CONTEXT]]
- [[WIKILINK_RULES]]
- [[validate-wikilinks]]
- [[use-obsidian-knowledge-graph]]
- [[REPOSITORY_GUIDELINES]]
- [[AGENTS]]
