# Implementation: object storage, warehouses, search and streaming

Verified against vendor documentation as at 05.08.2026. Databases and caches are in `impl-databases.md`.

## Amazon S3

The versioning trap is the most common object-storage retention defect. On a versioning-enabled bucket, deleting without a version id writes a delete marker; the object version becomes noncurrent and survives.

Complete rule set for a versioned bucket:

```xml
<LifecycleConfiguration>
  <Rule>
    <ID>expire-current-versions</ID>
    <Filter><Prefix>uploads/</Prefix></Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>
    <NoncurrentVersionExpiration>
      <NoncurrentDays>30</NoncurrentDays>
      <NewerNoncurrentVersions>1</NewerNoncurrentVersions>
    </NoncurrentVersionExpiration>
    <AbortIncompleteMultipartUpload>
      <DaysAfterInitiation>7</DaysAfterInitiation>
    </AbortIncompleteMultipartUpload>
  </Rule>
  <Rule>
    <ID>clean-expired-delete-markers</ID>
    <Filter><Prefix>uploads/</Prefix></Filter>
    <Status>Enabled</Status>
    <Expiration>
      <ExpiredObjectDeleteMarker>true</ExpiredObjectDeleteMarker>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

- Removing a noncurrent version requires **both** `NoncurrentDays` and, where set, `NewerNoncurrentVersions` to be exceeded.
- `ExpiredObjectDeleteMarker` cannot share a rule with `Days` — hence the second rule.
- `ExpiredObjectDeleteMarker` and `AbortIncompleteMultipartUpload` rules cannot use a tag-based filter.
- Lifecycle actions run asynchronously; objects can persist past the nominal expiry date. Monitor actual object age rather than trusting the rule's `Days`.
- Replication is separate: a replicated object has its own lifecycle, and delete-marker replication is a distinct setting.
- **Object Lock in compliance mode blocks deletion until the retention date, for every principal including the root user.** Such a bucket is one where an Art 17 request cannot be executed. Record it as an erasure exception in the schedule.

## Cloudflare R2

```sh
npx wrangler r2 bucket lifecycle add <BUCKET_NAME> [OPTIONS]
```

The S3-compatible API accepts `putBucketLifecycleConfiguration` with `Expiration`, `Transitions` and `AbortIncompleteMultipartUpload`. Deletion is not immediate: the documentation states objects are *"typically removed from a bucket within 24 hours of the `x-amz-expiration` value"*.

`[[UNVERIFIED: whether R2 supports object versioning as at 2026-08. The object-lifecycle documentation does not mention it; confirm before assuming the S3 delete-marker trap does not apply]]`

## Google BigQuery

```sql
-- expire partitions after 90 days
ALTER TABLE mydataset.events
  SET OPTIONS (partition_expiration_days = 90);

-- remove the expiry
ALTER TABLE mydataset.events
  SET OPTIONS (partition_expiration_days = NULL);
```

```sh
# same via CLI, in seconds
bq update --time_partitioning_expiration 7776000 --time_partitioning_type DAY mydataset.events

# drop one partition outright
bq rm --table 'mydataset.events$20260301'
```

Row-level deletion:

```sql
DELETE FROM mydataset.events
WHERE _PARTITIONDATE IN ('2026-03-06', '2026-03-07');
```

The recovery envelope: 7-day time travel, configurable only between 2 and 7 days via `max_time_travel_hours`, plus a 7-day fail-safe that is not configurable and not queryable — *"You can't query or directly recover data in fail-safe storage. To recover data from fail-safe storage, contact Cloud Customer Care."* Deleted data can persist **up to 14 days**. A table expiration takes precedence over a partition expiration.

## Elasticsearch and OpenSearch

```json
PUT _ilm/policy/logs-90d
{
  "policy": {
    "phases": {
      "hot":    { "actions": { "rollover": { "max_primary_shard_size": "50gb", "max_age": "1d" } } },
      "warm":   { "min_age": "7d",  "actions": { "forcemerge": { "max_num_segments": 1 } } },
      "delete": { "min_age": "90d", "actions": { "delete": { "delete_searchable_snapshot": true } } }
    }
  }
}
```

- `min_age` is measured from rollover, not from index creation, once rollover is in play. Getting this wrong is the usual reason an index outlives its policy.
- `delete_searchable_snapshot` defaults to `true`. If an index is deleted manually before ILM reaches the delete phase, ILM will not clean up the underlying searchable snapshot; it must be removed with the delete-snapshots API.
- Attach with `index.lifecycle.name` in the index template, or configure the data stream, so new backing indices inherit the policy automatically.
- **`delete_by_query` marks documents deleted; the data remains in the segment until merge.** For a subject erasure with a deadline, follow it with a force merge that expunges deletes, and record that step in the runbook.
- OpenSearch uses ISM (`_plugins/_ism/policies`) with equivalent states and a `delete` action; the marked-then-merged semantics are the same.

## Apache Kafka

```sh
kafka-configs.sh --bootstrap-server localhost:9092 --alter \
  --entity-type topics --entity-name events \
  --add-config retention.ms=2592000000,segment.ms=86400000
```

`cleanup.policy` semantics, quoted from the Kafka topic-configuration documentation: the `delete` policy (the default) *"will discard old segments when their retention time or size limit has been reached"*; the `compact` policy *"will enable log compaction, which retains the latest value for each key"*; both may be given as `delete,compact`; **an empty list means infinite retention — no cleanup policies will be applied and log segments will be retained indefinitely** (behaviour noted in the Kafka 4.2.0 upgrade notes).

The compaction trap: on `cleanup.policy=compact`, `retention.ms` does not remove a key's latest value. The only removal path is a **tombstone** — a record with the same key and a `null` payload — after which the delete marker is itself cleaned out following a configurable retention period:

```
produce(topic, key = subject_key, value = null)     # tombstone
# then wait for: min.compaction.lag.ms, the cleaner pass, and delete.retention.ms
```

Relevant knobs: `delete.retention.ms` (how long tombstones survive so consumers can observe them), `min.cleanable.dirty.ratio`, `min.compaction.lag.ms` / `max.compaction.lag.ms`, `segment.ms`. The active segment is never compacted, so a low-traffic topic can hold an uncompacted key for a long time.

Also check `log.local.retention.ms` / `log.local.retention.bytes` where tiered storage is enabled, and every consumer that has materialised the topic into its own state store — the tombstone must propagate there too.

## Checkpoints

- [ ] Every versioned bucket has `NoncurrentVersionExpiration` **and** an `ExpiredObjectDeleteMarker` rule
- [ ] `AbortIncompleteMultipartUpload` configured wherever multipart uploads occur
- [ ] Replication targets have their own lifecycle rules; delete-marker replication decided deliberately
- [ ] Object Lock compliance-mode buckets identified and recorded as erasure exceptions
- [ ] BigQuery `max_time_travel_hours` set deliberately; the 7-day fail-safe included in the published period
- [ ] ILM `min_age` verified against rollover semantics, not index creation
- [ ] Force merge follows any `delete_by_query` used to satisfy an erasure request
- [ ] Every compacted Kafka topic has a documented tombstone procedure, including downstream state stores
- [ ] No Kafka topic has an empty `cleanup.policy` unintentionally
- [ ] Actual object and index ages monitored, not just the configured rule
