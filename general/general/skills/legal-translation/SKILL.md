---
name: legal-translation
title: Legal Translation Skill  `v0.2.0`
description: 'Expert-level legal document translation — understands law, not just language. Use whenever a user wants to translate any legal document or legal text between any languages. Triggers: "translate this contract/agreement/order/affidavit/MoU/lease/ notice/petition", any legal document upload with a target language, or any request to make legal content readable in another language. Also trigger for transliteration of legal names/entities, bilingual legal document creation, and legal terminology lookups. Covers all major language pairs — contracts, MoUs, affidavits, court orders, power of attorney, wills, leases, legal notices, petitions, appeals, corporate filings, immigration docs, IP agreements, and employment contracts. Use when both law and language are involved. See "Not in Scope" before proceeding.'
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/legal-translation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Translation Skill  `v0.2.0`

**Legal translation that thinks about legal effect, not literal words.**

This skill is the international extension of **Modern Jurist** — a legal translation
app originally built for the Indian legal ecosystem (English ↔ Hindi, Marathi, Gujarati,
Kannada), which reached an advanced stage of development and was recognised for its
approach of translating legal *intent and effect*, not just words. This skill takes that
same philosophy global: every language pair, every jurisdiction, every document type.

The goal is not to produce a finished translation. The goal is to produce a high-quality
**draft** that a bilingual lawyer or qualified legal translator can review, verify, and
finalise for use.

---

## Audience

This skill is designed for use by:
- **Bilingual lawyers** reviewing AI-assisted drafts before client or court use
- **Qualified legal translators** using AI to accelerate first-draft production
- **In-house counsel** working across jurisdictions who need a working draft for review
- **Legal paralegals** preparing documents for supervising lawyer sign-off

**Not for:** end-clients self-serving translations of binding instruments without lawyer review. Every output from this skill is a draft, not a final-form instrument.

---

## Not in Scope

**Stop and redirect** if the request falls into any of these categories:

- **Certified / sworn translations** required for court filing, immigration authorities, or official government submission — route to a credentialed sworn translator in the relevant jurisdiction
- **Apostilled documents** where the translation must itself be re-apostilled — the apostille chain requires a human certified translator
- **Jurisdictions with statutory restrictions** on AI-assisted translation of court filings or legal instruments (check local bar rules before proceeding)
- **Documents where no bilingual reviewer is available** — if the user cannot identify a qualified bilingual reviewer, do not produce a full translation; explain why and suggest they engage a certified translator
- **Requests for legal advice** on the translated content — this skill translates; it does not advise on legal effect in the target jurisdiction

If any of the above applies, say so clearly and stop.

---

## Work Shape

This is **accretive-judgment work** — the output is a draft for a bilingual reviewer, not a final-form instrument. Every output must:

1. Be watermarked: `⚠ DRAFT — Bilingual lawyer or qualified legal translator review required before execution or filing`
2. Include clause-level confidence bands (see Step 3)
3. Include at least one specific clause flagged for lawyer review in Translator's Notes
4. End with the delegation gate (see Step 6)

---

## Escalation Triggers — Halt and Ask

Stop translating and ask the user before proceeding if any of the following apply:

- **Document type cannot be identified** — ask the user to describe it
- **Source or target jurisdiction is unclear** — do not assume; ask
- **Target language not specified** — ask; never assume from context
- **Document contains untranslatable terms with material legal effect** — flag each one, explain the gap, ask how to proceed
- **Request is for a certified/sworn output** — explain this is out of scope; redirect
- **Governing law clause conflicts with party addresses or stated jurisdiction** — flag the conflict; ask which governs
- **Source text is ambiguous in a way that changes legal meaning** — do not resolve arbitrarily; flag and ask

---

## The Four Layers of Legal Translation

Every legal translation must work at all four layers simultaneously:

1. **Linguistic** — correct grammar, syntax, vocabulary in target language
2. **Legal-technical** — correct legal terms of art, not dictionary translations
3. **Jurisdictional** — how this type of document is actually drafted in the target language's legal system
4. **Pragmatic** — does this read like it was drafted natively? Would a lawyer in the target jurisdiction trust this document?

A translation that passes Layer 1 but fails Layer 4 is useless for legal purposes.

---

## Step-by-Step Workflow

### Step 1 — Intake and Analysis

Before translating a single word, analyze the document:

