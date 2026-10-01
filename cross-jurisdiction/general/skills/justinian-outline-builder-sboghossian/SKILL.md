---
name: justinian-outline-builder-sboghossian
title: Justinian — Course Outline Builder
description: Use when a law student needs a comprehensive course outline for exam preparation, bar revision, or self-study. Produces a structured topic hierarchy with black-letter rules, leading cases (1–3 per topic), common exam patterns, issue interactions, and memorization aids (mnemonics, comparison charts). Calibrated to specific law-school courses (Contracts, Torts, Civ Pro, Con Law, Crim Law, Evidence, Property, Corporate, and more) and to the applicable jurisdiction. Particularly strong for MENA civil-law courses (Lebanon, UAE, KSA, Egypt) and common-law courses (DIFC, UK, US).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-outline-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Course Outline Builder

## When to use this

Use this skill when:

- A student is beginning exam preparation and needs a structured framework for a course
- A bar candidate needs a jurisdiction-calibrated rule summary for a tested subject
- A trainee lawyer needs to build a working knowledge of a new practice area quickly
- A professor wants a skeleton outline to share with students as a course reference

## Inputs

| Input | Required? | Default |
|-------|-----------|---------|
| Course name | Yes | — |
| Jurisdiction | Yes | Ask if not specified |
| Level | No | 2L/3L |
| Format preference | No | Markdown + flashcard-ready |
| Depth | No | Standard (3-level hierarchy) |

**Supported courses (non-exhaustive):** Contracts / Law of Obligations, Torts / Civil Liability, Civil Procedure, Constitutional Law, Criminal Law, Criminal Procedure, Evidence, Property / Real Rights, Corporate Law, Administrative Law, International Law, Employment Law, IP, Banking Law, Family Law, Arbitration, Tax.

**Supported jurisdictions:** US, UK, France (code-based), Lebanon (Code of Obligations and Contracts; French-influenced), UAE onshore (Civil Code; Civil Transactions Law), DIFC (common-law), ADGM (common-law), KSA (Sharia + Royal Decrees), Egypt (Civil Code Law 131/1948).

## Output structure

Every outline follows this pattern:

```
# [Course Name] — [Jurisdiction] Outline

## [Topic 1 Name]

### Black-letter rule
[The complete, element-by-element statement of the rule]

### Leading cases / instruments
- [Case or statute 1] — [one-line significance]
- [Case or statute 2] — [one-line significance]
- [Case or statute 3 if applicable]

### Common exam patterns
- [Scenario type 1]: [what to spot + what to argue]
- [Scenario type 2]: ...

### Tested issue interactions
- This topic often appears with [Topic X] because [reason]

### Memorization aid
[Mnemonic, acronym, comparison chart, or rule-decision tree]

---
## [Topic 2 Name]
...
```

## Standard topic sets by course

### Contracts / Law of Obligations

1. Formation — offer, acceptance, consideration / cause
2. Capacity
3. Defects in consent — mistake, duress, fraud, undue influence
4. Illegality + public policy
5. Interpretation — plain meaning, contra proferentem, ejusdem generis
6. Implied terms
7. Conditions, representations, and warranties
8. Performance + discharge
9. Breach — material vs minor; anticipatory
10. Remedies — damages (direct, consequential, punitive), specific performance, rescission
11. Third-party rights / stipulation pour autrui
12. Force majeure + hardship

**Jurisdiction callouts:**
- Lebanon: Code of Obligations and Contracts (COC) governs; French doctrine influential; civil-law cause doctrine rather than common-law consideration
- UAE onshore: Civil Transactions Law (Federal Law 5/1985 as amended); Art. 246 good-faith obligation; Art. 390 liquidated damages subject to court reduction
- DIFC: DIFC Contract Law 2004 (UNIDROIT-influenced); common-law approach to consideration; penalty clause discussion ongoing
- KSA: general contractual freedom under Sharia; specific rules for Islamic finance instruments

### Torts / Civil Liability

1. Negligence — duty, breach, causation, damage
2. Occupier's liability
3. Defamation
4. Product liability
5. Nuisance
6. Strict liability
7. Vicarious liability
8. Contributory negligence + comparative fault
9. Damages — general, special, non-pecuniary

