# Process Documentation Quality Checklist

## Objective

Validate that process and business-rule documentation is accurate, navigable,
and aligned with the implementation.

## When to use

Use this checklist before finishing a development task that updates or should
update project process knowledge.

Related governance:

- [[PROCESS_KNOWLEDGE_RULES]]
- [[update-process-knowledge-documentation]]
- [[0003-process-knowledge-documentation-lifecycle]]

## Items

- [ ] The documentation describes current behavior, not planned or historical
      behavior.
- [ ] The owning process or stage is clear.
- [ ] Changed business rules document inputs, criteria, outputs, missing-data
      behavior, and operational effect when applicable.
- [ ] Changed external system interactions document the system responsibility
      and integration boundary.
- [ ] Changed contracts document payloads, files, statuses, required fields, or
      schemas at the right level of detail.
- [ ] New or changed risks, manual steps, retries, fallbacks, or exceptions are
      documented when relevant.
- [ ] The central process map links to new process areas, systems, rules,
      contracts, or risks.
- [ ] Wikilinks represent meaningful relationships and do not create graph
      noise.
- [ ] Wikilinks are valid or intentionally marked as pending in draft notes.
- [ ] Canvas files, when maintained, are consistent with the Markdown source of
      truth.
- [ ] The documentation does not duplicate `.aiassistant` governance content.
- [ ] The delivery summary states whether process documentation was updated or
      why no update was required.

## Notes

This checklist validates documentation quality. It does not define the process
itself and does not replace implementation tests.
