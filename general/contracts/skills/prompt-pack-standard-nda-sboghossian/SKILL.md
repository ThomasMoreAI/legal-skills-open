---
name: prompt-pack-standard-nda-sboghossian
title: Standard NDA
description: Use when parties evaluating a potential transaction or collaboration need a mutual non-disclosure agreement covering standard confidentiality obligations, permitted disclosures, term, and governing law. Addresses the key MENA-specific traps in NDAs — enforceability under UAE Civil Law, the treatment of written form requirements, language obligations in KSA, and the distinction between bilateral and unilateral NDAs in common-law vs. civil-law practice.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-standard-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Standard NDA

## When to use this

Use this skill when:
- Two parties are about to share confidential information for the purpose of evaluating a potential transaction, partnership, or project.
- A company is engaging in preliminary M&A discussions and needs a clean NDA before sharing a data room.
- A startup is meeting investors and wants to protect its proprietary technology or business model.
- A vendor is receiving a client's confidential business requirements before quoting on a project.
- A company needs a mutual NDA for ongoing business discussions with a potential joint venture partner.

**Unilateral vs. mutual NDA:** A mutual (bilateral) NDA binds both parties equally. A unilateral NDA binds only the receiving party. Use a mutual NDA when both parties will share confidential information (most commercial evaluations). Use a unilateral NDA when only one party is disclosing (e.g., a job candidate receiving company information, a contractor receiving client data).

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Party A name and details** | Required for agreement header | Ask |
| **Party B name and details** | Required for agreement header | Ask |
| **Purpose of the disclosure** | Defines the permitted use of confidential information; too broad or too vague creates enforcement problems | Ask: "What are the parties evaluating?" |
| **Term of the NDA** | How long the agreement lasts | Default: 2 years from execution; adjust based on the nature of the transaction |
| **Confidentiality obligation duration** | How long parties are bound to keep information confidential after the NDA expires | Default: 3 years after disclosure for general information; indefinitely for trade secrets |
| **Governing law** | Determines enforceability of specific clauses | Ask; default UAE onshore if MENA parties |

## Optional inputs

- **Exclusivity or standstill obligation** — some NDAs include a standstill preventing the recipient from making a hostile acquisition bid; if intended, add this expressly.
- **Non-solicitation of employees** — prevents either party from poaching the other's employees during the NDA term.
- **Injection relief provision** — confirms that damages are inadequate and that injunctive relief is appropriate for breach.
- **Residuals clause** — allows a party's employees to retain in memory information absorbed during the disclosure without obligation to scrub their brains; controversial and strongly resisted by disclosing parties.

## Document structure

1. **Parties and purpose**
   - Names and jurisdictions of both parties.
   - Stated purpose: "the parties wish to explore a potential [describe transaction/project] and may disclose confidential information to each other for that purpose."
   - Defined as the "Permitted Purpose."

