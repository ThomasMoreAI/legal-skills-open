# Legal to Plain-Language Transformations

This reference catalogs common transformations from legal-jargon-heavy text to plain language. The transformations are heuristics, not rules — context determines whether each transformation preserves meaning.

The skill applies transformations selectively. Some legal terms have precise meaning that should be preserved; others are jargon habits that can be simplified without loss. The judgment is whether the simplified version means the same thing in the relevant context.

## Sentence structure transformations

### Long compound sentences → multiple shorter sentences

**Original:** "In the event that the Customer fails to make any payment when due hereunder, the Supplier may, after providing written notice and an opportunity to cure as set forth in Section 13.4, suspend the provision of Services until such time as the past-due amount is paid in full, including any applicable late fees and interest accrued thereon."

**Plain:** "If the customer is late on payment, the supplier can suspend service after giving notice and a chance to fix the issue. The customer must pay the past-due amount, including late fees and interest, before service resumes."

**What changed:** one 53-word sentence → two sentences, 19 and 17 words. The compound conditional ("In the event that... after providing... until such time as... including") was unbundled into chronological steps. "Hereunder" eliminated. "Such time as" → "before service resumes." The legal substance is preserved.

### Passive voice → active voice

**Original:** "Notice shall be deemed to have been given upon receipt by the Receiving Party."

**Plain:** "Notice is given when the receiving party receives it."

**What changed:** passive ("shall be deemed to have been given") → active ("is given"). "Upon receipt by" → "when [party] receives." The legal substance is preserved.

**Edge case:** sometimes passive voice is appropriate to avoid attributing fault or to keep the actor unspecified ("personal data was disclosed in violation of the agreement" rather than "[specific party] disclosed personal data"). The skill preserves passive voice where the original's choice serves a purpose.

### Inverted structures → direct statement

**Original:** "Notwithstanding anything to the contrary in this Agreement, the limitation of liability set forth in Section 8.1 shall not apply to claims arising out of a party's breach of confidentiality obligations."

**Plain:** "The liability cap in Section 8.1 doesn't apply to claims about confidentiality breaches. This is true regardless of any other provisions in this Agreement."

**What changed:** "Notwithstanding anything to the contrary" leads the original — the contradiction-protection clause comes first. Plain version leads with the substantive point and adds the contradiction-protection as a follow-up sentence. The legal substance is preserved.

## Word-level transformations

### Common simplifications

| Legal | Plain |
|---|---|
| utilize / utilize | use |
| commence | start, begin |
| terminate | end |
| in the event that | if |
| pursuant to | under |
| notwithstanding | even though, despite |
| heretofore | until now |
| hereinafter | from here on, below |
| hereto | to this |
| thereto | to that |
| hereinabove | above |
| said [thing] | the [thing], that [thing] |
| inasmuch as | because, since |
| in order to | to |
| with respect to | about, regarding |
| in connection with | about, regarding, related to |
| prior to | before |
| subsequent to | after |
| at such time as | when |
| for the purpose of | to, for |
| in the absence of | without |
| in addition to | also |
| in the event of | if |
| for so long as | while, as long as |
| in lieu of | instead of |
| with regard to | about |
| for and in consideration of | for |

These simplifications almost always preserve meaning. The legal terms are habits, not terms of art.

### Terms of art that often warrant preservation

These terms have specific legal meaning that may not be preserved by simplification:

- **"Material breach"** — legal term with consequences for remedies; "serious problem" is not equivalent.
- **"Reasonable efforts" / "best efforts" / "commercially reasonable efforts"** — graduated standards with case law; "try hard" is not equivalent.
- **"Including without limitation"** — legal mechanism preventing the listed examples from being construed as exclusive; "including" alone may be construed as exclusive in some jurisdictions.
- **"Sole and exclusive remedy"** — language affecting whether other remedies are available; "the only remedy" may not capture the legal effect.
- **"Joint and several"** — distinct from "joint" or "several"; refers to liability allocation among multiple parties.
- **"Consequential damages" / "indirect damages" / "incidental damages" / "special damages"** — specific damage categories with case-law definitions; bundling them as "other damages" loses the categories.
- **"Force majeure"** — defined term often referring to specific events; "act of God" or "unforeseen circumstances" may not capture the operative scope.
- **"Indemnify, defend, and hold harmless"** — three distinct obligations; saying just "indemnify" may be narrower.
- **"Personal data" / "personal information"** — defined terms under specific privacy regimes (GDPR, CCPA); definitions matter.
- **"Sale" / "share" / "sell"** — under CCPA these have specific definitions broader than common usage.

