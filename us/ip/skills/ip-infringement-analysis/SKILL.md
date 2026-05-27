---
name: ip-infringement-analysis
title: IP Infringement Analysis
description: Produces structured IP infringement memoranda evaluating patents, trademarks, copyrights, and trade secrets. Performs claim-by-claim patent comparisons, likelihood-of-confusion trademark tests, substantial similarity copyright assessments, and trade secret misappropriation evaluations with defense and remedies analysis. Use for infringement opinions, pre-filing assessments, cease-and-desist support, licensing disputes, or settlement valuation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ip-infringement-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [litigation, analysis, memo]
---

# IP Infringement Analysis

Generates an element-by-element infringement memorandum covering rights identification, type-specific analysis, defenses, and remedies quantification.

## Prerequisites

1. **IP registrations/filings** — patents (with claims), trademark registrations, copyright registrations, or trade secret identification documents
2. **Accused instrumentality** — product specs, screenshots, source code, marketing materials, or service descriptions
3. **Prosecution history** (patents) — file wrapper, claim amendments, examiner rejections
4. **Relevant agreements** — licenses, NDAs, employment/non-compete agreements, assignments
5. **Correspondence** — cease-and-desist letters, licensing negotiations, admissions
6. **Jurisdiction and procedural posture** — forum, statute of limitations status

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Quick Start

1. Identify the IP right(s) at issue (Step 1)
2. Characterize the accused activity (Step 2)
3. Apply the type-specific framework: Patent (A), Trademark (B), Copyright (C), or Trade Secret (D) (Step 3)
4. Assess defenses and vulnerabilities (Step 4)
5. Evaluate available remedies (Step 5)
6. State overall assessment with confidence level (Step 6)

Analyze each IP type separately when multiple types are at issue.

## Output Structure

### Step 1: IP Rights Identification

| Field | Detail |
|-------|--------|
| IP Type | Patent / Trademark / Copyright / Trade Secret |
| Registration/Application No. | |
| Filing/Priority Date | |
| Owner/Claimant | |
| Key Claims/Mark/Work Description | |
| Status | Active / Expired / Pending |

### Step 2: Accused Activity

| Field | Detail |
|-------|--------|
| Accused party | |
| Product/service/activity | |
| Date of first use | |
| Geographic scope | |
| Commercial context | |

### Step 3: Type-Specific Analysis

Apply the applicable framework(s):

#### A. Patent Infringement

1. **Claim construction** — construe disputed terms under Phillips v. AWH Corp., 415 F.3d 1303 (Fed. Cir. 2005) [VERIFY]
2. **Literal infringement** — all-elements rule, limitation-by-limitation comparison using claim chart below
3. **Doctrine of equivalents** — function-way-result or insubstantial differences test; check prosecution history estoppel per Festo [VERIFY]
4. **Means-plus-function** — identify § 112(f) limitations, map corresponding structure
5. **Indirect infringement** — induced (§ 271(b)): knowledge + specific intent; contributory (§ 271(c)): material component, no substantial non-infringing use
6. **Validity challenges** — anticipation (§ 102), obviousness (§ 103), enablement/written description (§ 112)

**Claim Chart:**

| Claim Element | Accused Feature | Literal? | DOE? | Notes |
|---------------|----------------|----------|------|-------|
| [Limitation 1] | | Y/N | Y/N | |
| [Limitation 2] | | Y/N | Y/N | |

A single missing limitation defeats literal infringement on that claim.

#### B. Trademark Infringement

Identify the correct circuit's likelihood-of-confusion test (Polaroid, Sleekcraft, Lapp, etc.) and apply:

| Factor | Analysis | Weight |
|--------|----------|--------|
| Similarity of marks (sight, sound, meaning, commercial impression) | | |
| Relatedness of goods/services | | |
| Strength of senior mark (inherent + acquired distinctiveness) | | |
| Evidence of actual confusion | | |
| Defendant's intent | | |
| Consumer sophistication | | |
| Channels of trade / marketing convergence | | |
| Likelihood of expansion into related markets | | |

If famous mark: assess dilution by blurring or tarnishment (§ 1125(c)). Evaluate defenses: descriptive fair use, nominative fair use, First Amendment.

#### C. Copyright Infringement

1. **Ownership** — valid registration, chain of title
2. **Access** — direct or circumstantial evidence
3. **Substantial similarity** — extrinsic test (objective, filterable elements) + intrinsic test (subjective, ordinary observer)
4. **Idea/expression filtration** — exclude ideas, facts, scènes à faire, merger doctrine elements before applying substantial similarity
5. **De minimis** — whether copying falls below actionable threshold

**Fair Use (17 U.S.C. § 107):**

| Factor | Analysis | Favors |
|--------|----------|--------|
| Purpose and character (transformative?) | | P / D |
| Nature of copyrighted work | | P / D |
| Amount and substantiality used | | P / D |
| Market effect | | P / D |

#### D. Trade Secret Misappropriation

1. **Identification** — describe each claimed trade secret with specificity
2. **Qualification** — independent economic value from secrecy + reasonable secrecy measures
3. **Misappropriation method** — improper means (theft, breach of duty, espionage) or breach of confidentiality obligation
4. **Inevitable disclosure** — applicable only in jurisdictions recognizing the doctrine; requires high similarity between roles
5. **Restrictive covenants** — NDA/non-compete scope, enforceability, temporal/geographic limits

### Step 4: Defenses & Vulnerabilities

| Defense | Applicability | Risk Level |
|---------|--------------|------------|
| Statute of limitations / laches | | High/Med/Low |
| Estoppel (prosecution, equitable, licensee) | | |
| Exhaustion / first sale | | |
| Independent creation / reverse engineering | | |
| Invalidity / unenforceability | | |
| Fair use / nominative use | | |
| Unclean hands | | |

### Step 5: Remedies Assessment

| Remedy | Availability | Estimated Range |
|--------|-------------|-----------------|
| Lost profits | | |
| Reasonable royalty | | |
| Disgorgement of profits | | |
| Statutory damages | | |
| Enhanced/treble damages (willfulness) | | |
| Attorneys' fees (exceptional case) | | |
| Preliminary injunction (eBay factors) | | |
| Permanent injunction | | |

All damages estimates are preliminary — validate with economic expert analysis.

### Step 6: Overall Assessment

| Item | Assessment |
|------|-----------|
| Infringement likelihood | Strong / Moderate / Weak |
| Strongest arguments for infringement | |
| Greatest vulnerabilities | |
| Recommended course of action | Litigate / Settle / License / Monitor |
| Settlement valuation range | |

Do not state ultimate legal conclusions without qualifying confidence level.

## Troubleshooting

| Issue | Resolution |
|-------|-----------|
| Uncertain claim construction | Flag ambiguous terms explicitly; present competing constructions with likelihood assessment |
| Circuit split on LOC factors | Identify the controlling circuit; note split and flag if forum selection could change outcome |
| Mixed literal/DOE results across claims | Analyze each claim independently; a single claim suffices for infringement |
| Incomplete accused instrumentality info | Note gaps; qualify analysis as preliminary; request missing specs before finalizing |
| Foreign IP rights implicated | Flag when Paris Convention, Berne Convention, or TRIPS may apply; analyze domestic and foreign rights separately |

## Guidelines

- Cite controlling authority from the relevant jurisdiction; flag persuasive-only authority from other circuits
- Use `[VERIFY]` for any citation not confirmed against source documents
- Flag privilege, work-product, or ethical issues (e.g., conflict of interest in analyzing a current client's competitor)
- Output is draft work product — include explicit notation that it does not constitute legal advice
