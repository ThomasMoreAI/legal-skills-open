---
name: california-property-tax
title: California Property Tax Research (BOE Rules + PTLG Annotations)
description: California property tax research workflow using BOE Property Tax Rules (especially 462.* change in ownership, including 462.180 legal entities) and BOE published Property Tax Annotations (PTLG, commonly 220.*). Use when the user needs rule/annotation identification, synthesis, and application to a factual scenario involving change in ownership, trusts, or legal entities.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/california-property-tax
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [california, property-tax, change-in-ownership, boe, ptlg, prop-13, prop-19, legal-entities]
---

# California Property Tax Research (BOE Rules + PTLG Annotations)

## Scope
This skill produces a research-backed analysis for California property tax change-in-ownership issues by:
1) locating the relevant BOE Property Tax Rule(s), typically in the 462.* series;
2) locating and synthesizing relevant BOE published Property Tax Annotations (PTLG), often in the 220.* range; and
3) applying those authorities to the user's facts via structured comparison.

Primary sources for this workflow:
- BOE Property Tax Rules (Title 18 CCR rules hosted as PDFs). Start point: https://boe.ca.gov/proptaxes/prop-tax-rules.htm
- BOE Property Taxes Law Guide (PTLG) Annotations index/table of contents. Start point: https://boe.ca.gov/lawguides/property/current/ptlg/annt/220-0000.html (for 220.* Change in Ownership)
- BOE links found in /references/boe-navigation-cheatsheet.md

## Operating principles
- Treat BOE Rules PDFs as the controlling articulation for this workflow; treat annotations as interpretive guidance and fact-pattern applications.
- Always capture the exact rule number, rule title, and a pinpoint reference (section/subdivision) when relying on a rule.
- For each annotation relied upon, extract: (a) key facts, (b) issue, (c) conclusion/result, (d) reasoning, and (e) what fact differences would plausibly change the outcome.
- Provide direct URLs for every rule PDF and every annotation page used.
- Do not invent rule text or annotation content. If source access fails, state "source unavailable" and proceed only with what is accessible.

## Inputs expected from the user
- Transaction / ownership structure (before and after), including entity types and ownership percentages.
- Property type and location (county is often relevant operationally even if BOE sources are statewide).
- Dates of transfers/events.
- Any trust terms relevant to control/beneficial ownership (if trust scenario).
- What outcome is being assessed (e.g., change in ownership, change in control, proportional interests, exclusions).

If inputs are missing, proceed by explicitly listing assumptions used to run the research and isolate the minimum additional facts that control the outcome.

## Step-by-step workflow

### Step 1 — Frame the research issue
Produce a one-paragraph "Issue framing" that identifies:
- suspected change-in-ownership trigger (e.g., transfer of fee interest, transfer to/from entity, change in control, cumulative transfers),
- likely rule family (e.g., 462.*),
- likely annotation family (often 220.*).

### Step 2 — Navigate to BOE Property Tax Rules and identify candidate rules
Primary navigation path:
1) Go to BOE Property Tax Rules landing page:
   - https://boe.ca.gov/proptaxes/prop-tax-rules.htm
2) Locate the 462.* series entries (Change in Ownership and New Construction) and shortlist rules by topic.

If the specific target is known (example: Rule 462.180):
- Open the rule PDF directly when available:
  - Example: https://boe.ca.gov/proptaxes/pdf/rules/Rule462_180.pdf

For each candidate rule:
- Record: rule number + title.
- Skim headings/subdivisions for the scenario match.
- Identify the smallest set of subdivisions that do the work (definitions, general rule, examples, special rules).

Deliverable after Step 2:
- A short list of candidate rules (usually 1–3) with URLs and the subdivisions likely controlling.

### Step 3 — Read the controlling rule(s) and extract "decision logic"
For each controlling rule:
- Extract a structured summary:
  - Rule purpose (1 sentence).
  - Operative test(s): the conditions that trigger change in ownership/change in control.
  - Key definitions used in the test.
  - Any explicit exceptions/exclusions described inside the rule.
  - Any examples inside the rule that resemble the facts.

Convert the above into a checklist or decision tree phrased in neutral, operational terms.

