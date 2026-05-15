# Validate Wikilinks

## Objective

Validate Obsidian-compatible wikilinks inside a Markdown vault, usually
`.aiassistant` or a project process knowledge root such as `project_knowledge`.

## When to use

Use this runbook when:

- adding or changing wikilinks;
- preparing to inspect the graph in Obsidian;
- checking for broken or ambiguous links;
- exporting graph data for later automation.

## Preconditions

- Python 3.10 or newer is available.
- The target Markdown vault exists in the repository root.
- Wikilinks follow [[WIKILINK_RULES]].

## Inputs

- Markdown vault path, such as `.aiassistant` or `project_knowledge`.
- Optional JSON output path.

## Steps

1. Open a terminal in the repository root.
2. Run:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant
```

3. For project process knowledge, run:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault project_knowledge
```

4. Review the summary.
5. If JSON graph data is needed, run:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant --json-output .aiassistant/graph.json
```

## Validation

- The command exits with code `0`.
- The report says there are no broken links.
- The report says there are no ambiguous links.
- TOML or Markdown examples inside code blocks do not appear as wikilinks.

## Outputs

- Console validation report.
- Optional JSON graph data containing nodes, edges, broken links, ambiguous links, and malformed links.

## Failure scenarios

### Broken links are reported

Create the missing Markdown file, rename the wikilink target, or remove the link if the relationship is not real.

### Ambiguous links are reported

Use an explicit Obsidian path with an alias, as defined in [[WIKILINK_RULES]].

### Malformed links are reported

Remove unsupported syntax from the wikilink target.

## Notes

This runbook validates `.aiassistant` documentation and can also validate
project process knowledge roots that use relative wikilinks.

It does not replace [[use-obsidian-knowledge-graph]], which remains the first-phase visual inspection flow.
