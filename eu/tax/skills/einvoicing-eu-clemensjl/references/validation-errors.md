# Validation errors: rule ID → cause → fix

Rule identifiers and messages reproduced verbatim from the EN 16931 validation artefacts **v1.3.16** (`schematron/abstract/EN16931-model.sch`, `schematron/UBL/EN16931-UBL-model.sch`) and from the Peppol BIS Billing 3.0 rule set (docs.peppol.eu/poacc/billing/3.0/rules/, November 2025 release). Messages carry the `[BR-xx]-` prefix in the actual output.

Rule families and where they come from:

| Prefix | Source | Meaning |
|---|---|---|
| `BR-nn` | EN 16931 | Presence and cardinality |
| `BR-CO-nn` | EN 16931 | Cross-field consistency and totals |
| `BR-DEC-nn` | EN 16931 | Maximum decimals for a monetary amount (21 rules, all "the allowed maximum number of decimals … is 2") |
| `BR-S-`, `BR-Z-`, `BR-E-`, `BR-AE-`, `BR-IC-`, `BR-G-`, `BR-O-` | EN 16931 | Per VAT category |
| `PEPPOL-EN16931-Rnnn` | Peppol CIUS | Peppol-only restrictions |
| `DE-R-nnn` | German national rules inside the Peppol/XRechnung profile | German-only restrictions |

## The calculation rules that reject most first attempts

These are the reason a first invoice fails. Note precisely which have a tolerance and which do not — verified against the Schematron test expressions.

