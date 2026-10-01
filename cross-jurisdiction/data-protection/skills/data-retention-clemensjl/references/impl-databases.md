# Implementation: databases and caches

Working syntax, and for each store the gap between what the API returns and what is actually gone. Verified against vendor documentation as at 05.08.2026. Object stores, warehouses, search and streaming are in `impl-storage.md`.

## PostgreSQL — batched deletion without long locks

Current release series: **PostgreSQL 18**. A single unbounded `DELETE` over a large table holds row locks for the whole statement, bloats the WAL, stalls replication and cannot be resumed. Batch it and commit per batch.

```sql
CREATE OR REPLACE PROCEDURE purge_events(p_cutoff timestamptz, p_batch int DEFAULT 5000)
LANGUAGE plpgsql AS $$
DECLARE
  v_deleted int;
  v_total   bigint := 0;
BEGIN
  LOOP
    WITH doomed AS (
      SELECT id
        FROM events
       WHERE occurred_at < p_cutoff
       ORDER BY occurred_at
       LIMIT p_batch
         FOR UPDATE SKIP LOCKED
    )
    DELETE FROM events e
     USING doomed d
     WHERE e.id = d.id;

    GET DIAGNOSTICS v_deleted = ROW_COUNT;
    v_total := v_total + v_deleted;
    COMMIT;                         -- procedures may commit; functions may not
    EXIT WHEN v_deleted = 0;
    PERFORM pg_sleep(0.05);         -- give replication and autovacuum room
  END LOOP;

  INSERT INTO retention_run_log(job, cutoff, rows_deleted, finished_at)
  VALUES ('purge_events', p_cutoff, v_total, now());
END $$;
```

- `FOR UPDATE SKIP LOCKED` makes concurrent runs safe and stops the job blocking on a row the application is editing.
- `ORDER BY` on the indexed predicate column keeps each batch a range scan rather than a full scan.
- `COMMIT` inside a procedure is required for the batching to mean anything; inside a function it is not permitted.
- The index is not optional: `CREATE INDEX CONCURRENTLY ON events (occurred_at);`
- `DELETE` leaves dead tuples. Autovacuum reclaims them for reuse; space returns to the filesystem only with `VACUUM FULL`, which takes an `ACCESS EXCLUSIVE` lock.
- The deletion is in the WAL, therefore in the archive, therefore in the PITR window. See `backups.md`.

Prefer a partition drop where the data is time-series; see `schema-patterns.md` for the DDL and the lock levels.

## pg_cron — scheduling inside the database

```sql
-- postgresql.conf
-- shared_preload_libraries = 'pg_cron'
-- cron.database_name = 'postgres'      -- default; the extension lives in this database

CREATE EXTENSION pg_cron;

SELECT cron.schedule(
  'purge-events',
  '15 3 * * *',
  $$CALL purge_events(date_trunc('day', now()) - interval '90 days')$$
);

-- target a different database
SELECT cron.schedule_in_database(
  'purge-events-app',
  '15 3 * * *',
  $$CALL purge_events(date_trunc('day', now()) - interval '90 days')$$,
  'appdb'
);

SELECT cron.unschedule('purge-events');
```

pg_cron also accepts interval syntax such as `'10 seconds'` for sub-minute schedules. Job history is in `cron.job_run_details`; that table is the evidence source for the checklist and needs its own retention row or it grows without bound.

## Redis

```
SET session:abc "…" EX 3600
EXPIRE session:abc 3600 NX      # NX/XX/GT/LT available since Redis 7.0.0
TTL session:abc
PERSIST session:abc             # removes the TTL - the key now lives forever
```

Facts that decide whether Redis is a retention risk:

- *"Normally Redis keys are created without an associated time to live. The key will simply live forever."* A key without an explicit TTL is unbounded retention.
- The TTL is cleared by any command that replaces the value — `SET`, `GETSET`, the `*STORE` commands. `INCR`, `LPUSH` and `HSET` leave it intact. A `SET` without `KEEPTTL` silently converts an expiring key into a permanent one.
- Expiry is passive (on access) plus active (periodic random sampling). It is not a scheduled sweep.
- On expiry a `DEL` is synthesised into the AOF and propagated to replicas, so replicas do not expire independently. The RDB snapshot and the AOF file on disk still hold the value until the next rewrite.
- `maxmemory-policy` evicts under memory pressure. It is a capacity control and guarantees nothing about retention.

## MongoDB

```js
db.sessions.createIndex({ lastModifiedDate: 1 }, { expireAfterSeconds: 3600 })
```

The TTL monitor runs **every 60 seconds**. The documentation is explicit: *"The TTL index does not guarantee that expired data is deleted immediately upon expiration."* Each pass deletes up to 50,000 documents or spends one second per index before moving on, deletion is single-threaded, and only the primary deletes — secondaries replicate. Under load, expired documents persist well beyond 60 seconds.

`expireAfterSeconds` must be between 0 and 2147483647. A document whose indexed field is not a date is never expired, silently.

## DynamoDB

TTL is configured per table on a numeric attribute holding a Unix epoch timestamp in seconds. Attributes of any other type are ignored silently.

Documented behaviour: *"DynamoDB automatically deletes expired items within a few days of their expiration time"*, and *"Items with valid, expired TTL attributes may be deleted by the system at any time, typically within a few days after their expiration."* Critically: *"Use filter expressions to remove expired items from Scan and Query results"* — an expired item is still returned until it is actually deleted.

TTL deletions appear in DynamoDB Streams as service deletions rather than user deletes, which matters if a downstream consumer distinguishes them. With Global Tables (2019.11.21), TTL deletes replicate to all replica tables.

Consequence: never treat the TTL attribute as the retention control on its own. Either filter expired items on every read path, or run a reconciling delete job, or both.

## Checkpoints

- [ ] Every deletion job is batched, resumable and writes a run record
- [ ] An index exists on every retention predicate column
- [ ] `VACUUM` strategy decided for high-churn tables, and the bloat accepted or scheduled away
- [ ] `cron.job_run_details` (or the equivalent scheduler history) has its own retention row
- [ ] Redis keys audited for missing TTLs and for `SET` calls that clear an existing TTL
- [ ] MongoDB TTL fields verified to be dates; expected lag documented rather than assumed to be zero
- [ ] DynamoDB read paths filter expired items, or a reconciling job exists
- [ ] No TTL value from this file is published anywhere as the retention period
