---
name: prompt-pack-motion-for-summary-judgment-sboghossian
title: Motion for Summary Judgment
description: Use when drafting a motion for summary judgment (or equivalent dispositive motion) arguing that there is no genuine dispute of material fact and the moving party is entitled to judgment as a matter of law. Covers the standard for summary judgment, statement of undisputed facts, legal argument, and relief requested. Applicable primarily to common-law litigation in DIFC, ADGM, UK, and US courts; includes notes on analogous mechanisms in civil-law MENA jurisdictions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-motion-for-summary-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Motion for Summary Judgment

## When to use this

Use this skill when a party seeks to dispose of all or part of a case before trial by demonstrating that the undisputed facts, together with the applicable law, compel judgment in the moving party's favor. Summary judgment (or summary disposal) avoids the cost and risk of trial on issues where no real factual dispute exists.

**Jurisdictional availability**: Summary judgment is a common-law mechanism (US federal Rule 56, English CPR Part 24, DIFC Court Rules, ADGM Court Rules). UAE onshore courts, KSA courts, and other civil-law MENA courts do not have an identical procedure, but may entertain early dismissal applications or demurrers in analogous circumstances — note this prominently and route to local counsel for civil-law courts.

Triggers:
- "Draft a motion for summary judgment in [case] arguing no genuine issue of material fact on [claim/defense]."
- "Write a Rule 56 motion arguing that the statute of limitations bars the plaintiff's claims."
- "File for summary judgment on liability in the [case] — all facts are established."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Case name and court / case number | Identifies the proceeding | Ask user |
| Movant (the party filing) | Determines framing — claimant seeking affirmative SJ or defendant seeking dismissal | Ask user |
| Claims or defenses at issue | Scopes the motion to specific issues | Ask user — be precise |
| Undisputed material facts | Core substance of the motion; must be supported by record evidence | Ask user |
| Legal basis | The rule, statute, or binding authority that entitles movant to judgment | Ask user |
| Record evidence available | Exhibits cited in support (affidavits, contracts, documentary evidence) | Ask user |

## Optional inputs

- Prior court orders relevant to the issues raised
- Key opposing arguments to be preemptively addressed
- Required format / page limits per court rules
- Whether partial summary judgment is sought (on liability only, or on specific claims/defenses)

## Motion structure

### Cover Page and Caption
Court name, case name, case number, motion title ("Defendant [Name]'s Motion for Summary Judgment" or "Claimant [Name]'s Motion for Summary Judgment on Liability").

### Introduction (1–2 pages)
Open with the strongest framing of why summary judgment is warranted: "This Court should grant summary judgment because [core argument in one paragraph]. The undisputed record evidence establishes [key facts], and applicable law is clear that [legal conclusion]. No trial is necessary."

State the relief requested upfront.

### Standard for Summary Judgment
Set out the applicable standard for the court:
- **DIFC Court**: Under Rule 24.2 of the DIFC Court Rules, the Court may give summary judgment on a claim or issue if a party has no real prospect of succeeding on the claim/defense and there is no other compelling reason why the case should go to trial.
- **ADGM Court**: Analogous provisions under ADGM Court Procedure Rules.
- **English Court (CPR Part 24)**: Standard is whether the respondent has a real prospect of success on the claim or defense; identical formulation.
- **US Federal Courts (Rule 56)**: Summary judgment is appropriate where "there is no genuine dispute as to any material fact and the movant is entitled to judgment as a matter of law." Fed. R. Civ. P. 56(a).

State the standard precisely for the applicable court.

### Statement of Undisputed Material Facts
This section is critical. Present the facts supporting the motion in numbered paragraphs, each supported by a specific cite to the record evidence (exhibit number, deposition transcript page, document reference).

Format:
> 1. On [date], the parties entered into the [Agreement]. (Ex. 1, Agreement, at p. 1.)
> 2. Under Clause X of the Agreement, Respondent was obligated to [obligation]. (Ex. 1, Clause X.)
> 3. On [date], Respondent failed to [perform obligation]. (Ex. 2, Correspondence from Respondent.)
> 4. Claimant suffered damages of [amount] as a result. (Ex. 3, Financial Analysis.)

