# Checklists

This directory contains validation checklists used to ensure correctness, completeness, and safety before executing or delivering something.

Checklists are designed to:

- validate conditions
- prevent mistakes
- enforce consistency

They represent **what must be verified**, not how to execute.

Related governance:

- [[CURRENT_CONTEXT]]
- [[runbooks/README|runbooks guidance]]
- [[decisions/README|decisions guidance]]
- [[WIKILINK_RULES]]

---

# When to create a checklist

Create a checklist when:

- a process must be validated before execution
- a deployment or production test is involved
- a flow has critical preconditions
- errors are costly and must be avoided
- consistency across executions is required

Examples:

- pre-production validation
- environment readiness
- input validation before processing
- verification before sending data to external systems

---

# When NOT to create a checklist

Do NOT create a checklist for:

- step-by-step execution (use `runbooks/`)
- system description (use `CURRENT_CONTEXT.md`)
- architectural rules (use `decisions/`)
- temporary notes
- debugging logs

---

# Required structure

Each checklist should follow this structure:

# Checklist Title

## Objective

What is being validated.

## When to use

When this checklist should be applied.

## Items

- [ ] Validation item 1
- [ ] Validation item 2
- [ ] Validation item 3

Each item must be:

- clear
- objective
- verifiable

## Notes

Optional additional context.

---

# Execution rules

When using a checklist:

- all items MUST be evaluated
- do not skip items
- do not assume items are satisfied
- explicitly confirm each item

---

# Relationship with other components

Use:

- checklists/ for validation
- [[runbooks/README|runbooks guidance]] for execution
- [[decisions/README|decisions guidance]] for rules
- [[CURRENT_CONTEXT]] for system understanding

---

# Key principle

A checklist does not execute.

It ensures that execution is safe and correct.

---

END OF FILE
