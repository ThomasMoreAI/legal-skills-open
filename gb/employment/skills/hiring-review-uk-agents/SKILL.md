---
name: hiring-review-uk-agents
title: /hiring-review
description: Review an offer letter and any post-termination restrictions — Right to Work compliance, Written Statement of Particulars, employment status, restrictive covenant enforceability, and Equality Act pre-employment obligations. Jurisdiction-specific rules are researched per hire, not stored. Use when the user says "review this offer", "can we use a non-compete here", "check this offer letter", "hiring in [location]", or attaches an offer letter or draft contract.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/employment-legal-uk/skills/hiring-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
---

# /hiring-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, hiring review triggers, restrictive covenant policy.
2. Use the workflow below.
3. Check: Right to Work, employment status, written particulars, restrictive covenants, Equality Act pre-employment obligations.
4. Flag anything that hits the jurisdiction-specific escalation table.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Offer letters are mostly boilerplate until they're not. The Right to Work check,
Written Statement of Particulars, employment status call, and restrictive
covenant analysis are where this skill earns its keep. It does not state the
law — every jurisdiction-specific rule is researched and cited at the time of
review.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → jurisdictional footprint, hiring review triggers, restrictive covenant policy, offer letter template location.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`).

## Workflow

### Step 1: Jurisdiction

Where will this person work? Not where HQ is — where *they* are.

- **England & Wales**: primary jurisdiction. ERA 1996 / EqA 2010 / WTR 1998 apply.
- **Scotland**: same statutory framework; some procedural differences.
- **Northern Ireland**: parallel legislation (Employment Rights (Northern Ireland) Order 1996 etc.) — flag explicitly; the rules largely mirror GB but are not identical.
- **Remote / hybrid**: the employee's home jurisdiction governs employment rights regardless of where the employer is based.

Check the jurisdiction table in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` for this location. If it's not in the table — first hire in this jurisdiction — flag it: "First hire in [location]. The jurisdiction table doesn't cover this. Research needed before the offer goes out."

### Step 2: Employment status

Employee, worker, or self-employed? The offer should make this clear. The correct status is determined by the working arrangements, not by what the offer letter calls it.

| Question | Employee | Worker (limb (b)) | Self-employed |
|---|---|---|---|
| Mutuality of obligation | Yes — employer must offer, employee must accept work | Sufficient mutuality while engaged | None |
| Personal service | Must perform personally | Must perform personally (limited substitution allowed) | Can substitute freely |
| Control | High | Moderate | Low or none |
| Integration | Part of the organisation | Partial | External |

> **Research before calling status.** The test for employment status is fact-specific and has been developed extensively in case law (*Autoclenz Ltd v Belcher* [2011]; *Uber BV v Aslam* [2021]; *Pimlico Plumbers Ltd v Smith* [2018]). For any hire that is not a straightforward direct employment, research the current state of the tests and verify that the proposed arrangement is consistent with the claimed status. Cite primary sources. Verify currency.

**IR35 / off-payroll working.** If the hire is via a personal service company (PSC) and the employer is a medium or large private-sector entity (or a public-sector body), the off-payroll working rules in ITEPA 2003 Chapter 10 may apply. If so, the employer (the "client") is responsible for determining employment status for tax purposes and, if IR35 applies, for deducting income tax and NICs before payment to the PSC. Flag any PSC engagement for IR35 assessment.

### Step 3: Right to Work

> **Check Right to Work before the start date.** The employer must carry out a compliant right-to-work check before employment begins — failure exposes the employer to a civil penalty of up to £60,000 per illegal worker and criminal liability in cases of knowledge. Research the currently operative check requirements for this individual's immigration status.

The check method depends on the individual's circumstances:

- **British and Irish citizens**: manual document check (List A or List B documents per the Home Office code of practice) or identity document validation technology (IDVT) via a certified provider.
- **EEA/Swiss nationals with EU Settlement Scheme status**: online Home Office right-to-work check using the share code.
- **Non-EEA nationals with a visa or biometric residence permit**: online Home Office right-to-work check using the share code; confirm the visa permits the work being offered (hours, occupation, employer).
- **Students**: check visa work restrictions — typically limited to 20 hours/week during term time.

> **Research the current Home Office code of practice** for right-to-work checks — it has been updated multiple times and the acceptable document lists and check methods have changed. Cite the current version. Do not rely on a previous version of the code.

Tag any right-to-work flag as 🔴 — this is a pre-hire legal obligation, not a checklist item for later.

