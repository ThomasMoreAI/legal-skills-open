---
name: termination-review-yachela
title: /termination-review
description: Termination review — high-risk flag detection, severance + release, and final pay timing by jurisdiction. Jurisdiction-specific rules and release consideration periods are researched per review, not stored. Use when the user says "reviewing a termination", "can we fire this person", "term review", or describes a termination scenario.
author: yachela
author_url: https://github.com/yachela/claude-for-legal-ar/tree/main/employment-legal/skills/termination-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: ar
practice: employment
language: en
---

# /termination-review

1. Load `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → termination review triggers, high-risk flags, severance practice, jurisdiction rules.
2. Use the workflow below.
3. Walk the checklist. Check every high-risk flag.
4. Final pay timing per employee's jurisdiction. Severance + release if applicable.
5. If any high-risk flag fires: escalate per table, don't proceed without sign-off.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Most terminations are fine. A few are lawsuits waiting to happen. This skill
runs the checklist that catches the second kind before the decision is final.
The skill does not state the law — every jurisdiction-specific rule and
release-period requirement is researched and cited at the time of review.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → termination review triggers, high-risk flags, standard severance,
jurisdiction table.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`). Match the memo format from seed term memos referenced in that config where one exists. The work-product header is always first.

## Workflow

### Step 1: The basic facts

- Employee name (or role if staying abstract)
- Jurisdiction (where they work)
- Reason for termination (performance, misconduct, RIF, position elimination)
- How long employed
- Age (relevant to release requirements for older-worker protections)
- Whether any other employees are being terminated as part of the same
  decisional unit or program (relevant to group-termination release rules)
- When is the planned term date

### Step 2: High-risk flag scan

This is the most important step. Check every flag from `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. Default
set:

| Flag | Why it's high-risk | Check |
|---|---|---|
| **Recent complaint** | Retaliation claim | Has this employee filed any complaint (HR, ethics hotline, regulatory) recently? |
| **Protected leave** | Leave-law interference/retaliation | Currently on or recently returned from protected leave (FMLA/state equivalents, disability, parental, military in the US; *enfermedad/accidente inculpable* Art. 208 LCT or *maternidad* Art. 177 LCT in Argentina)? |
| **Protected class + timing** | Discrimination claim | Protected class AND recently disclosed/visible (pregnancy, religious accommodation, disability)? In Argentina, note maternity (Art. 177/178 LCT) or marriage (Art. 180/181 LCT) protections. |
| **Whistleblower** | Federal and state whistleblower statutes | Has this employee raised concerns about illegality, safety, fraud? |
| **Thin documentation** | "Why now?" problem | For performance terms: is there a PIP, written warnings, documented feedback? Or did this come out of nowhere? |
| **Comparator problem** | Disparate treatment | Is someone else doing the same thing and not being terminated? |
| **Contract/handbook promise** | Breach | Does the offer letter, handbook, or any writing promise a process that isn't being followed? |
| **Exempt / Contractor misclassification** | FLSA + state wage claim / LCT dependency claim | See the classification checks below (US exempt threshold vs Argentina contractor/monotributo risk). |
| **Union representation (AR only)** | Tutela sindical protection | Is the employee a union delegate or representative (*delegado sindical*) protected by Ley 23.551? |

**Exempt/non-exempt classification flag (US).** Fire this flag when ALL of the following are true:
1. The employee works in a US state with a high exempt salary threshold — **CA, NY, WA, CO, AK** (and any other state listed in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → `## Wage & hour` → Known classification risk areas as a high-threshold state) — **AND**
2. The employee is classified **exempt** (salaried, no overtime) — **AND**
3. The employee's title contains **"supervisor," "lead," "coordinator," "analyst," "administrator,"** or **"specialist"** (case-insensitive, and any equivalent-scope title the practice profile flags as risky).

When all three fire, emit:
> 🔴 **Potential exempt misclassification (US)** — [title] earning $[X] in [state]. The exempt salary threshold in [state] is approximately $[Y] `[model knowledge — verify]`. Before termination, route to `/employment-legal:wage-hour-qa` for a classification check.

