---
name: employment-law-research
title: US Employment Law Research
description: Research a US employment law topic across federal, state, and city jurisdictions and produce structured research notes with proper source attribution. Use this skill any time the user asks about US employment laws, regulations, or pending legislation - from a single jurisdiction question to a 50-state survey. Triggers include phrases like "research [employment law topic]", "what are the laws on [employment topic]", "state-by-state [employment topic]", "help me understand [topic] across the US", or any prompt that asks for a legal landscape overview before another deliverable. Always run this BEFORE the employment-law-dashboard skill if a dashboard is the eventual output. Output is a structured research note that distinguishes primary sources (statutes, regs, agency guidance) from secondary sources (law firm alerts, tracker orgs).
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/employment-law-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# US Employment Law Research

This skill produces a structured research note on a specific area of US employment law. The note is the input for downstream work like building a dashboard, writing a memo, or briefing a stakeholder. The most important thing the skill does is enforce a clean separation between primary-source claims (the statute says X) and secondary-source claims (Cooley wrote about it last week).

Use this skill standalone when the user just wants research, OR as the first step before the `employment-law-dashboard` skill. If a dashboard is the eventual deliverable, complete this skill's workflow first and save the research note before invoking the dashboard skill.

## When to use

The skill should fire whenever a user asks for research, comparison, or landscape on a US employment law topic. Examples:
- "Research the state of US laws on workplace surveillance."
- "What are the pay transparency laws across the US?"
- "Help me understand non-compete enforcement state by state."
- "I need a brief on pregnancy accommodation requirements nationally."
- "Make a dashboard for [employment law topic]" → run this first, then the dashboard skill.

## Workflow

### 1. Clarify scope before researching

Before doing any web searches, lock down five things with the user:

1. **Topic** — be specific. "AI in hiring" is too broad; "use of AI tools for employment decisions" is workable.
2. **Jurisdictional scope** — federal layer + which states? Default to "federal layer + the 3-5 most prominent state regimes + any city laws", but confirm.
3. **Deep-dive jurisdictions** — ask the user which states or cities they want a more detailed treatment of. The downstream dashboard supports one or more deep-dive tabs (one per jurisdiction). Suggest a default based on the topic (typically the most stringent or most-litigated regime), but ask explicitly: "Which states do you want a deep-dive page for? I'd suggest [X] but happy to do more or different ones." Capture the full list before researching so you know which jurisdictions to gather extra detail on.
4. **Recency window** — how recent does "recent" mean? Default last 12 months for legislation, last 6 months for reporting.
5. **Audience** — practitioner / executive / general. This shifts how technical the writeup gets.

For dashboard prerequisites, you can usually inherit scope from the dashboard request directly without a separate clarification round.

### 2. Read the source policy

Before searching, read `references/source-policies.md`. This is the load-bearing constraint of the skill. It explains which kinds of statements need primary sources only, and which can use reputable secondary sources. Apply it as you research, not just at writeup time — if you find yourself reaching for a secondary source for a statutory claim, push back to the primary source.

### 3. Conduct research

Use available web search and fetch tools. Cover the layers in this order:

**a. Federal layer**
- Any federal statute, regulation, or controlling case law on the topic.
- Recent federal activity: executive orders, agency guidance, pending legislation, enforcement action.
- Primary sources for federal statutes: the U.S. Code on `uscode.house.gov` or `gpo.gov`. For regulations, the Code of Federal Regulations on `ecfr.gov`. For agency guidance, the agency's own `.gov` site.

**b. State and city enacted laws**
- Identify the most prominent enacted regimes (typically 3-5).
- For each: official statute citation, enacting bill number, effective date, enforcing agency, key obligations, key carveouts.
- Pull primary sources: state legislature websites, official rules databases, agency guidance pages on the agency's `.gov` domain. NYC laws are at `codelibrary.amlegal.com/codes/newyorkcity` and `rules.cityofnewyork.us`. State laws live on the state legislature site (e.g., `ilga.gov`, `leg.colorado.gov`, `capitol.texas.gov`).

