---
name: legal-opinion-letter
title: Legal Opinion Letter
description: Drafts formal legal opinion letters for corporate and transactional matters with jurisdiction-specific analysis, calibrated conclusion language, and comprehensive qualifications. Use when drafting closing opinion letters, third-party reliance opinions, enforceability opinions, or corporate authority opinions for mergers, acquisitions, financings, or regulatory compliance.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/legal-opinion-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Legal Opinion Letter

Produces a formal opinion letter with structured sections: scope, factual recitation, legal analysis, calibrated conclusions, and qualifications. Ensures proper assumptions, citation standards, and reliance limitations.

## Prerequisites

Gather before drafting:

1. **Transaction description** — structure, parties, purpose (M&A, financing, regulatory)
2. **Governing documents** — agreements, corporate records, certificates, resolutions
3. **Jurisdictions** — governing law and jurisdictions requiring analysis
4. **Opinion recipient** — client only or named third-party relying parties
5. **Specific questions** — enumerated legal issues the opinion must address
6. **Exclusions** — matters outside scope (tax, securities, antitrust, etc.)

## Letter Sections

Draft the following sections in order:

### 1. Introduction

Firm letterhead, date, recipient, and "Re:" line. One paragraph identifying the relationship, transaction, and purpose.

### 2. Scope of Opinion

Number each legal question being answered. Explicitly exclude out-of-scope matters:

| Excluded Matter | Note |
|---|---|
| Tax consequences | Advise client to consult tax counsel |
| Securities law compliance | Advise client to consult securities counsel |
| Antitrust / regulatory | Note if applicable |
| Business judgment / wisdom | Outside legal analysis |
| Laws of non-covered jurisdictions | Identify which are covered |

### 3. Documents Reviewed

Enumerated list with full titles, execution dates, parties, and relevant sections.

### 4. Factual Background

Material facts only. Categorize each:
- **Verified** — confirmed through document review (cite document, section, page)
- **Represented** — accepted as client representations
- **Assumed** — assumed for purposes of the opinion (flag prominently)

### 5. Assumptions

Include standard assumptions (tailor as needed):

- [ ] Signatures genuine and authorized
- [ ] Documents authentic and complete; no undisclosed amendments
- [ ] Signatories had requisite corporate authority
- [ ] No oral modifications to written agreements
- [ ] Entities duly formed and in good standing
- [ ] No insolvency proceedings pending or contemplated
- [ ] No undisclosed facts affecting the analysis

### 6. Legal Analysis

For each scoped question: state applicable law with full citation, apply rule to facts, address counterarguments or ambiguities. Where authority is split, acknowledge directly and explain basis for preferring one line.

**Citation standards:**
- Statutes: current version; note pending amendments `[VERIFY]`
- Cases: confirm not overruled; note binding vs. persuasive; pinpoint cite
- Regulations: current CFR section and effective date
- Agency guidance: note persuasive (not binding) weight

### 7. Conclusions

Use calibrated language matched to confidence:

| Confidence | Language |
|---|---|
| High (clear law, undisputed facts) | "It is our opinion that..." |
| Moderate (some ambiguity) | "It is our opinion that it is more likely than not that..." |
| Predictive (court outcome) | "We believe a court would likely conclude that..." |
| Conditional | "Assuming [X], it is our opinion that..." |

Number conclusions parallel to the scoped questions.

### 8. Qualifications and Limitations

- [ ] Opinion as of the letter date; no duty to update
- [ ] Based solely on laws of specified jurisdictions as of opinion date
- [ ] Does not address laws of other jurisdictions
- [ ] Reliance limited to named recipient(s) / client only
- [ ] No distribution or reliance by others without written consent
- [ ] Subject to equitable principles, bankruptcy/insolvency law, public policy
- [ ] Subject to general principles limiting specific remedies

### 9. Signature Block

Attorney name, bar admission (jurisdiction, number), title, firm, contact. For firm opinions, clarify signing capacity and whether institutional.

## Pitfalls

- **Scope creep** — never opine beyond enumerated questions; unsolicited opinions create unintended liability
- **Certainty calibration** — excessive hedging is as problematic as overstatement; use the table deliberately
- **Citation verification** — never cite from memory; mark uncertain citations `[VERIFY]`
- **Third-party reliance** — identify relying parties by name; time-limit reliance where appropriate
- **Local counsel** — if opining on a jurisdiction where drafter is not admitted, note basis for confidence
- **Length** — typically 3-10 pages; do not pad with background law that adds no analytical value
