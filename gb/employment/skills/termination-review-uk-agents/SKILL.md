---
name: termination-review-uk-agents
title: /termination-review
description: Termination review — automatic unfair dismissal flag detection, notice and final pay, statutory redundancy (where applicable), ACAS Code compliance, and Settlement Agreement gate. Jurisdiction-specific rules are researched per review, not stored. Use when the user says "reviewing a dismissal", "can we dismiss this person", "term review", "making someone redundant", "capability dismissal", or describes a termination scenario in England, Wales, or Scotland.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/employment-legal-uk/skills/termination-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
---

# /termination-review

1. Load `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → dismissal review triggers, high-risk flags, notice/severance practice, jurisdiction.
2. Use the workflow below.
3. Walk the checklist. Automatic unfair dismissal flags are the priority — they carry no qualifying period.
4. Notice, final pay, and accrued holiday per employee's jurisdiction (E&W / Scotland / NI).
5. If any high-risk flag fires: escalate per table, don't proceed without sign-off.

---

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Most dismissals are defensible. A few generate Employment Tribunal claims that
trace back to a preventable decision or a missed step. This skill runs the
checklist that catches the second kind before the decision is final. It does
not state the law — every jurisdiction-specific rule and statutory requirement
is researched and cited at the time of review.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → dismissal review triggers, high-risk flags, standard notice/severance practice, jurisdiction table.

## Output header

Prepend the work-product header from `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → `## Outputs` (it differs by user role — see `## Who's using this`). Match the memo format from seed dismissal memos referenced in that config where one exists. The work-product header is always first.

## Workflow

### Step 1: The basic facts

- Employee name (or role if staying abstract)
- Jurisdiction: England & Wales, Scotland, or Northern Ireland
- Reason for dismissal: capability (performance or ill-health), conduct (misconduct), redundancy, statutory illegality, or some other substantial reason (SOSR — specify)
- Length of continuous service (affects qualifying period for ordinary unfair dismissal and statutory redundancy entitlement)
- Employment status: employee, worker, or contractor (affects which protections apply — see employment status gate in Step 2)
- Age (relevant to statutory redundancy pay formula)
- Whether any other employees are being dismissed as part of the same exercise (collective redundancy threshold check)
- Proposed effective date of termination (EDT)
- Notice: contractual notice period; whether the employer intends to serve notice, place on garden leave, or pay in lieu (PILON)

### Step 2: High-risk flag scan

This is the most important step. Automatic unfair dismissal rights carry **no qualifying period** — they apply from day 1 of employment regardless of length of service. Check every flag.

| Flag | Why it's high-risk | Check |
|---|---|---|
| **Protected disclosure (whistleblowing)** | Automatic unfair dismissal — ERA 1996 s.103A; compensation uncapped | Has this employee made a qualifying disclosure about wrongdoing, illegality, a health & safety danger, an environmental breach, a miscarriage of justice, or a cover-up? |
| **Pregnancy / maternity / adoption / shared parental leave** | Automatic unfair dismissal — ERA 1996 s.99; protection extends through leave and for 18 months post-birth | Is the employee pregnant, on or recently returned from maternity, adoption, paternity, or shared parental leave? |
| **Health and safety activity** | Automatic unfair dismissal — ERA 1996 s.100 | Has the employee raised health and safety concerns, left or refused to return to a dangerous workplace, or acted as a safety representative? |
| **Trade union membership or activity** | Automatically unfair — TULRCA 1992 s.152 | Is the employee a union member, or have they taken part in trade union activities or lawful industrial action? |
| **Asserting a statutory right** | Automatic unfair dismissal — ERA 1996 s.104 | Has the employee recently asserted a statutory right (NMW, working time, right to written statement, right to be accompanied)? |
| **Protected characteristic (Equality Act 2010)** | Direct or indirect discrimination, or discriminatory dismissal — EqA 2010; compensation uncapped | Does the reason for or timing of the dismissal engage any of the nine protected characteristics: age, disability, sex, race, religion or belief, sexual orientation, pregnancy and maternity, marriage and civil partnership, gender reassignment? |
| **Disability — reasonable adjustments not made** | Failure to make reasonable adjustments before dismissal for incapability — EqA 2010 s.21 | Is there an underlying disability? Has occupational health been consulted? Have reasonable adjustments been considered and documented? Has the employer followed its own capability procedure? |
| **Part-time or fixed-term status** | Part-time Workers (Prevention of Less Favourable Treatment) Regulations 2000; Fixed-term Employees (Prevention of Less Favourable Treatment) Regulations 2002 | Is the employee being treated less favourably, or selected for redundancy, on the basis of part-time or fixed-term status without objective justification? |
| **ACAS Code not followed** | 25% uplift on ET compensatory award — TULRCA 1992 s.207A | For misconduct and capability dismissals: was the ACAS Code of Practice on Disciplinary and Grievance Procedures followed? Written investigation, invitation to meeting with reasonable notice, right to be accompanied (ERA 1999 s.10), written decision, right of appeal? |
| **Thin or contradictory documentation** | "Why now?" problem at tribunal | For capability/conduct: is there a paper trail (PIPs, written warnings, documented feedback)? Or a recent positive appraisal, pay rise, or promotion that contradicts the reason? |
| **Collective redundancy threshold** | TULRCA 1992 s.188 minimum consultation; HR1 notification; protective award of up to 90 days' pay per employee | Is this redundancy part of a wider exercise? How many employees at the same establishment are being made redundant within a 90-day window? (≥20 → 45-day minimum collective consultation and HR1; 1–19 → 30-day minimum) |
| **Contract or handbook promise** | Wrongful dismissal / breach of contract | Does the contract, handbook, or any written communication promise a process that is not being followed? |

