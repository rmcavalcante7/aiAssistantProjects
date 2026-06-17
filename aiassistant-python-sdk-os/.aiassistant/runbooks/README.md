# Runbooks

This directory stores executable procedures.

Runbooks define how to perform repeatable SDK tasks. They are not architectural
decisions and they are not general explanations.

## When To Create A Runbook

Create a runbook when:

- a task must be executed consistently;
- release or publication has multiple steps;
- validation must happen in a specific order;
- SDK setup is repeated across repositories;
- documentation generation has operational requirements;
- integration tests require controlled setup.

Do not create a runbook for:

- one-off notes;
- architectural rationale;
- temporary debugging observations;
- validation-only lists.

## Required Shape

Each runbook should include:

- objective;
- when to use;
- preconditions;
- inputs;
- steps;
- validation;
- outputs;
- failure scenarios or notes when relevant.

## Execution Rule

When a runbook exists for the task, follow it step by step.

If the runbook is wrong or incomplete, do not improvise silently. Identify the
gap, update the runbook if the process changed, and explain the change.

## Common SDK Runbooks

- [[bootstrap-python-sdk-context]]
- [[setup-python-sdk-repository]]
- [[generate-sdk-readme]]
- [[generate-pyproject-runbook]]
- [[setup-sphinx-docs]]
- [[validate-sdk-quality-gates]]
- [[prepare-sdk-release]]
- [[validate-wikilinks]]
- [[use-obsidian-knowledge-graph]]
- [[update-process-knowledge-documentation]]

## Relationship With Other Components

- decisions explain why constraints exist;
- specs define how a change will be implemented;
- runbooks execute procedures;
- checklists validate outcomes;
- context describes current reality.

