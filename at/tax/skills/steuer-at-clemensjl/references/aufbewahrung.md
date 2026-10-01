# Records and retention

Basis: § 132 BAO, § 132a Abs 6 BAO, § 11 Abs 2 UStG, § 7 Abs 3 RKSV. Consolidated versions as at 2026-08-05 (RIS).

## The period

> "Bücher und Aufzeichnungen sowie die zu den Büchern und Aufzeichnungen gehörigen Belege sind **sieben Jahre** aufzubewahren; darüber hinaus sind sie noch so lange aufzubewahren, als sie für die Abgabenerhebung betreffende anhängige Verfahren von Bedeutung sind, in denen diejenigen Parteistellung haben, für die auf Grund von Abgabenvorschriften die Bücher und Aufzeichnungen zu führen waren …" — § 132 Abs 1 BAO

- Business papers and other documents relevant to tax collection **should** likewise be kept seven years.
- **The clock starts at the end of the calendar year**: for books and records, the end of the year for which the entries were made; for belegs, business papers and other documents, the end of the year they relate to. With a non-calendar Wirtschaftsjahr, from the end of the calendar year in which that year ends.
- The period **extends** for as long as the material matters to a pending tax proceeding. A deletion job keyed purely on "seven years" will delete evidence out from under an open audit. Build a legal-hold flag.

Not seven years everywhere: this is the tax retention period. Other periods run in parallel under other statutes, and GDPR storage limitation runs against them. Where they conflict, the retention duty is a legal obligation under Art 6 Abs 1 lit c GDPR — but the scope must be limited to what the duty actually covers. Privacy-notice wording for that belongs to `legal-at`.

| Object | Period | Basis |
|---|---|---|
| Books, records, and their belegs | 7 years from the end of the calendar year | § 132 Abs 1 BAO |
| Invoice copies (Durchschrift/Abschrift) and documents referred to in the invoice | 7 years | § 11 Abs 2 UStG |
| Electronic invoices — authenticity, integrity, legibility | 7 years | § 11 Abs 2 UStG |
| Beleg duplicates under § 132a and the Abs 4 records | 7 years from the end of the year of issue, starting at receipt creation | § 132a Abs 6 Z 1 BAO |
| DEP quarterly backups, Startbeleg with its check result, Jahresbeleg, Schlussbeleg | per § 132 BAO | §§ 6 Abs 4, 7 Abs 3, 8 Abs 3, 17 Abs 8 RKSV |

## Electronic form — what § 132 Abs 2 and 3 actually require

> "Hinsichtlich der in Abs. 1 genannten Belege, Geschäftspapiere und sonstigen Unterlagen kann die Aufbewahrung auf **Datenträgern** geschehen, wenn die **vollständige, geordnete, inhaltsgleiche und urschriftgetreue Wiedergabe** bis zum Ablauf der gesetzlichen Aufbewahrungsfrist **jederzeit** gewährleistet ist. Soweit solche Unterlagen nur auf Datenträgern vorliegen, entfällt das Erfordernis der urschriftgetreuen Wiedergabe." — § 132 Abs 2 BAO

> "Wer Aufbewahrungen in Form des Abs. 2 vorgenommen hat, muß … **auf seine Kosten** innerhalb angemessener Frist diejenigen **Hilfsmittel zur Verfügung stellen**, die notwendig sind, um die Unterlagen lesbar zu machen, und, soweit erforderlich, ohne Hilfsmittel lesbare, dauerhafte Wiedergaben beibringen. Werden dauerhafte Wiedergaben erstellt, so sind diese **auf Datenträgern zur Verfügung zu stellen**." — § 132 Abs 3 BAO

Read as software requirements:

- **complete** — no partial archive, no "only the last three years online"
- **ordered** — retrievable by a comprehensible ordering, not a bucket of blobs with random keys
- **content-identical** — the stored representation carries the same content as issued
- **true to the original** — required for documents that also exist on paper; **not** required for documents that only ever existed digitally
- **at any time** — availability within the whole seven years, not on a restore-from-cold-storage-in-three-weeks basis
- **at the taxpayer's cost** the tools to make the data legible must be provided, and permanent reproductions supplied **on a data carrier**

## What this means for a SaaS storing invoices

1. **The tenant, not the vendor, carries the duty.** § 132 BAO binds the taxpayer. A vendor that deletes a tenant's invoices on account closure puts the tenant in breach. Contract for an export at termination and for a retention window; state it in the DPA and the terms.
2. **Export must be usable, not just present.** A ZIP of PDFs named by internal UUID is neither ordered nor practically legible. Ship a structured export (CSV or XML) plus the rendered documents plus a manifest linking them.
3. **Keep the structured data, not only the render.** The rendered PDF is content-identical only if it carries everything. Where the source of truth is a database row, that row must survive, or the render must be complete on its face.
4. **Format longevity is your problem.** Seven years is longer than most schema lifetimes. Store an immutable rendered form alongside the structured form and version the schema.
5. **Integrity for electronic invoices.** § 11 Abs 2 UStG requires authenticity of origin, integrity of content and legibility for the full seven years. Content-addressed storage with hashes recorded at issue, WORM buckets or object-lock, and an append-only audit log are the ordinary ways to evidence this. The BMF may specify by regulation the conditions under which those requirements are in any case met.
6. **Legal hold beats the retention timer.** Model retention as `max(statutory_expiry, legal_hold_until)` and require an explicit release.
7. **Deletion is an event, not a side effect.** Log what was deleted, when, and under which rule.

## Skeleton — retention metadata per document

```json
{
  "document_id": "[[uuid]]",
  "document_type": "invoice | beleg | dep_backup | jahresbeleg",
  "issued_at": "2026-03-14T10:22:41+01:00",
  "fiscal_year": 2026,
  "retention_basis": "§ 132 Abs 1 BAO",
  "retention_starts": "2026-12-31",
  "retention_expires": "2033-12-31",
  "legal_hold_until": null,
  "content_sha256": "[[hex]]",
  "storage": { "immutable": true, "object_lock_until": "2033-12-31" },
  "structured_source": "[[pointer to the structured record]]",
  "rendered_form": "[[pointer to the PDF]]"
}
```

## Checkpoints

- [ ] Retention computed from the **end of the calendar year**, not from the document date
- [ ] Seven years, not ten; the German § 147 AO period is not the Austrian one
- [ ] Legal-hold flag exists and blocks deletion regardless of the expiry date
- [ ] Archive is complete, ordered, content-identical and available at any time within the period
- [ ] Export to a data carrier produces a legible, ordered set plus a manifest
- [ ] Structured record retained, not only the rendered PDF
- [ ] Hash recorded at issue and verifiable later; storage is immutable or object-locked
- [ ] Electronic invoices: authenticity, integrity and legibility evidenced across the full period
- [ ] Recipient consent to electronic invoicing recorded (§ 11 Abs 2 UStG)
- [ ] DEP backups written at least quarterly to external media and included in the retention scheme
- [ ] Termination and deletion behaviour for tenant data documented in the contract, not only in code
- [ ] Deletion events logged with the rule applied