**Contractor / Monotributo misclassification flag (Argentina).** Fire this flag when the jurisdiction is Argentina (AR) AND:
1. The individual is engaged as an independent contractor (claims payment via invoice/*factura* / *Monotributo*) — **AND**
2. The relationship has characteristics of employment (regular schedule, office/systems access, direct supervision, integration into core teams).

When this fires, emit:
> 🔴 **Potential contractor misclassification (Argentina - Art. 23 LCT)** — Engaged as contractor but shows signs of employment. Art. 23 LCT establishes a strong presumption of an employment relationship when services are rendered. Under Argentine law, a terminated contractor who successfully claims employment status is entitled to full retrospective labor benefits, including salary differences, unpaid SAC/vacations, social security contributions, and severe penalties for unregistered employment (e.g., Ley 24.013 or Ley 25.323 `[model knowledge — verify]`). Route to `/employment-legal:worker-classification` for evaluation.

**Maternity / Marriage / Union protection flags (Argentina).** Fire if jurisdiction is Argentina (AR) AND:
- The employee is pregnant or has given birth within the last 7.5 months: presumes dismissal due to pregnancy (Art. 177/178 LCT), triggering 1 year of salary as additional penalty (Art. 182 LCT).
- The employee married within the last 3 months or is marrying in the next 6 months: presumes dismissal due to marriage (Art. 180/181 LCT), triggering 1 year of salary as penalty (Art. 182 LCT).
- The employee holds a union position (*delegado gremial*): stability under Ley 23.551. Absolute bar to dismissal without prior judicial exclusion process (*exclusión de tutela*).

If any flag fires, emit:
> 🔴 **Special Protection Flag (Argentina)** — Dismissal is highly restricted or triggers severe penalties under LCT Art. 182 or Ley 23.551 `[model knowledge — verify]`. Do not proceed with termination without legal counsel review.

**If a back-pay number is being computed as part of this review (severance modeling, settlement posture, exposure estimate), do NOT compute it in this skill.** Route to `wage-hour-qa` → Step 2a and use its regular-rate scaffold.

**Any flag fires → escalate per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` before the term proceeds.** Not after. Before.

### Step 3: Jurisdiction-specific requirements

> **Research the applicable rules for the employee's jurisdiction before finalizing the plan.** Specifically:
>
> - **Final-pay timing** — In the US, this varies by state. In Argentina, LCT Art. 128 requires payment within 4 business days of termination. Research waiting-time or late-pay penalties (e.g. Art. 9 Ley 25.013 / LCT Art. 275).
> - **Accrued-PTO payout** — In Argentina, proportional unused vacation (*vacaciones no gozadas*) must always be paid upon termination (Art. 156 LCT), plus the proportional SAC (aguinaldo) on those vacations.
> - **Required notices** — Research required notices (e.g. state unemployment in the US; telegram/notary notification of dismissal in Argentina under Art. 235 LCT).
> - **Mass-layoff / plant-closing notices** — In the US, research WARN Act / state mini-WARN. In Argentina, research the *Procedimiento Preventivo de Crisis* (PPC) under Ley 24.013 (required before collective dismissals or suspensions due to force majeure or lack of work).
>
> Cite primary sources. Verify currency.
>
> **No silent supplement.** If a research query to the configured legal research tool returns few or no results for the jurisdiction's final-pay, PTO, notice, or WARN/PPC rule, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking.
>
> **Source attribution.** Tag every citation in the plan — final-pay rule, PTO rule, notices, WARN / PPC, OWBPA consideration periods, LCT indemnity articles, state/national release restrictions — with where it came from: `[Westlaw]`, `[CourtListener]`, or the MCP tool name for citations retrieved from a legal research connector; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for citations the user supplied. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 4: Severance and release

Per `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → standard severance:

- Is severance being offered? Per formula or discretionary?
- Release required? (Usually yes if paying severance — that's the
  consideration.)

> **Research the applicable release-consideration rules.** If the employee is
> 40 or over, federal law (OWBPA) imposes specific requirements that affect
> the consideration period, revocation period, required advisements, and —
> for group terminations — required decisional-unit disclosures. The specific
> consideration period differs between an individual termination, a group
> RIF, and a group exit incentive; the rule also depends on the employee's
> age and the number of employees affected. Do not state the day count from
> memory — research the currently operative rule for the specific situation
> and cite primary sources. Also research any state-law analogs or parallel
> release requirements. Verify currency.

Separately, consider whether any of the following apply to the release:
- State-specific waiver restrictions (some states limit what can be released
  or require specific language).
- Federal or state restrictions on non-disclosure or non-disparagement
  clauses that relate to sexual harassment, discrimination, or other
  protected categories.
- Separation-agreement rules on NLRA-protected activity.

### Step 5: Documentation check

For performance terminations especially:

- Is there a paper trail? Written warnings, PIP, feedback docs?
- Does the paper trail tell a consistent story?
- Is there anything in writing that contradicts the reason (recent positive
  review, bonus, promotion)?

The "why now" question: if this person has been underperforming for a year,
what changed? The answer should be documented.

## Output

> **Research-connector pre-flight.** Before emitting the memo, check whether a legal research connector is reachable for this session — Westlaw, CourtListener, or any firm-configured research MCP. Collect this into the reviewer note per CLAUDE.md `## Outputs`: if no connector returns results in Step 3 (or none is configured at run time), record it in the **Sources:** line of the reviewer note — e.g., `not connected — cites from training knowledge; the highest-fabrication topics in termination-law memos are final-pay timing, OWBPA group/individual distinctions, state-specific NDA / non-disparagement rules (e.g., CA SB 331) in the US, and Art. 245 bases, preaviso, and Art. 241 mutual agreement validation in Argentina — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner.

> **Jurisdiction assumption.** This review assumes the employee's jurisdiction as stated in Step 1 and defaults from `CLAUDE.md` → Jurisdictional footprint. If the employee works in a different state or country (such as Argentina instead of a US state), the legal analysis, indemnities, and notice periods will differ fundamentally.

Match the memo format from seed term memos referenced in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If none:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Termination Review: [Role/Name] — [Date]

**Jurisdiction:** [State / Argentina (AR)]
**Reason:** [Performance / Misconduct / RIF / Elimination / Despido incausado]
**Planned date:** [Date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one-sentence why]

---

### High-risk flags

[Every flag from Step 2. ✅ Clear or 🔴 FLAG with detail.]

**Escalation:** [None needed | Escalate to [name] before proceeding — [which flag]]

---

### Jurisdiction requirements ([State / Argentina])

#### US (if applicable)
- Final pay: [researched rule and cite]
- Required notices: [list, each researched and cited]
- Mass-layoff notice: [researched rule and cite]

#### Argentina (if applicable)
- Final pay timing: LCT Art. 128 (within 4 business days)
- Base calculations & Indemnities (Art. 245 LCT for seniority, Art. 231/232 LCT for preaviso, Art. 233 LCT for integration of month of dismissal)
- Art. 80 LCT Certificate: Mandatory delivery of labor certificates within 30 days of termination (failing to do so triggers a fine of 3 salaries under Art. 45 Ley 25.345) `[model knowledge — verify]`.
- Dismissal communication: Written notification via Telegram/Notary (Art. 235 LCT).

---

### Severance and release

- Severance: [amount per formula / none]
- Release: [required / not. If Argentina (AR): must be executed via Mutual Agreement under Art. 241 LCT before a Notary (*escribano público*) or validated/approved (*homologado*) by the Ministry of Labor/SECLO under Art. 15 LCT to be valid and binding; private unhomologated agreements are high-risk under Art. 12 LCT `[model knowledge — verify]`].
- [Any state-law release rules or non-disclosure/non-disparagement restrictions that apply]

---

### Documentation

[Assessment of paper trail. Gaps flagged.]

---

### Go / No-go

[Clear to proceed | Proceed with changes below | Hold — escalation pending]

### Checklist for term day

#### US (if applicable)
- [ ] Final paycheck ready, correct amount, delivered per researched rule
- [ ] Continuation-coverage notices (COBRA / state analogs) prepared
- [ ] [State] unemployment notice prepared
- [ ] Severance agreement (if applicable)
- [ ] Return of property / access cutoff coordinated

#### Argentina (if applicable)
- [ ] Notary or Telegram notice drafted and sent (Art. 235 LCT)
- [ ] Final pay calculated: days worked, proportional SAC (aguinaldo), vacation settlement, LCT indemnities (Art. 245, 232, 233)
- [ ] final payment deposition scheduled within 4 business days
- [ ] Art. 80 LCT Certificate compilation started (to be delivered within 30 days)
- [ ] Mutual agreement draft prepared for SECLO / Ministerio de Trabajo or Notary (if Art. 241 LCT release is planned)
- [ ] Return of property / access cutoff coordinated
```

## Consequential-action gate (terminate an employee)

**Before producing a "Go" recommendation or a term-day checklist marked ready:** Read `## Who's using this` in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`. If the Role is **Non-lawyer**:

> Terminating an employee has legal consequences — wrongful-termination, discrimination, retaliation, and wage-law claims all trace back to how this decision is structured. Have you reviewed this termination with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - Employee, jurisdiction, reason, planned date
> - Every high-risk flag the review surfaced — with detail
> - Jurisdiction-specific findings (final pay, LCT indemnities, required notices, mass-layoff/PPC rules) and where they were cited from
> - Severance/release analysis, including any OWBPA (US) or Art. 241 LCT / SECLO (Argentina) validation requirements
> - Open questions and what's unresolved
> - What could go wrong (the claim theory this fact pattern supports)
> - What to ask the attorney
>
> If you need to find an attorney, solicitor, barrister, or other authorised legal professional: contact your professional regulator (state bar in the US; in Argentina, the *Colegio Público de Abogados* of the relevant jurisdiction, such as CPACF for Buenos Aires, or similar provincial associations) for a referral service.

Do not produce a "Clear to proceed" output past this gate without an explicit yes. A marked-DRAFT flagged for attorney review is fine.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customize the options to what this skill just produced. The tree is the output; the lawyer picks.

## What this skill does not do

- Make the termination decision. It checks the decision.
- Have the conversation. The manager does that.
- State release or jurisdiction rules from memory — every rule is researched and cited at the time of review.
- Guarantee no lawsuit. It reduces the risk by catching the obvious problems.
