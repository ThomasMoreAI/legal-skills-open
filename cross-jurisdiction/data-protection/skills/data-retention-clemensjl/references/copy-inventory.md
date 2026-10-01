# Copy-inventory worksheet

The failure mode is never the main table. It is the seventeenth copy. Fill one worksheet per data element that carries a retention period, before writing any deletion job.

The question for every row is not "do we delete it here" but **"can this location reconstruct the data after the primary copy is gone"**. If yes, it is in scope.

## Worksheet

Copy this table per data element. `[[PLACEHOLDER]]` slots are for the user to fill; unknown values stay `[[MISSING: …]]` in the report.

**Data element:** `[[schema.table.column or logical name]]`
**Owner:** `[[team or person]]`
**Statutory minimum:** `[[period + citation]]`
**Art 5(1)(e) maximum:** `[[period + reasoning]]`

| # | Location | System | Present? | Deletion mechanism | Lag until physically gone | Owner | Evidence of execution |
|---|---|---|---|---|---|---|---|
| 1 | Primary OLTP table | `[[ ]]` | | | | | |
| 2 | Secondary tables via FK (audit, history, versions) | `[[ ]]` | | | | | |
| 3 | Materialised views / read models | `[[ ]]` | | | | | |
| 4 | Read replicas | `[[ ]]` | | replication | replication lag | | |
| 5 | WAL / binlog / oplog archive | `[[ ]]` | | archive expiry | `[[ ]]` | | |
| 6 | PITR window | `[[ ]]` | | window rotation | `[[ ]]` | | |
| 7 | Automated snapshots / base backups | `[[ ]]` | | rotation | `[[ ]]` | | |
| 8 | Off-site / cross-region backup copy | `[[ ]]` | | rotation | `[[ ]]` | | |
| 9 | Backup vault soft-delete window | `[[ ]]` | | vault setting | `[[ ]]` | | |
| 10 | Search index (Elasticsearch, OpenSearch, Meilisearch, Algolia) | `[[ ]]` | | delete-by-query + merge | segment merge | | |
| 11 | Cache (Redis, Memcached, in-process) | `[[ ]]` | | TTL / explicit DEL | see `impl-databases.md` | | |
| 12 | Message queue / event log (Kafka, SQS, Pub/Sub) | `[[ ]]` | | retention or tombstone | `[[ ]]` | | |
| 13 | Compacted topics and their consumer state stores | `[[ ]]` | | tombstone + compaction | `[[ ]]` | | |
| 14 | Object storage: current versions | `[[ ]]` | | lifecycle `Expiration` | up to 24h+ | | |
| 15 | Object storage: noncurrent versions and delete markers | `[[ ]]` | | `NoncurrentVersionExpiration` + `ExpiredObjectDeleteMarker` | `[[ ]]` | | |
| 16 | Object storage: incomplete multipart parts | `[[ ]]` | | `AbortIncompleteMultipartUpload` | `[[ ]]` | | |
| 17 | Object storage under Object Lock | `[[ ]]` | | **none until retention expires** | `[[ ]]` | | |
| 18 | CDN cache and edge storage | `[[ ]]` | | purge | `[[ ]]` | | |
| 19 | Data warehouse / lakehouse tables | `[[ ]]` | | partition expiry or rewrite | + time travel | | |
| 20 | Warehouse time travel / fail-safe | `[[ ]]` | | not configurable | up to 14 days (BigQuery) | | |
| 21 | BI extracts, dashboards with cached result sets | `[[ ]]` | | extract refresh | `[[ ]]` | | |
| 22 | ETL staging areas and landing buckets | `[[ ]]` | | lifecycle | `[[ ]]` | | |
| 23 | Application logs (aggregator, hot tier) | `[[ ]]` | | ILM / retention tier | `[[ ]]` | | |
| 24 | Application logs (archive / cold tier) | `[[ ]]` | | separate policy | `[[ ]]` | | |
| 25 | Log agent local buffers on hosts | `[[ ]]` | | buffer rotation | `[[ ]]` | | |
| 26 | Error tracker | `[[ ]]` | | scrubbing + delete API | `[[ ]]` | | |
| 27 | APM / tracing vendor | `[[ ]]` | | retention tier | `[[ ]]` | | |
| 28 | Session replay | `[[ ]]` | | masking + delete | `[[ ]]` | | |
| 29 | Product analytics | `[[ ]]` | | per-subject delete API | `[[ ]]` | | |
| 30 | Advertising / conversion platforms | `[[ ]]` | | platform deletion request | `[[ ]]` | | |
| 31 | CRM (records + recycle bin) | `[[ ]]` | | delete + empty bin | `[[ ]]` | | |
| 32 | Support desk (tickets, attachments, surveys) | `[[ ]]` | | redact or delete | `[[ ]]` | | |
| 33 | Email service provider (messages, delivery logs) | `[[ ]]` | | contact delete | `[[ ]]` | | |
| 34 | Email suppression list | `[[ ]]` | | intentionally retained | permanent by design | | |
| 35 | Transactional email archives and inbound mailboxes | `[[ ]]` | | mailbox retention | + trash window | | |
| 36 | Billing / payment provider | `[[ ]]` | | provider-side statutory retention | `[[ ]]` | | |
| 37 | Accounting system and its exports | `[[ ]]` | | statutory minimum applies | `[[ ]]` | | |
| 38 | Identity provider / SSO directory | `[[ ]]` | | user delete | `[[ ]]` | | |
| 39 | Feature flag / experimentation platform | `[[ ]]` | | targeting lists | `[[ ]]` | | |
| 40 | LLM API provider (prompts, completions) | `[[ ]]` | | account setting | + provider abuse-monitoring floor | | |
| 41 | Vector store / embedding index | `[[ ]]` | | delete by metadata filter | `[[ ]]` | | |
| 42 | Model training sets and fine-tuned model weights | `[[ ]]` | | **usually irreversible** | `[[ ]]` | | |
| 43 | CI artefacts, test fixtures, seed data | `[[ ]]` | | artefact retention | `[[ ]]` | | |
| 44 | Staging and development database copies | `[[ ]]` | | refresh cycle | `[[ ]]` | | |
| 45 | Local developer machines and ad-hoc CSV exports | `[[ ]]` | | policy only | unbounded | | |
| 46 | Shared drives, spreadsheets, exported reports | `[[ ]]` | | manual | unbounded | | |
| 47 | Chat tools where records were pasted into a thread | `[[ ]]` | | workspace retention | `[[ ]]` | | |

