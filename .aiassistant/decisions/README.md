# Architectural Decisions

This directory stores project decisions that affect architecture, runtime behavior, integrations, constraints, or long-term maintainability.

Decision files are the source of truth for **why** the system works in a specific way.

Related governance:

- [[CURRENT_CONTEXT]]
- [[WIKILINK_RULES]]

---

# When to create a decision

Create a decision when the project defines or changes:

- architecture boundaries
- integration strategy
- directory or file policies
- security or credential handling
- persistence or evidence retention rules
- dependency management strategy
- runtime constraints
- behavior that must not be changed casually

---

# When NOT to create a decision

Do NOT create a decision for:

- temporary notes
- debugging observations
- task lists
- small implementation details
- experiments not yet accepted
- information that belongs in `CURRENT_CONTEXT.md`

---

# File naming

Use numeric prefixes:

0001-directory-structure-policy.md  
0002-evidence-retention-policy.md  
0003-excel-processing-boundary.md  

Rules:

- use lowercase
- use kebab-case
- keep names descriptive
- never rename accepted decisions unless necessary

---

# Required structure

Each decision MUST follow this structure:

# Decision Title

## Status

Accepted | Proposed | Superseded

## Context

Explain the problem, constraint, or situation.

## Decision

Describe the chosen approach.

## Alternatives Considered

List relevant alternatives when applicable.

## Consequences

Describe trade-offs, benefits, risks, and maintenance impact.

## Related Files

Reference important files, modules, configs, or runbooks.

---

# Status meaning

## Proposed

The decision is under discussion and must not be treated as final.

## Accepted

The decision is active and must be followed.

## Superseded

The decision is historical and has been replaced by another decision.

When superseding a decision, reference the newer decision clearly.

---

# Evolution rule

Accepted decisions must be followed by default.

If a better approach is identified:

- do not override the decision silently
- explain the trade-off
- propose a new decision or mark the old one as superseded
- ask for explicit approval before changing implementation behavior

---

# Relationship with context

[[CURRENT_CONTEXT]] may summarize decisions, but must not replace them.

Use:

- decisions/ for why the rule exists
- [[CURRENT_CONTEXT]] for how the system currently behaves
- [[runbooks/README|runbooks guidance]] for how to execute operational procedures

---

END OF FILE
