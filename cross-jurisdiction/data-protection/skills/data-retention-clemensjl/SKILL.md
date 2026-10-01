---
name: data-retention-clemensjl
title: Data retention and deletion
description: Use when deciding how long data may or must be kept, building a retention schedule, implementing a deletion or expiry job, answering an erasure request, or filling in the storage-period column of a privacy notice or ROPA. Also use when a table has no expiry at all, when logs, backups, warehouses or third-party tools hold copies nobody scheduled, when a TTL or lifecycle rule is about to be treated as proof of deletion, or before a processor engagement ends.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/data-retention
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
sources:
- title: Artefacts
  path: references/artefacts.md
- title: Backups
  path: references/backups.md
- title: Checklist
  path: references/checklist.md
- title: Copy Inventory
  path: references/copy-inventory.md
- title: Impl Databases
  path: references/impl-databases.md
- title: Impl Storage
  path: references/impl-storage.md
- title: Intake
  path: references/intake.md
- title: Legal Frame
  path: references/legal-frame.md
- title: Logs Telemetry
  path: references/logs-telemetry.md
- title: Minimum Periods
  path: references/minimum-periods.md
- title: Processors
  path: references/processors.md
- title: Schema Patterns
  path: references/schema-patterns.md
- title: Sector Overlays
  path: references/sector-overlays.md
---

# Data retention and deletion

Turning "we must delete data" into a schedule, a schema and a job that runs. Governing frame: GDPR Art 5(1)(e), 13(2)(a), 17, 18, 25, 28(3)(g), 30; national commercial and tax retention statutes (§ 147 AO, § 257 HGB, § 132 BAO, § 212 UGB, Code de commerce L123-22, art 2220 CC, Companies Act 2006 s 388); sector rules (PCI DSS v4.0.1, AML, health, telecom). Status as at 2026-08-05.

**Core principle:** retention is never one number. Every data element sits between a **minimum** imposed by commercial and tax law and a **maximum** imposed by Art 5(1)(e) storage limitation. Two different bodies set them, for opposite reasons, and neither knows about your schema. The engineering job is to resolve that interval **per data element** — not per table, and never per database. The second structural fact: an Art 17 erasure request does not beat a retention duty, because Art 17(3)(b) carves out processing "for compliance with a legal obligation which requires processing by Union or Member State law to which the controller is subject". The correct implementation is **restriction of processing under Art 18**, and almost no production schema can express that state.

## Not legal advice

This skill produces drafts, schedules and findings, not legal advice. Before anything goes live:

- Retention periods for accounting, tax, payroll, health, payments or AML data need sign-off from a tax adviser or lawyer for **each** jurisdiction of establishment. The periods here are the statutory floor, not a legal opinion on which of them binds you.
- Anything touching special categories (Art 9), children, or a processor chain across borders needs the DPO or external counsel.
- Every generated retention schedule, privacy-notice sentence and runbook carries `<!-- DRAFT - not legally approved -->` until the user confirms sign-off. Never remove the marker silently.

Never omit this section from the output and never soften it.

## Boundary to the legal-text skills

`legal-at`, `legal-de`, `legal-eu`, `legal-uk`, `legal-us`, `legal-au`, `legal-fr`, `legal-ch`, `legal-it` own the published texts — the privacy notice, imprint, terms. This skill owns the schedule and the machinery behind them, and hands those skills one finished sentence per processing activity for the storage-period field. It does not write the notice.

## Workflow

1. **Intake before anything else.** `references/intake.md`. Without the answers every period is a guess.
2. **Build the data-element inventory.** Element, not table. `customer.email` and `customer.tax_id` in the same row have different periods.
3. **Resolve the interval per element**: minimum from `references/minimum-periods.md` and `references/sector-overlays.md`, maximum from `references/legal-frame.md`. If minimum > maximum, the minimum wins and the element moves to restricted storage, not to deletion.
4. **Enumerate the copies.** `references/copy-inventory.md`. The failure mode is never the main table, it is the seventeenth copy.
5. **Choose the mechanism per copy.** `references/schema-patterns.md`, then `references/impl-databases.md` or `references/impl-storage.md` for the exact syntax.
6. **Produce the artefacts.** `references/artefacts.md`.
7. **Run the checklist.** `references/checklist.md`. It ends in a query that proves no row survives its period, not in a policy statement.

**Output shape.** Exactly four parts, in this order:

1. the artefact (schedule, runbook, job spec, design note), with the draft marker
2. the list of `[[MISSING: …]]` items the user must supply
3. adjacent open items, one sentence each
4. the sign-off note

