# Worked Example — Type C: Comparison / Unusualness

This example demonstrates Contract QA answering a comparison question with perspective calibration. The user wants to know whether a clause is unusual; the answer requires placing the clause in context against typical practice for the contract type.

## Input

**Document:** SaaS Master Services Agreement (12-page MSA, vendor-prepared, presented to customer for signature)

**Question:** "Is this limitation of liability clause unusual?"

**Optional inputs:**
- contract_type: "MSA-SaaS"
- perspective: "our_side" (customer)
- jurisdiction: "Delaware"
- prior_context: not provided

**Relevant contract excerpt:**

> **§10.1 Limitation of Liability.** EXCEPT FOR LIABILITY ARISING FROM A PARTY'S BREACH OF SECTION 6 (CONFIDENTIALITY) OR SECTION 8 (INDEMNIFICATION), IN NO EVENT SHALL EITHER PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO THIS AGREEMENT EXCEED THE AMOUNTS PAID OR PAYABLE BY CUSTOMER TO VENDOR DURING THE THREE (3)-MONTH PERIOD IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO LIABILITY.
>
> **§10.2 Exclusion of Damages.** IN NO EVENT SHALL EITHER PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, EXEMPLARY, OR PUNITIVE DAMAGES, INCLUDING LOSS OF PROFITS, REVENUE, DATA, OR BUSINESS OPPORTUNITY, WHETHER ARISING UNDER CONTRACT, TORT, OR ANY OTHER THEORY OF LIABILITY.

## Question classification

Type C — Comparison / unusualness. The question explicitly asks whether the clause is "unusual," which is the core Type C signal. Perspective is provided (customer), so the answer can be calibrated.

## Output

**Yes, this limitation of liability is aggressive against the customer side, primarily because of the three-month cap. Standard SaaS MSAs cap liability at fees paid in the prior twelve months; a three-month cap is materially below market.**

The relevant clauses:

> "EXCEPT FOR LIABILITY ARISING FROM A PARTY'S BREACH OF SECTION 6 (CONFIDENTIALITY) OR SECTION 8 (INDEMNIFICATION), IN NO EVENT SHALL EITHER PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATING TO THIS AGREEMENT EXCEED THE AMOUNTS PAID OR PAYABLE BY CUSTOMER TO VENDOR DURING THE THREE (3)-MONTH PERIOD IMMEDIATELY PRECEDING THE EVENT GIVING RISE TO LIABILITY."

[§10.1]

> "IN NO EVENT SHALL EITHER PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, CONSEQUENTIAL, SPECIAL, EXEMPLARY, OR PUNITIVE DAMAGES..."

[§10.2]

The structure is conventional — mutual cap with carve-outs for confidentiality and indemnification, plus a consequential-damages waiver — but the cap amount is the issue.

For SaaS MSAs, typical liability caps run from "fees paid in the prior twelve months" (most common) to "total fees paid under the agreement" (vendor-favorable but still within market) to "fees payable in the next twelve months" (customer-favorable in growth scenarios). A three-month cap is well below all of these, and on annual contracts it means the practical cap is roughly 25% of annual fees — barely enough to cover a single material outage or service failure.

The cap is also identically structured for both parties, but the practical asymmetry is large: the vendor's liability is what the customer might recover from the vendor; the customer's liability is what the vendor might recover from the customer (typically just unpaid fees). A three-month cap shrinks vendor exposure dramatically while having little effect on customer exposure. In a mutual cap structure, that's customer-unfavorable.

The carve-outs (confidentiality, indemnification) are standard. The skill notes that *gross negligence* and *willful misconduct* are not carved out — these are increasingly standard carve-outs in SaaS MSAs and their absence is a separate flag, especially in a cap this low.

**For your side (customer), recommend:**
- Negotiate the cap up to fees paid in the prior twelve months at minimum.
- Request a carve-out for gross negligence and willful misconduct.
- Consider whether super-cap protections are needed for specific high-stakes scenarios (data breach, regulatory violations) — supercaps of 2x or 3x the base cap are common for these categories.

The contract's enforceability of the cap in Delaware is a separate question; Delaware generally enforces commercial liability caps between sophisticated parties subject to unconscionability review. For this clause, enforceability is unlikely to be a real concern; the issue is commercial reasonableness, which is what the negotiation should focus on.

---

## What this example demonstrates

- **Direct verdict in the first sentence.** "Yes, this limitation of liability is aggressive against the customer side." The user asked is-this-unusual; the first sentence answers.
- **Severity is calibrated to the magnitude of deviation.** The cap is quantitatively below market (3 months vs. 12 months standard), so the verdict is "aggressive," not just "unusual." If the cap were 9 months instead of 3, the verdict would be "below market but not extreme."
- **Perspective is applied throughout.** The discussion of practical asymmetry (vendor exposure shrinks more than customer exposure) is a customer-perspective observation. From the vendor's perspective, this clause is a strength.
- **Comparative context is concrete.** "Typical SaaS MSAs cap at fees paid in the prior twelve months" is a specific reference point, not a vague "this is unusual." The user can verify the comparison against their own deal experience.
- **Surfaced a related issue not directly asked about.** The missing gross-negligence carve-out is flagged because it's relevant to the user's interest in this section, even though the user asked specifically about the cap. This is the "name the implicit" move from skill creation, applied to Q&A.
- **Closing recommendations are operational.** "Negotiate up to twelve months" is something the user can do. "Consider supercaps" is a specific structural option, not vague advice.
- **Enforceability is briefly addressed and routed.** The user mentioned Delaware governing law, so the answer notes that the cap's enforceability is unlikely to be a real concern under Delaware law — but explicitly does not give a definitive enforceability opinion. Stays in scope.
- **Did not turn into a full review.** The clause was assessed; surrounding clauses were not. The user asked a Type C question; they got a Type C answer. If they want a full review, the appropriate route is the MSA-SaaS Review skill.