2. **Definition of confidential information**
   - **Broad definition (recommended):** all information disclosed by one party to the other, in any form (written, oral, electronic, visual), that is marked as confidential, or that a reasonable person would understand to be confidential given its nature and the circumstances of disclosure.
   - **Specific categories:** financial information, business plans, customer lists, technical specifications, IP, pricing, personnel information, trade secrets.
   - **Exclusions from confidential information** (standard carve-outs):
     - Information that is or becomes publicly available without breach of this Agreement.
     - Information that was already known to the recipient before disclosure (provable by the recipient's prior records).
     - Information independently developed by the recipient without reference to the disclosing party's confidential information.
     - Information received by the recipient from a third party without restriction on further disclosure.

3. **Confidentiality obligations**
   - Each party (as a recipient of Confidential Information) shall:
     - Keep the Confidential Information strictly confidential.
     - Not disclose it to any third party without the disclosing party's prior written consent.
     - Use it solely for the Permitted Purpose.
     - Apply at least the same degree of care to protect it as it applies to its own confidential information, but in no event less than reasonable care.
   - Permitted disclosures:
     - To the recipient's employees, officers, advisors, and consultants who need to know and who are bound by written confidentiality obligations at least as protective as this Agreement.
     - As required by applicable law, court order, or regulatory requirement (subject to notice and cooperation obligations below).

4. **Compelled disclosure**
   - If a party is required by law or court order to disclose Confidential Information, it must:
     - Promptly notify the disclosing party (if legally permitted to do so).
     - Cooperate with the disclosing party's efforts to seek a protective order.
     - Disclose only the minimum information required.
     - Continue to maintain confidentiality for all information not required to be disclosed.

5. **Permitted purpose limitation**
   - Recipient may use the Confidential Information only for the Permitted Purpose.
   - Any use beyond the Permitted Purpose (including competitive use, reverse engineering, or use after the NDA terminates) constitutes a breach.

6. **Return / destruction of confidential information**
   - On the earlier of: (a) the disclosing party's written request, or (b) expiry or termination of this Agreement, the recipient must:
     - Return all documents and copies containing Confidential Information; or
     - Certify in writing that all such documents have been destroyed.
   - Exception: copies retained on secure backup systems that are regularly overwritten and not accessible in the ordinary course of business.

7. **No license**
   - Nothing in this Agreement grants any license, right, or interest in the Confidential Information or the disclosing party's IP.
   - Disclosure of Confidential Information does not create any obligation to continue the discussions or to proceed with any transaction.
   - Standard "no transaction obligation" clause: either party may terminate discussions at any time without liability.

8. **Representations and warranties**
   - Each party represents that it has authority to enter into this Agreement.
   - Each party represents that its Confidential Information does not violate the rights of any third party.
   - No warranty that Confidential Information is accurate or complete (this is critical — a disclosing party should not warrant the accuracy of preliminary information shared in a due diligence context).

9. **Injunctive relief**
   - The parties acknowledge that breach would cause irreparable harm and that monetary damages would be inadequate.
   - Each party agrees that injunctive relief, without the requirement to post a bond, is an appropriate remedy.
   - **MENA note:** UAE courts and DIFC courts both recognize injunctive relief. In UAE onshore practice, interlocutory injunctions in commercial matters are available but courts apply a balance-of-harm test; including this clause does not guarantee relief but it strengthens the legal basis.

10. **Term**
    - This Agreement commences on the date of execution and continues for [2] years, unless earlier terminated by either party on [30 days'] written notice.
    - The confidentiality obligations survive termination for a period of [3] years from the date of each disclosure (or indefinitely for trade secrets).

11. **General provisions**
    - Governing law and jurisdiction.
    - Entire agreement.
    - Amendments in writing.
    - No waiver.
    - Severability.
    - Counterparts (including electronic signatures — recognized under UAE e-Transactions Law, DIFC Electronic Transactions Law, and most modern NDA practice).

## Jurisdictional notes

### UAE — onshore
- UAE Civil Transactions Law (Art. 246): agreements to be performed in good faith; confidentiality in commercial dealings is generally recognized as a principle of good faith.
- No specific NDA statute; enforceability as a civil contract is well-established.
- Specific performance and injunctive relief available in UAE commercial courts.
- Arabic version: while not mandatory for all commercial NDAs, an Arabic version is required for enforcement in UAE mainland courts. Consider executing a bilingual Arabic/English agreement or ensuring the English version has an Arabic translation clause.
- Electronic signatures: recognized under UAE Federal Decree-Law No. 46 of 2021 on Electronic Transactions; DocuSign-executed NDAs are valid.

### DIFC / ADGM
- NDAs are standard contracts; enforced under DIFC Contract Law (DIFC Law No. 6 of 2004) or ADGM Contract Regulations.
- Injunctive relief readily available from DIFC / ADGM courts.
- No Arabic language requirement for DIFC/ADGM contracts.

### KSA
- NDAs are enforceable in Saudi commercial courts as contracts.
- Arabic version: strongly recommended for enforcement; courts apply Arabic-language documents as the controlling version.
- No specific NDA legislation; general contract law under Sharia principles governs.
- Notarization: not typically required for standard commercial NDAs but strengthens enforceability for high-value matters.

### Lebanon
- French civil-law tradition; NDAs are contracts subject to the Code of Obligations and Contracts.
- Courts recognize breach of confidentiality as a contractual and (in egregious cases) tortious matter.
- Injunctive relief (référé) available in Lebanese courts.

### UK / EU
- NDAs are standard commercial practice; enforceable as contracts.
- UK: recent scrutiny of NDAs used to silence harassment victims; "non-disclosure agreements" (NDAs) used to prevent reporting of criminal conduct are void and unenforceable (UK Employment Rights Act 1996; UK Serious Crime Act 2015). Ensure scope does not prevent regulatory or law enforcement disclosure.
- GDPR: if personal data is shared under the NDA, a separate DPA may be needed.

## Drafting standards

- Keep the NDA concise: 4–8 pages is standard for a mutual commercial NDA. Longer NDAs with exotic provisions often create more uncertainty, not less.
- Define "Confidential Information" by reference to what a reasonable person would understand to be confidential in context — this is more resilient than an exhaustive list.
- Do not promise the NDA's obligations will survive forever. Indefinite confidentiality obligations are hard to enforce and unusual in commercial contexts; use a defined period (3–5 years) for most information and "indefinitely" for genuine trade secrets only.
- Include a residuals clause only if the recipient's negotiating position requires it and the disclosing party can accept it; it significantly weakens the NDA.
- For cross-border NDAs with parties in MENA: always include a governing law clause even for a simple NDA — forum ambiguity is expensive.

## Common mistakes

- **Purpose defined too broadly.** An NDA "for general business discussions" with no defined purpose allows the recipient to claim virtually any use is permitted. Define the specific transaction or project.
- **No permitted disclosures to advisors.** A strict NDA that prevents a party from consulting its lawyers, accountants, or bankers about the transaction is unworkable; include a carve-out.
- **Confidential information includes publicly available information.** An NDA definition that includes publicly known information is overbroad and potentially unenforceable.
- **Missing consideration in some civil-law jurisdictions.** In certain jurisdictions, a contract requires consideration from both parties; in a unilateral NDA, both parties should provide some consideration (the purpose of the engagement is typically sufficient).

## Related skills

- [[prompt-pack-research-collaboration-agreement]]
- [[prompt-pack-reseller-agreement]]
- [[prompt-pack-service-agreement]]
- [[prompt-pack-share-purchase-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
