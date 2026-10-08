---
name: lba-drafter-b1rdmania
title: /lba-drafter
description: Drafts a Letter Before Action (LBA) for an employment dispute in England & Wales. Use when the user needs to put an employer on notice of a prospective Employment Tribunal claim or High Court / County Court claim arising from the employment relationship, before issuing proceedings. Triggers include "draft an LBA", "letter before action for unfair dismissal", "letter before claim", "put the employer on notice", or "pre-action letter".
author: b1rdmania
author_url: https://github.com/b1rdmania/claude-for-uk-legal/tree/master/uk-employment-legal/skills/lba-drafter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
---

# /lba-drafter

1. Confirm jurisdiction is England & Wales. Scotland and Northern Ireland have different time limits, tribunals, and procedural rules — this skill does not cover them.
2. Identify the dispute type: Employment Tribunal claim (unfair dismissal, discrimination, unlawful deduction, etc.) or contractual / High Court / County Court claim (wrongful dismissal, breach of contract, unpaid bonus over £25k).
3. Gather: claimant details, respondent details, factual chronology, statutory or contractual basis, remedies sought, deadline for response.
4. Apply the correct pre-action framework — Pre-Action Conduct Practice Direction for civil claims; ACAS Code of Practice for ET claims.
5. Draft. Surface time-limit risks before output (see Time-limit risk).
6. Render the finished letter — see the Output section. Do not echo the template back. For any unknown value, insert `[SOLICITOR: confirm X]` rather than guessing.

---

# Letter Before Action — UK employment

## Purpose

The LBA puts the prospective respondent on notice, sets out the claimant's case, invites response or settlement, and (where applicable) complies with pre-action protocols. A well-drafted LBA narrows issues, opens settlement, and protects costs position if the matter proceeds.

For Employment Tribunal claims, there is no formal pre-action protocol equivalent to those in civil litigation. The ACAS Code of Practice on Disciplinary and Grievance Procedures governs conduct that may affect compensation (up to 25% adjustment under s.207A TULR(C)A 1992). The LBA is still useful as a settlement and narrowing device.

For contractual employment claims in the civil courts, the Pre-Action Conduct Practice Direction applies, and non-compliance can attract costs sanctions.

## Time-limit risk

This is a prompt, not a system. It cannot enforce a deadline or block output. What it does is surface the limitation position so a solicitor cannot miss it. Date miscalculation is the single most common employment-litigation malpractice — so this skill never computes or asserts a limitation date as authoritative.

Employment Tribunal claims have **three-month** primary time limits (one month for some redundancy and TUPE claims) running from the act complained of (e.g. effective date of termination, last act of discrimination). ACAS early conciliation under s.18A Employment Tribunals Act 1996 extends the limit via the "stop the clock" mechanism in s.207B ERA 1996 — and the LBA does NOT stop time.

Infer from the matter file or inputs. Surface for confirmation if not provided:
- The act complained of and its date.
- Whether ACAS early conciliation has been started; if yes, Day A (notification to ACAS) and Day B (EC certificate issued).

Do not compute the limitation date. Insert `[SOLICITOR: confirm limitation date via a date calculator]` in the letter header and surface the inputs above for the solicitor to run the calculation. If the inputs suggest the primary limitation may be close, add a prominent note recommending the solicitor confirm the date and consider issuing ACAS notification before sending the LBA — a polite pre-action letter must not cost the client their claim. Flag inline: `[TIME LIMIT — confirm ET1 deadline before sending]`.

## Inputs to gather

- Claimant: full name, NI number (optional), address, dates of employment, role, contract type (employee / worker / self-employed — affects rights available).
- Respondent: legal entity name (check Companies House for limited companies, not the trading name), registered address, additional respondents if the claim is against named individuals for discrimination or harassment.
- Facts: chronology with dates. Pin down the effective date of termination if dismissal is alleged.
- Heads of claim: statutory (e.g., s.94 ERA — unfair dismissal; ss.13-27 ERA — unlawful deductions; Equality Act 2010 protected characteristics) or contractual.
- Remedies sought: reinstatement, re-engagement, basic and compensatory award, injury to feelings (discrimination), interest, costs (note ET costs regime is restrictive — see ETR 2013 rule 76).
- Settlement appetite: is the LBA inviting settlement, or purely putting on notice?

## Workflow

### Step 1 — Confirm jurisdiction and capacity

England & Wales only. Confirm the claimant was working under English law (Lawson v Serco `[CITE NEEDED — authority]`-style territorial scope checks for unusual cases). Confirm the respondent is a legal entity that can be served.

### Step 2 — Confirm claim type and forum

Most employment claims go to the Employment Tribunal. Contractual claims for sums over £25,000 must go to the civil courts (ET jurisdiction over contract claims under the Employment Tribunals (Extension of Jurisdiction) Order 1994 is capped at £25,000 and only on termination). Discrimination claims always go to the ET. Wrongful dismissal can go to either.

### Step 3 — Apply the correct pre-action framework

- **ET claim**: ACAS Code of Practice on Disciplinary and Grievance Procedures, plus the ACAS early conciliation regime (s.18A ETA 1996).
- **Civil claim**: Pre-Action Conduct PD, plus any specific protocol (none applies to most employment-contract claims, so PACC alone).

### Step 4 — Draft

