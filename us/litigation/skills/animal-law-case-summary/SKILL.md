---
name: animal-law-case-summary
title: Animal Law Case Summary
description: Produces litigation-grade case summaries for animal law disputes including cruelty/neglect prosecutions, ownership/custody, dangerous animal designations, veterinary malpractice, and service/assistance animal accommodations. Builds exhibit-cited factual timelines, maps evidence to statutory elements, evaluates expert evidence, and assesses remedies with jurisdiction-specific legal research. Use when summarizing animal law cases, analyzing animal cruelty charges, pet custody disputes, dangerous dog hearings, veterinary malpractice claims, or assistance animal accommodation matters. Also trigger for animal forfeiture, bite liability, wildlife possession, or animal-related court filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/animal-law-case-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Animal Law Case Summary

Produces structured, evidence-grounded case summaries connecting record citations to legal elements and realistic remedies across criminal, civil, administrative, and regulatory animal law forums.

## Prerequisites

Gather before drafting (skip if user says "use defaults" or "just draft"):

1. **Jurisdiction** — state, county, forum (state/federal/administrative)
2. **Procedural posture** — pre-suit, pleadings, TRO/PI, discovery, SJ, trial, sentencing, appeal
3. **Parties and animal ID** — species, breed, microchip/license numbers, current custody
4. **Core record** — see minimum record table below
5. **Audience** — attorney work product, client-facing, or public/educational
6. **Relief sought**

### Minimum Record by Matter Type

| Matter Type | Required Documents |
|---|---|
| Civil litigation | Complaint + exhibits, answer/counterclaims, TRO/PI papers, court orders, key discovery, depositions, expert reports, scheduling order |
| Criminal cruelty | Charging instrument, probable cause affidavit, incident reports/body cam, chain-of-custody docs, ACO/shelter logs, vet/necropsy reports |
| Service/assistance animal | Lease/HOA/accommodation policy, request + correspondence, verification docs, incident reports, decision records |
| Veterinary malpractice | Complete vet records (all providers), expert opinions, purchase/adoption docs, loss documentation |

**Defaults if user doesn't respond:** attorney work product audience; posture as stated or inferred; all applicable matter types. Mark unverified content "[VERIFY]."

## Workflow

### 1. Classify and Lock Posture

Classify into applicable archetypes:

- Criminal cruelty/neglect
- Civil forfeiture/impound challenge
- Dangerous animal designation
- Ownership/title dispute (replevin, conversion, declaratory relief)
- Veterinary malpractice / consumer protection
- Landlord-tenant/HOA pet dispute
- Service animal (ADA Title III) / assistance animal (FHA) accommodation
- Wildlife/exotics possession and permitting
- Agricultural animal welfare enforcement
- Animal-related torts (bite, nuisance, premises liability)

Write a caption block: court/agency, case number, judge/ALJ, filing date, next date.

Critical: never collapse allegations into findings. Identify current animal custody. Surface all deadlines — dangerous dog appeals can be 5–10 days [VERIFY]. Check for "best interest" statutes (e.g., CA Fam. Code § 2605) [VERIFY].

### 2. Build Factual Timeline

Chronological timeline with exhibit-level citations. Per event: date/time, actor, source (document + pinpoint cite), disputed accounts. Use neutral descriptions (body condition scores, not conclusory characterizations). Track both chain of title (ownership) and chain of care (maintenance, medical, bonding). Include exculpatory facts.

### 3. Map Claims to Elements and Evidence

Per claim, charge, or violation:

| Component | Detail |
|---|---|
| Legal standard | Statute + elements |
| Burden | BRD / preponderance / clear & convincing [VERIFY] |
| Key disputed elements | Most likely contested element |
| Supporting evidence | Exhibits mapped to each element |
| Weaknesses | Gaps or undermining evidence |
| Anticipated defenses | At least two opposition attack vectors |

Jurisdiction-specific checks:

