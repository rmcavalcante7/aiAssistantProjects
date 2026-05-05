# Migrate Legacy AI Assistant Structure To Knowledge Graph

## Objective

Migrate a project that already uses the older `.aiassistant` structure to the knowledge graph structure based on Obsidian-compatible wikilinks.

## When to use

Use this runbook when:

- a project already has `.aiassistant`;
- the project does not yet have wikilink rules;
- the project does not yet have `MAP.md`;
- the project should support Obsidian graph navigation;
- the project should validate wikilinks automatically.

## Preconditions

- The destination project has a `.aiassistant` directory.
- Existing project context and decisions have been reviewed.
- Existing `CURRENT_CONTEXT.md` will not be overwritten.
- The migration follows [[WIKILINK_RULES]].

## Inputs

- Updated template repository.
- Destination project repository.
- Existing `.aiassistant` structure in the destination project.

## Steps

1. Check whether the destination project has:

```text
.aiassistant/project_context/CURRENT_CONTEXT.md
```

2. If it exists, preserve it and update it manually only where the knowledge graph affects current repository behavior.

3. If it does not exist, initialize it by following [[bootstrap-project-context]].

4. Copy these files into the destination project:

```text
.aiassistant/MAP.md
.aiassistant/rules/WIKILINK_RULES.md
.aiassistant/runbooks/use-obsidian-knowledge-graph.md
.aiassistant/runbooks/validate-wikilinks.md
.aiassistant/tools/README.md
.aiassistant/tools/validate_wikilinks.py
```

5. Copy the knowledge graph decision into `.aiassistant/decisions/`.

6. If the destination project already has a `0001-*` decision, rename the copied decision to the next available number and update wikilinks that reference it.

7. Update the root `AGENTS.md` reading order so `WIKILINK_RULES.md` is read before `.aiassistant/rules/AGENTS.md`.

8. Update `.aiassistant/rules/AGENTS.md` so `WIKILINK_RULES.md` is part of the internal context loading priority.

9. Update `.aiassistant/rules/REPOSITORY_GUIDELINES.md` to describe:
   - `WIKILINK_RULES.md`;
   - `.aiassistant/tools/`;
   - when tools should be used.

10. Add wikilinks incrementally to existing Markdown files:
    - context to important decisions and runbooks;
    - decisions to related rules, runbooks, and context;
    - runbooks to required decisions and checklists;
    - specs to feedback, decisions, and validation;
    - templates to `templates/README`;
    - tools to their runbooks and rules.

11. Run validation:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant
```

12. Open `.aiassistant` as an Obsidian vault and inspect the graph by following [[use-obsidian-knowledge-graph]].

## Validation

- Existing `CURRENT_CONTEXT.md` was preserved or initialized correctly.
- The copied decision has a unique decision number.
- `WIKILINK_RULES.md` is included in both agent reading orders.
- `.aiassistant/tools/` is documented as helper tooling only.
- `MAP.md` appears as a central graph node.
- The wikilink validator reports:

```text
Broken links: 0
Ambiguous links: 0
Malformed links: 0
```

## Outputs

- Migrated `.aiassistant` structure.
- Obsidian-compatible knowledge graph.
- Validated wikilinks.
- Optional graph JSON export.

## Failure scenarios

### Existing decision number conflicts

Rename the copied knowledge graph decision to the next available number and update all references.

### Existing context conflicts with the new graph behavior

Do not overwrite context. Refactor only the sections affected by the adopted knowledge graph behavior.

### Obsidian does not show `.aiassistant` from the repository root

Open `.aiassistant` directly as the vault.

### The graph becomes noisy

Remove decorative or weak links. Keep only relationships that support architecture, execution, validation, or onboarding.

### The validator reports malformed links from code examples

Confirm the example is inside a fenced code block or inline code. The validator intentionally ignores code regions.

## Notes

The migration adds a relationship layer. It must not move files, duplicate documentation, or create a parallel wiki.
