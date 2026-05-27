---
name: answer-affirmative-defenses
title: Answer and Affirmative Defenses
description: Drafts U.S. civil litigation Answers with paragraph-by-paragraph admissions/denials, affirmative defenses, and counterclaim triage. Trigger when user needs a responsive pleading to a complaint, mentions affirmative defenses, admit/deny responses, Rule 8, or insufficient knowledge responses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/answer-affirmative-defenses
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Answer and Affirmative Defenses

Drafts a rule-compliant Answer with strategic admissions/denials and preserved affirmative defenses to avoid waiver.

## Prerequisites

Collect before drafting:

1. **Complaint** — filed version with numbered paragraphs and caption
2. **Service data** — date, method, proof of service
3. **Client facts** — timeline, documents, communications, witnesses
4. **Governing instruments** — contracts, policies, statutes
5. **Jurisdiction rules** — local rules on format, verification, deadlines

## Workflow

### 1. Caption + Appearance

- Match court, parties, case number exactly from complaint.
- Note general vs special appearance (if contesting jurisdiction/venue).

### 2. Response Matrix

Build a response table before drafting the pleading body.

| ¶ | Allegation | Response | Qualification | Source |
|---|---|---|---|---|
| 1 | Party identity | Admit | Name/status only | Client docs |
| 2 | Jurisdiction | Deny | — | Investigate |
| 3 | Contract exists | Qualified | Admit execution; deny breach | Contract |

Response types: **Admit** · **Deny** · **Lack knowledge** (deny on that basis) · **Qualified admit/deny**

### 3. Paragraph-by-Paragraph Responses

Response templates:

- **Admit**: "Defendant admits the allegations in Paragraph __ of the Complaint."
- **Deny**: "Defendant denies the allegations in Paragraph __ of the Complaint."
- **Lack knowledge**: "Defendant lacks knowledge or information sufficient to form a belief as to the truth of the allegations in Paragraph __ and on that basis denies them."
- **Qualified**: "Defendant admits [specific fact] as alleged in Paragraph __, but denies the remaining allegations in that paragraph."

Rules: Address every paragraph. Separate factual admissions from legal conclusions. Do not overuse lack-knowledge where defendant should reasonably know.

### 4. Affirmative Defenses

Number each defense separately. Include brief factual grounding without overcommitting.

**Procedural**: lack of subject-matter jurisdiction, lack of personal jurisdiction, improper venue, insufficient service, failure to join indispensable party, lack of standing.

**Substantive**: failure to state a claim, statute of limitations, statute of frauds, waiver, estoppel, laches, release, accord and satisfaction, payment, arbitration/award, unclean hands, illegality, comparative/contributory negligence, failure to mitigate.

Template: "[Defense Name]. Plaintiff's claims are barred because [factual basis]. The allegations show [timing/conduct/term], and the claim fails as a matter of law."

End with reservation clause: "Defendant reserves the right to assert additional defenses as they become known through discovery or further investigation."

### 5. Counterclaim Triage

- Compulsory counterclaim from same transaction?
- Permissive counterclaim worth asserting now?
- Cross-claim vs co-defendant (indemnity/contribution)?
- Third-party claim to shift liability?

If included, structure as: parties/jurisdiction → numbered factual allegations → cause of action with elements → damages and relief.

### 6. Prayer for Relief

Minimum: dismissal with prejudice, judgment for defendant, costs, attorney fees (if contractual/statutory basis), pre/post-judgment interest, catch-all "other relief as just and proper." Add specific relief tied to defenses or counterclaims.

### 7. Signature + Service

Attorney signature block with bar number. Verification if jurisdiction requires. Certificate of service with method and date.

## Quality Checklist

- [ ] Every complaint paragraph addressed — no admissions by omission
- [ ] Defenses tailored to facts and jurisdiction
- [ ] Counterclaims labeled compulsory/permissive
- [ ] Caption matches complaint exactly
- [ ] Deadline confirmed and calendared
- [ ] No defenses asserted without plausible factual basis
- [ ] Jurisdiction-specific pleading standard noted (notice vs fact)

## Pitfalls

- **Omitted paragraphs** may be deemed admitted — address every one.
- **Bare legal conclusions** should be denied, not admitted.
- **One-word defenses** risk being stricken — always include factual grounding.
- **Timing defenses** (limitations, laches) — verify periods before filing; flag if uncertain.
- **Verified answers** — check if jurisdiction or claim type requires defendant verification.
