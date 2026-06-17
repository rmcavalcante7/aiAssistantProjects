# Feedback

This directory stores structured feedback from real SDK usage.

Feedback is input for decision-making. It is not implementation and it is not a
task log.

## When To Create Feedback

Create feedback when:

- a user hits a public API gap;
- packaging or installation fails;
- documentation is misleading;
- integration behavior is fragile;
- release or PyPI behavior regresses;
- a workaround starts repeating;
- SDK behavior differs from the wrapped system in a surprising way.

## Required Structure

Each feedback file should include:

- date;
- status;
- priority;
- problem;
- impact;
- recommendation;
- notes.

## Status Values

Use:

- new;
- under evaluation;
- accepted;
- rejected;
- implemented.

## SDK-Specific Guidance

Good SDK feedback identifies:

- affected public API;
- affected user workflow;
- compatibility risk;
- docs/examples gap;
- expected behavior;
- observed behavior.

Accepted feedback may generate:

- [[specs/README|specs guidance]];
- [[roadmap/README|roadmap guidance]];
- [[decisions/README|decisions guidance]].

