# Runbooks

This directory contains executable procedures that define how to perform specific operational tasks in the system.

Runbooks are designed to be:

- step-by-step
- deterministic
- reproducible

They represent **how to execute something**, not why it exists.

Related governance:

- [[CURRENT_CONTEXT]]
- [[decisions/README|decisions guidance]]
- [[checklists/README|checklists guidance]]
- [[WIKILINK_RULES]]

---

# When to create a runbook

Create a runbook when:

- a process must be executed consistently
- a flow requires multiple steps
- an operation interacts with external systems
- a task is repeated frequently
- validation or testing requires a defined sequence

Examples:

- processing a file
- validating a pipeline
- running a production test
- setting up credentials
- executing an automation flow

---

# When NOT to create a runbook

Do NOT create a runbook for:

- architectural decisions (use `decisions/`)
- system description (use `CURRENT_CONTEXT.md`)
- temporary notes
- debugging logs
- high-level explanations without execution steps

---

# Required structure

Each runbook should follow this structure:

# Runbook Title

## Objective

What this runbook does.

## When to use

When this procedure should be executed.

## Preconditions

What must be true before execution.

## Inputs

Required data, files, or parameters.

## Steps

Step-by-step instructions.

Each step must be:

- clear
- ordered
- executable

## Validation

How to confirm the process worked correctly.

## Outputs

Expected results or artifacts.

## Failure scenarios

Common failure cases and how to handle them.

## Notes

Optional additional observations.

---

# Execution rules

When a runbook exists:

- follow it exactly
- do not skip steps
- do not improvise
- do not change flow unless explicitly instructed

---

# Relationship with other components

Use:

- runbooks/ for execution
- decisions/ for rules and constraints
- CURRENT_CONTEXT.md for system understanding

Common starter runbooks in this repository:

- [[bootstrap-project-context]]
- [[generate-project-readme]]
- [[generate-pyproject-runbook]]
- [[generic-python-package-publish]]
- [[use-obsidian-knowledge-graph]]
- [[validate-wikilinks]]
- [[migrate-legacy-aiassistant-to-knowledge-graph]]

---

# Key principle

A runbook is not documentation.

It is an **executable procedure**.

---

END OF FILE