### Step 4 — Navigate to PTLG Annotations and identify relevant annotations
Primary navigation path:
1) Use the BOE "Laws, Regulations & Annotations" portal:
   - https://boe.ca.gov/lawguides/
2) Enter the Property Taxes Law Guide (PTLG) annotations section and navigate by number/topic.
3) For change in ownership, start with:
   - https://boe.ca.gov/lawguides/property/current/ptlg/annt/220-0000.html
   - Use "View entire section" when helpful for scanning.

Selection method:
- Prioritize annotations that:
  - cite the same rule number as the controlling rule (e.g., 462.180), or
  - address the same trigger mechanism (change in control, proportional interests, trusts, tiered entities), or
  - match a distinctive fact pattern (e.g., manager-managed conversion without ownership interest, tiered ownership, original co-owner concepts).

Deliverable after Step 4:
- A list of the most relevant annotations (target 3–8), each with a one-line reason for inclusion and URL.

### Step 5 — Extract each annotation into a reusable case-brief block
For every selected annotation, create a block with:
- Citation: annotation number + title (as shown on BOE page) + URL.
- Key facts (bullet list, only the legally salient facts).
- Issue question (1 sentence).
- Result (1 sentence).
- Reasoning (3–8 bullets, no filler).
- "Fact sensitivity": list the 2–5 facts most likely to change the result.

### Step 6 — Apply to the user's facts by comparison table
Create a comparison matrix:
- Columns: User facts | Annotation facts | Same/Different | Why it matters under the rule | Impact on likely outcome.
- Only include facts that map to the rule's operative test.

Then synthesize:
- The best-fit annotation(s) and why.
- The limiting distinctions and how they likely move the outcome.

### Step 7 — Produce the final work product
Output format (default): refer to /references/output-template.md
1) Question Presented
2) Material Facts (as provided + stated assumptions)
3) Authorities
   - BOE Property Tax Rules: list rule number/title + URL + pinpoint subdivisions relied upon
   - PTLG Annotations: list annotation numbers + URLs
4) Analysis
   - Rule-based decision logic
   - Annotation synthesis
   - Application to facts
5) Conclusion (with confidence level and what fact(s) would flip it)
6) Sources (URLs only)

Quality control before finalizing:
- Confirm every authority used has a working URL.
- Confirm the rule PDF is the intended rule number (matches filename and header).
- Confirm annotation numbers are correct and not adjacent/near-miss.

## Notes on common targets
- Rule 462.* is the primary "change in ownership" cluster.
- Rule 462.180 is the primary "legal entities / change in control" rule and is often paired with 220.* change-in-ownership annotations when applying to factual patterns involving entities.

## Audience and Work Shape

Audience: California-qualified tax attorneys, property tax consultants, paralegals supervised by counsel, and in-house tax teams researching change-in-ownership exposure on specific transactions or restructurings. Not for unsupervised use by non-lawyers, real-estate brokers, escrow agents, or self-represented taxpayers preparing assessor filings.

Work shape: Accretive Judgment — research synthesis. The skill identifies controlling BOE Rules and PTLG annotations, extracts decision logic, and applies it to a factual pattern by structured comparison. Output is a draft research memo (issue, authorities, analysis, tentative conclusion with confidence) that the responsible attorney refines and signs.

## Scope and Legal Use

This skill provides legal *research support*, not legal advice and not a substantive opinion on assessability. A produced memo is a draft synthesis of publicly available BOE Rules and PTLG annotations applied to facts as provided; it is not a determination of change-in-ownership, change-in-control, base-year value, or exclusion eligibility, and is not a substitute for a Preliminary Change of Ownership Report (PCOR), BOE-100-B legal-entity filing, or counsel-issued opinion.

**Privilege and confidentiality.** When the skill is run against a real client's transaction, the inputs (entity structure, ownership percentages, transfer history, trust terms) and any conclusions about likely assessor outcomes are presumptively privileged work product. Run only in environments approved by the firm for client matter analysis. Do not paste live client facts into public LLM endpoints or external retrieval tools unless your firm has assessed the routing. BOE pages and rule PDFs are public sources — fetching them does not implicate privilege, but the *research output* applied to client facts does. Sanitize fact patterns for training/illustration use.

