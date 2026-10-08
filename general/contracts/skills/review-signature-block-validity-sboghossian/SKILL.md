---
name: review-signature-block-validity-sboghossian
title: Signature Block Validity Review
description: Use when verifying that a contract's signature pages and execution mechanics are legally valid before or after signing. Checks signatory authority, capacity description, entity name accuracy (including Arabic), witness requirements, date consistency, counterparts clauses, cross-border authentication (apostille, legalization), e-signature validity, common seal, and page initialing requirements. Applies across MENA and international jurisdictions with jurisdiction-specific execution rules.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-signature-block-validity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Signature Block Validity Review

## When to use this

Use this skill as a pre-execution checklist before a contract is signed, or as a post-execution audit to confirm a signed agreement is legally binding. Invalid execution is a surprisingly common source of disputes — a contract signed by an unauthorized person, missing witnesses, or with an incorrect entity name may be void or voidable.

Triggers:
- Before sending a contract for execution — confirm the signature block is correctly structured
- Before relying on a counterparty's signed document — verify their execution was valid
- M&A due diligence — confirm that material contracts were validly executed
- Enforcement proceedings — confirm that the contract being enforced was properly signed

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| Contract document (ideally signed copy) | To assess execution formalities | Required |
| Jurisdiction(s) | Execution requirements differ substantially | From governing-law clause or place of execution |
| Entity type | Company, partnership, government entity, natural person, trustee | From signature block or contract body |
| Authorization documents | Board resolution, power of attorney, commercial registration | Request if not provided |

## Review Checklist

### Check 1 — Signatory Authority

The person signing must have authority to bind the entity. Authority flows from:

1. **Statutory authority**: directors, managing directors, CEOs, and similarly named officers typically have implied authority under corporate law to bind the company for commercial contracts
2. **Board resolution / corporate authorization**: for significant contracts (value threshold varies by jurisdiction), a board resolution authorizing the specific agreement is needed
3. **Power of Attorney (POA)**: if signing by proxy — verify the POA: (a) is validly executed; (b) has not expired; (c) covers the specific act (signing this type and value of contract); (d) was issued in the correct form for the jurisdiction

Documents to request if authority is not obvious:
- Commercial Registration (CR) extract showing officers/directors and their authority
- Board resolution or written unanimous consent authorizing the agreement
- Delegation matrix if the signatory is below C-suite level
- POA document (if signing under power of attorney) with notarization/apostille as required

Flag: if the signatory is identified as "Authorized Signatory" but no authorization document is attached — the counterparty may challenge enforceability if a dispute arises.

### Check 2 — Capacity / Title Accuracy

The capacity block (title printed below the signature line) must accurately describe the signatory's role:

- Correct: "Director", "Chief Executive Officer", "Managing Director", "Authorized Signatory (per POA dated [X])"
- Flag: vague descriptions such as "Representative" or "Agent" without specification of the authority basis
- For POA signatories: capacity block should read: "Attorney-in-Fact pursuant to Power of Attorney dated [date], notarized by [notary], reference [number]"

### Check 3 — Entity Name Accuracy

The entity name in the signature block must match the Commercial Registration (CR) / equivalent registration document exactly, including:

- Exact legal name (not a trade name / DBA)
- Entity type suffix (LLC, PJSC, BSC, SPC, SAL, SAE, GmbH, Ltd., etc.)
- Arabic version where required (many MENA jurisdictions require the Arabic registered name)

**MENA-specific**:
- **UAE**: the Arabic name must match exactly as it appears on the CR issued by the Department of Economic Development (DED) or the relevant free-zone authority (DIFC Registrar, ADGM Registration Authority)
- **KSA**: Arabic entity name is legally controlling; English transliteration is for convenience only
- **Lebanon**: SAL (Société Anonyme Libanaise) or SARL must be accurately described; Ministry of Finance registration number may be included
- **Egypt**: SAE (Société Anonyme Égyptienne) registration with GAFI should match

Flag: any discrepancy between the contract entity name and the CR — even minor differences (dropped "LLC", different transliteration) can create enforceability arguments.

### Check 4 — Witness Requirements

Some jurisdictions require witnesses to contracts or to specific types of clauses:

