# Standard NDA Issue Checklist

This checklist drives Pass 2 of the NDA review (standard-protection check). For each item, classify the document as: **Present and standard** / **Present but unusual** / **Missing** / **N/A**.

The checklist is calibrated to typical US commercial NDAs. Items marked with † are particularly perspective-sensitive — the same clause language reads very differently depending on which side the user is on. See `perspective_lens.md` for how to flip the lens.

## 1. Definition of Confidential Information †

What it is: the clause defining what counts as "Confidential Information" subject to the agreement's protections.

What "standard" looks like:
- Covers information disclosed in any form (oral, written, electronic, visual).
- For unilateral-toward-discloser: defines confidential information broadly and does not require marking or written confirmation as a precondition for protection. Sometimes includes a "reasonable person would understand to be confidential" catch-all.
- For mutual or recipient-favorable: may require marking, may require written confirmation of orally-disclosed information within a stated period (typically 30 days), may exclude general business information.

What's unusual:
- Definition limited to information "marked confidential" with no catch-all (favors recipient; problematic for discloser).
- Definition extending to information *derived from* confidential information without limit (favors discloser; problematic for recipient).
- Definition extending to "any information" with no qualifier (overly broad).
- Asymmetric definitions in a "mutual" NDA — different scope for what each party's confidential information includes.

## 2. Exclusions from Confidential Information †

What it is: the clause carving out specific categories of information from the confidentiality obligation. Standard exclusions:
- Information already in the public domain.
- Information that becomes public through no fault of the recipient.
- Information independently developed by the recipient without use of the confidential information.
- Information rightfully received from a third party without confidentiality obligations.
- Information already known to the recipient before disclosure (sometimes requiring documentation).

What's unusual:
- Missing exclusions entirely (problematic for recipient; recipients should never agree).
- Overly broad "independently developed" carveout that effectively swallows the confidentiality obligation (problematic for discloser).
- "Reverse engineering" exclusion (often a recipient-favorable add; flag whenever present).
- Exclusion for information disclosed pursuant to legal process *without notice* to the discloser (problematic for discloser; standard exclusions allow disclosure with notice).
- Asymmetric exclusions in a "mutual" NDA.

## 3. Permitted Uses †

What it is: the clause specifying what the recipient may do with the confidential information.

What "standard" looks like:
- Use limited to a specifically named "Purpose" defined elsewhere in the agreement (e.g., "evaluating a potential business relationship between the parties").
- Use is for the named Purpose only; any other use requires written consent.

What's unusual:
- Broad permitted uses (e.g., "for any purpose related to the parties' business relationship") (problematic for discloser).
- Missing purpose definition entirely (problematic for both — the operative restriction is undefined).
- Permitted use that includes "internal evaluation" without a defined business purpose (vague; favors recipient).
- "Use" defined to exclude obvious activities like comparing with the recipient's own products (favors discloser; flag for recipient).

## 4. Permitted Disclosures †

What it is: the clause specifying who, on the recipient's side, may receive the confidential information. Typical categories:
- Employees with a need to know.
- Affiliates / subsidiaries.
- Professional advisors (lawyers, accountants, financial advisors).
- Subcontractors.

What "standard" looks like:
- Disclosure to employees with need to know, who are bound by confidentiality obligations at least as protective as this agreement.
- Disclosure to professional advisors under similar conditions.
- Disclosure required by law, with prompt notice to the discloser and cooperation in seeking a protective order.

What's unusual:
- No permitted disclosure to advisors (highly problematic for recipient — blocks legal counsel and accountants).
- Disclosure to "any person bound by confidentiality" without scope limit (favors recipient; problematic for discloser).
- Required disclosure without notice provision (favors recipient; problematic for discloser).
- Affiliates included without limit (problematic for discloser, especially for large-corporate-family recipients).
- "Need to know" not specified — disclosure to "employees" generally (favors recipient; problematic for discloser).

## 5. Term and Duration †

What it is: how long the agreement lasts and how long confidentiality obligations survive.

What "standard" looks like:
- Agreement term: 1–5 years (most commonly 2–3).
- Confidentiality obligation duration: 2–5 years from the date of disclosure (most commonly 3 years).
- For trade secrets specifically: often defined to continue "for as long as the information remains a trade secret" (this is the standard discloser ask).

What's unusual:
- Perpetual confidentiality on all confidential information (favors discloser; problematic for recipient — perpetual obligations on non-trade-secret information are operationally burdensome and may be unenforceable in some jurisdictions).
- Very short term (less than 1 year) (favors recipient; problematic for discloser).
- Confidentiality survives only for the term of the agreement, not from disclosure (favors recipient; common drafting error or aggressive recipient ask).
- Term tied to a deal that may not happen ("until consummation of the transaction"); flag the gap if the deal doesn't close.