Use the structure in the Output section. Keep tone firm but not aggressive. Plead the cause of action, the facts that support each element, and the loss. Invite a substantive response within a reasonable deadline (14 days for civil PACC by default; 14-21 days is conventional for ET LBAs).

### Step 5 — Costs and "without prejudice"

The LBA itself is open correspondence. If a settlement offer is being made, mark a separate enclosure "Without Prejudice Save As To Costs" — do not mix open and WP material in one letter. See the `without-prejudice-drafter` skill for WP correspondence.

### Step 6 — Citation discipline

Any case relied on in the letter must carry `[CITE NEEDED — authority]` until the solicitor verifies the citation. Do not state a case as settled law from memory. This applies to the unfair-dismissal authorities (Burchell, Polkey, Iceland Frozen Foods), territorial-scope authority (Lawson v Serco), and any other case the draft invokes. Verify every citation and the limitation date with counsel before the letter is sent.

## Output

Render the finished letter using the structure below. Do not echo this structure back as a template, and do not invent facts to fill a section. For any value you do not have, insert `[SOLICITOR: confirm X]` rather than guessing. The output is the letter itself, ready for a solicitor to review, complete, sign and serve.

[Solicitor letterhead / client letterhead]

[Date]

[Respondent name]
[Respondent address]

**BY EMAIL AND POST**

Dear Sirs,

**Re: [Claimant name] — Letter Before Action**

We act for [Claimant], formerly employed by you as [role] from [start date] to [EDT or date of resignation].

**Time-limit notice:** The primary limitation period for an Employment Tribunal claim arising from these matters expires on `[SOLICITOR: confirm limitation date via a date calculator]`. ACAS early conciliation [has been started on [date] / will be commenced shortly]. This letter does not extend the limitation period.

## 1. Background facts

[Numbered chronology of material facts, dated, neutral in tone.]

## 2. Cause(s) of action

[For each head of claim, plead the statutory or contractual basis and apply the facts to the elements.]

- **Unfair dismissal (s.94 ERA 1996)**: Our client had [length] of continuous service and was dismissed on [date]. The dismissal was unfair because [band of reasonable responses analysis per Iceland Frozen Foods `[CITE NEEDED — authority]`; conduct-dismissal test per Burchell `[CITE NEEDED — authority]`; Polkey `[CITE NEEDED — authority]` on procedural fairness, as applicable]. Reason: [conduct / capability / redundancy / SOSR / automatically unfair].
- **Discrimination (Equality Act 2010, s.[13/19/26/27])**: Protected characteristic — [characteristic]. Less favourable treatment / PCP / unwanted conduct / detriment. Comparator (actual or hypothetical): [...].
- **Unlawful deduction from wages (s.13 ERA 1996)**: Sums properly payable but not paid: [amount and basis].
- **Wrongful dismissal / breach of contract**: Notice period [length]; pay in lieu owed: [amount].

## 3. Loss and remedy sought

[Basic award computation; compensatory award (capped at the lower of one year's gross pay or the statutory cap — `[SME VERIFY — current compensatory award cap]`); injury to feelings per Vento bands `[SME VERIFY — current Vento bands]`; interest; pension loss.]

We invite you to make proposals for settlement within [14 / 21] days of the date of this letter, failing which our client reserves the right to issue proceedings without further notice.

Please confirm by return whether you instruct solicitors and, if so, provide their contact details for service.

## 4. ACAS Code

Our client expects you to engage with the ACAS Code of Practice. Failure to do so may result in an uplift of up to 25% on any compensation award under s.207A TULR(C)A 1992.

## 5. Costs

In the Employment Tribunal, costs are awarded only in limited circumstances (ETR 2013 rule 76). In any civil proceedings, our client will rely on this letter on the question of costs under CPR Part 44.

Yours faithfully,

[Signature block]

## Markers used

Mark uncertainty inline as you draft. Never silently guess a value.

- `[SOLICITOR: confirm X]` — any unknown value, including the limitation date. The solicitor confirms before sending.
- `[TIME LIMIT — confirm ET1 deadline before sending]` — when the inputs suggest limitation may be close.
- `[SME VERIFY — figure]` — for figures that change (compensatory award cap, statutory week's pay, Vento bands).
- `[CITE NEEDED — authority]` — any case cited from memory (Burchell, Polkey, Iceland Frozen Foods, Lawson v Serco, etc.); verify the citation before relying on it.
- `[FACT NEEDED — what's missing]` — for factual gaps that must be filled before sending.

## What this skill does not do

This skill drafts for solicitor review. It does not give legal advice. It produces a working draft, not a sent letter, and not a legal opinion.

- Give legal advice or substitute for independent legal advice for the claimant.
- Compute or assert a limitation date. Date miscalculation is the top employment-litigation malpractice — the solicitor must calculate and confirm the limitation date with a date calculator and verify against s.207B ERA 1996 before sending.
- Verify case law. Every authority is cited from memory and must be checked against a live source before the letter relies on it.
- Verify current statutory figures (compensatory cap, week's pay, Vento bands), which change annually.
- Send the letter. The solicitor reviews, completes, signs and serves.
- Advise on without-prejudice settlement strategy in the same document — that's the `without-prejudice-drafter` skill.
- Cover Scotland or Northern Ireland.