The legal basis goes inline next to the claim it supports. Reference-file names are working material and appear in none of the four parts.

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| No retention schedule exists at all | Art 30(1)(f) envisaged time limits, Art 5(1)(e) | `legal-frame.md`, `artefacts.md` |
| Invoice, ledger, voucher, tax-relevant record | § 147 AO / § 257 HGB / § 132 BAO / § 212 UGB / L123-22 / art 2220 CC / s 388 CA 2006 | `minimum-periods.md` |
| Erasure request arrives, record is inside a retention duty | Art 17(3)(b) plus Art 18(1)(b)/(2) restriction | `legal-frame.md`, `artefacts.md` |
| Card data, PAN, CVV, track data | PCI DSS v4.0.1 Req 3.2.1, 3.3.1, 3.5.1 | `sector-overlays.md` |
| KYC file, sanctions hit, transaction monitoring | AML record-keeping duty of the jurisdiction | `sector-overlays.md` |
| Patient record, prescription, diagnosis | National health-record statute, never an EU period | `sector-overlays.md` |
| Access logs, audit trail, error traces, analytics events | Art 5(1)(e) against security and incident-response need | `logs-telemetry.md` |
| Backups, snapshots, PITR windows, WAL archives | Bounded window plus documented re-delete on restore | `backups.md` |
| Soft delete, tombstones, anonymisation, crypto-shredding | Art 4(5), Recital 26, EDPB Guidelines 02/2026 (draft) | `schema-patterns.md` |
| Concrete expiry in Postgres, Redis, MongoDB, DynamoDB | Vendor semantics differ; some TTLs only hide rows | `impl-databases.md` |
| Concrete expiry in S3, R2, BigQuery, Elasticsearch, Kafka | Delete markers, fail-safe windows and compaction defeat naive rules | `impl-storage.md` |
| Processor, sub-processor, SaaS tool holding a copy | Art 28(3)(g) delete-or-return at end of engagement | `processors.md` |
| Executing a subject erasure across the stack | Enumerate, delete, restrict, evidence | `copy-inventory.md`, `artefacts.md` |

## Hard rules

- **One period per data element, never one per database.** Art 30(1)(f) requires "the envisaged time limits for erasure of the different categories of data" — the plural is the point. A single `retention_days` constant applied to a whole schema is simultaneously too short for the tax-relevant columns and too long for everything else.
- **An erasure request does not defeat a retention duty, and a retention duty does not defeat an erasure request.** Art 17(3)(b) suspends erasure for the data the statute requires; Art 18(1)(b) and 18(2) then limit that data to storage plus "the establishment, exercise or defence of legal claims". Deleting the invoice is unlawful; continuing to send marketing from it is also unlawful. Build the third state.
- **`deleted_at IS NOT NULL` is not erasure.** The row is still personal data, still readable by any query that forgets the predicate, still in every index, replica, read model and nightly export. Soft delete is a UX feature; treat it as retention only when a hard-delete job is scheduled behind it.
- **German accounting vouchers are eight years, not ten, and Austria is seven.** § 147 Abs 3 Satz 1 AO: ten years for Abs 1 Nr 1 and 4a, **eight years for Buchungsbelege (Abs 1 Nr 4)**, six years for the rest; same split in § 257 Abs 4 HGB; § 14b Abs 1 UStG likewise eight years for invoices. In force from 01.01.2025 for every document whose period had not expired on 31.12.2024 (Art 97 § 19a Abs 2 EGAO). Credit institutions (§ 1 Abs 1b KWG), undertakings supervised under § 1 Abs 1 VAG and securities institutions (§ 2 Abs 1 WpIG) keep applying the 31.12.2024 version, i.e. ten years (Art 97 § 19a Abs 3 EGAO). Austria is seven years throughout (§ 132 Abs 1 BAO, § 212 Abs 1 UGB). Never copy a German number into an Austrian schedule.
- **Never store the card verification code.** PCI DSS v4.0.1 (current standard as at 05.08.2026), Requirement 3, prohibits retaining sensitive authentication data after authorisation — full track data, verification code and PIN block alike. Encryption is not an exception and "only in the debug log" is not an exception. This is the one period in the whole schedule that is zero.
- **On a versioned S3 bucket, `Expiration` does not delete anything.** It writes a delete marker; the object version becomes noncurrent and survives. Deletion needs `NoncurrentVersionExpiration` (with `NoncurrentDays` and, if set, `NewerNoncurrentVersions` both exceeded) plus `ExpiredObjectDeleteMarker` cleanup. Verified against the AWS S3 lifecycle examples documentation.
- **A TTL is a hint until the vendor says otherwise.** DynamoDB deletes expired items "typically within a few days after their expiration" and expired-but-undeleted items are still returned by Query and Scan unless you filter them out. MongoDB's TTL monitor runs every 60 seconds with no immediacy guarantee. Never publish a TTL value as the retention period in a privacy notice; publish the period the job enforces and monitor the lag.
- **Recovery windows resurrect deleted rows.** BigQuery keeps a 7-day time-travel window (configurable only between 2 and 7 days) followed by a 7-day fail-safe period that you cannot configure, cannot query and can only reach through Cloud Customer Care — up to 14 days after the DELETE. Postgres PITR, WAL archives and RDS automated backups do the same thing. The retention period you publish must be the outer envelope, not the moment the DML ran.
- **Every deletion job produces evidence.** Rows affected, oldest surviving timestamp, run time, failures. A job that runs silently is indistinguishable from a job that has been failing for eight months, and Art 5(2) puts the burden of demonstrating compliance on the controller.

