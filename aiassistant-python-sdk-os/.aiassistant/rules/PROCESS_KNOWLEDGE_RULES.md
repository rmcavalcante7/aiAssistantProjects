---
apply: always
---

# Process Knowledge Rules

This file defines how process and business-rule documentation must be handled
when an SDK wraps operational behavior.

## Purpose

Process knowledge makes business behavior explicit.

It explains how the project works from the perspective of processes, rules,
systems, contracts, operational effects, risks, and validation needs.

For SDKs, process knowledge is not always needed. It becomes important when the
SDK encodes business behavior rather than only technical transport behavior.

## Scope

Use process knowledge when SDK work affects:

- business rules;
- process stages;
- external system responsibilities;
- input or output contracts;
- status transitions;
- retries, fallbacks, or manual intervention;
- evidence, audit, or reconciliation expectations;
- domain-specific validations or eligibility rules;
- workflow orchestration exposed as SDK methods;
- integration side effects visible to business users.

Pure technical SDK changes do not require process knowledge updates when they do
not change business or operational behavior.

## Location

Use:

```text
project_knowledge/
```

Do not use `project_knowledge/` as a replacement for `.aiassistant`.

If the target project already has an accepted process documentation root, use
that root instead of creating a duplicate.

## Minimum Structure

For process-heavy projects:

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

Do not create empty placeholder folders without real process knowledge.

## Agent Workflow

Before implementation:

1. read active context and accepted decisions;
2. check whether process knowledge exists;
3. identify whether the SDK change affects process behavior;
4. locate the owning process, rule, system, contract, or risk.

During implementation:

1. keep business rules isolated enough to test when possible;
2. preserve external-system boundaries;
3. update relevant process notes as behavior becomes clear;
4. avoid documenting assumptions as facts.

Before finishing:

1. update the central process map when a new area is added;
2. update process index notes when stage behavior changes;
3. update business-rule notes when criteria, inputs, outputs, or missing-data
   behavior change;
4. update system notes when integration responsibilities change;
5. update contract notes when payloads, schemas, statuses, or required fields
   change;
6. update risk notes when limitations, manual steps, or failure modes change;
7. validate wikilinks when available;
8. apply [[process-documentation-quality-checklist]].

## Business Rule Notes

Business rule notes should document, when applicable:

- owner or accountable process;
- business purpose;
- source of truth;
- input data;
- lookup keys;
- decision criteria;
- output or classification;
- missing-data behavior;
- operational effect;
- systems touched;
- evidence or audit requirement;
- known exceptions;
- unresolved questions.

Do not document line-by-line implementation details unless needed to understand
business behavior or a contract.

## Contract Notes

Contract notes should document:

- payload, file, schema, status, or object shape;
- required and optional fields;
- producer and consumer;
- validation rules;
- compatibility expectations;
- example payloads when useful and safe.

## System Notes

System notes should document:

- system responsibility;
- integration boundary;
- authentication location without secrets;
- important endpoints, files, queues, or transactions;
- operational risks;
- ownership or escalation path when known.

## Wikilinks

Use wikilinks for meaningful relationships:

- process map -> process index;
- process stage -> business rule;
- business rule -> system;
- business rule -> contract;
- process stage -> risk;
- contract -> owning or consuming system.

Avoid linking every repeated word.

Relative wikilinks are allowed in process documentation when they make folders
portable:

```md
[[../00-systems/source-system]]
[[rule-eligibility-check]]
[[contract-request-payload]]
```

## Obsidian Canvas

Canvas files may be used as visual navigation.

Rules:

- Markdown remains the source of truth.
- Canvas cards must link to Markdown notes when they represent real process
  knowledge.
- Canvas must not be the only place where a rule or contract exists.
- Keep canvas readable enough for onboarding.

## Completion Rule

A development task that changes business or operational behavior is complete
only when one of these is true:

- the related process knowledge was updated;
- the agent explicitly states that no process knowledge update was required and
  why.

If behavior is unclear, stop and ask for clarification before documenting
assumptions as facts.

## Related Files

- [[0006-process-knowledge-documentation-lifecycle]]
- [[update-process-knowledge-documentation]]
- [[process-documentation-quality-checklist]]
- [[WIKILINK_RULES]]

