# Prompts

This directory stores reusable prompts for recurring SDK work.

Prompts are operational tools. They do not replace context, decisions, runbooks,
or checklists.

## When To Create A Prompt

Create a prompt when:

- a workflow repeats frequently;
- output format must be controlled;
- release or implementation behavior must be standardized;
- an agent task requires strict role and validation guidance.

Do not create prompts for one-off reminders.

## Prompt Requirements

Each prompt should define:

- role;
- objective;
- required inputs;
- rules;
- expected output;
- validation expectations.

## Available Prompts

- [[python-sdk-implementation-prompt]]
- [[python-sdk-release-prompt]]

Use prompts together with:

- [[CURRENT_CONTEXT]]
- [[decisions/README|decisions guidance]]
- [[runbooks/README|runbooks guidance]]
- [[checklists/README|checklists guidance]]

