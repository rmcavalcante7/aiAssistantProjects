# Update Process Knowledge Documentation

## Objective

Update project-level process knowledge when SDK work affects business or
operational behavior.

## When To Use

Use when a change affects:

- business rules;
- process stages;
- external system interactions;
- contracts;
- risks;
- error handling;
- validation rules;
- status transitions;
- evidence or audit behavior.

Follow [[PROCESS_KNOWLEDGE_RULES]].

## Preconditions

- Active context has been read.
- Relevant accepted decisions have been read.
- The behavior change is understood.
- Existing `project_knowledge/` documentation has been inspected when present.

## Inputs

- Development change being implemented.
- Existing process knowledge documentation.
- Relevant SDK code, specs, decisions, runbooks, or checklists.

## Steps

1. Identify whether the SDK change affects process knowledge.
2. Locate `project_knowledge/MAP.md` or create it only when the project has real
   process complexity.
3. Locate or create affected process, rule, system, contract, or risk notes.
4. Update notes with current behavior.
5. Add meaningful wikilinks.
6. Update the central process map when a new process, system, contract, rule, or
   risk becomes relevant.
7. Update canvas files only if they are maintained and would otherwise become
   misleading.
8. Validate wikilinks when available.
9. Apply [[process-documentation-quality-checklist]].
10. Mention the documentation update in the delivery summary.

## Validation

- Business behavior is not documented only in code.
- Markdown remains the source of truth.
- Wikilinks target existing notes.
- Process map provides a navigation path to affected notes.
- Documentation does not duplicate `.aiassistant` governance.

## Outputs

- Updated process knowledge Markdown files.
- Optional updated canvas files.
- Validation result or explanation when validation could not run.

## Failure Scenarios

### No Process Knowledge Root Exists

Create `project_knowledge/` only when there is real process complexity or the
user asks for process documentation.

### Documentation Contradicts Implementation

Do not overwrite silently. Identify the conflict and ask when source of truth is
unclear.

### Behavior Is Unknown

Do not document assumptions as facts. Ask for clarification.

## Related Files

- [[PROCESS_KNOWLEDGE_RULES]]
- [[process-documentation-quality-checklist]]

