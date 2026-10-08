---
name: draft-non-solicit-sboghossian
title: Non-Solicitation Agreement (Customers and Employees)
description: Use when drafting non-solicitation clauses protecting a company's customer relationships and employee base from a departing employee, partner, or shareholder. Covers customer non-solicit and employee non-solicit provisions, definition of key terms (solicit, customer, employee), standard duration, jurisdictional enforceability, and the distinction from non-compete clauses. Non-solicits are easier to enforce than non-competes; this skill should often accompany [[draft-non-compete]]. Triggers on "non solicit", "non-solicitation", "no poaching", or "customer protection clause" requests.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-non-solicit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Non-Solicitation Agreement (Customers and Employees)

## When to use this

Non-solicitation clauses are the more defensible alternative — and essential complement — to non-compete provisions. They protect specific business interests (customer relationships and employee base) rather than broadly preventing someone from working, which makes them significantly easier to enforce in most jurisdictions.

Use this skill when:
- Drafting employment agreements and you want to protect customer relationships and talent
- A business sale includes protection of goodwill (customer and employee non-solicits protect the acquired goodwill)
- A consulting engagement requires preventing the consultant from soliciting customers or staff
- Non-compete protection is unavailable (California), insufficient, or under challenge, and you need a fallback

Always pair this skill with [[draft-non-compete]] — together they provide layered protection.

## Two distinct prohibitions

### Prohibition 1 — Customer non-solicitation

Prevents the departing party from soliciting, approaching, or enticing away customers of the business.

**Model clause:**

> "During the Restricted Period, the [Employee/Consultant/Partner] shall not, directly or indirectly, solicit, approach, or accept business from any Customer of the Company for the purpose of providing goods or services that compete with those provided by the Company, where such Customer was a customer of the Company at any time during the [12/24] months immediately preceding the [Employee/Consultant/Partner]'s departure, and with whom the [Employee/Consultant/Partner] had material personal contact or responsibility during that period."

**Key definitional elements:**
- **"Customer"** — limit to customers with whom the departing party had *material personal contact* or for whose account they had responsibility. Courts will not enforce a clause that prevents contact with customers the employee never touched.
- **Look-back period** — the definition of "Customer" includes only active customer relationships in the preceding [12-24] months — not historical customers from years prior who are no longer active
- **"Solicit"** — define as active, affirmative outreach; the clause does not (and cannot) prevent a customer from independently contacting the departing party. A customer who reaches out unprompted is not a solicitation.
- **Named-list approach (alternative)** — for high-stakes departures, attach a schedule of protected customers by name; this creates certainty on both sides

### Prohibition 2 — Employee non-solicitation (no-poaching)

Prevents the departing party from hiring away or inducing the departure of the business's employees.

**Model clause:**

> "During the Restricted Period, the [Employee/Consultant/Partner] shall not, directly or indirectly, solicit, recruit, induce, or encourage any Employee of the Company to leave their employment with the Company, or hire or engage any such Employee, whether as an employee, independent contractor, or otherwise.
>
> For purposes of this clause, '**Employee**' means any individual employed by the Company at the date of the [Employee's/departing party's] departure, or at any time during the [6] months immediately preceding that date."

**Key points:**
- **"Solicit" / "induce"** — active outreach to the employer's staff; does not prevent a departing party from hiring someone who spontaneously applies to a general job advertisement not targeted at the employer's workforce
- **General advertising carve-out** — state expressly that the clause does not prevent the departing party from placing general advertisements for employment (e.g., on LinkedIn), provided such advertisements are not targeted at the employer's employees — see *Beckett Investment Management Group Ltd v Hall* [2007] EWCA Civ 613 (UK) for the established principle
- **Duration** — employee non-solicit at 12 months is standard and well-accepted; 18 months is often the maximum courts will accept without requiring additional justification

## Standard duration

| Restriction | Typical duration |
|---|---|
| Customer non-solicit (employment) | 12-18 months |
| Employee non-solicit (employment) | 12-18 months |
| Customer non-solicit (M&A / business sale) | 24-36 months |
| Employee non-solicit (M&A / business sale) | 24-36 months |

Post-M&A and post-partnership non-solicits typically run longer than employment non-solicits because the parties have entered a deliberate commercial transaction with explicit protections built into the transaction value — courts see this as bargained-for protection at arm's length.

## Jurisdictional enforceability

Non-solicits are enforced on a similar framework to non-competes, but with materially more tolerance:

| Jurisdiction | Position on non-solicits |
|---|---|
| **Lebanon (LB)** | Generally enforceable where scope is specific and legitimate interest is demonstrated; proportionate duration required |
| **KSA** | Enforceable where protecting legitimate business interest; Labor Law Art. 83 framework applies; courts may reduce excessive duration |
| **UAE federal** | Broadly enforceable under Federal Decree-Law 33/2021; proportionality required; generally easier to enforce than outright non-competes |
| **DIFC / ADGM** | Common-law reasonableness test; non-solicits routinely upheld where scope is specific; blue-pencil available to sever unreasonable elements |
| **France** | Non-solicits are treated differently from non-competes; no statutory compensation requirement (unlike full non-competes); enforceable if scope is proportionate |
| **UK** | Well-established; enforceability depends on whether it protects a legitimate interest and is proportionate; general advertising carve-out is judge-made |
| **California (US)** | Non-solicits of employees may be unenforceable following *AMN Healthcare* line of cases (court applied § 16600 broadly to include employee non-solicits); customer non-solicits are also vulnerable in California; take specialist advice |

Note: California is the material outlier — both customer and employee non-solicits have been subject to challenge in recent case law. If the employee is California-based, the protection may be minimal regardless of choice-of-law clause.

## Carve-outs

Standard carve-outs that do not undermine the clause:
- **General advertisement carve-out** (always include for employee non-solicit): clause does not apply to general-purpose job listings that are not targeted at the employer's employees
- **Inbound customer contact**: if a former customer independently contacts the departing party without being solicited, this is not a breach
- **Prior personal relationships**: if the "customer" was a pre-existing personal relationship of the departing party before they joined the employer (and not developed through their employment), consider a carve-out

## Enforcement

If a departing party breaches a non-solicit:
- The employer's primary remedies are: (a) injunctive relief to stop the solicitation; (b) damages for the business lost as a result
- Liquidated damages clauses for non-solicit breaches are permissible in some jurisdictions if they represent a reasonable pre-estimate of loss — but must be calibrated carefully (see [[draft-non-compete]] discussion of KSA and UAE courts' treatment of penalty clauses)
- Evidence: monitor departing employee's communications carefully; document instances of solicitation; act quickly — delay undermines injunction applications

## Common mistakes

- Defining "solicit" to include passive receipt of an inbound customer inquiry — unenforceable in most jurisdictions and creates reputational issues
- No general advertising carve-out for employee non-solicit — the restriction then purports to prevent the departing party from running any hiring process, which courts will strike down
- Look-back period too long (e.g., "any customer in the last 5 years") — courts narrow this to active/recent relationships
- No "material contact" requirement for customer non-solicit — attempting to protect customers the departing party never interacted with is not a legitimate business interest
- Failing to pair with a non-compete — the non-solicit protects specific relationships but does not prevent the departing party from otherwise competing; use both

## Related skills

- [[draft-non-compete]]
- [[draft-employment-contract]]
- [[draft-nda-unilateral]]
- [[review-employment-risk]]
