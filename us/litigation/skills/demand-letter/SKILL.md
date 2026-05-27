---
name: demand-letter
title: Pre-Suit Demand Letter
description: Drafts litigation-ready U.S. pre-suit demand letters that function as settlement instruments and defensible future exhibits. Enforces element-driven narratives, verified authority, damages methodology, and ethics guardrails. Use this skill when the user mentions demand letter, pre-suit demand, breach and cure notice, settlement demand, insurance policy-limits demand, Stowers demand, FDCPA collection letter, notice of intent to file, cease and desist demand for payment, or pre-litigation correspondence. Also trigger when the user asks about FRE 408 framing, contractual notice compliance, statutory pre-suit prerequisites, evidence preservation notices, or quantifying damages for a demand package. Skill includes 14 verified real-letter exemplars referenced from `references/ARCHETYPE-INDEX.md`.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/demand-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, letter]
---

# Pre-Suit Demand Letter

A demand letter is simultaneously a settlement instrument and a future exhibit. A defective letter can contain admissions, unsupported claims, or ethics violations — and where statutory pre-suit notice is required (TX DTPA 60-day, MA Ch. 93A 30-day, FL med-mal, CLRA, FDCPA, construction defect), defects can waive claims entirely. This skill produces letters where every assertion is sourced, every theory verified or flagged, damages are quantified with methodology, and tone is calibrated for judicial review.

This file (SKILL.md) is the controller: intake checkpoints, step-by-step decision rules, quality audit. Operational detail lives in `references/` — open those files when a step tells you to.

---

## How to use this skill

**`[AGENT]`** — Run Checkpoint A (intake). Then Steps 1–8 in order. Then Checkpoint B (post-draft alignment). Then the Quality Audit. Open files in `references/` when a step says to. Never skip a step silently; if a step does not apply, state that.

**`[ATTORNEY]`** — Treat this as a checklist. Skim Steps 1–8; open `references/` files as needed for drafting detail; use the Quality Audit as the pre-send gate. The decision rules in Steps 1–8 mark where the skill's default posture yields to your judgment — override consciously, not by omission.

---

## Related skills

- `legal-research` — verify the statutory regime for the letter's state/claim type; resolve SOL tolling; check any case law cited
- `citation-bluebook` — Bluebook format + good-law status on cases referenced
- `spoliation-letter` — produce a dedicated preservation demand when Step 5 identifies high-risk evidence (surveillance, EDR, ESI systems); demand-letter's §5 is a trigger + catch-all, not a substitute
- `anthropic-skills:docx`, `anthropic-skills:pdf` — produce the final letter as a file deliverable, invoked only after the Quality Audit passes
- Adjacent workflows: `pi-demand-summary` (builds the damages narrative that feeds §4), `demand-package` / `demand-package-compilation` (assembles the letter plus exhibits into a transmittable package), `bad-faith-demand` (insurer-directed escalation after a policy-limits demand is refused)

---

## Output format

Default: return the letter inline in chat. Invoke `anthropic-skills:docx` or `anthropic-skills:pdf` **only** when the user explicitly asks for a file deliverable, and **only** after the Quality Audit passes — never before. Do not return both formats unless asked.

If the user says "send it," stop. Demand letters require attorney signature and service. This skill drafts; it does not send.

---

## Checkpoint A: Pre-Draft Intake (Mandatory) `[AGENT action]`

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Governing contract(s)** — notice clauses, cure provisions, forum-selection, arbitration clauses
2. **Correspondence** — emails, letters, texts in chronological order
3. **Financial records** — invoices, payments, chargebacks, proof of tender
4. **Supporting evidence** — incident reports, photos, expert reports, third-party communications
5. **Prior demands** — settlement communications or notices already sent
6. **Statute of limitations** — accrual date, tolling facts, contractual limitations periods. **Decision rule:** if tolling facts exist, OR the accrual date is unclear, OR the claim appears near SOL, trigger `legal-research` before drafting.
7. **Forum facts** — entity citizenship, principal place of business, forum-selection clauses
8. **Client objectives** — preferred outcome, authorized settlement ceiling, timing, relationship preservation. **The ceiling in this item is what "authorized range" means in Checkpoint B.**
9. **Recipient entity** — corporate name as filed with Secretary of State, registered agent, contractual notice address. **How-to:** verify via the state's SoS business-entity search; if the state of incorporation is unknown, ask the user. Never invent a registered agent or address.
10. **Represented-party check** — is the recipient known or reasonably believed to be represented by counsel in this matter? If yes, Model Rule 4.2 requires service on counsel (details in `references/ETHICS-AND-PRIVILEGE.md`). If unknown but the recipient is a corporation, make a reasonable inquiry (prior correspondence, public-facing counsel).

**Defaults** (if user says "use defaults" or does not respond): general demand for payment; commercial dispute; FRE 408 header; 30-day response deadline; formal professional tone. Label all defaults explicitly in the draft.

---

## Step 1: Diagnose Legal Function

