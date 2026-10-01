---
name: design-data-retention-jeffreytse
title: Design Data Retention
description: Use when establishing or reviewing a data retention and deletion policy for personal or business data
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/privacy/skills/design-data-retention
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
tags: [law, privacy, data-retention, gdpr, iso-27001, legal-hold, storage-limitation]
---

# Design Data Retention

Establish a legally defensible data retention schedule that balances regulatory minimization obligations with legal hold and business requirements.

## Why This Is Best Practice

**Adopted by:** ISO/IEC 27001, GDPR supervisory authorities, ARMA International (information governance), legal departments globally
**Impact:** GDPR storage limitation violations carry significant fines; conversely, deletion of data subject to legal hold constitutes spoliation (destruction of evidence) with severe litigation consequences including adverse inference jury instructions; a documented retention schedule is the only way to satisfy both obligations simultaneously.

**Why best:** Data retention sits at the intersection of privacy law (minimize), records law (retain certain records), and litigation law (legal hold). Without a formal retention schedule, organizations either retain everything forever (GDPR violation) or delete too aggressively (spoliation risk). A properly designed schedule navigates both hazards.

## Steps

1. **Inventory all data categories** — Map every type of data held: customer personal data, employee records, financial records, contracts, communications, audit logs, marketing data, product usage data; document format, location, and volume.
2. **Identify applicable retention obligations** — For each data category, identify the legal minimum retention period imposed by regulation: financial records (IRS/HMRC: 7 years), employee records (FLSA: 3 years payroll, OSHA: 30 years exposure records), contracts (statute of limitations + 2 years), tax records (7 years), healthcare records (HIPAA: 6 years), corporate records (state law, often perpetual for board minutes).
3. **Apply the GDPR storage limitation principle** — Personal data must not be kept longer than necessary for its specified purpose; where no legal minimum applies, define a business purpose period and a maximum retention period; document the rationale.
4. **Create the retention schedule** — Build a schedule mapping each data category to: retention trigger (date created, date of last transaction, date of contract expiry), retention period, deletion method, and responsible system/team; publish the schedule as a formal policy document.
5. **Design the legal hold process** — Define a legal hold procedure triggered by: litigation threatened or commenced, regulatory investigation, preservation letter received; legal hold suspends scheduled deletion for specific data categories relevant to the matter; require legal counsel sign-off on all holds; document hold issuance, custodians notified, and data preserved.
6. **Implement technical deletion controls** — Configure automated deletion or archival in each system at the end of the retention period; deletion must be: complete (all copies, backups, and DR environments), verifiable (deletion logs), and irreversible (secure erasure per NIST SP 800-88 or equivalent, not just logical deletion).
7. **Address backup and archive media** — Retention schedules must account for backup media; deleted data may survive in backups past the retention period; implement a backup retention period aligned to the shortest retention period in the schedule, or document backup tape recycling timelines.
8. **Document and train** — Publish the retention schedule to all data owners; train staff on legal hold obligations; conduct annual retention reviews to add new data categories and update periods for regulatory changes.

## Rules

- Never delete data subject to a legal hold regardless of scheduled retention period; document all active holds in a hold register.
- Do not equate deletion from primary systems with data erasure; confirm deletion from all backups, DR sites, and third-party processors within the retention period.
- Retain deletion logs (date, data category, volume, method, and authorizing individual) as evidence of compliance; these logs themselves have a retention period (minimum 3–5 years).
- Align the retention schedule with Article 30 ROPA (GDPR); the retention period column in the ROPA must reflect actual scheduled deletion.
- Review the retention schedule annually; regulatory changes, new data categories, and new systems require schedule updates.

## Rules

- Never delete data subject to a legal hold regardless of the scheduled retention period.
- Do not treat deletion from production systems as complete; also purge from backups, DR sites, and all sub-processors.
- Maintain deletion logs as compliance evidence; target retention for deletion logs is 5 years minimum.
- Annual review of the retention schedule is mandatory; add new data categories as they emerge.
- Escalate retention conflicts (legal hold vs. GDPR erasure request) to legal counsel; the two obligations require case-by-case resolution.

## Examples

**Retention schedule entry:** Data category: Customer purchase history. System: Shopify + data warehouse. Trigger: date of last transaction. Retention period: 7 years (tax/financial records obligation under IRS Rev. Proc. 98-25). Deletion method: automated purge job in data warehouse + Shopify data export + deletion via API. Exception: legal hold overrides. Responsible: Data Engineering team. Last reviewed: 2026-01-01.

## Common Mistakes

- **Setting "retain indefinitely" as the default** — Indefinite retention violates GDPR storage limitation for personal data; every category needs a defined period and deletion trigger.
- **Not accounting for backups** — Data deleted from production databases often persists in daily/weekly backups for months; retention periods must account for backup cycles.
- **Conflating archival with deletion** — Moving data to cold storage (AWS Glacier, offline tape) is not deletion; archived data remains subject to GDPR obligations and legal hold requirements.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.
