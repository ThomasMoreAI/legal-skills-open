---
name: prompt-pack-technology-licensing-agreement-sboghossian
title: Technology Licensing Agreement
description: Use when a licensor needs to grant a licensee rights to use technology (patents, software, know-how, trade secrets, technical processes) on an exclusive or non-exclusive basis in a defined territory. Covers license scope, sublicensing, royalty structures, IP ownership, warranties, indemnification, and audit rights. MENA-specific guidance addresses patent registration enforceability in UAE and KSA, technology license approval requirements, know-how protection, and Sharia-compliant royalty structures.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-technology-licensing-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Technology Licensing Agreement

## When to use this

Use this skill when:
- A technology owner (licensor) wants to allow another party (licensee) to use its technology in exchange for royalties or other consideration, without permanently transferring ownership.
- A company is expanding into a new territory and licensing its technology to a local partner rather than establishing a subsidiary.
- A patent holder is monetizing its patents through a licensing program.
- A company holds know-how or trade secrets (manufacturing processes, formulas, methods) that it wants to license commercially.
- A joint venture involves each party contributing technology for use in the JV entity under a licensing structure.

**Distinguish from:** A software license agreement (use [[prompt-pack-software-license-agreement]]) for software code specifically; a technology transfer agreement (use [[prompt-pack-technology-transfer-agreement]]) for permanent transfer of ownership; a research collaboration agreement (use [[prompt-pack-research-collaboration-agreement]]) for joint development.

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| **Licensor and licensee identities** | Determines IP filing obligations, tax treatment of royalties, withholding tax | Ask |
| **Technology description** | What is being licensed? Patents, know-how, software, trade secrets, technical processes, or all of the above? | Ask; list specifically |
| **License scope** | Exclusive vs. non-exclusive; territory; field of use; sub-licensing rights | Ask; all four dimensions are commercially significant |
| **Royalty structure** | Fixed fee; per-unit royalty; percentage of revenue; milestone payments | Ask |
| **Jurisdiction / governing law** | Determines patent protection, trade secret protection, enforceability | Ask |

## Optional inputs

- **Patent portfolio details** — if the licensed technology includes patents, list them (by registration number and jurisdiction) in a Schedule; unregistered patents or pending applications need to be characterized accurately.
- **Know-how delivery** — if the license includes know-how, specify how it will be delivered (technical documentation, training, on-site assistance).
- **Improvements** — who owns improvements the licensee makes to the licensed technology (grant-back provisions)?
- **Export control** — if the technology is dual-use or subject to US EAR or EU dual-use controls, include compliance provisions.
- **Non-compete / field of use restriction** — prevent the licensee from using the technology in competition with the licensor outside the agreed field of use.

## Document structure

1. **Definitions**
   - **Licensed Technology:** [specifically described technology, including all patents listed in Schedule A, know-how, and technical documentation].
   - **Licensed Territory:** [geographic area; or "worldwide"].
   - **Field of Use:** [specific application or industry segment in which the license is granted; if unrestricted, state "all fields of use"].
   - **Improvements:** any modification, enhancement, or derivative of the Licensed Technology created by either party during the term.
   - **Net Revenue / Net Sales:** the basis for royalty calculation (define carefully — is this gross revenue minus returns? minus taxes? minus sub-distributor payments?).
   - **Royalty Rate, Milestone Payments.**

2. **Grant of license**
   - Licensor grants to Licensee a [exclusive / non-exclusive], [sublicensable / non-sublicensable], [perpetual / term] license to use the Licensed Technology in the Licensed Territory for the Field of Use.
   - **Exclusivity mechanics:** if exclusive, the licensor cannot grant the same rights to a third party in the same territory and field of use during the license term. Exclusivity commands a higher royalty and often a minimum royalty guarantee.
   - **Sub-licensing:** if permitted, specify: (a) sub-licensee must be a third party agreeing to be bound by terms at least as protective as this Agreement; (b) licensor must be notified; (c) licensee remains liable for sub-licensee's compliance.
   - **Affiliates:** licensee's affiliates may typically be extended license rights without a sub-license; specify which affiliates and conditions.

