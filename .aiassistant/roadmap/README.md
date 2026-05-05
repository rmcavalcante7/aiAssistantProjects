# Roadmap

This directory stores release-oriented planning files.

Each roadmap represents a planned or in-progress release.

Related governance:

- [[feedback/README|feedback guidance]]
- [[specs/README|specs guidance]]
- [[decisions/README|decisions guidance]]
- [[WIKILINK_RULES]]

---

# 🧠 Objective

Define:

- what will be built
- in which order
- under which constraints
- with clear validation criteria

---

# 📌 When to create a roadmap

Create a roadmap when:

- planning a new release
- grouping multiple related changes
- organizing implementation phases
- defining delivery scope

---

# 📄 File structure

One roadmap file per release.

Example:

v0.2.0-roadmap.md

---

# 🧱 Required structure

Each roadmap MUST follow this structure:

# Roadmap <version>

## Status

- planned
- in progress
- completed

## Objective

What this release aims to achieve.

## Scope

List of features or changes included.

## Principles

Rules that must guide the implementation:

- backward compatibility
- safety
- simplicity
- etc.

## Phases

Break down implementation into phases:

### Phase X - Name

- goal
- expected outputs
- acceptance criteria

## Validation

How the release will be validated:

- tests
- manual checks
- production validation

## Deliverables

- code
- documentation
- release artifacts

## Future Radar

Items intentionally NOT included in this release.

---

# 🔄 Relationship with other components

- roadmap is fed by [[feedback/README|feedback]]
- roadmap may generate [[specs/README|specs]]
- roadmap execution may produce [[decisions/README|decisions]]

---

# 🧠 Key Principle

A roadmap defines **what will be built and why**, not how.

---

END OF FILE
