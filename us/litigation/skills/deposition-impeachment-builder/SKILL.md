---
name: deposition-impeachment-builder
title: Deposition Impeachment Builder
description: Drafts deposition-ready impeachment sequences using the Commit–Credit–Confront (CCC) method. Use this skill when the user mentions impeachment preparation, prior inconsistent statements, Commit-Credit-Confront, CCC method, deposition cross-examination, FRE 613, witness contradictions, impeachment scripts, prior testimony conflicts, or asks for help building impeachment sequences. Also trigger when the user references creating transcript clips for summary judgment, preparing confrontation questions, or analyzing contradictions between deposition testimony and prior documents. Even if the user just says "this witness changed their story" or "build me an impeachment sequence," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-impeachment-builder
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, checklist, drafting, summary]
---

# Deposition Impeachment Builder

## Why This Skill Exists

Impeachment at deposition is the highest-skill questioning technique in civil litigation — and the most commonly botched. Attorneys either confront too early (before locking the witness in), skip the credit phase (weakening the contradiction's impact), or ask open-ended follow-ups after confrontation (giving the witness an escape). A poorly executed impeachment is worse than none at all, because it educates the witness and inoculates them for trial.

This skill produces a controlled Commit–Credit–Confront script, a deployment memo with timing recommendations, and a checklist of missing information — grounded in FRE 613, FRE 801(d)(1)(A)/(d)(2), and FRCP 30 guardrails.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Current testimony** — verbatim transcript excerpt (Q&A with page/line) or exact anticipated answer; paraphrases require attorney confirmation of precise phrasing
2. **Prior statement** — full text (not snippet), statement type, date, author/speaker, recipients, and pin-cite (page:line for transcripts; paragraph/section for documents)
3. **Witness's connection** — how the witness authored, signed, verified, sent, or adopted the prior statement
4. **Case context** — forum (federal/state), posture (fact discovery/MSJ/pretrial), claims/defenses, witness role (party, 30(b)(6) designee, percipient, expert)
5. **Strategic intent** — impeachment only vs. substantive use; video deposition; protective order applicability

**If the user doesn't respond**, apply and clearly label these defaults: federal court; impeachment-only use; conservative confrontation variant; deposition (not trial).

> **If any required input is missing, pause and ask targeted follow-up questions. Never fabricate quotes, dates, page numbers, or document attributes.**

---

## Step 1: Assess Materiality

Before drafting, tie the contradiction to a claim element, defense element, damages component, or credibility theme in one sentence. If you cannot, flag the impeachment as a candidate for trial cross-examination rather than deposition use.

---

## Step 2: Draft the Commit Phase

**Goal:** Eliminate every escape hatch before the witness knows a contradiction is coming.

Rules:
- Use the witness's own vocabulary
- Single factual proposition per question
- No compound questions
- Define ambiguous terms neutrally before committing
- Confirm certainty; fork hedged answers into a second committed proposition

**Template pattern:**
```
"Just so I understand: you [core proposition], correct?"
"You're not saying [narrowing qualifier]—you're saying [absolute proposition], right?"
"You're certain about that? No doubt in your mind?"
"And [close remaining escape route], correct?"
```

---

## Step 3: Draft the Credit Phase

Establish reliability and adoption of the prior statement. Tailor foundation to prior statement type:

| Statement Type | Credit Focus | Key Questions |
|---|---|---|
| **Prior deposition/hearing testimony** | Oath, counsel present, opportunity to correct errata | "You were under oath?" / "Your lawyer was present?" / "You reviewed and didn't change this testimony?" |
| **Signed declaration / verified response** | Signature, review, penalty of perjury | "You read this before signing?" / "You swore the contents were true?" |
| **Email / text authored by witness** | Account ownership, routine practice, contemporaneity, recipients, intent to rely | "That's your email address?" / "You sent this in the ordinary course?" / "You intended [recipient] to rely on it as accurate?" |
| **Email / doc drafted by others, adopted by witness** | Review, approval, transmission authority | "You reviewed this before it was sent?" / "You authorized it to go out?" |
| **Interrogatory response** | Witness's role in preparation, verification, accuracy steps | "Did you review the draft?" / "You signed the verification?" |
| **Corporate record / third-party doc** | Receipt, reliance, notice — **flag:** may not constitute witness's "statement"; different evidentiary posture | "You were copied?" / "You relied on it?" |

**Credit containment:** If witness tries to devalue the prior statement mid-Credit ("I was confused"):
> "You wouldn't give false testimony just because you were [tired/confused], right?"

---

## Step 4: Draft the Confront Phase

Disciplined rhythm — do not deviate:

1. **Re-commit** — immediately restate current testimony
2. **Mark and orient** — mark exhibit or identify by Bates; confirm witness is on correct page/line
3. **Read verbatim** — quote exact language; include `[PAGE:LINE]` placeholder if pin-cite unavailable
4. **Obtain admission** — two variants:

| Variant | Language | Use When |
|---|---|---|
| Conservative | "So your testimony today is different from what you said under oath on [DATE], correct?" | Preserving the record; avoiding overreach |
| Aggressive | "Which is accurate — your [email/deposition] from [DATE], or your testimony today?" | Witness is a party; full contradiction is binary |

5. **Stop.** Do not ask "why," "how," or "could it be." No open-ended questions after confrontation.

**Containment follow-ups** (if witness evades):
- "What part is inaccurate?"
- "When did you first realize it was wrong?"
- "Who told you that?" / "What document did you review?"
- "Where is that reflected in writing?"

---

## Step 5: Produce the Deployment Memo

Include:
- **What this impeachment accomplishes** (element/credibility theme it addresses)
- **Timing recommendation** — impeach now vs. bank for trial
- **Opposing responses to anticipate** and containment strategy
- **Substantive vs. impeachment-only use** — flag for attorney analysis under FRE 801(d)(1)(A) / 801(d)(2)

**Timing decision table:**

| Objective | Timing | Rationale |
|---|---|---|
| Discovery roadmap | Early | Forces witness to explain, surfaces documents/witnesses |
| Trial-quality clip | Bank | Starker after multiple aligned denials; avoids educating witness |
| Settlement signal | Mid-deposition | Demonstrates narrative instability without full rehearsal |
| Rapid-fire credibility destruction | Series at end | Effective for witnesses with multiple contradictions |

---

## Step 6: Produce Missing Information Checklist

List all `[PLACEHOLDERS]` requiring attorney completion before use:
- `[PAGE:LINE]` — pin-cite for prior statement
- `[EXHIBIT NO.]` — exhibit identifier
- `[DATE]` — any unconfirmed date
- Any quotation labeled as a paraphrase requiring verbatim verification

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial impeachment package, ask:

1. Is the contradiction as framed accurate — does the current testimony and prior statement match what you have?
2. Should the confrontation use the conservative or aggressive variant?
3. Are there additional prior statements that could stack with this impeachment?
4. Should I draft the full sequence for deposition use or adapt it for trial cross-examination?

If the user doesn't answer, recommend the conservative variant and proceed if authorized.

---

## Quality Audit

Before finalizing, verify:

- Materiality test completed — contradiction tied to a claim element, defense, or credibility theme
- Commit phase uses single-proposition questions with no compound constructions
- Credit phase tailored to the specific prior statement type
- Confront phase uses verbatim quotation (or labeled placeholder)
- No open-ended questions after confrontation
- Deployment memo includes timing recommendation
- All placeholders clearly marked for attorney completion
- Evidentiary rule basis identified (FRE 613, 801(d)(1)(A), 801(d)(2))
- No fabricated quotes, page numbers, dates, or document attributes
- State-specific variations flagged if not federal

---

## Guidelines

**Evidentiary rules — federal defaults (flag state variations):**
- **FRE 613(a):** No obligation to show prior statement to witness before examining on it, but must disclose to adverse party's counsel on request
- **FRE 613(b):** Extrinsic evidence of prior inconsistent statement requires opportunity to explain or deny
- **FRE 801(d)(1)(A):** Prior inconsistent statement given under penalty of perjury at a proceeding or deposition is non-hearsay and usable substantively
- **FRE 801(d)(2):** Opposing party statements are non-hearsay
- **FRE 106 (Completeness):** Opposing counsel may require introduction of other portions; review full context before use

**State-specific flags:**

| Jurisdiction | Key Rule |
|---|---|
| California | EC § 770 — judge may exclude extrinsic evidence unless witness given opportunity to explain; EC § 780 — credibility factors |
| New York | CPLR 4514 — stricter limits on unsworn/unwritten prior statements |
| Common law (Browne v. Dunn) | Must "put the case" to the witness — confront explicitly before relying in closing |
| Arbitration | AAA/JAMS rules and scheduling order govern; treat as separate regime |

**Professional responsibility:**
- ABA Model Rule 3.3 — candor when excerpts used in court filings
- ABA Model Rule 3.4 — do not impeach with a document that does not actually contain the contradiction
- ABA Model Rule 4.2 — all questioning through formal proceeding with counsel present

**Anti-hallucination (non-negotiable):**
- Never invent page/line numbers, quotation marks around fabricated text, dates, or document attributes
- Every proposed quotation without a verbatim source must be labeled `[PLACEHOLDER — VERIFY BEFORE USE]`
- Every case law or statutory citation must be verified or labeled `[VERIFY]`

**Attorney review required before use in any proceeding. This skill is attorney work product, not legal advice.**
