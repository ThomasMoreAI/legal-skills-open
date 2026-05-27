---
name: pet-custody-best-interest
title: Pet Custody Best Interest Analysis
description: Produces a jurisdiction-aware best-interests analysis for companion animal disputes in domestic dissolutions. Classifies the governing framework (well-being statute, hybrid equitable, or pure property), builds distinct ownership/caregiving/control evidentiary threads, applies welfare factors with adversarial awareness, and generates enforceable allocation recommendations. Use when drafting pet custody analyses, animal allocation memos, pet possession briefs, or when a user asks about dividing pets in a divorce, breakup, or cohabitation dissolution.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/pet-custody-best-interest
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
tags: [analysis, drafting, litigation, memo]
---

# Pet Custody Best Interest Analysis

Companion animal statutes vary sharply: CA, IL, NY, and AK have genuine best-interest standards while most jurisdictions treat pets as personal property. Applying the wrong framework — or importing child custody language into a property-only forum — undermines court credibility. This skill maps the correct legal standard, separates ownership from caregiving from de facto control, and produces a factor-by-factor analysis that anticipates adversarial attacks.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft."

1. **Forum** — state, court level, proceeding type (divorce, domestic partnership dissolution, cohabitation breakup, civil dispute)
2. **Procedural posture** — temporary relief vs. final allocation; deadlines
3. **Case documents** — petition, responses, temporary orders, property schedules listing pet, mediation statements
4. **Ownership records** — adoption/purchase agreements, microchip, municipal license, breeder contract
5. **Veterinary records** — full history (minimum 3 years); note who attended appointments
6. **Financial records** — food, grooming, insurance, emergency care, boarding payments; whose name on accounts
7. **Caretaking evidence** — routine logs, calendar entries, texts on pet-care duties, pet-sitting app records
8. **Living environment** — current/proposed residences, lease/HOA pet policies, proximity to parks/vet, daily schedule, travel frequency
9. **Bond evidence** — third-party affidavits (neighbors, trainers, groomers), timestamped photos/videos, behavioral observations
10. **Pet profile** — age, breed, temperament, medical conditions, training level, anxiety triggers
11. **Safety concerns** — neglect/abuse allegations, DV, threats involving pet, interference with access

**Defaults if no response:** well-being statute analysis if jurisdiction has one, otherwise hybrid equitable; attorney work product audience; final allocation posture. Mark assumed facts `[ASSUMED]`.

---

## Step 1: Determine Governing Legal Standard

Classify the forum into one of three modes:

| Mode | Frame | Key Evidence |
|---|---|---|
| **Well-being statute** | Animal welfare factors control | Caregiving, stability, attachment, medical management |
| **Hybrid equitable** | Property with equitable discretion | Ownership + welfare as equitable considerations |
| **Pure property** | Ownership and equitable distribution | Title, purchase, registration, financial contribution |

**Key statutes** (all `[VERIFY]` for current amendments):

| Jurisdiction | Statute | Standard |
|---|---|---|
| California | Fam. Code § 2605 | Sole/joint ownership considering care of pet |
| Illinois | 750 ILCS 5/503(n) | Well-being of companion animal |
| New York | DRL § 236(B)(5)(d)(15) | Best interest of companion animal |
| Alaska | AS 25.24.160(a)(5) | Well-being of the animal |

- **Property-only jurisdictions** (e.g., TX, FL): use "allocation," "possession," or "award" — never "custody." Frame welfare facts as evidence of intrinsic value to the possessor.
- Do not assume availability of pet visitation, pet support, or enforcement mechanisms without verified authority.

---

## Step 2: Build the Fact Record

Produce three distinct evidentiary threads — never conflate them:

| Thread | Definition | Key Evidence |
|---|---|---|
| **Legal ownership** | Contractual title and registration | Adoption/purchase docs, microchip, license |
| **Primary caregiving** | Daily non-discretionary care and medical decision-making | Vet records, pharmacy receipts, feeding/walking logs, training records |
| **De facto control** | Post-separation possession and stability | Timeline since separation, interference allegations |

Construct a chronological timeline: acquisition → separation → present. Flag gaps and propose targeted discovery (subpoenas, declarations, interrogatories).

---

## Step 3: Apply Best-Interests Factors

Analyze each factor with neutral, court-ready language. Avoid anthropomorphism. Tie every assertion to evidence. For each factor, include an **adversarial awareness** note identifying how opposing counsel will attack and how to preempt.

**Factor 1: Primary Caregiver History & Continuity**
- Distinguish burdensome care (medication, emergencies, chronic conditions) from recreational interaction (play, social media)
- Show pre-separation pattern to preempt "wrongful withholding" arguments
- Do not stereotype by gender; account for delegated care

**Factor 2: Financial Capacity & Willingness**
- Compile historical spending by each party with receipts; project foreseeable costs
- Not a wealth test — focus on demonstrated willingness and practical capacity
- Court-ordered pet support authority must be `[VERIFY]`'d

**Factor 3: Living Environment & Logistics**
- Compare: housing type, yard/park access, vet proximity, pet policy, other animals/children, schedule, travel frequency
- Assess housing certainty (executed lease vs. contingent plans); match to pet's specific needs
- Temporary orders: emphasize present stability. Final orders: account for longer-term plans.

