---
apply: always
---

# Context Management Rules

This file defines how project context must be created, updated, and maintained.

It MUST be followed at all times.

Related governance:

- [[CURRENT_CONTEXT]]
- [[CONTEXT_TEMPLATE]]
- [[bootstrap-project-context]]
- [[REPOSITORY_GUIDELINES]]
- [[MAP]]

---

# 🧠 1. Single Source Of Truth

- There MUST be only ONE active context file:
  `.aiassistant/project_context/CURRENT_CONTEXT.md`
- This file is the ONLY valid runtime context.

---

# 🚫 2. Forbidden Behaviors

The system MUST NOT:

- create multiple active context files
- keep parallel versions of context
- append context blindly without refactoring
- use outdated context as source of truth
- mix temporary notes with permanent context

---

# 🔄 3. Context Creation

## When `CURRENT_CONTEXT.md` does NOT exist

- Do NOT generate context from assumptions.
- Do NOT invent flows, integrations, or constraints.
- Use `.aiassistant/rules/CONTEXT_TEMPLATE.md` only after enough explicit project information exists.
- Ask the user for the missing definition first.

## Once the required information exists

- Generate `CURRENT_CONTEXT.md` using `.aiassistant/rules/CONTEXT_TEMPLATE.md`.
- Ensure all sections are present.
- Do NOT leave placeholders.

---

# 🔁 4. Context Update (Critical)

When new information is introduced:

## DO

- refactor the existing `CURRENT_CONTEXT.md`
- keep it clean, structured, and consistent
- integrate new information into the correct section

## DO NOT

- append raw notes at the end
- duplicate sections
- create `v2`, `new`, or similar files

---

# 🧱 5. Context Vs Decisions

## Use context for

- current system behavior
- flows
- integrations
- runtime understanding

## Use decisions for

- architectural rules
- constraints
- long-term choices

## Rule

- context must NOT override decisions
- context must reference decisions when relevant

---

# 📜 6. Context Vs History

Files inside `.aiassistant/project_context/history/` are historical snapshots only.

## Rules

- NEVER use them as active context
- ONLY consult them when explicitly requested

---

# 🧹 7. Context Cleanliness

`CURRENT_CONTEXT.md` must always be:

- coherent
- concise
- non-redundant
- aligned with system reality

If the file becomes inconsistent, duplicated, or confusing:

- refactor it immediately

---

# ⚠️ 8. When To Update Context

Update `CURRENT_CONTEXT.md` when:

- a new integration is added
- a core flow changes
- a decision impacts runtime behavior
- a major bug changes system understanding
- a migration or refactor is completed

---

# 🧠 9. Engineering Behavior

When working with context:

- ALWAYS read `CURRENT_CONTEXT.md` first when it exists
- ALWAYS validate against decisions
- NEVER assume missing information
- ASK if something is unclear

---

# 🆕 10. Context Bootstrap

When `.aiassistant/project_context/CURRENT_CONTEXT.md` does NOT exist:

## DO NOT

- generate context automatically
- assume system structure
- invent flows or integrations

## INSTEAD

- offer to initialize project context
- gather information progressively
- create the file only after enough explicit details are available

Example behavior:

`It looks like this project does not have a defined context yet. Would you like me to help you create a structured CURRENT_CONTEXT.md?`

## If the user agrees

Guide the user progressively through:

1. Project overview
2. Scope and project type
3. Core flows
4. Integrations
5. Constraints

## After collecting answers

- generate `CURRENT_CONTEXT.md`
- follow `.aiassistant/rules/CONTEXT_TEMPLATE.md`
- ensure clarity and consistency

## Important

- do NOT ask all questions at once if the user is still exploring
- adapt questions progressively
- keep interaction natural and concise

---

# 🎯 Final Rule

Context is a living document, not a log.

It must represent:

- the current state of the system
- not its history

---

END OF FILE
