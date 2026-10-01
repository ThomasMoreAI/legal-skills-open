---
name: prompt-pack-social-media-knowledge-content-prompt-sboghossian
title: Social Media / Knowledge Content Prompt
description: Use when a law firm, legal team, or lawyer needs to create accessible knowledge content for professional social media channels (LinkedIn, X/Twitter) explaining a legal or tax topic to a non-specialist audience. Produces a structured content brief and draft thread or post that translates legal complexity into plain-language explanations with concrete examples, without crossing into unauthorized legal advice. Particularly useful for MENA-facing law firms building their thought-leadership presence.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-social-media-knowledge-content-prompt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: general
language: en
---

# Social Media / Knowledge Content Prompt

## When to use this

Use this skill when a lawyer, law firm, or legal content team needs to:
- Translate a new law, regulatory change, or legal concept into an accessible LinkedIn or X/Twitter thread for clients, business professionals, or the public.
- Create thought-leadership content that demonstrates expertise without providing individualized legal advice.
- Explain a jurisdiction-specific legal issue (UAE corporate tax, Saudi labour reform, DIFC employment law update) in a format that clients and prospects will actually read.
- Prepare content for a firm newsletter, website, or knowledge hub in a social-media-friendly format.

**Key constraint:** Social media legal content must be educational, not advisory. The content explains a legal framework or concept; it does not constitute legal advice for any specific situation. A disclaimer must be included.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Topic or legal issue** | The core of the post | Ask; the more specific the better ("UAE Corporate Tax impact on free zone companies" beats "UAE tax") |
| **Target audience** | General public / business owners / in-house lawyers / CFOs | Ask; determines language complexity and which aspects to emphasize |
| **Platform** | LinkedIn (long-form, professional) vs. X/Twitter (short threads) vs. both | Default: LinkedIn primary, X/Twitter thread as secondary |
| **Jurisdiction focus** | Ensures accuracy for local rules | Ask; default to UAE if MENA context |
| **Firm tone / voice** | Authoritative but accessible; some firms prefer formal; others conversational | Ask; default: professional and approachable |

## Optional inputs

- **Recent trigger event** — a new law published in the Official Gazette, a regulatory announcement, a court decision; timely content performs better.
- **Case study or example** — concrete examples dramatically improve engagement; if a (sanitized) client scenario is available, use it.
- **Word count / post length target** — LinkedIn allows up to 3,000 characters; a LinkedIn article allows more; specify.
- **Images or infographic brief** — if a visual (flowchart, comparison table) is to accompany the text, describe the visual concept.
- **Call to action** — "contact us for a consultation," "download our guide," "subscribe to our newsletter," etc.

## Content structure

### LinkedIn post / thread structure

1. **Hook (first 2 lines)** — must stop the scroll. LinkedIn truncates posts after ~200 characters; the first sentence must compel the reader to click "see more." Use a question, a striking statistic, or a bold statement.
   - Example: "Did you know that UAE companies operating in free zones may still owe corporate tax under the new UAE CT Law? Here's what every CFO needs to know in 5 key points."

2. **The 3-5 key points** — the substance of the post. Each point should:
   - Be a single, digestible idea.
   - Use plain language; avoid legal jargon without explanation.
   - Be accurate; do not oversimplify to the point of misleading.
   - Be specific to the jurisdiction stated.
   - Include a concrete example where possible.

3. **Common misconception (optional but high-value)** — address one thing that most people get wrong about this topic. This builds credibility and generates engagement ("Actually, I thought...").

4. **Practical takeaway** — the one thing the reader should do or know after reading. "If you are a [type of entity], you should [action] before [deadline]."

5. **Disclaimer** — short and standard:
   - "This post is for educational purposes only and does not constitute legal or tax advice. Consult a qualified professional for advice specific to your situation."

6. **Call to action** (optional) — one, specific: "Follow for more UAE law updates" / "Comment if you have questions" / "DM us to discuss your situation."

### X/Twitter thread structure

