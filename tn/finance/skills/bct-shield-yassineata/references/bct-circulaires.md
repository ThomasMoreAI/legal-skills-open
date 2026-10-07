# BCT circulars — forex rules that matter for freelancers and exporters

## General context

The **Central Bank of Tunisia (BCT)** issues **circulars** that govern foreign-exchange operations and cross-border money flows. Freelancers receiving payments in foreign currency fall under this framework.

---

## ⚠️ CRITICAL — December 2025 forex law: announced, NOT yet enforceable

In December 2025, Tunisia announced the end of a 50-year-old rule that forced people to convert foreign currency to TND. The headline news said freelancers would be allowed to **receive and hold** foreign currency without forced conversion.

**But there is a catch that most online articles miss:**

> The law was passed, but no **application decrees** (اوامر ترتيبية / *arrêtés d'application*) have been published in the Journal Officiel (JORT) yet. In Tunisian legal practice, a law is not operational until its implementing decrees are gazetted. Until that happens, the **OLD regime stays in force in practice**: the 1976 Code des Changes plus the 1993-13 circular and its amendments.

**What this means for you, today:**

- Treat the December 2025 announcement as a future change, not a current right.
- Continue to operate under the OLD rules: forced repatriation timelines from Circular 2025-13, PPR Devises account usage as before, no automatic right to keep USD or EUR balances long-term.
- Most forums, blog posts, and even some bankers are spreading the news as if it were already operational. **It is not.**
- Check JORT every week for the application decree. When it lands, this entire page will need to be rewritten.

[src: launchbaseafrica.com/2025/12/04 + sources.json id `tunisia-forex-deregulation-dec-2025-announcement`]

---

## Key circulars 2025-2026

### Circular 2025-13 (27 October 2025) — settlement of imports and exports

[src: lapresse.tn/2025/11/06 + lucapacioli.com.tn/blog/bct-circular-2025-13]

**Scope:** exporters of **goods** (physical merchandise).

What it says:
- Payment by **any settlement method** must arrive within **120 days** from shipment.
- Longer timelines (121–360 days) are allowed only if backed by one of:
  - A guarantee from a non-resident bank, OR
  - An irrevocable documentary credit, OR
  - A Standby Letter of Credit (SBLC), OR
  - A bill of exchange guaranteed by a foreign institution.

**Why it matters for freelancers:** indirect — the circular targets goods, not services. But it signals BCT's general direction toward gradual liberalization.

### Circular 2025-10 (full PDF available)

URL: https://www.bct.gov.tn/bct/siteprod/documents/Cir_2025_10_fr.pdf

[REQUIRES MANUAL LEGAL VERIFICATION: read the full PDF to extract exact provisions. Numbering 10 comes before 13 — probably covers a different topic (licensed intermediaries, etc.)]

### Circular 2025-03 (full PDF available)

URL: https://www.bct.gov.tn/bct/siteprod/documents/Cir_2025_03_fr.pdf

[REQUIRES MANUAL LEGAL VERIFICATION: same as above]

### Circular 2026-04 — restrictions on imports of "non-priority" products ⚠️

[src: challenges.tn — discovered via BA7ATH OSINT]

**Scope:** importers — restrictions on access to foreign currency for products classified as "non-priority".

What it says:
- A long annex lists products whose imports are restricted in terms of bank foreign-currency allocation.
- Effect: the bank can **refuse** an international transfer for a listed non-priority product, even if customs would let it through.

**Why it matters for freelancers — DIRECTLY and critically:** if you want to import a laptop, a GPU, or any tech equipment, check the 2026-04 annex **before** you order.

[REQUIRES MANUAL LEGAL VERIFICATION: confirm whether HS codes 8471 (laptops) and 8517 (smartphones) are on the 2026-04 non-priority list]

---

## Foreign-currency accounts — available instruments

See `compte-devises.md` for details. Quick map:

| Account type | Who can open | Convertibility |
|---|---|---|
| PPR Devises (resident individual, foreign currency) | All residents | Usable, but holding rules still under OLD regime (Dec 2025 law not yet enforceable) |
| Professional Devises account | Export-oriented SUARL / SARL | Per BCT rules |
| Convertible Dinar account | Residents with a foreign-currency source | Convertible abroad under conditions |

Practical reference (BNA): http://www.bna.tn/fr/compte-personne-physique-residente-en-devises-ou-en-dinars-convertibles.755.html

---

## How to receive freelancer payments (Upwork / Stripe / Deel / Payoneer)

### Recommended workflow under the CURRENT (old) regime

1. **Source:** the foreign platform (Upwork, etc.) pays in USD / EUR.
2. **Intermediary:** Payoneer / Wise / direct SWIFT transfer.
3. **Tunisian receiving account:**
   - **Best option:** an open PPR Devises account at a Tunisian bank (BNA, BIAT, Attijari, ATB, etc.).
   - **Acceptable fallback:** a standard dinar account (the bank converts automatically at the daily rate).
4. **Holding foreign currency:** still bound by old repatriation and conversion rules. The Dec 2025 announcement does NOT yet override this.
5. **Conversion to TND:** done on request, at the daily rate.
6. **Tax declaration:** the income still goes into IRPP / IS depending on your status.

### Documents to keep (BCT and tax audit)

- Contract or purchase order from the foreign client
- The invoice you issued (with the export VAT 0% mention if you are a SUARL)
- Proof of payment from the platform (Upwork / Stripe / etc. statement)
- The bank credit note in foreign currency
- The conversion statement (if you converted to TND)

---

## Cash in foreign currency — entering or leaving Tunisia

- **Declaration threshold:** above **25 000 TND** equivalent in cash → mandatory customs declaration on entry AND exit. [src: tn.usembassy.gov]
- Below the threshold: no cash declaration (but bank accounts remain traceable).
- Failure to declare = seizure + fine.

---

## Myths to bust

| Myth | Reality |
|---|---|
| "Above 1 000 TND the BCT freezes your account" | **FALSE** — no official BCT source confirms this threshold. Urban legend. |
| "You must convert foreign currency immediately when you receive it" | **STILL TRUE under the OLD regime in force.** The Dec 2025 announcement would change this, but the application decrees are not out yet. |
| "Upwork is banned in Tunisia" | **FALSE** — Upwork is usable; receive via Payoneer or SWIFT. |
| "A patente cannot receive foreign currency" | Historically hard, but possible via PPR Devises. The Dec 2025 announcement promised more flexibility, but again — not yet enforceable. |
| "BCT automatically freezes foreign accounts above 5 000 USD" | **FALSE** — no automatic freeze. Inspections happen but they are not systematic. |
| "The 50-year forex rule is gone since December 2025" | **PARTIALLY FALSE in practice today.** The law was passed in December 2025, but no application decrees are in JORT yet. The old regime is still de facto in force. |

---

## Sources

- `data/sources.json` → `bct-cir-2025-13`, `bct-cir-2025-10`, `bct-cir-2025-03`, `bct-cir-2026-04`, `tunisia-forex-deregulation-dec-2025-announcement`, `forex-cash-25k`
- `data/bct_circulars.json` → structured schema
- `compte-devises.md` (practical side)
