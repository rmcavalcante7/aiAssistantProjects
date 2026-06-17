# Specs

This directory stores implementation specs for SDK changes.

Specs define how a change will be implemented before coding begins.

## When To Create A Spec

Create a spec before:

- changing public API;
- changing package structure;
- changing release behavior;
- adding or changing external integration behavior;
- adding transport, retry, auth, or error semantics;
- introducing a new public domain namespace;
- changing public models, configuration objects, or exception taxonomy;
- adding behavior that requires live integration validation.

## Required Structure

Each spec should include:

- problem;
- context;
- decision;
- public API direction;
- scope;
- compatibility;
- implementation notes;
- tests;
- documentation impact.

## SDK Compatibility Rule

Every spec that touches public API must state whether the change is:

- additive;
- behavior-preserving internal change;
- deprecation;
- breaking change.

Breaking changes require explicit approval and migration guidance.

## Done Rule

A spec is not implemented until:

- code is changed;
- tests are updated;
- docs/examples are updated when public behavior changed;
- context is updated if current reality changed;
- release notes or changelog impact is known.

Related files:

- [[0003-sdk-public-api-compatibility-policy]]
- [[sdk-public-api-compatibility-checklist]]
- [[sdk-template-consolidation-from-pipebridge]]

