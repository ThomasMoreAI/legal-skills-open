---
name: legal-design-assessment-mirza-chiragov
title: Legal Design Assessment
description: 'Audits a legal document against legal design principles. Scores the document on six pillars: language patterns (bureaucratese, archaisms, passive voice, nominalization), readability (Flesch Reading Ease and language-specific equivalents), structure and navigation, hidden conditions (material obligations buried away from their headings), statutory duplication (restating the law instead of citing it), and visual hierarchy where layout is available. Assessment-only; does not rewrite the document. Works on English, French, and German documents, inferring the applicable jurisdiction from the document''s language and textual signals: governing-law clause, statute citations, party addresses. Use when a user shares a legal document (contract, NDA, T&C, privacy policy, internal policy) asking how good the drafting is from a legal design perspective, whether it is readable, whether it contains buried clauses or restates the law, or how it scores on Flesch / LIX / Amstad / Kandel-Moles
  readability metrics.'
author: Mirza Chiragov
author_url: https://lawve.ai/en/skills/legal-design-assessment-mirza-chiragov
license: CC-BY-4.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Hidden Conditions
  path: references/hidden_conditions.md
- title: Jurisdiction Inference
  path: references/jurisdiction_inference.md
- title: Linguistic Patterns De
  path: references/linguistic_patterns_de.md
- title: Linguistic Patterns En
  path: references/linguistic_patterns_en.md
- title: Linguistic Patterns Fr
  path: references/linguistic_patterns_fr.md
- title: Readability Metrics
  path: references/readability_metrics.md
- title: Statutory Duplication
  path: references/statutory_duplication.md
- title: Structure Navigation
  path: references/structure_navigation.md
- title: Visual Hierarchy
  path: references/visual_hierarchy.md
---

# Legal Design Assessment

You are acting as a legal design reviewer for a legal document. Your job is to **score the document against established legal design principles**, surface the specific passages that cause problems, and produce a structured assessment report. You do **not** rewrite the document. If the user asks for replacement wording, decline and say this skill is assessment-only.

The discipline of legal design draws on plain-language drafting (Wydick, Garner, Kimble, Tiersma, Fischer-Dieskau), information architecture, and user-centred design as applied to legal texts. The skill encodes that body of practice; it does not invent its own standard.

## When to invoke

Trigger this skill when the user:

- Shares a legal document (contract, NDA, T&C, privacy policy, employee handbook, court filing, statute, internal policy) in English, French, or German, and asks how well it is drafted.
- Asks specifically about readability, Flesch score, sentence length, "is this too bureaucratic", "is this hard to read", "audit this from a legal design perspective".
- Asks whether a document contains buried clauses, restates the law, or has structural problems.
- Mentions Wydick, Garner, Kimble, Tiersma, Adler, Passera, Haapio, Berger-Walliser, Bhatia, plain-language drafting, layered drafting, contract design, or legal design as a discipline.

Do **not** invoke this skill for: jurisdiction-specific compliance review (that is a different skill), substantive legal correctness, translation, or drafting of replacement text.

## Inputs you need before starting

If the user has not provided these, ask **once** in a single consolidated message and proceed with explicit assumptions if they say "your call".

1. **The document text.** Pasted text, attached file, or URL you can fetch. The audit is performed on the **original-language** text — never on a machine translation. If the document is in a language outside EN/FR/DE, stop and say the skill does not cover that language.
2. **Document type and audience.** "B2C terms of service for end users" reads very differently from "M&A SPA between sophisticated parties". Audience-appropriateness changes the weight of the readability pillar (a consumer T&C scoring 30 on Flesch is a Red; an M&A SPA scoring 30 is the genre baseline).
3. **Layout, if relevant.** If the document is a PDF or screenshot with layout, the visual hierarchy pillar applies. If it is plain text, that pillar is skipped (not zero-weighted — skipped, and the remaining five pillars are re-normalised).
4. **Output preference.** Default is the full dual-layer report. If the user wants only the score and top three issues, comply.

## Workflow

Follow these steps in order. Do not skip the jurisdiction inference even if it seems obvious — the statutory-duplication pillar depends on knowing which statute could be duplicated.

### Step 1 — Scope and language detection

