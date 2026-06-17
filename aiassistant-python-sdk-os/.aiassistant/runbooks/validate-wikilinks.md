# Validate Wikilinks

## Objective

Validate Obsidian-compatible wikilinks inside a Markdown vault.

## When To Use

Use when adding or changing `.aiassistant` Markdown links.

## Preconditions

- Python is available.
- The target vault exists.

## Steps

From the repository root, run:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant
```

To export graph data:

```powershell
python .aiassistant/tools/validate_wikilinks.py --vault .aiassistant --json-output .aiassistant/graph.json
```

## Validation

The report should show:

```text
Broken links: 0
Ambiguous links: 0
Malformed links: 0
```

## Related Files

- [[WIKILINK_RULES]]
- [[0001-knowledge-graph-wikilink-policy]]

