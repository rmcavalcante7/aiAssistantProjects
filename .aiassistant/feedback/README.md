# Feedback

This directory stores structured feedback collected during the usage of the system.

Feedback is the starting point for:

- improvements
- bug fixes
- new features
- architectural evolution

Related governance:

- [[specs/README|specs guidance]]
- [[decisions/README|decisions guidance]]
- [[roadmap/README|roadmap guidance]]
- [[WIKILINK_RULES]]

---

# 🧠 Objective

Capture real-world problems in a structured and reusable format.

---

# 📌 When to create feedback

Create a feedback entry when:

- a limitation is identified
- a bug or inconsistency appears
- a repeated pain point is observed
- a missing feature becomes evident
- a workaround is required

---

# 📄 File structure

Each feedback must be stored in a separate file.

Example:

2026-04-10-transport-retry.md

---

# 🧱 Required structure

Each feedback file MUST follow this format:

# Feedback Title

## Date

YYYY-MM-DD

## Status

- new
- under evaluation
- accepted
- rejected
- implemented

## Priority

- low
- medium
- high

## Problem

Clear description of the issue.

## Impact

Explain why this matters:

- user experience
- reliability
- performance
- maintainability

## Recommendation

Proposed solution or direction.

## Notes

Optional additional context.

---

# 🔄 Relationship with other components

- Accepted feedback may generate:
  - a [[specs/README|spec]] (detailed design)
  - a [[decisions/README|decision]] (if architectural)
  - a [[roadmap/README|roadmap]] item (if planned work)

---

# 🧠 Key Principle

Feedback is not implementation.

It is **input for decision-making**.

---

END OF FILE