## 6. Return / Destruction of Confidential Information †

What it is: what happens to confidential information when the agreement ends or the discloser requests it back.

What "standard" looks like:
- On request or termination, recipient returns or destroys all confidential information.
- Recipient may retain one archival copy in legal/compliance files.
- Recipient may retain copies on standard backup systems (with continuing confidentiality obligations).
- Certificate of destruction provided on request.

What's unusual:
- Mandatory return (no destruction option) (problematic for recipient; impossible to fully comply with for digital information).
- No retention exception for legal/compliance archives (problematic for recipient).
- No backup-system exception (problematic for recipient).
- Required certification within unreasonable time (e.g., 5 days) (problematic for recipient).
- No return/destruction obligation at all (favors recipient; problematic for discloser).

## 7. Residuals Clause

What it is: a clause stating that information retained in the unaided memory of recipient personnel is not subject to confidentiality obligations.

What "standard" looks like:
- Most NDAs do not have a residuals clause.
- When present, scope is typically limited to general knowledge, skills, and experience retained in unaided memory.

What's unusual:
- Any residuals clause from a discloser perspective is problematic; flag as material.
- Broad residuals clauses (e.g., covering "ideas, concepts, and know-how") effectively eliminate the protection; flag as critical from discloser perspective.
- Residuals coupled with a no-license clause is the standard recipient-favorable construction; from a recipient perspective, this is the desired structure.

## 8. No-License Language

What it is: explicit statement that disclosure of confidential information does not grant any license, ownership, or other rights to the recipient.

What "standard" looks like:
- Brief, clear statement that no license is granted by implication, estoppel, or otherwise.

What's unusual:
- Missing entirely (flag whenever absent; both sides typically want this).
- Coupled with broad IP assignment language (flag — IP assignment in an NDA is a red flag, see `red_flags.md`).

## 9. Equitable Remedies / Injunctive Relief †

What it is: clause acknowledging that breach of confidentiality may cause irreparable harm and providing for injunctive relief without bond.

What "standard" looks like:
- Acknowledgment of irreparable harm.
- Right to seek injunctive relief in addition to damages.
- Waiver of bond requirement.

What's unusual:
- Missing entirely (favors recipient; standard discloser ask).
- One-sided availability (e.g., only the discloser may seek injunctive relief, even in a mutual NDA) (asymmetry; flag).
- Waiver of damages or limitation on damages alongside injunctive relief (favors recipient).
- Liquidated damages amounts (rare in NDAs; flag — see `red_flags.md`).

## 10. Governing Law and Venue

What it is: choice of governing law and forum for disputes.

What "standard" looks like:
- A specified state's law and a specified venue (state or federal court in that state, or arbitration with seat).

What's unusual:
- No governing law specified (creates conflict-of-laws uncertainty).
- Counterparty's home state law for both governing law and venue (negotiable; flag if user has no presence there).
- Mandatory arbitration with non-standard rules (flag for recipient if a NDA breach is at issue — recipients usually prefer court for the equitable remedy access).
- Exclusive venue in a hostile or inconvenient forum.
- Governing law of a non-US jurisdiction in an otherwise-US deal (flag).

## 11. Assignment

What it is: whether and how the agreement can be assigned to a successor entity.

What "standard" looks like:
- Either silent (defaults to general contract law) or restricted with consent.
- Permitted assignment to successors-in-interest in a merger, acquisition, or sale of substantially all assets.

What's unusual:
- Free assignability (problematic for discloser — counterparty can assign confidentiality obligations to a competitor of the discloser).
- Prohibition on assignment even to successors-in-interest (problematic for both sides if either may be acquired).

## 12. Integration / Entire Agreement and Amendment

What it is: clause stating the document is the entire agreement and can only be amended in writing.

What "standard" looks like:
- Standard integration clause; amendments must be in writing signed by both parties.

What's unusual:
- Integration clause that purports to override prior agreements addressing the same subject (flag if user mentioned prior agreements in business context).
- Oral amendments allowed (flag).

## 13. Notice

What it is: clause specifying how formal notices under the agreement are delivered.

What "standard" looks like:
- Email or certified mail to specified addresses; typically deemed received on a specified day.

What's unusual:
- No notice provision (creates ambiguity for return-of-information requests, breach notifications, etc.).
- Notice requirements that effectively block notice (e.g., physical mail only to a foreign address with no email option).

## 14. Counterparts and Electronic Signatures

What it is: clause permitting execution in counterparts and via electronic signature.

What "standard" looks like:
- Standard counterparts and e-signature clause.
- Missing this is rarely material (most jurisdictions allow electronic signatures by default), but it's a small flag for cleanliness.
