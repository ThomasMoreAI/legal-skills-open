---
name: public-tool-case-summarizer-public-sboghossian
title: Case Summarizer (Public Tool)
description: Use when a user pastes or links a court judgment URL and needs a structured plain-English summary — covering facts, legal issue, holding, reasoning, and practical implications. This is a free public-facing tool with multi-jurisdictional coverage including DIFC, ADGM, UK (BAILII), US federal (CourtListener), and ECJ; limited for KSA and UAE onshore where public full-text databases are restricted. Designed as a lead-generation entry point with a daily free usage limit.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/public-tool/public-tool-case-summarizer-public
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Case Summarizer (Public Tool)

## What it does

The Case Summarizer is a free, no-login public tool that converts a court judgment — submitted as pasted text or a supported URL — into a structured plain-English summary. It is designed to make case law accessible to legal professionals who need a rapid digest, law students, and informed non-lawyers researching their rights or contracts.

### Output format (per judgment)

Every summary produces seven sections:

1. **One-paragraph summary** — the whole case in 3–5 sentences: who, what happened, what the court decided, and why it matters
2. **Facts** — three bullets covering the key background facts (parties, transaction or conduct, how the dispute arose)
3. **Legal issue(s)** — the specific legal question(s) the court was asked to decide, stated as questions
4. **Holding** — the court's answer to each issue; stated plainly ("The court held that...")
5. **Reasoning** — five bullets summarizing the reasoning chain that led to the holding; includes any key principles or tests applied
6. **Dissent (if any)** — brief note on any dissenting judgment and the alternative view
7. **Practical implications** — what this case means for practitioners and clients going forward; any open questions it leaves; impact on prior decisions it overrules or qualifies

---

## Capabilities and coverage

### Fully supported jurisdictions and databases

| Jurisdiction | Source | Coverage |
|---|---|---|
| DIFC Courts | DIFC Courts official website (judgments published) | Full text — all published judgments from 2006 onwards |
| ADGM Courts | ADGM Judiciary website | Full text — published judgments |
| UK | BAILII (bailii.org) — England & Wales, Scotland, Northern Ireland | Supreme Court, Court of Appeal, High Court, Employment Tribunal (major decisions) |
| US federal | CourtListener (courtlistener.com) | Federal circuit courts, district courts, Supreme Court |
| ECJ / CJEU | EUR-Lex (eur-lex.europa.eu) | Full text of all CJEU and General Court decisions |

### Partially supported (text-paste only)

| Jurisdiction | Status | Reason |
|---|---|---|
| UAE onshore courts | Text-paste only | No public full-text database; Abu Dhabi and Dubai courts do not publish judgments to a public-access URL |
| KSA courts | Text-paste only | Ministry of Justice does not operate a public full-text judgment database for general users |
| Lebanon courts | Text-paste only | Limited online publication; Cassation Court decisions available through subscription databases (Lexis Legal) |
| Egypt courts | Text-paste only | No consolidated public-access database |
| GCC jurisdictions (Bahrain, Kuwait, Qatar, Oman) | Text-paste only | Varies; Bahrain Court of Cassation has some online publication |

**For UAE and KSA:** Users who have access to the court's authenticated portal or subscription database (Lexis Legal ME, Westlaw MENA, LexisNexis) can paste the judgment text directly; the summarizer will produce the structured output.

---

## Usage limits and account tiers

| Tier | Daily limit | Features |
|---|---|---|
| Free (no login) | 1 case summary / day | All 7 sections; watermarked PDF output |
| Registered (free account) | Unlimited summaries | No watermark; saved history; export to Word |
| Pro (paid subscription) | Unlimited; batch processing | API access; custom output templates; team sharing |

Output watermark for free tier: *"Summarized by Louis — louis.haqq.ai | For informational purposes only — not legal advice."*

---

## Behavior rules

- **Do not fabricate citations.** If the URL does not resolve or the text provided is not a judgment, output an error message asking for valid input.
- **Do not give legal advice.** The summary is a research aid. Include the disclaimer: *"This summary is for informational purposes only and does not constitute legal advice. Consult qualified legal counsel before relying on any case."*
- **Preserve quoted text accurately.** When quoting the holding or key reasoning passages, quote verbatim (or mark as paraphrased).
- **Flag when the case has been appealed, overturned, or superseded.** If the tool can detect a subsequent decision (from the same database) that affects this case, flag it prominently.
- **Multi-issue cases.** Where a judgment deals with multiple legal issues, address each issue separately in the Issues / Holding / Reasoning sections.

---

## Usage patterns

**Pattern 1 — URL submission**
```
User: Summarize this DIFC case: https://difccourts.ae/judgments/[reference]
Tool: [fetches page, extracts judgment text, produces 7-section summary]
```

**Pattern 2 — Text paste**
```
User: [pastes judgment text]
Tool: [parses text, identifies parties, court, date, issues, holding, produces summary]
```

**Pattern 3 — Research context**
```
User: "I'm looking at a DIFC unfair dismissal case — what are the key precedents?"
Tool: [if the user provides a specific case, summarize it; if they're asking generally, route to [[research-case-law]] instead]
```

---

## Failure modes and escalation

| Failure mode | Response |
|---|---|
| URL does not resolve or is behind a paywall | Return error; ask user to paste text directly |
| Text provided is not a judgment (e.g., news article, legal brief) | Alert user; ask for the judgment itself |
| Judgment is in Arabic and user requests English summary | Invoke [[public-tool-legal-translator-ar-en-public]] first, then summarize |
| Judgment length exceeds context window | Apply [[ref-long-documents-50pp]] chunked processing approach; summarize each major section, then synthesize |
| Court or case reference cannot be verified | Include a verification warning in the output |

---

## Permissions and safety

- **Read-only tool** — does not file documents, access court portals, or make any write actions
- **No personal data storage** — judgment text submitted by free (no-login) users is not stored after the session
- **Legal disclaimer always included** — the output always includes the non-legal-advice disclaimer; this cannot be disabled in the free tier

---

## Related skills

- [[public-tool-statute-explainer-public]]
- [[public-tool-legal-jargon-simplifier-public]]
- [[public-tool-contract-summarizer-public]]
- [[public-tool-legal-translator-ar-en-public]]
- [[research-case-law]]
- [[ref-long-documents-50pp]]
