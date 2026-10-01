# Pre-ship checklist

Run before a retention scheme is declared done, and before any privacy notice states a period. Every finding is reported with its article or statute and its location, not as general advice.

This checklist ends in **queries that must return zero**, not in a policy document. A retention scheme that cannot be falsified by a query has not been verified.

## Run these first

Four checks, minutes each, that produce most of the findings.

1. **Tables with no expiry.** List every table holding personal data and diff it against the schedule. Anything in the schema and not in the schedule is a finding.
2. **Columns with no owner.** Any schedule row with `[[MISSING: owner]]` will not be maintained.
3. **Grep the estate for prohibited values.** Search the repository, the log platform, the error tracker and the fixtures for: `cvv`, `cvc`, `cav2`, `card_verification`, `track2`, `pin_block`, `password`, `authorization: bearer`.
4. **Diff the copy inventory against reality.** List the actual buckets, indexes, topics and SaaS integrations, and compare with the worksheet. The delta is where the surviving data is.

## Schedule and documentation

- [ ] One row per data element; no row covers a whole table or a whole database
- [ ] Every minimum carries a statute and a section number
- [ ] Every maximum carries reasoning that could be published under Art 13(2)(a)
- [ ] Jurisdiction determined from establishment and tax residence
- [ ] German 8-year period not applied to a supervised financial entity (Art 97 § 19a Abs 3 EGAO)
- [ ] Austrian periods not copied from a German template (7 years, § 132 BAO / § 212 UGB)
- [ ] Period start implemented as end-of-calendar-year where the statute says so
- [ ] Art 30(1)(f) column filled for every category
- [ ] Privacy notice states a period or explicit criteria per activity, never "as long as necessary"
- [ ] Litigation-hold mechanism exists and suspends the jobs it must suspend

## Erasure and restriction

- [ ] Erasure request path exists, with identity verification that does not over-collect (Art 12(6), Art 11)
- [ ] The path distinguishes ERASE, RESTRICT and REFUSE, with a citation on every non-erasure
- [ ] Art 17(3)(b) records are restricted, not deleted and not left in active processing
- [ ] Restriction is enforced by grants or row-level security, not by a WHERE clause
- [ ] Restricted rows are provably invisible to search, analytics, marketing, support and warehouse loads
- [ ] Restricted rows are provably visible to the finance and legal paths
- [ ] Lifting restriction notifies the data subject beforehand (Art 18(3))
- [ ] Response template states the residual set, its statute and its end date
- [ ] One-month deadline tracked per request (Art 12(3)), with the extension path documented

## Mechanisms

- [ ] No `deleted_at` column without a scheduled, monitored hard-delete job
- [ ] Base tables with soft delete are not readable by the application role
- [ ] High-volume time-series tables are partitioned; expiry is a partition drop
- [ ] Batched deletes are idempotent, resumable and bounded
- [ ] An index exists on every retention predicate column
- [ ] Every versioned bucket has `NoncurrentVersionExpiration` **and** an `ExpiredObjectDeleteMarker` rule
- [ ] `AbortIncompleteMultipartUpload` set wherever multipart uploads occur
- [ ] Object Lock compliance-mode buckets identified and recorded as erasure exceptions
- [ ] BigQuery `max_time_travel_hours` set deliberately; 7-day fail-safe included in the published period
- [ ] ILM `min_age` verified against rollover semantics
- [ ] Force merge follows delete-by-query used for an erasure
- [ ] Every compacted Kafka topic has a documented tombstone procedure; no unintended empty `cleanup.policy`
- [ ] Redis keys audited for missing TTLs and for `SET` calls that clear an existing TTL
- [ ] DynamoDB read paths filter expired items, or a reconciling job exists
- [ ] No TTL value is published anywhere as the retention period

## Backups and recovery

- [ ] Backup rotation window bounded and documented per system
- [ ] Restore runbook contains a re-apply-erasures step, tested at least once
- [ ] Suppression list exists, is minimal, and has its own retention row
- [ ] PITR window and WAL/binlog archive retention recorded per database
- [ ] Provider soft-delete and recycle-bin windows enumerated
- [ ] Published period is the outer envelope including all of the above

## Logs and third parties

