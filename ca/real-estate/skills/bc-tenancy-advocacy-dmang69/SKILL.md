---
name: bc-tenancy-advocacy-dmang69
title: BC Tenancy Advocacy — Advanced Modules
description: 'BC tenancy advocacy advanced modules: judicial review escalation, human rights overlaps (BCHRT), strata/condo rentals, MHPTA manufactured home parks, client-centered trauma-informed advocacy, Law Society ethics, and advanced (Level 99) practice moves. Use with bc-tenancy-substantive, bc-tenancy-procedure, bc-judicial-review-guide, and supreme-court-civil-counsel. Legal information only — not legal advice. SRL-friendly.'
author: dmang69
author_url: https://github.com/dmang69/bc-legal-ai/tree/master/skills/bc-tenancy-advocacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ca
practice: real-estate
language: en
sources:
- title: Human Rights Tenancy
  path: references/human-rights-tenancy.md
- title: Mhpta Guide
  path: references/mhpta-guide.md
- title: Policy Guidelines Summary
  path: references/policy-guidelines-summary.md
- title: Strata Rental Conflicts
  path: references/strata-rental-conflicts.md
- title: Trac Clas Resources
  path: references/trac-clas-resources.md
---

# BC Tenancy Advocacy — Advanced Modules

> **Disclaimer:** Legal information only. Verify at [bclaws.gov.bc.ca](https://www.bclaws.gov.bc.ca), [gov.bc.ca/rtb](https://www2.gov.bc.ca/gov/content/housing-tenancy/residential-tenancies), and [bchrt.bc.ca](https://www.bchrt.bc.ca). Consult a lawyer for high-stakes decisions.  
> **Not legal advice.** Self-represented parties: verify every section number, deadline, and form before filing.  
> Statutory pinpoints below are **working references** — confirm against the current consolidation before reliance: `[VERIFY ON BCLAWS]`.

## Skill routing

| Need | Skill |
|------|--------|
| Substantive RTA (evictions, illegal charges, repairs) | `bc-tenancy-substantive` |
| RTB procedure, evidence packaging, hearings, negotiation, enforcement | `bc-tenancy-procedure` (full runtime Modules 1–7) |
| JR petitions, stays, Court of Appeal | `bc-judicial-review-guide` + Module 1 here |
| This skill under alternate name | `bc-tenancy-advanced` (alias) |
| Court-ready drafting standard | `supreme-court-civil-counsel` |
| CanLII / BOA | `canlii-boa-builder` |

## Analytical tags (always)

`[FACT]` · `[ALLEGATION]` · `[LAW]` · `[ARGUMENT]` · `[INFERENCE]` · `[ASSUMPTION]` · `[PROCEDURAL HISTORY]` · `[RECOMMENDATION]` · `[REMEDY]`

---

## Module 1: Judicial Review & Court Escalation

**Next-level:** petitions, stays, appeals to Court of Appeal. Timelines are tight. Grounds are limited. Requires civil litigation chops.

### When to escalate

| Trigger | Notes |
|---------|--------|
| RTB decision unreasonable, procedurally unfair, or jurisdictionally wrong | Map to JR grounds carefully |
| RTB internal review (often discussed as s. 79-type review — **`[VERIFY ON BCLAWS]`**) denied or upheld flawed decision | Exhaust / document the path |
| Tenant needs a **stay** to remain in the unit while litigating | Urgency + RJR-type test |

### Errors that ground judicial review (typical framing)

| Error type | Examples |
|------------|----------|
| Ignored key evidence | Illegal charges, retaliation, *res judicata* |
| Procedural fairness breach | No notice; no meaningful opportunity to respond |
| Jurisdictional error | Decided outside statutory authority |
| Unreasonable finding | No rational basis in the evidence (Vavilov framework — verify pinpoints on CanLII) |
| Fettering of discretion | Rigid policy without considering the facts |

### Handoff package for `bc-judicial-review-guide`

Provide this foundation **first**:

1. Full RTB record (decision, evidence submitted, hearing notes)  
2. All grounds identified (illegal charges, retaliation, *res judicata*, procedural fairness, etc.)  
3. Timeline of RTB proceedings  
4. Evidence the RTB ignored or mischaracterized  

The JR skill then handles: JRPA petition drafting, stay test (commonly *RJR-MacDonald* three-part test — verify), Vavilov reasonableness analysis, BCSC filing and service, responding to applications to set aside a stay.

→ See also: `../bc-judicial-review-guide/SKILL.md`

**`[INDEPENDENT COUNSEL RECOMMENDED]`** for most JR and stay applications (tight timelines, costs risk, opposing counsel).

---

## Module 2: Human Rights Overlaps

**BC Human Rights Code s. 10** — protected grounds in tenancy (confirm current text on BC Laws):

Race, colour, ancestry, place of origin, religion, marital status, family status, disability (physical or mental), sex, sexual orientation, gender identity/expression, age, source of income — **`[VERIFY ON BCLAWS]`**.

### Dual-filing strategy

File at **both** RTB and BC Human Rights Tribunal where grounds overlap. Claims are often **complementary** — one does not automatically preclude the other (**verify current preclusion / parallel-proceeding principles**).

| Forum | Typical remedy focus |
|-------|----------------------|
| **RTB** | Tenancy remedy (void notice, compensation, repair order) |
| **BCHRT** | Discrimination remedy (damages, systemic/public interest remedies) |

### Common intersections

| Situation | Action |
|-----------|--------|
| Eviction after disability disclosure | Test the actual RTA notice ground/good-faith requirements and consider a BCHRT complaint; current RTA s. 47.1 is not a general retaliation section |
| "No pets" used to exclude service animal | BCHRT (Code) |
| Refusal of housing-benefit recipients | Code s. 10 (source of income) — **`[VERIFY]`** |
| Eviction pretext based on family status (children) | RTB dispute + BCHRT |
| Harassment targeting ethnicity or religion | BCHRT analysis + RTB quiet enjoyment under current RTA s. 28, with proof and remedy verified |

### BCHRT filing basics

- File within **1 year** of the last discriminatory act (**confirm current limitation**)  
- Form: Human Rights Complaint — [bchrt.bc.ca](https://www.bchrt.bc.ca)  
- Mediation often offered before hearing  
- Remedies: compensation, policy change, public interest remedy  

→ `references/human-rights-tenancy.md`

---

## Module 3: Strata & Condo Rentals

**Two frameworks, one unit:** RTA (landlord–tenant) + *Strata Property Act* (SPA) (strata–owner).

### Core principle

Strata bylaws bind the **owner (landlord)**, not the tenant directly in the RTA relationship. The landlord **cannot** use strata rules as an RTA workaround.

### Common conflict points

| Situation | Working rule (verify) |
|-----------|------------------------|
| Strata levies fine/cost for tenant conduct | Analyze the SPA/bylaws and procedure, tenancy agreement, indemnity/allocation, RTA s. 5, proof, and remedy; current RTA s. 8 does not invalidate the charge |
| Strata bylaw regulates pets | Analyze SPA/bylaws plus tenancy pet terms and RTA deposit provisions; do not assume one framework automatically answers every issue |
| Strata restricts rentals | Verify current SPA provisions, exemptions/transitions, bylaws, and effect on the particular tenancy |
| Strata move-in/out restrictions | May engage quiet enjoyment under RTA s. 28; assess reasonableness, notice, interference, and loss |
| Access involving strata/contractors | Identify who seeks access and authority; landlord–tenant entry analysis begins with current RTA s. 29 and its exceptions |

**When SPA conflicts with RTA for the landlord–tenant relationship:** RTA typically prevails for that relationship — **confirm** with current authorities.

→ `references/strata-rental-conflicts.md`

---

## Module 4: Manufactured Home Parks (MHPTA)

For mobile/manufactured homes on rented park pads. User owns the home; rents the **pad**. Pad tenancy is regulated under the *Manufactured Home Park Tenancy Act* (MHPTA) — parallel to RTA.

| Issue | RTA (Residential) | MHPTA (Park Pads) |
|-------|-------------------|-------------------|
| What's rented | Residential unit | Land/pad only |
| Eviction notice period | Often 1–4 months (context-dependent) | Often **12 months** for many park terminations — **`[VERIFY]`** |
| Dispute forum | RTB | RTB (same tribunal family — confirm process) |

**Key difference:** Longer notice often reflects investment in the structure on the pad.

→ `references/mhpta-guide.md`

---

## Module 5: Client-Centered Advocacy ⭐ (The Human API)

Evictions hit hard. Housing insecurity is acute stress. **Lead with the human.**

### Trauma-informed approach

1. **Acknowledge first, law second.**  
   Example: *“That’s an incredibly stressful situation. Let me help you understand your options and what needs to happen first.”*
2. Watch for overwhelm — break information into smaller pieces.  
3. Repeat key deadlines clearly: *“The most important thing right now is [deadline].”*  
4. Avoid legalese overload — translate (table below).  
5. Acute housing crisis = real urgency — prioritize next deadline.

### Plain language

| Legal term | Plain language |
|------------|----------------|
| Dispute resolution application | Filing a complaint with the RTB |
| Arbitrator | The RTB official who decides your case |
| Order of Possession | Official order saying you must leave |
| Participatory hearing | A phone/video call where both sides speak |
| Void and unenforceable | That charge/clause doesn’t count — you don’t have to pay it |
| Procedural fairness | You had the right to a fair hearing |
| Judicial review | Taking a bad RTB decision to BC Supreme Court |
| *Res judicata* | The same issue was already decided — can’t be relitigated |
| Retaliatory eviction | Evicted because you stood up for your rights |

### Accessibility

- RTB interpreters (many languages) — inform every client of this right  
- Accommodations: disability, hearing, cognitive access  
- Written submissions if phone/video is a barrier  
- Request accommodation **at filing** — not only on hearing day  

---

## Module 6: Ethics & Professional Rules

### Law Society of BC (for lawyers / supervised practice)

| Duty | Application |
|------|-------------|
| **Competence** (Rule 3.1) | Current RTA knowledge; check amendments before filing |
| **No conflicts** | Cannot act for landlord and tenant in same matter; conflict check first |
| **Candour** | No misrepresentations to RTB or any tribunal |
| **PG 26 / advocates** | Non-lawyer advocates appear under arbitrator permission; lawyers who supervise must ensure competence |
| **Confidentiality** | Tenancy file info protected; consent for filings containing personal details |

### For self-represented parties

This skill provides **legal information, not legal advice**. For complex matters consider:

| Resource | What they do | Contact |
|----------|--------------|---------|
| TRAC | Free tenant information + advocacy | [tenants.bc.ca](https://tenants.bc.ca) |
| CLAS | Legal aid + low-income representation | [clasbc.net](https://clasbc.net) |
| Legal Aid BC | Income-tested representation | [legalaid.bc.ca](https://legalaid.bc.ca) |
| Law Society Referral | First consult reduced rate | [lawsociety.bc.ca](https://www.lawsociety.bc.ca) |

→ `references/trac-clas-resources.md`

---

## Module 7: Level 99 Pro Moves

### Cross-cultural competence

- Interpreter right — request early  
- Cultural context affects documentation, comfort with authority, communication  
- Systemic barriers — meet clients where they are  
- Do not assume legal process familiarity — explain RTB structure from scratch when needed  

### Data-driven arguments

- **CanLII:** published RTB decisions; same landlord tactics defeated  
- RTB decisions database / issue search  
- Pattern evidence: multiple applications by same landlord — may support bad-faith / retaliation theory (**fairness + relevance**)  
- Housing stats (vacancy, average rents) to contextualize harm for abatement/compensation  

**Example argument form** (fill only with verified cites):

> “The landlord’s claim that this was a genuine renovation is undermined by RTB Decision [**verified cite**] where the same landlord issued a Four Month Notice at [prior address] in [year] and the unit was re-rented within 60 days at a higher rate.”

Never invent decision numbers or landlord history.

### TRAC / CLAS collaboration matrix

| Situation | Recommendation |
|-----------|----------------|
| Needs full representation; can’t afford lawyer | TRAC / CLAS / Legal Aid BC |
| Self-rep with support | `bc-tenancy-substantive` + `bc-tenancy-procedure` + TRAC factsheets |
| Complex judicial review | `bc-judicial-review-guide` + legal aid referral + **`[INDEPENDENT COUNSEL RECOMMENDED]`** |
| Human rights overlap | BCHRT + CLAS referral |
| Landlord-side corporate client | Direct legal representation |
| Manufactured home park | Module 4 MHPTA + TRAC if tenant-side |

---

## Reference files

| File | Content |
|------|---------|
| [references/strata-rental-conflicts.md](references/strata-rental-conflicts.md) | SPA vs RTA |
| [references/mhpta-guide.md](references/mhpta-guide.md) | Manufactured home parks |
| [references/human-rights-tenancy.md](references/human-rights-tenancy.md) | BCHRT dual-file |
| [references/trac-clas-resources.md](references/trac-clas-resources.md) | Community resources |
| [references/policy-guidelines-summary.md](references/policy-guidelines-summary.md) | RTB Policy Guidelines index (verify) |

## Workflow for this skill

1. Stabilize client (Module 5) — deadline first.  
2. Route: RTA vs MHPTA vs strata vs human rights.  
3. Load substantive + procedure skills.  
4. If JR path → Module 1 handoff package.  
5. Ethics / referral check (Module 6–7).  
6. Draft with supreme-court-civil-counsel discipline if court-bound.  
