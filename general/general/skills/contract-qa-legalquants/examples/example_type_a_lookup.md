# Worked Example — Type A: Direct Lookup

This example demonstrates Contract QA handling a direct lookup question. The user wants a fact; the answer is brief, cited, and does not pad.

## Input

**Document:** Software Subscription Agreement (15-page MSA between SaaS vendor and customer)

**Question:** "What's the term of this agreement and how does renewal work?"

**Optional inputs:**
- contract_type: "MSA-SaaS"
- perspective: "our_side" (customer)
- jurisdiction: not provided
- prior_context: not provided

**Relevant contract excerpt (for the example):**

> **§13.1 Term.** This Agreement commences on the Effective Date and continues for an initial term of two (2) years (the "Initial Term"), unless earlier terminated in accordance with Section 13.2 or 13.3.
>
> **§13.2 Renewal.** Upon expiration of the Initial Term, this Agreement shall automatically renew for successive one (1)-year periods (each, a "Renewal Term"), unless either party provides written notice of non-renewal to the other party at least sixty (60) days prior to the end of the then-current term.

## Question classification

The question is mixed — partly Type A (what's the term) and partly Type B/D (how renewal works, which is interpretation/scenario). Apply the merger rule: when types mix, pick the more demanding format that subsumes the simpler one. Here, the user wants both the fact and the operational explanation; Type B (interpretation) is the right format.

But the answer can be expressed compactly because the renewal mechanism is simple. Use a hybrid: lead with the term (Type A response), then add the renewal mechanics (Type B response).

## Output

The initial term is two years from the Effective Date, with automatic one-year renewals unless either party gives at least sixty days' written notice of non-renewal before the end of the then-current term [§13.1, §13.2].

The relevant clauses:

> "This Agreement commences on the Effective Date and continues for an initial term of two (2) years (the 'Initial Term'), unless earlier terminated in accordance with Section 13.2 or 13.3."

[§13.1]

> "Upon expiration of the Initial Term, this Agreement shall automatically renew for successive one (1)-year periods (each, a 'Renewal Term'), unless either party provides written notice of non-renewal to the other party at least sixty (60) days prior to the end of the then-current term."

[§13.2]

The mechanism is auto-renewal with opt-out, not opt-in renewal. Practical implication: if you want to avoid an unwanted renewal, calendar the 60-day deadline relative to your current term's expiration. Missing the deadline locks in another year.

---

## What this example demonstrates

- **Direct answer first.** The first sentence answers the user's question completely. Citations support the answer; they do not lead.
- **Verbatim quotes are exact.** Both quotes preserve the contract's original capitalization, parenthetical numerals, and quote marks around defined terms.
- **Citations are placed naturally.** Inline citations at end of summary sentence; standalone citations after each block quote.
- **The closing paragraph is operational, not legal commentary.** It tells the user what to *do* with the answer (calendar the deadline). This is appropriate for a Type A/B answer where the user has practical follow-up; it's not lecturing.
- **Length is proportional.** The contract has a clean, simple renewal mechanism; the answer is short. A more complex renewal (multiple notice periods, conditions, reset triggers) would warrant more explanation. Don't pad.
- **Perspective is used implicitly.** The closing paragraph addresses "you" — the customer (the user's stated perspective). For a counterparty perspective, the closing would have noted the same calendar concern from the vendor's side ("your auto-renewal is a revenue lock-in; the customer can opt out only with 60 days' notice").
- **Did not invent or speculate.** No discussion of whether 60 days is "standard" (that would be a Type C answer, not asked); no speculation about what jurisdictions might affect enforceability. Stayed in scope.