- [ ] Security, application and analytics logs separately routed and separately expired
- [ ] IP truncation or dropping happens at ingest in the collector
- [ ] No unkeyed hash is described as anonymisation
- [ ] Redaction enforced at the logging library with a CI check
- [ ] User ids absent from metric labels
- [ ] Every processor has a signed Art 28(3) contract, a recorded deletion granularity and a documented turnaround
- [ ] Vendor-side retention floors recorded, including abuse-monitoring copies
- [ ] Account-teardown-only vendors flagged as an erasure constraint

## Monitoring and evidence

- [ ] Every deletion job emits rows examined, rows deleted, oldest surviving timestamp
- [ ] Alert on job not completing within its interval
- [ ] Alert on oldest surviving timestamp exceeding the period
- [ ] Alert on zero deletions across consecutive runs on a table that receives writes
- [ ] Run log retained as the Art 5(2) record, with its own schedule row

## The verifiable assertions

Each element in the schedule gets a query that **must return zero rows**. Run them on a schedule, not once. A retention scheme is verified when every one of these is green, and unverified otherwise.

```sql
-- 1. no row older than its period survives
SELECT count(*) AS violations
  FROM events
 WHERE occurred_at < now() - interval '90 days';

-- 2. period start is the end of the calendar year, not created_at
SELECT count(*) AS violations
  FROM invoices
 WHERE retention_until <> (date_trunc('year', issued_at) + interval '9 years')::date
   AND issued_at IS NOT NULL;         -- 8 years, counted from the following 1 January

-- 3. nothing soft-deleted has been left behind the hard-delete window
SELECT count(*) AS violations
  FROM customers_all
 WHERE deleted_at < now() - interval '30 days';

-- 4. no restricted row is reachable by the application role
--    run this AS the application role; it must return 0 even without a predicate
SET ROLE app_role;
SELECT count(*) AS violations FROM invoices WHERE restricted_at IS NOT NULL;
RESET ROLE;

-- 5. every table holding personal data has a schedule row
SELECT t.table_name AS unscheduled
  FROM information_schema.tables t
  LEFT JOIN retention_schedule s ON s.table_name = t.table_name
 WHERE t.table_schema = 'public'
   AND t.table_type = 'BASE TABLE'
   AND s.table_name IS NULL;

-- 6. every deletion job ran recently and produced evidence
SELECT jobname AS stale_job
  FROM cron.job j
 WHERE NOT EXISTS (
   SELECT 1 FROM cron.job_run_details d
    WHERE d.jobid = j.jobid
      AND d.status = 'succeeded'
      AND d.end_time > now() - interval '2 days'
 );

-- 7. no erasure request is past its Art 12(3) deadline
SELECT count(*) AS overdue
  FROM erasure_requests
 WHERE completed_at IS NULL
   AND received_at < now() - interval '1 month';
```

Non-SQL equivalents, one per store:

| Store | Assertion |
|---|---|
| S3 | no object under the prefix has `LastModified` older than the period, **and** `list-object-versions` returns no version older than the period |
| BigQuery | `SELECT max(_PARTITIONDATE)` boundary check plus confirmation that `max_time_travel_hours` is set |
| Elasticsearch | oldest index `creation_date` within the period; `_ilm/explain` shows no index in an error step |
| Kafka | earliest offset timestamp within `retention.ms`; for compacted topics, tombstone produced and the key absent after a cleaner pass |
| Redis | count of keys matching the pattern with `TTL = -1` is zero |
| DynamoDB | scan with a filter on the TTL attribute in the past returns zero items |
| Third-party SaaS | deletion confirmation on file, dated, per subject or per engagement |

## Findings format

Report findings as a table, most severe first:

| Severity | Location | Norm | Finding | Fix |
|---|---|---|---|---|
| critical / high / medium | system, table, bucket or file:line | Art or § | what is wrong | concrete step |

**Critical** means: data retained past a statutory maximum with no mechanism; sensitive authentication data present anywhere; an erasure request answered as complete while data survives; a statutory minimum breached by a deletion job. Everything else starts at high.

- [ ] All `[[MISSING: …]]` items resolved or reported back to the user
- [ ] All `[[UNVERIFIED: …]]` items in the reference files resolved before the corresponding figure is published
- [ ] Draft marker still present on every artefact, unless sign-off has been recorded