When these terms appear in the original, the skill: (a) preserves them in the rewrite if `preserve_specific_terms` indicates; (b) flags them in the explanation otherwise, with a note about why preservation may matter.

### Defined terms

Many contracts use capitalized defined terms ("the Service," "Personal Data," "Confidential Information"). These are typically defined in a definitions section. Plain-language rewrites for non-legal audiences should:

- **Preserve the term verbatim if the rewrite is for a deal-team audience or other audience that needs to map back to the contract.**
- **Replace with a description if the rewrite is for an audience that won't see the contract.** "Personal Data" in a contract becomes "data that identifies a specific person" in a sales-team explanation.
- **Flag the choice in the explanation** so the user can verify.

## Structural transformations

### Lead with the bottom line

Legal text often builds: facts → analysis → conclusion. Plain-language audiences want: conclusion → reasoning → details.

**Original:** "Section 13.4 of the agreement provides that, in the event of any material breach by the Customer that remains uncured for a period of thirty (30) days following written notice from the Supplier, the Supplier may exercise its right to terminate the agreement and accelerate all unpaid amounts due thereunder."

**Plain:** "If the customer doesn't fix a serious breach within 30 days of being notified, the supplier can terminate the agreement and demand payment of all unpaid amounts. (Section 13.4)"

**What changed:** the bottom-line action ("supplier can terminate and demand payment") leads. The conditions and statutory citation follow. The legal substance is preserved.

### Replace conditional structures with concrete examples

**Original:** "The Service is intended for use by enterprise customers; consumer use may be subject to additional restrictions and may require separate consent under applicable law."

**Plain:** "The Service is built for businesses, not individual consumers. Different rules may apply if individual consumers use the Service."

**What changed:** "may be subject to" and "may require" are the legal hedge; the plain version replaces with "different rules may apply." The substance is preserved but lossiness is acknowledged.

### Replace abstract qualifications with concrete examples

**Original:** "Customer shall have the right to receive aggregated, anonymized data analytics outputs from the Service in accordance with industry-standard practices for data anonymization."

**Plain:** "Customer can receive analytics about how the Service is used, in summary form that doesn't identify any specific user. The standard for 'doesn't identify' follows industry practice for anonymization."

**What changed:** "in accordance with industry-standard practices for data anonymization" (abstract) → "the standard for 'doesn't identify' follows industry practice for anonymization" (concrete). The reader now understands what kind of data they get and what the anonymization standard is.

## Common pitfalls in plain-language rewriting

### Over-simplification that drops meaning

**Original:** "Indemnification under this Section is the sole and exclusive remedy for breach of the warranties set forth in Section 5.1."

**Bad rewrite:** "If the warranty is broken, indemnification is what you get."

**Why it's bad:** drops "sole and exclusive" — the operative legal effect is that other remedies (e.g., termination, additional damages) are not available. The plain version makes it sound like indemnification is *one* available remedy.

**Better rewrite:** "If the warranty is broken, indemnification is your only remedy. You can't seek termination, additional damages, or other recourse for that breach."

### Adding meaning the original didn't carry

**Original:** "The parties shall negotiate in good faith to resolve any disputes arising under this Agreement."

**Bad rewrite:** "We'll work together to fix problems and find solutions that work for everyone."

**Why it's bad:** adds "find solutions that work for everyone" — the original requires good-faith negotiation, not actual resolution. Plain version implies an outcome that the original doesn't promise.

**Better rewrite:** "If there's a dispute about the agreement, both parties will negotiate in good faith to try to resolve it."

### Translating legal terms whose precise meaning matters

**Original:** "Vendor shall promptly notify Customer of any Personal Data Breach as defined under applicable Data Protection Laws."

**Bad rewrite:** "If there's a data security incident, the vendor will tell us right away."

**Why it's bad:** "Personal Data Breach as defined under applicable Data Protection Laws" has a specific meaning under GDPR (loss of confidentiality, integrity, or availability of personal data, including unauthorized access) and CCPA (different scope). "Data security incident" is broader and includes events that may not trigger notification obligations.

**Better rewrite:** "If a Personal Data Breach happens (as defined by privacy law — basically, unauthorized access, loss, or change of personal data), the vendor will tell us right away." Or: "If there's a Personal Data Breach (a defined term), the vendor will tell us right away."

The judgment of when to preserve, simplify, or partially preserve depends on audience and use. The skill defaults to preserving terms with substantial legal weight and flagging the choice.
