# Processors and cascading deletion

Every processor holds a copy. Art 28(3)(g) governs what happens to it at the end of the engagement, and nothing else in the GDPR obliges the processor to run your retention schedule for you. That gap is where most of the surviving data lives.

## Art 28(3)(g) — what it actually requires

The processing contract must stipulate that the processor, **at the choice of the controller, deletes or returns all the personal data to the controller after the end of the provision of services relating to processing, and deletes existing copies unless Union or Member State law requires storage of the personal data**.

Three things engineers read into it that are not there:

| Assumption | Reality |
|---|---|
| "The processor deletes on our schedule" | The duty triggers at the end of the engagement, not on your retention dates. Running retention inside the processor is a separate contractual and configuration matter. |
| "Deletion is automatic on termination" | The controller must **choose** delete or return. Absent a choice, the processor's default (often "retain for N days then delete") governs. Make the choice in writing before termination. |
| "It covers everything" | It covers what the processor holds as processor. Data the vendor holds as its own controller — billing records, security logs, abuse-monitoring copies — is outside it and has its own retention. |

The carve-out "unless Union or Member State law requires storage" is the same structure as Art 17(3)(b): the processor's own statutory retention survives your instruction.

## Sub-processors

Art 28(2) and 28(4) put the sub-processor chain on the processor, but your copy inventory does not stop at the first hop. For each processor, record:

- the current sub-processor list and where it is published
- whether you receive advance notice of changes and can object
- whether the deletion instruction propagates contractually to sub-processors
- which sub-processors are in third countries and on which transfer mechanism

A processor that cannot tell you where the data physically is cannot tell you that it has been deleted.

## Building the deletion path per processor

For each entry in the copy inventory, record the following before you need it:

| Field | Why |
|---|---|
| Deletion API or process | a support ticket is a valid answer, but it changes the achievable SLA |
| Granularity | per-subject, per-record, per-account, or account-teardown only |
| Documented turnaround | this is what you can promise under Art 12(3) |
| Evidence produced | API response, confirmation email, audit-log entry, or nothing |
| Vendor's own retention floor | logs and backups the vendor keeps regardless of your instruction |
| Whether deletion propagates to their sub-processors | otherwise the chain is broken one hop down |
| Contract clause reference | so termination does not become a negotiation |

Vendors whose only granularity is account teardown are a structural problem for subject erasure: you cannot satisfy an individual request without terminating the whole integration. Identify them at procurement, not at request time.

## The end-of-engagement runbook

Run this whenever a processor relationship ends, including a quiet one — a tool nobody logs into any more is still a processor holding data.

1. Issue the Art 28(3)(g) instruction **in writing**, naming the choice: delete, or return then delete.
2. If return: agree the format, the transfer channel and the verification method before the data moves. A returned export is a new copy in your inventory.
3. Require written confirmation of deletion, with a date, covering the processor and its sub-processors.
4. Ask explicitly what is retained under the law-requires-storage carve-out, on which legal basis, and for how long. Record the answer in the schedule.
5. Ask explicitly about backups: rotation window, and when the last restorable copy ages out. That date, not the confirmation date, is when the data is gone.
6. Revoke credentials, API keys, OAuth grants, webhooks and IP allowlist entries. A live integration key is a live data flow.
7. Remove the processor from the ROPA, the privacy notice's recipient list, and the transfer register.
8. Diary the backup-expiry date and confirm again at that point.
9. Archive the confirmation with the contract. It is the evidence for Art 5(2).

## Cascading a subject erasure across the stack

Order matters, because a deletion in one system can be undone by a sync from another.

1. **Freeze the inbound syncs first.** Suppress the subject in the CDP, reverse-ETL and any identity-resolution tool. Otherwise the CRM repopulates from the warehouse an hour after you delete it.
2. **Delete or restrict in the primary store**, applying the minimum/maximum resolution per element. Some elements are erased, others move to restricted. Record which is which.
3. **Fan out to derived stores**: search index (then force merge), caches, read models, materialised views.
4. **Fan out to processors** in dependency order, deepest first, so nothing is re-synced from a system you have already cleaned.
5. **Handle append-only stores**: tombstone compacted topics, schedule warehouse rewrites, wait out log retention.
6. **Add to the backup suppression list** so a restore does not reintroduce the data.
7. **Collect evidence per hop** and store it against the request.
8. **Respond to the subject** within Art 12(3), stating what was erased, what is retained under Art 17(3)(b) with the legal basis and until when, and that the retained data is restricted under Art 18.

Step 8 is the one most often skipped. Telling a data subject that everything was deleted while the invoice remains is a false statement; telling them the invoice is retained until a stated date under a named statute is a complete and defensible answer.

## Template: Art 28(3)(g) instruction

```
<!-- DRAFT - not legally approved -->

To:      [[processor legal entity]]
From:    [[controller legal entity]]
Date:    [[date]]
Subject: Instruction under Article 28(3)(g) GDPR - [[service name]], contract [[reference]]

The provision of services under the above contract ends on [[date]].

In accordance with Article 28(3)(g) GDPR and clause [[clause reference]] of the
data processing agreement, we instruct you to [[DELETE / RETURN AND THEN DELETE]]
all personal data processed on our behalf, and to delete all existing copies.

Where you rely on the exception for storage required by Union or Member State law,
please identify: the data concerned, the legal provision relied on, and the date
on which that obligation expires.

Please confirm in writing, by [[date]]:

1. that the deletion has been carried out, and on which date;
2. that the instruction has been passed to and executed by all sub-processors,
   with each named;
3. the date on which the last backup copy containing this data will have aged out
   of your backup rotation;
4. any data retained under the legal-storage exception, per point above.

Contact for this instruction: [[name, role, email]]
```

## Checkpoints

- [ ] Complete processor list, each with a signed Art 28(3) contract on file
- [ ] Sub-processor list obtained and dated for each processor
- [ ] Deletion granularity recorded per processor; account-teardown-only vendors flagged
- [ ] Documented turnaround recorded per processor and reflected in the Art 12(3) plan
- [ ] Vendor's own retention floor recorded, including abuse-monitoring and security-log copies
- [ ] Erasure fan-out order defined so no system re-syncs deleted data
- [ ] Inbound syncs suppressed before, not after, the primary deletion
- [ ] Backup suppression list updated as part of every erasure
- [ ] Evidence collected per hop and stored against the request
- [ ] Subject response distinguishes erased data from data retained under Art 17(3)(b), with the statute and the end date
- [ ] End-of-engagement runbook executed for every terminated processor, including dormant tools
