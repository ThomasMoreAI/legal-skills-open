---
name: prompt-pack-patent-license-agreement-sboghossian
title: Patent License Agreement
description: 'Use when drafting a patent licence agreement granting exclusive or non-exclusive rights to specified patents. Covers field of use, territory, royalty structure, sublicensing, improvements, enforcement obligations, validity representations, and termination. MENA-aware: addresses patent registration and recordation requirements in UAE (ESMA/MOCCAE), KSA (SAIP), and relevant cross-border licensing structures through DIFC/ADGM.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-patent-license-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Patent License Agreement

## When to use this

Use this skill when a patent holder (Licensor) wants to grant rights to use specified patents to another party (Licensee) without transferring ownership. Patent licences are central to technology commercialization, standard-essential patent (SEP) licensing, cross-licensing, R&D collaboration, and manufacturing arrangements.

**Key distinction from assignment**: A licence grants the right to use the patent; title remains with the Licensor. For a full transfer of ownership, use [[prompt-pack-ip-assignment-agreement]].

Triggers:
- "Draft a patent licence for [Licensor] to grant rights to [Licensee] to use [Patent Number(s)]."
- "We want to license our manufacturing process patent on an exclusive basis."
- "Draft a cross-licensing agreement where both parties grant licences to each other."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Licensor and Licensee names | Identifies the parties | Ask user |
| Licensed Patents | Patent numbers, titles, jurisdictions | Ask user — must be specific; attach a schedule |
| Exclusivity | Exclusive / non-exclusive / sole licence | Ask user |
| Field of use | Limits or scopes the licence to specific applications | Ask user; if omitted, the licence is not field-limited |
| Territory | Countries where the licence is effective | Ask user; if omitted, worldwide |
| Royalty structure | Basis for compensation | Ask user |
| Governing law | Determines contract interpretation and available remedies | Jurisdiction of Licensor's principal place of business |

## Optional inputs

- Sublicensing rights (may sublicense to Affiliates / third parties)
- Grant-back clause (improvements made by Licensee feed back to Licensor)
- Milestones or minimum royalties (maintain exclusivity)
- Most-favoured licensee clause
- Step-down royalties on expiry of key patents
- Cross-licence arrangement

## Document structure

### 1. Definitions
Define clearly: "Affiliate," "Field of Use," "Licensed Patents," "Licensed Products," "Net Sales," "Royalty," "Territory," "Sublicensee," "Improvement."

The definition of "Net Sales" is critical for royalty calculation — define precisely: gross revenues less (i) trade discounts actually taken; (ii) returns; (iii) freight/insurance if separately invoiced; (iv) taxes collected from customers. List the permitted deductions explicitly and nothing else.

### 2. Grant of Licence

**Non-exclusive licence**:
> "[Licensor] hereby grants to [Licensee] a non-exclusive, non-transferable [and non-sublicensable] licence under the Licensed Patents to make, have made, use, sell, offer for sale, and import Licensed Products within the Field of Use in the Territory."

**Exclusive licence**:
> "[Licensor] hereby grants to [Licensee] an exclusive licence under the Licensed Patents to make, have made, use, sell, offer for sale, and import Licensed Products within the Field of Use in the Territory. Licensor retains the right to practice the Licensed Patents for internal research and development purposes only."

**Note on exclusivity**: An exclusive licence in a specific field or territory is a powerful tool; the licensor cannot grant the same rights to anyone else. In exchange, licensees often pay higher royalties or commit to minimum royalties to maintain exclusivity.

**"Have made" right**: Include this right if Licensee may want to engage contract manufacturers or toll manufacturers. Without "have made" rights, Licensee cannot outsource manufacturing of licensed products.

### 3. Sublicensing
- If sublicensing is permitted: state whether it applies to Affiliates only or extends to third parties; require that sublicences are consistent with the licence terms; Licensee remains responsible for sublicensee compliance.
- If sublicensing is not permitted: state clearly "Licensee may not sublicense the Licensed Patents to any third party without [Licensor's] prior written consent."
- Sublicensee obligations: all sublicences must flow down the material obligations of this agreement; Licensee must provide Licensor with a copy of each sublicence upon request.

### 4. Royalties and Payments

**Running royalty**:
- Rate: [X]% of Net Sales of Licensed Products
- Reporting: Licensee must submit quarterly royalty reports within [30] days after the end of each quarter showing: units sold, gross revenues, permitted deductions, Net Sales, royalty owed
- Payment: within [30 / 45] days of each quarterly report

**Upfront licence fee** (non-refundable):
- A one-time, non-refundable licence initiation fee of [USD X] due upon execution; not creditable against running royalties

**Minimum annual royalties** (for exclusive licences):
- To maintain exclusivity, Licensee must pay minimum annual royalties of [USD X] per year, starting in Year [2] of the licence term; if actual royalties fall short, Licensee must top up to the minimum
- Failure to pay minimum royalties: Licensor may convert the licence to non-exclusive or terminate

**Milestone payments** (for R&D stage licences):
- Upon [first regulatory submission]: USD [X]
- Upon [first regulatory approval]: USD [X]
- Upon [first commercial sale]: USD [X]

### 5. Audit Rights
- Licensee must keep accurate records sufficient to calculate and verify royalties
- Licensor (or its designated accountant) may audit Licensee's records [once per year] on [30-day] notice, during business hours
- If audit reveals an underpayment of more than [5 / 10]%, Licensee pays the deficiency plus interest [at [LIBOR + X%] / at [X]% per annum from the due date] and bears the audit cost

### 6. Patent Prosecution and Maintenance

**Licensor obligations**:
- Licensor shall use commercially reasonable efforts to maintain the Licensed Patents in force in the Territory, including payment of maintenance fees and annuities
- Licensor shall promptly notify Licensee of any final decision to abandon any Licensed Patent

