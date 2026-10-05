---
name: bc-judicial-review-guide-dmang69
title: BC Judicial Review Guide (RTB / tribunal → BCSC)
description: Use when BC RTB/tribunal JR, Form 66, stay, or ATA s.57/s.58 work is needed. Patent unreasonableness path for RTB.
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/bc-judicial-review-guide
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: administrative
language: en
---

# BC Judicial Review Guide (RTB / tribunal → BCSC)

## Overview

Expert path for **BC Supreme Court judicial review** of Residential Tenancy Branch and similar tribunal decisions. Optimized for self-represented litigants and counsel handling RTB escalations.

**Legal information only — not legal advice.** Verify JRPA, ATA, RTA, Supreme Court Civil Rules, forms, fees, and practice on **BC Laws** and official court sites before filing. Most JR matters: **`[INDEPENDENT COUNSEL RECOMMENDED]`**.

**Hard truth:** Most RTB petitions are dismissed. Courts defer to the tribunal. JR is **not a rehearing**. Fight when grounds are real; do not sell false hope.

## When to Use

- RTB decision (or other BC tribunal with ATA incorporation) heading to BCSC JR
- Stay of order of possession / related interlocutory relief
- Form 66 petition, Form 109 affidavits, Form 32 stay application
- Standard of review selection (ATA s.58 vs correctness carve-outs)
- 60-day clock and service planning

**Prerequisites:** pull substance from `bc-tenancy-substantive` and process/record from `bc-tenancy-procedure`. Drafting standards from `supreme-court-civil-counsel`.

## Locked corrections (// product law)

1. Consent ≠ privilege.  
2. Consent withdrawal ≠ unconditional deletion (PIPA).  
3. **Form 66** commences the petition; **Form 67** is the response; interlocutory ≈ **Form 32** / response **Form 33**; affidavits **Form 109**.  
4. Ordinary JR time limit for ATA s.57 tribunals: **60 days from issuance of the final decision** (s.57(1)); extension criteria in **s.57(2)**. Uncertain finality/date/Act/review → **alternatives**, not one confident date.  
5. Honest encryption claims only.  
6. RTB published archive ≠ complete corpus; absence ≠ non-existence.

## Skill tree (modules)

| # | Module |
|---|--------|
| 1 | Standard of review — **ATA s.58** (not default Vavilov for RTB) |
| 2 | Jurisdiction — RTA s.84.1 exclusive jurisdiction |
| 3 | Grounds that survive vs rarely succeed |
| 4 | **60-day clock** — ATA s.57 + Form 66 filing |
| 5 | Petition drafting — Form 66 |
| 6 | Affidavits — Form 109 + exhibits |
| 7 | RTB record acquisition |
| 8 | Stay applications — RJR-MacDonald three-part test |
| 9 | Associate Judge vs Judge |
| 10 | Procedural fairness — correctness / Baker |
| 11 | Oral argument structure |
| 12 | Ethics, odds, procedural glitch hunt |
| 13 | Reconsideration / set-aside of interlocutory orders |
| 14 | Service (Rule 4-7 et seq.) |

---

## Module 1 — Standard of review (core)

### ATA governs RTB (do not default to Vavilov)

Where the enabling scheme incorporates **ATA s.58** and a privative clause exists, the ordinary standard for questions of fact, law, and mixed fact and law inside expertise is:

**Patent unreasonableness** — ATA s.58(2)(a) (verify current text).

**Correctness** — ATA s.58(2)(b) and common law carve-outs for:

- questions of central importance to the legal system as a whole outside expertise  
- true jurisdiction / vires (careful with modern caselaw — verify)  
- **procedural fairness** (correctness; court decides afresh)

| Question type | Working standard | Court posture |
|---------------|------------------|---------------|
| Findings of fact | Patent unreasonableness | Defer unless no rational basis in evidence |
| RTA applied to facts | Patent unreasonableness | Defer unless clearly irrational |
| Pure law of central importance | Correctness | Fresh look |
| Procedural fairness | Correctness | Fresh look |
| True jurisdiction / ultra vires | Correctness (verify framing) | Fresh look |

**Patent unreasonableness is not** “I disagree,” “mistaken,” or “another interpretation is better.”  
**It is** “no rational person applying the RTA could reach this result on this evidence” / clearly irrational.

**Vavilov** remains important comparative admin doctrine and may inform defining reasonableness/patent unreasonableness language — but **do not mislabel the RTB statutory standard as reasonableness under Vavilov without checking ATA incorporation.**

---

## Module 2 — Jurisdiction (RTA s.84.1)

RTB exclusive jurisdiction over RTA disputes (verify **s.84.1** current text). Court generally:

- does **not** redecide the tenancy merits as first-instance decision-maker  
- may **quash / remit**, declare, stay ancillary orders  