**Accountability.** A California-qualified attorney (or appropriately supervised tax professional) must review the rule selection, the annotation synthesis, and the application-to-facts before any output is sent to a client, taxpayer, assessor, or used to advise on filing position. The skill does not sign off on accuracy of authority selection, substantive correctness, completeness of the rule/annotation universe surveyed, or fitness for filing or controversy use.

## Confidence Bands

- **High** — controlling rule (typically 462.* or 462.180) is unambiguous on the operative test; one or more PTLG annotations match the user's facts on the legally salient elements with no material distinctions; no split lines of authority; no post-Prop 19 ambiguity on the relevant exclusion.
- **Medium** — controlling rule is identified but the closest annotations differ on 1–2 salient facts, OR multiple annotations point in the same direction without an exact-match fact pattern, OR the rule's subdivision-level pinpoint is clear but the BOE has issued differing guidance over time. Flag for attorney review and identify the 2–3 facts that would move the result.
- **Low / Review** — controlling rule unclear or arguably overlapping (e.g., 462.180 vs. 462.040), conflicting annotations on point, post-Prop 19 implementation guidance still evolving, novel entity structure (tiered LLCs with non-pro-rata distributions, series LLCs, foreign entities), or trust terms where control/beneficial ownership turns on terms not in the user's submission. Do not present as "likely result"; route to REVIEW with the specific gap identified.

## Out of Scope

- Property tax regimes outside California (other state ad valorem regimes, local taxes outside the Title 18 / Rev. & Tax. Code framework).
- Federal tax consequences of the same transaction (income tax, estate tax, GST, gift tax, IRC §704(b), §754, §1031, transfer-pricing analyses).
- California *state* income, franchise, sales/use, or documentary transfer tax analysis — even where the same transaction triggers them.
- Welfare exemption, builder's exclusion, base-year value transfer mechanics outside of the change-in-ownership question itself, escape assessments, supplemental assessments, or assessment appeals procedure.
- Drafting of PCORs, BOE-100-B, BOE-502-A, assessor correspondence, or appeals briefs (the skill produces research; document drafting is downstream).
- Negotiation positions vis-à-vis a county assessor or AAB hearing strategy.
- Any matter where the controlling source is non-BOE (Revenue & Taxation Code sections without an implementing rule, California Constitution Article XIII A interpretation without a 462.* rule on point, or court decisions post-dating the PTLG annotations on point — those require independent research outside this skill).

## Escalation

Stop and route to the responsible attorney when:
- the candidate rules include both a general rule and a special rule (e.g., 462.040 vs. 462.180) and the choice materially changes the result;
- two or more PTLG annotations on materially similar facts reach different results, or the BOE has superseded or modified an annotation relied upon;
- the transaction is post-Prop 19 (Feb 16, 2021 effective) and the open question is parent-child / grandparent-grandchild exclusion mechanics, family-farm exclusion, or base-year value transfer interaction;
- the entity structure is novel for change-in-ownership analysis (tiered LLCs, series LLCs, disregarded entities with non-pro-rata membership economics, foreign holding companies, beneficial-ownership chains through trusts);
- the trust terms control the answer but the user has not provided the trust instrument or the relevant grantor/beneficiary provisions;
- the user is asking the skill to take a filing position (rather than research the issue);
- the facts implicate a pending or threatened assessor inquiry, escape assessment, or appeal — controversy posture changes what the output must support and is out of scope here.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants added the Audience and Work Shape, Scope and Legal Use, Confidence Bands, Out of Scope, and Escalation sections to align this community-contributed skill with the Legal Skill Design Framework (legal-advice-vs-support boundary, privilege handling for client-specific property analyses, and accountability handoff to a California-qualified attorney). The existing research workflow (Steps 1–7, operating principles, common targets) is preserved unchanged. Frontmatter was extended with `version`, `last_reviewed`, `last_reviewed_by`, `jurisdiction`, and `tags`; the `name` field was changed from `ca-prop-tax-research` to `california-property-tax` to match the folder name and the Anthropic Skills lowercase-hyphen convention. Original author is unknown and is recorded as "Legal Quants community contribution".