**Required inputs — if any are missing, ask before proceeding:**
- Source language *(required)*
- Source jurisdiction *(required — do not proceed with assumed jurisdiction)*
- Target language *(required)*
- Target jurisdiction *(required — do not proceed with assumed jurisdiction)*

**Also identify:**
- Document type (see Document Type Library below)
- Parties and their roles
- All defined terms (these must be translated consistently throughout)
- Special clauses: arbitration, governing law, force majeure, indemnity, liability caps
- Dates, reference numbers, amounts — note all; they must not change

**Read the right reference file:**
- For target language conventions → `references/legal-language-conventions.md`
- For document-type patterns → `references/document-type-library.md`
- For legal terms across languages → `references/legal-glossary.md`

**State your intake findings** briefly before translating, e.g.:
> *"Detected: English lease agreement (Indian jurisdiction) → Hindi (Maharashtra). Parties: Landlord / Tenant. Defined terms: 8. Special clauses: arbitration (Mumbai seat), notice period. No escalation triggers. Proceeding."*

### Step 2 — Pre-Translation Glossary Build

For any document over ~200 words, mentally build a translation glossary first:

1. List all defined terms in the source document
2. Assign their target-language equivalents (consistently)
3. Note any terms with no direct equivalent in the target legal system
4. Note proper nouns, company names, reference numbers — flag these as UNTRANSLATED

For long documents, show this glossary to the user before proceeding:
> *"Before I translate, here are my term mappings: [table]. Does this look right?"*

This is the single most important quality step. Inconsistent term translation is the #1 failure mode in legal translation.

### Step 3 — Translate with Confidence Bands

**The golden rule:** Translate legal *effect*, not legal *words*.

**Assign a confidence band to every clause or section:**

| Band | Meaning |
|------|---------|
| 🟢 H | Standard term with a well-established direct equivalent in the target legal system. Low reviewer burden. |
| 🟡 M | Term of art with a documented equivalent, but jurisdictional drift is possible. Reviewer should verify. |
| 🔴 L | No direct equivalent in target legal system — explanatory translation only. Lawyer must review and adapt. |

Mark each clause or section with its band in the output: `[H]`, `[M]`, or `[L]`.

Apply these rules without exception:

#### Structure
- Preserve ALL structural elements: clause numbering (1.1, 1.1.1), headings, sub-headings, schedules, annexures, recitals, definitions sections, signature blocks
- Never merge or split clauses
- Never reorder content
- Tables → preserve as tables; column headers translated, data preserved

#### Legal Language Conventions
- Use the traditional formal opening for this document type in the target language (see `references/document-type-library.md`)
- WHEREAS clauses → translate to the traditional recital form in target language
- IN WITNESS WHEREOF → translate to the traditional closing attestation in target language
- Operative words (shall, will, must, may, agrees to) → use their correct legal equivalents, not conversational equivalents
- "Shall" in legal drafting ≠ future tense; it means obligation — translate accordingly

#### Defined Terms
- Once a term is defined (e.g., "the Company"), use only that translated term everywhere
- Never paraphrase a defined term mid-document
- Definitions section → translate the definition label AND the definition body

#### Proper Nouns — STRICT RULE
- Party names (people, companies) → NEVER translate, NEVER transliterate unless specifically requested
- Place names → keep in original, add transliteration in parentheses on first use if target uses a different script
- Reference numbers, case numbers, registration numbers → NEVER change

#### Dates and Numbers — STRICT RULE
- Dates: preserve in original format; optionally add local format in parentheses
- Currency: preserve symbol and amount exactly (₹50,000 stays ₹50,000)
- Percentages, fractions, measurements → never change

#### Operative vs Recital Language
- Recitals (WHEREAS) → descriptive, past/present tense, translate naturally
- Operative provisions (the actual obligations) → precise, use "shall/will/must" equivalents, no ambiguity
- Definitions → match the formality and precision of the source

### Step 4 — Transliteration (when requested or needed)

Transliteration = converting a word's *sounds* into a different script, while translation = converting its *meaning*.

**When to transliterate vs translate:**

| Scenario | Approach |
|----------|----------|
| Party name in a different script | Transliterate (e.g., "Rahul Sharma" → "راحل شرما" in Urdu script) |
| Company name | Transliterate, never translate |
| A legal term that exists in the source jurisdiction but not the target | Translate + transliterate original in parentheses |
| Place names | Translate official name if one exists; otherwise transliterate |
| Currency names | Translate (rupee → روپیہ) |
| Legal latin phrases (force majeure, mens rea, etc.) | Keep in Latin; add translated meaning in parentheses |