### Intervene when

- patent unreasonableness on the record  
- jurisdictional excess  
- procedural fairness denied  
- wrong legal test applied entirely  

---

## Module 3 — Grounds identification

### Stronger traction

**Procedural fairness (correctness):** inadequate notice; no meaningful response opportunity; reliance on evidence not put to the party; bias/prejudgment; decision without presence and without proper process; reasons so inadequate decision cannot be understood.

**Patent unreasonableness:** relevant evidence ignored; finding contradicted by uncontested evidence; wrong RTA section applied; internal contradiction with no rational reconciling path.

**Jurisdiction:** matter outside RTA; fettering; refusal to consider evidence on wrong procedural basis.

**Res judicata / issue estoppel** mishandled.

### Rarely succeed alone

- pure credibility preference for the other side  
- “harsh but authorized” outcomes  
- “new evidence” not properly before RTB / not fitting JR new-evidence exceptions  

---

## Module 4 — The 60-day clock ★

### Ordinary rule (ATA s.57 when incorporated)

An application for judicial review of a **final decision** of the tribunal must be commenced within **60 days of the date the decision is issued** (ATA s.57(1) — verify).

Working product lock: **clock runs from issuance of the final decision**, not casual “when I felt like I understood it.” Deemed-service rules for RTB notices do **not** rewrite an issuance-based JR clock.

### What must happen in time

1. **File Form 66** petition at BC Supreme Court registry (stamped)  
2. Filing fee or fee waiver path  
3. Serve respondents (service may trail filing but do not sleep)

### Extension — ATA s.57(2)

Court **may** extend if statutory criteria are met (serious grounds for relief; reasonable explanation for delay; no substantial prejudice/hardship to persons affected — **paraphrase only; verify current ATA text**). Not automatic. Do not plan to live on an extension.

### Alternatives engine (mandatory when uncertain)

When any of the following is uncertain, **do not** report one filing-safe date:

- issuance date unknown / competing documents  
- finality unknown (interim vs final; review/correction/clarification pending)  
- enabling Act’s ATA s.57 incorporation unknown  
- internal RTB review may change which decision is “final”

Always:

1. Compute candidates from **each plausible issuance date**  
2. Apply **earliest-candidate** filing discipline while investigating later candidates  
3. Preserve parallel calendars if post-review finality is argued  
4. Require **HITL** confirmation before any “you must file by X” is treated as filing advice  

### Who is typically named / served (verify practice)

- Director, Residential Tenancy Branch (tribunal)  
- Attorney General of British Columbia (statutory decision context)  
- Opposing tenancy party (landlord/tenant)

Addresses and current service preferences: **verify** government/court directories before use; do not rely on stale PO boxes from memory.

---

## Module 5 — Petition drafting (Form 66)

**Form 66** — Petition (under Supreme Court Civil Rules / JRPA). Pull current PDF from official court forms site.

### Working skeleton

1. **Parties** — Petitioner; Respondents (Director RTB; AG; other party)  
2. **Decision under review** — maker, date of issuance, type, RTB file #  
3. **Legal basis** — JRPA + ATA (as applicable) + RTA privative/review scheme  
4. **Grounds** — one numbered ground per paragraph: rule violated → what arbitrator did/failed → record pin  
5. **Relief** — e.g. quash (certiorari); remit; interim stay of possession order; costs; further relief  
6. **Material facts** — numbered, chronological, each tied to affidavit exhibit  
7. **Optional short legal argument** — often fuller argument reserved for hearing brief  

### Drafting rules

- One ground per paragraph  
- Cite the record: “(see Exhibit C, decision at para. 12)”  
- Precise statutes: ATA s.58 / s.57, JRPA provisions, specific RTA sections (BC Laws)  
- No emotional advocacy colour for pure narrative facts  
- No new evidence as if it were RTB record  

---

## Module 6 — Affidavits (Form 109)

- Personal knowledge baseline; information and belief only where permitted and sourced  
- Exhibit letters A, B, C… with commissioner exhibit markings  
- Typical core exhibits: decision first; notices; RTB packages; service proof; FOI/record extracts  
- **Not** for pure legal argument or inadmissible new-case theory dressed as fact  

---

## Module 7 — Record acquisition

Court reviews the **record**, not recollection.

- FOI / FIPPA request for RTB file (hearing materials, recording/transcript if any)  
- Court order path if production deficient (JRPA powers — verify)  
- Hunt: ignored evidence, mismatched reasons vs hearing, excluded evidence, credibility comments  

---

## Module 8 — Stays (halt eviction)

Ancillary to the petition. Interlocutory application envelope: generally **Form 32** (app); **Form 33** (response).

### RJR-MacDonald three-part test