- Analyze contractual notice requirements — methods, deemed-received provisions, cure periods
- Classify letter type: demand for payment, breach + intent to terminate, anchored settlement invitation, preservation trigger, or statutory prerequisite
- Align with dispute resolution mechanism — do not threaten filing in an improper forum (arbitration clauses govern)

**Statutory pre-suit branch.** If any of these apply, open `references/JURISDICTION-PRESUIT.md` and follow the row for that regime **before continuing to Step 2**:

- TX DTPA § 17.505 (60-day)
- MA Ch. 93A § 9 (30-day)
- CA CLRA § 1782(a) (30-day)
- FL med-mal Ch. 766 (90-day, plus verified expert affidavit)
- Construction defect (CA SB 800 / TX Ch. 27 / FL Ch. 558)
- FDCPA § 1692g
- MMWA reasonable-opportunity-to-cure
- TX Stowers or equivalent policy-limits framework
- Defamation retraction (state-specific)

If the jurisdiction / claim is not in the table, invoke `legal-research` with the query template at the bottom of `JURISDICTION-PRESUIT.md`.

**Exemplar lookup.** Identify the nearest archetype in `references/ARCHETYPE-INDEX.md`. Read the referenced PDF from `assets/examples/` before drafting — this grounds tone, length, and cite density. If no archetype matches, say so explicitly to the user.

**Template branch selection.** Pick one branch in `references/TEMPLATE.md`:
- `statutory-notice` — any statutory-prerequisite letter
- `policy-limits` — insurer-directed bad-faith / Stowers / Holt framework
- `commercial` — breach + cure, C&D, contract-anchored demand for payment

---

## Step 2: Build Element-Driven Fact Narrative

- Chronological structure tied to claim elements
- Source every fact ("On April 18, your project manager wrote…") with an inline exhibit or record citation
- Quote contract terms and correspondence exactly — selective quotation is an attack surface
- No conclusory labels ("fraudulent," "criminal," "willful") without supporting facts for each element of that label
- Adversarial awareness: opposing counsel will mine this for admissions

**Decision rule.** Element-tied granularity = **one source-cited fact per claim element, minimum.** If an element has no factual support, do not plead that cause of action in Step 3 — tell the user what's missing and await instruction. Do not paper over a missing element.

---

## Step 3: Articulate Legal Theories

- State primary claims tied to requested remedy — do not over-plead
- Cite specific statutory sections for UDAP and fee-shifting hooks
- Mark unverified citations: `[VERIFY]`
- Never assert fee recovery without a verified contractual or statutory basis (see `references/ETHICS-AND-PRIVILEGE.md` fee-recovery rule)

**Primary-vs-secondary rule.** Primary claim = the one whose elements are best-supported by §2 facts AND whose remedy matches the client objective from Checkpoint A item 8. Include a secondary claim only if it (a) independently unlocks a remedy the primary does not (fee-shifting, punitive, treble), OR (b) survives a foreseeable defense to the primary. Otherwise omit — over-pleading weakens the letter's credibility as a future exhibit.

**Verification trigger.** Every statutory citation → `legal-research`. Every case citation → `citation-bluebook` for format and good-law status. Unverified → `[VERIFY]` inline.

---

## Step 4: Quantify Damages

Use `references/DAMAGES-METHODOLOGY.md`. Categories covered: Direct/expectation, Consequential, Statutory multipliers, Prejudgment interest, Liquidated, Mitigation offsets, Fees and costs. Cross-cutting rules — including what to do when the client provides a total without line-item backup — are in that file's "Cross-cutting rules" section; follow them.

Address mitigation, offsets, and credits affirmatively when facts suggest the defense is in play. Provide enough detail for credibility without revealing the walkaway number.

---

## Step 5: Include Preservation Notice

Include formal litigation-hold language requiring preservation of all documents and ESI (emails, texts, database records, metadata) and immediate suspension of routine destruction policies. The paragraph template is in `references/TEMPLATE.md` §5.

**Scope rule.** The §5 paragraph is a trigger + catch-all. For matters involving specific high-risk evidence — surveillance footage with short retention, vehicle EDR / black-box data, product exemplars, ESI on custodian-controlled systems, medical devices — invoke the `spoliation-letter` skill to produce a dedicated preservation demand with full itemization and a confirmation deadline. Do not attempt full preservation itemization inside the demand letter.

---

## Step 6: Frame Demands and Proposed Resolution

- Monetary: specify amount, payee, timing, method
- Non-monetary: specify deliverables, acceptance criteria, deadlines

**Term-sheet rule.** Include release-scope, confidentiality, and non-disparagement language **only when the letter explicitly invites settlement** (typically policy-limits and commercial branches). **Omit** from pure statutory-notice letters (Ch. 93A, DTPA, CLRA, FDCPA § 1692g, FL med-mal) — those terms belong in the response-negotiation phase after the recipient responds. Drop-in boilerplate is in `references/TEMPLATE.md` §6.

---

## Step 7: Set Deadline and Consequences

