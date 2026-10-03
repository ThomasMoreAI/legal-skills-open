---
name: justinian-flashcards-from-statute
title: Justinian — Flashcards from Statute
description: Use when a user wants to generate spaced-repetition flashcards from a statute, legal code, or regulation for bar exam or legal education purposes. Produces four card formats — term/definition, article/content, fact-pattern/rule, and comparison — plus a spaced-repetition schedule. Supports export to Anki, CSV, and in-app review. Covers all jurisdictions; most heavily used for MENA statutes (UAE Labor Law, KSA Companies Law, KSA PDPL, Lebanese COC).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/justinian/justinian-flashcards-from-statute
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Justinian — Flashcards from Statute

## When to use this

Invoke when a user:
- Wants to memorize a statute, code, or regulation for a bar exam
- Asks for flashcards on a specific legal subject (e.g., "make me flashcards on UAE labor law")
- Wants to set up a spaced-repetition study system for a legal topic
- Has a target exam and needs systematic statute coverage

## Inputs

| Input | Why it matters | Default if missing |
|---|---|---|
| **Statute or statute name** | Determines the source material | Ask: "Which statute or code do you want to cover?" |
| **Jurisdiction** | Determines which version of the statute applies | Infer from statute name; ask if ambiguous |
| **Difficulty level** | Adjusts card complexity | Default: intermediate (bar-exam level) |
| **Number of cards** | Scopes the generation | Default: 20–30 cards per session; offer more |
| **Card format preferences** | User may want only certain types | Default: all 4 formats mixed |

## The four card formats

### Format 1: Term → Definition

Tests vocabulary and definitional precision — essential for code-based systems where statutory definitions are binding.

**Template**: `[Term] ([Jurisdiction])` → `[Statutory definition]`

**Examples**:
- *Front*: "Probation period (UAE)" → *Back*: "Maximum 6 months per Federal Decree-Law 33/2021 art. 9; renewable once"
- *Front*: "Waqf (KSA)" → *Back*: "Inalienable Islamic endowment; dedicated to charitable purposes; administered by Ministry of Awqaf"
- *Front*: "Force majeure (Lebanon — COC)" → *Back*: "Cas de force majeure: event external to the debtor, unforeseeable, and irresistible; releases debtor from contractual liability"

### Format 2: Article → Content

Tests recall of specific statutory provisions — critical for exams where citing the article number earns points.

**Template**: `What does [statute] art. [N] say?` → `[Content, verbatim key elements]`

**Examples**:
- *Front*: "What does UAE Decree-Law 33/2021 art. 51 say about end-of-service gratuity?" → *Back*: "EOSG: 21 days basic salary per year for first 5 years of service; 30 days per year thereafter; total capped at 2 years' basic salary; not owed if employee resigns before completing 1 year"
- *Front*: "What does Lebanese COC art. 364 say?" → *Back*: "[Content of that article — do not fabricate; use source text]"

**Important**: generate article-content cards only from the actual statute. Do not fabricate article numbers or content. If the user provides the statute text, generate from it directly. If working from memory, stay at the level of well-known, verifiable provisions.

### Format 3: Fact Pattern → Rule

Tests rule application — the core bar exam skill. The student must identify which rule applies and state it correctly.

**Template**: `[Scenario]` → `[Rule + outcome]`

**Examples**:
- *Front*: "Employee terminated for cause in UAE after 4 years. EOSG owed?" → *Back*: "Per FDL 33/2021 art. 44 (grounds for cause termination), EOSG is forfeited if the termination meets one of the enumerated grounds; otherwise full EOSG per art. 51 applies. Check: did the employer meet the procedural requirements (written notice, investigation)?"
- *Front*: "Lebanese company formed as SARL. Minimum share capital required?" → *Back*: "Under Lebanese Commercial Code, SARL requires minimum capital of LBP 5,000,000 (note: practical thresholds may have shifted; verify current regulatory practice given currency instability)"
- *Front*: "KSA company under Companies Law 2022: shareholder wants to transfer shares in a closed joint-stock company. Any restrictions?" → *Back*: "Under the Companies Law 2022, transfer of shares in a closed JSC is subject to pre-emptive rights of existing shareholders unless the articles provide otherwise; registration with the commercial registry required"

### Format 4: Comparison

Tests the ability to distinguish between similar rules across jurisdictions or within a single statute — high-yield for multi-jurisdictional practitioners.

**Template**: `How does [rule] in [Jurisdiction A] differ from [Jurisdiction B]?`

**Examples**:
- *Front*: "Non-compete: UAE (FDL 33/2021) vs KSA (Labor Law art. 83)" → *Back*: "Both: max 2 years duration. UAE (Cabinet Decision 1/2022): requires proportionality test — geographic scope, subject-matter, and time must all be reasonable; employee may seek damages if overbroad. KSA: more textual; courts enforce if within statutory parameters; proportionality analysis less developed"
- *Front*: "Arbitration: DIFC (DIAC) vs KSA (SCCA)" → *Back*: "Both UNCITRAL Model Law aligned. DIFC: common law jurisdiction; English-language proceedings standard; DIAC Rules (2022). KSA: Arabic primary; Sharia arbitrability limits (certain family and public law matters not arbitrable); SCCA Rules (2021)"

## Spaced repetition schedule

Cards are cycled through the following schedule, adjusting based on performance:

| Performance | Next review |
|---|---|
| New card (unseen) | Review today + tomorrow |
| Correct once | Review in 3 days |
| Correct twice | Review in 1 week |
| Correct three times | Review in 1 month |
| Correct four or more times | Review in 3 months |
| Wrong at any stage | Reset to "new card" |

The schedule is based on the core principle of spaced repetition (Ebbinghaus forgetting curve): reviewing a card just before you would forget it is maximally efficient.

## Export formats

| Format | Use case |
|---|---|
| **Anki (.apkg)** | Anki desktop or mobile; most flexible spaced-repetition app |
| **Plain CSV** | Import to Quizlet, RemNote, Notion, or any custom system |
| **In-app review** | Justinian's native flashcard interface with session tracking |

**Anki import notes**: cards export as Basic (front/back) and Cloze (fill-in-the-blank for article-content cards). Decks are organized by statute name and jurisdiction.

## Bilingual card support

For Arabic-language statutes (UAE, KSA) or bilingual practice (Lebanese COC in French and Arabic):

- Cards can be generated with the Arabic original on one side and English translation on the other
- Arabic legal terminology is preserved and bolded
- Bilingual cards are tagged separately for review

## Quality rules

- **Do not fabricate article numbers or content**. If the source statute is not provided and you do not have high-confidence knowledge of the specific provision, flag it: "This card references [article N] — please verify against the official text before relying on it for exam."
- Where the source gave specific article citations (as in the UAE Labor Law examples), keep them exactly.
- For statutes subject to recent amendment (KSA PDPL 2024, UAE Labor Law 2022 amendments), include a note: "Verify: this provision reflects [year] version; check for amendments."

## Related skills

- [[justinian-curriculum-builder]]
- [[justinian-bar-exam-prep-uae]]
- [[justinian-bar-exam-prep-ksa]]
- [[justinian-bar-exam-prep-lb]]
- [[justinian-exam-time-management-coach]]
