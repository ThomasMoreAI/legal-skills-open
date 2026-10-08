---
name: prompt-pack-non-compete-agreement-sboghossian
title: Non-Compete Agreement
description: 'Use when drafting a non-compete (post-termination restrictive covenant) agreement for an employee, senior executive, or commercial party. Covers restricted activities, geographic scope, duration, consideration, and permitted activities. MENA-first: addresses enforceability standards in UAE Labour Law, KSA Labour Law, Lebanese Labour Code, and Egyptian Labour Law, as well as DIFC/ADGM employment frameworks and common-law reasonableness doctrine.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-non-compete-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Non-Compete Agreement

## When to use this

Use this skill when an employer, company, or business partner wants to restrict a party (employee, contractor, or commercial partner) from competing with the protected business during or after the relationship. Non-compete agreements in the employment context are the most common use case; they are also used in M&A (sellers restricting competition post-acquisition) and JV contexts.

Triggers:
- "Draft a non-compete for our new Head of Sales."
- "Include a non-compete for the founder in connection with the acquisition of his company."
- "Draft a post-employment restriction preventing our software engineer from joining a competitor."

**Critical threshold question**: Before drafting, determine whether a non-compete is *enforceable* in the governing jurisdiction — and, if so, what the maximum permissible scope is. Drafting an overly broad non-compete that courts will strike is no better than having no restriction at all (and worse in some jurisdictions where courts will not blue-pencil).

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Employer / Beneficiary name | The party being protected | Ask user |
| Employee / Covenantor name and role | Identifies the person bound; seniority affects legitimate interest | Ask user |
| Restricted activities | Precisely what the covenantor is prohibited from doing | Ask user — must be specific |
| Geographic restriction | Territory of the restriction | Ask user — must be reasonable |
| Duration | Post-termination duration | Jurisdiction-specific maximum (see table below) |
| Consideration | What the covenantor receives in exchange | Signing bonus / ongoing employment / deal proceeds |
| Governing law | Determines enforceability standard | Jurisdiction where employee works |

## Optional inputs

- Garden leave clause (employee continues to be paid but does not work during the notice period — reduces the duration of the post-termination restriction)
- List of specific competitor companies prohibited
- Non-solicitation (clients and/or employees — often more enforceable than non-compete)
- Confidentiality cross-reference
- Blue-pencil / severance clause

## Document structure

### 1. Parties and Context
Identify the employer and employee; state the role; state the date of the employment agreement to which this restriction is attached (or is entered into separately).

### 2. Definition of Restricted Business
Define the business being protected precisely:
> "Restricted Business means [Employer's] business of [describe: developing and selling enterprise software for the logistics sector / operating retail banking services / providing legal process outsourcing services / etc.] in which [Employee] is materially involved or has had significant access to Confidential Information during the [12 / 24] months prior to termination."

Avoid: "any business competitive with [Employer]'s entire business" — courts will strike this as too broad.

### 3. Restricted Activities
List the specific activities prohibited during the restriction period:
- Directly or indirectly carrying on, being employed by, or consulting for a Competing Business
- Soliciting or attempting to solicit any client or prospective client of [Employer] with whom the Employee had material contact in the [12 / 24] months preceding termination
- Soliciting or inducing any employee of [Employer] to leave their employment

Draft each restriction separately so that a court can enforce each one independently if another is struck.

### 4. Geographic Scope
Be specific. Examples:
- "Within the Emirate of Dubai and the Emirate of Abu Dhabi"
- "Within the Kingdom of Saudi Arabia"
- "In the countries in which [Employer] operates as at the date of termination" (attach schedule of countries)
- No geographic restriction (only appropriate where activity is purely online and geography is not a meaningful limit)

### 5. Duration
State the duration clearly: "For a period of [X months] following the Termination Date." If garden leave applies, state whether the garden leave period counts toward the restriction period (it typically should).

### 6. Consideration
State the consideration for the restriction. Without consideration, a non-compete entered into after the start of employment may be unenforceable in many jurisdictions:
- At hire: employment itself constitutes consideration
- Mid-employment: signing bonus, promotion, or other benefit
- M&A context: sale proceeds
- Standalone restrictive covenant deed: nominal consideration acknowledged by the covenantor

### 7. Permitted Activities
Carve out activities the covenantor is expressly permitted to engage in:
- Passive investments (owning up to [X]% of publicly traded securities)
- Employment in parts of a competitor's business unrelated to the Restricted Business
- Industry association and professional body participation