### Step 4: Written Statement of Particulars

Under ERA 1996 s.1, employees and workers are entitled to a written statement of certain particulars on or before their first day of employment (day 1 right since 6 April 2020). The statement must cover:

| Required item | Check |
|---|---|
| Employer and employee names and addresses | Present |
| Start date and, if applicable, commencement of continuous service | Present |
| Pay: scale/rate and pay intervals | Present |
| Hours of work (including normal working hours and days of the week) | Present |
| Holiday entitlement and accrual (and whether it includes public holidays) | Present — must equal or exceed 5.6 weeks statutory minimum (WTR 1998) |
| Sick leave and sick pay entitlement | Present |
| Pension: particulars or reference to accessible document | Present |
| Notice: required from employer and employee | Present — must meet or exceed ERA s.86 statutory minimum |
| Job title or a brief description of work | Present |
| Place of work / employer's address | Present |
| Whether employment is temporary or fixed-term | Present if applicable |
| Collective agreements that affect terms and conditions | Present if applicable |
| Working outside the UK for more than 1 month | Present if applicable |
| Disciplinary and grievance procedures (or reference to accessible document) | Present |

> **Research the current s.1 requirements.** The ERA 1996 s.1 particulars have been expanded; verify the current statutory list and whether any recent amendments apply to this hire. Cite primary sources.

### Step 5: Post-termination restrictions

If the offer includes a non-compete, customer non-solicitation, employee non-solicitation, or similar post-termination restriction:

> **Research enforceability before advising.** Post-termination restrictions in UK employment contracts are enforceable only if they protect a legitimate business interest and go no further than reasonably necessary to protect it — the blue-pencil rule (*Cavendish Square Holding BV v Talal El Makdessi* [2015]; *Tillman v Egon Zehnder Ltd* [2019]). The courts will not rewrite an unreasonable restriction. Research the current enforceability standard for each type of restriction and for this role and industry. Cite primary sources. Verify currency.

Check specifically:

- **Legitimate business interest**: trade secrets and confidential information, trade connections (customers/clients), or stability of the workforce — which interests does the employer actually have and are they documented?
- **Garden leave clause**: if the contract includes a garden leave provision, the court will consider the garden leave period when assessing whether a non-compete is reasonable in duration (*Symbian Ltd v Christensen* [2001]).
- **Duration and geographic scope**: are they proportionate to the role and the interest being protected? Broad geography + long duration = higher enforceability risk.
- **Customer / employee non-solicitation**: generally easier to enforce than a blanket non-compete, but must still be tied to legitimate interest and be proportionate.
- **Confidentiality**: implied duty of confidentiality survives employment; express clauses add enforceability certainty for genuinely confidential information.

Per `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` restrictive covenant policy: does this role require restrictions, and if so, at what scope? Apply the house policy first, then overlay the research.

> **No silent supplement.** If a research query returns few or no results for the jurisdiction's restrictive covenant standards, pay transparency law, or any other item being researched, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [jurisdiction / topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) flag as unverified and stop. Which would you like?"
>
> **Source attribution.** Tag every citation: `[uk-legal MCP]` for legislation or case law retrieved via the uk-legal MCP; `[BAILII]` for case law from BAILII; `[legislation.gov.uk]` for statutory provisions; `[govuk MCP]` for GOV.UK guidance; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations from training data; `[user provided]` for user-supplied citations. Never strip or collapse the tags.

### Step 6: Equality Act pre-employment obligations

> **Research the EqA 2010 s.60 restriction** before advising on pre-offer screening. Asking about health or disability before making a conditional job offer is restricted under EqA 2010 s.60. The restriction is strictly interpreted: questions about attendance, sickness record, and adjustments are generally prohibited pre-offer. Post-offer occupational health assessments are permitted. Research the current scope of the restriction and any permitted exceptions (e.g., assessing whether reasonable adjustments are needed to the recruitment process itself, or whether a health question is genuinely necessary to determine whether a person has a protected characteristic required for the role). Cite primary sources.

Also check:
- **DBS checks**: for roles involving regulated activity with children or vulnerable adults, a Disclosure and Barring Service (DBS) check is mandatory. For other roles, a Basic DBS check is available. Research the current eligibility and legal framework for the check level proposed.
- **Rehabilitation of Offenders Act 1974**: for roles that are not exempted, convictions that are "spent" under the ROA 1974 need not be disclosed and cannot be used as a reason not to hire. Research whether this role is exempted (i.e., whether an Enhanced DBS check is permissible), and if not, whether the offer letter or application process asks about spent convictions. Verify currency.
- **Discrimination in recruitment**: are the shortlisting criteria, interview process, and offer terms free of direct or indirect discrimination on any of the nine protected characteristics?