**Automatic unfair dismissal — no qualifying period.** The flags marked above apply from day 1 of employment. Do not discount these because the employee has short service. The 2-year qualifying period (ERA 1996 s.108) applies only to ordinary unfair dismissal — not to the automatic grounds listed above.

**Employment status gate.** If employment status is not confirmed as **employee**, note it prominently. Workers have NMW, working time, and holiday rights but generally lack ordinary unfair dismissal protection. Genuinely self-employed contractors have neither. If status is contested or the arrangement looks like disguised employment, route to `/employment-legal-uk:worker-classification` before proceeding — the dismissal risk profile changes materially.

**If any flag fires → escalate per `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` before the dismissal proceeds.** Not after. Before.

### Step 3: Jurisdiction-specific requirements

> **Research the applicable rules for the employee's jurisdiction before finalising the plan.** ERA 1996 and EqA 2010 apply across Great Britain; TULRCA 1992 applies across Great Britain. Northern Ireland has parallel legislation (Employment Rights (Northern Ireland) Order 1996 etc.) — flag any NI dismissal explicitly. Research specifically:
>
> - **Statutory minimum notice** — ERA 1996 s.86: 1 week per completed year of continuous service, up to a maximum of 12 weeks (minimum of 1 week after the first month). Contractual notice applies if longer. Research the current rule and verify currency.
> - **PILON clause** — if the employer intends to pay in lieu of notice, verify whether the contract contains a PILON clause. Paying PILON without a contractual PILON clause was historically treated as a breach of contract (wrongful dismissal); since April 2018, all PILON payments are taxable as earnings under ITEPA 2003 s.402D regardless of whether a PILON clause exists, but the breach-of-contract analysis still matters for the dismissal itself.
> - **Accrued but untaken holiday** — under WTR 1998, accrued statutory annual leave (up to 5.6 weeks) must be paid out on termination. Research the current calculation method, especially for employees with irregular hours or variable pay (the *Brazel v Harpur Trust* [2022] UKSC 21 12.07% cap approach was overruled; check the current position for part-year/irregular-hours workers post the Employment Rights Act holiday pay amendments). Verify currency.
> - **Statutory redundancy pay** — if the reason is redundancy, research the current statutory redundancy pay formula: age bracket × years of service (capped at 20) × weekly pay (capped at the current statutory maximum, uprated each April). Verify the current weekly pay cap.
> - **Collective redundancy** — if ≥20 redundancies in 90 days at the same establishment: TULRCA 1992 s.188 minimum consultation period (45 days), duty to notify Secretary of State on form HR1, and obligation to consult appropriate representatives. Failure carries a protective award of up to 90 days' pay per affected employee with no upper cap. Research current requirements and verify.
> - **Effective date of termination (EDT)** — the EDT governs the 3-month ET limitation period. Research how the EDT is calculated in this scenario (notice given and worked, notice given and paid in lieu, summary dismissal for gross misconduct).
>
> Cite primary sources. Verify currency.
>
> **No silent supplement.** If a research query returns few or no results for a required topic, report what was found and stop. Do NOT fill the gap from web search or model knowledge without asking. Say: "The search returned [N] results from [tool]. Coverage appears thin for [topic]. Options: (1) broaden the search query, (2) try a different research tool, (3) search the web — results will be tagged `[web search — verify]` and should be checked against a primary source before relying, or (4) stop here and flag for solicitor verification. Which would you like?"
>
> **Source attribution.** Tag every citation: `[uk-legal MCP]` for legislation or case law retrieved via the uk-legal MCP; `[BAILII]` for case law from BAILII; `[legislation.gov.uk]` for statutory provisions checked against the official source; `[govuk MCP]` for GOV.UK guidance; `[web search — verify]` for web-search citations; `[model knowledge — verify]` for citations recalled from training data; `[user provided]` for user-supplied citations. Citations tagged `verify` carry higher fabrication risk and should be checked first. Never strip or collapse the tags.

