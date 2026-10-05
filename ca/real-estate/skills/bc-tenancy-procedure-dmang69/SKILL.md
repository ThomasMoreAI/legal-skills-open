---
name: bc-tenancy-procedure-dmang69
title: BC Tenancy Procedure — RTB Runtime Environment
description: 'BC RTB procedure runtime: evidence packaging, witness prep, applications, negotiation, hearing strategy, document drafting, enforcement/collections. Use for RTB filing, hearings, settlements, and post-order enforcement. Pair with bc-tenancy-substantive for RTA law and bc-tenancy-advocacy (advanced) for JR, human rights, strata, MHPTA. Legal information only — not legal advice.'
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/bc-tenancy-procedure
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: real-estate
language: en
sources:
- title: Deposit Rules
  path: references/deposit-rules.md
- title: Evidence Packaging Guide
  path: references/evidence-packaging-guide.md
- title: Rtb Hearing Procedure
  path: references/rtb-hearing-procedure.md
- title: Settlement Tactics
  path: references/settlement-tactics.md
- title: Witness Prep Guide
  path: references/witness-prep-guide.md
---

# BC Tenancy Procedure — RTB Runtime Environment

> **Disclaimer:** Legal information only. Verify at [gov.bc.ca/rtb](https://www2.gov.bc.ca/gov/content/housing-tenancy/residential-tenancies) and [bclaws.gov.bc.ca](https://www.bclaws.gov.bc.ca).  
> Form numbers, fees, deadlines, and section cites: **`[VERIFY]`** against current RTB materials before filing.  
> Not legal advice. Self-represented parties: evidence deadlines are hard.

## Skill routing

| Need | Skill |
|------|--------|
| Substantive RTA (sections, bad-faith, eviction defence, illegal charges, deposits) | `bc-tenancy-substantive` (deep Modules 1–7) |
| JR, human rights, strata, MHPTA, trauma-informed, ethics | `bc-tenancy-advocacy` (alias: `bc-tenancy-advanced`) |
| Court drafting / JR petition standard | `supreme-court-civil-counsel` + `bc-judicial-review-guide` |

## Analytical tags

`[FACT]` · `[ALLEGATION]` · `[LAW]` · `[ARGUMENT]` · `[INFERENCE]` · `[ASSUMPTION]` · `[PROCEDURAL HISTORY]` · `[RECOMMENDATION]` · `[REMEDY]`

---

## Module 1: Evidence Packaging ⭐ — Turning Drama Into Proof

**Core skill:** Convert chaotic “he said / she said” into a package an arbitrator can follow in ~30 minutes and resolve in your favour.

### Evidence assessment (no fixed hierarchy)

RTA **s. 75** provides that formal rules of evidence do not apply to RTB dispute-resolution proceedings. Admissibility, reliability, relevance, authenticity, completeness, procedural fairness, and weight remain distinct questions. No evidence type is automatically stronger merely because it appears in a ranked list.

Assess each item for:

- source and personal knowledge;
- creation date and whether it is contemporaneous;
- authenticity, completeness, and metadata;
- relevance to a disputed statutory element;
- corroboration or contradiction;
- hearsay level and ability to test the account;
- service/disclosure compliance and opportunity to respond;
- privacy, privilege, redaction, and necessity.

Anchor material claims to precise exhibit/page/timestamp references. Undated evidence is not automatically excluded, but missing date or provenance can reduce reliability and weight.  

### Evidence bundle structure

| Tab | Contents |
|-----|----------|
| **TAB 1** | Tenancy Agreement (signed original) |
| **TAB 2** | Condition Inspection Reports (move-in + move-out) |
| **TAB 3** | Payment Records (receipts, e-transfer history, bank statements) |
| **TAB 4** | Correspondence Chronology (all texts + emails, oldest → newest, timestamped) |
| **TAB 5** | Photos/Videos (dated, labelled by defect or issue) |
| **TAB 6** | Repair Requests and Responses (with delivery confirmation) |
| **TAB 7** | All Notices (with service evidence) |
| **TAB 8** | Third-Party Records (inspector, city, medical, bylaw) |
| **TAB 9** | RTB Decisions / Precedents (CanLII — verified only) |
| **TAB 10** | RTA sections + Policy Guidelines (relevant passages highlighted) |

### Exhibit labelling protocol

- Every document: letter label (**A, B, C…**) referenced in affidavit/submissions.  
- Each photo: label + date + description.  
- Example: *Exhibit F — Mold on bathroom ceiling, photographed [date], [address]*

### Building the timeline

```
[Date] — [Event] — (Exhibit reference)
[Date] — [Event] — (Exhibit reference)
```

Makes patterns (retaliation timing, notice defects, payment history) visually obvious.

### Admin law principles to deploy (hearing or post-decision)

| Principle | Question |
|-----------|----------|
| Natural justice / procedural fairness | Notice + meaningful opportunity to respond? |
| Reasonableness | Decision rationally connected to evidence and RTA? |
| Fettering of discretion | Rigid policy without facts? |
| Adequacy of reasons | Can you follow evidence → conclusion? |
| Jurisdiction | Outside arbitrator authority? |

Any failure → RTB internal review (**often discussed as s. 79 — `[VERIFY]`**) or judicial review → `bc-judicial-review-guide`.

→ `references/evidence-packaging-guide.md`

---

## Module 2: Witness Prep

### Interviewing clients and witnesses

1. **Open first:** “Tell me what happened in your own words.”  
2. **Then narrow:** “What date? Do you have anything in writing?”  
3. **Document everything** — written summary they confirm.  
4. Separate **direct knowledge** vs **secondhand (hearsay)**.  

### Core testimony rules

- Answer only the question asked — don’t volunteer.  
- “I don’t recall” is better than a wrong answer.  
- Stick to what you personally saw, heard, or did.  
- Stay calm and professional — arbitrators notice rattling.  
- Pause before answering — taking a moment is fine.  

### Anticipating landlord counters

| Likely landlord argument | Rebuttal + evidence |
|--------------------------|---------------------|
| “Tenant caused the damage” | Condition inspection shows pre-existing |
| “Rent was not paid” | E-transfer records + bank statements |
| “Notice was properly served” | Address discrepancy / service method defect |
| “The charge is legitimate” | Classify the amount; test the agreement under RTA s. 5 and the specific governing Act/regulation provision—never current s. 8 |
| “Tenant violated the rules” | No written warning; first offence; remediated |
| “Genuine renovation” | No permits; unit re-listed immediately after |

→ `references/witness-prep-guide.md`

---

## Module 3: RTB Applications & Process

| Item | Working detail | Status |
|------|----------------|--------|
| Tenant form | Often **RTB-12** (or current tenant application form) | **`[VERIFY form number]`** |
| Landlord form | Often **RTB-12L** / landlord equivalent | **`[VERIFY]`** |
| Fee | Often ~$100 | **`[VERIFY current fee]`** |
| Fee waiver | Financial hardship form (e.g. RTB-FF) | **`[VERIFY form code]`** |
| Where | Online RTB portal, mail, Service BC | Confirm current channels |

### Application checklist

- [ ] Exact legal names from tenancy agreement  
- [ ] Full unit address with designation (not just civic address)  
- [ ] One issue per numbered paragraph  
- [ ] Specific dollar amounts for monetary claims  
- [ ] RTA section cited for each claim  
- [ ] Evidence submitted by deadline (commonly discussed as **14 days before hearing** — **`[VERIFY]`**)  
- [ ] Witnesses identified  

Evidence deadlines are important. Late material may be excluded, adjourned, or otherwise addressed under the current RTB Rules and procedural-fairness requirements. Verify the current rule, calculation method, service requirements, and any available exception or direction; do not state that there are “no exceptions.”

### Hearing types

| Type | When used |
|------|-----------|
| Participatory (phone/video/in-person) | Most eviction and monetary cases |
| Written submissions | Smaller monetary claims; on consent |
| Direct Request | Uncontested — no response filed; certain deposit claims |

**Direct Request tip:** If the other side does not file a Response, Direct Request may allow decision on your written materials alone — powerful when they ghost. Confirm current eligibility.

→ `references/rtb-hearing-procedure.md`

---

## Module 4: Negotiation & Settlement — The Leverage Map

Mediate with a clear leverage map **before** the hearing.

### When to settle vs fight

| Settle when… | Fight when… |
|--------------|-------------|
| Certainty > risk | Strong case |
| Ongoing tenancy relationship | Other side stalling |
| Other side has genuine defence | Conduct warrants public order / paper trail for JR |

### Leverage map

| Your leverage | Their exposure |
|---------------|----------------|
| RTB filing imminent | Cost, delay, permanent RTB record |
| Airtight evidence package | No selective disclosure at hearing |
| Retaliation claim in play | Enhanced damages risk |
| Illegal charge documented | Void + repayment + penalty |
| Procedural defect in notice | Notice potentially void |
| Bad-faith renoviction | Significant compensation exposure (confirm current RTA) |
| *Res judicata* from prior RTB | Prior loss on same facts is often fatal |

### Damage calculation worksheet

```
Unpaid repairs compensation:      $___
Rent reduction (retroactive):     $___ × ___ months = $___
Deposit + interest:               $___
Double-deposit type penalty:      $___   [VERIFY current section e.g. s.38(6)]
Moving expenses (if applicable):  $___
Illegal charges repayment:        $___
──────────────────────────────────────
TOTAL LANDLORD EXPOSURE:          $___
```

**Rent abatement / compensation:** Do not use preset percentage bands as a legal rule or settlement valuation. Build the amount from duration, severity, affected space/service, rent, notice, response, mitigation, causation, comparable verified decisions (if any), and proof of actual loss. Explain any methodology and present alternatives where valuation is uncertain.

### Settlement offer structure

1. Specific relief (dollars + required action)  
2. Clear acceptance deadline (7–14 days typical)  
3. Consequences of non-acceptance (hearing, costs, order on record)  
4. **In writing** — good-faith evidence  
5. Does not waive unaddressed rights  

→ `templates/settlement-offer-letter.md` · `references/settlement-tactics.md`

---

## Module 5: Hearing Strategy

### IRAC for every issue

```
ISSUE:       The specific legal dispute
RULE:        RTA section / Policy Guideline / verified precedent
APPLICATION: Rule applied to exact facts (dates, amounts, names, exhibit tabs)
CONCLUSION:  Specific order requested
```

### Opening statement (template)

> “My name is [Name]. I am the [tenant/landlord] at [unit] since [date]. I am asking for [specific relief] because [grounds in one sentence]. I have [X] evidence tabs and [X] witnesses. I estimate [X] minutes.”

### Cross-examination principles

- Only ask questions you know the answer to  
- One fact per question — never compound  
- Impeach with documents: “You wrote on [date]… is that your message?”  
- Do not argue with the witness — argue in submissions  
- Let silence after a damaging answer land  

### Closing submissions

1. Facts proved (each tied to a specific exhibit tab)  
2. Law that applies (RTA section + PG cited)  
3. Why the other side’s evidence fails (hearsay, inconsistency, no corroboration)  
4. Precise order requested (amounts, dates, conditions)  

---

## Module 6: Document Drafting

**Standards:** Professional plain language · Precise dates and amounts · RTA section for every legal claim · Numbered paragraphs · Explicit relief · Dated and signed.

### Templates

| Document | Template |
|----------|----------|
| Demand Letter — Repairs | `templates/demand-letter-repairs.md` |
| Demand Letter — Illegal Charges | `templates/demand-letter-illegal-charges.md` |
| Demand Letter — Deposit Return | `templates/demand-letter-deposit.md` |
| Settlement Offer Letter | `templates/settlement-offer-letter.md` |
| RTB Application (Tenant) | `templates/rtb-application-tenant.md` |
| RTB Application (Landlord) | `templates/rtb-application-landlord.md` |
| Dispute Response (Tenant) | `templates/dispute-response-tenant.md` |
| Hearing Submissions | `templates/hearing-submissions.md` |
| Affidavit of Evidence | `templates/affidavit-rtb.md` |
| Notice of Rent Withholding | `templates/rent-withholding-notice.md` |
| Condition Inspection Record | `templates/condition-inspection.md` |
| Witness Statement | `templates/witness-statement.md` |
| Evidence Timeline | `templates/evidence-timeline.md` |

**Caution on rent withholding:** High-risk strategy — confirm current RTA and Policy Guidelines before advising; often **`[INDEPENDENT COUNSEL RECOMMENDED]`**.

---

## Module 7: Enforcement & Collections

An RTB monetary order is generally enforceable as a court order once filed correctly. A paper win is worthless if they ghost.

| Amount | Typical enforcement venue |
|--------|---------------------------|
| ≤ $35,000 (confirm current small claims limit) | BC Provincial Court (Small Claims) — **`[VERIFY limit]`** |
| Above that limit | BC Supreme Court |

### Enforcement mechanisms (civil)

- Wage garnishment (serve employer)  
- Bank account seizure (serve financial institution)  
- Certificate of Judgment (credit / property effects)  
- Writ of Seizure (Sheriff — personal property)  
- Lien / registration against land title if landlord owns real property  

### Steps

1. Obtain **certified** RTB order  
2. File at appropriate court  
3. Asset search (land title, PPSA, skip-trace if needed)  
4. Serve enforcement documents  
5. Return to court if assets hidden  

→ Confirm current Small Claims / Supreme Court enforcement practice guides.

---

## Reference files

- [references/rtb-hearing-procedure.md](references/rtb-hearing-procedure.md)  
- [references/deposit-rules.md](references/deposit-rules.md)  
- [references/evidence-packaging-guide.md](references/evidence-packaging-guide.md)  
- [references/witness-prep-guide.md](references/witness-prep-guide.md)  
- [references/settlement-tactics.md](references/settlement-tactics.md)  

## Workflow (every RTB file)

1. Stabilize deadline (hearing / possession / response date).  
2. Build **timeline** + **10-tab evidence bundle**.  
3. Draft application / response with RTA sections.  
4. Map leverage → negotiate or fight.  
5. IRAC + opening/closing for hearing.  
6. Enforce monetary order if needed.  
7. If decision defective → review / JR handoff package.  
