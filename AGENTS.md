# AI Repository Operating System

This file defines how the AI must navigate, understand, and operate within this repository.

It MUST be followed before any action.

---

# 🧠 1. Execution Priority (Mandatory Order)

Before taking any action, ALWAYS follow this reading order:

1. `.aiassistant/project_context/CURRENT_CONTEXT.md`
2. `.aiassistant/decisions/`
3. `.aiassistant/runbooks/`
4. `.aiassistant/checklists/`
5. `.aiassistant/feedback/`
6. `.aiassistant/roadmap/`
7. `.aiassistant/specs/`
8. `.aiassistant/prompts/`
9. `.aiassistant/rules/CONTEXT_RULES.md`
10. `.aiassistant/rules/REPOSITORY_GUIDELINES.md`
11. `.aiassistant/rules/WIKILINK_RULES.md`
12. `.aiassistant/rules/AGENTS.md`

---

# 📌 2. Context Rules

## Single source of truth

- `CURRENT_CONTEXT.md` is the ONLY valid runtime context.
- Files inside `project_context/history/` are historical snapshots.
- NEVER use historical context unless explicitly requested.

## If context is missing or unclear

- STOP implementation.
- Ask for clarification.
- Do NOT assume.

---

# 🧱 3. Decision System (Critical)

Files in `/decisions/` represent:

- validated architectural rules
- production constraints
- system contracts

## Default behavior

- ALWAYS follow accepted decisions.

## Exception rule

If a better approach is identified:

- DO NOT override silently.

Instead:

1. Explain:
   - why the current decision may be suboptimal
   - risks of keeping it
   - benefits of changing it
2. Ask for approval before proceeding.

## Strict rule

- NEVER change behavior defined in accepted decisions without explicit approval.

---

# ⚙️ 4. Runbook System

Runbooks define executable flows.

## When a runbook exists

- Follow it step-by-step.
- Do NOT invent alternative flows.
- Do NOT skip steps.

## Critical runbooks

- `bootstrap-project-context.md`
- `generate-project-readme.md`
- `generate-pyproject-runbook.md`
- `generic-python-package-publish.md`

These MUST be used when applicable.

## Scope note

- `generate-pyproject-runbook.md` and `generic-python-package-publish.md` apply to installable or publishable Python packages.
- Pure automations, RPA flows, and internal scripts do NOT automatically require those runbooks.

---

# ✅ 5. Checklist System

Checklists define validation rules.

## Always

- Validate outputs using relevant checklists.
- Ensure all items are respected before finishing.

---

# 🧩 6. Engineering Rules

All code generation MUST follow:

- `.aiassistant/rules/AGENTS.md`

All Markdown relationship links inside `.aiassistant` MUST follow:

- `.aiassistant/rules/WIKILINK_RULES.md`

---

# 🚫 7. Forbidden Behaviors

The AI MUST NOT:

- assume missing context
- use outdated context
- ignore decisions
- bypass runbooks
- introduce architectural changes without approval
- mix responsibilities across components

---

# 🔍 8. Debugging Mode

- Identify root cause first.
- Do NOT patch blindly.
- Do NOT refactor unrelated code.
- Preserve existing behavior.

---

# ⚡ 9. Operating Mode

The AI must behave as:

- a senior engineer working in a production system

---

# 🧠 10. Context Generation And Evolution

Context must be managed as a structured, single source of truth.

## 10.1 Initialization

If `CURRENT_CONTEXT.md` does not exist:

- follow `.aiassistant/rules/CONTEXT_RULES.md`
- do NOT generate context from assumptions
- ask the user for the missing project definition
- create the file only after enough explicit information is available

## 10.2 Creation

Create initial context only when:

- the system is defined
- main flows are known
- integrations or constraints are known

## 10.3 Update

Once context exists:

- refactor the existing file
- do NOT append raw notes
- keep structure aligned with the template
- update it as the project evolves

## 10.4 Consistency

- context must reflect the current system
- context must NOT become a log

## 10.5 Relationship

- decisions -> why
- runbooks -> how
- checklists -> validation
- context -> current behavior

## 10.6 Forbidden

- multiple active context files
- outdated context
- mixed temporary notes
- ignored context rules

## 10.7 Living document

- keep it clean
- keep it aligned with reality
- refactor when needed

## 10.8 Guard

- Do NOT generate context without real project definition.
- Ask first when the information is incomplete.

---

# 🧩 11. Repository Governance

The repository MUST follow:

- `.aiassistant/rules/REPOSITORY_GUIDELINES.md`

This includes:

- when to create decisions
- when to update context
- when to create runbooks and checklists
- how the system evolves

---

# 🧠 12. Evolution System

Advanced layers:

- `feedback/` -> real-world input
- `roadmap/` -> planning
- `specs/` -> design before implementation
- `prompts/` -> operational behavior
- `templates/` -> reusable scaffolding for new artifacts

## Rules

- feedback may generate specs
- specs may generate decisions
- roadmap organizes execution
- templates accelerate creation but are NEVER a source of truth

---

# 🧠 Final Rule

If there is ANY doubt:

- ask before acting

---

END OF FILE
