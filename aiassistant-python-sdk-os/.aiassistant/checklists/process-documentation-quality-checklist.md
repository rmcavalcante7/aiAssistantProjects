# Process Documentation Quality Checklist

## Objective

Validate process and business-rule documentation when an SDK wraps operational
behavior.

## Current Behavior

- [ ] Documentation describes current behavior, not planned or historical
      behavior.
- [ ] Owning process or stage is clear.
- [ ] The SDK method or public capability that exposes the behavior is clear
      when applicable.

## Rules And Contracts

- [ ] Business rules document inputs, criteria, outputs, missing-data behavior,
      and operational effect when applicable.
- [ ] External systems document responsibilities and boundaries.
- [ ] Contracts document payloads, statuses, required fields, or schemas.
- [ ] Risks, manual steps, retries, fallbacks, or exceptions are documented when
      relevant.
- [ ] Evidence or validation expectations are documented when relevant.

## Navigation

- [ ] The process map links to affected notes.
- [ ] Wikilinks are meaningful and valid.
- [ ] Canvas files, when maintained, link back to Markdown notes.
- [ ] Markdown remains the source of truth.

## Governance Separation

- [ ] Documentation does not duplicate `.aiassistant` governance.
- [ ] Process docs do not replace `CURRENT_CONTEXT.md`.
- [ ] Delivery summary states whether process documentation changed.

## Related Files

- [[PROCESS_KNOWLEDGE_RULES]]
- [[update-process-knowledge-documentation]]
- [[0006-process-knowledge-documentation-lifecycle]]

