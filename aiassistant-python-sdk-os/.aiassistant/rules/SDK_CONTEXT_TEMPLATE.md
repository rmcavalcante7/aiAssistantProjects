---
apply: always
---

# SDK Context Template

Use this template only when creating the initial active context for a real
Python SDK project.

Do not leave placeholders in the finished context.

## 1. Project Overview

Describe what the SDK is, what problem it solves, and who uses it.

## 2. Package Identity

Document:

- package name;
- import name;
- repository URL;
- documentation URL if known;
- PyPI/project registry target if known.

## 3. Public API

Document:

- top-level public imports;
- facade or main client;
- domain namespaces;
- public configuration objects;
- public models and exceptions;
- compatibility constraints.

## 4. Architecture

Describe package layers such as:

- transport/client;
- service/domain logic;
- models;
- facade;
- exceptions;
- utilities;
- workflow or policies when needed.

## 5. Integrations

Document external APIs, authentication, environment variables, endpoints,
credentials, and sandbox/live boundaries.

## 6. Testing Strategy

Document:

- unit tests;
- functional tests;
- integration tests;
- destructive/live test rules;
- required environment variables.

## 7. Documentation

Document README, Sphinx docs, examples, use cases, and publishing rules.

## 8. Release And Publication

Document:

- versioning strategy;
- release branch or Git flow;
- CI workflows;
- PyPI publication;
- GitHub Release behavior;
- required secrets.

## 9. Business Or Process Knowledge

If the SDK wraps process-heavy behavior, link to the process knowledge map.

If not applicable, state that no process knowledge root is active.

## 10. Known Risks / Limitations

List operational, API, compatibility, documentation, or release risks.

## 11. Next Steps / Priorities

List current implementation or release priorities.

## Rules

- This file must reflect current reality.
- Do not use templates, old context, or reference projects as active context.
- Update this file after meaningful SDK behavior, API, or release changes.

