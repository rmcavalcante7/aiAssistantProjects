# Generate Project README

This runbook defines how to generate a high-quality `README.md` adapted to the type of project.

There are TWO supported README types:

1. Product README (SDK, library, public repo)
2. Operational README (automation, RPA, internal system)

The correct type MUST be selected before generation.

Important:

- Product README is for installable packages, libraries, SDKs, and public repositories.
- Operational README is for automations, RPAs, internal workers, and integration systems.
- The examples below are structural examples, not mandatory filenames.

---

# 🧠 Objective

Generate a README that:

- reflects the real system
- is structured and consistent
- is useful for onboarding and maintenance
- matches the project type

---

# 📌 Step 1 - Identify project type

Determine the project category:

## Product README (use when):

- SDK
- Python package
- reusable library
- public/open-source project

## Operational README (use when):

- automation (RPA)
- internal system
- integration pipeline
- job/worker/loop-based system

If unclear:

→ Ask the user before proceeding

---

# 🧱 PRODUCT README STRUCTURE

Use this structure for SDKs and libraries.

## 1. Branding

- Logo (optional)
- Badges (CI, version, docs, license)
- Project name

## 2. Overview

- What the project is
- What it does
- Positioning

## 3. Why it exists

- Problem solved
- Limitations of alternatives
- Value proposition

## 4. Installation

```bash
pip install package-name
```

## 5. Quick Start

Minimal working example:

- import
- usage
- output

## 6. Public API Surface

- main entrypoint
- exposed modules/services
- high-level usage

## 7. Core Capabilities

- grouped features
- short explanation
- examples

## 8. Advanced Features (optional)

- extensibility
- configuration
- performance features

## 9. Documentation Links

- docs
- examples
- repo

## 10. Tests

- how tests are structured
- how to run

## 11. Status / Roadmap (optional)

## 12. License

---

# 🧱 OPERATIONAL README STRUCTURE

Use this for automations and internal systems.

## 1. Project Description

- what the automation does
- high-level responsibilities

## 2. Flow Overview

Example:

<entrypoint>  
-> orchestrator  
-> services  

## 3. What the system does (step-by-step)

1. read input
2. process data
3. generate output
4. send data
5. update system

## 4. Architecture

- entrypoints
- orchestrator
- services
- integrations

## 5. Integrations

- external systems (APIs, Pipefy, DBs)
- libraries used
- important configs

## 6. Data Flow / Processing

- pipelines
- transformations
- rules

## 7. Operational Directories

- input
- output
- temp
- logs
- errors

## 8. Credentials & Security

- how credentials are stored
- how to initialize them
- what NOT to do

## 9. Configuration

- environment variables
- config files

## 10. Execution

```bash
python <entrypoint>.py
```

## 11. Validation / Testing

- how to test locally
- test directories

## 12. Logging

- log strategy
- file structure

## 13. Performance Notes

- known bottlenecks
- decisions already made

## 14. Important Decisions

- constraints
- business rules
- what must NOT change

## 15. Known Limitations

## 16. Future Improvements

---

# 🎯 Quality Rules

The README MUST:

- reflect CURRENT system behavior
- be aligned with CURRENT_CONTEXT.md
- be concise but complete
- avoid duplication
- avoid outdated information

---

# ⚠️ Non-regression Rules

- Do NOT remove core sections
- Do NOT break examples
- Do NOT include outdated flows
- Do NOT mix product and operational styles

---

# 🔍 Validation

Before finalizing:

- examples run correctly
- commands are valid
- structure matches project type
- no broken links
- no missing sections

---

# 🧠 Key Principle

README is:

→ the entry point of the system  
→ the contract for understanding it  

---

END OF FILE