### Step 4: Notice, final pay, and settlement

Per `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → standard notice and severance practice:

- **Notice**: what form is the employer giving notice? Working notice, garden leave, or PILON?
- **Garden leave**: if used, check the contract for an express garden leave clause. Placing an employee on garden leave without one can be treated as a repudiation of the contract.
- **Enhanced / ex-gratia payment**: if an enhanced payment is being offered above the statutory and contractual minimum, is a Settlement Agreement (under ERA 1996 s.203) being used to obtain a valid waiver of ET claims? A Settlement Agreement requires the employee to have received independent legal advice from a relevant independent adviser; the employer customarily contributes to the cost of that advice.

> **Research the Settlement Agreement requirements** if a compromise is being offered. ERA 1996 s.203 sets mandatory conditions for a valid waiver. Do not state the requirements from memory — verify the current statutory requirements, including the independent adviser certificate requirement, and the HMRC/ITEPA 2003 position on termination payments (the £30,000 statutory exemption under s.403, the post-April 2018 PILON rules, injury to feelings payments in discrimination cases). Cite primary sources and verify currency.

### Step 5: Documentation check

For capability and conduct dismissals:

- Is there a paper trail? Disciplinary or capability proceedings, written warnings, PIPs, documented one-to-ones, occupational health referrals?
- Was the ACAS Code of Practice on Disciplinary and Grievance Procedures followed? Written investigation, invitation to meeting with reasonable notice, right to be accompanied, written decision, right of appeal?
- Does the paper trail tell a consistent story — or does a recent positive appraisal, bonus, or promotion contradict the reason for dismissal?

For redundancy:

- Was there a genuine redundancy situation (ERA 1996 s.139 definition)?
- Was a fair selection pool identified and applied?
- Were fair and objective selection criteria used (not criteria that indirectly discriminate)?
- Was meaningful individual consultation carried out with the at-risk employee?
- Were alternatives to redundancy genuinely considered (redeployment, reduced hours)?

## Output

> **Research-connector pre-flight.** Before emitting the memo, check whether a legal research connector is reachable — the uk-legal MCP or BAILII. If no connector returns results in Step 3 (or none is configured), record it in the **Sources:** line of the reviewer note: e.g., `not connected — cites from training knowledge; the highest-fabrication topics in UK dismissal memos are statutory pay caps (uprated each April), holiday pay calculation method for irregular-hours workers (post-*Brazel* amendments), collective redundancy thresholds, and PILON tax treatment post-April 2018 — spot-check those first`. Per-citation `[model knowledge — verify]` tags remain inline. Do not emit a standalone banner above the memo.

> **Jurisdiction assumption.** This review assumes England & Wales unless stated otherwise. ERA 1996, EqA 2010, and TULRCA 1992 apply across Great Britain; Northern Ireland has parallel legislation and should be flagged explicitly. If the employee works cross-border or choice-of-law is contested, this analysis may not apply as written.

Match the memo format from seed dismissal memos referenced in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`. If none:

```markdown
[WORK-PRODUCT HEADER — per plugin config ## Outputs — differs by role; see `## Who's using this`]

## Termination Review: [Role/Name] — [Date]

**Jurisdiction:** [England & Wales / Scotland / Northern Ireland]
**Reason:** [Capability / Misconduct / Redundancy / SOSR — specify]
**Continuous service:** [length — flag if under 2 years for ordinary UD]
**Proposed EDT:** [date]

