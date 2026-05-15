# Update Process Knowledge Documentation

## Objective

Update project-level process and business-rule documentation as part of a
development change.

## When to use

Use this runbook when a task changes business behavior, process stages, external
system interactions, input/output contracts, operational risks, error handling,
or validation rules.

Follow [[PROCESS_KNOWLEDGE_RULES]].

## Preconditions

- The active project context has been read.
- Accepted decisions relevant to the change have been read.
- The implementation change or intended behavior is clear.
- Existing `project_knowledge/` documentation has been inspected when present.

## Inputs

- The development change being implemented.
- Existing process knowledge documentation, if any.
- Relevant code, specs, decisions, runbooks, or checklists.

## Steps

1. Identify whether the change affects process knowledge.
2. Locate the owning process map or process `index.md`.
3. Locate or create notes for affected business rules, systems, contracts, and
   risks.
4. Update the notes with the current behavior.
5. Add wikilinks only for meaningful relationships.
6. Update the central process map when a new process, stage, system, contract,
   or rule becomes relevant.
7. If a maintained canvas exists, update it only when the visual navigation
   would otherwise become misleading.
8. Run wikilink validation when available.
9. Apply [[process-documentation-quality-checklist]].
10. Mention the documentation update in the delivery summary.

## Validation

- The updated notes describe current behavior.
- No new business behavior exists only in source code.
- Wikilinks target existing Markdown notes.
- The process map still provides a navigation path to the affected notes.
- Markdown remains the source of truth even when a canvas exists.

## Outputs

- Updated process knowledge Markdown files.
- Optional updated canvas file.
- Validation results or a clear explanation when validation could not be run.

## Failure scenarios

### No process knowledge root exists

Create `project_knowledge/` only when the project has real process complexity or
the user asks for process documentation. Start with `MAP.md` and the smallest
useful process folder.

### Existing documentation contradicts the implementation

Do not silently overwrite the documentation. Identify the conflict, decide
whether code or documentation is outdated, and ask the user when the source of
truth is unclear.

### The behavior is not known

Do not document assumptions as facts. Ask for clarification or record the open
question in the appropriate note.

## Notes

This runbook updates project process knowledge. It does not replace
`.aiassistant` governance documents such as [[CURRENT_CONTEXT]], decisions, or
repository rules.