## False friends

| Plausible wrong assumption | Actual position |
|---|---|
| "The GDPR says delete after N years" — from vendor blog posts and compliance SaaS marketing | The GDPR contains no retention period at all. Art 5(1)(e) is a necessity test: kept "no longer than is necessary for the purposes". The number always comes from somewhere else, or from your own documented reasoning. |
| "Accounting data is ten years, that is the German rule" — from pre-2025 templates | Eight years for Buchungsbelege since 01.01.2025 (§ 147 Abs 3 S 1 AO, Art 97 § 19a Abs 2 EGAO). Ten still applies to books, inventories, annual accounts, and to banks/insurers/securities institutions. |
| "Austria follows the German periods" | Seven years (§ 132 Abs 1 BAO, § 212 Abs 1 UGB), extended while a proceeding in which the undertaking is a party is pending. |
| "A right-to-erasure request means we delete everything" | Art 17(3)(b) excludes data held under a legal retention obligation. Restriction under Art 18 is the answer, not deletion and not silence. |
| "We anonymised it, so it is out of scope" | Recital 26 requires that the data subject is no longer identifiable by any means reasonably likely to be used. Hashing an id is pseudonymisation under Art 4(5), which stays personal data. EDPB Guidelines 02/2026 on anonymisation are in public consultation until 30.10.2026 and are not final — cite them as draft. |
| "Our processor handles deletion" | Art 28(3)(g) is a duty to delete or return at the **end of the engagement**. It is not a running retention control and it does not cover sub-processors you never enumerated. |
| "DELETE removed it from Postgres" | The tuple is dead but present until VACUUM, the change is in the WAL, the WAL is in the archive, the archive feeds PITR and replicas, and the base backup predates the DELETE. |
| "Setting a TTL on the Redis key is the retention control" | Keys without a TTL live forever, `SET` without `KEEPTTL` clears an existing TTL, and RDB/AOF files keep the value until rewrite. The TTL is one layer, not the control. |
| "Kafka retention.ms handles it" | Not on a compacted topic. `cleanup.policy=compact` retains the latest value per key indefinitely; the only removal is a tombstone (a record with a null payload) followed by compaction, and an empty `cleanup.policy` means infinite retention. |
| "The backup is out of scope because it is a backup" | It is processing. What is accepted is a bounded rotation window plus a documented, tested re-delete on restore — not an exemption. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| Retention policy written as a document, never as a job | Art 5(2) requires demonstrating compliance; a document nobody executes demonstrates the opposite |
| One `DELETE FROM events WHERE created_at < ...` over 400 million rows | Long lock, bloated WAL, replication lag, job killed halfway, no idempotence. Batch it or partition it |
| Anonymisation used as a substitute for deletion | Only lawful if identification is no longer reasonably possible; otherwise it is retention with extra steps |
| Privacy notice says "as long as necessary" | Art 13(2)(a) requires the period **or**, if that is impossible, the criteria used to determine it. "As long as necessary" is neither |
| ROPA time-limit column left empty or set to "n/a" | Art 30(1)(f) requires envisaged time limits where possible; blank is a finding in any audit |
| Deletion job has no monitoring | Silent failure is the default failure mode of a nightly cron |
| Erasure executed in the primary DB only | Warehouse, search index, cache, queue, analytics, error tracker, CRM, support desk and email provider each hold a copy |
| Object storage cleaned without checking versioning and soft-delete | Versioning, delete markers and provider soft-delete keep the bytes after the API returns success |
| Log lines treated as non-personal | A line carrying a user id, session id or IP address is personal data; the retention period applies to it |
| Retention interval measured from row creation for tax records | The statutory periods run from the end of the calendar year of the last entry or of issue, not from `created_at` |

## Reference files

- `references/intake.md` — questionnaire to run before any period is stated
- `references/legal-frame.md` — Art 5(1)(e), 13(2)(a), 17, 18, 25, 30; minimum/maximum resolution; the CNIL three-phase model
- `references/minimum-periods.md` — statutory floors per jurisdiction with citations
- `references/sector-overlays.md` — payment, health, AML, telecom, CCTV, employment
- `references/logs-telemetry.md` — security, application and analytics logs; IP handling; NIS2 pull
- `references/backups.md` — rotation windows, PITR, WAL, versioning, soft delete, restore-and-re-delete
- `references/schema-patterns.md` — soft vs hard delete, tombstones, anonymisation, crypto-shredding, partitioning
- `references/impl-databases.md` — Postgres batched deletes, pg_cron, Redis, MongoDB, DynamoDB
- `references/impl-storage.md` — S3, R2, BigQuery, Elasticsearch/OpenSearch, Kafka
- `references/processors.md` — Art 28(3)(g), sub-processors, cascading deletion
- `references/copy-inventory.md` — the copy-inventory worksheet
- `references/artefacts.md` — schedule, ROPA column, notice sentence, erasure runbook, restriction design note, job spec
- `references/checklist.md` — pre-ship checklist ending in verifiable assertions