3. **License fees and royalties**

   *Structure A — Upfront license fee + ongoing royalties:*
   - Upfront fee: [amount] due on execution.
   - Running royalty: [X%] of Net Revenue on all products incorporating the Licensed Technology, payable [quarterly/semi-annually].

   *Structure B — Milestone payments:*
   - Milestone 1: [event: first commercial use] → [payment].
   - Milestone 2: [event: first USD X million in revenue] → [payment].

   *Structure C — Minimum royalties:*
   - Annual minimum royalty: [amount]; if actual royalties fall below the minimum, licensee pays the minimum.
   - For exclusive licenses: minimum royalties are the licensor's protection against a licensee that "shelves" the technology.

   *Royalty calculation:*
   - Royalty base: Net Revenue = Gross Revenue from sales of Licensed Products minus [returns, VAT, government levies].
   - Stacking royalties: if the licensee also licenses technology from third parties for the same product, negotiate a stacking clause to prevent the aggregate royalty burden from exceeding a commercial threshold.
   - Most Favored Licensee: licensor agrees not to grant more favorable terms to other licensees in the same territory and field; or conversely, this clause is excluded (licensor's negotiating preference).

4. **Royalty reporting and payment**
   - Licensee submits royalty reports within [30/45] days of each quarter-end, stating: number of licensed products sold; revenue; royalties due.
   - Payment accompanies each report.
   - Currency: [USD / AED / SAR / EUR].
   - Late payment: interest at [rate]% from due date; check KSA for conventional interest limitation.
   - **Withholding tax:** in many MENA jurisdictions, royalty payments to foreign licensors are subject to withholding tax (UAE: no WHT on royalties to non-residents generally; KSA: 15% WHT on royalties unless reduced by tax treaty; verify current rates). Clarify whether royalties are gross or net of withholding.

5. **Know-how delivery and training**
   - Licensor will deliver technical documentation describing the Licensed Technology within [X] days of execution.
   - Licensor will provide up to [X hours/days] of technical training to licensee's personnel.
   - Ongoing technical support: [specify; or state "not included; available on request at licensor's then-current rates"].
   - Know-how updates: licensor will provide updates to the know-how during the term at [no charge / agreed rates].

6. **IP ownership and improvements**
   - Licensed Technology: owned by licensor; this Agreement does not transfer ownership.
   - Improvements by Licensor: remain owned by licensor; may (or may not) be automatically included in the license.
   - Improvements by Licensee:
     - *Licensor-favorable:* all improvements by licensee are owned by licensor; licensee receives a non-exclusive license.
     - *Licensee-favorable:* improvements made solely by licensee are owned by licensee; licensor receives a non-exclusive license ("grant-back").
     - *Compromise:* improvements jointly developed are jointly owned; solely developed improvements are owned by the developing party.
   - Patent filing: if the licensee discovers a new patentable invention based on the licensed technology, who files? Who owns? Specify.

7. **Record-keeping and audit rights**
   - Licensee must maintain complete, accurate records of all sales of licensed products and royalty calculations for [5] years.
   - Licensor may audit: once per year; 30 days' notice; at licensor's cost unless underpayment exceeds [X%] of royalties due.
   - If audit reveals underpayment: licensee pays deficit plus [10%] penalty on the shortfall; if material underpayment (above [Y%]), licensor may terminate.

8. **IP maintenance and protection**
   - Licensed Patents: licensor is responsible for maintaining patents and paying renewal fees. If licensor decides to abandon a patent, it must notify licensee; licensee may elect to maintain it at its own cost.
   - Enforcement: if a third party infringes the Licensed Technology, either party may notify the other. Licensor has the primary right to enforce; if licensor declines, licensee may enforce (subject to licensor's consent; costs and recoveries to be agreed).
   - Infringement by licensee: immediate termination right.

9. **Licensor's representations and warranties**
   - Licensor is the owner of the Licensed Technology and has the right to grant this license.
   - The Licensed Technology does not infringe the IP rights of any third party to licensor's knowledge.
   - Licensed patents are valid and subsisting (within the limits of the licensor's knowledge; patent validity is a matter of law that can change).
   - No other exclusive license has been granted for the same technology in the licensed territory and field of use (if this is an exclusive license).

10. **IP indemnification**
    - Licensor indemnifies licensee against third-party IP infringement claims arising from licensee's permitted use of the Licensed Technology.
    - Exclusions: claims arising from licensee's modifications, combination with other technology, or use outside the permitted field/territory.
    - Licensee must: notify licensor promptly; cooperate; give licensor sole control of defense.

11. **Confidentiality**
    - Both parties treat the Licensed Technology (especially know-how and trade secrets) as confidential.
    - Licensee may disclose to employees, contractors, and sub-licensees who need to know and are bound by confidentiality.
    - Post-termination: know-how confidentiality obligations survive for [5] years; trade secrets survive indefinitely.

12. **Term and termination**
    - Term: [5/10/15 years / perpetual].
    - Termination for cause: material breach; insolvency; challenge to licensed IP validity by licensee (many licensors include a "patent challenge termination" clause — terminable if licensee challenges the validity of the licensed patents).
    - Termination for convenience: [X months'] notice.
    - Effect: licensee must cease use; return or destroy confidential know-how materials; pay all outstanding royalties.

13. **Governing law and dispute resolution** — arbitration preferred for international licenses.

## Jurisdictional notes

### UAE — Patents and Know-how
- UAE Patent Law (Federal Law No. 11 of 2021 on Industrial Property): patents protecting inventions; technology licenses involving registered UAE patents should be recorded with the Ministry of Economy for third-party enforceability.
- Know-how: protected under trade secret principles (Art. 3 of the Federal Law on Trade Secrets) and contractual confidentiality obligations.
- Technology licensing agreements with foreign licensors may require registration with the Ministry of Economy under the Commercial Agencies framework — **only** if the arrangement creates an "agency" relationship; pure IP licenses are generally not commercial agencies.

### KSA
- Patent protection through Saudi Authority for Intellectual Property (SAIP).
- Technology license agreements may require registration with MISA for enforcement against third parties.
- Withholding tax: 15% WHT on royalties paid to non-residents (unless a tax treaty reduces this); the license agreement should address gross-up obligations.
- No conventional interest on late royalties; structure as delay compensation.

### DIFC / ADGM
- IP protected under DIFC IP Law (DIFC Law No. 4 of 2019).
- Technology license agreements are freely enforceable as contracts.
- No WHT on royalties paid from DIFC or ADGM entities (generally).

### EU
- Technology Transfer Block Exemption Regulation (TTBER — Commission Regulation (EU) 2022/720): safe harbor for technology licensing agreements between competitors and non-competitors meeting defined conditions; review for EU competition law compliance.
- GDPR: if the technology processes personal data, a data processing agreement is needed.

## Drafting standards

- The royalty calculation clause is the most commercially sensitive and most litigated provision; draft it with mathematical precision.
- The field of use restriction is a significant commercial choice: an exclusive license in a narrow field is very different from an exclusive worldwide all-fields license.
- Improvement ownership (grant-back provisions) should be negotiated explicitly; avoid ambiguity.
- For know-how licenses: the know-how must be described with enough specificity to be enforceable; "all licensor's know-how related to [product]" is unenforceable without further definition.

## Common mistakes

- **No minimum royalties in an exclusive license.** Without minimum royalties, the licensee can effectively sit on the technology and prevent the licensor from licensing to anyone else.
- **Improvements not addressed.** Without explicit improvements language, disputes will arise about who owns modifications to the licensed technology.
- **Withholding tax not addressed.** If the licensee's jurisdiction imposes WHT on royalties, the agreement must say whether the royalty is gross or net; otherwise the licensor receives less than expected.
- **Patent challenge clause omitted.** Without it, the licensee can continue to use the technology while simultaneously challenging the patent's validity — a risk licensor must address.

## Related skills

- [[prompt-pack-software-license-agreement]]
- [[prompt-pack-technology-transfer-agreement]]
- [[prompt-pack-research-collaboration-agreement]]
- [[prompt-pack-standard-nda]]
- [[heuristic-always-state-jurisdiction-first]]
