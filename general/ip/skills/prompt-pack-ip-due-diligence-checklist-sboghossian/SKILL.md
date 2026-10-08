---
name: prompt-pack-ip-due-diligence-checklist-sboghossian
title: IP Due Diligence Checklist
description: Use when conducting IP due diligence in connection with an M&A transaction, investment, or licensing deal. Generates a comprehensive checklist covering patents, trade marks, copyrights, trade secrets, licences, assignments, encumbrances, and ongoing/threatened IP litigation. Relevant for target-company evaluation across MENA, EU, UK, and US IP registries.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-ip-due-diligence-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# IP Due Diligence Checklist

## When to use this

Use this skill when a buyer, investor, or licensee needs to assess the intellectual property portfolio of a target company before completing a transaction. It produces a structured checklist that the legal team and IP counsel can work through systematically.

Triggers:
- M&A: acquiring a technology company, brand, or product line
- Investment: venture capital or private equity due diligence on a startup
- Licensing: evaluating an IP portfolio before taking an exclusive licence
- Joint venture formation: assessing what IP each party will contribute

## Required inputs

| Input | Why it matters |
|---|---|
| Target company name / description | Scopes the request correctly |
| Transaction type | M&A / investment / JV / licensing deal — determines depth and angle of review |
| IP types present | Patent-heavy vs brand-heavy vs software copyright vs trade secret business — allows tailored checklist |
| Jurisdictions of operation and registration | IP rights are territorial; determines which registries to search |

## Checklist — Patents and Utility Models

- [ ] Schedule of all granted patents and pending applications (by country, number, filing date, status)
- [ ] Chain of title: assignments, inventor declarations, employment agreements confirming company ownership
- [ ] Freedom-to-operate (FTO) searches on key products/processes
- [ ] Patent prosecution history: any office actions, rejections, or claim amendments that narrow scope
- [ ] Maintenance fees and annuity payment status (lapsed or expiring patents)
- [ ] Inter partes reviews (IPR), oppositions, or invalidity proceedings pending or threatened
- [ ] Licences granted to third parties (exclusive/non-exclusive, field of use, royalty rates, sublicensing rights)
- [ ] Cross-licences, patent pools, or standards-essential patent (SEP) obligations
- [ ] Government funding: any march-in rights or IP ownership restrictions (e.g., Bayh-Dole in the US, KSA/UAE government-funded research agreements)

## Checklist — Trade Marks and Trade Names

- [ ] Schedule of all registered trade marks and pending applications (by country, class, registration number, renewal date)
- [ ] Common-law / unregistered marks used in commerce
- [ ] Evidence of use in each jurisdiction to support registration / prevent lapse
- [ ] Chain of title: assignments, name-change recordings
- [ ] Licences and co-existence agreements
- [ ] Pending oppositions, cancellation actions, or infringement claims
- [ ] Domain name portfolio and social media handle registrations; cybersquatting disputes
- [ ] Geographic indications or appellations of origin (if applicable)
- [ ] MENA note: trade marks in UAE, KSA, Egypt, Lebanon should be verified at local registries (UAE Ministry of Economy, SAIP, Egyptian Trade Marks Office, Lebanese IP Directorate) as international searches may miss local recordings

## Checklist — Copyrights and Software

- [ ] Key software products: source code ownership (company-owned, contractor-assigned, joint authorship)
- [ ] Employee IP assignment agreements covering all contributing developers
- [ ] Contractor / freelancer assignment agreements (especially for off-shore development teams)
- [ ] Open source component inventory and licence compliance (GPL, LGPL, MIT, Apache, AGPL — identify any copyleft obligations that require source disclosure)
- [ ] Third-party software licences and SaaS subscriptions (are they assignable / change-of-control provisions?)
- [ ] Database rights (EU/UK) and sui generis database rights
- [ ] Marketing materials, brand assets, photographs, audiovisual works — ownership vs licence confirmed

## Checklist — Trade Secrets and Confidential Information

- [ ] Key trade secrets identified and documented
- [ ] Reasonable measures to maintain secrecy: NDAs with employees, contractors, customers, suppliers
- [ ] Non-compete and non-solicitation agreements with key personnel
- [ ] Data room / information security practices evidencing trade secret protection
- [ ] Any prior leaks, misappropriation incidents, or claims

## Checklist — Licences and Agreements

- [ ] All inbound IP licences: identify term, territory, exclusivity, change-of-control provisions
- [ ] All outbound IP licences: royalty rates, audit rights, sublicensing, reversion triggers
- [ ] Technology transfer agreements and R&D collaboration agreements
- [ ] Co-development or co-ownership agreements (who owns improvements?)
- [ ] Software escrow arrangements

## Checklist — Encumbrances

- [ ] IP pledges or security interests (e.g., IP collateral registered with UCC in the US; DIFC/ADGM security registration)
- [ ] Liens from creditors or insolvency proceedings
- [ ] Government or regulatory encumbrances

## Checklist — Litigation and Disputes

- [ ] Pending or threatened infringement claims (as plaintiff or defendant)
- [ ] Settled IP disputes: review settlement terms for ongoing obligations
- [ ] Administrative proceedings: oppositions, cancellations, IPRs

## Output format

Produce the checklist in three sections:
1. **Items confirmed clean** — no issues found
2. **Items requiring further information** — information requests to be sent to target
3. **Red flags** — items that materially affect deal value or require representation/warranty/indemnity protection

Include a summary table: IP category | Status | Risk level (Low/Medium/High) | Action required.

## Jurisdictional / practice-area notes

- **MENA registries** are not always accessible through international search services; instruct local counsel in UAE, KSA, LB, EG to run local registry searches independently.
- **Civil-law jurisdictions (FR, LB, EG)**: Copyright arises automatically but recording assignments at IP offices is important for enforceability against third parties.
- **DIFC / ADGM**: IP owned by entities registered in DIFC or ADGM is governed by DIFC/ADGM IP regulations; separate from UAE federal IP law.
- **KSA**: SAIP launched a modernized IP registry; patent and trade mark prosecution timelines have shortened since Vision 2030 reforms.

## Limits & escalation

This checklist is a due diligence framework — it does not constitute a freedom-to-operate opinion or a validity assessment. Engage qualified local IP counsel for: FTO analysis in target markets, valuation of IP assets, and assessment of prosecution quality.

## Related skills

- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-patent-license-agreement]]
- [[prompt-pack-open-source-compliance-review]]
- [[prompt-pack-merger-agreement]]
- [[prompt-pack-letter-of-intent]]
