---
name: review-nda-quick-check-sboghossian
title: NDA Quick Check (5-Minute Review)
description: Use when a fast (5-minute) NDA review is needed to assess whether an NDA is safe to sign, needs negotiation, or should be rejected as drafted. Runs a 10-point checklist covering mutual vs unilateral structure, Confidential Information definition, permitted recipients, term, return/destruction, no-license language, remedies, governing law, jurisdiction-specific execution requirements, and boilerplate. Produces a traffic-light rating and links to counter-proposal drafting.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-nda-quick-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Quick Check (5-Minute Review)

## When to use this

Use when:
- A counterparty has sent an NDA for signature and you need a rapid assessment of whether it is safe to sign
- A client asks "is this NDA okay?" — you need to give a quick, structured answer
- You have 5–10 minutes before a meeting to flag the biggest issues
- You want a first-pass before running a deeper review

This skill delivers a go / negotiate / reject verdict plus a prioritized list of issues. For a more thorough review, escalate to [[review-unusual-terms-detector]] and [[review-missing-clauses]].

## Inputs

| Input | Why it matters | Default |
|---|---|---|
| NDA text | Full document | Required |
| Party's role | Disclosing party, receiving party, or both? | Ask if unclear |
| Jurisdiction | Affects enforceability of term, scope, and execution requirements | Infer from governing-law clause; ask if absent |
| Purpose | Why are the parties entering into the NDA? (M&A discussions, vendor evaluation, employment) | Ask if not obvious from document |

## 10-Point Quick Checklist

Run through each item; output a Yes / No / Issue flag:

### 1. Mutual or Unilateral?

- Confirm whether the NDA is mutual (both parties can disclose and receive) or unilateral (one party only discloses)
- Does it match what the user expects? A counterparty sending a one-sided NDA when both parties will be sharing information is an immediate flag
- For M&A preliminary discussions: mutual is standard
- For vendor/supplier evaluations where only the vendor shares proprietary information: unilateral from vendor is acceptable

### 2. Definition of Confidential Information

A complete definition:
- Covers written, electronic, oral, and visual disclosures
- May include a marking requirement (written information must be marked "Confidential") — note: an oral marking-based definition is problematic if oral disclosures are expected but cannot be marked
- Contains the **four standard exclusions**:
  1. Information already in the public domain (not through breach)
  2. Information the Receiving Party independently developed without reference to Confidential Information
  3. Information lawfully received from a third party without restriction
  4. Information the Receiving Party already knew before disclosure (must be documented)

Flag: if any of the four exclusions is absent — the definition is overbroad and the Receiving Party may be restricted from using information it legitimately owns or developed independently.

### 3. Permitted Recipients

A well-drafted clause:
- Limits disclosure to employees, officers, directors, and professional advisors who have a need to know
- Requires Receiving Party to impose equivalent confidentiality obligations on those recipients (flow-down)
- Treats any breach by a recipient as a breach by the Receiving Party

Flag: permitted recipients too broad (e.g., "group companies" without need-to-know limitation); no flow-down obligation; no liability for recipients' breaches.

### 4. Term — Duration of Obligations

Market ranges:
- Commercial NDAs (general vendor evaluation): 2–3 years
- M&A preliminary discussions: 2–5 years (longer survival appropriate)
- Technology / trade secrets: 5–7 years or indefinite for specific trade secret categories (different rules by jurisdiction)
- Employment: post-termination confidentiality is often longer or indefinite but must be proportionate

Flag: perpetual obligation for all information (including general business information) — may be unenforceable in some jurisdictions and is commercially unusual. Perpetual treatment is appropriate only for genuine trade secrets, defined specifically.

### 5. Return / Destruction Obligation

On expiry of the NDA, or upon request by the Disclosing Party:
- All Confidential Information and copies must be returned or certifiably destroyed
- Certification of destruction is standard (a written statement from a senior officer)
- Exception: automatically-archived copies (backup systems) and legally required retention are typically excluded from destruction

Flag: no return/destruction obligation — allows Receiving Party to retain Confidential Information indefinitely. This is also a data protection compliance issue where personal data is involved.

### 6. No License / No IP Transfer Language

The NDA should expressly state:
- Disclosure of Confidential Information does not grant any license, right, or title to any IP
- No obligation to disclose anything is created by the NDA itself (the NDA merely governs what happens if information is disclosed)
- No obligation to proceed with any transaction is created

