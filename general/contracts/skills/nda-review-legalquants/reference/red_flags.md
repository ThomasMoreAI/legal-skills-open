# Red Flags and Operational Issues

This reference drives Pass 4 of the NDA review. These are issues to flag *whenever they appear*, regardless of perspective, because they create operational risk, suggest the counterparty is using the NDA for purposes beyond confidentiality protection, or signal that the document was drafted from a template inappropriate for the deal.

A red flag is not necessarily a deal-breaker. Many of these are negotiable or acceptable in context. But every red flag deserves explicit treatment in the review report so the user can make a deliberate business judgment.

## Provisions That Should Not Be in a Standard NDA

The following provisions belong in other agreements, not in NDAs. When they appear, the document is functioning as something more than a confidentiality agreement, and the user should treat it accordingly.

### Indemnification

NDAs should not contain indemnification obligations. Standard NDA remedies are damages and equitable relief; indemnification expands that to third-party liability, defense costs, and (often) gross-disproportion to actual breach. When indemnification appears in an NDA, flag as material and ask: what is the indemnification protecting against, and is that risk something the user is prepared to underwrite?

Common variants:
- Mutual indemnification for "any breach of this agreement" — flag as material; turns standard breach exposure into a magnified risk.
- One-sided indemnification (user must indemnify counterparty) — flag as critical from user perspective.
- Indemnification for IP infringement — flag as material and out of scope; this belongs in a license or services agreement.

### IP Assignment

NDAs should not transfer intellectual property. When clauses purport to assign work product, feedback, derivatives, or improvements, the document is functioning as an IP transfer. Common patterns:

- "Any feedback provided by the recipient becomes the property of the discloser" — common in product-evaluation NDAs from vendors. Flag as material from recipient perspective; recipient is being asked to give up IP rights as a condition of evaluating a product.
- Assignment of "derivatives" of confidential information — flag as critical; turns the NDA into a broad IP grab.
- "Improvements" assignment — flag as critical for the same reason.

When IP assignment appears, the user needs to decide whether the deal contemplates IP transfer (and if so, the right document is a license or services agreement, not an NDA).

### Non-Solicitation

Non-solicitation clauses ("you will not solicit our employees / customers / vendors") inside NDAs are common but problematic for two reasons:

1. **Enforceability concerns.** Non-solicits face heightened scrutiny in many jurisdictions. California voids most employee non-solicits as restraints on trade. Other jurisdictions evaluate reasonableness, scope, and consideration.
2. **Misuse of NDA as trade restraint.** The recipient signed up for confidentiality protection, not for restraints on hiring or business development. Buried non-solicits expand the recipient's obligations beyond what was bargained for.

Always flag whenever present. Severity depends on:
- Scope (employees only? customers? vendors?).
- Duration (matched to NDA term, or longer?).
- Jurisdiction (governing-law-dependent enforceability).
- User's organizational exposure (is the recipient likely to interact with the discloser's employees or customers in the ordinary course?).

### Non-Competition

Non-competition clauses inside NDAs are a critical-issue red flag, full stop. Non-competes face the most aggressive enforceability review of any restrictive covenant; many jurisdictions (California, Minnesota, Oklahoma, North Dakota; increasingly others) void them outside specific contexts. Inside an NDA — where there is typically no consideration beyond access to the confidential information — they are particularly vulnerable.

Always flag as critical whenever present in a non-M&A NDA. In an M&A context (where the NDA is part of pre-closing diligence), non-competes are more common and more defensible, but still warrant explicit user review.

### Non-Circumvention

"Non-circumvention" clauses originate in deal-broker contexts (e.g., introducer-broker arrangements) and are usually vague. They typically prohibit the recipient from "going around" the discloser to deal directly with the discloser's customers, partners, or sources. Problems:

- Often vague enough to create operational restrictions the recipient did not bargain for.
- Frequently overlap with non-solicit obligations, creating compounding restraint.
- Unusual in a standard commercial NDA; their presence suggests the document was drafted from a deal-broker template.

Flag whenever present. Severity is contextual but usually material.

### No-Hire