### 8. Blue-Pencil / Severance Clause
> "If any restriction in this Agreement is held unenforceable, the parties agree that the court or tribunal shall have authority to modify (reduce) the restriction to the minimum extent necessary to make it enforceable, and the remaining provisions shall remain in full force and effect."

Note: some jurisdictions (notably California and certain civil-law systems) will not blue-pencil; check governing law.

### 9. Remedies
Cross-reference the NDA / confidentiality clause. State that breach may result in:
- Injunctive relief without the requirement to post a bond
- Recovery of any financial benefit obtained by the covenantor in breach
- Other remedies at law

## Jurisdictional enforceability table

| Jurisdiction | Enforceability | Maximum duration | Key requirements | Notes |
|---|---|---|---|---|
| **UAE (onshore, Labour Law)** | Yes, for employees | 2 years max (Labour Law Art. 10) | Must be justified by legitimate interests; scope must be limited to activities that harm employer; written; Arabic language recommended | Courts reduce but generally enforce reasonable restrictions; overly broad restrictions struck |
| **DIFC** | Yes (common law) | Reasonableness standard | Must protect a legitimate proprietary interest; reasonable in scope, geography, duration; consideration required | Courts will enforce well-drafted restrictions; garden leave credit reduces risk of challenge |
| **ADGM** | Yes (common law) | Reasonableness standard | Same as DIFC | |
| **KSA (Labour Law)** | Yes | 2 years max (Labour Regulations) | Written; restricted to specific activity; must be geographically limited | Courts generally uphold reasonable restrictions; employer must demonstrate legitimate interest |
| **Lebanon (Labour Code)** | Yes but limited | 1 year strongly preferred | Written; must be ancillary to employment; courts apply strict reasonableness test | Overly broad restrictions often struck entirely (no blue-pencil tradition) |
| **Egypt (Labour Law)** | Yes | Maximum 2 years | Written; limited to specific sector and geography; consideration required | Courts may strike if considered against public policy |
| **France** | Yes but strict | Typically 1–2 years | Must be justified by interests of enterprise; limited in time, geography, and professional activity; mandatory financial compensation (min. 30% of gross monthly salary) | Financial compensation for restriction is mandatory; without it, restriction is void |
| **UK** | Common law reasonableness | Typically max 12 months post-employment | Must protect a legitimate proprietary interest; no wider than necessary; garden leave credit | Courts will strike unreasonable restrictions; non-solicitation is more reliably enforced than activity restriction |
| **US (varies by state)** | Highly variable | California: void; others: reasonableness | No uniform rule; California bans employment non-competes almost entirely; other states apply reasonableness | Do not assume US-style non-competes are enforceable across MENA |

**Key MENA practice point**: UAE Labour Law Article 10 is the primary provision; it requires the restriction to be limited in time (max 2 years), place, and type of activity. Employment non-competes for DIFC/ADGM entities are governed by DIFC/ADGM employment regulations, not UAE Federal Labour Law — very different enforceability analysis.

**M&A context**: Non-competes given by selling shareholders in connection with a business sale are generally treated more favorably by courts than employment non-competes, because the seller has received substantial consideration (the sale price) and is not a weaker party needing protection.

## Common mistakes

- **No geographic limitation**: MENA courts consistently reduce or void non-competes with no geographic scope.
- **Duration exceeds statutory maximum**: UAE Labour Law caps at 2 years; exceeding this renders the restriction invalid.
- **Drafted as a "no-compete" with an entire industry**: restricting a software engineer from "any technology company" for 2 years is voidable in virtually every jurisdiction; restrict to the employer's specific sector and role.
- **No consideration at signing**: a non-compete added to an employment agreement months after hire without new consideration may be unenforceable; provide a nominal consideration payment.
- **No French-style financial compensation**: for French-law-governed employment agreements, failing to include mandatory financial compensation for the restriction renders it void.
- **Omitting a non-solicitation**: where non-compete enforceability is uncertain, a client and employee non-solicitation clause is more reliable and should always be included alongside the non-compete.

## Related skills

- [[prompt-pack-performance-improvement-plan]]
- [[prompt-pack-joint-venture-agreement]]
- [[prompt-pack-nda-strength-check]]
- [[prompt-pack-master-services-agreement]]
- [[heuristic-always-state-jurisdiction-first]]