1. **Thread opener tweet** — the thesis in one sentence; include a numbered hook: "🧵 UAE Corporate Tax: 5 things every free zone company must know. A thread."
2. **Tweets 2–6** — one point per tweet; keep each under 280 characters; use line breaks for readability.
3. **Tweet 7** — common mistake or misconception.
4. **Tweet 8** — practical takeaway + disclaimer.
5. **Final tweet** — follow/share prompt.

## Quality standards for legal knowledge content

### Accuracy
- Every legal statement must be verifiable against the applicable law or regulation.
- Do not state specific article numbers or citation-level precision in a social post unless you are certain of accuracy — a widely shared post with a wrong citation damages credibility.
- Qualify where the law is evolving: "as of [date]" or "implementing regulations are pending."
- When covering MENA law, check whether the Arabic-language text of the regulation has been considered (English summaries of UAE/KSA laws are sometimes incomplete or behind).

### Accessibility
- Write at a reading level accessible to a senior businessperson, not a lawyer.
- Define any term that a non-lawyer might not know (e.g., "beneficial owner (the person who ultimately owns or controls the company)").
- Use numbers, bullet points, and emoji (where platform/firm tone allows) to break up text.
- Avoid Latin or archaic legal terms entirely in social posts.

### Jurisdictional honesty
- If the post covers a specific jurisdiction, say so clearly at the outset: "This applies to UAE mainland companies."
- Do not universalize a MENA rule as if it applies everywhere; different jurisdictions treat the same issue differently.
- Flag if the rule covered has DIFC/ADGM exceptions (common for corporate and employment law topics).

### Tone calibration by platform
- **LinkedIn:** Professional, first-person, substantive. Law firms with a strong partner brand should write from the partner's perspective ("In my experience advising..."). Generic firm accounts should use "our team" or "we advise."
- **X/Twitter:** More conversational; shorter sentences; more direct. Use numbered lists ("1/ ... 2/ ... 3/ ...").

## Examples

### Good LinkedIn opener
"The UAE Corporate Tax Law is now in effect — and free zone entities may not be as protected as they think. Here are 5 rules that could catch your CFO by surprise."

### Weak LinkedIn opener
"We are pleased to share this update on the UAE Corporate Tax Law which came into effect following the issuance of Federal Decree-Law No. 47 of 2022."

### Good key point
"2/ If a free zone entity earns income from a UAE mainland customer, that income may be subject to the 9% CT rate — even if the company has a free zone license. The law distinguishes between 'qualifying income' and non-qualifying income."

### Weak key point
"The law provides for a 0% rate for qualifying free zone persons in respect of qualifying income as defined in Article 18 of the CT Law and related guidance."

The good version explains; the weak version cites.

## Compliance and ethical considerations

- Social media legal content is **not legal advice.** Include a disclaimer every time, without exception.
- Do not reference specific clients or matters; anonymize any examples.
- Bar association advertising rules vary by jurisdiction; some require disclaimers beyond the standard "not legal advice" caveat:
  - UAE: DIFC and onshore UAE legal practice regulations apply to law firm advertising; avoid any language that could be construed as guaranteeing outcomes.
  - KSA: Saudi Ministry of Justice has specific rules on lawyer advertising; check current rules before publishing.
  - UK: SRA Transparency Rules require certain disclosures by regulated firms.
- Do not create content that could be construed as legal advice to a specific person based on the comments and replies it generates; have a process for redirecting specific inquiries to a consultation.

## Common mistakes

- **Too long for the platform.** A 2,000-word LinkedIn post will not be read; aim for 300–600 words for a post; longer is appropriate for a LinkedIn article.
- **No hook.** Posts that start with "We are pleased to announce..." or "As many of you know..." fail to capture attention.
- **Citing article numbers without context.** A post that says "per Art. 18(1)(a)(ii)" is inaccessible; explain the rule in plain English and cite the article only if it adds credibility.
- **Missing disclaimer.** Every piece of legal knowledge content must carry a disclaimer; omitting it creates professional liability exposure.
- **No call to action.** Knowledge content that does not tell the reader what to do next is a missed opportunity.

## Related skills

- [[prompt-pack-professional-email-draft]]
- [[prompt-pack-regulatory-change-impact-assessment]]
- [[heuristic-always-state-jurisdiction-first]]
