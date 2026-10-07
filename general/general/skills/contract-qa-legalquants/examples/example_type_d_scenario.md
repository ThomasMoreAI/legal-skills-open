# Worked Example — Type D: Scenario

This example demonstrates Contract QA tracing a hypothetical scenario through the contract's controlling provisions. The user wants to know what would happen under specified facts; the answer follows the chain of clauses that operate.

## Input

**Document:** SaaS Master Services Agreement (12-page MSA)

**Question:** "What happens if we miss the renewal notice deadline by a few days?"

**Optional inputs:**
- contract_type: "MSA-SaaS"
- perspective: "our_side" (customer)
- jurisdiction: "Delaware"
- prior_context: "We discussed the renewal mechanism earlier; I'm now asking about consequences of missing the deadline."

**Relevant contract excerpts:**

> **§13.2 Renewal.** Upon expiration of the Initial Term, this Agreement shall automatically renew for successive one (1)-year periods (each, a "Renewal Term"), unless either party provides written notice of non-renewal to the other party at least sixty (60) days prior to the end of the then-current term.
>
> **§13.4 Notice.** All notices required under this Agreement shall be in writing and shall be deemed delivered when sent by certified mail, return receipt requested, or by a nationally recognized overnight courier, in each case addressed to the recipient at the address set forth on the signature page (or such updated address as a party may designate by notice given pursuant to this Section).
>
> **§13.5 No Cure Periods for Renewal Notices.** The notice period set forth in Section 13.2 is strict; failure to provide timely notice of non-renewal results in automatic renewal as set forth in Section 13.2, and no cure period applies to such failure.
>
> **§13.6 Termination for Convenience During Renewal Term.** Customer may terminate this Agreement during a Renewal Term for convenience, upon at least one hundred eighty (180) days' prior written notice, provided that Customer shall pay Vendor an early-termination fee equal to fifty percent (50%) of the fees that would have been payable for the remainder of the Renewal Term.

## Question classification

Type D — Scenario. The user is asking what happens under a specific factual scenario (missing the renewal deadline by a few days). The answer traces the chain of clauses that operate.

The `prior_context` input establishes that the user has the renewal mechanism in mind already — so the answer doesn't need to re-establish it; it can focus on the consequence of missing.

## Output

**If you miss the 60-day notice deadline by even one day, the Agreement auto-renews for another year. There is no cure period and no equitable workaround in the contract; your only contractual exit is termination for convenience during the Renewal Term, which carries a substantial early-termination fee.**

The controlling provisions:

- **§13.2 Renewal.** Sets the 60-day notice period and the auto-renewal default. The deadline is calculated from the end of the then-current term.

  > "Upon expiration of the Initial Term, this Agreement shall automatically renew for successive one (1)-year periods (each, a 'Renewal Term'), unless either party provides written notice of non-renewal to the other party at least sixty (60) days prior to the end of the then-current term."

  [§13.2]

- **§13.4 Notice.** Specifies how notice must be delivered (certified mail or overnight courier). Email or in-app notice does not satisfy the formal notice requirement; if the user attempted to give notice via email, that notice is invalid regardless of timing.

  > "All notices required under this Agreement shall be in writing and shall be deemed delivered when sent by certified mail, return receipt requested, or by a nationally recognized overnight courier..."

  [§13.4]

- **§13.5 No cure for renewal notices.** Forecloses the most common workaround. In some contracts, missed notice deadlines have an implicit grace period or cure right; this contract explicitly removes that.

  > "The notice period set forth in Section 13.2 is strict; failure to provide timely notice of non-renewal results in automatic renewal as set forth in Section 13.2, and no cure period applies to such failure."

  [§13.5]

- **§13.6 Convenience termination during renewal.** Provides the only contractual exit once auto-renewal occurs.

  > "Customer may terminate this Agreement during a Renewal Term for convenience, upon at least one hundred eighty (180) days' prior written notice, provided that Customer shall pay Vendor an early-termination fee equal to fifty percent (50%) of the fees that would have been payable for the remainder of the Renewal Term."

  [§13.6]

The chain of consequence: missing the notice deadline triggers auto-renewal under §13.2; §13.5 forecloses any cure; §13.6 provides the only exit, but at substantial cost. If you discover the missed deadline immediately and the auto-renewal has just attached, the early-termination fee is calculated against twelve months of fees, with 180 days' notice required — meaning you pay the fee and continue paying through the notice period.

A practical workaround, which is not in the contract but exists in industry practice: contact the vendor directly and ask them to accept late notice or to mutually rescind the auto-renewal. Vendors sometimes accommodate this — particularly if the customer is in good standing and the vendor wants to preserve the relationship. Whether this works depends on the vendor's posture, not the contract.

**If you have already missed the deadline, recommend:**
1. Reach out to the vendor immediately and request mutual rescission of the auto-renewal. Frame it as a mistake rather than a tactical maneuver.
2. If the vendor declines, evaluate whether the early-termination fee plus the 180-day notice period is acceptable, versus running out the renewal term.
3. Calendar the next renewal deadline now — well in advance of 60 days — to prevent a recurrence.

**If you have not yet missed the deadline:**
- Calendar the deadline at multiple points (90 days out, 75 days out, 65 days out) to ensure timely action.
- Confirm the notice delivery method (certified mail or overnight courier) and obtain delivery confirmation.

The skill cannot determine whether equitable relief would be available under Delaware law for a one-day-missed notice deadline. Delaware courts generally enforce strict notice provisions in commercial contracts; equitable relief is theoretically available for unconscionable enforcement but rare. For an enforceability opinion specific to your facts, recommend a research query.

---

## What this example demonstrates

- **Direct answer in the first paragraph.** "If you miss the 60-day notice deadline by even one day, the Agreement auto-renews..." The user asked what happens; the first paragraph answers.
- **Chain of consequence is traced explicitly.** Each operative clause is named, quoted, and connected to the next. The user can follow the logic without re-reading the contract.
- **Each clause has its own bullet with quote and citation.** The structured format makes the chain easy to follow. A wall of prose would obscure the logic.
- **Contract-only answer is distinguished from out-of-contract reality.** The "practical workaround" paragraph clearly notes that it's industry practice, not contract language. The user knows what's enforceable vs. what's negotiable.
- **Recommendations are split by user's actual situation.** "If you have already missed" vs. "If you have not yet missed" — the user gets the recommendation that applies to them, not a generic list.
- **Out-of-scope question explicitly routed.** The Delaware enforceability question is acknowledged and routed to research. The skill does not opine.
- **`prior_context` was honored.** The answer does not re-explain the renewal mechanism (which the user said they already knew); it goes directly to consequences. If `prior_context` had not been provided, the answer would have included a brief recap of the renewal mechanism before the consequences.
- **Did not invent a cure period or wishful workaround.** Section 13.5 explicitly forecloses cure periods; the answer respects that and does not pad with "but maybe you can argue..." speculation. If the contract is clear, the answer is clear.
