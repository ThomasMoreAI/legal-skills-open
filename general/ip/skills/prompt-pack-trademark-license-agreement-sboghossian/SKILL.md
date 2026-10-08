---
name: prompt-pack-trademark-license-agreement-sboghossian
title: Trademark License Agreement
description: Use when a trademark owner (licensor) wants to authorize another party (licensee) to use one or more registered trademarks in connection with specified goods or services in a defined territory, in exchange for royalties or other consideration. Covers quality control (the critical element that maintains trademark validity), usage guidelines, royalty mechanics, audit rights, protection obligations, and term/termination. Particularly important in MENA where trademark licensing registration requirements and Arabic language obligations vary by jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-trademark-license-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Trademark License Agreement

## When to use this

Use this skill when a trademark owner wants to allow another entity to use its trademark(s) commercially. Common scenarios:

- A brand owner licensing regional distributors or franchise partners in the GCC or Levant to use its name and logo
- A franchisor licensing a sub-brand to a master franchisee (trademark license is typically embedded within or attached to the franchise agreement)
- A company entering a joint venture where both parties will use a shared or parent brand
- A software company licensing its product name for bundled OEM use by a hardware partner

Quality control is the legal heart of a trademark license: in every jurisdiction, a trademark owner who does not exercise meaningful quality control over a licensee's use risks "naked licensing" — a ground for cancellation of the mark. The agreement must document the quality control mechanism, not merely assert it.

## Required inputs

| Input | Why it matters | Sensible default |
|-------|---------------|-----------------|
| Licensor full name + mark details (word mark / device, registration numbers, classes) | Defines what is being licensed | Prompt user |
| Licensee full name | The authorized user | Prompt user |
| Licensed goods / services | Scope of the license — must match trademark classes | Prompt user; confirm against NICE classification |
| Territory | Geographic scope; affects registration requirements | Prompt user |
| Exclusivity | Exclusive licenses require registration in most MENA jurisdictions to be enforceable against third parties | Prompt user (exclusive / non-exclusive / sole) |
| Royalty structure | Consideration; tax implications differ (KSA withholding 5–15%) | Prompt user; suggest % of net sales or flat fee |
| Term | Duration; renewal mechanics | Prompt user; suggest 3–5 year initial term |

## Optional inputs

- **Sub-licensing rights** — whether licensee may grant sub-licenses (high risk unless tightly controlled)
- **Minimum sales / royalty guarantees** — ensures licensor receives value even if licensee underperforms
- **Marketing spend commitments** — protects brand equity
- **Brand guidelines schedule** — color palette, font, logo usage, prohibited uses; attach as Schedule C
- **Audit rights** — licensor right to inspect licensee's quality control processes and financial records
- **Termination for change of control** — if licensee is acquired, licensor may want termination right
- **Registration of license** — most MENA jurisdictions require recordal with the trademark office for the license to be effective against third parties

## Document structure