**Jurisdiction callouts:**
- Lebanon: Arts. 122–134 COC — fault (khata'), damage, and causation
- UAE: Civil Transactions Law Arts. 282–298 — general civil liability
- DIFC: common-law tort principles applicable as received English law

### Criminal Law

1. Actus reus elements
2. Mens rea — intent, recklessness, negligence, strict liability
3. Inchoate offences
4. Complicity
5. Defences — necessity, duress, self-defence, insanity
6. Homicide hierarchy
7. Property offences
8. Financial crimes (fraud, embezzlement, AML)

**Jurisdiction callouts:**
- KSA: Islamic criminal law (hudud, qisas, ta'zir categories); no codified penal code historically; Criminal Procedure Law (Royal Decree M/39)
- UAE: Penal Code (Federal Law 3/1987 as amended); plus special laws (cybercrime, AML, economic crimes)
- Lebanon: Penal Code 1943 (French-influenced)

### Evidence

1. Relevance + probative/prejudicial balancing
2. Hearsay + exceptions
3. Character evidence
4. Expert witnesses
5. Privileges — attorney-client, work product, spousal
6. Authentication + chain of custody
7. Best evidence rule
8. Burden of proof standards

### Corporate Law

1. Entity types + formation
2. Directors' duties — care, loyalty, disclosure
3. Shareholder rights + remedies
4. Capital maintenance
5. M&A — due diligence, representations, conditions, closing
6. Insolvency basics
7. Listed company obligations

**Jurisdiction callouts:** See [[kb-corporate-law-uae]], [[kb-corporate-law-lb]], [[kb-corporate-law-ksa]] for jurisdiction-specific frameworks.

## Exam-pattern section — how to write it

For each topic, identify:

1. **The classic test scenario** — what fact pattern reliably tests this rule?
2. **The trap** — what do students commonly miss (hidden sub-issue, element they skip)?
3. **The counter-argument** — what's the strongest opposing argument?

Example (Contracts — Formation):

> **Classic test:** Offer + attempted acceptance by conduct + cross in the mail. Tests mailbox rule, mirror-image, and whether conduct constitutes acceptance.
>
> **Trap:** Students miss that the offer was revoked before acceptance — revocation timing matters.
>
> **Counter-argument:** Even if mailbox rule doesn't apply, conduct may create estoppel.

## Memorization aids

Where appropriate, include:

- **Acronyms**: IRAC, DEEDS (Duress, Error, Exclusions, Damages, Statute) etc.
- **Decision trees**: binary flowchart from facts to conclusion for complex elements (e.g., negligence tree: duty → breach → factual cause → proximate cause → damages)
- **Comparison tables**: side-by-side of two similar concepts (e.g., condition vs warranty, material breach vs minor breach)
- **Element checklists**: box-check format for complex offences or tests

## Flashcard-ready format

Append a flashcard block at the end of each topic:

```
FLASHCARD: [Topic]
Q: What are the elements of [rule]?
A: (1) [element 1]; (2) [element 2]; (3) [element 3].
Source: [statute/case]
```

These can be imported directly into Anki or similar spaced-repetition tools.

## Quality checks

- Every rule statement is complete (no shortcuts)
- Every case cited is real and the one-line significance is accurate
- Every exam pattern is genuinely tested, not hypothetical
- Memorization aids are accurate (a wrong mnemonic is worse than none)
- Jurisdiction callouts are present whenever the rule varies across jurisdictions

## Do not

- Do not fabricate case citations or statute numbers — flag gaps as "verify current version"
- Do not include rules from a different jurisdiction than specified without clearly labeling them
- Do not pad topics with academic debate that never appears on exams (unless the user specifically wants a research-oriented outline)

## Related skills

- [[justinian-irac-coach]] — practice applying rules from this outline to fact patterns
- [[justinian-legal-essay-grader]] — assess how well the student has internalized the outline
- [[justinian-law-school-brief-summarizer]] — brief the leading cases listed in each topic
- [[justinian-flashcards-from-statute]] — convert element lists into flashcard format
- [[justinian-exam-time-management-coach]] — plan exam timing given the number of topics
