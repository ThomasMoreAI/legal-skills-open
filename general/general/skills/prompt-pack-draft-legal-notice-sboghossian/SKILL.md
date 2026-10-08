---
name: prompt-pack-draft-legal-notice-sboghossian
title: Draft Legal Notice
description: Use when drafting a legally structured formal notice to another party — covering statement of facts, applicable legal provisions, specific demands, and consequences of non-compliance. Applicable to pre-litigation notices, contractual breach notices, demand letters, and regulatory compliance notices across MENA (UAE, KSA, LB, EG), UK, EU, and US. Trigger when a client needs to put a counterparty formally on notice before commencing legal action or exercising a contractual right.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-draft-legal-notice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Draft Legal Notice

## When to use this

Use this skill to produce a formal legal notice — a structured written communication from one party to another that establishes a legal record, triggers rights, or places the recipient in formal default. Legal notices serve critical functions: they start limitation clocks, trigger cure periods, preserve rights, and demonstrate that a party attempted to resolve a dispute before resorting to litigation or arbitration.

Typical triggers:
- Contractual breach requiring formal notice before termination rights arise
- Pre-litigation demand letter asserting a claim and requesting payment or specific performance
- Intellectual property infringement cease-and-desist notice
- Landlord/tenant or property notice (eviction, disrepair, quiet enjoyment)
- Employment dismissal notice or notice of disciplinary action
- Regulatory non-compliance notice to a licensee or supplier
- Notice of arbitration / notice of dispute triggering contractual dispute resolution clause

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Issuing party (sender) | Identity and capacity to issue the notice | Ask |
| Recipient party | Name, address, and contact details for service | Ask |
| Jurisdiction and governing law | Determines applicable notice requirements, formalities, and legal provisions to cite | Ask; critical |
| Subject matter / issue | The facts giving rise to the notice | Ask in detail |
| Specific demand or relief sought | What the recipient must do — pay X, cease Y, remedy Z | Ask |
| Deadline for compliance | Response or cure period | Ask; default is 14 days (reasonable in most jurisdictions) unless contract specifies |
| Contract or legal basis | Which agreement or legal provision is being invoked | Ask |

## Optional inputs

- Prior correspondence or course of dealing (to contextualize the notice)
- Expert or consultant evidence supporting the claim (reference only, do not attach)
- Amount claimed (with interest calculation method)
- Specific consequences of non-compliance (legal proceedings, termination, withholding payment)
- Service method requirements (registered mail, notary, bailiff — jurisdiction-specific)

## Document structure

1. **Header and reference** — Date; sender's name and address; recipient's name and address; reference number; subject line (e.g., "Notice of Breach / Clause 5.3 of the Service Agreement dated [date]").

2. **Background facts** — A concise, chronological statement of the relevant facts:
   - The contractual or legal relationship between the parties
   - The obligation the recipient has failed to perform
   - Dates, amounts, or specific conduct giving rise to the notice
   - Prior correspondence or notifications (if any)

3. **Legal basis** — Cite the specific contractual provisions and/or applicable law provisions being relied upon:
   - Relevant contract clauses (e.g., Clause 5.3 — payment obligation; Clause 12 — termination for breach)
   - Applicable statutory provisions (e.g., UAE Civil Transactions Law, Art. [X]; Lebanese Code of Obligations and Contracts, Art. [X])
   - Do not fabricate article numbers; cite the framework by name if specific numbers are not confirmed

4. **The demand** — Clear, unambiguous statement of what the recipient must do:
   - "We hereby demand that you [pay the sum of USD X / cease and desist from / remedy the breach by doing Y] within [14] days from the date of this notice."

5. **Consequences of non-compliance** — What happens if the demand is not met:
   - Commencement of legal proceedings / arbitration
   - Termination of the contract
   - Exercise of security or set-off rights
   - Referral to regulatory authority
   - Accrual of default interest

6. **Reservation of rights** — Standard reservation: "This notice is without prejudice to any other rights or remedies available to [Sender] under the agreement, applicable law, or otherwise."

7. **Signature and authorization** — Signed by authorized representative; include position/title.

## Jurisdictional notes

### Service of notice requirements

| Jurisdiction | Recommended service method | Notes |
|---|---|---|
| **UAE** | Registered courier (DHL/FedEx) with delivery confirmation; notarial service (Tawtheeq) for high-stakes notices | Many contracts require notice by specific method; check clause before serving |
| **KSA** | Courier with receipt; in some cases notary public authentication | Ministry of Justice notary service for formal notices |
| **Lebanon** | Bailiff service (huissier de justice) for formal legal effect; registered post also common | Bailiff service is preferred before litigation; establishes date of service definitively |
| **Egypt** | Official notification through court bailiff (recommended for pre-litigation); registered mail also accepted | Egyptian courts may require proof of receipt |
| **DIFC / ADGM** | Service by email, courier, or as specified in the contract | DIFC/ADGM contracts often specify email as valid service |
| **UK** | Contractual notice clause governs; personal delivery or first-class post to registered office | Companies Act 2006 sets default rules for service on companies |
| **France / EU** | Huissier (bailiff) for formal notices with legal effect; registered letter with acknowledgment receipt for contract notices | "Mise en demeure" — formal demand letter — starts running breach cure periods |

### Pre-litigation notice requirements

Several jurisdictions and sectors impose mandatory pre-litigation notice requirements:
- **UAE**: UAE Civil Procedure Law requires a formal notification before filing many types of civil claims; 15-day warning notice is required before filing a bounced-cheque case.
- **Lebanon**: In tenancy and certain commercial disputes, the notice period must comply with specific statutory minimums.
- **KSA**: Commercial courts encourage (and sometimes require) pre-action correspondence; arbitration clauses requiring notice of dispute before arbitration commencement must be honored.
- **France**: "Lettre recommandée avec accusé de réception" (LRAR — registered letter with acknowledgment of receipt) is the standard; formal notice by huissier is required for some lease and employment situations.

## Drafting standards

- Keep the factual section accurate and specific — this document may become an exhibit in later proceedings.
- Avoid inflammatory language; maintain a formal, professional tone throughout.
- Do not include legal threats that cannot be acted upon — empty threats undermine credibility.
- Cite specific contractual clause numbers and dates; do not cite generic "your agreement to comply."
- The demand must be unambiguous: the recipient must know exactly what to do and by when.
- Include the sender's contact details for the recipient to respond to.
- In civil-law jurisdictions, the notice that starts a cure period or puts a party in default (mise en demeure) must be unequivocal and give a reasonable deadline.

## Common mistakes

- **No specific legal basis**: A notice that merely says "you are in breach" without citing the clause or law is legally weak and may not start cure periods.
- **Wrong service method**: If the contract requires service by registered mail and you send by email, the notice may be legally ineffective.
- **Inadequate cure period**: Giving 24 hours to cure a complex breach is unlikely to be upheld; most courts and arbitral tribunals look for a reasonable cure period.
- **Missing reservation of rights**: Without this clause, the notice may be construed as an election of a single remedy, potentially waiving others.
- **Disclosing privileged information**: Notices should reference facts, not legal strategy. Do not include privileged legal advice or litigation strategy in the notice.
- **Inconsistency with prior correspondence**: If prior letters took inconsistent positions, the notice can be used against the sender in proceedings.

## Related skills

- [[prompt-pack-draft-reply-to-department-notice]]
- [[prompt-pack-injunction-application]]
- [[prompt-pack-enforcement-of-judgment]]
- [[prompt-pack-discovery-request]]
