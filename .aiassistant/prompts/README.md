# Prompts

This directory stores reusable, project-specific prompts.

Prompts define how the AI should behave in specific scenarios.

Related governance:

- [[CURRENT_CONTEXT]]
- [[decisions/README|decisions guidance]]
- [[runbooks/README|runbooks guidance]]
- [[WIKILINK_RULES]]

---

# 🧠 Objective

Provide consistent, high-quality instructions for recurring tasks.

---

# 📌 When to create a prompt

Create a prompt when:

- a task is repeated frequently
- a workflow requires strict rules
- behavior must be standardized
- output format must be controlled

Examples:

- release process
- code generation
- debugging flows
- documentation generation

---

# 📄 File structure

One prompt per use case.

Example:

release-prompt.md

---

# 🧱 Prompt guidelines

Each prompt should:

- define a clear role
- define clear objectives
- define strict rules
- define expected output format

---

# 🔄 Relationship with other components

- prompts may use:
  - [[CURRENT_CONTEXT]]
  - [[decisions/README|decisions]]
  - [[runbooks/README|runbooks]]

- prompts must reflect:
  - current system behavior
  - current architecture

---

# ⚠️ Rules

- avoid generic prompts
- avoid vague instructions
- keep prompts aligned with the project
- update prompts when system behavior changes

---

# 🧠 Key Principle

Prompts are **operational tools**, not documentation.

---

END OF FILE