**c. Pending bills**
- Approximate count of states with pending legislation.
- The 2-3 most-watched pending bills.
- Primary citation: the actual bill page on the state legislature site. Tracker citation (for the count) goes to a tracker org.

**d. Multi-state trackers**
- Identify 2-4 reputable trackers covering this topic.
- Strong candidates: Littler, Bryan Cave Leighton Paisner, K&L Gates, Multistate.ai, Bloomberg Law, NCSL (caveat — NCSL has been less reliably updated for AI legislation since 2024; check before citing).
- Capture: org name, tracker title, URL, update cadence, brief description of what makes the tracker useful.

**e. Recent reporting**
- 3-5 articles on enacted laws (within the last 6 months preferred).
- 1-3 articles on pending bills (within the last 3 months preferred).
- Capture: source name (firm or publication), date, title, URL, one-sentence "why this is worth reading" framing.

### 4. Apply the source policy at writeup time

For every statement in the research note, classify it as Bucket A (primary-source-only) or Bucket B (secondary-source-welcome) per `references/source-policies.md`. Reject any Bucket A claim that lacks a primary citation. If you can't find one, that's a signal that the claim is wrong, oversimplified, or you're confusing two regimes.

Common failure modes:
- Citing a law firm summary for a "the statute requires X" statement → fix by going to the statute.
- Citing the bill number when you mean the codified statute → for enacted laws, prefer the codified citation (e.g., "775 ILCS 5/2-102(L)") over the bill ("HB 3773").
- Linking to a state legislature's "bill page" when the public act / final text is what's load-bearing → link to the public act / final text.

### 5. Produce the research note

Save the output as a single markdown file. Use this exact structure:

```markdown
# [Topic] — US Employment Law Research

**Scope:** [topic, jurisdictions covered, recency window]
**Compiled:** [date]
**Audience:** [practitioner / executive / general]

## Federal layer
[Statutes / regs / EOs / agency guidance / pending federal action]
[Primary citations]

## Enacted laws by jurisdiction
For each jurisdiction (in alpha order, or grouped state/city):

### [Jurisdiction name]
- **Law:** [Codified citation; bill number in parens if helpful]
- **Effective date:**
- **Covered employers:**
- **Key obligations:** [notice / audit / disparate impact / anti-discrimination / etc.]
- **Enforcement:** [agency, private right of action, penalties, cure period]
- **Citations:** [primary sources only]

## Pending bills
- **Approximate count:** [N states] (cite tracker)
- **Notable pending bills:**
  - [Bill] — [State] — [status] — [link]

## Multi-state trackers
- **[Org name]** — [tracker title] — [URL] — [update cadence] — [why useful]
- ... 2-4 entries

## Recent reporting
### Enacted laws
- **[Source]** — [date] — [title] — [URL] — [one-sentence framing]
- ... 3-5 entries

### Pending bills
- **[Source]** — [date] — [title] — [URL] — [one-sentence framing]
- ... 1-3 entries

## Open questions / things to watch
[Items the user may want to monitor; uncertainties; unresolved interpretations]
```

### 6. Hand off

Save the file in the user's workspace folder so they can read it and refer back. If this research is feeding into a dashboard, point the user to the `employment-law-dashboard` skill as the next step and tell them where you saved the research note.

## Notes on common pitfalls

- **Don't conflate bill and statute.** A state legislature page for HB ###### is fine for tracking pending bills, but for an enacted law the codified citation (e.g., "775 ILCS 5/2-102(L)") is what attorneys actually cite. Find both; lead with the statute.
- **Watch for stale "draft" or "proposed" rules.** Many states publish draft regulations months before final adoption. Always note the status (draft vs final) and the effective date.
- **Federal preemption attempts ≠ federal preemption.** A federal executive order or pending bill that *attempts* to preempt state law isn't actually preempting until courts say so. Be careful with framing.
- **City laws matter.** NYC LL 144 is a city law, not a state law, and it's been a major part of the AI hiring landscape. Don't filter to "state only" by default.
