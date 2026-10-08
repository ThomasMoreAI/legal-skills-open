---
name: draft-non-compete-sboghossian
title: Non-Compete Clause / Agreement
description: Use when drafting a non-compete clause or standalone non-compete agreement for an employment, partnership, or M&A context. Covers enforceability rules by jurisdiction (LB, KSA, UAE federal, DIFC, FR, US California), required elements (duration, geography, activity scope, consideration), a model clause, carve-outs, and the critical pairing with non-solicit provisions. Triggers on "non compete", "non-competition", "restraint of trade", "post-employment restriction", or "competition clause" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-non-compete
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Non-Compete Clause / Agreement

## When to use this

Use this skill when drafting a post-employment or post-relationship non-competition obligation. Three primary contexts:

1. **Employment**: restricting a departing employee from working for a competitor or starting a competing business for a defined period and geography
2. **Business / share sale (M&A)**: restricting the seller of a business from competing with the buyer's newly acquired business (these are generally more enforceable than employment non-competes because the seller has received consideration specifically for the goodwill)
3. **Partnership / JV dissolution**: restricting a departing partner or JV party from competing with the remaining business

Always pair with [[draft-non-solicit]] — non-solicitation clauses protect customer and employee relationships, are easier to enforce, and provide protection even when the non-compete fails.

## Required inputs

| Input | Why it matters | Default |
|-------|---------------|---------|
| Restrained party | Employee / departing shareholder / partner | — must supply |
| Restraining party | Employer / buyer / remaining business | — must supply |
| Duration | How long after departure | 12 months (employment); 24-36 months (M&A or partnership) |
| Geographic scope | Country, region, named cities | The jurisdiction(s) where the business actively competes |
| Activity scope | Specific industry, specific competitors, customer-facing roles only | The narrower the better for enforceability |
| Consideration | What the restrained party receives for agreeing | Signing bonus, severance, continued employment, purchase price |
| Governing law | Determines enforceability | Jurisdiction of employment / transaction |

## Enforceability — jurisdiction matrix

Enforceability of non-competes varies dramatically by jurisdiction. Always verify current law with local counsel before finalizing.

| Jurisdiction | Enforceability | Key rules |
|---|---|---|
| **Lebanon (LB)** | Enforceable in principle | Civil-law courts narrowly construe; must protect a legitimate business interest; limited in scope, geography, and duration; consideration recommended but not strictly required; court may reduce but typically will not rewrite |
| **KSA** | Enforceable up to 2 years | Saudi Labor Law Art. 83: enforceable if it protects a legitimate interest, is limited in scope and duration, and is proportionate; courts may judicially narrow excessive provisions |
| **UAE federal** | Enforceable up to 2 years | Federal Decree-Law 33/2021 (Labor Law) Art. 10 + Cabinet Decision 1/2022: enforceable for specialized roles where employee has access to confidential info or customer relationships; must be proportionate; may require court order for enforcement; 2-year cap on duration |
| **DIFC** | Enforceable per DIFC Employment Law Art. 13 | Common-law reasonableness test; protection of legitimate business interest; limited scope, geography, duration; Blue-pencil doctrine applied — courts may sever unreasonable provisions without voiding the whole clause |
| **ADGM** | Enforceable — reasonableness test | Similar to DIFC; based on common-law principles |
| **France** | Strictly regulated | Four mandatory elements: (1) written form; (2) limited in time; (3) limited in geography; (4) limited in activity; AND (5) mandatory financial compensation paid to employee during the restraint period (typically 25-33% of last monthly salary per month of restraint) — without compensation, the clause is void |
| **UK** | Enforceable if reasonable | Common law garden leave / non-compete; reasonableness test; PILON clauses interact; consideration at time of contract |
| **California (US)** | Essentially unenforceable | Business and Professions Code § 16600 voids employment non-competes with very narrow exceptions (sale of business); note: California courts apply this to California employees regardless of choice-of-law clause pointing to another state |

## Model clause (employment context)