**Transliteration quality rules:**
- Use the most widely accepted romanization/script convention for the language pair
- For Devanagari ↔ Latin: use IAST standard for formal/academic; simplified phonetic for legal
- For Arabic ↔ Latin: use simplified ALA-LC for legal documents
- For Cyrillic ↔ Latin: use BGN/PCGN romanization
- For Chinese ↔ Latin: use Hanyu Pinyin with tone marks
- For Japanese ↔ Latin: use Modified Hepburn

Always mark transliterations clearly: *[transliteration]* or in italics

### Step 5 — Format and Present Output

**Mandatory output header on every translation:**
```
⚠ DRAFT — Bilingual lawyer or qualified legal translator review required before execution or filing
Skill: legal-translation v0.2.0 | Source: [language/jurisdiction] | Target: [language/jurisdiction]
```

**For inline text (pasted content, short extracts):**
Show the full translated text in a clean block with confidence bands per clause. Follow with Translator's Notes.

**For full documents:**
```
---
⚠ DRAFT — Bilingual lawyer or qualified legal translator review required before execution or filing
---
[DOCUMENT HEADER - translated]
---
[Full translated document body — each clause marked [H], [M], or [L]]
---
TRANSLATOR'S NOTES:
[See Step 6]
---
```

**For file inputs (PDF/DOCX) → file outputs:**
- Read source file using pdf-reading skill or docx skill as appropriate
- Produce translated DOCX using the docx skill
- Preserve formatting: fonts, spacing, heading styles, tables
- For RTL languages (Arabic, Hebrew, Urdu, Persian): note to user that paragraph direction must be set RTL in Word

**For bilingual documents (side-by-side):**
Present in a two-column table: Original | Translation, clause by clause, with confidence band in a third column.

### Step 6 — Translator's Notes and Delegation Gate

Every output ends with this structure:

```
TRANSLATOR'S NOTES
==================
Confidence summary: [X clauses H] [Y clauses M] [Z clauses L]

Terms with no direct equivalent:
• [term] — [what was chosen and why] [L]

Jurisdictional gaps:
• [any concept that exists in source jurisdiction but not target]

Flagged for mandatory lawyer review:
• Clause [X] — [reason: untranslatable term / jurisdictional gap / operative ambiguity]
• [at least one clause must always be listed here]

Transliteration key:
• [any names or terms that were transliterated]

─────────────────────────────────────────────────────
DELEGATION GATE

This output is a translation draft, not a final-form legal instrument.

✗ This is NOT legal advice. Interpretation of legal effect in the target 
  jurisdiction is the responsibility of a qualified lawyer in that jurisdiction.

✗ Privilege warning: If this document is privileged or work-product protected,
  sharing it for translation may break privilege unless the translator is within 
  the privilege circle. Confirm with supervising counsel before sharing.

✗ Accountability: The bilingual lawyer or qualified legal translator reviewing 
  this draft is accountable for the final translation — not this skill.

✗ For court filing, official submission, apostilled documents, or certified use:
  engage a sworn/certified translator in the relevant jurisdiction.
─────────────────────────────────────────────────────
```

---

## Failure Modes

### (i) Legal advice vs. legal support
This skill provides **translation support**, not legal advice. It does not and cannot:
- Advise on whether a translated clause will be enforceable in the target jurisdiction
- Advise on whether the original document's terms are commercially appropriate
- Interpret legal effect in the target jurisdiction's courts

Interpretation of legal effect in the target jurisdiction is the local lawyer's call.

### (ii) Privilege implications
Translating a privileged document or work-product may **break legal professional privilege** if the document is shared outside the privilege circle. Before translating any litigation document, draft legal advice, or privileged communication:
- Confirm the translator is within the privilege circle (e.g., engaged by the same client or instructed by the same lawyer)
- Flag this to the user if the document appears to be privileged material

### (iii) Accountability gap
This skill produces a draft. The bilingual lawyer or qualified legal translator named in the engagement is accountable for the final translation. This skill is not a substitute for professional accountability.

---

## File Handling

| Input type | Method |
|------------|--------|
| Uploaded PDF | Use pdf-reading skill: `pdftotext -layout` first; rasterize pages if garbled/scanned |
| Uploaded DOCX | Use docx skill: `extract-text document.docx` |
| Pasted text | Translate directly |
| Scanned image/PDF | Rasterize pages with `pdftoppm`, read visually via vision, then translate |