*[RJR-MacDonald Inc. v. Canada (Attorney General)]*, [1994] 1 S.C.R. 311 (verify CanLII):

1. **Serious question** — non-frivolous JR ground (low merits threshold at stay stage)  
2. **Irreparable harm** — harm not compensable in damages; loss of home often central — must be **evidence-based**  
3. **Balance of convenience** — housing insecurity vs property interest; record the evidence  

Urgent / without-notice stays: exceptional; full candour; undertake prompt service; expect set-aside motion.

Set-aside response checklist: Form 33 + Form 109 + three-part test + exhibits; comply with Rule 8-1 time/service minima (**verify current Rules**).

---

## Module 9 — Associate Judge vs Judge

| Associate Judge (working) | Judge |
|---------------------------|-------|
| Interlocutory stays, procedural applications | Final determination of JR petition |
| Many Rule 8-1 manners of application | Injunctions / higher final remedies as Rules provide |

Verify post-2022 jurisdiction notes before asserting hard boundaries in a filing.

---

## Module 10 — Procedural fairness (correctness)

**Baker** factors (*[Baker v. Canada (Minister of Citizenship and Immigration)]*, [1999] 2 S.C.R. 817 — verify): nature of decision; statutory scheme; importance to individual (eviction = high); legitimate expectations; tribunal’s chosen procedure.

Checklist: notice · opportunity to respond · consideration of evidence/submissions · impartiality / RAP bias · adherence to ordered procedure · adequate reasons · no secret evidence.

Bias: reasonable informed person, realistic possibility of bias (prejudgment; interest; prior involvement; demonstrated hostility/favoritism).

---

## Module 11 — Oral argument spine

1. Overview (issue + strongest ground + remedy)  
2. Standard of review map (fairness = correctness; fact/law mix often patent unreasonableness)  
3. Grounds with record pins  
4. Precise remedy (quash + remit usual when facts remain)  
5. Pre-butt deference: expertise does not authorize ignoring uncontested evidence or skipping fairness  

---

## Module 12 — Ethics & strategy

- Honest odds: patent unreasonableness is a **high** bar  
- Flat/scoped JR work is common; put odds in writing for SRL  
- Procedural glitch hunt: clock trigger date; original hearing notice validity; form/authority used; expansion beyond notice; representative authorization; internal review pathway  
- Advise **against** filing when only weak credibility grounds or non-patent disagreement exists  

---

## Module 13 — Reconsideration / set-aside (interlocutory)

Rule 8-1 paths for material change, new evidence, without-notice orders, fairness defects in interlocutory hearing — **verify current Rules**.

---

## Module 14 — Service

- Personal / alternative / email on **written consent** (Rule 4-7 framework — verify)  
- Irregular service may sometimes be cured if actual notice / Rules allow — do not plan around curing  
- Parties: tribunal, AG when required, opposing party  

---

## Prerequisites handoff (from RTB)

1. Full tribunal record (decision, evidence, notes/recording if available)  
2. Grounds matrix  
3. Complete procedural timeline  
4. Evidence ignored / mischaracterized list  
5. Internal review / clarification outcome and how it affects **finality** for s.57  

## Output structure for JR memo

`PROCEDURAL HISTORY` · issuance/finality/clock candidates · `LAW` (s.58 map) · `ARGUMENT` (grounds) · record pins · counterarguments · `REMEDY` · `ASSUMPTIONS` · `RECOMMENDATION` · counsel flag · disclaimer  

## Combine with

- `supreme-court-civil-counsel` — analytical tags & quality gates  
- `bc-tenancy-substantive` / `bc-tenancy-procedure`  
- `canlii-boa-builder`  
- `administrative-law-canada` · `evidence-law-canada`  

## Common pitfalls

1. Form **67** used as originating petition  
2. Vavilov **reasonableness** labeled as RTB’s statutory default without ATA s.58 check  
3. Single confident JR deadline despite pending review or unknown issuance  
4. Treating JR as a new trial / dumping new evidence casually  
5. Arguing only “arbitrator believed them”  
6. Stale service addresses from training memory  
7. Archive absence as proof no prior decision exists  

## Verification checklist

- [ ] Form 66 petition draft; not Form 67 as origin  
- [ ] ATA s.58 standard map correct for each ground  
- [ ] 60-day candidates + alternatives if uncertain  
- [ ] s.57(2) not treated as automatic  
- [ ] Stay uses RJR three-part test with evidence  
- [ ] Affidavit Form 109 + exhibit discipline  
- [ ] Respondents / AG issues flagged for verification  
- [ ] Every FACT pinned to record  
- [ ] `[INDEPENDENT COUNSEL RECOMMENDED]` if eviction/clock/complexity  
- [ ] Disclaimer present  