"No-hire" clauses (recipient may not hire discloser's employees, even those who approach recipient unsolicited) are stricter than non-solicits. Increasingly disfavored:

- Several jurisdictions void them outright.
- The Department of Justice has prosecuted no-hire agreements as antitrust violations (no-hire pacts among competitors).
- Inside an NDA, often unrelated to the confidentiality purpose.

Flag as material whenever present.

## Asymmetric Damages and Remedy Provisions

### Liquidated Damages

NDAs rarely include liquidated damages clauses; their presence is unusual. When they appear:
- Per-incident dollar amounts (e.g., "$50,000 per disclosure") — flag as material.
- Multipliers on actual damages (e.g., "treble damages") — flag as material.
- Liquidated damages combined with equitable relief and full damages — flag as critical (compounding).

### Limitation of Liability Asymmetry

Some NDAs include limitation-of-liability provisions that limit the recipient's exposure but not the discloser's, or vice versa. Asymmetric LoL in an NDA is a flag — the document is doing more than confidentiality work.

### Consequential Damages

NDAs sometimes exclude consequential damages, sometimes preserve them, and sometimes do both for one party but not the other. Asymmetric treatment of consequential damages is a flag.

## Restrictions Beyond Confidentiality

### Non-Disparagement

"Non-disparagement" clauses prohibit the parties from making negative statements about each other. These are appropriate in settlement agreements and some employment contexts, but out of place in a standard NDA. They restrict speech beyond the confidentiality purpose. Flag whenever present.

### Publicity Restrictions

Some NDAs prohibit either party from disclosing the existence of the conversation or the relationship. This is sometimes appropriate (early M&A discussions, sensitive deals) and sometimes overreach.

- Flag whenever present.
- Check whether mutual or one-sided.
- Check whether time-limited or permanent.
- Check whether the restriction extends beyond reasonable need (e.g., "you may not list us on your customer page even if the deal closes").

### Non-Disclosure of NDA Terms

Some NDAs include a clause stating that the terms of the NDA itself are confidential. This can be reasonable but creates compliance complexity (recipient cannot circulate the NDA internally for review without violating it). Flag and ensure permitted-disclosure exceptions cover internal review.

### Audit Rights

Audit rights (one party may audit the other's compliance with the NDA) are common in regulated-data contexts (HIPAA-adjacent NDAs, financial-information NDAs). In standard commercial NDAs, audit rights are unusual. When present:

- Flag and assess proportionality.
- Check scope (records related to confidential information vs broader business records).
- Check frequency (how often can auditor audit?).
- Check who pays (auditor's costs typically).
- Check confidentiality of audit results.

## Drafting Indicators That Warrant Caution

These are not red-flag provisions but indicators that the document may have problems beyond the issues already enumerated.

### Unusual Length

Standard commercial NDAs run 2–5 pages. NDAs over 8 pages typically contain non-standard provisions. NDAs over 15 pages are functioning as something more than NDAs (often diligence agreements, evaluation agreements, or framework agreements with confidentiality components). When length exceeds 8 pages, conduct an extra pass to identify what additional provisions are present.

### Definitions Section Larger Than Operative Provisions

When the definitions section consumes more than ~25% of the document, the document is using definitions to import substantive obligations. Read the definitions especially carefully — substantive recipient obligations are sometimes hidden inside definitions of "Permitted Use," "Confidential Information," or "Affiliate."

### Repeated Cross-References

When operative provisions cross-reference other sections heavily, the substance is hard to evaluate clause-by-clause. This is sometimes legitimate (well-drafted complex agreements use cross-references), but in NDAs it often signals retrofit or layering. Read affected provisions in conjunction.

### Heavy Use of "Notwithstanding," "Subject To," and "Provided That"

These conjunctions create exceptions and carveouts that can swallow rules. When a provision contains multiple "notwithstanding" or "provided that" clauses, parse them carefully — the operative effect may be the opposite of the surface read.

### Misapplied Templates

Some NDAs are clearly drafted from templates intended for different deal types:

- M&A NDA being used for a vendor evaluation (often has standstill provisions, deal-protection language, and aggressive non-solicit/non-circumvention).
- Employment NDA being used for a commercial relationship (often has IP assignment, work-product language).
- Government-contractor NDA being used for a private deal (often has classification language, security-clearance provisions).

When the document feels like it's about something other than the actual deal, flag the template misalignment in "Items requiring human judgment."

## Conflicts with Existing Agreements

If the user provided a `prior_agreements` input identifying existing agreements between the parties (an existing MSA, a prior NDA, an SOW), check the document for:

- Express references to the named prior agreements (and whether the references are accurate).
- Integration / entire-agreement clauses that purport to override prior agreements (this can extinguish prior protections).
- Term provisions that don't account for existing relationships.
- Provisions that conflict with specific terms the user mentioned in the prior agreement.

Flag any potential conflicts in the report. If `prior_agreements` was not provided, this check is skipped — do not speculate about agreements the user did not mention.

## When in Doubt

When a provision creates risk that the skill is uncertain about — unfamiliar jurisdiction-specific issues, novel deal structures, unusual regulatory contexts — surface it in the "Items requiring human judgment" section of the report rather than producing potentially-wrong analysis. The skill's job is to surface issues for the user's judgment, not to substitute for it.