| Rule | Message | Tolerance | Fix |
|---|---|---|---|
| `BR-CO-10` | Sum of Invoice line net amount (BT-106) = Σ Invoice line net amount (BT-131). | **None.** Test is exact equality after `round(sum(...) * 100) div 100` | Round each line net amount to 2 decimals first, then sum. Do not sum at full precision and round once. |
| `BR-CO-13` | Invoice total amount without VAT (BT-109) = Σ Invoice line net amount (BT-131) - Sum of allowances on document level (BT-107) + Sum of charges on document level (BT-108). | **None.** Exact after rounding to 2 decimals | If there are no document-level allowances or charges, BT-109 must equal BT-106 exactly. |
| `BR-CO-14` | Invoice total VAT amount (BT-110) = Σ VAT category tax amount (BT-117). | None | Compute BT-110 from the breakdown, not from the lines. |
| `BR-CO-15` | Invoice total amount with VAT (BT-112) = Invoice total amount without VAT (BT-109) + Invoice total VAT amount (BT-110). | None | Never compute BT-112 independently. |
| `BR-CO-16` | Amount due for payment (BT-115) = Invoice total amount with VAT (BT-112) - Paid amount (BT-113) + Rounding amount (BT-114). | None | If nothing was prepaid and there is no rounding amount, BT-115 must equal BT-112 exactly. |
| `BR-CO-17` | VAT category tax amount (BT-117) = VAT category taxable amount (BT-116) x (VAT category rate (BT-119) / 100), rounded to two decimals. | **± 1 currency unit** — the test asserts `abs(TaxAmount) - 1 < computed` and `abs(TaxAmount) + 1 > computed` | This is the only meaningful tolerance in the standard. It exists to absorb line-level rounding differences. Do not rely on it for anything larger. |
| `BR-S-09` (and the `-09` rule in each category family) | Standard rated VAT tax amount = taxable amount × rate | ± 1 currency unit, same construction | Same as BR-CO-17. |
| `BR-S-08` (and each category's `-08`) | Per rate, the VAT category taxable amount equals the sum of line net amounts plus charges minus allowances at that rate | ± 1 currency unit | Build the breakdown by grouping lines on (category, rate). |

**The one rounding rule to build against:** round every monetary value to 2 decimals at the point it enters the document (BR-DEC-*, 21 rules), aggregate the *rounded* values, and let the ±1 tolerance in BR-CO-17 absorb the residual VAT difference. Aggregating at full precision fails BR-CO-10 and BR-CO-13.

## Presence rules

| Rule | Message | Fix |
|---|---|---|
| `BR-01` | An Invoice shall have a Specification identifier (BT-24). | Populate `cbc:CustomizationID` with the exact target string. |
| `BR-02` | An Invoice shall have an Invoice number (BT-1). | `cbc:ID`. Not the internal database key unless it is the legal sequential number under Art 226(2). |
| `BR-03` | An Invoice shall have an Invoice issue date (BT-2). | `YYYY-MM-DD` in UBL, `format="102"` `YYYYMMDD` in CII. |
| `BR-04` | An Invoice shall have an Invoice type code (BT-3). | `380` normally. |
| `BR-05` | An Invoice shall have an Invoice currency code (BT-5). | ISO 4217. |
| `BR-06` / `BR-07` | An Invoice shall contain the Seller name (BT-27) / the Buyer name (BT-44). | `cac:PartyLegalEntity/cbc:RegistrationName`. `cac:PartyName/cbc:Name` is the trading name and does not satisfy this. |
| `BR-08` / `BR-10` | An Invoice shall contain the Seller / Buyer postal address. | Address group must exist even when only the country is known. |
| `BR-09` / `BR-11` | The Seller / Buyer postal address shall contain a country code (BT-40 / BT-55). | ISO 3166-1 alpha-2. |
| `BR-12` … `BR-15` | An Invoice shall have BT-106 / BT-109 / BT-112 / BT-115. | All four totals, always, even when zero. |
| `BR-16` | An Invoice shall have at least one Invoice line (BG-25). | A zero-line invoice is not valid. |
| `BR-CO-18` | An Invoice shall at least have one VAT breakdown group (BG-23). | One `cac:TaxSubtotal` per (category, rate). |
| `BR-CO-25` | If Amount due for payment (BT-115) is positive, either Payment due date (BT-9) or Payment terms (BT-20) shall be present. | Ship a payment terms note if you have no due date. |
| `BR-CO-26` | In order for the buyer to automatically identify a supplier, the Seller identifier (BT-29), the Seller legal registration identifier (BT-30) and/or the Seller VAT identifier (BT-31) shall be present. | At least one of the three. A small business with no VAT number needs BT-30. |
| `BR-CO-09` | The Seller VAT identifier (BT-31), the Seller tax representative VAT identifier (BT-63) and the Buyer VAT identifier (BT-48) shall have a prefix in accordance with ISO code ISO 3166-1 alpha-2 … Nevertheless, Greece may use the prefix 'EL'. | Store VAT identifiers with the country prefix. Greece is `EL`, not `GR`. |
| `BR-31` … `BR-38`, `BR-CO-21` … `BR-CO-24` | Each allowance/charge needs an amount, a VAT category code and a reason or reason code | Never emit an allowance with only an amount. |
| `BR-52` | Each Additional supporting document (BG-24) shall contain a Supporting document reference (BT-122). | Attachments need an identifier. |
| `BR-57` | Each Deliver to address (BG-15) shall contain a Deliver to country code (BT-80). | Required for intra-Community supplies via BR-IC-12. |
| `BR-63` | The Buyer electronic address (BT-49) shall have a Scheme identifier. | `schemeID` from the EAS list. |

## VAT category rules

The seven families are structurally identical. For category `X`:

| Suffix | Requirement |
|---|---|
| `-01` | An invoice with any line, allowance or charge in category X shall contain a VAT breakdown for X (exactly one for Z, E, AE, K, G, O) |
| `-02` / `-03` / `-04` | Identifier requirements on line / allowance / charge |
| `-05` / `-06` / `-07` | Rate constraint: > 0 for S; = 0 for Z, E, AE, K, G; absent for O |
| `-08` | Taxable amount equals sum of line net amounts + charges − allowances in that category and rate (± 1) |
| `-09` | Tax amount equals taxable amount × rate (± 1); 0 for Z, E, AE, K, G, O |
| `-10` | Exemption reason: forbidden for S and Z, **required** for E, AE, K, G, O |

Frequent failures:

- **`BR-AE-02`** — reverse charge lines require the seller VAT identifier (or tax registration, or tax representative VAT) **and** the buyer VAT identifier or buyer legal registration identifier. Sending a reverse-charge invoice without the buyer's VAT number fails.
- **`BR-IC-11` / `BR-IC-12`** — an intra-Community supply needs an actual delivery date or an invoicing period, **and** a deliver-to country code (BT-80). Most first attempts omit BT-80.
- **`BR-O-02`** — for "Services outside scope of tax" the invoice must **not** contain seller or buyer VAT identifiers. This is the opposite of every other category and surprises everyone.
- **`BR-O-11` … `BR-O-14`** — an invoice using category O may contain only that one breakdown group and no lines, allowances or charges in any other category. O cannot be mixed.
- **`BR-E-10`** — exempt without a reason. Supply a VATEX code (`identifiers.md`) or free text.

## Peppol-only rules

| Rule | Message | Fix |
|---|---|---|
| `PEPPOL-EN16931-R001` | Business process MUST be provided. | Add `cbc:ProfileID`. |
| `PEPPOL-EN16931-R004` | Specification identifier MUST have the value 'urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0'. | The plain EN 16931 identifier is rejected on Peppol. |
| `PEPPOL-EN16931-R003` | A buyer reference or purchase order reference MUST be provided. | BT-10 or BT-13. Not optional on Peppol even though it is in the core standard. |
| `PEPPOL-EN16931-R007` | Business process MUST be in the format 'urn:fdc:peppol.eu:2017:poacc:billing:NN:1.0'. | Copy `…billing:01:1.0` verbatim. |
| `PEPPOL-EN16931-R008` | Document MUST not contain empty elements. | Serialisers that emit `<cbc:Note/>` for null values fail here. Suppress empty elements. |
| `PEPPOL-EN16931-R010` / `R020` | Buyer / Seller electronic address MUST be provided. | `cbc:EndpointID` with EAS `schemeID` on both parties. |
| `PEPPOL-EN16931-R051` | All currencyID attributes must have the same value as the invoice currency code (BT-5), except BT-111. | One currency per document. |
| `PEPPOL-EN16931-R053` | Only one tax total with tax subtotals MUST be provided. | One `cac:TaxTotal` containing all `cac:TaxSubtotal` children — not one per rate. |
| `PEPPOL-EN16931-R044` | Charge on price level is NOT allowed. Only value 'false' allowed. | `cac:Price/cac:AllowanceCharge/cbc:ChargeIndicator` must be `false`. |
| `PEPPOL-EN16931-R046` | Item net price MUST equal (Gross price - Allowance amount) when gross price is provided. | Either omit the gross price or make the arithmetic exact. |
| `PEPPOL-EN16931-R120` | Invoice line net amount MUST equal (Invoiced quantity * (Item net price / item price base quantity)) + line charges - line allowances. | The most common Peppol failure after the totals. Base quantity defaults to 1 but must be consistent. |
| `PEPPOL-EN16931-R121` | Base quantity MUST be a positive number above zero. | Never emit `0`. |
| `PEPPOL-EN16931-R130` | Unit code of price base quantity MUST be same as invoiced quantity. | Same `unitCode` on both. |
| `PEPPOL-EN16931-R110` / `R111` | Line period must lie within the invoice period. | Clamp line periods. |
| `PEPPOL-EN16931-R061` | Mandate reference MUST be provided for direct debit. | Required with payment means 49 / 59. |

## German national rules inside the profile

| Rule | Message | Note |
|---|---|---|
| `DE-R-001` | An invoice shall contain information on "PAYMENT INSTRUCTIONS" (BG-16). | Fatal. BG-16 is optional in the core standard but mandatory for German receivers. |
| `DE-R-026` | If "Invoice type code" (BT-3) contains the code 384 (Corrected invoice), "PRECEDING INVOICE REFERENCE" (BG-3) should be provided at least once. | Warning, but fix it — this becomes mandatory content under Art 226(16) from 2030. |
| `PEPPOL-EN16931-R002` | No more than one note is allowed on document level, unless both the buyer and seller are German organizations. | Germany is explicitly carved out; other countries are not. |

## Diagnosis order

1. XSD fails → element order or namespace wrong. Fix the serialiser, not the data.
2. `BR-nn` fails → a field is missing. Data model gap.
3. `BR-CO-1x` fails → arithmetic. Almost always precision, not logic.
4. `BR-<category>-xx` fails → VAT modelling. Check the category code first, then the breakdown grouping.
5. `PEPPOL-…` or `DE-R-…` fails → the document is EN 16931 valid but not valid for this receiver. Only the CIUS is wrong.
6. Everything passes but the platform rejects → country platform rule, not a Schematron rule. Read the platform's own error code list (`countries-mandates.md`, `countries-other.md`).

## Checkpoints

- [ ] Validator run is the current artefact version (v1.3.16, 2026-04-13), not a vendored copy from years ago
- [ ] Both the EN 16931 and the CIUS Schematron were run, in that order
- [ ] Money rounded to 2 decimals before aggregation
- [ ] Exactly one `cac:TaxTotal` with subtotals in Peppol documents
- [ ] Empty elements suppressed
- [ ] VAT identifiers carry the ISO country prefix, Greece as `EL`
- [ ] Each fatal finding fixed; each warning either fixed or explicitly accepted with a reason
