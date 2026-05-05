# Example CURRENT_CONTEXT.md For An Automation Project

This file is a fictitious example created only as a reference.

It is NOT an active runtime context.

It MUST NOT be treated as the source of truth for any real project.

It MUST NOT be moved to `.aiassistant/project_context/CURRENT_CONTEXT.md` without full adaptation to a real system.

---

# 🧠 1. PROJECT OVERVIEW

The system automates supplier invoice intake for an internal finance operation.

Its main purpose is to reduce manual work in the accounts payable team by collecting invoices from email, validating required metadata, storing the files in an internal repository, and notifying the finance team when manual review is needed.

Business value:

- reduces repetitive manual triage
- shortens invoice processing lead time
- improves consistency of file naming and validation
- creates traceability for received documents

---

# 🧱 2. SYSTEM ARCHITECTURE

High-level architecture:

- entrypoint layer
- orchestration layer
- service layer
- integration layer
- persistence and logging layer

Main components:

- `invoiceIntakeLoop`: scheduled entrypoint that runs the automation cycle
- `invoiceOrchestrator`: coordinates the end-to-end flow
- `emailService`: fetches unread messages and attachments
- `documentValidationService`: validates naming, metadata, and required fields
- `storageService`: saves accepted files to the internal repository
- `notificationService`: sends alerts for manual review
- `auditRepository`: records execution events and outcomes

Data flow:

1. read unread invoice emails
2. extract attachments and sender metadata
3. validate file type and required invoice information
4. classify invoice as accepted, rejected, or manual review
5. store accepted files and register audit data
6. notify finance team when review is required

---

# 🔌 3. INTEGRATIONS

## Microsoft 365 Mailbox

- Purpose: source of incoming supplier invoices
- Critical constraints:
  - mailbox credentials must come from environment-specific secret storage
  - the automation must not delete emails during initial processing
- Known issues:
  - some suppliers send malformed attachments or images instead of PDFs

## Internal File Repository

- Purpose: store accepted invoice files in a standardized folder structure
- Critical constraints:
  - destination path must be deterministic
  - duplicate filenames must be handled safely
- Known issues:
  - occasional latency during peak hours

## Team Notification Channel

- Purpose: alert the finance team when an invoice needs manual review
- Critical constraints:
  - notifications must include invoice identifier, sender, and reason
  - avoid duplicate alerts for the same invoice in the same execution cycle
- Known issues:
  - rate limiting may delay bursts of notifications

## Relational Database

- Purpose: persist execution audit logs and document processing status
- Critical constraints:
  - writes must be idempotent for retry scenarios
  - execution failures must remain traceable
- Known issues:
  - connection pool exhaustion can happen if retries are uncontrolled

---

# 📂 4. PROJECT STRUCTURE

Key directories:

- `src/entrypoints/`: scheduled jobs and CLI entrypoints
- `src/orchestrators/`: end-to-end automation coordination
- `src/services/`: business services and validation logic
- `src/integrations/`: mailbox, storage, database, and notification clients
- `src/models/`: DTOs and domain models
- `src/config/`: configuration loading and environment mapping
- `src/utils/`: helper utilities with limited scope
- `logs/`: runtime logs
- `tests/`: unit and integration tests

Responsibilities:

- entrypoints trigger the flow
- orchestrators define execution order
- services contain domain behavior
- integrations isolate external systems
- models standardize data exchanged across layers

---

# ⚙️ 5. CORE FLOWS

## Email invoice intake flow

Input:

- unread emails from the finance mailbox
- attachments and sender metadata

Processing:

- fetch candidate emails
- extract supported attachments
- normalize sender and subject data
- map raw inputs into internal document models

Output:

- a list of invoice intake candidates ready for validation

## Invoice validation flow

Input:

- normalized invoice candidate
- attachment content

Processing:

- verify supported extension
- validate required metadata
- detect duplicate invoice identifiers
- classify as accepted, rejected, or manual review

Output:

- validated invoice result with status and reason

## Storage and notification flow

Input:

- validated invoice result

Processing:

- persist accepted invoice files
- write audit data
- notify finance team when review is needed

Output:

- stored files
- audit records
- review notifications

---

# 🧠 6. BUSINESS RULES

- Only PDF invoices are accepted automatically.
- Missing supplier identifier forces manual review.
- Duplicate invoice number from the same supplier in the same month must not be auto-approved.
- The automation must never overwrite an existing accepted invoice file silently.
- Rejected invoices must remain auditable even when no file is stored.
- Notification messages must explain the review reason in operational language.

---

# 🧱 7. ARCHITECTURAL DECISIONS (SUMMARY)

- External systems are accessed only through the integration layer.
- Orchestrators coordinate flow but do not contain low-level API logic.
- Validation logic remains in services, not in entrypoints.
- Audit persistence is mandatory for every processed invoice candidate.
- Credentials are loaded from environment-aware configuration, never hardcoded.

---

# 🚨 8. KNOWN RISKS / LIMITATIONS

- OCR is not implemented, so image-only invoices require manual review.
- Supplier-specific exceptions are still handled by generic rules, which may increase false positives.
- Mailbox bursts may increase execution time significantly.
- Downstream repository latency can cause partial flow slowdown.

---

# 🔄 9. CURRENT STATE

- The end-to-end happy path is implemented for PDF invoices with valid metadata.
- Audit logging has been validated in a development environment.
- Manual review notifications are working for the most common validation failures.
- Stability level: early operational baseline, suitable for controlled internal rollout but not yet hardened for high-volume intake.

---

# 🎯 10. NEXT STEPS / PRIORITIES

- Add supplier-specific validation exceptions where business rules are stable.
- Improve duplicate detection resilience.
- Add retry strategy for transient integration failures.
- Create a release checklist for internal deployment.
- Define decision records for repository path policy and notification deduplication.

---

# 📌 EXAMPLE NOTE

This file exists only to demonstrate what a filled `CURRENT_CONTEXT.md` can look like for a fictional automation project.

For a real project:

- use this file only as inspiration
- adapt every section to the real system
- do not copy fictitious rules, flows, or integrations into active context
