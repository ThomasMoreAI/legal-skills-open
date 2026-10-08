---
name: draft-promissory-note-sboghossian
title: Promissory Note (سند أذني / Billet à Ordre)
description: Use when drafting a promissory note — an unconditional written promise to pay a certain sum on demand or at a future date. Covers the mandatory elements for negotiable-instrument status (Geneva Convention / commercial codes), optional provisions (interest, acceleration, cross-default, endorsement), and critical MENA-specific issues (KSA Sharia interest treatment, UAE criminal dishonor risk, LB/EG commercial code requirements). Triggers on "promissory note", "note payable", "iou", "acknowledgment of debt", or "سند أذني" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-promissory-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: finance
language: en
---

# Promissory Note (سند أذني / Billet à Ordre)

## When to use this

A promissory note is an unconditional written promise by one party (the Maker) to pay a fixed sum of money to another party (the Payee) or their order, on demand or at a specified future date. When properly drafted, it is a negotiable instrument — it can be transferred by endorsement, sued on without proving the underlying obligation, and enforced summarily in most jurisdictions.

Use this skill when:
- Formalizing a straightforward loan obligation between two parties
- A lender wants a standalone instrument separate from the loan agreement (for ease of enforcement)
- Acknowledging existing indebtedness in a legally enforceable form
- Part of a transaction package (e.g., a promissory note as a component of a real estate transaction)
- Creating an instrument that a Payee can discount, transfer, or use as collateral

A promissory note is simpler than a full loan agreement — use [[draft-loan-agreement]] when the transaction requires covenants, representations, events of default, security arrangements, or syndication.

## Mandatory elements for negotiable-instrument status

Per the Geneva Convention on Bills of Exchange and Promissory Notes (and most civil-law commercial codes derived from it), a promissory note must contain:

| Element | Why mandatory | Example |
|---------|--------------|---------|
| 1. Designation as "Promissory Note" | Identifies the instrument type | "PROMISSORY NOTE" or "سند أذني" (Arabic) or "Billet à Ordre" (French) in the title |
| 2. Unconditional promise to pay | Negotiable instruments cannot be conditional — "I will pay if X happens" destroys negotiability | "The Maker hereby unconditionally and irrevocably promises to pay..." |
| 3. Sum certain | A fixed, calculable amount | USD 500,000 (five hundred thousand United States Dollars) |
| 4. Payee identification | To whom payment is made | "Pay to the order of [Payee Name]" |
| 5. Maturity | When payment is due | "On [Date]" / "On demand" / "At sight" / "30 days after sight" |
| 6. Date and place of issue | Establishes jurisdiction and limitation period start | "Issued in [City], [Country], on [Date]" |
| 7. Maker's signature | Unconditional acceptance of the obligation | Maker's authorized signature; for companies, authorized officer + company stamp (where required) |
| 8. Place of payment | Where the Payee presents the note | "[Bank name and branch]" or "[Address]" |

**If any mandatory element is missing**: the instrument may lose its status as a negotiable promissory note and become merely an ordinary acknowledgment of debt — enforceable as a contract but not summarily enforceable as a bill of exchange.

## Optional provisions

### Interest
- State the rate: "[X]% per annum, calculated on the outstanding principal from [Issue Date] until payment in full"
- Basis: "on a 365/actual-day basis" or "30/360" — specify to avoid calculation disputes
- Compounding: "interest shall not compound" (default for simple notes) or specify if interest compounds
- **KSA caution**: see Jurisdictional notes — interest should be characterized as a "profit charge" or "administrative fee" in KSA-governed instruments

### Default interest
- "If the principal or any interest is not paid on its due date, default interest shall accrue on the overdue amount at [X]% per annum above the stated rate" from the due date until actual payment

### Acceleration clause on default
- "If the Maker fails to pay any amount due hereunder on its due date and such failure continues for [5] business days, the full outstanding principal and all accrued interest shall, at the Payee's option, become immediately due and payable without further notice or demand"

### Cross-default
- "Any default by the Maker under [the Loan Agreement / any other financial obligation to the Payee] shall constitute a default under this Note"
- Cross-default provisions are appropriate when the promissory note is one component of a broader financing; otherwise they add complexity without benefit

### Joint and several liability (multiple makers)
- "Each Maker is jointly and severally liable for the full amount of this Note"
- The Payee can pursue any one Maker for the full amount; that Maker's right to contribution from the others is separate

### Endorsement / transfer
- "This Note is transferable by endorsement and delivery"
- OR: "This Note is non-transferable without the Maker's prior written consent"
- If no endorsement restriction is included, the note is freely transferable as a negotiable instrument

