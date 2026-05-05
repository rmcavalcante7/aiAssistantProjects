---
apply: always
---

# Project Context Template

This file defines how the CURRENT_CONTEXT.md must be structured.

It MUST be followed when creating or updating project context.

---

# 🧠 1. PROJECT OVERVIEW

* What the system does
* Main purpose
* Business value

---

# 🧱 2. SYSTEM ARCHITECTURE

* High-level architecture (layers)
* Main components
* Data flow

---

# 🔌 3. INTEGRATIONS

List all external integrations:

* APIs
* Services
* SDKs
* External systems

For each:

* Purpose
* Critical constraints
* Known issues (if any)

---

# 📂 4. PROJECT STRUCTURE

* Key directories
* Responsibility of each layer/module

---

# ⚙️ 5. CORE FLOWS

Describe the main flows of the system:

Example:

* File processing flow
* API processing flow
* Automation loop

Each flow should include:

* Input
* Processing
* Output

---

# 🧠 6. BUSINESS RULES

* Critical rules that define system behavior
* Constraints that MUST NOT be violated

---

# 🧱 7. ARCHITECTURAL DECISIONS (SUMMARY)

* Summarize key decisions from `/decisions/`
* Do NOT duplicate full content
* Only list what impacts execution

---

# 🚨 8. KNOWN RISKS / LIMITATIONS

* Technical limitations
* Known fragile points
* Performance bottlenecks

---

# 🔄 9. CURRENT STATE

* What is already working
* What was recently validated
* Stability level

---

# 🎯 10. NEXT STEPS / PRIORITIES

* What should be done next
* Current focus of development

---

# 📌 RULES

* Be concise, but complete
* Avoid duplication with decisions
* Prefer clarity over verbosity
* Update this file whenever the system evolves
* This is the ONLY valid runtime context

---

END OF FILE
