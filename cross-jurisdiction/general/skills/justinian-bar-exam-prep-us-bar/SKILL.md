---
name: justinian-bar-exam-prep-us-bar
title: Justinian — US Bar Exam Prep (UBE + State)
description: 'Use when a user is preparing for the US bar examination — primarily the Uniform Bar Exam (UBE) covering the MBE, MEE, and MPT, or state-specific exams (California, Florida, Virginia). Provides NCBE-aligned MBE drilling, MEE essay grading with rubric feedback, MPT timed practice, and MPRE ethics preparation. Jurisdiction: US.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-bar-exam-prep-us-bar
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — US Bar Exam Prep (UBE + State)

## Scope

Most US states use the Uniform Bar Exam (UBE), administered by the National Conference of Bar Examiners (NCBE). A UBE score is portable across UBE jurisdictions. This skill covers the full UBE and flags key state-specific variations for California, Florida, and Virginia — the three major non-UBE or hybrid states.

## UBE structure

| Component | Format | Weight | Duration |
|---|---|---|---|
| MBE (Multistate Bar Examination) | 200 MCQs | 50% | Day 2: 6 hours |
| MEE (Multistate Essay Examination) | 6 essays | 30% | Day 1 AM: 3 hours |
| MPT (Multistate Performance Test) | 2 tasks | 20% | Day 1 PM: 3 hours |

Total: two-day exam. Most UBE states require a score of 260–270 (out of 400) to pass; varies by state.

## MBE — Multistate Bar Examination

### Subjects (7 tested)

| Subject | Approximate % of questions |
|---|---|
| Civil Procedure | ~25 questions |
| Constitutional Law | ~25 questions |
| Contracts (including UCC Article 2) | ~25 questions |
| Criminal Law and Procedure | ~25 questions |
| Evidence | ~25 questions |
| Real Property | ~25 questions |
| Torts | ~25 questions |

### MBE technique

**Format**: 200 questions over 6 hours = 1.8 minutes per question. Answer all questions — there is no penalty for wrong answers.

**Approach per question**:
1. Read the call of the question first (what is being asked?)
2. Read the facts actively — identify which subject area is implicated
3. Apply the rule to the facts; eliminate clearly wrong answers
4. On close calls: NCBE tests nuances; the "most correct" answer is the one that precisely applies the rule

**Common traps by subject**:

| Subject | Common trap |
|---|---|
| Contracts | Common law vs UCC distinction; mirror image rule vs battle of forms (UCC 2-207) |
| Constitutional Law | State action requirement; levels of scrutiny (rational basis / intermediate / strict) |
| Crim Law / Procedure | Common law felony murder vs modern MPC approach; 4th Amendment curtilage |
| Evidence | Hearsay vs non-hearsay; present sense impression vs excited utterance timing |
| Real Property | Future interests (remainder, executory interest, reversion); RAP |
| Civil Procedure | Personal jurisdiction (International Shoe / Walden); Erie doctrine |
| Torts | Negligence vs strict liability triggers; comparative vs contributory negligence |

**Pacing rule**: if you have not answered after 90 seconds, mark your best answer and move on. Return at the end if time permits.

## MEE — Multistate Essay Examination

### Format
6 essay questions, 30 minutes each. NCBE publishes the list of MEE subjects (expands beyond the 7 MBE subjects):

**Additional MEE subjects** (beyond MBE 7):
- Business Associations (agency, partnerships, corporations, LLCs)
- Conflict of Laws
- Family Law
- Secured Transactions (UCC Article 9)
- Trusts and Estates (wills, intestacy, trust formation and administration)

### MEE rubric and grading

NCBE graders use a point grid. A well-structured answer that:
1. Identifies all legal issues in the question
2. States the applicable rule for each issue
3. Applies the rule to the specific facts
4. Reaches a clear conclusion

...will score better than a longer answer that misidentifies the central issue.

**IRAC is the default framework for all MEE answers.** On a 30-minute essay, a typical strong answer covers 3–5 issues and is approximately 1–2 pages.

**Common MEE error patterns**:
- Issue-spotting only without rule application
- Applying the wrong body of law (e.g., applying common law contract rules to a UCC sale of goods)
- Forgetting the MEE-specific subjects when prepping (Secured Transactions and Conflict of Laws are under-studied)

## MPT — Multistate Performance Test

### Format
2 tasks, 90 minutes each. Each MPT provides a "file" (client memo, deposition excerpt, contract, factual record) and a "library" (cases, statutes, regulations). The task is to produce a specific document: a memo, a brief, a letter, a contract clause analysis.

**Key rules**:
- Use only the library provided — outside law knowledge is not tested and should not be inserted
- The task document is specified; follow the format and structure requested exactly
- Demonstrate legal analysis and persuasive writing; not comprehensive law review

**Justinian MPT coaching**:
- Time-boxed MPT simulations (90 minutes)
- Feedback on: task compliance, use of library sources, analytical quality, writing clarity

## MPRE — Multistate Professional Responsibility Exam

A separate 60-question ethics exam required by most states:
- Tests the ABA Model Rules of Professional Conduct
- 2 hours; closed book
- Passing scores range by state (~75–86 depending on jurisdiction)
- Typically taken during law school (after Professional Responsibility course) or before bar admission

**Key MPRE topics**: confidentiality (Rule 1.6); conflicts of interest (1.7, 1.8, 1.9); competence (1.1); communications with represented and unrepresented parties; fees; advertising; supervisory responsibilities.

## State-specific variations

### California Bar Exam

California does not fully use UBE. The California Bar Exam includes:
- California-specific essays (5 essays) testing California law variations
- Performance test (similar to MPT)
- MBE component (UBE MBE questions)
- Separate MCLE and character and fitness requirements

**Key California-only subjects**: Community property, California civil procedure (distinct from FRCP), California Evidence Code variations, Professional Responsibility (California-specific rules differ from ABA Model Rules).

### Florida Bar Exam

Florida uses UBE MBE but Florida-specific essays:
- Tests Florida-specific rules in property, torts, procedure
- Separate Florida Board of Bar Examiners character and fitness process

### Virginia Bar Exam

Virginia uses a hybrid: UBE MBE scores accepted for transfer, but Virginia has separate essay component testing Virginia-specific law.

## Character and fitness

All jurisdictions require a character and fitness review. Disclosure of criminal records, academic misconduct, and financial irregularities (including significant debt) is required. Timeline for this review can be lengthy — initiate early.

## Justinian-specific support

- **MBE drills**: NCBE-aligned questions by subject; explanations for each answer; weakness tracking by subject
- **MEE essay grading**: submit practice essays; receive rubric-based scoring with line-by-line commentary
- **MPT simulations**: full 90-minute timed practice with realistic files and libraries; feedback on task compliance
- **MPRE practice**: 60-question mock exam + ABA Model Rules flashcards
- **California prep module**: California-specific supplement covering community property, CA civil procedure, CA professional responsibility

## Caveats

Bar exam format, passing scores, and accepted scores differ by jurisdiction and are updated annually. Always verify current NCBE guidance and state-specific requirements. This guide reflects publicly available NCBE and state bar information and is a preparation resource, not an authoritative source.

## Related skills

- [[justinian-curriculum-builder]]
- [[justinian-flashcards-from-statute]]
- [[justinian-exam-time-management-coach]]
- [[justinian-case-explainer-socratic]]
- [[justinian-bar-exam-prep-uk-sqe]]
