---
name: casesim-fact-pattern-builder-sboghossian
title: Fact Pattern Builder — Realistic Case Files for Training and Scenario Planning
description: Use when building a realistic fact pattern for litigation training, moot court preparation, bar exam practice, or settlement scenario planning. Generates a complete synthetic or semi-synthetic case file from real or provided facts, with complicating factors (witness credibility, evidence gaps, jurisdictional issues), a supporting document set, and a difficulty score. Produces privileged and non-privileged document splits. Applicable across MENA and international forums.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-fact-pattern-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Fact Pattern Builder — Realistic Case Files for Training and Scenario Planning

## When to use this

Invoke when:
- A law school or moot court program needs a realistic fact pattern for student exercises
- A firm is training junior associates on a practice area using synthetic scenarios
- A bar candidate needs practice scenarios for exam preparation
- A litigation team wants to model settlement scenarios from a real case (using partial real facts, with synthetic additions for confidentiality)
- A mock arbitration preparation requires a complete case file
- An attorney wants to stress-test a legal theory against a developed fact pattern before committing to it

## Inputs

| Input | Required | Notes |
|---|---|---|
| Use case type | Yes | Training / bar prep / moot court / settlement modeling |
| Practice area | Yes | Contract, employment, real estate, tort, commercial, criminal, family, etc. |
| Jurisdiction | Yes | Primary forum; secondary if cross-border |
| Desired difficulty | Yes | 1 (introductory) to 5 (distinction / complex) |
| Seed facts | Optional | Real or partial facts to build around (will be sanitized/synthetic in output) |
| Complicating factors | Optional | See list below |
| Output format | Optional | Full case file / summary only / document set only |

## Complicating factor options

These are added to increase realism and training value:

| Factor | Description |
|---|---|
| Witness credibility issue | One key witness has a prior inconsistent statement or conflict of interest |
| Evidence gap | A document that should exist is missing or destroyed (raises adverse inference question) |
| Jurisdictional split | The contract has a foreign governing-law clause; local mandatory law may override |
| Parallel proceedings | A related arbitration or regulatory investigation is ongoing |
| Third-party liability | A non-party may be partly responsible |
| Corporate veil question | The contracting entity is a shell; a related company holds the real assets |
| Timing issue | A limitation period or notice requirement is close to being triggered or may have expired |
| Expert disagreement | The two expert witnesses reached opposite conclusions from the same data |
| Language/translation dispute | A key contract term means different things in the Arabic and English versions |

## Case file output structure

A complete fact pattern produced by this skill includes:

### 1. Case Overview
- Parties (plaintiff/claimant; defendant/respondent; third parties if any)
- Background narrative (how the dispute arose)
- Key dates timeline
- Forum and applicable law
- Brief statement of the claims and defenses

### 2. Document Set
A realistic supporting document set — all synthetic unless the user provided seed facts:
- The relevant contract(s) with specific provisions highlighted
- Key correspondence (email chains, letters, notices)
- Meeting minutes or board resolutions (where relevant)
- Financial documents (invoices, payment records, bank statements where relevant)
- Expert reports (summary form)
- Witness statements (first-person narrative format)

**Privileged / non-privileged split:** each document is labeled:
- Non-privileged (disclosable)
- Privileged — attorney-client (training: note why privilege applies)
- Privileged — work product (training: note why)
- Disputed (training: reason for dispute, arguments for both positions)

### 3. Difficulty Assessment

Each fact pattern is scored 1–5:

| Score | Description |
|---|---|
| 1 — Foundation | Single issue; clear liability; standard damages; no complicating factors; one jurisdiction |
| 2 — Developing | Two issues; one factual dispute; standard procedural posture |
| 3 — Intermediate | Multiple issues; at least one complicating factor; cross-jurisdictional element |
| 4 — Advanced | Several interacting issues; credibility dispute; evidentiary challenges; jurisdictional complexity |
| 5 — Expert | All of the above plus strategic uncertainty; multiple possible outcomes; high-stakes damages |

### 4. Legal Issues Map

A structured list of the key legal issues the fact pattern raises, organized by:
- Primary issues (those the exercise is designed to develop)
- Secondary issues (ancillary; can be addressed for extra credit)
- Trap issues (designed to mislead; tests whether the student chases red herrings)

### 5. Model Answer / Teaching Notes

(For training use; withheld if the fact pattern is used for competitive assessment)
- How an experienced practitioner would analyze the primary issues
- Key arguments for each side
- Likely outcome range
- Where most students / trainees go wrong on this pattern

## Practice-area-specific notes

### Contract disputes (MENA context)
- Include a governing-law clause with a potential conflict between chosen law and mandatory local law
- For UAE: consider whether the UAE Civil Transactions Law mandatory provisions might override a foreign-law clause
- For DIFC: DIFC Contract Law (modeled on English common law) applies; consider whether the contract is entirely within DIFC or has onshore touchpoints

### Employment disputes
- MENA employment law is highly regulatory; include a limited-term vs. unlimited-term contract ambiguity for UAE scenarios
- For KSA: Saudi Labour Law end-of-service benefits (Article 84 and related provisions) are a rich source of realistic disputes
- For Lebanon: the Lebanese Labour Code's mandatory indemnity provisions

### Commercial fraud / dishonesty
- Include documentary trail that can be read two ways
- Include at least one witness whose testimony is internally consistent but inconsistent with the documents

## Use cases — examples

### Moot court competition (intermediate level)
A UAE-incorporated joint venture between a Beirut-based company and a Dubai-based company disputes the distribution of profits after one party claims the other diverted business opportunities. Governing law: UAE Civil Transactions Law. Complicating factors: a parallel arbitration in DIAC; a dispute about whether a key email is privileged.

### Bar prep — Lebanese contract law (foundation)
A Lebanese contractor has not been paid for construction work. The employer claims the work was defective. The contract has a disputes clause requiring notice within 14 days of a complaint. The employer gave notice on day 17. Issues: breach of contract; defect claims; notice requirement; damages quantification.

### Associate training — employment (advanced)
A Dubai law firm associate must advise on a termination scenario involving a UAE-national employee who was on a limited-term contract, terminated early, claims arbitrary dismissal under the UAE Labour Law, and has a parallel DIFC claim because the employment agreement references DIFC law. Expert disagreement on the correct annualized salary for compensation purposes.

## Related skills

- [[casesim-client-q-and-a-prep]]
- [[casesim-cross-examination-rehearsal]]
- [[casesim-judge-bench-perspective]]
- [[casesim-outcome-probability-estimator]]
- [[academy-justinian-tutor]]
- [[academy-litigation-game-coach]]