| Output type | Method |
|-------------|--------|
| Chat (default) | Present translated text in clean formatted block with draft watermark |
| DOCX output | Use docx skill to produce formatted Word document; include draft watermark in header |
| Bilingual DOCX | Two-column table + confidence band column in DOCX via docx skill |
| PDF output | Use pdf skill |

---

## Document Type Library

Quick reference — for full patterns, see `references/document-type-library.md`.

| Document Type | Key Features to Preserve |
|---------------|--------------------------|
| Contract / Agreement | Definitions section, operative clauses, representations & warranties, governing law, dispute resolution |
| MoU / LoI | Non-binding language, intent clauses, exclusivity provisions |
| Affidavit | Solemn declaration language, deponent identity, court reference, jurat |
| Power of Attorney | Scope of authority, revocation terms, principal/agent designations |
| Will / Testament | Testator identity, beneficiary designations, executor appointment, revocation of prior wills |
| Lease / Tenancy Agreement | Property description, rental amounts, term, renewal, termination clauses |
| Court Order | Court identity, case reference, operative orders, compliance timelines, judge's authority |
| Legal Notice | Notice period, demand/action requested, consequences of non-compliance |
| Petition / Application | Court/authority addressed, relief sought, grounds, prayer clause |
| Corporate Resolution | Entity identity, quorum, resolution operative language, authorization |
| IP Assignment | IP description, consideration, warranty of ownership, assignment operative clause |
| Employment Contract | Designation, compensation, IP assignment, non-compete, termination |
| Arbitration Clause | Seat, rules, language, number of arbitrators |
| Immigration Document | Personal data fields, authority stamps, reference numbers |

---

## Supported Language Pairs

This skill handles all major language pairs. For language-specific conventions and script guidance, see `references/legal-language-conventions.md`.

**Priority legal languages** (most common in international legal work):
- English ↔ Spanish, French, German, Portuguese, Italian, Dutch
- English ↔ Hindi, Marathi, Gujarati, Bengali, Tamil, Telugu, Urdu
- English ↔ Arabic (MSA), Hebrew, Turkish, Persian
- English ↔ Mandarin Chinese, Japanese, Korean
- English ↔ Russian, Ukrainian, Polish
- Any ↔ Any (not just English-based)

**Script awareness:**
- RTL scripts (Arabic, Hebrew, Urdu, Persian, Sindhi) → flag layout direction in output
- Devanagari (Hindi, Marathi, Sanskrit) → always native script unless user requests romanization
- CJK (Chinese, Japanese, Korean) → use appropriate character set; never mix Simplified/Traditional Chinese
- Latin-script languages with diacritics (French, German, Spanish, Polish, Vietnamese) → never drop accent marks

---

## Quality Checklist

Run this before presenting any translation:

- [ ] Escalation triggers checked — none apply (or halted and asked)
- [ ] Document type correctly identified
- [ ] Source jurisdiction confirmed (not assumed)
- [ ] Target jurisdiction confirmed (not assumed)
- [ ] Draft watermark on output
- [ ] All defined terms translated consistently
- [ ] Confidence bands (H/M/L) on every clause
- [ ] At least one clause flagged for lawyer review in Translator's Notes
- [ ] Proper nouns, names, company names untouched (or transliterated if requested)
- [ ] All dates, amounts, reference numbers unchanged
- [ ] Clause numbering and structure preserved
- [ ] Traditional document opening used for target language
- [ ] Traditional closing (attestation/witness clause) used for target language
- [ ] Operative words (shall/must/may) correctly rendered
- [ ] Transliterations marked clearly
- [ ] Translator's Notes complete
- [ ] Delegation Gate included
- [ ] Failure modes noted where relevant (privilege, legal advice, accountability)

---

## Reference Files

Read these when needed — do not load all at once:

- `references/legal-glossary.md` — ~80 core legal terms translated across 12 languages
- `references/legal-language-conventions.md` — Document conventions, formal openings/closings, script rules, and jurisdiction notes for major legal languages
- `references/document-type-library.md` — Full templates and structural patterns for 14 document types across languages

---

*Review cadence: ad hoc. Report issues at https://github.com/braveheartjun/Modern-Jurist-international-legal-translation-skill/issues*