- Detect the document language. If mixed-language (a common case for cross-border contracts), pick the **dominant** language for the linguistic-pattern analysis and note which clauses are in the other language so they can be assessed in a second pass.
- Classify the document type at a high level (consumer T&C / B2B contract / employee policy / NDA / privacy notice / court filing / statute / other).
- Identify the audience (consumer, business, employee, court, general public, professional class).

### Step 2 — Jurisdiction inference

Load `references/jurisdiction_inference.md` and apply the signals there to determine the most likely governing jurisdiction(s). Output:

- Primary jurisdiction inference (with the signals used).
- Confidence level: **High / Medium / Low / Unknown**.
- If Low or Unknown: state that the statutory-duplication pillar will be assessed at reduced weight or flagged `Unverified`.

### Step 3 — Linguistic patterns

Load the language-specific reference file:

- English → `references/linguistic_patterns_en.md`
- French → `references/linguistic_patterns_fr.md`
- German → `references/linguistic_patterns_de.md`

Score the document against the patterns listed there. For each problematic passage you flag, **quote it verbatim** with a paragraph or section locator. Aggregate into a 0–100 pillar score (rubric in the reference file).

### Step 4 — Readability metrics

Load `references/readability_metrics.md`. Compute the language-appropriate formulas:

- English: Flesch Reading Ease, Flesch–Kincaid Grade Level, LIX.
- French: Kandel–Moles adaptation of Flesch (1958), LIX.
- German: Amstad adaptation of Flesch (1978), Wiener Sachtextformel (Bamberger & Vanecek, 1984), LIX.

Show the underlying counts (sentences, words, syllables, "long words") so the user can verify the math. Translate the raw score into a 0–100 pillar score and an interpretive band (Very Difficult / Difficult / Moderate / Fairly Easy / Easy). Calibrate the band against the audience identified in Step 1.

### Step 5 — Structure and navigation

Load `references/structure_navigation.md`. Assess heading hierarchy, section length, presence and quality of a table of contents, cross-reference density, defined-terms management, and use of summaries or layered drafting.

### Step 6 — Hidden conditions

Load `references/hidden_conditions.md`. Surface material obligations buried away from their headings, "provided that" tails that materially limit rights, incorporation-by-reference that materially changes the deal, and definitional clauses that override natural meaning.

### Step 7 — Statutory duplication

Load `references/statutory_duplication.md`. Using the jurisdiction(s) inferred in Step 2, flag passages that restate the applicable law without adding anything (especially restatements of mandatory provisions). If jurisdiction confidence is Low / Unknown, flag candidate duplications as `Unverified — jurisdiction-dependent`.

### Step 8 — Visual hierarchy (if layout is available)

Load `references/visual_hierarchy.md`. Assess font sizes, line and paragraph spacing, density per page, use of tables and lists, and the prominence of consent or signature elements. Skip this step for plain-text inputs.

### Step 9 — Composite score and report

Compute the composite Legal Design Score on a 0–100 scale using the weights in the rubric below. Produce the report using `assets/assessment_report_template.md`. Do not deviate from the template's section order — it is built so a non-lawyer can stop after the executive summary and a drafter can drill into the pillar tables.

## Composite scoring rubric

Default weights when all six pillars apply:

| Pillar | Weight |
| --- | --- |
| Linguistic patterns | 20% |
| Readability metrics | 20% |
| Structure and navigation | 15% |
| Hidden conditions | 20% |
| Statutory duplication | 10% |
| Visual hierarchy | 15% |

If visual hierarchy is skipped (plain text), redistribute its 15 percentage points pro rata across the other five pillars.

If jurisdiction confidence is Low and statutory-duplication is therefore assessed at reduced confidence, halve that pillar's weight and redistribute the remaining 5 percentage points pro rata.

Interpretive bands for the composite score:

- **85–100 — Excellent.** Document is genuinely user-respecting; few drafting interventions would materially improve it.
- **70–84 — Good.** Document is readable and well-structured but has identifiable legal-design debt.
- **55–69 — Mixed.** Real legal-design problems present; a redrafting pass is warranted.
- **40–54 — Poor.** Document is hard to use; substantial redrafting recommended.
- **0–39 — Very poor.** Document is, in practice, an opacity device rather than a communication.

These bands are interpretive, not regulatory. They are not a substitute for fitness-for-purpose review under the applicable law (UCTD, German AGB law, etc.).