---

### Bottom line

[Can you proceed / Need to fix X first / Stop — one sentence]

---

### High-risk flags

[Every flag from Step 2. ✅ Clear or 🔴 FLAG with detail.]

**Escalation:** [None needed | Escalate to [name] before proceeding — [which flag]]

---

### Jurisdiction requirements (E&W / Scotland / NI)

- Statutory minimum notice: [ERA s.86 calculation vs contractual notice — whichever is longer]
- PILON clause: [present / absent — implications]
- Accrued holiday: [calculation method, researched and cited]
- Statutory redundancy pay (if applicable): [formula, current weekly pay cap, computed amount]
- Collective consultation (if applicable): [TULRCA s.188 check — number of redundancies, applicable period, HR1 requirement]
- EDT: [how calculated in this scenario]

---

### Notice, final pay, and settlement

- Notice: [form, amount, garden leave clause check if applicable]
- Final pay breakdown: [notice pay / PILON + accrued holiday + statutory redundancy + any ex-gratia]
- Settlement Agreement (if applicable): [ERA s.203 requirements, independent adviser note, tax treatment under ITEPA s.403]

---

### Documentation

[ACAS Code compliance for conduct/capability. Redundancy consultation record for redundancy. Assessment of paper trail and gaps.]

---

### Go / No-go

[Clear to proceed | Proceed with changes below | Hold — escalation pending]

### Checklist for dismissal day

- [ ] Dismissal letter prepared: reason, EDT, right of appeal (conduct/capability) or redundancy notice
- [ ] Notice served / garden leave commenced / PILON payment calculated per contract
- [ ] Accrued holiday pay included in final payment
- [ ] Statutory redundancy pay prepared (if applicable)
- [ ] P45 issued on or before final payment date
- [ ] Settlement Agreement issued and independent adviser contribution confirmed (if applicable)
- [ ] HR1 submitted to Insolvency Service (if collective redundancy ≥20)
- [ ] [etc.]
```

## Consequential-action gate (dismiss an employee)

**Before producing a "Go" recommendation or a dismissal-day checklist marked ready:** Read `## Who's using this` in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`. If the Role is **Non-lawyer**:

> Dismissing an employee has legal consequences — unfair dismissal, discrimination, whistleblower, and wrongful dismissal claims all trace back to how this decision is structured, documented, and timed. The Employment Tribunal time limit is 3 months less one day from the EDT; ACAS Early Conciliation must be initiated before that clock expires. Have you reviewed this dismissal with a solicitor or an HR professional with employment law expertise? If yes, proceed. If no, here's a brief to bring to them:
>
> - Employee, jurisdiction, reason, proposed EDT, length of service
> - Every high-risk flag the review surfaced — with detail
> - Jurisdiction-specific findings (notice, accrued holiday, redundancy pay, collective consultation) and where they were cited from
> - Settlement / ex-gratia payment analysis if applicable
> - Open questions and what's unresolved
> - What could go wrong (the ET claim this fact pattern supports, whether compensation is capped or uncapped)
> - What to ask the solicitor (is this a clean dismissal; do we need more documentation or process; should we offer a Settlement Agreement; is the redundancy selection defensible)
>
> If you need to find a solicitor specialising in employment law: the SRA's Find a Solicitor tool (sra.org.uk/consumers/find-a-solicitor) is the official public register. ACAS (acas.org.uk) provides free guidance and operates the Early Conciliation service. Employment tribunal representation can also be provided by barristers directly under the Bar Direct Access scheme.

Do not produce a "Clear to proceed" output past this gate without an explicit yes. A marked-DRAFT flagged for solicitor review is fine.

---

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced — the five default branches (draft the X, escalate, get more facts, watch and wait, something else) are a starting point, not a lock-in. The tree is the output; the lawyer or HR professional picks.

## What this skill does not do

- Make the dismissal decision. It checks the decision.
- Have the dismissal conversation. The manager does that.
- State notice entitlements, holiday pay calculation methods, or statutory pay caps from memory — every figure is researched and cited at the time of review.
- Guarantee no ET claim. It reduces the risk by catching the obvious problems.
- Advise in detail on Northern Ireland law — flag and refer to NI-specific employment advice where applicable.
- Cover TUPE transfers, where the dismissal may be automatically unfair — flag and refer separately.
