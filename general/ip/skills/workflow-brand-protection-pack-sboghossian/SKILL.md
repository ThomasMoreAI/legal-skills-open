---
name: workflow-brand-protection-pack-sboghossian
title: Brand Protection Pack
description: Use when a user needs a complete, end-to-end brand protection program — from trademark registration strategy through monitoring, enforcement, and IP holding structure. Covers global and MENA-specific trademark filing, WIPO Madrid Protocol, domain protection, marketplace enforcement, and brand-house structuring, with jurisdiction-specific notes on UAE, KSA, LB, and DIFC.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/workflow/workflow-brand-protection-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Brand Protection Pack

## Purpose

This workflow orchestrates an end-to-end brand protection program. It covers registration, monitoring, enforcement, and holding-structure strategy for companies operating in or expanding into MENA markets and internationally. The output is a portfolio of filed trademarks, active monitoring infrastructure, a tested enforcement playbook, and a compliant IP holding structure.

---

## Inputs / Signals

| Input | Required | Notes |
|-------|---------|-------|
| Brand name(s) | Yes | All word marks, logos, taglines to protect |
| Goods and services description | Yes | Needed for Nice Classification; be specific |
| Current operating jurisdictions | Yes | File in all active markets |
| Near-term expansion markets | Yes | File before entering, not after |
| Existing TM registrations | If any | Identify gaps and upcoming renewals |
| IP holding company preference | If applicable | Tax-efficient jurisdiction consideration |
| Budget range | Recommended | Per-jurisdiction filing fees vary significantly |

---

## Logic — Phase 1: Registration Strategy

### Jurisdiction Priority Matrix

File trademark applications in this priority order:

| Priority | Jurisdictions | Rationale |
|----------|-------------|-----------|
| Immediate | Home jurisdiction + all current markets | Core protection; establishes priority dates |
| Near-term (6–12 months) | All expansion markets + strategic markets | Anti-cybersquatting; preempts competitors |
| International | Madrid Protocol designations | Cost-efficient multi-country coverage |

**MENA trademark registration authorities:**
| Jurisdiction | Authority | Key notes |
|-------------|----------|-----------|
| UAE (federal) | Ministry of Economy — Trademarks Office | Arabic transliteration required for non-Arabic marks; 10-year registration; renewals available |
| KSA | Saudi Authority for Intellectual Property (SAIP) | Arabic-language trademark required or Arabic transliteration alongside; 10-year term |
| Lebanon | Ministry of Economy and Trade — IP Directorate | Civil law system; relatively fast registration; 15-year term |
| Egypt | Commercial Registry, Intellectual Property Protection Department | 10-year term; Arabic transliteration required |
| DIFC | DIFC does not have its own trademark registry — UAE federal registration covers DIFC |
| EU (all member states) | EUIPO — EU Trade Mark (EUTM) | Single registration covering 27 countries; 10-year term |
| UK | UK Intellectual Property Office (UKIPO) | Post-Brexit: separate from EUTM |
| US | USPTO — federal trademark registration | TEAS Plus online filing; 10-year term; use-in-commerce requirement |

### Nice Classification Strategy

File in all relevant classes. Common stacks by industry:

| Industry | Key Nice Classes |
|----------|----------------|
| Technology / SaaS | 9 (software), 38 (telecommunications), 42 (tech services) |
| Legal-tech | 9 (software), 38 (tech platforms), 42 (legal services delivery platform), 45 (legal services — check jurisdiction rules for this class) |
| Consumer goods | 3, 18, 25 (fashion/beauty/consumer); class depends on product |
| Financial services | 36 (insurance, financial, banking) |
| Healthcare | 5 (pharmaceuticals, medical), 44 (medical services) |
| Media / publishing | 9, 16, 38, 41 |

Register defensively in adjacent classes where you intend to expand within 3 years.

### Madrid Protocol — International Filing

The Madrid System (administered by WIPO) allows a single "international registration" to designate multiple countries:

