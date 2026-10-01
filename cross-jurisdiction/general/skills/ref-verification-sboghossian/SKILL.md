---
name: ref-verification-sboghossian
title: Reference — Verification Checklist
description: Use as a mandatory quality-control checklist before any AI-generated legal output is sent to a client, filed with a court, or used in negotiation. Covers verification of cited statutes, case citations, numerical values, jurisdiction accuracy, currency of the law, and whether the conclusion actually answers the question asked. This is a non-skippable step for high-stakes outputs. Applies across all jurisdictions and practice areas.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/ref/ref-verification
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Reference — Verification Checklist

## Scope

Every AI-generated legal output that will be used in a high-stakes context — sent to a client, filed with a court or regulator, used in contract negotiation, or relied on for a business decision — must pass through this verification checklist before use. Skipping verification is one of the most common and most consequential anti-patterns in legal AI use (see [[ref-anti-patterns]]).

AI language models produce confident, fluent outputs that can be wrong in ways that are not obvious. Unlike a calculation error, a fabricated case citation or a misquoted statute article number looks exactly like a correct citation. Only verification against authoritative sources catches these errors.

---

## The Verification Checklist

Work through each item before releasing the output. Check each item; do not treat any item as optional for high-stakes output.

---

### Check 1 — Are all cited statutes real?

For each statute, regulation, or decree referenced in the output:

- [ ] Confirm the instrument exists with the stated name and number (e.g., "UAE Federal Decree-Law No. 33/2021 on the Regulation of Labour Relations" — verify on the UAE Official Gazette or the relevant government website)
- [ ] Confirm the specific article or provision cited exists within the instrument
- [ ] Confirm the article number and its content match what the AI attributed to it
- [ ] Confirm the instrument is currently in force (not repealed, superseded, or materially amended since the AI's knowledge cutoff)

**Verification sources by jurisdiction:**

| Jurisdiction | Primary source |
|---|---|
| UAE federal laws | UAE Federal Gazette (Ministerial / Official Gazette website); moj.gov.ae |
| DIFC laws | DIFC Laws website (difclaw.ae) |
| ADGM laws | ADGM website (adgm.com/practice-and-regulation) |
| KSA laws | Saudi Official Gazette (Umm Al-Qura); National Centre for Government Technology (noga.gov.sa) |
| Lebanon | Official Gazette (Journal Officiel); Lebanese Parliament website |
| Egypt | Egyptian Official Gazette; Ministry of Justice |
| EU | EUR-Lex (eur-lex.europa.eu) |
| UK | legislation.gov.uk |
| US | US Code (uscode.house.gov); Electronic Code of Federal Regulations (ecfr.gov) |

---

### Check 2 — Are all cited cases real?

For each case citation in the output:

- [ ] Confirm the case exists in the cited court's records (DIFC case → check DIFC Courts judgment database; UK case → check BAILII; US case → check CourtListener or Westlaw)
- [ ] Confirm the case name and parties are correct
- [ ] Confirm the citation (year, court, neutral citation or law report reference) is accurate
- [ ] Confirm the proposition of law attributed to the case in the AI output accurately reflects the court's actual holding
- [ ] Confirm the case has not been overturned, distinguished, or materially limited by subsequent decisions

**Red flag:** If a cited case cannot be found in the primary database, do not assume it exists in a database you do not have access to. Assume the citation may be fabricated until proven otherwise.

---

### Check 3 — Is the jurisdiction correct?

- [ ] Does the output apply the law of the correct jurisdiction — the one the user specified or the one that governs the matter?
- [ ] Does the output acknowledge the correct governing law instrument (e.g., for a UAE employment matter: Federal Decree-Law 33/2021, not the predecessor Labor Law 8/1980)?
- [ ] If the matter involves multiple jurisdictions: does the output correctly distinguish between them (e.g., differentiating UAE onshore law from DIFC law for a matter involving entities in both zones)?

---

### Check 4 — Are all numbers and dates correct?

AI models make numerical errors, particularly:
- Transposing digits (e.g., "Article 34" instead of "Article 43")
- Applying the wrong threshold or penalty amount
- Misquoting a date (e.g., the year of an amendment)
- Incorrect calculation of a duration ("within 30 days" cited as "within 60 days")

- [ ] Every specific number in the output has been verified against the source
- [ ] Every date has been verified
- [ ] Every calculated duration or deadline has been independently verified
- [ ] Every monetary threshold or penalty amount has been confirmed against the current statutory text (statutory thresholds are frequently updated)

---

### Check 5 — Has currency of the law been validated?

AI training data has a knowledge cutoff. Laws change. Amendments, implementing regulations, and new judgments may have come into effect after the AI's training data cutoff.

- [ ] For each jurisdiction covered in the output: has the law been checked for amendments since the AI's knowledge cutoff?
- [ ] Specifically check: UAE FDL 33/2021 implementing regulations (ongoing); KSA PDPL implementing regulations (2023); EU AI Act implementation (2024–2026 phase-in); any jurisdiction where a major reform was recently enacted

**Practical approach:** For commonly-changing areas (data protection, employment, AML/KYC, corporate law), check the relevant regulatory authority's website for announcements issued within the past 12 months. A 5-minute check is sufficient for routine output; a deeper check is required for client-facing work or regulated industry advice.

---

### Check 6 — Is the conclusion supported by the analysis?

This is the logical verification step — confirming that the AI's conclusion follows from the analysis it presented.

- [ ] Does the stated conclusion follow from the AI's own reasoning? (An AI may correctly state the legal framework and then state a conclusion inconsistent with it)
- [ ] Does the analysis address the actual question asked, or a related-but-different question? (AI sometimes answers a slightly different question more easily than the hard one)
- [ ] Is the conclusion qualified correctly? If the law is uncertain or jurisdiction-specific, does the conclusion say so, or does it state things with false confidence?

---

### Check 7 — Does the answer satisfy the question asked?

Before sending any output:

- [ ] Re-read the original question or instruction
- [ ] Read the AI's output as if you are the recipient
- [ ] Ask: has the question been answered? Or has the AI answered a related question, provided general background, or hedged so much that the actual answer is obscured?

If the question has not been fully answered, the output requires revision before it is released.

---

## Escalation rules

| Output type | Verification standard |
|---|---|
| Internal research memo (not sent to client) | Checks 1, 2, 3, 6, 7 required; Check 5 recommended |
| Client-facing memo or advice | All 7 checks required |
| Contract or transactional document | Checks 1, 3, 4, 5, 7 required |
| Court filing or pleading | All 7 checks required; independent review by a qualified lawyer required |
| Regulatory submission | All 7 checks required; verify against regulator's most recent guidance |
| High-value transaction (> AED 5M / USD 1.5M) | All 7 checks; qualified lawyer review required |

**Never skip verification on high-stakes outputs.** A confident AI output that is factually wrong about a statute number or case holding is more dangerous than an incomplete output — because it can be relied upon without verification.

---

## How to use this reference efficiently

For routine outputs, verification should take 5–15 minutes. For high-stakes outputs, allocate 30–60 minutes.

- Work through the checklist in order
- Mark each item as confirmed or flagged
- If any item is flagged, correct the output before release
- Do not release an output with unresolved flags

Pair with [[ref-anti-patterns]] (Anti-Pattern 1: over-trusting AI outputs, and Anti-Pattern 5: pasting unverified citations) for the rationale behind each check.

---

## Related skills

- [[ref-anti-patterns]]
- [[ref-privilege-layers]]
- [[ref-long-documents-50pp]]
- [[ref-skill-authoring]]
