# Worked Example — Recipient Perspective, Unilateral NDA

This example shows the skill applied to a unilateral NDA where the user is the recipient. The scenario: a SaaS company is evaluating a vendor's product and the vendor has presented a unilateral NDA protecting only the vendor's information.

## Input

**Perspective:** recipient
**Deal type:** vendor_evaluation
**Jurisdiction:** Delaware (governing law in the document)
**Prior agreements:** none

**Document (excerpts):**

> **MUTUAL NON-DISCLOSURE AGREEMENT**
> *Note: title says "Mutual" but operative language is unilateral toward the vendor.*
>
> **1. Confidential Information.** "Confidential Information" means any and all information disclosed by Discloser to Recipient, in any form, whether or not marked or identified as confidential at the time of disclosure, including without limitation all technical information, business information, customer information, financial information, product information, and any derivative works thereof. Confidential Information shall include all such information regardless of the form in which it is communicated and regardless of whether Recipient retains any tangible record of it.
>
> **2. Exclusions.** The obligations herein shall not apply to information that Recipient can demonstrate by competent written evidence: (a) was in the public domain at the time of disclosure; or (b) was known to Recipient prior to disclosure pursuant to a written record predating disclosure.
>
> **3. Use.** Recipient shall use Confidential Information solely for the purpose of evaluating Discloser's products and services and shall not use Confidential Information for any other purpose, including without limitation product development, competitive analysis, or benchmarking.
>
> **4. Disclosure.** Recipient may disclose Confidential Information only to its employees who have a need to know for the Purpose and who are bound by written confidentiality obligations at least as protective as those herein. Recipient shall not disclose Confidential Information to any other person or entity, including without limitation affiliates, contractors, advisors, or agents, without Discloser's prior written consent.
>
> **5. Term.** This Agreement shall remain in effect for a period of seven (7) years from the Effective Date. Recipient's obligations with respect to Confidential Information shall survive termination indefinitely.
>
> **6. Return.** Upon Discloser's request or upon termination of this Agreement, Recipient shall promptly return all Confidential Information to Discloser. Recipient shall provide a written certification of return within five (5) business days.
>
> **7. Feedback.** Any suggestions, ideas, improvements, or feedback provided by Recipient regarding Discloser's products or services shall become the sole and exclusive property of Discloser. Recipient hereby assigns all right, title, and interest in such feedback to Discloser.
>
> **8. Non-Solicitation.** During the term of this Agreement and for two (2) years thereafter, Recipient shall not solicit for employment any employee of Discloser with whom Recipient had contact in connection with this Agreement.
>
> **9. Indemnification.** Recipient shall indemnify, defend, and hold harmless Discloser from and against any and all claims, damages, losses, and expenses (including reasonable attorneys' fees) arising out of or related to any breach by Recipient of this Agreement.
>
> **10. Equitable Relief.** Recipient acknowledges that any breach of this Agreement would cause irreparable harm to Discloser for which monetary damages would be inadequate, and that Discloser shall be entitled to injunctive relief and specific performance without the requirement of posting bond.
>
> **11. Governing Law.** This Agreement shall be governed by the laws of the State of Delaware. The parties consent to exclusive jurisdiction in the state and federal courts of New Castle County, Delaware.

---

## Output

# NDA Review: [Vendor] Mutual Non-Disclosure Agreement

**Perspective:** recipient
**Document type:** Unilateral NDA toward discloser (despite "Mutual" in the title — operative provisions only obligate Recipient)
**Governing law:** Delaware
**Term:** 7-year agreement; perpetual confidentiality obligations

## Bottom line

This is a recipient-unfavorable document mislabeled as mutual. It contains four critical issues — perpetual confidentiality, indemnification, IP assignment of feedback, and missing standard exclusions — plus material issues with permitted disclosure and a non-solicitation clause unrelated to the confidentiality purpose. The document is not signable as drafted; substantial negotiation is required, or the document should be replaced with a balanced template. The single most important issue is the perpetual confidentiality obligation on a broadly-defined category of information, which is operationally impossible to comply with and likely unenforceable beyond the trade-secret subset.

## Critical issues

### Perpetual confidentiality obligation (§5)

**What the document says:** "Recipient's obligations with respect to Confidential Information shall survive termination indefinitely."

**Why it's a problem:** Combined with the broad definition of Confidential Information in §1 (which covers "all technical information, business information, customer information, financial information, product information"), this creates an indefinite obligation across a vast category of information. Recipient's compliance program must track and protect this information forever, including through reorganizations, acquisitions, employee turnover, and infrastructure migrations. Operationally impossible. Beyond operations, perpetual obligations on non-trade-secret information face enforceability questions in many jurisdictions; Delaware courts have not categorically rejected perpetual NDAs, but the reasonableness of perpetual term on a broad information category would be tested in any enforcement action.

**Suggested redline:** Replace §5 with: *"This Agreement shall remain in effect for a period of three (3) years from the Effective Date. Recipient's obligations with respect to Confidential Information shall survive for three (3) years from the date of disclosure of such information; provided, however, that with respect to any Confidential Information that constitutes a trade secret under applicable law, such obligations shall survive for so long as such information continues to qualify as a trade secret."*

### Indemnification obligation (§9)

**What the document says:** Recipient indemnifies Discloser for any breach of the agreement, including attorneys' fees.

**Why it's a problem:** Indemnification is out of place in an NDA. Standard NDA remedies are damages and equitable relief; indemnification expands recipient's exposure to third-party-claim risk and shifts defense costs even when claims are unsubstantiated. The clause as drafted is one-sided (only Recipient indemnifies Discloser) in an agreement labeled "mutual."

**Suggested redline:** Delete §9 entirely. If Discloser insists on some additional protection, propose limiting indemnification to actual third-party claims arising from Recipient's intentional or grossly negligent breach, capped at a defined amount.

### IP assignment of feedback (§7)

**What the document says:** Any feedback Recipient provides on Discloser's products becomes Discloser's sole property; Recipient assigns all rights.

**Why it's a problem:** This turns the NDA into an IP transfer document. Recipient cannot evaluate the product without giving feedback (asking questions, identifying issues, requesting features), and any such feedback — including ideas Recipient already had independently — vests in Discloser. A senior architect who comments "we'd want this to integrate with X" has just transferred their architectural insight to Discloser. Beyond the immediate IP loss, the clause creates ambiguity about Recipient's own product development if Recipient is in an adjacent space.

**Suggested redline:** Replace §7 with: *"Recipient may, but is under no obligation to, provide feedback regarding Discloser's products and services. Such feedback is provided 'as is' and Discloser may use such feedback for any purpose, but no rights are granted by Recipient to Discloser in any underlying intellectual property, and Recipient retains all rights in any pre-existing IP."*

If Discloser refuses redline, alternative: scope the feedback assignment narrowly to feedback specifically directed at Discloser's products, exclude general industry insights, and reserve Recipient's rights to develop products in Recipient's own space.

### Missing standard exclusions (§2)

**What the document says:** Exclusions are limited to (a) information in the public domain at time of disclosure and (b) information already known to Recipient pursuant to written record predating disclosure.

**Why it's a problem:** Standard NDA exclusions cover five categories. This document only includes two, both with restrictive evidentiary requirements:

- Missing: information that *becomes* public after disclosure through no fault of Recipient.
- Missing: information independently developed by Recipient without use of Confidential Information.
- Missing: information rightfully received from a third party without confidentiality obligations.
- The "prior knowledge" exclusion requires "competent written evidence" — a standard provision allows demonstration by reasonable evidence rather than imposing a contemporaneous-documentation requirement.

The combined effect is that Recipient takes on confidentiality obligations for information that becomes public through Discloser's own subsequent actions, for information Recipient develops independently, and for information Recipient receives from third parties — none of which Discloser has a legitimate basis to protect.

**Suggested redline:** Replace §2 with: *"The obligations of this Agreement shall not apply to information that Recipient can demonstrate: (a) was in the public domain at the time of disclosure; (b) becomes part of the public domain after disclosure through no breach of this Agreement by Recipient; (c) was known to Recipient prior to disclosure without obligation of confidentiality; (d) is independently developed by Recipient without use of or reference to the Confidential Information; or (e) is rightfully received by Recipient from a third party without restriction on disclosure."*

## Material issues

### Permitted disclosure does not include advisors (§4)

**What the document says:** Recipient may disclose only to employees with need to know; not to affiliates, contractors, advisors, or agents without prior written consent.

**Why it's a problem:** Recipient cannot meaningfully evaluate the platform without involving outside counsel (for contract negotiation), accountants (for cost-benefit analysis), and potentially security consultants (for technical evaluation). Operating under this provision would require obtaining written consent for each advisor disclosure — operationally burdensome and creates a record of every advisor consultation that Discloser sees.

**Suggested redline:** Add to §4: *"Notwithstanding the foregoing, Recipient may disclose Confidential Information to its outside legal, financial, and technical advisors who have a need to know for the Purpose and who are bound by professional or contractual obligations of confidentiality at least as protective as those herein. Recipient may also disclose to its affiliates and contractors who are bound by written confidentiality obligations at least as protective as those herein, provided Recipient remains responsible for any breach by such affiliates or contractors."*

### Non-solicitation clause (§8)

**What the document says:** Recipient may not solicit Discloser's employees Recipient had contact with, for two years after termination.

**Why it's a problem:** Non-solicits inside NDAs are not inherently problematic but warrant the user's deliberate business judgment. Considerations:

- Scope is reasonable (only employees Recipient had contact with, not all employees).
- Two-year duration extends past the agreement's relevance and binds Recipient long after the evaluation ends.
- Delaware enforces reasonable non-solicits, but the user should be aware that any of Recipient's employees who happen to know any of Discloser's employees becomes a compliance question.

**Recommendation:** This may be acceptable depending on the user's appetite. If accepting, consider negotiating duration down to one year and confirming the scope is limited to the user organization (not affiliates).

### 5-business-day return certification (§6)

**What the document says:** Written certification of return within 5 business days.

**Why it's a problem:** Five business days is tight for a meaningful return-and-certification process. For digital information, "return" typically means destruction; for an organization with backup systems and distributed storage, certifying complete destruction within 5 business days requires either skipping the actual destruction steps or making a representation that may not be accurate.

**Suggested redline:** Modify §6 to: *"Upon Discloser's request or upon termination of this Agreement, Recipient shall promptly return or destroy all Confidential Information, except that Recipient may retain (i) one archival copy in its legal and compliance files and (ii) copies on standard backup systems pursuant to ordinary backup retention policies, in each case subject to continuing confidentiality obligations under this Agreement. Recipient shall provide a written certification of return or destruction within thirty (30) days of request."*

## Minor issues and observations

- Document is titled "Mutual" but operative provisions are unilateral. While not a substantive issue (the substance controls), the title-vs-substance mismatch is a drafting flag — either change the title or make the obligations actually mutual.
- Use restriction in §3 explicitly prohibits "competitive analysis" — fine in a vendor evaluation context but worth noting if the user has any business overlap with Discloser.
- Equitable relief provision (§10) is one-sided in an agreement labeled mutual. If §1 and other provisions are made mutual through redline, mirror equitable relief on Recipient's side.
- Governing law is Delaware (acceptable; neutral commercial forum).
- No counterparts/e-signature clause; minor cleanliness issue.

## Missing standard protections

- **No-license language.** Standard NDA includes an explicit statement that disclosure does not grant any license, ownership, or other rights. Add: *"No license is granted, by implication, estoppel, or otherwise, under any patent, copyright, trademark, trade secret, or other intellectual property right of either party. All Confidential Information remains the property of the disclosing party."*
- **Compelled disclosure provision.** Standard NDA includes a clause permitting disclosure pursuant to legal process with prompt notice to the discloser and cooperation in seeking a protective order. Add: *"Recipient may disclose Confidential Information to the extent required by law, regulation, or court order, provided that Recipient promptly notifies Discloser (to the extent legally permitted) and reasonably cooperates with Discloser's efforts to obtain a protective order or other appropriate remedy."*
- **Survival clause clarity.** §5 has perpetual confidentiality survival but no clear list of which other provisions survive (typically: confidentiality, definitions, equitable relief, governing law, notices).

## Operational red flags

- **IP assignment of feedback (§7)** — addressed as critical above.
- **Indemnification (§9)** — addressed as critical above.
- **Non-solicitation (§8)** — addressed as material above.
- **Mutual title with unilateral operative language** — drafting concern; raises questions about whether the document was prepared in good faith for a mutual evaluation.

## Recommended next steps

1. **Do not sign as-is.** The four critical issues collectively make this document unacceptable for a vendor evaluation.
2. **Negotiate with the redlines proposed above** — particularly §2 (exclusions), §5 (term), §7 (feedback IP), and §9 (indemnification). These are non-negotiable from a recipient perspective.
3. **Consider proposing the user's standard mutual NDA template instead.** If the user's organization has a template, replacing this document with a template the user controls is faster than redlining this one.
4. **If Discloser insists on this document with material critical issues unresolved**, escalate to a senior decision-maker on the user's side. Signing this document as-drafted creates exposure that should be a senior business decision, not a procurement-level approval.

## Items requiring human judgment

- **Enforceability of perpetual confidentiality in Delaware.** Delaware has not categorically rejected perpetual NDAs; user should confirm with own analysis whether perpetual term on broad information categories would be enforceable in the user's specific factual context.
- **Acceptability of the non-solicitation clause** depends on user's hiring patterns and any overlap between user's and Discloser's talent pools. Skill cannot assess.
- **Whether to push back on "Mutual" mislabeling.** This is a relationship-management call about how aggressively to negotiate at the start of a vendor evaluation. The user knows the relationship dynamic.

---

*End of example output.*

## What this example demonstrates

- **The four-pass workflow visible in the structure.** Pass 1 (orientation) produced the document-type assessment in the header. Pass 2 (standard-protection check) surfaced the missing exclusions and missing no-license. Pass 3 (asymmetry) drove the recognition that "mutual" is mislabeled. Pass 4 (red flags) caught the IP assignment, indemnification, and non-solicitation.
- **Severity calibrated to user response.** Four critical issues, each tied to a recommended next step that would be different at material severity. Material issues are negotiable but acceptable in some scenarios. Minor issues are observations.
- **Specific clause references on every finding.** A reviewer can navigate to §5, §9, §7, §2 immediately.
- **Redline language proposed for every critical and material issue.** Not just "negotiate this" but "here is language to propose."
- **"Items requiring human judgment" used appropriately.** Enforceability questions and business judgments deflected to the user, rather than the skill pretending to know.
- **Bottom line opens with the recommendation, not with the analysis.** The user gets the punchline before the work.
