# Backups, snapshots and recovery windows

The reason erasure fails in practice is not the backup tape. It is the four recovery mechanisms nobody classified as a backup: the PITR window, the WAL archive, object versioning, and provider soft delete. Each silently retains deleted data, and three of them are on by default.

## The accepted position, and how to state it

The workable position for backups is: **you do not surgically edit a backup; you bound the window and re-apply the deletion on restore.** Three components, all required:

1. a **bounded rotation window** — every backup is guaranteed to age out within a known, short period
2. a **documented restore procedure** that re-applies pending erasures before the restored system is returned to production use
3. a **suppression list** of subjects whose erasure is pending or complete, itself retained for exactly this purpose and no other, so the re-delete can be executed against a restored copy

Do not tell the user that a regulator has blessed this without citing the guidance you actually read. Several supervisory authorities have published positions on erasure and backups; verify the one that applies to the user's lead authority and quote it.

`[[UNVERIFIED: the ICO's published wording on erasure and backups, including the "put the data beyond use" formulation — ico.org.uk returns 403 to automated fetches. Read the ICO right-to-erasure guidance page and quote it directly before relying on it]]`

`[[UNVERIFIED: whether the CNIL, the Irish DPC or the Danish Datatilsynet have published a more specific backup position that binds the user's lead authority]]`

What is not defensible in any reading: an indefinite backup window, an undocumented restore path, or a claim that erasure completed while a restorable copy exists and no suppression mechanism does.

## The suppression list is itself personal data

Keeping "do not restore this person" requires keeping enough to identify them. Handle it as its own schedule row:

- store the minimum linking value — a hash of the identifier is usually enough to match on restore
- purpose is exactly one thing: preventing reintroduction of erased data
- retention is bounded by the longest backup window plus a margin, then it expires too
- it is not a marketing suppression list and must not be joined to one

## Point-in-time recovery windows

PITR is a continuously maintained ability to reconstruct the database at any moment inside a window. Inside that window, a deleted row is recoverable, therefore retained.

| Mechanism | What it retains |
|---|---|
| Managed-database automated backup retention | full snapshots plus the transaction log needed to roll forward |
| WAL / binlog / oplog archive | every change, including the DELETE and the value it removed |
| Read replicas | the row until replication applies the delete |
| Storage-layer snapshots | the block image, independent of the database |

`[[UNVERIFIED: current maximum automated-backup retention for AWS RDS and Aurora, and whether Aurora Backtrack is a separate window on top — verify against the AWS documentation before quoting a number]]`

`[[UNVERIFIED: default and maximum PITR windows for Supabase and Neon — verify against vendor documentation]]`

The published retention period must be the **outer envelope**: the moment the DML ran plus the PITR window plus the backup rotation. Publishing the DML moment is a false statement.

## Postgres specifics

`DELETE` does not remove data from disk. It marks the tuple dead. The bytes remain in the heap page until `VACUUM` reclaims the space, and `VACUUM` reuses the space rather than returning it to the filesystem. `VACUUM FULL` rewrites the table and does return it, at the cost of an `ACCESS EXCLUSIVE` lock. Verified against the PostgreSQL 18 documentation, which is the current release series.

Additionally: the delete itself is written to the WAL, the WAL goes to the archive, the archive feeds PITR and any standby, and the base backup underneath predates the delete. A single `DELETE` therefore touches at least five retention surfaces.

Practical consequence: for genuinely sensitive elements, prefer **crypto-shredding** (see `schema-patterns.md`) over relying on physical erasure of heap pages, because destroying the key invalidates every copy in every one of those surfaces at once.

## BigQuery time travel and fail-safe

Verified against the BigQuery time-travel documentation:

- **time travel**: 7 days by default, configurable only within a range of 2 to 7 days via `max_time_travel_hours`
- **fail-safe**: a further 7 days, **not configurable**, not queryable — *"You can't query or directly recover data in fail-safe storage. To recover data from fail-safe storage, contact Cloud Customer Care."*
- total: deleted data can persist for **up to 14 days** after the DELETE

Setting `max_time_travel_hours` to the 48-hour minimum reduces the envelope to 9 days. It cannot be reduced further.

## Object storage: versioning, delete markers and soft delete

On a versioning-enabled S3 bucket, deleting an object without a version id **does not delete anything** — it writes a delete marker. The AWS lifecycle documentation states it directly: *"If you don't specify a version ID in your delete request, Amazon S3 adds a delete marker instead of deleting the object. The current object version becomes noncurrent, and the delete marker becomes the current version."*

Consequences for a lifecycle rule:

- `Expiration` on a versioned bucket creates delete markers. The data survives as noncurrent versions.
- `NoncurrentVersionExpiration` removes the noncurrent versions — but only where **both** `NoncurrentDays` and, where set, `NewerNoncurrentVersions` have been exceeded.
- `ExpiredObjectDeleteMarker` cleans up delete markers left with no noncurrent versions behind them. It cannot be combined with `Days` in the same rule.
- `AbortIncompleteMultipartUpload` with `DaysAfterInitiation` removes orphaned parts, which are also copies of the data.
- Cross-region replication may have replicated the object; delete-marker replication is a separate setting.

**Object Lock in compliance mode makes deletion impossible until the retention date expires, and cannot be overridden by any account including the root user.** A bucket in compliance mode is a bucket where an Art 17 request cannot be executed. That is a design decision with legal consequences and it must be recorded in the schedule, not discovered during a request.

`[[UNVERIFIED: whether Cloudflare R2 supports object versioning as at 2026-08 — the R2 object-lifecycle documentation does not mention it. Verify before assuming R2 has no versioning trap]]`

R2 lifecycle deletion is not immediate: *"Objects will typically be removed from a bucket within 24 hours of the `x-amz-expiration` value."*

## Provider soft delete

Almost every managed platform now has a recycle bin that is enabled by default and invisible in the API response:

- object storage soft-delete / recycle-bin features with their own retention days
- managed file shares and backup vaults with soft-delete windows
- SaaS trash folders (mailboxes, CRM records, support tickets) that retain for 30 days or more after the UI says "deleted"
- snapshot retention policies attached to the volume rather than the database

Every one of these is a row in `copy-inventory.md` with its own window.

## Backup encryption as a lever

If backups are encrypted per-subject or per-tenant with keys held outside the backup, destroying the key removes the restorability of that subject's data from every backup simultaneously. This is the only mechanism that makes "erased from backups" true in a short timeframe. It requires designing the key hierarchy before the backups exist.

## Checkpoints

- [ ] Backup rotation window is bounded and the number is written down per system
- [ ] Restore runbook contains an explicit re-apply-erasures step, and it has been tested at least once
- [ ] Suppression list exists, is minimal, has its own retention row and is not joined to marketing suppression
- [ ] PITR window recorded per managed database and included in the published period
- [ ] WAL / binlog / oplog archive retention recorded
- [ ] `max_time_travel_hours` set deliberately on BigQuery datasets; the non-configurable 7-day fail-safe is accounted for in the published period
- [ ] Every bucket's versioning status known; lifecycle rules include `NoncurrentVersionExpiration` and `ExpiredObjectDeleteMarker` where versioning is on
- [ ] `AbortIncompleteMultipartUpload` configured on every bucket that receives multipart uploads
- [ ] Object Lock compliance-mode buckets identified and their erasure impossibility recorded in the schedule
- [ ] Provider soft-delete / recycle-bin windows enumerated per service
- [ ] Published retention period is the outer envelope including all of the above
