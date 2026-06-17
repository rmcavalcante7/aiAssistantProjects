# Roadmap

This directory stores release-oriented SDK planning.

A roadmap defines what will be built and why. It does not replace specs,
decisions, runbooks, or checklists.

## When To Create A Roadmap

Create a roadmap when:

- planning a release;
- grouping related SDK changes;
- sequencing public API work;
- coordinating docs, tests, and release work;
- preserving future-radar items without implementing them now.

## Required Structure

Each roadmap should define:

- status;
- objective;
- scope;
- principles;
- phases;
- validation;
- deliverables;
- future radar.

## SDK-Specific Requirements

SDK roadmaps must explicitly call out:

- public API impact;
- backward compatibility impact;
- docs/examples impact;
- packaging or release impact;
- integration-test requirements;
- versioning expectations.

## Scope Discipline

Do not smuggle future-radar items into the current release.

If a roadmap item changes public API or architecture, create a spec before
implementation.

Related files:

- [[feedback/README|feedback guidance]]
- [[specs/README|specs guidance]]
- [[sdk-release-checklist]]

