# Implementation — rounding, formatting, numbering, cancellation, output

The statutory requirements above translate into a handful of engineering decisions that are wrong by default in most stacks. Basis for each rule is named inline.

## Money representation

Never floating point. Use a decimal type with an explicit scale, or integer minor units. `0.1 + 0.2` in binary floating point is not `0.3`, and § 11 Abs 1 Z 3 lit f UStG requires the tax amount attributable to the Entgelt — an amount that must reconcile exactly.

```python
from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")

def round_cent(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)
```

Use `ROUND_HALF_UP` (kaufmännisches Runden), not banker's rounding. Python's `round()` and `Decimal`'s default `ROUND_HALF_EVEN` both round `2.675` to `2.67`; commercial practice and every Austrian accounting package round to `2.68`.

## Rounding order

Pick **one** order and apply it everywhere, because the invoice must reconcile:

1. round each **line** net amount to the cent
2. **sum** line nets **per tax rate** into a per-rate tax base
3. compute the **tax per rate** from the rounded per-rate base, and round that
4. the invoice total is the sum of the per-rate bases plus the sum of the per-rate taxes

Computing tax per line and summing the rounded per-line taxes produces a different figure from taxing the rounded per-rate base. Both are defensible in isolation; mixing them within one document is not, because the printed Steuerbetrag then does not equal base × rate and the recipient's audit flags it.

Gross-priced catalogues (consumer shops must show gross under PrAG and § 5 Abs 2 ECG) invert the arithmetic:

```python
def net_from_gross(gross: Decimal, rate: Decimal) -> Decimal:
    return round_cent(gross / (Decimal(1) + rate))

def tax_from_gross(gross: Decimal, rate: Decimal) -> Decimal:
    return round_cent(gross - net_from_gross(gross, rate))
```

Derive tax as `gross − net`, never as `net × rate` computed separately, or the three printed figures will not add up.

Rates as exact decimals: `Decimal("0.20")`, `Decimal("0.13")`, `Decimal("0.10")`, `Decimal("0.049")`. Note that 4,9 % is a three-decimal rate — a schema with `numeric(3,2)` for rates cannot hold it.

## Austrian formatting

| Item | Austrian form | Common wrong form |
|---|---|---|
| Decimal separator | comma — `1.234,56` | dot |
| Thousands separator | dot — `1.234,56` | comma or thin space |
| Currency | `1.234,56 €` or `EUR 1.234,56` | `€1,234.56` |
| Date | `14.03.2026` or ISO `2026-03-14` | `03/14/2026` |
| Locale tag | `de-AT` | `de-DE` (same numerals, different defaults elsewhere) |

```javascript
new Intl.NumberFormat("de-AT", { style: "currency", currency: "EUR" }).format(1234.56);
// "€ 1.234,56"
new Intl.DateTimeFormat("de-AT").format(new Date("2026-03-14"));
// "14.3.2026"
```

Two exceptions where the Austrian display format must **not** be used:

- the **RKSV signature payload** requires JSON `number` with 2 decimals and ISO 8601 `JJJJ-MM-TT'T'hh:mm:ss` **without time zone**, Austrian local time assumed (RKSV Anlage Z 4). Never feed a locale-formatted string into the signature.
- **structured e-invoice formats** (ebInterface, UBL) carry their own canonical representations.

Locale detail carried by a wider skill: general i18n and locale correctness belongs to `i18n-locale-correctness`; only the tax-document constraints are stated here.

## Sequential numbering that survives concurrency and gaps

§ 11 Abs 1 Z 3 lit h UStG: "eine fortlaufende Nummer mit einer oder mehreren Zahlenreihen, die zur Identifizierung der Rechnung einmalig vergeben wird". § 132a Abs 3 Z 2 BAO says the same for the Beleg, identifying the Geschäftsvorfall.

Rules that follow:

- **Several series are allowed.** Per branch, per year, per document type. What is not allowed is a series with unexplainable holes.
- **Allocate the number in the same transaction that persists the document.** A number handed out and then abandoned on a rollback is a gap nobody can explain three years later.
- **Drafts must not consume numbers.** Number on issue, not on creation.
- **Never derive the number from a timestamp, a UUID or a hash.** Those are unique but not fortlaufend.
- **Never allocate client-side.** Two tabs produce two documents with the same number.

Portable pattern, correct under concurrency, no gaps on rollback because the counter row is locked for the duration of the transaction:

```sql
CREATE TABLE invoice_counter (
  series   text PRIMARY KEY,
  next_val bigint NOT NULL
);

BEGIN;
  UPDATE invoice_counter
     SET next_val = next_val + 1
   WHERE series = '2026'
  RETURNING next_val - 1 AS assigned;

  INSERT INTO invoice (number, series, issued_at, ...)
  VALUES (format('%s-%06s', '2026', assigned), '2026', now(), ...);
COMMIT;
```

Do **not** use a database `SEQUENCE` for this: sequences are deliberately non-transactional and burn values on rollback, which is exactly the gap you must avoid. The row lock serialises invoice issue within a series — acceptable, because issuing is not a hot path and correctness outranks throughput here.

Where a gap does arise (an outage, a migration), **document it** — a written note of the cause, retained with the records under § 132 BAO, is the answer to the auditor's question.

## An issued document is never edited

