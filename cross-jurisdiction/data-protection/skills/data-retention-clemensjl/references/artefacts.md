# Artefacts

Six deliverables, each as a template. Every one carries the draft marker until sign-off. Unknown values are `[[MISSING: …]]`, never plausible defaults.

## 1. Retention schedule

The central artefact. One row per **data element**, not per table.

```
<!-- DRAFT - not legally approved -->
```

| Data element | Purpose | Legal basis | Minimum + citation | Maximum + reasoning | Storage locations | Deletion mechanism | Owner | Review |
|---|---|---|---|---|---|---|---|---|
| `invoices.*` | fulfil and account for a sale | Art 6(1)(b), 6(1)(c) | 8 years from end of year of issue (§ 14b Abs 1 UStG; § 147 Abs 3 S 1 iVm Abs 1 Nr 4 AO) | purpose exhausted at payment; minimum governs | primary DB, warehouse, PDF bucket, accounting system | restrict at payment + 90d; hard delete at `retention_until` | `[[owner]]` | `[[date]]` |
| `users.email` | authentication and service email | Art 6(1)(b) | none | account closure + 30d grace, so accidental closures can be reversed | primary DB, ESP, CRM, search index | cascade delete | `[[owner]]` | `[[date]]` |
| `events.*` | product improvement | Art 6(1)(f) | none | 14 months raw; a raw event past one annual cycle has no marginal value | primary DB (partitioned), warehouse, analytics SaaS | partition drop + warehouse partition expiry | `[[owner]]` | `[[date]]` |
| `access_log.*` | detect and investigate incidents | Art 6(1)(f), Art 32 | none | 12 months, covering realistic detection latency | log platform hot + archive tier | ILM delete phase | `[[owner]]` | `[[date]]` |
| card verification code | none — must not exist | none available | **0** | **0** | must be absent everywhere | prevented at capture (PCI DSS v4.0.1 Req 3) | `[[owner]]` | `[[date]]` |
| `[[element]]` | `[[MISSING: purpose]]` | `[[MISSING: basis]]` | `[[MISSING: minimum + citation]]` | `[[MISSING: maximum + reasoning]]` | `[[MISSING: locations]]` | `[[MISSING: mechanism]]` | `[[MISSING: owner]]` | `[[ ]]` |

Rules for filling it:

- **A minimum without a citation is not a minimum.** If no statute applies, write "none". Do not invent a conservative number — a conservative number is an Art 5(1)(e) breach.
- **A maximum without reasoning is not a maximum.** The reasoning is what you publish under Art 13(2)(a) when a bare period is not possible.
- Where minimum > maximum, the mechanism column says "restrict at X, delete at Y", never a single date.
- "Storage locations" is the summary of the copy inventory, not a guess.
- A review **date**, not a cadence. A date is diariable.

## 2. ROPA time-limit column

Art 30(1)(f) asks for "the envisaged time limits for erasure of the different categories of data". Fill it per category:

```
Billing and invoicing data — 8 years from the end of the calendar year in which the
  invoice was issued (§ 14b Abs 1 UStG, § 147 Abs 3 S 1 AO); once the commercial purpose
  ends the data is restricted under Art 18 and accessible only to finance and legal.
Marketing consent records — for the duration of the consent, plus 3 years after
  withdrawal to evidence that the withdrawal was honoured. Criteria rather than a fixed
  date, because the start depends on the subject's act.
```

Never write "n/a", "see policy" or "as required by law" in this column.

## 3. Privacy-notice sentence

Art 13(2)(a) requires the period or the criteria. Hand the legal-text skill one finished sentence per processing activity, in the publication language. Two patterns: `[[Category]]` wird `[[period]]` ab `[[start event]]` gespeichert (`[[statute]]`), or `[[Category]]` wird gespeichert, solange `[[condition]]`; danach `[[what happens]]`.

> Rechnungs- und Buchhaltungsdaten werden acht Jahre ab dem Ende des Kalenderjahrs der Rechnungsausstellung gespeichert (§ 14b Abs 1 UStG, § 147 Abs 3 AO). Nach Wegfall des ursprünglichen Zwecks werden sie in der Verarbeitung eingeschränkt und nur noch für steuerliche und rechtliche Zwecke verwendet.

> Support tickets are kept until the ticket is closed and for a further 12 months, so that a follow-up request can be linked to the earlier contact. Attachments are deleted with the ticket.

Fails Art 13(2)(a): "as long as necessary", "in line with statutory retention periods", "for the duration of the business relationship" with nothing following.

## 4. Erasure-request runbook