- Use specific calendar dates, not relative periods ("within 10 days" → "by [specific date]")
- Align with contractual cure periods
- State intent to file — specify forum
- Never threaten criminal prosecution as civil leverage (Model Rule 8.4; see forbidden-phrasings list in `references/ETHICS-AND-PRIVILEGE.md`)

**Deadline-length rule.** Default 30 calendar days. Override to the statutory period where applicable (MA 93A: 30; TX DTPA: 60; CLRA: 30; FDCPA § 1692g: 30; FL med-mal: 90). Sub-14-day deadlines only for imminent-harm scenarios (ongoing infringement, spoliation risk, foreclosure sale date) — justify the shorter deadline in the letter text.

**Forum-selection rule.** Contract forum-selection clause controls. Absent a clause, default to a forum with (a) personal jurisdiction over the recipient and (b) venue under 28 U.S.C. § 1391 or the state equivalent. When multiple valid forums exist, match the client's preference from Checkpoint A item 7. If the client has not decided, flag and ask — do not name a forum you have not confirmed.

---

## Step 8: Calibrate Tone and Privilege Posture

- Write as if a judge will read it
- Consider marking "Settlement Communication — Subject to FRE 408 / State Equivalent" per the decision rule in `references/TEMPLATE.md` (optional FRE 408 header) and the reality check in `references/ETHICS-AND-PRIVILEGE.md`
- Exclude defamatory statements, attorney-client communications, and unnecessary personal information

---

## Checkpoint B: Post-Draft Alignment (Mandatory) `[AGENT action]`

After delivering the draft, ask:

1. Does this correctly identify the recipient entity and contractual notice address?
2. Is the damages methodology and total demand within the **authorized range** (Checkpoint A item 8)? **If the demand total exceeds the ceiling, STOP and escalate to attorney. Never send an unauthorized demand number.**
3. Are there statutory pre-suit requirements to verify before sending? (Cross-check `JURISDICTION-PRESUIT.md`.)
4. Should this be sent as a settlement communication (FRE 408) or an unconditional demand?

If the user does not answer, recommend verifying recipient entity and notice method (most common failure point) and proceed only if Checkpoint A item 8 authorized the proposed demand total.

---

## Quality Audit

- [ ] Correct recipient entity name and notice address (Secretary of State verified; source recorded)
- [ ] Contractual notice method satisfied (certified mail, courier, etc.)
- [ ] Cure period aligned with contract terms
- [ ] Every factual assertion sourced or labeled `[UNVERIFIED — client-provided]`
- [ ] Legal citations verified (via `legal-research` / `citation-bluebook`) or marked `[VERIFY]`
- [ ] Damages internally consistent (dates, interest, mitigation)
- [ ] No threats of criminal/regulatory action as civil leverage
- [ ] FRE 408 / settlement posture addressed per the `ETHICS-AND-PRIVILEGE.md` decision rule
- [ ] Preservation notice included; dedicated `spoliation-letter` invoked if high-risk evidence is in play
- [ ] **FDCPA disclosures** included if sender is a "debt collector" under 15 U.S.C. § 1692a(6) AND the communication concerns a "debt" under § 1692a(5). Required verbatim text in `references/ETHICS-AND-PRIVILEGE.md` (§ 1692e(11) mini-Miranda and § 1692g validation notice).
- [ ] Specific calendar deadline
- [ ] Exemplar consulted — name the file from `assets/examples/`, or state no archetype match
- [ ] If represented-party, letter addressed to counsel (Model Rule 4.2)
- [ ] Bar number on signature block
- [ ] Attorney review required before sending — flagged to user

---

## Guidelines

**Jurisdiction-specific requirements.** See `references/JURISDICTION-PRESUIT.md` for MA Ch. 93A, TX DTPA, TX Stowers, CA CLRA, construction defect (CA/TX/FL), FL med-mal, FDCPA, MMWA, and defamation retraction. If your jurisdiction / claim is not there, invoke `legal-research`.

**Ethics and privilege.** See `references/ETHICS-AND-PRIVILEGE.md` for Model Rules 3.1 / 4.1 / 4.2 / 8.4, FRE 408 reality check, FDCPA verbatim disclosures, work-product limits, and forbidden phrasings.

**Damages methodology.** See `references/DAMAGES-METHODOLOGY.md` for category-by-category rules, verification hooks, and presentation choices.

**Letter skeleton and branches.** See `references/TEMPLATE.md` for the fill-in template with statutory-notice / policy-limits / commercial variants.

**Exemplars.** See `references/ARCHETYPE-INDEX.md` for the 14-letter corpus in `assets/examples/`, mapped to archetype with use-when and do-not-copy notes.

**Anti-hallucination.**
- Do not invent statutory citations, case names, or verdict data
- Mark all unverified legal claims with `[VERIFY]`
- Do not assert fee recovery without a verified basis
- No defamatory statements or conclusory labels without factual support
- If a fact or source is uncertain, flag it — do not publish it

**ATTORNEY REVIEW REQUIRED** — No demand letter produced by this skill may be sent without attorney review and approval. The skill drafts; it does not sign, it does not serve.