§ 11 Abs 12 UStG: a tax amount shown that is not owed for the supply **is owed on the strength of the document**, unless the invoice is corrected towards the recipient; § 16 Abs 1 applies analogously to the correction. § 11 Abs 14: showing a tax amount without making a supply, or without being an Unternehmer, means owing that amount.

So:

| Situation | Correct handling |
|---|---|
| Invoice not yet sent, error found | still a new document if a number was allocated; otherwise fix the draft before issue |
| Wrong amount, wrong rate, wrong recipient | **Storno** — a separate document with its own number, referencing the original, reversing it, then a new correct invoice |
| Price reduction agreed later | credit note / Gutschrift referencing the original |
| Recipient details wrong only | corrected invoice referencing the original, with the original expressly cancelled |

Two distinct meanings of "Gutschrift" collide here and must not be conflated:

- a **credit note** reducing a claim, and
- the **Gutschrift as a self-billing document** under § 11 Abs 7 and 8 UStG, where the recipient settles the supply. That one counts as the supplier's invoice, needs prior agreement between the parties, must be labelled as a Gutschrift, must carry the Abs 1 and Abs 1a data, must reach the supplier, and loses invoice effect to the extent the supplier objects to the tax amount shown.

In the Registrierkasse, a cancellation is not a deletion: § 7 Abs 2 RKSV requires Trainings- and Stornobuchungen to be captured and stored **like Barumsätze**, they must be signed (§ 9 Abs 1), the machine-readable code must carry the word `Stornobuchung` (§ 10 Abs 3), and the receipt must be expressly labelled (§ 11 Abs 3).

Storage model: documents are **append-only**. A `status` column (`issued`, `cancelled`) plus a `cancelled_by_document_id` link. No `UPDATE` on amounts, rates or numbers after issue.

## Storing the signature chain

From `registrierkasse.md`, restated as a data requirement:

- persist the full **JWS compact string** per receipt, not just the signature value — Anlage Z 11 makes it the mandatory DEP field `JWS-Kompakt`
- persist the certificate and the CA chain, or a reference resolving to them, so the Anlage Z 3 export can be produced
- persist the **DEP storage order**; the export must preserve it and the chaining from position *x* to *x+1* must hold
- guard chain construction with a **lock**: the Anlage requires explicitly that "durch den Einsatz von Zugriffsteuerungsmethoden … auch bei der parallelen Abarbeitung der Belegerstellung die Verkettung über die Signatur- bzw. Siegelwerte korrekt abgebildet wird" (Anlage Z 4 and Z 11). Two concurrent receipts reading the same predecessor break the chain irrecoverably.
- the Umsatzzähler is a **monotonic counter excluding Trainingsbuchungen** (§ 8 Abs 1 RKSV), encrypted per receipt with AES-256-ICM using an IV derived from `Kassen-ID` + `Belegnummer` — never reuse an IV under one key (Anlage Z 9)

## PDF plus machine-readable payload

- Render the PDF from the **persisted structured record**, never from live-recomputed figures. A re-render two years later must be byte-identical in content.
- Embed or attach the structured payload where the counterparty can use it; keep the structured record regardless, because § 132 Abs 2 BAO wants content-identical reproduction and the PDF alone may not carry everything.
- Use **PDF/A** for archival. It is not a legal requirement in Austria — § 132 Abs 2 BAO speaks of complete, ordered, content-identical reproduction, not of a format — but it is the ordinary way to evidence it over seven years.
- Embed fonts. A PDF that renders differently in 2033 because a font is missing is not content-identical.
- Record a **SHA-256 of the issued document** at issue time, and store it alongside. That is the cheap evidence of integrity under § 11 Abs 2 UStG.
- The QR code on a Registrierkasse receipt is **not** a payment QR code (EPC/Girocode) and must not be replaced by one. Two codes may coexist if labelled.

## Checkpoints

- [ ] All money in decimal or integer minor units; no float anywhere in the tax path
- [ ] `ROUND_HALF_UP` used throughout, not banker's rounding
- [ ] One rounding order chosen, documented, and applied identically on invoice, receipt and export
- [ ] Gross-priced flows derive tax as `gross − net`, so the three printed figures reconcile
- [ ] Rate column can hold `0.049`; no `numeric(3,2)` on rates
- [ ] Output uses `de-AT` formatting; RKSV payload and structured e-invoices use their own canonical forms
- [ ] Numbers allocated inside the persisting transaction, from a locked counter row, not a `SEQUENCE`
- [ ] Drafts do not consume numbers; no client-side allocation
- [ ] Any gap in a series has a written, retained explanation
- [ ] Issued documents are append-only; corrections are separate numbered documents referencing the original
- [ ] Self-billing Gutschrift under § 11 Abs 7 and 8 UStG not conflated with a credit note
- [ ] Storno in the Registrierkasse is a signed, labelled booking, never a deletion
- [ ] Full `JWS-Kompakt` string persisted per receipt, with certificates resolvable for the DEP export
- [ ] Chain construction serialised by a lock; no two receipts share a predecessor
- [ ] Umsatzzähler excludes Trainingsbuchungen; AES IV never reused under one key
- [ ] PDF rendered from the persisted structured record, fonts embedded, SHA-256 recorded at issue
- [ ] Receipt QR code is the RKSV code, not a payment code
