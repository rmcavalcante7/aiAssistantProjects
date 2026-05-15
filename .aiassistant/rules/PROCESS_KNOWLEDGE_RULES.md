---
apply: always
---

# Process Knowledge Rules

This file defines how agents must create and evolve project-level process and
business-rule documentation while development work is happening.

Related governance:

- [[0003-process-knowledge-documentation-lifecycle]]
- [[0002-automation-simplicity-and-stage-boundaries]]
- [[WIKILINK_RULES]]
- [[update-process-knowledge-documentation]]
- [[process-documentation-quality-checklist]]

## Purpose

Process knowledge documentation makes business behavior explicit.

It should explain how the project works from the perspective of processes,
rules, systems, data contracts, operational effects, and validation needs.

It must evolve together with the implementation.

## Scope

Use these rules when development changes or creates:

- a business rule;
- a business process or automation stage;
- an input, output, payload, status, or data contract;
- an external system interaction;
- a lookup, filtering, validation, routing, or eligibility rule;
- an error-handling, retry, fallback, or missing-data behavior;
- an evidence, audit, logging, or reconciliation requirement;
- an operational risk, limitation, or manual intervention point.

Purely internal refactors do not require process documentation updates when they
do not change observable behavior, contracts, business meaning, or operational
flow.

## Documentation Location

The recommended project-level root is:

```text
project_knowledge/
```

Use this root for business and operational knowledge about the application or
automation being built.

Do not use `project_knowledge/` as a replacement for `.aiassistant`.

- `.aiassistant/` governs how agents operate in the repository.
- `project_knowledge/` documents how the project business process works.

If a project already has an accepted documentation root for process knowledge,
use that existing root instead of creating a duplicate structure.

## Minimum Structure

For projects with meaningful process complexity, prefer this structure:

```text
project_knowledge/
  MAP.md
  00-systems/
  01-<process-or-stage>/
    index.md
    rule-<business-rule>.md
    contract-<input-or-output>.md
    risk-<operational-risk>.md
```

The structure may be smaller for simple projects. Do not create empty folders or
placeholder files that do not describe real behavior.

## Agent Workflow

Before implementation:

1. Read the active context and accepted decisions.
2. Check whether process knowledge already exists.
3. Identify which process, stage, rule, system, contract, or risk the change
   affects.

During implementation:

1. Keep business rules isolated enough to be tested when possible.
2. Preserve external system boundaries as process-stage boundaries.
3. Update or create the relevant process knowledge notes as behavior becomes
   clear.

Before finishing:

1. Update `project_knowledge/MAP.md` or the equivalent central map when a new
   process area, stage, system, contract, or rule is added.
2. Update the process `index.md` when stage behavior changes.
3. Update business-rule notes when criteria, inputs, outputs, or missing-data
   behavior changes.
4. Update system notes when integrations, system responsibilities, or ownership
   change.
5. Update contract notes when payloads, files, statuses, schemas, or required
   fields change.
6. Update risk notes when a known limitation, manual dependency, or failure mode
   changes.
7. Validate wikilinks when automatic validation is available.
8. Apply [[process-documentation-quality-checklist]].

## Business Rule Notes

Every business rule note should make these points explicit when they apply:

- owner or accountable area;
- business purpose;
- source of truth for the rule;
- input data and lookup keys;
- decision criteria;
- output or classification produced by the rule;
- behavior when required data is missing;
- operational effect of applying the rule;
- process stage where the rule belongs;
- systems touched by the rule;
- evidence, audit, or validation requirement;
- known exceptions or unresolved questions.

Do not document line-by-line implementation details unless they are necessary to
understand the business behavior or operational contract.

## Wikilinks

Use wikilinks to connect meaningful process relationships:

- process map -> process index;
- process stage -> business rule;
- business rule -> system note;
- business rule -> input or output contract;
- process stage -> risk or manual intervention;
- contract -> system that owns or consumes it.

Avoid linking every repeated word. Links should improve navigation and graph
readability.

Use relative wikilinks when they make process documentation easier to move as a
folder:

```md
[[../00-systems/source-system]]
[[rule-eligibility-check]]
[[contract-request-payload]]
```

## Obsidian Canvas

Canvas files may be used as curated visual maps.

Rules:

- Markdown notes remain the source of truth.
- Canvas must link back to Markdown notes when it represents real process
  knowledge.
- Do not create a canvas that duplicates detailed rule text already stored in
  Markdown.
- Keep canvas readable enough for navigation and onboarding.

## Completion Rule

A development task that changes process or business behavior is not complete
until one of these is true:

- the relevant process knowledge documentation was updated;
- the agent explicitly states that no process knowledge update was required and
  why.

If the process behavior is unclear, stop and ask for clarification before
documenting assumptions as facts.
