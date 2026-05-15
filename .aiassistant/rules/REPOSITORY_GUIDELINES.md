---
apply: always
---

# Repository Guidelines

This file defines how the repository must evolve over time.

It ensures consistency, maintainability, and correct usage of all AI-related structures.

---

# 🧠 1. PURPOSE

The repository is structured to support:

- context-aware development
- consistent architecture
- reproducible execution
- safe validation
- long-term maintainability

All components MUST be used according to their defined roles.

---

# 🧩 2. COMPONENT RESPONSIBILITIES

Each directory has a strict responsibility:

## rules/

Defines behavior and standards:

- AGENTS.md → engineering rules
- CONTEXT_TEMPLATE.md → context structure
- CONTEXT_RULES.md → context lifecycle
- REPOSITORY_GUIDELINES.md → repository governance
- WIKILINK_RULES.md → Markdown relationship and Obsidian graph rules
- PROCESS_KNOWLEDGE_RULES.md → project process and business-rule documentation rules

---

## project_context/

Contains runtime understanding:

- CURRENT_CONTEXT.md → current system state
- history/ → historical snapshots (non-active)

---

## decisions/

Defines architectural constraints:

- what must be followed
- why the system behaves in a certain way

---

## runbooks/

Defines execution:

- how to perform tasks
- step-by-step procedures

---

## checklists/

Defines validation:

- what must be verified
- preconditions and safety checks

---

## feedback/

Captures structured input from real usage:

- bugs
- limitations
- repeated pain points
- improvement opportunities

---

## roadmap/

Defines release-oriented planning:

- scope
- phases
- validation targets

---

## specs/

Defines implementation design before coding:

- problem framing
- chosen solution
- scope boundaries
- validation approach

---

## prompts/

Stores reusable operational prompts:

- repeated workflows
- standardized output formats
- project-specific behavior

---

## templates/

Provides reusable scaffolding:

- starter artifacts
- document skeletons
- project kick-off helpers

Rules:

- templates are accelerators
- templates are NOT a source of truth
- generated files must be adapted to the real project

---

## tools/

Provides executable helpers for repository maintenance:

- validation scripts
- derived graph exports
- automated governance checks

Rules:

- tools are not a source of truth
- tools must support existing repository artifacts
- tools must not replace decisions, context, runbooks, or checklists

---

## project_knowledge/ (optional, outside `.aiassistant/`)

Documents the business process, operational flow, external systems, contracts,
risks, and business rules of the project being built.

Rules:

- use `project_knowledge/` only when the project has real process knowledge to
  document
- do not use it as an alternative `.aiassistant`
- keep Markdown as the source of truth
- use Obsidian Canvas only as visual navigation
- follow [[PROCESS_KNOWLEDGE_RULES]]

---

# 🔄 3. WHEN TO UPDATE EACH COMPONENT

## Update CURRENT_CONTEXT.md when:

- system behavior changes
- new flows are introduced
- integrations are added or modified
- a migration or refactor is completed

---

## Create a decision when:

- a rule affects architecture
- behavior must be preserved long-term
- a constraint must be enforced
- a trade-off is accepted

---

## Create a runbook when:

- a task requires repeatable execution
- a process has multiple steps
- an operation must be standardized

---

## Create a checklist when:

- validation is required before execution
- errors are costly
- safety or correctness must be ensured

---

## Create feedback when:

- a real pain point is observed
- a bug or limitation is identified
- a workaround starts repeating

---

## Create a roadmap when:

- planning a release
- grouping related changes
- organizing phased delivery

---

## Create a spec when:

- a change is complex
- a public API will change
- architecture may be affected
- implementation needs prior alignment

---

## Create a prompt when:

- a task is repeated frequently
- behavior must be standardized
- output format needs tight control

---

## Use templates when:

- starting a new project artifact
- standardizing the initial structure of a document
- creating the first version of a decision, checklist, roadmap, spec, or prompt

---

## Use tools when:

- a repository validation can be automated
- a derived artifact can be generated from source Markdown files
- manual review needs a repeatable helper

---

## Update project process knowledge when:

- a business rule changes
- a process stage is added, removed, or redefined
- an external system interaction changes
- an input, output, file, payload, status, or schema contract changes
- error handling, retry, fallback, or missing-data behavior changes
- evidence, audit, reconciliation, or validation expectations change
- an operational risk or manual intervention point changes

Use [[update-process-knowledge-documentation]] and validate with
[[process-documentation-quality-checklist]].

---

# 🚫 4. FORBIDDEN PRACTICES

The repository MUST NOT:

- mix responsibilities across components
- store decisions inside context
- store execution steps inside context
- duplicate information across files
- create multiple sources of truth
- keep outdated files active
- create alternative AI governance structures outside `.aiassistant/`
- use project process documentation as a replacement for `.aiassistant`

---

# 🧱 5. EVOLUTION RULES

## Incremental evolution

- prefer extending over rewriting
- avoid breaking existing behavior
- maintain compatibility whenever possible

---

## Decision-first changes

For significant changes:

1. define or update a decision
2. update context accordingly
3. implement changes
4. update runbooks/checklists if needed

---

## Context integrity

- CURRENT_CONTEXT.md must always reflect reality
- it must NOT become a log
- it must NOT accumulate duplicated information

---

# 🔍 6. AI BEHAVIOR EXPECTATION

When operating in this repository, the AI must:

- follow AGENTS.md (root) first
- respect context and decisions
- use runbooks for execution
- use checklists for validation
- avoid assumptions
- ask when unclear

---

# 🎯 7. KEY PRINCIPLE

Each file has ONE responsibility.

If a file tries to do more than one thing:

→ it must be refactored

---

# 🧠 FINAL RULE

This repository is a structured system.

Not a collection of notes.

---

END OF FILE