- File via your home country trademark office (the "office of origin")
- Designate all target countries in the international application
- Cost: WIPO basic fee (~CHF 653 for b&w mark) + per-designation fees (varies by country)
- Equivalent to separate national filings in each designated country; refusal in one country does not affect others
- Dependency period: first 5 years, if the home application is refused or abandoned, all designations fall; after 5 years the international registration is independent

For MENA companies: UAE, KSA, Egypt, and Lebanon are all Madrid Protocol members.

---

## Logic — Phase 2: Domain and Digital Asset Protection

### Domain Registration — Defensive Strategy

- Register all plausible variants: `.com`, `.ae`, `.sa`, `.co.uk`, `.io`, `.ai`, plus all active-market country codes
- Register common typo-squatting variants (transposed letters, common misspellings)
- Register brand name + generic suffix (brandname-legal.com, brandname-app.com)
- Monitor for new gTLD registrations using your brand terms

### Social Media Handle Reservation

- Reserve all major platform handles immediately, even if not yet actively used: Instagram, TikTok, LinkedIn, Twitter/X, Facebook, YouTube, Snapchat, WhatsApp Business
- MENA: also Telegram channels, Jeel (Saudi), Anghami (brand pages)
- Document the handle reservations as part of the IP portfolio

---

## Logic — Phase 3: Monitoring Infrastructure

### Trademark Watch Services

Commercially available TM watching services (Dennemeyer, Corsearch, Clarivate, CompuMark):
- **Application watch**: alerts when new TM applications are filed that are similar to your marks (in your designated countries + classes)
- **Publication watch**: alerts at the publication stage (when opposition period opens)
- **Registration watch**: alerts when conflicting marks proceed to registration

Set watch in all registered jurisdictions plus priority expansion markets.

### Marketplace Monitoring

| Platform | Monitoring approach |
|----------|-------------------|
| Amazon (Global) | Amazon Brand Registry enrollment; automated IP infringement detection |
| Noon (UAE/KSA) | Brand protection program; manual review |
| Namshi | Platform escalation; manual reporting |
| AliExpress / Alibaba | IPPS (Intellectual Property Protection System) enrollment; automated |
| eBay | VeRO (Verified Rights Owner) program |
| Social media platforms | Platform-specific IP infringement reporting; Meta Business Help Center for Facebook/Instagram |

Budget for at least monthly marketplace reviews + automated monitoring for high-value categories.

### Physical Goods Counterfeit Monitoring

For consumer goods and pharma:
- Engage investigators in key source markets (typically Mainland China, Turkey, Hong Kong for MENA)
- Customs recordation (see below) to interdict at borders
- Coordinate with brand protection agencies (brand protection companies like Incopro, Red Points, or local equivalents)

---

## Logic — Phase 4: Enforcement Playbook

### Escalation Ladder

| Level | Action | When to use |
|-------|--------|------------|
| 1 | Cease and desist letter — [[draft-cease-and-desist]] | First contact; low/medium infringers; gives opportunity to comply |
| 2 | Platform takedown | Online sellers, social media infringers; Amazon Brand Registry, Meta IP tools |
| 3 | Domain UDRP/URS | Cybersquatters; WIPO Arbitration Center processes (faster and cheaper than court) |
| 4 | Customs recordation | Cross-border counterfeits; UAE Customs, SAIP customs program, GCC customs |
| 5 | Civil litigation | Serious or repeat infringers; when damages warranted; common-law (DIFC) or civil (UAE mainland) |
| 6 | Criminal complaint | Counterfeiting; UAE and KSA are active; significant deterrent effect |

### Cease and Desist — Key Elements

See [[draft-cease-and-desist]] for full template. Must include:
- Proof of trademark ownership (registration numbers)
- Identification of the infringing activity (with evidence)
- Demand: cease infringing use + destroy existing infringing goods
- Deadline (typically 7–14 days)
- Consequence statement (litigation / criminal complaint if no compliance)