**Licensee rights**:
- If Licensor decides to abandon a Licensed Patent, Licensee may, at its option and expense, take over prosecution and maintenance; Licensor must cooperate and execute any necessary documents

**Cost-sharing**:
- Option: Licensee pays [X]% of prosecution and maintenance costs for exclusively licensed patents; Licensor controls prosecution

### 7. Improvements

**Licensor improvements**: Any improvements to the Licensed Patents made by Licensor during the licence term are automatically included in the licence grant ("Improvements Included" model); or must be licensed separately ("No Automatic Grant" model) — choose based on the commercial deal.

**Licensee improvements (grant-back)**:
- If a grant-back is included, Licensee grants Licensor a [non-exclusive / exclusive] licence to any improvements made by Licensee to the Licensed Patents during the term
- Note: grant-backs can create antitrust / competition law concerns in the EU and US if the patent licensor has market power; ensure the grant-back is non-exclusive or subject to FRAND terms

### 8. Infringement and Enforcement

**Notification**: Each party shall promptly notify the other of any known or suspected infringement of the Licensed Patents by a third party.

**Enforcement rights**:
- Primary right: [Licensor / Licensee] has the first right to initiate and control enforcement proceedings against infringers of the Licensed Patents in the Territory
- Secondary right: if the party with the first right does not initiate proceedings within [90 / 180] days of notification, the other party may do so

**Costs and recoveries**:
- Enforcement costs borne by the party initiating proceedings
- Recoveries from infringement proceedings: first applied to reimburse enforcement costs; balance shared in [agreed ratio, e.g., 70/30 or pro-rata to royalty rate]

**Assistance**: Each party shall provide reasonable assistance, at the other's cost, in enforcement proceedings.

### 9. Representations and Warranties of Licensor

- Licensor has the right and authority to grant the licence
- The Licensed Patents are in force and, to Licensor's knowledge, valid
- Licensor is not aware of any claim that the Licensed Patents are invalid or unenforceable
- No prior licences granted conflict with the grant to Licensee (for exclusive licences)
- To Licensor's knowledge, practicing the Licensed Patents in the Field of Use does not infringe any third-party IP rights

**Disclaimer**: "EXCEPT AS EXPRESSLY SET OUT ABOVE, LICENSOR MAKES NO WARRANTY, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY WARRANTY OF NON-INFRINGEMENT, FITNESS FOR A PARTICULAR PURPOSE, OR MERCHANTABILITY."

### 10. Indemnification
- Licensor indemnifies Licensee against third-party claims that the Licensed Patents are owned by a third party (title defect claims)
- Licensee indemnifies Licensor against claims arising from Licensee's exercise of the licence or Licensee's Licensed Products

### 11. Term and Termination

**Term**: The licence commences on the effective date and continues until the expiry or abandonment of the last to expire of the Licensed Patents, unless earlier terminated.

**Termination for cause**:
- Either party may terminate on [30-day] written notice for material breach, if not cured within the notice period
- Licensor may terminate immediately on insolvency of Licensee
- Licensor may terminate immediately if Licensee challenges the validity of any Licensed Patent (anti-challenge clause — note this may be unenforceable in EU under competition law; omit or tailor for EU governing law)

**Effect of termination**: Licensee must cease all use of the Licensed Patents; all sublicences (if permitted) terminate simultaneously unless Licensor elects to assume them directly.

### 12. Governing Law, Dispute Resolution, and Recordation
- Governing law: choose carefully for cross-border licences; DIFC or ADGM law for MENA cross-border transactions
- Dispute resolution: arbitration (ICC / LCIA / DIAC) with a seat in [DIFC / Dubai / London]
- **Recordation**: state which party is responsible for recording the licence with the relevant patent offices; Licensee (especially for exclusive licences) has a strong interest in recording to establish priority

## Jurisdictional notes

| Jurisdiction | Key points |
|---|---|
| **UAE** | Patent licences should be recorded with the UAE Ministry of Economy (MoE) through the Emirates Intellectual Property Association (ESMA) to be enforceable against third parties; Arabic-language version may be required. |
| **KSA** | Patent licences recorded with SAIP; Arabic-language licence deed required for official recording; SAIP processing timelines vary. |
| **DIFC / ADGM** | English-law governed licence; recordation with DIFC / ADGM IP registry; sophisticated enforcement through DIFC / ADGM Courts or arbitration. |
| **EU (competition law)** | Technology Transfer Block Exemption Regulation (TTBER) provides safe harbours for patent licences; anti-challenge clauses are generally unenforceable for exclusive licences under EU competition law. |
| **US** | Federal circuit court law on patent licences; recording at USPTO recommended for exclusive licences; anti-challenge clauses are permitted for non-exclusive licences in many circuits. |

## Common mistakes

- **Vague "Licensed Patents" definition**: schedule of patent numbers must be attached; a generic "all patents owned by Licensor relating to X" creates scope disputes.
- **No "have made" right**: if Licensee needs to outsource manufacturing, the "have made" right is essential; its omission is a common oversight.
- **Minimum royalty without termination mechanism**: minimum royalties without a clear remedy (conversion to non-exclusive, termination) are unenforceable incentives.
- **No audit provision**: without audit rights, Licensor cannot verify royalty reports; underpayments go undetected.
- **Anti-challenge clause in EU context**: including a termination-on-challenge clause for exclusive licences in an EU-governed agreement may violate EU competition law.

## Related skills

- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-ip-due-diligence-checklist]]
- [[prompt-pack-open-source-compliance-review]]
- [[prompt-pack-nda-strength-check]]
- [[heuristic-always-state-jurisdiction-first]]