```
<!-- DRAFT - not legally approved -->

REQUEST [[id]]   RECEIVED [[date]]   DUE [[received + 1 month, Art 12(3)]]
SUBJECT [[identifier used to locate records]]
VERIFIED BY [[method]] ON [[date]]

0  Verify identity. Do not act on an unverified request; do not demand more data
   than needed to verify (Art 12(6), Art 11).
1  Locate. Run the subject-lookup query across every system in the copy inventory.
   Record what was found AND what was searched but empty.
2  Classify each element found:
     ERASE    - no statutory minimum, or the minimum has expired
     RESTRICT - minimum still running; Art 17(3)(b) applies
     REFUSE   - another Art 17(3) ground applies; name it
   Record the citation next to every RESTRICT and REFUSE.
3  Suppress inbound syncs (CDP, reverse ETL, identity resolution) BEFORE deleting
   anything downstream, or the CRM repopulates from the warehouse within the hour.
4  Execute ERASE in the primary store. Record rows affected.
5  Execute RESTRICT: set restricted_at; verify invisible to the application role
   and still visible to finance and legal.
6  Fan out: search index (delete + force merge), caches, read models, materialised
   views, warehouse, message topics (tombstones).
7  Fan out to processors, deepest first. Record API response or ticket reference each.
8  Add the subject to the backup suppression list.
9  Evidence pack: per-system result, timestamps, operator, residual set with its
   legal basis and end date.
10 Respond within one month (Art 12(3)): what was erased; what is retained, under
   which statute, until which date, and that it is restricted under Art 18; the date
   backups age out; the right to complain (Art 77).

ESCALATE if identity cannot be verified, a litigation hold applies, a processor
cannot delete at subject granularity, or one month is not achievable (two further
months possible under Art 12(3) with reasons, notified inside the first month).
```

## 5. Restriction-of-processing design note

```
<!-- DRAFT - not legally approved -->

PURPOSE   Implement the Art 18 state for [[system]], so records under a statutory
          retention duty survive an Art 17 request without remaining in processing.

SCHEMA    restricted_at         timestamptz NULL
          restricted_reason     text        NULL  -- art17_request | art18_1b | litigation_hold
          retention_until       date        NOT NULL
          restriction_lifted_at timestamptz NULL

ENFORCEMENT
  Row-level security, not a WHERE clause. The application role must be unable to read
  restricted rows even when the predicate is omitted; finance and legal read without it.
  Rationale: Art 18(2) permits storage plus processing for the establishment, exercise
  or defence of legal claims. Any other path is unlawful, and a forgotten predicate is
  the normal way that happens.

MUST NOT SEE RESTRICTED ROWS
  [[search index, recommendations, marketing exports, support UI, analytics events,
    warehouse loads, LLM context assembly, backfill jobs]]

MUST SEE THEM
  [[finance export, tax audit extract, legal-claims lookup]]

LIFTING (Art 18(3))
  Only by an explicit operation that notifies the data subject BEFORE the lift.
  Never a side effect of a migration or a backfill.

EXPIRY
  When retention_until passes, the row is hard-deleted by [[job]], not returned to live.

OPEN  [[MISSING: which roles exist today and whether RLS is available on this engine]]
```

## 6. Deletion-job specification

```
<!-- DRAFT - not legally approved -->

JOB       [[name]]        SCHEDULE [[cron]]        OWNER [[team]]
SCOPE     [[data elements and systems]]
PREDICATE [[exact condition, with the period start explicitly defined]]

SEMANTICS
  Idempotent - re-running produces no additional effect
  Resumable  - interruption loses at most one batch
  Batched    - [[n]] rows per transaction, [[m]] ms between batches
  Bounded    - max [[k]] rows per run; exceeding it alerts instead of running
               unbounded, because that means the predicate changed

SAFETY
  Dry-run mode reports counts without deleting; required before any predicate change.
  Refuses to run if the predicted count exceeds [[threshold]]% of the table.
  Respects litigation holds: [[how the hold is expressed and checked]].

OUTPUT (every run, to [[destination]])
  job, started_at, finished_at, rows_examined, rows_deleted, rows_skipped,
  oldest_surviving_timestamp, errors

MONITORING
  Alert if no successful completion within [[interval]].
  Alert if oldest_surviving_timestamp exceeds the retention period.
  Alert if rows_deleted is zero for [[n]] consecutive runs on a table that receives
  writes - that means the predicate has stopped matching.

EVIDENCE
  Run log retained [[period]] as the Art 5(2) accountability record, and the run log
  itself has a row in the schedule.

VERIFICATION QUERY (must return zero)
  [[the query from checklist.md for this element]]

OPEN  [[MISSING: alert destination]]  [[MISSING: threshold values]]
```

## Checkpoints

- [ ] One row per data element, citation on every minimum, reasoning on every maximum
- [ ] Elements with no statutory minimum say "none", not a conservative guess
- [ ] Elements with minimum > maximum carry a two-stage mechanism
- [ ] Every row has a named owner and a dated review
- [ ] ROPA time-limit column filled per category, no "n/a"
- [ ] One publication-ready sentence per activity, stating a period or explicit criteria
- [ ] Runbook distinguishes ERASE, RESTRICT and REFUSE with a citation for each non-erasure
- [ ] Subject response states the residual set, its statute and its end date
- [ ] Restriction enforced by grants or RLS, with visible and invisible paths both listed
- [ ] Every job spec has a verification query that must return zero
- [ ] Draft marker present on every artefact, unless sign-off is recorded