## The four rows that decide whether the whole exercise is honest

- **Row 20 (time travel / fail-safe)** and **row 6 (PITR)** set the floor on how fast anything can truly disappear. The published period must include them.
- **Row 17 (Object Lock)** and **row 42 (model weights)** are locations where deletion may be impossible. If either is populated, the schedule must say so explicitly rather than implying deletion happens everywhere.
- **Rows 45 to 47** are where the copies nobody authorised live. They cannot be solved with a job, only with a control that prevents the export in the first place.

## How to use it

1. Fill "Present?" honestly by checking, not by assuming. Grep the schema, list the buckets, read the vendor's data-retention page.
2. For every "yes", record the mechanism and the lag. "Manual" and "none" are valid answers and are the findings.
3. Sum the lags along the longest path. That number, not the DELETE timestamp, is what goes into the privacy notice.
4. Any row with no owner is a row that will not be maintained. Assign one or record it as `[[MISSING: owner for …]]`.

## Checkpoints

- [ ] One worksheet exists per data element carrying a retention period
- [ ] "Present?" answered by inspection, not by assumption, for every row
- [ ] Longest-path lag computed and used as the published period
- [ ] Every location with no deletion mechanism is recorded as a finding, not left blank
- [ ] Locations where deletion is impossible (Object Lock, model weights) are named explicitly in the schedule
- [ ] Every row has a named owner or a `[[MISSING: …]]` marker
- [ ] Third-party rows carry the vendor's own retention floor, not only the setting you chose
- [ ] Uncontrolled copies (rows 45 to 47) have a prevention control, not a cleanup task
