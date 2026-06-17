---
apply: always
---

# Wikilink Rules

This file defines how Obsidian-compatible wikilinks must be used inside
`.aiassistant` Markdown artifacts.

## Purpose

Wikilinks connect existing governance artifacts into a navigable graph.

They must not create a separate wiki or duplicate source of truth.

The repository must remain useful without Obsidian.

## Link Format

Use file stems when the target is unique:

```md
[[CURRENT_CONTEXT]]
[[prepare-sdk-release]]
```

Use aliases when the visible label needs to be clearer:

```md
[[0004-sdk-release-publication-policy|release publication policy]]
```

Use explicit Obsidian paths when stems are duplicated:

```md
[[rules/AGENTS|AGENTS rules]]
[[runbooks/README|runbooks guidance]]
```

Do not include `.md` in wikilink targets.

## Target Rule

Use file stems when unique:

- `[[CURRENT_CONTEXT]]`
- `[[prepare-sdk-release]]`

Use explicit paths when generic names repeat:

- `[[runbooks/README|runbooks guidance]]`
- `[[rules/AGENTS|AGENTS rules]]`

Avoid linking to generic `README` without a path.

## When To Link

Create a link when the relationship supports:

- architecture;
- execution;
- validation;
- onboarding;
- release flow;
- public API compatibility;
- dependency between a decision and a runbook;
- validation relationship between checklist and runbook;
- design relationship between spec and public API policy.

## When Not To Link

Do not link:

- generic terms;
- planned files that do not exist;
- decorative mentions;
- every repeated use of a concept;
- code identifiers unless the Markdown artifact relationship matters.

## Broken Links

Accepted or implemented artifacts must not contain broken wikilinks.

Draft artifacts may link to planned targets only when clearly marked as pending.

## Responsibility Rule

A wikilink does not move responsibility:

- context remains current state;
- decisions remain binding why/constraints;
- runbooks remain execution;
- checklists remain validation;
- specs remain planned implementation design;
- templates remain scaffolding;
- tools remain helpers.

## Project Process Knowledge

Project-level process documentation may use relative wikilinks when it is easier
to move as a folder.

Follow [[PROCESS_KNOWLEDGE_RULES]].

## Obsidian Usage

Prefer opening `.aiassistant` directly as an Obsidian vault.

Repository-root files may not appear when `.aiassistant` is opened as the vault.
That is expected.

## Validation

Before finishing changes to `.aiassistant` Markdown files:

- confirm that new links target existing Markdown files;
- confirm that links represent meaningful relationships;
- run [[validate-wikilinks]] when available.

## Related Files

- [[0001-knowledge-graph-wikilink-policy]]
- [[use-obsidian-knowledge-graph]]
- [[validate-wikilinks]]

