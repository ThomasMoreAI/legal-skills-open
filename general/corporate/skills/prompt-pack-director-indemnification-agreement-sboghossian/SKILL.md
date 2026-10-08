---
name: prompt-pack-director-indemnification-agreement-sboghossian
title: Director Indemnification Agreement
description: 'Use when a company needs to draft an indemnification agreement for its directors and officers, covering scope of indemnification, advancement of expenses, exclusions (fraud, criminal conduct), insurance requirements, and the procedure for claiming indemnification. MENA-aware: addresses UAE, KSA, LB, EG companies law limitations on director indemnification; contrasts DIFC/ADGM common-law approach; covers the relationship between the D&O agreement and D&O insurance.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-director-indemnification-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Director Indemnification Agreement

A Director Indemnification Agreement (also called a Deed of Indemnity or D&O Indemnity Agreement) supplements statutory protections and D&O insurance by creating a direct contractual obligation between the company and each director. It matters most when insurance coverage is disputed, the insurance policy has expired, or the loss exceeds the policy limit. Without it, directors are exposed to personal liability for decisions made in good faith in their official capacity.

## When to use this

- A company is appointing new directors — individual indemnification agreements should be signed at the time of appointment.
- The company is seeking experienced independent directors and the prospective directors have requested confirmation of indemnification arrangements.
- A listed company's governance review has identified the absence of individual D&O indemnification agreements as a gap.
- Following a corporate incident (regulatory investigation, shareholder claim) that has exposed the risk of personal director liability.
- A company is expanding internationally and new-jurisdiction directors need agreements aligned with local law.
- A MENA company is establishing a DIFC or ADGM entity and needs a common-law compliant indemnification agreement.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction of incorporation | Determines the applicable companies law framework | Ask the user |
| Director's full name and role | The agreement is specific to an individual | Ask the user |
| Governing law | Must align with the jurisdiction where the company is incorporated and the director's duties arise | Ask the user; default to jurisdiction of incorporation |
| Scope of protection desired | Full indemnity vs. partial (limited by statute) | Ask the user; note statutory limits below |
| Whether D&O insurance is in place | The indemnity agreement should operate as a backstop to, not a replacement for, D&O insurance | Ask the user |

## Optional inputs

- Whether the agreement covers subsidiary directorships held at the company's request.
- Whether the agreement covers former directors (post-resignation tail coverage is recommended).
- Whether the agreement is to be executed as a deed (recommended for maximum enforceability).
- Maximum indemnification cap (some companies impose a cap; others do not).

## Document structure

### 1. Parties and background
- The company (full legal name, jurisdiction) and the director (full name, address, appointment date, and role).
- Recital: the director serves at the request of the company and has agreed to do so on the basis of the indemnification set out in this Agreement.

### 2. Scope of indemnification

**Standard scope:**
The company indemnifies the director against:
- All claims, proceedings, damages, and losses arising from the director's service in their official capacity.
- Legal fees and expenses reasonably incurred in connection with any investigation, claim, or proceeding.
- Judgments, fines, penalties, and settlement amounts that are not otherwise reimbursed by D&O insurance.
- Claims by shareholders, regulators, third parties, or employees arising from the director's official conduct.

**Subsidiary and affiliate directorships:**
The indemnity should extend to directorships in group companies held at the company's request.

**Former director tail:**
The indemnity should survive resignation or removal and cover claims arising from acts or omissions during the director's tenure.

### 3. Advancement of expenses

One of the most practically important provisions:
- The company will advance legal fees and expenses to the director as they are incurred, before the final determination of whether the director is entitled to indemnification.
- Advancement requires an undertaking from the director to repay if it is ultimately determined that they are not entitled to indemnification.
- The advancement right is critical: directors cannot wait until the end of potentially years-long proceedings to be reimbursed; the cost of defence is immediate.

### 4. Exclusions

Indemnification is not available for:

**Universal exclusions (applicable in all jurisdictions):**
- Fraud, willful misconduct, or dishonesty.
- Criminal conduct where the director is convicted.
- Wilful disregard of the director's duties.
- Claims where the director acted in bad faith.
- Intentional violation of applicable law.
- Fines imposed by criminal courts (cannot indemnify against criminal fines in most jurisdictions).

**Civil law jurisdiction exclusions (UAE, KSA, LB, EG):**
- In UAE, the Companies Law (Federal Decree-Law No. 32 of 2021) provides that indemnifying a director against liability for negligence or breach of fiduciary duty is subject to statutory limits; gross negligence may not be indemnifiable.
- In KSA, the Companies Law (Royal Decree M/3, 2015) similarly limits indemnification for wilful misconduct.
- In Lebanon, directors' personal liability under commercial company law cannot be excluded; indemnification for third-party claims is generally permissible.
- In Egypt, Companies Law No. 159 of 1981 (as amended) restricts indemnification for fraud and gross negligence.

