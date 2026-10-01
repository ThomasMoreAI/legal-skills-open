---
name: output-table-of-comparisons-sboghossian
title: Table of Comparisons
description: Use when Claude must present a structured comparison of legal rules, options, or outcomes across jurisdictions, contract types, or scenarios. Ideal for multi-jurisdiction surveys (UAE vs KSA vs Lebanon vs DIFC), option comparisons in deal structuring, and regulatory regime analysis. Triggers on any question asking to compare, contrast, or evaluate multiple alternatives side by side.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-table-of-comparisons
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Table of Comparisons

A comparison table is the most efficient way to present multi-variable legal analysis. When a user asks "how does X work across UAE, KSA, and Lebanon?" or "what are the pros and cons of these two structures?", a prose answer forces the reader to do the comparison themselves. A table does it for them. This skill governs when and how to build comparison tables that are accurate, readable, and decision-useful.

## When to use this

Use a comparison table when:
- The question spans 2+ jurisdictions or 2+ legal options
- Each option has the same set of relevant attributes (statute, threshold, consequence, etc.)
- The user needs to make a decision or recommendation based on the comparison
- The output will be shared with a non-lawyer audience who needs a scannable summary

Do not use a comparison table when:
- There is only one jurisdiction / one option (use IRAC or BLUF)
- The comparison attributes differ significantly between options (use a narrative instead)
- The table would require more than 6 columns (break into two tables or use a narrative)

## Standard pattern

```markdown
| Aspect | Option A / Jurisdiction A | Option B / Jurisdiction B | Option C / Jurisdiction C |
|--------|--------------------------|--------------------------|--------------------------|
| Governing instrument | … | … | … |
| Key threshold / limit | … | … | … |
| Enforceability | … | … | … |
| Formality requirement | … | … | … |
| Regulatory filing | … | … | … |
| Cost / timing | … | … | … |
| **Summary / recommendation** | … | … | … |
```

End the table with a bold **Summary / recommendation** row. Follow the table with a narrative paragraph identifying the preferred option and the decision factors.

## Construction rules

**Same row order for every column.** Apples-to-apples comparison requires that each column addresses the same attribute in the same row. Do not re-order attributes between columns.

**Same level of detail per cell.** If one cell has a specific article citation, every equivalent cell must have one (or explicitly say "no equivalent provision" or "[not available — verify]").

**Cite per cell where it matters.** For any cell containing a legal rule or threshold, include the citation in the cell:
> `UAE FDL 33/2021 art 10 — max 2 years`

**Flag uncertainty inline.** If data for a cell is uncertain: `[unverified — confirm with local counsel]`. Do not leave cells blank or populated with guesses.

**Use a summary row, not a separate section.** The recommendation belongs in the last row of the table and in the follow-on paragraph — not buried three paragraphs later.

## Example — non-compete enforceability

| Aspect | Lebanon | KSA | UAE (federal) | DIFC |
|--------|---------|-----|---------------|------|
| Governing instrument | Labor Code arts 35-36 | Labor Law RD M/51; HRSD guidelines | FDL 33/2021 art 10; Cabinet Decision 1/2022 | DIFC Employment Law (DIFC Law 4/2021) |
| Statutory max duration | Not specified; courts assess case-by-case | Up to 2 years | Up to 2 years | "Reasonable" (common-law test) |
| Geographic scope limit | Proportionate to employer's market presence | Proportionate to employer interest | Proportionate to protected interest (Cabinet Decision 1/2022) | Reasonableness standard |
| Consideration required | Recommended; improves enforceability | Not required | Not required | Not required |
| Court approach to excess | Void or narrow (split in case law) | Reduce to reasonable scope | Equitable reduction — courts prefer narrowing to voiding | Common-law severance / blue pencil |
| Notarisation required | Recommended for evidentiary clarity | Not mandatory | Not mandatory | No |
| Enforceability rating | Mixed — depends heavily on judge | Moderate — proportionality enforced | High if proportionate and justified | High if reasonable and supported by consideration |
| **Recommendation** | **Include but do not over-rely** | **Proportionate scope critical** | **Preferred jurisdiction for enforcement** | **Preferred for senior / IP-sensitive roles** |

*Sources: LB Labor Code arts 35-36; Saudi Labor Law RD M/51; UAE FDL 33/2021 art 10; Cabinet Decision 1/2022; DIFC Law 4/2021.*

## Example — deal structure comparison

| Aspect | Asset Purchase | Share Purchase | Joint Venture |
|--------|---------------|----------------|---------------|
| Target | Specific assets + liabilities | 100% of target entity | New or existing co-owned entity |
| Liability exposure | Buyer takes only selected liabilities | Buyer inherits all historical liabilities | Shared proportionate to stake |
| UAE regulatory filing | May trigger FDI approval (if strategic sector) | Triggers commercial register transfer | MoA / JV agreement + commercial register |
| Stamp duty / transfer tax | Transfer fees on real assets | Share transfer fees (if any) | Registration fees |
| IP transfer | Explicit assignment needed per IP type | IP stays in entity | Licensing or assignment by agreement |
| Employment | TUPE-equivalent under UAE labor law | Employees stay with entity | New employment contracts typically required |
| Complexity / timing | Moderate | Lower (cleaner) | Highest |
| **Recommendation** | **Preferred when liability ring-fencing is essential** | **Preferred for clean acquisitions** | **Preferred for strategic partnerships / growth markets** |

## Best practices for MENA multi-jurisdiction tables

- Always include DIFC / ADGM as a separate column from UAE-onshore — the legal frameworks are materially different (common-law vs civil-law influenced).
- For KSA: note that both Hijri and Gregorian dates may appear in source instruments.
- For Lebanon: flag currency / enforcement instability as a separate risk row where relevant.
- For Egypt: include a "Cassation court position" row for any topic where Egyptian jurisprudence varies from the statute's plain text.
- For GCC comparisons: flag whether the rule is federal (KSA, UAE) or emirate-level (Abu Dhabi, Dubai DIFC).

## Pair with

After the table, always add:
1. A narrative paragraph: "Based on the above, [preferred option/jurisdiction] is recommended because [1–3 reasons]."
2. Sources block per [[output-source-attribution-block]].
3. If any cell is uncertain, a section: "Information to verify" listing the uncertain cells and the steps to confirm them.

## Related skills

- [[output-irac-structure]]
- [[output-inline-citations-with-pinpoints]]
- [[output-source-attribution-block]]
- [[output-partner-memo-style]]
- [[research-jurisdiction-comparison]]
