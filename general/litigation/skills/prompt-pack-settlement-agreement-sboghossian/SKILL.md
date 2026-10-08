---
name: prompt-pack-settlement-agreement-sboghossian
title: Settlement Agreement
description: Use when parties to a dispute need to draft a settlement agreement resolving pending or threatened litigation or arbitration. Covers settlement amount, payment terms, mutual releases, confidentiality, non-disparagement, and dismissal of claims. MENA-specific guidance on release enforceability under UAE civil law, waqf from liability under Lebanese law, confidentiality limitations in KSA court proceedings, and Arabic-language execution requirements.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-settlement-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Settlement Agreement

## When to use this

Use this skill when:
- Parties to litigation, arbitration, or a commercial dispute have reached a negotiated resolution and need to document it formally.
- A party wishes to pre-empt formal proceedings by offering a full and final settlement.
- A previous settlement is being renegotiated or supplemented.
- Settlement is being used to restructure a commercial relationship alongside dispute resolution (e.g., settling a payment dispute while amending the underlying contract).

**Relationship to the template skill:** [[prompt-pack-settlement-agreement-template]] produces a reusable template with more bracketed variables; this skill generates a fuller, more specific draft for a particular dispute. For a quick template, use the template skill.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Parties** | Full legal names, jurisdictions of incorporation | Ask |
| **Description of the dispute** | Defines the subject matter of the release | Ask; be specific — a vague release may not cover all disputed claims |
| **Settlement terms** | Amount, non-monetary terms, conditions | Ask; the most important input |
| **Payment structure** | Lump sum, installments, dates | Ask |
| **Governing law / seat** | Determines enforceability of release, confidentiality, and dispute resolution mechanism | Ask; default UAE if MENA parties |

## Optional inputs

- **Pending proceedings reference** — if litigation or arbitration is already filed, state the case reference and court/tribunal; the settlement agreement triggers dismissal.
- **Non-monetary terms** — business arrangements, asset transfers, contract amendments, references or representations.
- **Non-disparagement scope** — parties to key individuals and corporate communications.
- **Tax treatment** — whether the settlement payment is characterized as damages, compensation, or otherwise; affects VAT and withholding tax.

## Document structure

1. **Recitals / background**
   - Brief description of the dispute, including date of the underlying contract or event.
   - Reference to any pending proceedings (case number, court/arbitral institution, filing date).
   - Statement that the parties wish to resolve the dispute on the terms set out below.

2. **Settlement payment and consideration**
   - Amount (in figures and words; currency).
   - Payment mechanism: bank transfer to specified account.
   - Payment schedule: on signature / within [X] business days / in installments on specified dates.
   - Consequence of non-payment: settlement void, or right to enter judgment for the agreed amount (consent judgment clause).
   - Tax: "gross of / net of tax" as agreed; typically the paying party is not responsible for the recipient's tax.

3. **Mutual releases** — the most legally critical provision
   - **Full and final settlement:** each party releases and forever discharges the other from all claims, demands, actions, liabilities, damages, costs and expenses arising out of or in connection with [specifically described dispute / subject matter] that are known or unknown as at the date of this agreement.
   - **Scope of release:** must be carefully defined:
     - *Specific release:* releases only the identified claims. Safer for complex ongoing relationships.
     - *General release:* releases all claims between the parties up to the date of the agreement. Broader but riskier if there are other disputes.
   - **Known and unknown claims:** in common-law jurisdictions, a release that does not expressly cover unknown claims may not release them; include "including claims that the parties did not know or suspect to exist." In civil-law systems (UAE, LB), releases operate differently — see Jurisdictional notes.
   - **Carve-outs from release:** rights and obligations arising under the settlement agreement itself; any continuing commercial relationship terms not in dispute.

4. **Non-monetary terms** (if applicable)
   - Contract amendments, delivery of assets, provision of references, reinstatement of services.

5. **Confidentiality**
   - Terms of the settlement (amount, conditions) are confidential.
   - Permitted disclosures: to legal and financial advisors, tax authorities, as required by law or by a regulator.
   - No press releases or public statements about the settlement without the other party's written consent.
   - Carve-out: a party may disclose that the dispute has been resolved, without disclosing the terms.

6. **Non-disparagement**
   - Each party agrees not to make disparaging or defamatory statements about the other, its officers, directors, employees, or products.
   - Temporal scope: indefinite (standard) or time-limited.
   - Carve-out: truthful statements required by law or regulatory process.

7. **Dismissal of proceedings** (if applicable)
   - Claimant undertakes to file a dismissal with prejudice / discontinuance of all pending claims in [Court/Arbitral Tribunal] within [X] business days of receipt of the settlement payment.
   - Parties will cooperate to effect dismissal.
   - Until payment is received, proceedings are stayed.

8. **No admission of liability**
   - Standard clause: this settlement does not constitute an admission of liability, wrongdoing, or fault by either party.
   - This protects both parties' positions in future proceedings or with third parties.

