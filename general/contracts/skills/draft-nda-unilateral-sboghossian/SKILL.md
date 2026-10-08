---
name: draft-nda-unilateral-sboghossian
title: Unilateral NDA (One-Way Confidentiality Agreement)
description: Use when drafting a unilateral (one-way) NDA where only one party is the Discloser and the other is the Recipient bearing all confidentiality obligations. Covers asymmetric obligation structure, narrower carve-outs, stronger IP ownership clauses, explicit injunctive-relief language, and longer default term. Common scenarios include investor pitch sharing, vendor receiving customer data, and employee-trade-secret situations. Triggers on "unilateral nda", "one-way nda", "one-sided nda", or "disclosure agreement" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-nda-unilateral
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Unilateral NDA (One-Way Confidentiality Agreement)

## When to use this

A unilateral NDA is appropriate when the confidential information flows in one direction only: the Discloser shares sensitive information with the Recipient, and only the Recipient is bound by confidentiality obligations.

Use this — not a mutual NDA — when:

1. **Investor pitch / fundraising**: a founder discloses financials, business plans, IP information, and strategic data to prospective investors (VCs, angels, family offices). The investor shares nothing confidential in return.

2. **Vendor access to customer data**: a client onboards a vendor, supplier, or contractor who will receive access to the client's customer data, systems, or internal information to perform a service. The client discloses; the vendor receives.

3. **Pre-employment / employment**: an employer shares trade secrets, proprietary processes, and client lists with a new employee or consultant. The employer discloses; the employee receives. (Note: in many cases this is integrated into the employment contract rather than a standalone NDA — verify the preferred practice in the relevant jurisdiction.)

4. **Due diligence (sell-side NDA)**: a company being acquired provides a data room to prospective acquirers. The target discloses; the acquirer receives.

5. **Technology evaluation**: a potential licensee receives access to a technology vendor's proprietary materials for evaluation purposes before licensing terms are agreed.

## Structure — what differs from a mutual NDA

Build this document on the same framework as [[draft-nda-mutual]], with these asymmetric modifications:

### 1. Obligation asymmetry
- Only the **Recipient** bears confidentiality obligations
- The Discloser has no confidentiality obligations because the Discloser is not receiving any confidential information
- State this plainly in the recitals and in the obligations section: "The Discloser discloses Confidential Information to the Recipient. The Recipient's obligations under this Agreement are one-directional."

### 2. Narrower definition of Representatives
In a mutual NDA, each party's definition of Representatives can be similar. In a unilateral NDA:
- The Recipient's "Permitted Recipients" should be defined narrowly: only those individuals with a specific need to know in connection with the Permitted Purpose
- Consider requiring the Recipient to maintain a written list of individuals who have accessed the Confidential Information
- The Discloser should have the right to require the Recipient to identify the individuals who received access, on request

### 3. Stronger IP / ownership clauses
- Express statement: the Discloser retains full ownership of all Confidential Information and all IP rights therein. No rights are transferred or licensed.
- No implied license: the receipt or use of Confidential Information for the Permitted Purpose does not, by implication or otherwise, confer any license to use, reproduce, or exploit the Discloser's IP.
- Work product: if the Recipient creates any work product, analysis, or output based on the Confidential Information, the Discloser may want to include a provision stating that such work product is also Confidential Information (or is assigned to the Discloser).

### 4. Explicit irreparable-harm acknowledgment
In a mutual NDA, both parties acknowledge the inadequacy of monetary damages. In a unilateral NDA, the acknowledgment is Recipient-specific and should be more emphatic:
- "The Recipient acknowledges that any breach or threatened breach of this Agreement would cause the Discloser irreparable harm that monetary damages could not adequately compensate, and that the Discloser is entitled to seek urgent injunctive relief or other equitable relief in any competent court, without the requirement to post a bond or other security, in addition to any other remedies the Discloser may have."
- In civil-law MENA jurisdictions (UAE, KSA, LB), add: "The Recipient agrees that this clause constitutes an acknowledgment of the conditions for a precautionary attachment (saisie conservatoire) or interlocutory injunction under applicable law."

### 5. Term — default longer
A unilateral NDA typically runs longer than a mutual NDA because there is no symmetric commercial pressure on the Discloser to limit the duration:
- **Standard default**: 3-5 years from the date of each disclosure
- **Trade secrets**: indefinite — obligations survive as long as the information remains a trade secret under applicable law
- In the investor context: the Discloser may accept 1-2 years if the VC insists, but 3 years is more protective

### 6. Return or destruction — more aggressive
On the Discloser's request or on termination of the relationship:
- Recipient must promptly return or destroy all Confidential Information (all media)
- Provide a written destruction certificate within [3] business days
- Confirm that all electronic copies, cloud storage, and backup media containing Confidential Information have been purged (to the extent technically practicable)

### 7. No obligation to disclose
Include: the Discloser is not obligated to disclose any particular information. Any information disclosed is at the Discloser's sole discretion.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Disclosing Party | Full identification | — must supply |
| Receiving Party | Full identification | — must supply |
| Permitted Purpose | Defines scope of use | — must supply precisely |
| Term of confidentiality obligation | Duration | 3 years from disclosure; trade secrets survive indefinitely |
| Governing law | Controls remedies and interpretation | Jurisdiction agreed between parties or Discloser's home |

## Standard carve-outs

Same as mutual NDA, but applied to the Recipient only:
1. Publicly available through no breach by the Recipient
2. Already known to the Recipient prior to disclosure (without restriction)
3. Independently developed by the Recipient without reference to the Discloser's CI
4. Received lawfully from a third party
5. Required by law / court order (with advance notice obligation)

No additional carve-outs should be conceded without commercial justification.

## Governing law and remedies

In MENA cross-border contexts where the Discloser is from one jurisdiction and the Recipient from another, the Discloser typically prefers its home law as governing law (to ensure familiar remedies). Where both are UAE-based: UAE law / DIFC (if DIFC-nexus). For transactions with GCC parties: DIAC arbitration is a common choice.

Injunctive relief: most MENA courts (UAE, KSA, LB) can grant urgent precautionary relief (preliminary injunctions, attachments) in respect of trade secret or IP misappropriation. The contractual acknowledgment of irreparable harm assists but does not automatically guarantee relief — local counsel should advise.

## Drafting standards

- Produce a complete, ready-to-execute document. Do not leave blank fields. If a value was not provided, state a clearly-labeled default at the top of the output.
- The document title must make clear this is a "one-way" or "unilateral" confidentiality agreement — avoid naming it "Mutual NDA" in error.
- Signature block: Discloser signs on left or first; Recipient signs on right or second. Consider including a recital acknowledging the asymmetric nature so that any recipient who signs cannot later claim ignorance that they were the bound party.

## Common mistakes

- Using a mutual NDA form and crossing out the Discloser's obligations — creates a sloppy, ambiguous document; draft the unilateral form from the start
- Not defining the Permitted Purpose with sufficient specificity — leaves the Recipient free to use the CI for adjacent purposes
- Omitting the injunctive relief clause — leaves the Discloser relying on monetary damages for what is often an IP/trade-secret violation that is better stopped than compensated
- Short duration (1 year) for a technology or business-model NDA — valuable business information disclosed today should be protected longer

## Related skills

- [[draft-nda-mutual]]
- [[review-nda-quick-check]]
- [[conversation-intake-nda]]
- [[draft-boilerplate-clauses]]
