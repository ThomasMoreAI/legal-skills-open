---
name: prompt-pack-complex-law-simple-summary-sboghossian
title: Complex Law → Simple Summary
description: Use when a lawyer needs to summarise a complex legal or tax provision in plain language suitable for a non-lawyer client or business team. The output captures key compliance requirements, practical implications, and any action items — stripping technical jargon while preserving all substantive meaning. Applicable to any jurisdiction; MENA-aware for UAE, KSA, LB, EG, and GCC regulatory instruments.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-complex-law-simple-summary
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Complex Law → Simple Summary

Regulatory texts, tax codes, and complex contract provisions are written by lawyers for lawyers. This skill converts them into clear, accurate summaries that business clients can read, understand, and act on — without losing the substantive content that makes the advice useful.

## When to use this

- A client has been provided with a legal or regulatory document and needs a non-technical summary before a decision or meeting.
- The in-house legal team needs to brief finance, HR, or operations on a new regulation or statutory obligation.
- A law has changed and the firm needs to produce a client alert that explains the change in plain terms.
- Preparing board packs or executive briefings that include a legal section.
- A complex tax provision needs to be explained to a CFO or accountant who is not a lawyer.
- Following a due diligence exercise, distilling findings into non-technical language for management.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| The legal / tax provision or document text | This is what will be summarised | The user pastes the text or attaches the document |
| Target audience | Determines vocabulary, depth, and format | Ask the user: C-suite / finance team / HR / all-staff |
| Jurisdiction | The summary must be accurate for the applicable legal system | Ask the user |
| Purpose of the summary | Drives what to emphasise: compliance obligations, financial impact, operational changes, risk | Ask the user |

## Optional inputs

- Length target (e.g., "fit in one slide" or "maximum one page").
- Whether examples or analogies should be included.
- Whether action items should be embedded or listed separately.
- Whether a "what this means for us" tailored section is needed.

## Methodology

### Step 1 — Read for legal structure
Before summarising, identify:
- The type of instrument (statute, regulation, contract clause, court decision, regulatory guidance).
- The operative provisions (obligations, rights, prohibitions, thresholds, deadlines).
- The exception and safe-harbour provisions (what is excluded from the rule).
- The penalty or consequence provisions (what happens if the rule is breached).

### Step 2 — Identify the key points
Extract only the points that are material to the reader's situation. Typical categories:
1. **Who is affected?** (Scope of application — entity type, size, sector, location.)
2. **What must be done?** (The primary obligation or right.)
3. **By when?** (Deadline or effective date.)
4. **What happens if we don't?** (Penalty, liability, regulatory consequence.)
5. **Are there any exceptions?** (Carve-outs or safe harbours that might apply.)
6. **What do we need to do now?** (Practical action items.)

### Step 3 — Write the summary

**Structure for a plain-language summary:**

**What this provision says (one sentence):**
State the purpose of the provision in one plain sentence. No legal terms.

**Who it applies to:**
List the scope concisely (e.g., "All UAE-incorporated companies with turnover above AED 3.75 million").

**Key obligations:**
- Bullet-point list of what the reader must do or must not do.
- Use active voice and present tense.
- Each bullet = one obligation.

**Key deadlines or thresholds:**
Present as a small table if there are multiple dates or numbers.

**Exceptions or safe harbours:**
Explain any exceptions in equally plain language; do not omit — they may be the most important part for the client.

**Consequences of non-compliance:**
State penalties factually (fines, criminal liability, license suspension) without understating or overstating severity.

**What this means for [Company / us]:**
Tailor to the client's specific situation: which obligations apply, which are already met, and which need action.

**Action items:**
Numbered list, each with a responsible party and deadline.

### Step 4 — Quality check
Before sending the summary, verify:
- Every material obligation from the source text is captured (nothing has been accidentally omitted).
- No obligation has been softened or eliminated by the simplification.
- Any numbers (thresholds, rates, deadlines) are exactly as stated in the source.
- Technical terms that could not be avoided are defined in plain language in parentheses on first use.
- The summary does not add qualifications or caveats that are not in the source text.

## Format guidance

| Audience | Format |
|---|---|
| Board or C-suite | One-page max; leading summary sentence; three to five bullets; action table |
| Finance / tax team | Can be two pages; include numbers in a table; reference the source article/section |
| All-staff communication | No jargon; use real-world examples; FAQ format if multiple questions |
| In-house legal briefing | Structured as a legal note but written in plain English; include source citations |

## MENA regulatory context

When summarising MENA instruments, note:
- UAE federal laws are in Arabic; official English translations exist for many (but are advisory rather than authoritative). If summarising a translation, state this limitation.
- KSA laws are enacted in Arabic and published in the Official Gazette (Um al-Qura); English translations are unofficial.
- Lebanese laws are in Arabic (and sometimes French); many practitioners work from the French text.
- Egyptian laws are in Arabic; the Adl database publishes official texts.
- DIFC and ADGM legislation is in English and is the authoritative version.

## Common mistakes

- Over-simplifying to the point of removing a material qualification (e.g., "all companies must file" when the law says "companies with annual turnover above X").
- Using the summary to add legal advice not in the source text — a summary distils, it does not interpret.
- Omitting penalty provisions because they are uncomfortable — clients need the full picture.
- Using passive voice and abstract language ("it is required that") instead of direct language ("you must").

## Related skills

- [[prompt-pack-client-advisory-note]]
- [[prompt-pack-convert-complex-document-into-key-points]]
- [[prompt-pack-convert-law-into-checklist]]
- [[prompt-pack-contract-summary-for-executives]]
- [[prompt-pack-case-law-research-prompt]]