Flag: absence of this language creates an argument that the disclosure implied a license — particularly relevant for technology NDAs where proprietary methods or code are shared.

### 7. Injunctive Relief

Standard remedy provision:
- The parties acknowledge that monetary damages may be inadequate for breach
- Each party is entitled to seek injunctive or other equitable relief without posting bond and without proving actual damages
- This is in addition to other remedies, not exclusive

Flag: NDA limited to damages only — makes enforcement effectively impossible given the difficulty of proving loss from a disclosure. In many jurisdictions, injunctions are obtainable even without this clause, but the express language removes disputes.

### 8. Governing Law and Forum Selection

Check:
- Is governing law specified? (If not — see [[review-missing-clauses]])
- Does the chosen law / forum favor the user's party?
- For cross-border NDAs: check whether courts of the chosen jurisdiction will enforce the NDA as written; some jurisdictions have limitations on confidentiality enforcement terms

**MENA-specific flags**:
- KSA: if confidentiality disputes arise, specifying SCCA arbitration is faster than general courts; court enforcement of injunctions is possible but slower
- UAE: DIFC Courts have efficient injunction procedures; specifying DIFC Courts for enforcement adds value if either party has DIFC assets
- Lebanon: enforcement of foreign-court judgments is possible under reciprocity but domestic courts are preferred for speed

### 9. Jurisdiction-Specific Execution Requirements

Before signing, verify local form requirements:

| Jurisdiction | Requirement |
|---|---|
| LB | Some commercial documents benefit from notarization (Tawqi3i) for enforceability in local courts; cross-border NDAs with foreign parties may need Apostille |
| UAE | Commercial documents executed outside UAE may need notarization + Apostille + MOFA attestation for use in UAE courts or RERA filings |
| KSA | Notarization (توثيق) at a Saudi notary public (كاتب عدل) required for certain categories; English-language NDAs may need a certified Arabic translation |
| US | No general notarization requirement for commercial contracts; e-signatures under ESIGN Act are valid |
| DIFC / ADGM | E-signatures valid; no notarization requirement |

### 10. Boilerplate Completeness

Confirm the following are present:
- **Entire agreement**: this NDA supersedes prior discussions on confidentiality (prevents argument that earlier oral NDA had different terms)
- **No waiver**: failure to enforce a breach does not waive future breaches
- **Severability**: if one clause is void, the rest remain in force
- **Notices**: address for formal notices (must match Commercial Registration / official address)
- **Amendment**: amendments require written agreement signed by both parties

Flag: absent boilerplate is a medium risk item — individually minor; collectively creates enforcement gaps.

## Traffic-Light Output

After completing all 10 checks, issue a verdict:

| Rating | Criteria | Action |
|---|---|---|
| Green — Safe to sign | All 10 checks pass; no material issues | Proceed; note any low-priority suggestions |
| Yellow — Negotiate | 1–3 items require negotiation; no fatal flaws | Identify top priorities; draft counter-positions |
| Red — Reject as drafted | Fundamental structural issue (e.g., no CI definition; perpetual overbroad obligation; no exclusions; wrong party structure) | Return to drafter with marked-up counter-proposal |

## Counter-Proposal Drafting

If the verdict is Yellow or Red, offer to:
- Produce a marked-up counter-proposal addressing the identified issues (use [[draft-nda-mutual]] or [[draft-nda-unilateral]])
- Prioritize the top 3 items to push on if full counter is not practical

## Common Mistakes in NDA Review

- Treating "perpetual" obligation for generic business information as acceptable — it is usually not and may be void
- Missing the absence of the fourth exclusion (prior knowledge) — allows the Receiving Party to be bound by information it already knew
- Not checking whether the NDA binds affiliates — if the NDA only names the contracting entity, disclosures to the parent company may not be covered
- Not checking the definition of "Representatives" or "Permitted Recipients" to ensure professional advisors (lawyers, accountants) are included with appropriate flow-down

## Related Skills

- [[review-unusual-terms-detector]]
- [[review-missing-clauses]]
- [[review-risk-flagging]]
- [[draft-nda-mutual]]
- [[draft-nda-unilateral]]
- [[review-signature-block-validity]]