### Step 7: Offer letter content

Read the letter. Check:

- Start date, job title, salary/pay rate, pay interval, and reporting line stated
- Employment status stated clearly (employee / worker)
- Notice period present and meets ERA s.86 statutory minimum (or reference to the written statement where the full particulars will appear)
- Holiday entitlement present and meets 5.6 weeks statutory minimum (WTR 1998)
- Right-to-work contingency clear (offer conditional on satisfactory check)
- DBS check contingency clear (if applicable)
- Probationary period stated (if intended — note that probation does not remove unfair dismissal rights for automatic grounds; ordinary unfair dismissal qualifying period is 2 years regardless of probation)
- Post-termination restrictions cross-referenced to the main contract (where included)
- Governing law: confirm English / Scottish / Northern Irish law as appropriate

**Do not include "at-will" language.** Employment at will does not exist in UK law. Employees have statutory rights from day 1, including protection from automatic unfair dismissal and discrimination. Adding at-will language to a UK offer letter is legally meaningless at best and misleading at worst. If any US-template language appears in the offer, flag it for removal.

## Output

> **Jurisdiction assumption.** This review applies the rules of the employee's work jurisdiction identified in Step 1. Post-termination restriction enforceability, s.1 particulars requirements, DBS check eligibility, and ROA exemptions are jurisdiction-specific. If the candidate's work location changes after the offer, this review may not apply as written.

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Hiring Review: [Candidate] — [Role] — [Jurisdiction]

**Overall:** [Clear to send | Changes needed | Escalate]

### Jurisdiction: [E&W / Scotland / NI]
[Jurisdiction table entry. Any auto-escalate triggers that fire.]

### Employment status
[Employee / worker / self-employed call, grounded in working arrangements.
IR35 flag if via PSC. Any flags.]

### Right to Work
[Check method required. Any flags — 🔴 if pre-hire obligation outstanding.]

### Written Statement of Particulars (ERA s.1)
[Missing items from the checklist above. Flag any gap.]

### Post-termination restrictions
[If any. Enforceability call per researched case law, with pinpoint cites and
currency note. Suggested changes.]

### Equality Act / DBS / ROA
[Pre-employment health questions check. DBS check level and legality. ROA
spent conviction flag if applicable.]

### Offer letter
[Any remaining issues with the letter itself — at-will language, missing
notice period, holiday below statutory minimum, etc.]

### Action items
- [ ] [specific change needed before sending]
```

## Consequential-action gate (make an offer)

**Before producing a "Clear to send" recommendation or a final offer for signature:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Making an offer has legal consequences — the letter is a contract, and employment status, Right to Work compliance, and post-termination restrictions are difficult to reset once the offer is accepted. Have you reviewed this offer with a solicitor or HR professional with employment law expertise? If yes, proceed. If no, here's a brief to bring to them:
>
> - Candidate, role, jurisdiction (where they'll actually work)
> - Employment status call and why
> - Right to Work: check method required and whether it has been carried out
> - Post-termination restrictions in the offer and the enforceability analysis
> - Equality Act pre-employment obligations (health questions, DBS, ROA)
> - Missing or non-compliant s.1 particulars
> - Open questions and what's unresolved
> - What could go wrong (illegal working civil penalty, unenforceable restrictive covenant, EqA s.60 breach, IR35 liability)
> - What to ask the solicitor (is the status call correct; can we enforce this restriction; is the DBS check level right; are there any missing particulars)
>
> If you need to find a solicitor specialising in employment law: the SRA's Find a Solicitor tool (sra.org.uk/consumers/find-a-solicitor) is the official public register. ACAS (acas.org.uk) provides free guidance for employers on hiring obligations.

Do not produce a "Clear to send" output past this gate without an explicit yes. A marked-DRAFT flagged for solicitor review is fine.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer or HR professional picks.

## What this skill does not do

- Draft the offer letter — reviews it.
- Make the hire decision — checks the paperwork.
- State restrictive covenant enforceability, s.1 particulars requirements, or DBS check eligibility from memory — every call is based on researched, cited primary sources verified for currency.
- Assess the Right to Work check itself — the employer must use the Home Office online service or carry out the document check directly.
- Cover TUPE obligations where the hire relates to a business transfer — flag and refer separately.