**Common law jurisdictions (DIFC, ADGM, UK):**
- DIFC Companies Law 2018 permits indemnification against third-party liability and against costs of defending proceedings brought by the company, subject to statutory exceptions for fraud and bad faith.
- ADGM Companies Regulations permit equivalent indemnification.
- UK Companies Act 2006 ss. 232–236: a company cannot exempt a director from liability to the company itself (including derivative claims), but can indemnify against third-party claims (Qualifying Third Party Indemnity Provision — QTPIP).

**Key distinction:** Most civil and common law jurisdictions distinguish between:
- **Third-party claims** (claims by shareholders, regulators, and third parties) — generally indemnifiable.
- **Company's own claims against the director** — generally not indemnifiable; would constitute returning the loss to the company.

### 5. Insurance obligation
- The company undertakes to maintain Directors' and Officers' Liability Insurance (D&O insurance) for the benefit of the director at specified minimum coverage levels.
- The indemnification agreement operates as a backstop where D&O insurance does not cover, or where coverage is denied or insufficient.
- The director is named as an additional insured under the D&O policy.
- The company undertakes to notify the director before cancelling or materially reducing D&O coverage.

**D&O insurance levels for MENA companies:**
- Minimum recommended: USD 5–10 million per claim for mid-size companies; USD 20–50 million for listed or large companies.
- Side A coverage (individual director coverage where the company cannot or does not indemnify) is the most important component for directors.

### 6. Procedure for claiming indemnification

- **Notice:** The director must notify the company of any claim, investigation, or proceeding as soon as possible, and in any event within [30] days of becoming aware.
- **Cooperation:** The director must cooperate with the company and its insurers in the defence of any claim.
- **Control of defence:** Address whether the company controls the defence or the director controls the defence (with the company funding). For regulatory investigations against the director personally, the director typically needs independent counsel.
- **Approval of settlements:** The director must obtain the company's consent before settling any claim covered by the indemnity (to avoid the company being bound by an unfavorable settlement made for the director's personal convenience).
- **Claiming advancement:** Process for submitting a request for advancement of expenses (typically a written request with an estimate and an undertaking to repay if found not entitled).

### 7. Subrogation
- If the company pays an indemnity amount, it is subrogated to the director's rights of recovery against any third party.
- The director must assign any recovery rights to the company to the extent of the indemnity paid.

### 8. Miscellaneous
- The agreement is independent of any other agreement between the company and the director (including the appointment letter or service agreement).
- The agreement may be amended only by written agreement signed by both parties.
- Execution as a deed: recommended for maximum enforceability; a deed has a longer limitation period than a simple contract in common-law jurisdictions.

## Jurisdictional notes

| Jurisdiction | Key constraint | Recommended approach |
|---|---|---|
| UAE (onshore) | Companies Law limits indemnification for wilful misconduct; indemnity for gross negligence is uncertain | Cover third-party claims; pair with UAE-admitted D&O insurance |
| UAE (DIFC) | DIFC Companies Law permits QTPIP-style indemnification; Side A D&O insurance strongly recommended | DIFC QTPIP structure; include advancement of expenses |
| UAE (ADGM) | Equivalent to DIFC | ADGM-compliant structure |
| KSA | Companies Law limits scope; Arabic language agreement required for enforceability before Saudi courts | Cover third-party claims; KSA-admitted D&O insurance; Arabic version required |
| Lebanon | Indemnity for third-party claims generally permissible; directors still personally liable to the company | Cover third-party claims; Lebanon-admitted D&O policy |
| Egypt | Companies Law No. 159 restricts indemnification for fraud and gross negligence | Cover third-party claims; Egypt-admitted D&O insurance |

## Common mistakes

- No advancement of expenses clause — the most practical protection for directors is immediate funding of defence costs, not reimbursement at the end.
- The exclusion for "gross negligence" is broader than the applicable law requires — this can strip protection for ordinary business mistakes (gross negligence is a high bar, not the same as bad judgment).
- Not addressing what happens when the director and the company have conflicting interests in the defence — this requires independent counsel and a clear protocol.
- Failing to maintain D&O insurance and not disclosing this to directors — directors who accept appointments on the basis of insurance coverage they discover later is inadequate have a claim against the company.
- No tail coverage provision — former directors are often sued for acts during their tenure years after they have left; the indemnity should explicitly survive departure.

## Related skills

- [[prompt-pack-corporate-governance-policy]]
- [[prompt-pack-code-of-conduct]]
- [[prompt-pack-delegation-of-authority-matrix]]
- [[prompt-pack-d-and-o-insurance-review]]
- [[prompt-pack-corporate-resolutions]]
