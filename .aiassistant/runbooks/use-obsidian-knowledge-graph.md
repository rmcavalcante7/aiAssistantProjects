# Use Obsidian Knowledge Graph

## Objective

Open the `.aiassistant` knowledge base in Obsidian and inspect the wikilink graph.

## When to use

Use this runbook when:

- reviewing relationships between `.aiassistant` artifacts;
- onboarding into the repository structure;
- checking whether new wikilinks improve or pollute the graph;
- validating the first-phase visual knowledge map without a custom script.

## Preconditions

- Obsidian is installed.
- `.aiassistant` exists in the repository root.
- Markdown files use wikilinks according to [[WIKILINK_RULES]].

## Inputs

- Repository path.
- `.aiassistant` directory.

## Steps

1. Open Obsidian.
2. Choose `Open folder as vault`.
3. Select the `.aiassistant` directory, not the repository root.
4. Open Graph View.
5. Inspect whether important artifacts are connected:
   - [[MAP]]
   - [[CURRENT_CONTEXT]]
   - [[0001-knowledge-graph-wikilink-policy]]
   - [[WIKILINK_RULES]]
   - [[bootstrap-project-context]]
6. Check whether the graph has noisy or decorative links.
7. Check whether any expected relationship is missing.

## Validation

- Obsidian shows Markdown files from `.aiassistant`.
- Graph View displays wikilink relationships.
- Important governance artifacts are connected.
- [[MAP]] acts as the main navigation hub.
- No accepted artifact intentionally depends on a broken link.
- The graph helps explain repository structure instead of duplicating content.

## Outputs

- A visual graph in Obsidian.
- Optional feedback entries if graph usage reveals missing, noisy, or broken relationships.

## Failure scenarios

### `.aiassistant` is not visible from the repository root

Open `.aiassistant` directly as the vault.

### Root files do not appear in the graph

This is expected when `.aiassistant` is opened directly as the vault. Files such as `../README.md` and `../AGENTS.md` are outside the vault and remain root-level entrypoints.

To include root files as graph nodes, open the repository root as the vault and verify that Obsidian indexes the `.aiassistant` dot-folder.

### `Sem título.canvas` appears as an isolated node

This is an Obsidian canvas file created inside the vault. Delete it in Obsidian if it is not being used.

### Graph has too many nodes

Remove decorative or weak links. Keep only relationships that support architecture, execution, validation, or onboarding.

### A link appears broken

Verify that the wikilink target matches an existing Markdown file stem. If the target is planned but not created, keep it only in a draft artifact and document it as pending work.

## Notes

This runbook does not require a custom graph generator.

Future automation may add a Python validation script that detects broken wikilinks and exports graph data.
