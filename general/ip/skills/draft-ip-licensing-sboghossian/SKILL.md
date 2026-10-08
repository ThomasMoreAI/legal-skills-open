---
name: draft-ip-licensing-sboghossian
title: IP Licensing Agreement
description: Use when drafting an intellectual property licensing agreement that grants rights to use a patent, trademark, copyright, trade secret, or software. Covers exclusive, sole, and non-exclusive licenses across any territory and field of use, with full attention to royalty structures, audit rights, improvement ownership, and MENA-specific enforceability traps (commercial agency law, gharar, SAIP registration). Triggers on phrases like "ip license", "licensing agreement", "royalty deal", or "technology transfer".
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-ip-licensing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP Licensing Agreement

## When to use this

Use this skill whenever a party wishes to grant another party rights to use intellectual property — a patent, trademark, copyright, trade secret, know-how, or software — while retaining ownership. Common triggers:

- A technology owner licensing manufacturing rights to a local distributor or OEM in a new market
- A software vendor granting named-user or field-of-use rights across multiple territories
- A brand licensing a trademark to a franchisee or co-manufacturer
- A research institution licensing a patent to a commercialization partner in exchange for milestone payments and royalties
- A content owner licensing copyright for adaptation, translation, or synchronization

If the goal is to permanently transfer ownership rather than grant a use right, use [[draft-ip-assignment]] instead.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Licensor + Licensee | Party identification, entity type, registration | — must supply |
| Licensed IP (precise description, registration numbers) | Defines what is licensed; ambiguity = scope disputes | — must supply |
| Field of use | Limits licensee to a defined market or application; allows licensor to license other fields separately | All fields (if licensor accepts) |
| Territory | Governs where the licensee may exploit the IP | Worldwide (if licensor accepts) |
| Exclusivity level | Exclusive / sole / non-exclusive | Non-exclusive |
| Term | Duration of the license | 3 years, automatically renewable |
| Royalty structure | Fixed fee / % of net sales / milestone / hybrid | % of net sales; define Net Sales carefully |
| Sublicense rights | Can the licensee grant sub-licenses? | No sublicensing without prior written consent |

## Optional inputs

- Minimum annual royalty (MAR) — guarantees the licensor a floor regardless of licensee's sales volume
- Most-favored-licensee clause — licensor cannot grant third parties better terms
- Grantback provisions — whether licensee-developed improvements are licensed back
- Step-in rights — licensor can take control of prosecution or enforcement if licensee defaults
- Source-code escrow (for software licensing)
- Quality-control standards (mandatory for trademark licenses to prevent naked-license invalidity)

## Document structure

1. **Recitals** — Identify the parties, the IP, and the transaction purpose.
2. **Definitions** — Licensed IP, Territory, Field of Use, Net Sales, Royalty, Sublicensee, Affiliate, Improvement, Background IP, Foreground IP. Precision here prevents every subsequent dispute.
3. **Grant of license** — Scope must enumerate the bundle of rights conveyed (make, use, sell, import, sublicense, reproduce, distribute, perform, display — pick what applies). State exclusivity plainly.
4. **Reservations** — Licensor retains all rights not expressly granted. Express reservation is belt-and-suspenders protection.
5. **Sublicensing** — If permitted, conditions (written approval, flow-down of obligations, licensor approval of sublicensee). Licensor should have audit rights over sublicensees.
6. **Royalty, payment, and reporting**
   - Royalty rate and base (% of Net Sales; define Net Sales precisely — see Royalty pitfalls below)
   - Milestone payments (on patent grant, regulatory approval, commercial launch, annual thresholds)
   - Payment schedule and currency
   - Late payment interest
   - Quarterly royalty reports with supporting detail
7. **Audit rights** — Licensee keeps records for 3 years; Licensor may audit 1-2×/year on 30-day notice; licensee bears cost if discrepancy exceeds 5% of reported royalties.
8. **IP maintenance and prosecution**
   - Who pays patent/trademark maintenance fees?
   - Who controls prosecution before the patent office?
   - Consultation rights on claim amendments?
   - What happens if licensor decides to abandon IP?
9. **Improvements and new developments**
   - Background IP: each party's pre-existing IP — neither party acquires rights to the other's background IP unless expressly stated.
   - Foreground IP: developments arising from the license relationship — ownership and license-back must be expressly allocated.
   - Grantback: if licensor takes a license back on licensee's improvements, it should be non-exclusive and royalty-free (exclusive grantbacks can raise competition-law issues).
10. **Infringement enforcement**
    - Who has the primary right to sue infringers? (Often licensor, sometimes exclusive licensee with standing)
    - Cost-sharing and recovery allocation
    - Notification obligations; licensee must promptly notify licensor of known infringement