**Factor 4: Emotional Bond & Attachment**
- Observable behavioral indicators only: proximity-seeking, separation anxiety, training responsiveness, daycare/boarding notes
- Rely on third-party records and long-term patterns over staged demonstrations
- In property-only jurisdictions: bond arguments support equitable settlement but carry less judicial weight

**Factor 5: Safety & Welfare Concerns**
- Document harm allegations, threats involving pet, coercive control using pet
- Address exchange logistics if protective orders exist (neutral sites, third-party intermediaries)
- Never disclose confidential location information

**Factor 6: Willingness to Facilitate Contact**
- Assess which party is more likely to honor a shared schedule
- Do not import child custody terminology unless the jurisdiction explicitly supports it for animals

---

## Step 4: Recommendation

Propose one primary recommendation and at least one fallback, each tied to the factor analysis.

**Primary possession elements:**
- Who retains possession; transfer logistics and timeline
- Document updates (microchip, license, vet authorized-agent forms) with deadline
- Structured contact terms for the other party, if any
- Conditions: non-interference, compliance with medical regimen

**Shared schedule elements** (if parties insist):
- Minimize transitions for anxious animals; neutral exchange site
- Holiday/travel rules; right of first refusal for boarding
- Medical decision-making protocol (routine vs. emergency); cost-sharing formula
- End-of-life care protocol; dispute resolution mechanism
- Self-executing default if schedule breaks down

**Strategic note:** In high-conflict cases, recommend sole ownership with defined contact over joint ownership. Joint arrangements invite continued litigation; police typically will not enforce pet visitation orders `[VERIFY for jurisdiction]`.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

1. Does this correctly identify the governing legal standard for your jurisdiction?
2. Are there caregiving or ownership records not yet provided that could change the analysis?
3. Should I develop any factor in greater depth or compare across jurisdictions?
4. Is the recommendation posture correct (sole allocation vs. shared schedule)?

---

## Quality Audit

- [ ] Governing legal standard correctly identified and verified
- [ ] Three evidentiary threads kept distinct (ownership, caregiving, de facto control)
- [ ] Every material assertion tied to source or marked `[ASSUMED]`
- [ ] All six factors analyzed with evidence citations
- [ ] Adversarial awareness note present for each factor
- [ ] No child custody terminology without verified jurisdictional authority
- [ ] Citations verified or marked `[VERIFY]`
- [ ] Recommendation tied to factor analysis with fallback
- [ ] Pet's specific needs addressed in environment analysis
- [ ] Safety concerns addressed with confidentiality protections
- [ ] Property-only jurisdictions use correct terminology (allocation/possession, not custody)

---

## Guidelines

- **Jurisdiction first** — never proceed without confirming the forum
- **Verify all citations** — use web search or mark `[VERIFY]`; citation hallucination is the primary risk
- **Evidence-anchored** — every assertion needs a source ("vet record dated…," "receipt from…")
- **Flag gaps** — propose how to fill (subpoena, declaration, discovery)
- **Acknowledge weaknesses** — if opposing party's name is on the adoption contract, address and explain why other factors outweigh
- **Consistency check** — ensure caretaking claims align with employment schedules and lifestyle evidence
- **No child custody importation** — unless the jurisdiction explicitly authorizes it for animals
- **Professional responsibility** — ABA Model Rules 1.1, 1.6, 3.3, 4.1 apply; label contested assertions "alleged," "disputed," or "reported"
- **Confidentiality** — assume all client facts are confidential; flag before any external sharing
- **Conflict check** — remind attorney-user to confirm no conflicts under Rule 1.7

**Required disclaimer on every output:**

> This is attorney work product support, requires attorney review before use, and does not constitute legal advice. All citations must be independently verified.

---

## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Analysis uses "custody" in property-only jurisdiction | Wrong legal mode applied | Re-classify forum per Step 1; use "allocation" or "possession" |
| Opposing counsel attacks caregiving claims | Caretaking evidence conflicts with work schedule | Run consistency check; reconcile with delegated care or shift patterns |
| Court rejects visitation/support request | No verified authority for pet visitation in jurisdiction | Reframe as property access terms in settlement; verify enforcement mechanisms |
| Evidentiary threads blurred | Ownership conflated with caregiving | Rebuild fact record per Step 2 with strict thread separation |
| Citation flagged as non-existent | Hallucinated statutory reference | Replace with verified cite or mark `[VERIFY]`; never present unverified cites as authoritative |

---

**Key changes from the original:**

- **198 → 163 lines** (~18% reduction). Removed the verbose "Why This Skill Exists" section and replaced with a 2-sentence overview. Compressed factor sub-bullets from 4-5 to 3 each. Consolidated recommendation template lists. Removed the `transactional` tag (not applicable to dissolution litigation).
- **Added Troubleshooting section** (required by SKILL-SPEC.md but missing from original).
- **Tightened frontmatter description** — shorter while keeping all trigger keywords.
- **Quality Audit uses checkboxes** for scanability, matching the advance-directive pattern.
- All legal substance, factor structure, adversarial awareness, and citation verification requirements preserved intact.
