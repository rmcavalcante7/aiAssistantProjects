# Knowledge Graph Wikilink Policy

## Status

Accepted

## Context

This SDK template uses `.aiassistant` governance artifacts for context,
decisions, runbooks, checklists, feedback, roadmap, specs, prompts, rules,
templates, and tools.

The documentation should be navigable by humans and agents without creating a
parallel wiki.

## Decision

Use Obsidian-compatible wikilinks as a lightweight relationship layer across
existing `.aiassistant` Markdown artifacts.

Wikilinks must:

- connect meaningful governance, execution, validation, or onboarding
  relationships;
- point to Markdown file stems by default when unique;
- use explicit Obsidian paths when stems are duplicated;
- avoid decorative links;
- avoid creating a second source of truth.

## Alternatives Considered

- Separate wiki directory: rejected because it creates duplicate sources.
- Plain Markdown links only: rejected because Obsidian graph support is useful.
- Custom graph generator first: deferred because validation and Obsidian are
  sufficient for the first layer.

## Consequences

Benefits:

- relationships become visible;
- governance artifacts are easier to navigate;
- validators can catch broken links.

Risks:

- over-linking can make the graph noisy;
- broken links can mislead agents.

## Related Files

- [[CURRENT_CONTEXT]]
- [[WIKILINK_RULES]]
- [[validate-wikilinks]]
- [[use-obsidian-knowledge-graph]]

