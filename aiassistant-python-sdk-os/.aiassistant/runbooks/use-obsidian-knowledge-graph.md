# Use Obsidian Knowledge Graph

## Objective

Inspect `.aiassistant` governance relationships in Obsidian.

## When To Use

Use when reviewing repository structure, onboarding, or validating graph quality.

## Preconditions

- Obsidian is installed.
- `.aiassistant` exists.
- Wikilinks follow [[WIKILINK_RULES]].

## Steps

1. Open Obsidian.
2. Choose `Open folder as vault`.
3. Select `.aiassistant`, not necessarily the repository root.
4. Open Graph View.
5. Inspect central artifacts:
   - [[MAP]];
   - [[CURRENT_CONTEXT]];
   - [[REPOSITORY_GUIDELINES]];
   - [[0002-python-sdk-lifecycle-policy]];
   - [[prepare-sdk-release]].
6. Remove noisy or decorative links.

## Validation

- Important governance artifacts are connected.
- No accepted artifact depends on broken links.
- The graph explains structure instead of duplicating content.

