# QC Checklists

## Standard Checklist (all deliverable types)

### Core (used in Quick depth)
1. **Factual claims sourced** — Every factual claim traces to a named source. No orphan claims.
2. **Numbers verified** — Every figure cross-checked against its source. If two sources disagree, both shown.
3. **Logic coherent** — Conclusions follow from premises. No gaps, no non-sequiturs.
4. **Completeness** — Does it answer what was asked? Any obvious omissions?
5. **Cringe test** — Would a domain expert read this and nod, or wince?

### Extended (added in Standard depth)
6. **Vague language** — Flag "significant", "considerable", "various" without specifics.
7. **Consistency** — Same terms/numbers/classifications used throughout. No contradictions.
8. **Source methodology** — Right type of source for each claim? Published schedules ≠ live status. Press releases ≠ financial data.
9. **Attribution** — Every quote, data point, or borrowed idea attributed.
10. **Formatting** — Consistent structure, no orphan headers, no broken references.
11. **Actionability** — If it recommends actions, are they specific enough to execute?
12. **Scope creep** — Does it stay within the requested scope or drift into unrequested territory?

### Deep (added in Deep depth)
13. **Source re-verification** — Go back to at least 3 key claims and re-fetch the source. Did the original check get it right?
14. **Adversarial read** — Read as someone who wants to prove this is wrong. What's the weakest point?
15. **Staleness** — Any data that might have changed since it was gathered? Flag with dates.
16. **Hedging audit** — Is uncertainty properly communicated? Overconfident claims are worse than honest uncertainty.
17. **Recipient test** — Imagine the specific person receiving this. What would they question first?

## Type-Specific Additions

### Reports & Analysis
- Executive summary matches body content (no unsupported claims in summary)
- Data visualizations match underlying data
- Recommendations ranked by evidence strength

### Scripts & Code
- All file paths exist and are accessible
- Dependencies listed and available
- Error handling present (what happens when something fails?)
- Idempotency — safe to run twice?
- Rollback mechanism if applicable

### Legal Documents
- Jurisdiction specified and consistent
- Defined terms used consistently after definition
- Cross-references point to correct sections
- No conflicting obligations
- Governing law and dispute resolution clause present

### Plans & Proposals
- Timeline realistic (not just optimistic)
- Dependencies identified
- Cost estimates sourced or methodology explained
- Risk section present and honest
- Success criteria defined and measurable

### Emails & Communications
- Tone appropriate for recipient
- No ambiguous commitments
- Call to action clear
- Reply-to and CC list correct
- Nothing that shouldn't be in writing