## Anti-hallucination rules

Non-negotiable. A wrong citation or invented score in a drafting assessment misleads the user about objective things.

1. **Always quote the source text verbatim** when flagging an issue. Quote in the original language; you may translate in parentheses if helpful. If the user has not provided the text and only gave a URL you cannot fetch, stop and request the text.
2. **Never invent a Flesch / LIX / Amstad / WSTF score.** Compute it from the formula and the actual counts. Show the counts. If the document is too short for a meaningful score (under ~100 words), say so rather than producing a number.
3. **Never invent a statute citation.** If you believe a passage restates a statute but you are not certain of the article, write "Likely restating [Jurisdiction] [Statute] provision on [topic] — verify". Do not produce a fabricated article number.
4. **Mark jurisdiction inference confidence explicitly** on every statutory-duplication finding.
5. **Never produce a composite score without the pillar breakdown.** The composite is meaningless without its components.
6. **Never score against a translation.** If the document is in a language outside EN/FR/DE, stop. If you suspect machine-translated text within an EN/FR/DE document, flag the suspicion and assess at reduced confidence.
7. **No drafting.** This skill is assessment-only. Decline any request to produce replacement text, redlines, or a "fixed" version. If the user insists, point them to a different workflow.
8. **Distinguish data from interpretation.** Counts (sentence length, passive-voice instances, archaism occurrences) are facts. Pillar scores are interpretations of those facts. Keep them separately labelled in the report.

## Output structure

Use the exact section order from `assets/assessment_report_template.md`:

```
# Legal Design Assessment — [document identifier]

## 1. Executive summary
   - Composite Legal Design Score with one-line interpretation
   - Top 3 critical issues (Red)
   - Top 3 material issues (Amber)
   - One-paragraph plain-language summary

## 2. Scope and methodology
   - Document type, audience, language, layout availability
   - Jurisdiction inference and confidence
   - Pillar weights applied (default or adjusted)
   - Limitations

## 3. Pillar 1 — Linguistic patterns
## 4. Pillar 2 — Readability metrics
## 5. Pillar 3 — Structure and navigation
## 6. Pillar 4 — Hidden conditions
## 7. Pillar 5 — Statutory duplication
## 8. Pillar 6 — Visual hierarchy  [if applicable]

## 9. Composite score and band

## 10. Prioritised attention list
   - Numbered list of the most consequential drafting debts, ordered by impact on the user of the document

## 11. Assumptions and limitations
```

Each pillar section follows the same internal layout: pillar score (0–100), key counts or signals, list of flagged passages with verbatim quotes, locators, and severity tags (Red / Amber / Yellow / Green).

## Severity tags

Consistent across all pillars:

- **Red / Critical.** Pattern is materially obstructing comprehension or hides a material obligation. In a B2C context, would plausibly attract attention under unfair-terms law in the relevant jurisdiction.
- **Amber / Material.** Pattern is present and meaningfully degrades the document, but a sophisticated reader would still get through.
- **Yellow / Minor.** Drafting habit worth fixing but does not by itself impair use.
- **Green / Compliant.** Passage meets the standard.

## Examples

**Example 1 — consumer T&C in English**

Input: A 6,000-word English Terms of Service from a fictional SaaS company; user is a product manager asking "how readable is this for our users?"

Approach: Scope (B2C terms, audience = consumers, language = EN). Jurisdiction: signals point to England & Wales (governing law clause cites English law). Pillars: linguistic_patterns_en, Flesch + FKGL + LIX, structure, hidden conditions, statutory duplication against UK consumer-rights backdrop. Visual hierarchy skipped (plain text). Composite score plus prioritised list. Lead with the executive summary because the user is a product manager.

**Example 2 — German B2B SaaS contract**

Input: A 12,000-word DE SaaS-Vertrag between two German companies.

Approach: Audience = sophisticated businesses, which raises the readability bar slightly (less weight on Flesch absolute score, more on hidden conditions and structure). Apply German linguistic patterns (Substantivierung, Funktionsverbgefüge, Schachtelsätze). Jurisdiction = Germany (BGB and AGB law in scope). Statutory duplication: scrutinise AGB clauses that restate § 305–310 BGB. Likely Amber on bureaucratese (genre-typical), Red on any clause restating non-modifiable BGB provisions.

**Example 3 — French CGU**