| Jurisdiction | Witness requirement |
|---|---|
| UAE (onshore) | Certain commercial documents and real estate transfers require 2 witnesses; employment contracts and lease agreements may require witnesses |
| KSA | Certain contracts benefit from notarization by a كاتب عدل (Kātib 'Adl — notary public); witness blocks are customary for significant commercial agreements |
| Lebanon | Notarization (Tawqi3i at Notaire) is required for real estate transfers; customary but not always required for commercial contracts; strongly recommended for security documents |
| DIFC / ADGM | No general witness requirement for commercial contracts; English-law approach |
| UK | Deeds (as opposed to simple contracts) require a witness; if a contract is executed as a deed (for lack of consideration, or to achieve 12-year limitation period), witness is mandatory |
| US | Most commercial contracts: no witness requirement; notarization required for real estate deeds and certain statutory filings |

Flag: witness block absent where required; witness is a party to the contract (generally disqualifies the witness in many jurisdictions); witness description (name, ID, contact) missing.

### Check 5 — Date Consistency

Execution issues:
- All parties should have the same execution date, or if different dates, the agreement should specify which party's date is the "Effective Date"
- Backdating: a contract dated earlier than its actual execution date is problematic — may be void for fraud; may affect limitation periods; may conflict with contemporaneous documents
- Future dating: acceptable if the agreement is intended to take effect on a future date, but the execution date should still reflect when signatures were applied

Gregorian / Hijri date handling:
- In Saudi Arabia, some official documents use Hijri dates; for commercial contracts, both Gregorian and Hijri dates are commonly included
- Verify that any date conversion is accurate — calendar conversion errors create ambiguity about when obligations commenced

### Check 6 — Counterparts Clause

If parties are signing in different locations (common in cross-border deals), the contract should contain a counterparts clause:
- "This Agreement may be executed in counterparts, each of which shall be deemed an original, and all of which together shall constitute one and the same instrument"
- Without this clause, a party might argue that only a single physical document with all signatures is binding
- In PDF/e-signature scenarios: add that electronic counterparts are valid (unless e-signature is not accepted — see Check 9)

### Check 7 — Cross-Border Authentication (Apostille / Legalization)

When a contract executed in one country needs to be used or enforced in another:

| Scenario | Requirement |
|---|---|
| UAE executing a contract to be used in France | UAE is Apostille Convention member (acceded 2021); UAE documents can be apostilled by UAE Ministry of Foreign Affairs (MOFA) |
| Saudi Arabia (not an Apostille member) | Documents must be notarized + attested by KSA MOFA + attested by the embassy of the destination country |
| Lebanon | Lebanon is an Apostille Convention member; Lebanese documents can be apostilled by the Lebanese MOFA |
| Egypt | Egypt is an Apostille Convention member (acceded 2022); documents apostilled by the Egyptian MOFA |
| UK contract used in UAE | UK documents: apostille from UK FCO + MOFA attestation in UAE |

Flag: cross-border contracts where the authentication chain is incomplete — the document may be inadmissible in the foreign jurisdiction's courts.

### Check 8 — Electronic Signature Validity

E-signatures are accepted in most jurisdictions but with different conditions:

| Jurisdiction | E-signature validity |
|---|---|
| UAE | Federal Law No. 46 of 2021 on Electronic Transactions and Trust Services: e-signatures valid for commercial contracts; exceptions include property transfers, wills, family law matters |
| DIFC | DIFC Electronic Transactions Law: e-signatures valid |
| ADGM | ADGM e-signatures valid |
| KSA | E-signatures recognized under the Anti-Cyber Crime Law and Electronic Transactions Law; notarized documents still require wet ink + notary |
| Lebanon | Electronic signatures recognized under Law No. 81 of 2018 on Electronic Transactions; certain contracts (real estate, commercial registration) require wet ink |
| France | Qualified Electronic Signatures (QES) under eIDAS regulation have full legal effect; simple e-signatures may be challenged for high-value contracts |
| UK | E-signatures valid for most contracts under Electronic Communications Act 2000; deeds require wet ink or very specific e-sign process |

Flag: e-signature used for a category of document that requires wet ink; e-signature platform used is not certified to the required trust level (e.g., QES required but only Advanced Electronic Signature obtained).

### Check 9 — Common Seal

Older requirements:
- **Lebanon (older SAL companies)**: some articles of incorporation require the company seal to be affixed
- **KSA**: company seal (ختم) is customary and provides practical enforceability signal; not always strictly legally required but strongly recommended
- **UK pre-2006**: common seal requirement largely abolished by Companies Act 2006; now optional
- **UAE**: company seal still commonly affixed as a practical matter, though not strictly required for all contract types

### Check 10 — Page Initialing

- UAE and many MENA practice: initialing each page by both parties' signatories is customary but not a strict legal requirement for validity
- However: initialing provides strong evidence that the pages initialed were part of the agreement as at the date of signing — important protection against substitution of pages
- Check: if a contract is long (over 10 pages) and is not initialed page by page, a party might argue that pages were substituted after execution. Recommend initialing in any contested or high-value deal.

## Output Format

```json
{
  "issues": [
    {
      "signatory": "<name / entity>",
      "check": "<check number and title>",
      "problem": "<description>",
      "severity": "critical|high|medium|low",
      "remediation": "<action required>"
    }
  ],
  "overall_execution_validity": "valid|defective|void",
  "authentication_complete": true/false,
  "e_signature_valid": true/false/null,
  "critical_issues_count": <int>
}
```

## Common Mistakes

- Relying on a title like "CEO" without a board resolution for contracts above the officer's standard authority threshold
- Accepting an English-only entity name for a MENA counterparty whose CR is in Arabic — the English name may not be a registered name at all
- Failing to check that a POA covers the specific type of transaction being signed (a general commercial POA may not cover real estate or IP assignments)
- Ignoring Hijri/Gregorian date conversion errors — they can cause genuine ambiguity about notice periods and limitation start dates

## Related Skills

- [[review-missing-clauses]]
- [[review-nda-quick-check]]
- [[review-msa-deep-review]]
- [[review-risk-flagging]]
- [[draft-power-of-attorney]]
