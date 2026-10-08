---
name: draft-definitions-builder-sboghossian
title: Definitions Builder
description: Use when building or auditing the Definitions section of any contract. Provides structural rules for definition drafting, a core-term checklist applicable to most commercial agreements, anti-patterns to eliminate, and guidance on cross-referencing defined terms consistently across a document. Works as both a drafting aid (building definitions from scratch) and a cleanup tool (fixing an inconsistent existing definitions section).
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-definitions-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Definitions Builder

## When to use this

Use this skill when:

- You are drafting a contract from scratch and need to build its Definitions section.
- You are reviewing a contract and the definitions section is inconsistent, circular, or incomplete.
- You need to add or modify a term definition mid-draft without breaking cross-references.
- You are translating a definitions section into Arabic/English bilingual form and need consistent term handling.

The skill applies equally to short commercial agreements (2 pages) and large transactional documents (100+ pages). The rules are the same; what scales is the depth of the definitions list.

## Core drafting rules

### Structure
- **Alphabetical order** always. Reviewers scan alphabetically; random order wastes time and signals poor draftsmanship.
- **Capitalize defined terms throughout the document** — including in the operative clauses, schedules, and annexes. Consistency signals that the term is being used in its defined sense.
- **One definition per term** — never define the same concept in two different clauses. If a concept is defined in an operative clause, promote it to the Definitions section or cross-reference to it.
- **Definitions are pure meaning, not obligations** — a definition clause should define a concept, not impose an obligation. The sentence "Confidential Information means… and the Receiving Party shall not disclose it" is two clauses, not one. Split them.
- **Nesting is acceptable where warranted** — "Business Day" may reasonably define itself partly by reference to "Approved Banking List" if that list is separately defined. But nesting beyond one level invites circular definitions.

### Language
- Use **"means"** not "shall mean", "is defined as", or "refers to". Plain present tense is clearest.
- Use **"includes"** only for non-exhaustive extension of a definition; use **"means… and includes"** when the core meaning is given and you want to avoid doubt about edge cases.
- Avoid **"including but not limited to"** — use "including" alone, which courts in most jurisdictions already treat as non-exhaustive.
- Use **"unless the context otherwise requires"** as the standard overriding caveat in the Interpretation clause (not buried in individual definitions).

## Required definitions for most contracts

The following terms should appear in virtually every commercial agreement. Adapt the content to your specific transaction.

| Term | Standard drafting approach |
|------|---------------------------|
| **Affiliate / Subsidiary** | Define using the standard control test: entity that controls, is controlled by, or is under common control with a party. Specify "control" as holding >50% of voting rights or the ability to direct management. |
| **Agreement** | "This [name of agreement] dated [date] between [parties], including all Schedules and Annexes." |
| **Business Day** | A day (other than Saturday, Sunday, or a public holiday) on which banks are open for ordinary business in [jurisdiction]. MENA note: Friday is a non-business day in most GCC jurisdictions; the standard work week is Sunday–Thursday in KSA and many UAE entities. |
| **Confidential Information** | Material non-public information disclosed by either party in connection with the Agreement. Include carve-outs: (a) information in the public domain not due to recipient's breach; (b) independently developed; (c) received without restriction from a third party; (d) required to be disclosed by law. |
| **Effective Date** | The date this Agreement becomes legally binding — typically the date of the last party to sign. |
| **Force Majeure Event** | Events beyond a party's reasonable control preventing performance. Enumerate (war, natural disaster, pandemic, governmental action, sanctions). MENA note: include strikes (which some civil-code jurisdictions treat differently), cyber-attacks, and sanctions/embargo events. |
| **Governing Law** | The law chosen to govern the interpretation and enforcement of the Agreement. Note: choice of law and choice of forum are distinct concepts — a separate Dispute Resolution clause handles the forum. |
| **Intellectual Property Rights** | All present and future IP rights including patents, copyright, database rights, trade secrets, trademarks, trade names, domain names, designs, and moral rights (where assignable). |
| **Notice Address** | Define once with full address, email, and named recipient for each party. Cross-reference in the Notices operative clause. |
| **Party / Parties** | Define the signatories by their short-form names used throughout. |
| **Person** | Includes natural persons, companies, partnerships, associations, and governmental bodies. Useful where a defined term could reasonably apply to all of these. |
| **Term** | The duration of the Agreement: initial period + renewal mechanics. |

## Contract-type specific definitions

Some definitions are standard in particular practice areas:

**Technology / SaaS**
- "Service / Platform" — the software or service being provided
- "Data" / "Customer Data" — data uploaded or generated by the customer
- "SLA" / "Uptime" — performance standards
- "Permitted Users" / "Authorized Users" — access scope

**Employment**
- "Basic Salary" vs. "Total Remuneration" — critical in KSA and UAE where EOSG and overtime are calculated on different bases
- "Probation Period" — must match statutory limits (see jurisdiction-specific employment skills)
- "Good Leaver" / "Bad Leaver" — define precisely if equity is involved

**Finance / Banking**
- "Business Day" (financial) — often defined with reference to TARGET2 or relevant clearing system
- "SOFR / SONIA / EIBOR" — reference rate for floating-rate obligations
- "Majority Lenders" — voting threshold (typically 66.67%)

**Real Estate**
- "Premises" — legal description + demise plan by reference
- "Rent" / "Service Charge" / "Insurance Contribution"
- "Permitted Use"

**MENA-specific**
- "Wali / Wilayah" in personal-status documents — legal guardian
- "Kafil / Kafala" in employment contexts — immigration sponsor
- "Hijri / Gregorian Date" — dual-date definitions for instruments filed with KSA authorities

## Anti-patterns to eliminate

| Anti-pattern | Problem | Fix |
|---|---|---|
| Defining a term used only once | Creates definitional overhead with no benefit | Use the full description inline |
| Multi-paragraph definition that imposes obligations | Definitions are not operative clauses | Extract the obligation to the operative section |
| Circular definitions | A defines B, B defines A | Break the circle: make one the anchor and the other derived |
| "Means any and all…" | Verbose and legally equivalent to "means" | Remove "any and all" |
| Defining the same concept twice in different clauses | Contradiction risk | Centralize in Definitions; cross-reference |
| Undefined capitalized terms | Reviewers search for definitions that don't exist | Scan document for capitalized terms not in the Definitions section |
| Definitions not capitalized in body | Reviewer cannot tell when a term is being used in its defined sense | Global search-and-replace to enforce capitalization |
| Placeholders left in definitions | `[INSERT DEFINITION]` in a final draft | Complete or delete before delivery |

## Definitions audit checklist

After drafting, run these checks:

1. Every capitalized term in the document body has a definition.
2. Every defined term is actually used in the document (no ghost definitions).
3. No term is defined more than once.
4. Definitions are in alphabetical order.
5. No definition contains an operative obligation — obligations are in operative clauses.
6. "Business Day" is calibrated to the right jurisdictions (GCC work week, local public holidays).
7. Cross-references within definitions are accurate (defined term capitalized, correct section number).
8. Bilingual documents: defined terms in English and Arabic are aligned in meaning.

After drafting, check definitions consistency across the full document with [[review-definitions-consistency]].

## Related skills

- [[review-definitions-consistency]] — automated audit of a contract's definitions for consistency with usage in the body
- [[draft-nda-mutual]] — standard definitions structure in an NDA (first contract many practitioners draft)
- [[draft-msa]] — master services agreement definitions section for technology/professional-services contexts
- [[draft-shareholders-agreement]] — complex definitions set covering share classes, governance, exit mechanics
- [[review-contract]] — full contract review that includes a definitions-consistency pass
