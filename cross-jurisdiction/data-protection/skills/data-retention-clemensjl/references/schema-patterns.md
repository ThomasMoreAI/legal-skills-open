# Schema and implementation patterns

How the interval from `legal-frame.md` becomes something a table can express. Status as at 05.08.2026.

## Soft delete is not erasure

`deleted_at TIMESTAMPTZ` marks a row as gone for the application. It does not:

- remove the data from the heap, the indexes, the replicas or the backups
- protect against a query that forgets `WHERE deleted_at IS NULL`
- prevent the nightly warehouse load from copying the row
- prevent the search indexer from having already copied it
- satisfy Art 17

Soft delete is legitimate as a **staging state** ahead of a hard delete, and as an undo window for user-initiated deletes. It becomes a retention control only when a job is scheduled behind it and the job is monitored. Write the hard-delete job in the same pull request as the `deleted_at` column.

If soft delete must exist, defend it at the schema level rather than by convention:

```sql
-- the application never reads the base table
ALTER TABLE customers RENAME TO customers_all;

CREATE VIEW customers AS
  SELECT * FROM customers_all WHERE deleted_at IS NULL AND restricted_at IS NULL;

REVOKE ALL ON customers_all FROM app_role;
GRANT SELECT, INSERT, UPDATE ON customers TO app_role;
```

A forgotten predicate now returns nothing instead of returning erased people.

## The three states a retention-aware schema needs

Most schemas have two states. They need three.

| State | Meaning | Readable by |
|---|---|---|
| live | purpose active | everything |
| **restricted** | purpose exhausted, statutory minimum still running (Art 18) | finance export, tax audit path, legal-claims path only |
| erased | statutory minimum expired or never applied | nothing |

Implementing restricted:

```sql
ALTER TABLE invoices
  ADD COLUMN restricted_at   TIMESTAMPTZ,
  ADD COLUMN restricted_reason TEXT,
  ADD COLUMN retention_until DATE NOT NULL;   -- end of the statutory minimum
```

- `retention_until` is computed from the **end of the calendar year** of the driving event, not from `created_at`.
- restriction must be enforced by the grant model, not by a predicate the caller may omit. Row-level security is the mechanism that survives a new developer:

```sql
ALTER TABLE invoices ENABLE ROW LEVEL SECURITY;

CREATE POLICY invoices_app ON invoices FOR SELECT TO app_role
  USING (restricted_at IS NULL);

CREATE POLICY invoices_finance ON invoices FOR SELECT TO finance_role
  USING (true);
```

- Art 18(3) requires informing the data subject **before** restriction is lifted. Lifting restriction is therefore an explicit operation with a notification step, never a side effect of a backfill.

## Tombstones and referential integrity

Hard-deleting a person from `users` breaks every foreign key pointing at them. The three viable resolutions:

| Pattern | Mechanism | When |
|---|---|---|
| Cascade | `ON DELETE CASCADE` | the dependent rows are also that person's data and have no independent retention duty |
| Null out and keep | `ON DELETE SET NULL` on a nullable FK | the dependent row must survive for its own reason (an order line inside the tax period) and no longer needs to name the person |
| Tombstone user | repoint the FK at a permanent sentinel row (`user_id = 0`, "deleted user") | aggregate integrity matters and the sentinel carries no personal data |

Never keep the FK value pointing at a deleted row and rely on the join failing. That leaves the id — which is itself personal data as an identifier — scattered across the schema.

The dangerous variant: `ON DELETE SET NULL` on a column that is also in a unique or composite index used by an analytics job. Deleting the user then silently changes the grouping of historical reports. Decide this consciously and record it in the schedule row.

## Anonymisation vs pseudonymisation

Art 4(5) defines pseudonymisation as processing such that the data can no longer be attributed to a subject **without the use of additional information**, kept separately and subject to technical and organisational measures. Pseudonymous data remains personal data.

Anonymous data falls outside the Regulation entirely (Recital 26), but only where the subject is no longer identifiable **by any means reasonably likely to be used** — by anyone, not only by you.

The test to apply to any proposed "anonymisation", following the long-standing WP29 framing:

| Risk | Question |
|---|---|
| Singling out | can a single individual still be isolated in the dataset? |
| Linkability | can two records about the same person still be linked, here or against another dataset? |
| Inference | can an attribute of an individual still be deduced with significant probability? |

Techniques and where they actually land:

| Technique | Result |
|---|---|
| Replace user id with a random id, keep the mapping | pseudonymisation |
| Replace user id with a keyed hash, key retained | pseudonymisation |
| Replace user id with an unkeyed hash of an email address | pseudonymisation, and weak: the input space is enumerable |
| Delete direct identifiers, keep a rich behavioural record | usually still personal data — singling out survives |
| Aggregate to counts with a minimum group size and suppression of small cells | plausibly anonymous, depending on the cells |
| Differential privacy with a documented budget | strongest available claim |

Reference the current guidance honestly: **EDPB Guidelines 02/2026 on anonymisation are open for public consultation from 08.07.2026 to 30.10.2026 and are not final** (edpb.europa.eu public-consultations register). Any position drawn from them is a draft position.