11. **Representations and warranties**
    - Licensor: owns the IP, no encumbrances, no pending litigation, IP is valid and enforceable (to licensor's knowledge)
    - Licensee: duly incorporated, has authority, will comply with applicable laws
    - Note: licensor rarely warrants non-infringement of third-party rights — expensive and risky
12. **Indemnification** — See [[review-indemnification-balance]].
    - Licensor indemnifies licensee for infringement claims arising from the licensed IP itself (cap usually at royalties paid)
    - Licensee indemnifies licensor for modifications made by licensee, uses beyond permitted scope
13. **Term and termination**
    - Fixed term with renewal option; or perpetual with termination rights
    - Termination for breach with cure period (30-60 days)
    - Termination for non-payment (10-15 days notice)
    - Termination for insolvency (immediate or at licensor's election)
    - Licensor's right to terminate if licensee challenges validity of licensed IP (anti-challenge clause — valid in some jurisdictions, void in others)
14. **Post-termination obligations**
    - Licensee immediately ceases use of Licensed IP
    - Sell-off period for existing inventory (typically 90-180 days)
    - Return or certified destruction of materials; deletion of digital copies
    - Royalty obligations survive through sell-off period
    - Surviving clauses (audit, confidentiality, indemnification)
15. **Confidentiality** — Trade secrets and know-how component survive termination; standard NDA-grade obligations.
16. **Governing law and dispute resolution** — Arbitration recommended for cross-border; seat and rules must be specified.
17. **Boilerplate** — see [[draft-boilerplate-clauses]]: force majeure, severability, entire agreement, no waiver, notices.

## Jurisdictional notes

| Jurisdiction | Key issues |
|---|---|
| **DIFC / ADGM** | Standard common-law IP licensing conventions; IP Regulations DIFC Law No. 4 of 2019; arbitration at DIAC or LCIA strongly preferred |
| **UAE onshore (federal)** | Trademark licenses must be registered with the Ministry of Economy (MoE) to be enforceable against third parties and to avoid commercial agency characterization. Federal Decree-Law 36/2021 on IP governs trademarks; Federal Law 44/1992 as amended governs patents |
| **KSA** | Saudi SAIP handles patents and trademarks. Sharia constraint on gharar (unacceptable uncertainty): royalty base and rates must be determinable at the time of the agreement — no open-ended percentage on unquantifiable base. Consider structuring uncertain milestone payments as conditional lump sums rather than percentages |
| **LB** | Law 75/1999 governs IP. Registered trademark licenses should be recorded at OEIP. Civil-law formalism: express written license required; implied licenses are difficult |
| **EG** | Law 82/2002 governs IP; trademark licenses must be recorded with IPRO to be enforceable against third parties |
| **EU** | Technology Transfer Block Exemption Regulation (TTBER) Reg. 316/2014: hardcore restrictions (price-fixing on sublicensees, market allocation) void. Safe-harbor market share thresholds apply. Exclusive grantbacks and no-challenge clauses need careful review |
| **France** | Contrat de licence; trademark licenses should be recorded at INPI. Loi Pacte amendments to IP code apply |
| **UK** | CDPA 1988 (copyright), Patents Act 1977 (patents), Trade Marks Act 1994 (trademarks) — all allow exclusive licenses to be recorded for priority against subsequent licenses |

### MENA commercial agency trap

In UAE, KSA, and Qatar, certain exclusive distribution arrangements can be recharacterized as a commercial agency if the licensed territory is the whole country and the licensee acts as a "promoter" for the licensor. Commercial agency laws provide strong local-party protections including automatic renewal and compensation on termination. To avoid this:
- Do not grant "exclusive" rights to promote or represent; grant "exclusive exploitation rights" in the licensed IP
- Expressly state the agreement is a license, not a commercial agency
- Obtain local counsel sign-off in each GCC state

## Royalty pitfalls

**Net Sales definition** — This is the most-litigated clause in any royalty agreement. Be explicit about what may be deducted:
- Returns and allowances (cap the deduction, e.g., "not to exceed 3% of gross sales")
- Freight and insurance
- Sales and use taxes, VAT (specify whether to gross-up or net)
- Early-payment discounts (permitted deduction? capped?)
- Intra-group transfer pricing (must be at arm's length)

**Royalty stacking** — Where a product is covered by multiple licensed patents (from different licensors), total royalties can become uneconomic. Consider:
- A royalty stacking cap clause (aggregate royalties on a given product not to exceed X% of net sales)
- A reduction clause if licensee must take additional licenses on third-party IP to use the licensed IP

**Currency and FX** — Specify reporting currency and payment currency; specify the FX rate used (central bank mid-market rate on payment date is standard).

**Audit trigger** — Licensee will resist unlimited audit rights. Reasonable compromise: auditor must be a nationally recognized accounting firm; licensee may require confidentiality agreement from auditor; audit window limited to 12 months preceding notice.

## Drafting standards

- Define every term that appears more than once.
- Never use "including without limitation" as a substitute for careful enumeration — it creates ambiguity.
- The exclusivity clause must state whether the licensor itself is also excluded from the defined field and territory (exclusive vs sole: "sole" = licensor retains right to compete itself).
- Include a "no implied license" provision: rights are only those expressly granted.
- Produce a complete, ready-to-sign document. Do not leave `[INSERT X]` placeholders unless the user asked for a template. If a value is unknown, state a clearly-labeled default and list it at the top of the output.

## Common mistakes

- Vague field-of-use definitions that expand through good-faith use over time
- Omitting prosecution control provisions — licensor loses patent validity while licensee keeps paying no royalties
- Failing to carve out licensee's existing products from improvement clauses
- Not requiring licensee to maintain quality standards for trademark licenses (naked-license invalidity risk)
- Anti-challenge clause without jurisdictional verification (void in EU, valid in some US circuits)
- Forgetting to register the license with the relevant IP office in MENA jurisdictions

## Related skills

- [[draft-licensing-agreement]]
- [[draft-ip-assignment]]
- [[review-indemnification-balance]]
- [[draft-nda-mutual]]
- [[draft-msa]]