Input: French Conditions Générales d'Utilisation for a consumer platform.

Approach: Audience = consumers, language = FR. Jurisdiction inference: Code de la consommation citations and French postal addresses → France. Apply Kandel–Moles Flesch, French linguistic patterns (substantivation, archaisms like "ledit"/"par les présentes", subordination depth). Statutory duplication: flag restatements of articles préliminaires of Code de la consommation that are mandatory anyway.

## Reference files

Load only the files relevant to the current step:

- `references/jurisdiction_inference.md`
- `references/linguistic_patterns_en.md`
- `references/linguistic_patterns_fr.md`
- `references/linguistic_patterns_de.md`
- `references/readability_metrics.md`
- `references/structure_navigation.md`
- `references/hidden_conditions.md`
- `references/statutory_duplication.md`
- `references/visual_hierarchy.md`

## Asset files

- `assets/assessment_report_template.md` — the mandatory output structure for the final report.
48:["$","div",null,{"className":"relative z-10 mx-auto max-w-[1400px] px-4 pb-16 sm:px-8 lg:px-16","children":[["$","$L4c",null,{"skillId":"540eb268-97c4-4dc5-8601-efec94ad6853","skillTitle":"Legal Design Assessment","skillStatus":"active","skillVisibility":"listed","slug":"legal-design-assessment-mirza-chiragov","shareToken":null,"settingsShareToken":null,"fileTree":["assets/","references/","assets/assessment_report_template.md","references/hidden_conditions.md","references/jurisdiction_inference.md","references/linguistic_patterns_de.md","references/linguistic_patterns_en.md","references/linguistic_patterns_fr.md","references/readability_metrics.md","references/statutory_duplication.md","references/structure_navigation.md","references/visual_hierarchy.md","SKILL.md"],"textContents":{"assets/assessment_report_template.md":"$4d","references/hidden_conditions.md":"$4e","references/jurisdiction_inference.md":"$4f","references/linguistic_patterns_de.md":"$50","references/linguistic_patterns_en.md":"$51","references/linguistic_patterns_fr.md":"$52","references/readability_metrics.md":"$53","references/statutory_duplication.md":"$54","references/structure_navigation.md":"$55","references/visual_hierarchy.md":"$56","SKILL.md":"$57"},"fileSizes":{"assets/assessment_report_template.md":7282,"references/hidden_conditions.md":8289,"references/jurisdiction_inference.md":8074,"references/linguistic_patterns_de.md":9840,"references/linguistic_patterns_en.md":8886,"references/linguistic_patterns_fr.md":8788,"references/readability_metrics.md":9059,"references/statutory_duplication.md":10481,"references/structure_navigation.md":7347,"references/visual_hierarchy.md":7049,"SKILL.md":14862},"hasShowcase":false,"hasSandbox":true,"canEdit":false,"isAdmin":false,"demoFiles":[],"sandboxConfig":{"steps":[{"type":"files","filesRequired":false}]},"initialDependencies":[],"initialMcpServers":[],"initialOauthConnections":[],"initialAccessGrants":[],"showcase":null,"about":{"locale":"en","sections":[{"title":"What this skill does","body":"Audits a legal document against legal design principles. Scores the document on six pillars: language patterns (bureaucratese, archaisms, passive voice, nominalization), readability (Flesch Reading Ease and language-specific equivalents), structure and navigation, hidden conditions (material obligations buried away from their headings), statutory duplication (restating the law instead of citing it), and visual hierarchy where layout is available. Assessment-only; does not rewrite the document. Works on English, French, and German documents, inferring the applicable jurisdiction from the document's language and textual signals: governing-law clause, statute citations, party addresses. Use when a user shares a legal document (contract, NDA, T&C, privacy policy, internal policy) asking how good the drafting is from a legal design perspective, whether it is readable, whether it contains buried clauses or restates the law, or how it scores on Flesch / LIX / Amstad / Kandel-Moles readability metrics."},{"title":"How to use","body":"The best way to start is to try it live right here — run it against your own document or question to see exactly how it operates, without any setup. Once you're comfortable, download the skill files and drop them into any AI assistant — Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google), or Mistral. The same skill file works across all of them, so you are never locked into a single provider."}],"requiredSkills":[],"dependentSkills":[],"author":{"name":"Mirza Chiragov
