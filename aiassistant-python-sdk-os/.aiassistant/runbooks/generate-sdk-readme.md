# Generate SDK README

## Objective

Create or update a README suitable for GitHub and package-registry users.

For public packages, README quality directly affects SDK adoption and PyPI
rendering.

## When To Use

Use when:

- starting a new SDK;
- public API changes;
- installation or release behavior changes;
- authentication/configuration behavior changes;
- PyPI rendering has changed;
- docs or examples are reorganized.

## Preconditions

- Active context exists.
- Package identity is known.
- Public entrypoint is known.
- Installation strategy is known.

## Inputs

- Package name.
- Import name.
- Install command.
- Quick start example.
- Public API summary.
- Authentication/configuration model.
- Documentation URL.
- Repository URL.
- License and author details.
- Asset URLs for logos or badges.

## Required Sections

Include:

- project name;
- badges;
- short overview;
- installation;
- quick start;
- public API surface;
- configuration/authentication;
- examples;
- documentation links;
- development commands;
- testing commands;
- release/versioning note when useful;
- license.

## Steps

1. Confirm package name and import name from context.
2. Use [[readme-sdk-template]] as a starting point.
3. Replace all placeholders.
4. Ensure examples use public API only.
5. Use public URLs for PyPI-facing images.
6. Keep badges intentional and stable.
7. Link docs, examples, changelog, and repository.
8. Explain integration limitations and retry/destructive behavior when relevant.
9. Apply [[sdk-documentation-quality-checklist]].

## Validation

- README matches current context.
- Quick start is realistic.
- Install command matches `pyproject.toml`.
- PyPI-facing assets are public.
- No stale project names remain.
- Public API examples match tests where possible.
- Links are current.

## Failure Scenarios

### Logo Does Not Render On PyPI

Use a public absolute URL instead of a local relative path.

### Quick Start Uses Internals

Rewrite examples to use top-level imports and facade/client methods.

### README And pyproject Disagree

Fix package name, readme path, URLs, and install command before release.

## Outputs

- Updated `README.md`.

## Related Files

- [[0005-sdk-documentation-and-examples-policy]]
- [[sdk-documentation-quality-checklist]]
- [[prepare-sdk-release]]