9. **Representations and warranties**
   - Each party represents that it has authority to enter into this agreement.
   - Each party represents that it has not assigned the claims being released to any third party.
   - Claimant (in a litigation settlement): represents that the claim(s) being settled are the only claims arising from the described dispute.

10. **Cooperation and further assurances**
    - Each party will do all things reasonably necessary to give effect to this settlement.
    - Execute further documents if required.

11. **Governing law and dispute resolution**
    - Governing law: [UAE onshore / DIFC / English law / etc.].
    - Disputes about interpretation or enforcement of this settlement agreement: [court / arbitration].
    - Consent to jurisdiction.

12. **General provisions** — entire agreement, amendments in writing, severability, no waiver, counterparts (relevant if parties are in different countries).

13. **Execution**
    - Signatures of authorized representatives.
    - Witnesses (required in some jurisdictions: see Jurisdictional notes).
    - Date and place of execution.

## Jurisdictional notes

### UAE — onshore (UAE Civil Transactions Law, Federal Law No. 5 of 1985)
- Settlement (Sulh) is specifically recognized under UAE Civil Transactions Law Arts. 867–878 as a distinct contract type.
- Art. 867: Sulh is a contract by which parties end a dispute by mutual concession. It requires consensus on the subject matter; if the subject matter is not clearly defined, the sulh may be void.
- Art. 871: a sulh on one dispute does not settle other disputes between the same parties unless expressly stated.
- **Releases in UAE civil law:** a general release of "all claims" is effective but may be interpreted restrictively; specify the disputed subject matter with precision. UAE courts may interpret a broad release as covering only the specific dispute that was the context of the sulh.
- **Notarization:** not mandatory for commercial settlement agreements, but for real property-related claims or amounts above AED 250,000 being enforced in court, a notarized agreement is advisable.
- **Arabic language:** enforcement in UAE courts requires an Arabic translation; consider executing a bilingual agreement.

### DIFC / ADGM
- Common-law principles apply; settlement agreements are standard contracts.
- Full and final release (including unknown claims) is enforceable if clearly worded.
- Consent judgments: parties can record a settlement in a DIFC/ADGM court consent order, which is then enforceable as a judgment.
- Tomlin orders (UK practice): DIFC courts accept Tomlin orders for settlements reached during litigation.

### KSA
- Settlement (sulh) is deeply rooted in Islamic jurisprudence and is recognized and encouraged in Saudi courts.
- Confidentiality of settlement terms may be difficult to maintain if either party later presents the settlement in court proceedings; Saudi courts may require disclosure of settlement terms.
- Arabic: the settlement agreement must be in Arabic for enforcement in Saudi courts; any English version is a translation.
- Notarization before a notary (كاتب العدل) strengthens enforceability.

### Lebanon
- Settlement (acte transactionnel) recognized under Lebanese Code of Obligations and Contracts Art. 1041+.
- French civil-law tradition: settlement has the force of res judicata between the parties for the settled matters.
- Broad releases are effective; courts respect party autonomy in commercial matters.
- Confidentiality: Lebanese courts will generally respect confidentiality provisions but may order disclosure in related criminal proceedings.

### Egypt
- Settlement recognized under Egyptian Civil Code Arts. 549–560.
- Egyptian courts will enforce a properly executed settlement agreement as a final resolution of the settled dispute.
- Registration with the court: if the settlement resolves pending court proceedings, it must be presented to the court for the case to be dismissed.

## Drafting standards

- **Define the release scope with precision.** The single most common failure in settlement agreements is a vague release that does not cover the actual claims in dispute. Draft a release that specifically describes the dispute (referring to contract, date, claim type) and states that the release covers all claims arising from that dispute, whether known or unknown.
- **Consent judgment mechanism.** For settlements involving installment payments, include a consent judgment clause: if the paying party defaults on any installment, the receiving party may enter judgment for the entire unpaid balance without further proceedings.
- **Tax legal review.** Settlement payments may be subject to VAT (if they relate to a supply of services) or withholding tax in some jurisdictions. Flag this for tax counsel review.
- **No admission clause.** Always include; it is standard and both parties' lawyers will expect it.

## Common mistakes

- **Releasing claims without specifying their scope.** A release of "all claims" between parties with a long commercial relationship may release far more than the disputed matter — and may be challenged as signed under duress or without adequate consideration for the broader release.
- **Omitting dismissal mechanics.** Agreeing to settle but not specifying how and when pending proceedings will be dismissed leaves the other party with leverage and the claimant with enforcement risk.
- **No payment default mechanism.** Settlement agreements without a default consequence for non-payment are unenforceable without further litigation.
- **Confidentiality clause without carve-outs.** A clause that prohibits disclosure to tax authorities or regulators is unenforceable and may expose the parties to sanctions; include standard carve-outs.

## Related skills

- [[prompt-pack-settlement-agreement-template]]
- [[prompt-pack-statement-of-claim]]
- [[prompt-pack-statement-of-defense]]
- [[prompt-pack-professional-email-draft]]
- [[heuristic-always-state-jurisdiction-first]]
