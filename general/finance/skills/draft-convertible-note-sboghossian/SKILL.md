---
name: draft-convertible-note-sboghossian
title: Draft — Convertible Note
description: Use when asked to draft a convertible promissory note — a debt instrument that converts into equity on a qualified financing event. Covers required inputs (principal, interest, maturity, valuation cap, discount), the conversion mechanics, change-of-control treatment, events of default, the note-vs-SAFE structural choice, and MENA-specific considerations including interest structuring under Sharia-compliant frameworks and jurisdiction availability of SAFEs.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-convertible-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Draft — Convertible Note

## When to use this

Use this skill to draft a convertible promissory note for early-stage company financing where:
- The parties want to defer valuation negotiations until a priced equity round (the "qualified financing").
- The investor wants debt treatment with downside protection pending conversion.
- The jurisdiction has better legal precedent for debt instruments than for SAFEs (see note below).

A convertible note is a loan from an investor to a company that converts into equity — typically preferred shares — when a defined triggering event occurs (usually a qualified equity financing round). Until conversion, it is a debt obligation on the company's balance sheet.

## Note vs SAFE — the structural choice

| Dimension | Convertible Note | SAFE |
|---|---|---|
| Legal nature | Debt (promissory note) | Equity-like instrument; not a debt |
| Balance sheet | Liability until conversion | Not a liability (no debt obligation) |
| Maturity date | Yes (typically 18–24 months); cash repayment if no conversion | No maturity; can theoretically remain outstanding indefinitely |
| Interest | Yes (typically 5–8% simple interest) | No interest |
| Investor protection | More: debt defaults, bankruptcy priority | Less: investor has no claim if no qualified financing |
| Jurisdiction fit | Better legal certainty in most MENA jurisdictions | SAFEs are a US/DIFC/ADGM concept; less certainty in onshore Arab states |
| Sharia compatibility | Interest is problematic for KSA; restructure as profit-sharing or fee | SAFEs avoid the interest problem |

**Recommendation for MENA**:
- DIFC / ADGM: both notes and SAFEs are well-understood; use SAFE if company prefers clean cap table.
- UAE onshore: convertible notes are more familiar; SAFEs are used but with less judicial precedent.
- KSA: interest-bearing notes create Sharia compliance issues; use a Sharia-compliant structure (murabaha or profit-participation) or a SAFE equivalent.
- LB: note structure is well-understood; SAFE is uncommon.

## Required inputs

| Input | Notes |
|---|---|
| Issuer (the company) | Full legal name, registration, authorized signatory |
| Holder (investor) | Full legal name, registration or personal details |
| Principal amount | Total investment amount; currency |
| Interest rate | Typically 5–8% per annum, simple interest accruing (not paid in cash) |
| Maturity date | Typically 18–24 months from issuance |
| Valuation cap | The maximum pre-money valuation at which the note converts; protects early investor from high-priced round dilution |
| Discount rate | Percentage discount to the next round price (typically 15–25%); rewards early investor for risk taken |
| Qualified financing threshold | The minimum equity raise that triggers automatic conversion (e.g., aggregate proceeds ≥ USD 1,000,000) |
| Governing law | Determines enforceability of debt terms and conversion mechanics |

## Document structure

### 1. Principal amount and interest accrual
```
1. PRINCIPAL AND INTEREST

1.1 Principal. The Company promises to pay to the order of the Holder 
    the principal sum of [CURRENCY AMOUNT] (the "Principal").

1.2 Interest. Interest shall accrue on the outstanding Principal at 
    the rate of [X]% per annum (simple interest, not compounding) from 
    the Issue Date until the earlier of: (a) the Maturity Date; 
    (b) the date of conversion; (c) the date of full repayment.

1.3 No cash interest payments. Interest accrues but is not payable in 
    cash until the Maturity Date or conversion (at which point the 
    accrued interest converts along with the Principal).
```

### 2. Qualified financing — automatic conversion

```
2. CONVERSION ON QUALIFIED FINANCING

2.1 Automatic conversion. Upon the closing of a Qualified Financing, 
    the outstanding Principal and all accrued interest shall 
    automatically convert into shares of the class sold in the 
    Qualified Financing ("Conversion Shares") at the Conversion Price.

2.2 "Qualified Financing" means: the issuance and sale of equity 
    securities of the Company in a single closing or series of 
    related closings, resulting in aggregate gross proceeds to the 
    Company of not less than [CURRENCY AMOUNT] (the "Threshold").

2.3 "Conversion Price" shall equal the lesser of:
    (a) the Capped Price: [Valuation Cap] ÷ [fully diluted shares 
        outstanding immediately prior to the Qualified Financing]; and
    (b) the Discounted Price: the per-share price paid by new investors 
        in the Qualified Financing, multiplied by (1 minus [Discount 
        Rate, e.g., 0.20 for a 20% discount]).
```