Each fact must be genuinely undisputed (supported by record evidence that the opposing party cannot reasonably dispute). Do not include facts that are contested — those go to trial.

### Legal Argument

#### I. [First Ground for Summary Judgment]

**State the legal standard for the claim or defense at issue.**
Example: "Under [governing law], a claim for breach of contract requires: (1) a valid contract; (2) Claimant's performance or excuse for non-performance; (3) Respondent's breach; and (4) resulting damages."

**Apply the standard to the undisputed facts.**
Cite the undisputed facts established above; explain why each element of the claim/defense is established or fatally absent. Keep the argument tight — cite to the fact statement by paragraph number rather than repeating facts.

**Address the anticipated counter-argument.**
Anticipate the opposing party's best argument and explain why it fails as a matter of law: "Respondent may argue that [X]. However, [legal rule / undisputed fact] forecloses this argument because [reason]."

#### II. [Second Ground, if applicable]
Repeat the structure: legal standard → application to undisputed facts → rebuttal of counter-argument.

#### III. There Is No Genuine Dispute of Material Fact
If not already covered in the grounds section, close with a summary paragraph explaining why there is no triable factual issue:
- "The record is unequivocal on all material facts. Respondent's only potential argument goes to [peripheral issue], which is immaterial because [reason]."

### Conclusion and Relief Requested
Request the specific relief:
- "For the foregoing reasons, [Movant] respectfully requests that this Court grant summary judgment in [Movant's] favor on [specific claims / all claims] and enter judgment [dismissing Respondent's claims / awarding Claimant the following relief: ...]."

### Supporting Documents (exhibits)
- Witness statements / affidavits authenticating each exhibit
- Exhibits: contracts, correspondence, financial evidence, prior orders
- Comply with court rules for exhibit formatting and filing

## Jurisdictional / court-specific notes

| Jurisdiction | Key procedural points |
|---|---|
| **DIFC Court** | Applications for summary disposal under Practice Direction No. 2; typically heard on papers unless court directs a hearing; respondent has 14 days to file a response; court may summarily dismiss unmeritorious defenses. |
| **ADGM Court** | Expedited determination available; less developed case law on summary judgment than DIFC; consult most recent practice directions. |
| **UK (CPR Part 24)** | Widely used; standard is "real prospect of success" / "no other compelling reason"; summary judgment can be granted on a limited issue even if the case proceeds to trial on others. |
| **US Federal (Rule 56)** | "No genuine dispute of material fact" standard; celotex / Anderson / Matsushita trilogy sets the framework; non-movant must demonstrate specific facts creating a triable issue. |
| **UAE onshore courts** | No direct equivalent; requests for preliminary dismissal are less structured; consult local counsel on early dismissal applications under UAE Civil Procedure Law. |
| **KSA courts** | No direct equivalent; early motion practice is limited; consult Saudi lawyer on applicable procedures. |

**Important**: Do not file a summary judgment motion in a civil-law court where the mechanism does not exist. An unsuccessful motion in a court that does not recognize the procedure may prejudice the movant or draw sanctions.

## Common mistakes

- **Relying on disputed facts**: a summary judgment motion stands or falls on whether the material facts are genuinely undisputed; including a contested fact as "undisputed" exposes the motion to denial.
- **Neglecting the record support**: every fact in the statement of undisputed facts must be tied to a specific exhibit or citation; unsupported assertions will be struck.
- **Failure to address the standard for the specific court**: the threshold ("no real prospect" vs "no genuine dispute") and procedural rules differ; using the wrong standard in the brief weakens the motion.
- **Overreaching on scope**: a motion seeking summary judgment on all claims when only one is clearly dispositive invites denial; a partial motion on the strongest ground is strategically superior.

## Related skills

- [[prompt-pack-post-hearing-brief]]
- [[prompt-pack-legal-opinion-on-dispute]]
- [[prompt-pack-litigation-hold-notice]]
- [[heuristic-always-state-jurisdiction-first]]
