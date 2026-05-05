# Changelog

## 2026-05-05 - Knowledge Graph And Obsidian Support

This release evolves the `.aiassistant` repository structure with a lightweight knowledge graph layer based on Obsidian-compatible wikilinks.

The goal is to make relationships between context, decisions, runbooks, checklists, feedback, roadmap, specs, prompts, rules, templates, and tools visible without creating a separate wiki or a second source of truth.

## Added

- `.aiassistant/MAP.md`
  - Main navigation map for the Obsidian vault.
  - Connects the major `.aiassistant` governance artifacts.

- `.aiassistant/rules/WIKILINK_RULES.md`
  - Defines when and how to use Obsidian wikilinks.
  - Defines link naming, aliases, broken link handling, and graph hygiene.

- `.aiassistant/decisions/0001-knowledge-graph-wikilink-policy.md`
  - Records the accepted architectural policy for the knowledge graph.
  - Establishes that wikilinks are a relationship layer, not a new documentation layer.

- `.aiassistant/runbooks/use-obsidian-knowledge-graph.md`
  - Explains how to open `.aiassistant` as an Obsidian vault.
  - Explains why repository-root files do not appear when `.aiassistant` is opened directly.

- `.aiassistant/runbooks/validate-wikilinks.md`
  - Defines the validation flow for wikilinks.

- `.aiassistant/tools/validate_wikilinks.py`
  - Validates wikilinks without external dependencies.
  - Detects broken links, ambiguous links, and malformed links.
  - Ignores fenced code blocks and inline code.
  - Can export graph data as JSON.

- `.aiassistant/tools/README.md`
  - Defines the role of executable repository helpers.

## Changed

- `AGENTS.md`
  - Adds `WIKILINK_RULES.md` to the mandatory reading order.
  - States that Markdown relationship links inside `.aiassistant` must follow the wikilink rules.

- `.aiassistant/rules/AGENTS.md`
  - Adds `WIKILINK_RULES.md` to the internal context loading priority.

- `.aiassistant/rules/REPOSITORY_GUIDELINES.md`
  - Defines the responsibility of `.aiassistant/tools/`.
  - Registers `WIKILINK_RULES.md` as a repository rule.

- `README.md`
  - Documents the knowledge graph capability.
  - Documents `.aiassistant/tools/`.

- `.aiassistant/*/README.md`
  - Adds meaningful wikilinks between governance artifacts.
  - Avoids decorative or generic links.

- `.aiassistant/project_context/CURRENT_CONTEXT.md`
  - Initializes active context for this repository.
  - Documents the current knowledge graph behavior.

## Migration Guide

Use this section for projects that already use the older `.aiassistant` structure.

### 1. Preserve Existing Project Context

Do not overwrite an existing:

```text
.aiassistant/project_context/CURRENT_CONTEXT.md
```

If the project already has context, update it manually to mention the knowledge graph only if the graph is adopted.

If the project does not have context, create it using:

```text
.aiassistant/runbooks/bootstrap-project-context.md
```

### 2. Copy New Governance Files

Copy these files from the updated template:

```text
.aiassistant/MAP.md
.aiassistant/rules/WIKILINK_RULES.md
.aiassistant/decisions/0001-knowledge-graph-wikilink-policy.md
.aiassistant/runbooks/use-obsidian-knowledge-graph.md
.aiassistant/runbooks/validate-wikilinks.md
.aiassistant/tools/README.md
.aiassistant/tools/validate_wikilinks.py
```

If the destination project already has a decision named `0001-*`, choose the next available decision number and update links accordingly.

### 3. Update Agent Reading Order

Update the root `AGENTS.md` so `WIKILINK_RULES.md` is read before `.aiassistant/rules/AGENTS.md`.

Expected order near the end:

```text
.aiassistant/rules/CONTEXT_RULES.md
.aiassistant/rules/REPOSITORY_GUIDELINES.md
.aiassistant/rules/WIKILINK_RULES.md
.aiassistant/rules/AGENTS.md
```

Also update `.aiassistant/rules/AGENTS.md` to include:

```text
.aiassistant/rules/WIKILINK_RULES.md
```

in its context loading priority.

### 4. Update Repository Guidelines

Update `.aiassistant/rules/REPOSITORY_GUIDELINES.md` to include:

- `WIKILINK_RULES.md` under `rules/`;
- `tools/` as executable helpers, not a source of truth;
- guidance for when to use tools.

### 5. Add Wikilinks Incrementally

Start with stable governance links:

- `CURRENT_CONTEXT` to important decisions and runbooks;
- decisions to related rules, runbooks, and context;
- runbooks to required decisions and checklists;
- specs to feedback, decisions, and validation;
- templates to `templates/README`;
- tools to runbooks and rules.

Do not link every mention of every concept.

### 6. Open In Obsidian

Open this folder as the Obsidian vault:

```text
.aiassistant
```

This is the recommended setup because some Obsidian environments hide root-level dot-folders when the repository root is opened as the vault.

Repository-root files such as `README.md` and `AGENTS.md` will not appear in the graph when `.aiassistant` is opened directly. This is expected.

### 7. Validate

Run:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant
```

Expected result:

```text
Broken links: 0
Ambiguous links: 0
Malformed links: 0
```

Optional JSON export:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant --json-output .aiassistant/graph.json
```

## Compatibility Notes

- No existing project files need to be moved.
- No external Python dependency is required.
- The graph remains useful without Obsidian because links are plain Markdown text.
- Obsidian is used for visualization only.
- The validator is a helper and does not replace repository governance.

## Recommended Migration Order

1. Copy files.
2. Update reading order.
3. Update repository guidelines.
4. Add `MAP.md`.
5. Add wikilinks gradually.
6. Validate with Python.
7. Open `.aiassistant` in Obsidian.
8. Remove noisy links if the graph becomes hard to read.