**Worked example**:
- Valuation Cap: USD 5,000,000
- Discount: 20%
- Next round price (Series A): USD 2.00/share (at USD 10M pre-money, 5M shares)
- Cap-implied price: USD 5M ÷ 5M shares = USD 1.00/share
- Discount-implied price: USD 2.00 × 0.80 = USD 1.60/share
- Conversion price: lesser of USD 1.00 and USD 1.60 = **USD 1.00/share**
- Note holder with USD 100,000 principal (plus interest) gets 100,000+ shares at USD 1.00 while Series A investors pay USD 2.00.

### 3. Maturity — what happens if no Qualified Financing by Maturity Date?

Three common options; select one:

**Option A (repayment)**:
```
If the Note has not converted as of the Maturity Date, the Company 
shall repay the outstanding Principal and all accrued interest in 
cash within [30] days of the Maturity Date.
```

**Option B (investor's election)**:
```
If the Note has not converted as of the Maturity Date, the Holder 
may elect, in writing within [30] days, to: (a) require repayment 
of Principal and accrued interest; or (b) convert the Note into 
ordinary shares at the Conversion Price (using the Valuation Cap 
as the implied pre-money valuation).
```

**Option C (automatic conversion into ordinary shares)**:
```
If the Note has not converted by the Maturity Date, the outstanding 
Principal and accrued interest shall automatically convert into 
ordinary shares at the Capped Price.
```

Option B is most investor-friendly; Option C is most company-friendly.

### 4. Optional conversion (if desired)

Some notes allow voluntary conversion before a Qualified Financing at the Holder's election:
```
At any time prior to the Maturity Date, the Holder may elect to 
convert the outstanding Principal and accrued interest into ordinary 
shares at [specified price or Capped Price].
```

### 5. Change of control

If the company is acquired before the note converts:
```
5. CHANGE OF CONTROL

Upon a Change of Control, the Holder shall elect, within [10] 
Business Days of notice, to either:
(a) require repayment of [1×/1.5×/2×] the outstanding Principal 
    plus accrued interest; or
(b) convert the Note into the class of equity at the lesser of 
    the Capped Price or the acquisition price per share.

"Change of Control" means: any acquisition of more than 50% of the 
Company's voting shares; a merger or consolidation in which the 
Company's existing shareholders hold less than 50% post-closing; 
or a sale of all or substantially all of the Company's assets.
```

The multiplier (1×, 1.5×, 2×) protects the early investor from an exit at a price that would not adequately reward the risk taken.

### 6. Events of default and remedies

```
6. EVENTS OF DEFAULT

Each of the following constitutes an Event of Default:
(a) Failure to pay any amount due within [10] days of the due date;
(b) Material breach of any representation, warranty, or covenant 
    that is not remedied within [30] days of written notice;
(c) Insolvency, liquidation, or appointment of a receiver;
(d) Material adverse change that materially impairs the Company's 
    ability to perform its obligations under this Note.

Upon an Event of Default, the Holder may declare the entire 
outstanding Principal and accrued interest immediately due and 
payable, without notice or demand.
```

### 7. Representations and warranties of the Company (brief)

```
The Company represents that: (a) it is duly organized and has 
authority to issue this Note; (b) this Note constitutes a valid, 
binding, and enforceable obligation; (c) issuance of this Note 
and the anticipated Conversion Shares has been duly authorized 
by the Board; (d) no regulatory approval is required for issuance 
other than as disclosed.
```

### 8. Subordination (if applicable)

If senior lenders are in place:
```
This Note is subordinated in right of payment to all Senior Indebtedness 
of the Company [as defined]. In the event of the Company's insolvency, 
holders of Senior Indebtedness shall be paid in full before any payment 
on this Note.
```

### 9. Governing law
```
This Note is governed by and construed in accordance with the laws 
of [DIFC / UAE Federal / English law / Delaware]. Any disputes 
shall be resolved by [DIAC arbitration / DIFC Courts / English courts].
```

## MENA-specific considerations

### KSA — Sharia-compliant alternative
- Standard interest-bearing notes conflict with Sharia prohibition on riba (interest).
- Alternative structures:
  - **Murabaha note**: the "investment" is structured as a purchase-resale transaction with a fixed profit mark-up; the mark-up replaces interest.
  - **Musharaka / Mudaraba**: profit-and-loss sharing structure; investor participates in profits rather than receiving fixed interest.
  - **Fee-based return**: frame the investor's return as a consulting or arrangement fee, not interest.
- These structures add complexity; specialist Islamic finance counsel should review.

### UAE onshore
- Convertible notes are used but the conversion into equity requires proper formalization under UAE Companies Law (notification to registrar; AoA amendment for new share class issuance).
- The valuation cap mechanism works as a matter of contract; the conversion itself requires a board resolution and registrar filing.

### DIFC / ADGM
- Convertible notes and SAFEs are familiar; no structural complications.
- DIFC and ADGM have developed investor-friendly legal frameworks for startup financing.
- Multiple institutional investors in one note: use a note purchase agreement structure with multiple holders.

## Related skills

- [[draft-cap-table-resolution]]
- [[draft-board-resolution]]
- [[draft-articles-of-association]]
- [[draft-safe]]