1. **Definitions** — "Licensed Mark(s)," "Licensed Goods/Services," "Territory," "Quality Standards," "Net Sales," "Royalty," "Approved Sub-licensee," "Regulatory Approval"
2. **Grant of license** — express grant; exclusivity level; field of use; territory; confirmation that license does not extend to unregistered use in territories where the mark is not registered (or that licensor warrants registration coverage)
3. **Restrictions** — no sub-licensing without prior written consent; no modification of the mark; no use outside the licensed goods/services; no combination with third-party marks without approval; no online use outside specified domains / geographies
4. **Quality control** — licensor's right to specify and amend quality standards; licensee's obligation to comply; inspection rights (annual inspection, ad hoc upon reasonable notice); approval of new products / packaging before launch; right to require remedy within 30 days of non-conformity notice; right to terminate if quality breach is not remedied
5. **Brand guidelines** — reference to Schedule C; prohibition on unapproved use; specific prohibitions (tarnishment, disparagement, generic use)
6. **Royalties and payments** — royalty rate and base (% of net sales, per-unit fee, or combination); payment frequency (quarterly typical); late payment interest; currency (specify; for KSA and UAE transactions state AED or SAR or USD); withholding tax gross-up obligation
7. **Records and audit** — licensee maintains accurate sales records; licensor audit right (once per year on 30-day notice; at own cost unless discrepancy > 5% in licensor's favor); dispute procedure for audit findings
8. **Protection of the mark** — licensee must promptly notify licensor of infringement or passing-off by third parties; licensor has primary right to prosecute infringement; licensee must cooperate; costs allocation
9. **Registration obligations** — licensor undertakes to maintain registrations in Territory; licensee cooperates with any renewal or defense proceedings; if license must be recorded with trademark office (see §Registration below), licensor undertakes to file recordal promptly after execution
10. **Representations and warranties** — licensor: valid registrations, no pending cancellation, authority to grant license; licensee: will comply with quality standards and applicable law, no conflicting obligations
11. **Term and renewal** — initial term; automatic renewal vs. active renewal option; renewal conditions (royalty uplift, quality audit pass)
12. **Termination** — for material breach (30-day cure); for insolvency; for change of control; for persistent quality failure; for non-use by licensee for > 3 consecutive years (risks revocation for non-use in some jurisdictions)
13. **Effect of termination** — licensee ceases use immediately; sell-off period for existing inventory (30–90 days); return / destruction of branded materials; no compensation for goodwill (unless required by local law — note UAE and Lebanese franchise-adjacent rules)
14. **Governing law and dispute resolution** — jurisdiction; arbitration clause (DIAC, ICC, SIAC common in MENA); language
15. **Schedules** — A: Mark registrations by territory; B: Licensed goods/services with NICE classes; C: Brand guidelines; D: Form royalty statement; E: Approved sub-licensees (if any)

## Jurisdictional notes

| Jurisdiction | Registration of license | Quality control standard | Key trap |
|---|---|---|---|
| UAE (onshore) | Recordal with MOE required for license to be binding on third parties; fee applies; Arabic documents | Not codified separately — inferred from trademark validity principles | "Naked licensing" (no quality control) can ground cancellation action |
| DIFC / ADGM | License enforceable as commercial contract; no separate trademark recordal procedure (federal registration governs the mark) | Common-law standard: genuine supervision | Assignment-vs-license distinction: rights registered with MOE regardless |
| KSA | Recordal with SAIP mandatory for exclusive licenses; recommended for all; Arabic required | Not separately codified; courts apply general IP law principles | Withholding tax on royalties: 15% for unregistered; 5% if in treaty country |
| Lebanon | Recordal with Ministry of Economy and Trade recommended; Law 240/2000 Art. 24 | Not codified; courts apply equity / tort principles | No specific quality control doctrine; breach of contract is primary remedy |
| Egypt | Recordal with EGYPO required under Law 82/2002; notarization and Arabic required | Law 82/2002 Art. 25 — licensor must ensure quality | Registry records are public; unrecorded exclusive license not enforceable against third parties |
| GCC | GCC Trademark Office recordal separate from national offices | National quality control standards apply | GCC-wide license still requires national recordal in each member state for third-party effect |
| EU | EUTMR Arts. 25–27 — recordal optional but recommended for third-party effect; no quality control mandate in statute but doctrine developed via case law | "Naked licensing" doctrine less developed than US but not absent | Post-Brexit: UK registration separate |
| US | No recordal requirement but useful | "Naked licensing" is a developed doctrine — courts have cancelled marks for failure to supervise quality | State trade secret law may interact with brand guidelines obligations |

**MENA tax trap:** Royalties paid from a KSA entity to a non-resident licensor are subject to Saudi withholding tax (15% standard; reduced under applicable tax treaty). Gross-up obligations must be expressly agreed or the licensor will net less than expected. UAE has no withholding tax on royalties, making UAE-seated licensing structures common.

**Non-use revocation:** In UAE (5 years of non-use), KSA (5 years), and EU (5 years), a registered trademark can be revoked for non-use. If the licensee fails to use the mark in the territory, the licensor faces revocation risk. Include a minimum-use obligation and monitoring right.

## Drafting standards

- **Quality control clause must be operational, not aspirational** — specify the inspection mechanism, the standards document (Schedule C), and consequences of non-compliance; a bare "licensee shall maintain quality" clause is insufficient
- **Royalty base definition matters** — "net sales" vs. "gross revenue" vs. "units sold" can differ by 20–40%; define deductions (returns, taxes, shipping, discounts) precisely
- **Registration of license** — if not required by statute, still recommend recordal for evidentiary purposes; identify who bears the filing fee and timeline obligation
- **Arabic language** — in KSA and UAE, the executed agreement may need to be translated and the Arabic version filed with the trademark office; state which language governs
- **Post-termination sell-off** — specify maximum period (30–60 days) and require destruction certificate for remaining branded inventory

## Common mistakes

- **No quality control mechanism** — single most common drafting error; creates "naked licensing" cancellation risk
- **Forgetting to register the license** — in UAE and KSA, an unrecorded license is not enforceable against third-party infringers
- **Vague territory definition** — "the Middle East" is not a legal territory; enumerate countries
- **Missing withholding tax gross-up** — particularly critical for KSA-outbound royalties
- **No change-of-control termination right** — licensor may find its brand carried by an unknown acquiree
- **Granting sub-licensing rights without restrictions** — sub-licensees are outside the direct quality control chain; if permitted, require prior written approval of each sub-licensee and flow-down of all quality obligations

## Related skills

- [[prompt-pack-trademark-coexistence-agreement]]
- [[prompt-pack-work-for-hire-agreement]]
- [[kb-ip-mena]]
- [[draft-ip-assignment]]
- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