### Waiver of presentment, demand, protest
- "The Maker hereby waives presentment, demand, notice of dishonor, and protest"
- These formalities (traditional requirements for enforcing bills of exchange) are commonly waived in commercial promissory notes; verify whether the governing law requires specific waiver language

### Governing law
- "This Note shall be governed by and construed in accordance with the laws of [jurisdiction]"

### Jurisdiction / enforcement
- "[Courts of [jurisdiction]] shall have exclusive jurisdiction for disputes arising from this Note"
- OR: "This Note may be enforced in any court of competent jurisdiction"
- Consider including attorney's fees provision: "In any action to enforce this Note, the prevailing party shall be entitled to recover its reasonable attorneys' fees and costs"

## Jurisdictional notes

| Jurisdiction | Key requirements |
|---|---|
| **Lebanon (LB)** | Commercial Code (Code de Commerce libanais) — Articles on promissory notes (billets à ordre / سند أذني); execution of judgment available via "ordonnance sur requête" procedure; fast enforcement through commercial court summary proceedings |
| **France / OHADA** | Code de Commerce / OHADA Uniform Act on Securities; same Geneva Convention-based framework; swift enforcement by summary proceedings |
| **Egypt (EG)** | Commercial Code — promissory notes (سند إذني); registration not required; enforcement by summary proceedings available |
| **KSA** | Promissory notes enforceable under Saudi Commercial Code; but **interest**: under Sharia principles, pure interest on money loans (riba) is prohibited. Restructure: (a) characterize the return as a "compensation for cost of capital" / "administrative fee" or (b) use an Islamic finance structure. Work with local counsel to confirm that the interest characterization will be accepted by the Saudi courts or arbitral tribunal |
| **UAE federal** | Commercial Transactions Law (Federal Law 18/1993 as amended); promissory notes enforceable; criminal dishonor: under UAE criminal law, issuing a promissory note without adequate funds or stopping payment on a note without legal justification may constitute a criminal offense (analogous to check fraud). Verify current law before taking commercial notes — the criminal dimension affects the risk profile significantly |
| **DIFC / ADGM / UK / US** | Full negotiable-instrument law applies; Geneva Convention framework (UK Bills of Exchange Act 1882; US UCC Article 3); freely transferable; summary enforcement available |
| **Negotiable instrument vs acknowledgment of debt** | A note that contains conditional language, lacks a fixed sum, or is missing mandatory elements becomes an ordinary contractual debt rather than a negotiable instrument. Enforcement then requires proving the underlying obligation — slower and more complex |

## Anti-patterns

- **Vague IOU language**: "I, [Name], owe [Other Name] USD 100,000" — does not constitute a negotiable promissory note; becomes only a contractual debt acknowledgment; no summary enforcement
- **Conditional promise**: "I will pay USD X when the project is completed" — destroys negotiability; the condition must be satisfied before a court can enforce
- **Omitting the unconditional promise**: "I intend to pay USD X on [date]" — "intend" introduces uncertainty; use "unconditionally promise to pay"
- **Incorrect rate calculation**: specifying "5% interest" without stating the basis (per annum, per month, simple, compound, day-count) leads to disputes
- **UAE criminal exposure**: taking a promissory note from a counterparty who may not have funds to pay — investigate the Maker's financial position first; criminal dishonor is a serious risk in UAE commercial practice

## Document template (core)

```
PROMISSORY NOTE

[City, Country], [Date]

FOR VALUE RECEIVED, [Maker Full Name / Company Name, a [company type] incorporated in 
[jurisdiction] with registration number X] (the "Maker") HEREBY UNCONDITIONALLY AND 
IRREVOCABLY PROMISES TO PAY to the order of [Payee Full Name / Company Name] (the 
"Payee") the principal sum of [CURRENCY AND AMOUNT IN WORDS] ([Currency Symbol][Amount 
in Figures]), together with interest at the rate of [X]% per annum on the outstanding 
principal, from the date hereof until paid in full.

This Note shall be due and payable on [MATURITY DATE / ON DEMAND].

Payment shall be made to [Payee bank account details / Payee's address] in immediately 
available funds in [Currency].

This Note is governed by the laws of [Jurisdiction].

IN WITNESS WHEREOF, the Maker has executed this Note on the date first written above.

MAKER:

________________________
[Full Name]
[Title, if corporate]
[Company Name, if corporate]
[Date]

[Witness or notarization block if required by jurisdiction]
```

## Related skills

- [[draft-loan-agreement]]
- [[draft-guarantee]]
- [[draft-mortgage]]
- [[draft-security-agreement]]