> "During the Term of Employment and for a period of [12/24] months following the termination of the Employee's employment for any reason (the **Restricted Period**), the Employee shall not, directly or indirectly, within the [Restricted Territory] (meaning [defined geography]):
> 
> (a) own, manage, operate, control, be employed by, provide services to, participate in, or be connected with, in any capacity, any Competing Business (as defined below);
> 
> (b) hold any equity interest in any Competing Business exceeding [2%] of the issued share capital of a publicly listed company;
> 
> (c) serve as a director, officer, consultant, advisor, or independent contractor for any Competing Business.
> 
> For the purposes of this clause, '**Competing Business**' means any business that competes directly with [Employer's Business as defined in Schedule X]."

Adjust bracketed items per the inputs. The more specifically the Competing Business is defined, the more enforceable the clause — "any business that competes in any way" is far weaker than naming specific types of companies or named competitors.

## Critical elements

### Legitimate business interest
A non-compete that protects no genuine interest will be struck down in most jurisdictions. Recognized legitimate interests include:
- Trade secrets and confidential customer/technical information
- Customer relationships (the employee had material contact with and relationship with customers)
- Business goodwill acquired by the employee at the employer's expense
- Specialized skills or training provided by the employer

A non-compete that simply prevents an employee from using their general skills and experience in the market is not protecting a legitimate interest — it is suppressing labor mobility, which courts do not accept.

### Proportionality
Even where there is a legitimate interest, the restraint must be proportionate:
- **Duration**: 12 months is standard and generally enforceable; 24 months is the outer limit in most jurisdictions (especially UAE Art. 10); anything beyond 24 months for employees is very high risk
- **Geography**: must match the actual area in which the business operates and where the employee competed — a Saudi-based employee with a global non-compete is unlikely to be enforced globally
- **Activity scope**: "any employment in the technology sector" is too broad; "any role in B2B fintech product development focused on MENA remittances" is more precise and more enforceable

### Consideration
- In employment contexts: consideration is the employment itself if the clause is signed at the start; for clauses added during employment, additional consideration (bonus, promotion, salary increase) must be provided for the new restriction
- In France: mandatory financial compensation during the restraint period is a statutory requirement, not optional
- In M&A: the purchase price for the business is the consideration

## Carve-outs

Standard carve-outs that improve commercial acceptability without destroying protection:
- Holding up to [2-5%] of shares in a publicly listed company (passive investment, no management role)
- Employment in the same broad industry but in a non-competing division (e.g., working for a bank that does not compete in the employer's specific product line)
- Return to home jurisdiction if the employee was relocated for the role (limits the geographic scope effectively)
- Activities that the employer is not currently conducting (protects existing business, not future aspirations)

## Pairing with non-solicit

Non-compete and non-solicit clauses serve different but complementary functions:
- **Non-compete**: prevents the departing party from working for or building a competing business
- **Non-solicit**: prevents the departing party from taking customers or employees from the former employer

Courts universally consider non-solicit clauses more favorably than non-competes because they protect a more specific, definable business interest without broadly preventing the individual from earning a living.

**Best practice**: include both provisions. If the non-compete is struck down or narrowed, the non-solicit may survive and provide meaningful protection for the employer's customer relationships and talent.

See [[draft-non-solicit]] for the companion skill.

## Common mistakes

- Drafting a global non-compete for an employee whose work was regionally limited — unenforceable in most jurisdictions
- No additional consideration for a mid-employment clause amendment — renders the new restriction unenforceable for lack of consideration (common-law jurisdictions)
- Copying a California non-compete form for use in UAE or France — fundamentally different enforceability frameworks
- Activity scope defined as the entire industry rather than the specific competitive activity — courts will strike it down
- Omitting France's mandatory compensation — the clause is void without it; the employer does not even get a morally binding commitment

## Related skills

- [[draft-non-solicit]]
- [[draft-employment-contract]]
- [[draft-nda-unilateral]]
- [[review-employment-risk]]
