---
apply: always
---

# Wikilink Rules

This file defines how Obsidian-compatible wikilinks must be used inside `.aiassistant` Markdown artifacts.

## Purpose

Wikilinks connect existing repository artifacts into a navigable knowledge graph.

They must represent meaningful relationships between context, decisions, runbooks, checklists, feedback, roadmap, specs, prompts, templates, and rules.

They must not create a separate wiki or duplicate source of truth.

Related governance:

- [[0001-knowledge-graph-wikilink-policy]]
- [[validate-wikilinks]]
- [[use-obsidian-knowledge-graph]]

## Link Format

Use Obsidian wikilinks:

- `[[CURRENT_CONTEXT]]`
- `[[0001-knowledge-graph-wikilink-policy]]`
- `[[bootstrap-project-context]]`
- `[[WIKILINK_RULES]]`

Use aliases only when the target name is correct but the visible text needs to be clearer:

- `[[0001-knowledge-graph-wikilink-policy|Knowledge graph policy]]`

## Target Rule

Link to the Markdown file stem, without `.md`, when the target name is unique inside the `.aiassistant` vault.

Use:

- `[[CURRENT_CONTEXT]]`
- `[[bootstrap-project-context]]`

Do not use:

- `[[CURRENT_CONTEXT.md]]`
- `[[runbooks/bootstrap-project-context.md]]`

If multiple files share the same stem, use an Obsidian path with an alias:

- `[[rules/AGENTS|AGENTS rules]]`

Avoid linking to repeated generic names such as `README` unless the target path is explicit.

## When To Link

Create a wikilink when the relationship is meaningful.

Valid relationships include:

- a decision constrains a runbook;
- a checklist validates a runbook;
- a spec implements accepted feedback;
- a roadmap item includes a spec or decision;
- context summarizes a decision that affects current behavior;
- a rule governs how an artifact must be written.

## When Not To Link

Do not create wikilinks for decorative references, generic concepts, temporary ideas, or files that do not exist.

Avoid linking every mention of a concept. The graph should stay useful for architecture, execution, validation, and onboarding.

## Broken Links

Accepted or implemented artifacts must not contain broken wikilinks.

Draft artifacts may reference planned targets only when the missing target is intentional and clearly listed as pending work in the same file.

## Responsibility Rule

A wikilink does not move responsibility between files.

- `CURRENT_CONTEXT.md` remains the source of truth for current behavior.
- `decisions/` remains the source of truth for why constraints exist.
- `runbooks/` remains the source of truth for execution.
- `checklists/` remains the source of truth for validation.
- `rules/` remains the source of truth for repository and agent behavior.
- `tools/` stores executable helpers only.

## Obsidian Usage

Prefer opening `.aiassistant` itself as the Obsidian vault.

If the repository root is opened as the vault, verify that Obsidian indexes the `.aiassistant` dot-folder. Some Obsidian setups may hide or ignore root-level dot-folders unless configured or extended with a plugin.

Obsidian should detect the Markdown files and display wikilink relationships in Graph View.

The repository must remain readable and useful without Obsidian.

## Validation

Before finishing changes to `.aiassistant` Markdown files:

- confirm that new wikilinks target existing Markdown file stems;
- confirm that links represent real relationships;
- confirm that no new source of truth was created;
- confirm that aliases do not hide unclear or unstable targets.
- run [[validate-wikilinks]] when automatic validation is available.