Do not send without confirming: (1) your registration predates the infringer's use; (2) the infringement is genuine, not a permitted use.

### Domain UDRP Process (WIPO)

Three-element test for UDRP complaints:
1. The domain name is identical or confusingly similar to the complainant's mark
2. The registrant has no rights or legitimate interests in the domain name
3. The domain name was registered and is being used in bad faith

WIPO proceedings are online, typically resolved in 60 days, and cost approximately $1,500 (one panelist) for one domain. A well-documented UDRP complaint can recover cybersquatted domains without litigation.

---

## Logic — Phase 5: Brand-House Structure

### IP Holding Company Strategy

Separating IP ownership from operations provides:
- Tax efficiency: royalties paid from operating subsidiaries to IP holdco reduce taxable profits in high-tax jurisdictions
- Risk isolation: IP is not exposed to operational liabilities
- Financing: IP can be pledged as collateral
- Clear audit trail for enforcement

**Common holding jurisdictions:**
| Jurisdiction | Advantages | Considerations |
|-------------|-----------|---------------|
| Netherlands | Favorable IP box regime; extensive treaty network | Substance requirements post-BEPS |
| Ireland | Low CIP rate; IP box; EU member | Substance; post-BEPS changes |
| UAE (mainland or DIFC) | 0% corporate tax on qualifying IP income (under UAE CT regime); central to MENA operations | Emerging CT framework; verify current IP box treatment |
| Luxembourg | Established holding structure; EU member | Substance requirements |
| KSA | For KSA-exclusive IP: consider local entity | Required for some government contract requirements |

Royalty rates between holdco and opco must comply with OECD transfer pricing guidelines (arm's-length principle). For Sharia-compliant structures in MENA, royalty payments must be structured as genuine licensing fees for use of IP rather than interest-bearing arrangements.

---

## Critical Compliance Points

| Item | Detail |
|------|-------|
| Renewal calendaring | TMs renew every 10 years in most jurisdictions; missed renewals lose protection; calendar renewals 18 months in advance |
| Non-use vulnerability | Most jurisdictions allow cancellation for non-use after 3–5 years; use the mark genuinely or risk cancellation action |
| Annual portfolio audit | Review all registered marks; prune dormant marks; identify gaps for new products/services/geographies |
| Watch service continuity | TM watch is not a one-time task; must be a continuous subscription |
| Evidence of use | Maintain records of use for each mark in each jurisdiction (ads, products, invoices) — essential for renewals and cancellation defenses |

---

## Output

This workflow produces:

1. **Trademark filing matrix** — jurisdiction × class × status table
2. **Madrid Protocol application** (if multi-country) — WIPO dossier
3. **Domain registration inventory** — all domains registered, monitored, and flagged
4. **Social media handle inventory** — documented
5. **Monitoring infrastructure** — watch service active + marketplace monitoring enrolled
6. **Enforcement playbook** — [[draft-cease-and-desist]] + platform procedures + litigation escalation path
7. **IP holding company analysis** — jurisdiction comparison + recommended structure
8. **Annual review calendar** — renewals, audits, monitoring reviews

Pair with [[draft-ip-assignment]] for ownership cleanup (ensure all IP is properly vested in the holding company or the correct entity).

---

## Why This Matters

A brand without enforcement is a brand without protection. Trademark registrations are a use-it-or-lose-it asset: non-use cancellation actions, generic terms, and competitor filings can erode protection if not actively managed. In MENA, marketplace counterfeiting and cybersquatting are active threats; UAE and KSA criminal enforcement of IP rights is a significant deterrent that many MENA-operating brands underutilize.

---

## Related Skills

- [[draft-trademark-application]]
- [[draft-cease-and-desist]]
- [[draft-takedown-dmca]]
- [[draft-ip-assignment]]
- [[workflow-startup-incorporation-pack]]
- [[wiki-strategy]]
