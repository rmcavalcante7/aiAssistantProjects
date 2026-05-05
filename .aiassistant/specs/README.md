# Specs

This directory stores detailed implementation specifications for approved changes.

Specs are created before implementing complex or impactful changes.

Related governance:

- [[feedback/README|feedback guidance]]
- [[decisions/README|decisions guidance]]
- [[roadmap/README|roadmap guidance]]
- [[checklists/README|checklists guidance]]
- [[WIKILINK_RULES]]

---

# 🧠 Objective

Provide a clear and structured design before implementation.

---

# 📌 When to create a spec

Create a spec when:

- modifying public APIs
- introducing new flows
- changing architecture
- implementing complex features
- resolving critical feedback

---

# 📄 File structure

One spec per change area.

Example:

transport-retry-spec.md

---

# 🧱 Required structure

Each spec MUST follow this structure:

# Spec Title

## Status

- draft
- approved
- implemented

## Problem

Clear description of the issue.

## Context

Relevant background and constraints.

## Decision

Chosen solution.

## Scope

What is included and what is NOT included.

## Compatibility

Impact on existing behavior.

## Implementation Notes

Technical considerations.

## Tests

How the change will be validated.

---

# 🔄 Relationship with other components

- specs are derived from [[feedback/README|feedback]]
- specs may lead to [[decisions/README|decisions]]
- specs feed [[roadmap/README|roadmap]]

---

# 🧠 Key Principle

A spec defines **how a change will be implemented before coding begins**.

---

END OF FILE