**The recurring failure is anonymisation used as a substitute for deletion**: the identifiers are stripped, the record is kept, and the retention obligation is declared satisfied while a re-identifiable dataset survives. If the answer to all three risk questions is not "no", the record was retained, not anonymised, and the schedule row is unsatisfied.

`[[UNVERIFIED: the EDPB CEF 2025 coordinated enforcement action on the right to erasure, its report reportedly adopted 10.02.2026 across 32 supervisory authorities, and the reported finding that anonymisation was used as a substitute for deletion. This report was not locatable in the EDPB news or documents registers during verification. Confirm the title, date and findings against edpb.europa.eu before citing it]]`

## Crypto-shredding

Encrypt each subject's data under a per-subject key; erase by destroying the key. The ciphertext becomes unreadable everywhere it exists at once — including backups, replicas, PITR windows and any copy a processor holds.

```
subject_key  = HKDF(master_key, subject_id)        -- derived, never stored alone
row_payload  = AEAD_encrypt(subject_key, plaintext, aad = table||row_id)
erase(subject) = destroy subject_key material in the KMS/HSM
```

Constraints that decide whether it is usable:

- **Only the encrypted columns are shredded.** An id or an email in an unencrypted index, a foreign key, a log line or a search index is untouched. Crypto-shredding is a component, not a strategy.
- **Queryability collapses.** You cannot index, sort, join or aggregate on an encrypted column. It suits document blobs, attachments, free-text notes and message bodies; it does not suit anything the application filters on.
- **Key destruction must be real.** A KMS key scheduled for deletion with a mandatory waiting period is not destroyed yet, and a key backed up outside the KMS is not destroyed at all. Record the actual destruction latency.
- **Derived keys must not be reconstructable** from a master key that survives. If `subject_key = HKDF(master_key, subject_id)` and `master_key` still exists, nothing was destroyed. Store per-subject key material as an independently deletable object.

## Time partitioning

The cheapest expiry is dropping a partition: a metadata operation instead of a row scan, no dead tuples, no vacuum debt.

```sql
CREATE TABLE events (
  id         bigint      NOT NULL,
  user_id    bigint      NOT NULL,
  occurred_at timestamptz NOT NULL,
  payload    jsonb
) PARTITION BY RANGE (occurred_at);

CREATE TABLE events_2026_08 PARTITION OF events
  FOR VALUES FROM ('2026-08-01') TO ('2026-09-01');
```

Dropping an old partition:

```sql
-- DROP TABLE on a partition takes ACCESS EXCLUSIVE on the parent
ALTER TABLE events DETACH PARTITION events_2025_08 CONCURRENTLY;  -- SHARE UPDATE EXCLUSIVE only
DROP TABLE events_2025_08;
```

Verified against the PostgreSQL 18 partitioning documentation: `DROP TABLE` on a partition requires an `ACCESS EXCLUSIVE` lock on the parent, while `DETACH PARTITION CONCURRENTLY` needs only `SHARE UPDATE EXCLUSIVE`. Detach first, then drop, on a live system.

Partitioning does not help with a **subject** erasure, which cuts across every partition. Use partitions for age-based expiry and a batched delete for subject-based erasure.

## TTL features: guaranteed vs advisory

| Mechanism | What it guarantees |
|---|---|
| Postgres partition drop | immediate, physical |
| BigQuery `partition_expiration_days` | partition removed, then time travel and fail-safe (up to 14 days) |
| Elasticsearch ILM `delete` phase | index deleted; searchable snapshot only if `delete_searchable_snapshot` is true (default true) |
| Redis `EXPIRE` | key removed lazily on access and by active random sampling; RDB/AOF hold the value until rewrite |
| MongoDB TTL index | monitor runs every 60 seconds; documentation states expired data may exist beyond that |
| DynamoDB TTL | "typically within a few days"; expired items still returned by Query and Scan until deleted |
| Kafka `retention.ms` | segment-level, and **inoperative on a compacted topic** |
| S3 `Expiration` on a versioned bucket | a delete marker, not deletion |

The rule that follows: never publish a TTL value as the retention period. Publish the period you enforce and alert on, and treat the TTL as the mechanism that usually achieves it.

## Checkpoints

- [ ] No `deleted_at` column exists without a scheduled, monitored hard-delete job behind it
- [ ] Base tables with soft delete are not directly readable by the application role
- [ ] A restricted state exists and is enforced by grants or row-level security, not by a predicate
- [ ] `retention_until` computed from the end of the calendar year of the driving event
- [ ] Lifting restriction is an explicit operation with an Art 18(3) notification step
- [ ] Referential-integrity strategy chosen per FK and recorded, with the analytics impact noted
- [ ] Any "anonymised" dataset passes singling out, linkability and inference, with the reasoning written down
- [ ] EDPB Guidelines 02/2026 cited as draft wherever referenced
- [ ] Crypto-shredding scope stated explicitly: which columns it covers and which identifiers it does not
- [ ] Key destruction latency recorded, and derived keys are not reconstructable from a surviving master
- [ ] High-volume time-series tables are partitioned by time
- [ ] No TTL value is published as a retention period
