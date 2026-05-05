# Bootstrap Project Context

This runbook defines how to create the first `CURRENT_CONTEXT.md` for a project that does not have active context yet.

It exists to prevent the AI from inventing system behavior during project setup.

---

# Objective

Create an initial `CURRENT_CONTEXT.md` that is:

- based on explicit information
- aligned with the real project
- useful enough to guide implementation without guesswork

---

# When to use

Use this runbook when:

- a project is starting from this template
- `.aiassistant/project_context/CURRENT_CONTEXT.md` does not exist
- the user wants to initialize project context

Do NOT use it to update an existing context file.

---

# Preconditions

Before execution:

- the user has agreed to initialize project context
- there is enough explicit information to describe the project at a high level

If the information is still missing:

- pause
- ask follow-up questions
- do NOT create the file yet

---

# Inputs

Collect at least the following:

- project overview
- project type
- main flows
- known integrations
- important constraints

Optional inputs:

- initial directory structure
- known business rules
- known risks or limitations
- initial priorities

---

# Steps

## Step 1 - Confirm context is missing

Verify that `.aiassistant/project_context/CURRENT_CONTEXT.md` does not exist.

If it already exists:

- stop this runbook
- update the existing file instead of creating a new one

## Step 2 - Classify the project

Determine the project profile:

- automation or RPA
- API or service
- integration system
- data pipeline
- reusable library or package

If unclear:

- ask the user before proceeding

## Step 3 - Gather minimum viable context

Ask progressive questions until the following are known:

- what the system does
- what problem it solves
- its main inputs
- its main outputs
- the core processing steps
- external systems involved
- relevant constraints

Do NOT ask every possible question if the project is still exploratory.

## Step 4 - Draft the context file

Create `.aiassistant/project_context/CURRENT_CONTEXT.md` using:

- `.aiassistant/rules/CONTEXT_TEMPLATE.md`

Rules:

- do not leave placeholders
- do not invent unknown flows
- do not copy historical notes into active context
- keep the text concise and operational

## Step 5 - Validate the draft

Confirm that the draft:

- reflects explicit user-provided information
- separates runtime behavior from architectural decisions
- does not include speculative content
- is understandable enough to guide implementation

## Step 6 - Identify follow-up artifacts

If the bootstrap reveals stable rules or repeatable processes, create follow-up artifacts as needed:

- `decisions/` for accepted constraints
- `runbooks/` for repeatable execution
- `checklists/` for critical validation
- `roadmap/` for phased delivery
- `specs/` for complex changes

Use `.aiassistant/templates/` when a starter file is helpful.

---

# Validation

Before finalizing:

- `CURRENT_CONTEXT.md` exists
- all sections are grounded in explicit information
- there are no placeholders
- there is no duplicated source of truth
- the context is sufficient to start work safely

---

# Outputs

Expected outputs:

- `.aiassistant/project_context/CURRENT_CONTEXT.md`

Optional outputs:

- starter decision files
- a first checklist
- a roadmap or spec draft

---

# Failure scenarios

## Not enough information

Do NOT create the context file.

Ask only the missing questions required to continue.

## Conflicting information

Pause and clarify the conflict before writing the file.

## User is still exploring

Keep the interaction progressive and light.

Do not force a full system definition too early.

---

# Notes

- This runbook creates the initial context only.
- After the file exists, future changes must update the same file instead of creating alternatives.
- Templates are helpers; the final file must reflect the actual project.