- **Cruelty**: mens rea requirement + statutory exemptions (veterinary, agriculture, hunting, research)
- **Dog bite**: strict liability vs. negligence; provocation/trespass/assumption-of-risk defenses
- **Accommodation**: separate ADA "service animal" (task-trained dog only, 28 C.F.R. § 36.104) from FHA "assistance animal" (broader, 24 C.F.R. § 100.204) — never conflate

### 4. Verify Governing Law

Every cited authority must be verified or marked [VERIFY].

Key federal frameworks:

| Framework | Citation |
|---|---|
| Animal Welfare Act | 7 U.S.C. § 2131 et seq. |
| Endangered Species Act | 16 U.S.C. § 1531 et seq. |
| ADA Title III (service animals) | 28 C.F.R. § 36.104, § 36.302(c) |
| FHA (assistance animals) | 24 C.F.R. § 100.204; HUD FHEO-2020-01 |
| ACAA (air travel) | 14 C.F.R. Part 382 [VERIFY] |

For state/local law: locate exact cruelty, dangerous dog, and pet custody statutes plus municipal ordinances. Confirm text and effective dates.

### 5. Analyze Evidence Quality

Per expert/professional witness: qualifications, methods (peer-reviewed?), admissibility (Daubert or Frye [VERIFY]), contested assumptions.

Key checks: vet opinions (full history reviewed?), digital evidence (authenticity, metadata), photos (metadata, fair depiction), necropsy (chain of custody), lay witnesses (distinguish from medical conclusions).

### 6. Assess Remedies

| Category | Considerations |
|---|---|
| Ownership | Replevin, conversion damages, injunctive relief |
| Criminal | Penalties, disposition orders, cost-of-care [VERIFY], ownership bans |
| Dangerous dog | Euthanasia vs. alternatives; stay pending appeal? [VERIFY] |
| Accommodation | Injunctive relief, damages, fees |
| Damages | Market value vs. intrinsic/companionship; statutory/punitive; attorney's fees [VERIFY] |
| Collateral | Housing, professional licenses, immigration |

Address bond/forfeiture deadlines and settlement leverage tied to animal's current placement.

## Output Structure

1. **Overview** — 2–3 sentence case description
2. **Parties and Animals** — identification, relationships, current custody
3. **Procedural Posture** — caption block + status
4. **Key Facts (Timeline)** — exhibit-cited chronology
5. **Claims/Charges and Governing Law** — element mapping
6. **Evidence Strengths and Weaknesses** — candid assessment
7. **Key Disputes** — contested issues
8. **Remedies and Risk Assessment** — realistic outcomes
9. **Next Steps and Deadlines** — action items with dates
10. **Key Takeaways** — non-advocacy, action-oriented paragraph

State the animal's legal classification explicitly (property, property-plus, best-interest standard).

## Post-Draft Alignment

After delivering the summary, confirm:

1. Correct case, parties, and procedural posture?
2. Missing record documents to incorporate?
3. Sections to expand (remedies, expert critique, timeline)?
4. Audience and privilege markings correct?

## Guidelines

- **Neutrality**: distinguish allegations vs. findings vs. stipulations vs. inference throughout
- **Adversarial resilience**: identify top 3 client vulnerabilities; at least 2 opposition attack vectors per claim
- **Citation integrity**: every factual assertion traceable to a record cite or marked [VERIFY]; no invented authorities
- **Audience calibration**: adjust tone, privilege handling, strategic candor by audience
- **Scope**: case summary only — not a memo, motion, demand letter, or press statement
- **Privilege**: label attorney work product; redact sensitive details in client-facing versions
- **Conflicts**: flag dual-role parties (e.g., shelter as both representative and witness)
- **Deadline sensitivity**: animal law deadlines can be 5–10 days; always surface and flag uncertainty
- **Property status**: always state the animal's legal classification — affects standing, remedies, damages
- **ADA vs. FHA**: never conflate service animal (ADA) with assistance animal (FHA)

**Required disclaimer on every output:**

> THIS SUMMARY REQUIRES INDEPENDENT ATTORNEY VERIFICATION OF ALL CITATIONS, LOCAL CODES, AND FACTUAL ASSERTIONS, AND DOES NOT CONSTITUTE LEGAL ADVICE.
