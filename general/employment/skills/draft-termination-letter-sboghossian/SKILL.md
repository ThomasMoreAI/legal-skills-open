---
name: draft-termination-letter-sboghossian
title: Termination Letter
description: Use when drafting an employment termination letter — the formal notice document that initiates the end of an employment relationship. Covers terminations for cause, without cause, mutual agreement, and fixed-term non-renewals. Provides jurisdiction-aware statutory references for UAE (Decree-Law 33/2021), KSA (Article 80), Lebanon (Labor Code Articles 50 and 74), and DIFC, including the requirement to itemize final settlement, the visa-cancellation coordination obligation for MENA non-citizen employees, and the critical rule against characterizing misconduct beyond what is documented.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-termination-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: employment
language: en
---

# Termination Letter

The termination letter is the formal legal notice that ends the employment relationship. It triggers the running of notice periods, the calculation of final entitlements, and the start of the visa-cancellation window in MENA. In "for cause" cases, it must accurately characterize the grounds without overreaching — a defamatory or unsupported characterization of misconduct creates a separate claim. In "without cause" cases, it should state the basis neutrally (operational redundancy, restructuring) without implied wrongdoing.

## When to use this

- Terminating an employee for cause (documented misconduct, performance, serious breach)
- Terminating an employee without cause (redundancy, restructuring, role elimination)
- Mutual-agreement separation (use alongside [[draft-severance-agreement]])
- Non-renewal of a fixed-term contract
- Confirming a constructive dismissal resignation and the employer's position

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Employer full legal name + signatory | The party issuing the notice | Must provide |
| Employee full name + title + employee ID | Precise identification | Must provide |
| Effective termination date | Last day of employment; triggers all calculations | Must specify — not "immediately" unless dismissal for serious cause |
| Grounds for termination | For cause: specific factual basis; without cause: operational reason | Must provide; see jurisdictional notes on valid grounds |
| Notice period or pay in lieu | Based on contract or statutory minimum, whichever is higher | Must specify |
| Final settlement itemization | Salary owed; untaken leave; EOSG/EOSA; ex gratia (if any) | Must itemize |
| Restrictive covenant reminder | If employment contract contains post-termination restrictions | Remind; do not impose new ones in the letter |
| Property return | What property must be returned and by when | Last day of employment |

## Optional inputs

- Reference letter terms (if agreed as part of the separation)
- Non-disparagement (if agreed as part of the separation)
- Confidentiality continuation reminder (ongoing obligations)
- Cooperation obligation for transition

## Document Structure

### Standard Termination Letter Format

```
[Company Letterhead]

[Date]

[Employee Full Name]
[Address / via email to registered address]

Subject: Notice of Termination of Employment — [Employee Name]

Dear [Mr./Ms./Name],

[SECTION 1 — FORMAL NOTICE]
This letter constitutes formal notice of the termination of your employment
with [Employer Legal Name] ("the Company"), effective [Date] ("Termination
Date").

[For cause — specific and factual:]
Your employment is being terminated for cause. Specifically, [precise factual
description of the conduct or performance failures — dates, incidents,
references to prior warnings]. This conduct constitutes [cite specific policy
or contract clause violated]. [Cite statutory basis: e.g., "pursuant to
Article 80 of the KSA Labor Law / Article 44 of UAE Decree-Law 33/2021 /
Article 74 of the Lebanese Labor Code"].

[Without cause — neutral:]
This termination is effected without cause due to [restructuring of the
Company's operations / elimination of your role as part of an organizational
reorganization / operational requirements that have resulted in the elimination
of your position]. This decision does not reflect on your personal performance.

[SECTION 2 — NOTICE PERIOD]
Your contractual / statutory notice period is [X days/months]. 
[Choose one:]
- Your last day of work will be [Date]. You are [required to / released from
  the obligation to] work during this notice period.
- In lieu of notice, the Company will pay you [Amount] representing [X months]
  salary in lieu of notice, to be included in your final settlement.

[SECTION 3 — FINAL SETTLEMENT ITEMIZATION]
Your final settlement will be calculated as follows:

  Item                                      Amount
  ─────────────────────────────────────     ────────
  Salary owed to Termination Date           [Amount]
  Accrued untaken annual leave              [X days × daily rate = Amount]
  End-of-service gratuity (EOSG/EOSA)       [Calculation basis]
  Notice pay (if pay in lieu)               [Amount]
  Other accrued benefits                    [Amount if any]
  Ex gratia (if applicable)                 [Amount]
  ─────────────────────────────────────     ────────
  Total                                     [Amount]

  Less any outstanding recoveries:
  Salary advances                           [Amount]
  Other deductions                          [Amount]
  ─────────────────────────────────────     ────────
  Net payable to you                        [Amount]

Payment will be made to your [designated bank account] within [X] days of
your Termination Date / within the period required by law.

[SECTION 4 — RETURN OF COMPANY PROPERTY]
Please return all company property, including [laptop, access cards, mobile
device, confidential documents, keys], by no later than [Date / your last
working day].

[SECTION 5 — ONGOING OBLIGATIONS]
Your post-employment obligations under [your employment contract / company
policy] continue to apply, including [confidentiality, non-compete for X
period, non-solicitation of clients and employees for X period].

[SECTION 6 — VISA / RESIDENCY PERMIT]
[For MENA non-citizen employees:]
The Company will initiate the cancellation of your work permit and residency
visa within [X] days of your Termination Date. Please cooperate with this
process. You are required to depart the country / transfer your visa to a
new sponsor within the period specified by [UAE MOHRE / Saudi MOL / applicable
authority].

[SECTION 7 — ACKNOWLEDGMENT (OPTIONAL)]
Please sign and return a copy of this letter as acknowledgment of receipt.
Your acknowledgment of receipt does not constitute agreement to the terms.

Yours sincerely,

[Authorized Signatory Name]
[Title]
[Company]
```

## Jurisdictional Notes

### UAE Federal (Decree-Law 33/2021)
- **For cause (Article 44)**: Exhaustive list of valid grounds for immediate dismissal without notice or EOSG. Grounds include: impersonation, causing financial loss to the employer, repeated failure to perform duties after warnings, physical assault, serious moral breach, disclosure of trade secrets, being found in the workplace intoxicated, committing an offense injuring the employer's honor or trust.
- **Without cause**: "Arbitrary dismissal" (فسخ تعسفي) — employer must prove a legitimate reason or pay compensation in addition to EOSG (courts can award up to 3 months' additional compensation)
- **Procedural requirement**: employer must give written notice; for documented cause cases, employer should have issued at least one written warning prior to dismissal (except for the most serious misconduct)
- **MoHRE notification**: employer must notify the Ministry of Human Resources and Emiratisation of the termination; non-citizen employees' work permits must be cancelled through MoHRE TASHEEL system

### DIFC (DIFC Employment Law)
- For cause (Article 32): employer may summarily dismiss for "serious misconduct" — conduct that is sufficiently serious to justify immediate termination without notice; the DIFC courts apply a reasonableness standard similar to English unfair dismissal principles
- Arbitrary dismissal exposes the employer to compensation under Article 33
- Minimum notice (Article 35): 30 days for <3 years' service; 60 days for ≥3 years
- DEWS/EOSG: even summary dismissal for cause does not forfeit accrued DEWS/EOSG entitlement for periods of service before the misconduct

### KSA (Labor Law)
- **Article 80 — for cause termination**: employer may dismiss without notice or EOSA only for specific grounds: false identity, deliberate damage, physical assault, absence without excuse for 20 days in one year or 10 consecutive days, final court conviction for a crime/misdemeanor involving dishonor, failure to comply with safety instructions after warning, incitement to disorder, and several others
- **Arbitrary dismissal**: courts award compensation typically equivalent to 2–12 months of salary; Ministry of Human Resources can mediate
- **Procedural requirements**: written investigation (investigation report) before dismissal for cause; documented warnings for performance cases; employee has right to respond

### Lebanon (Labor Code)
- **Article 74 — dismissal without cause**: employer may dismiss a permanent employee with notice; employee receives end-of-service indemnity under Article 50
- **Article 73 — dismissal for cause**: specific valid grounds (criminal conviction, serious misconduct); only these grounds justify summary dismissal without indemnity
- **Protective indemnity (Article 74)**: if dismissal is arbitrary (without valid grounds or disproportionate), the Labor Court may award up to one year's salary as additional damages
- **Warning requirement (Article 75)**: for certain types of misconduct (particularly performance-related), a written warning must be issued before dismissal

### France
- **Entretien préalable**: employer must convene a pre-dismissal meeting (entretien préalable au licenciement) before issuing any dismissal letter; minimum 5 business days' notice of the meeting; dismissal letter may only be sent 2 business days after the meeting
- **Lettre de licenciement**: must state precise, real, and serious grounds (cause réelle et sérieuse); vague grounds = dismissal without real and serious cause (licenciement sans cause réelle et sérieuse)
- **Notification**: sent by registered mail (lettre recommandée avec accusé de réception)

## Critical Drafting Rules

### Do not characterize misconduct beyond what is documented
The termination letter is not the place to make findings of fact about misconduct that have not been established through a proper disciplinary process. Statements like "your dishonest behavior" or "your fraudulent conduct" without documented evidence create defamation exposure. Stick to factual descriptions: "On [date], you [specific act described]."

### Statutory minimums cannot be waived by characterizing a termination as "for cause"
Even where there is valid cause for termination, employees in most MENA jurisdictions retain statutory entitlements (accrued leave, salary owed to the termination date). In UAE, an employee terminated for cause may lose their EOSG entitlement, but they retain their accrued leave and salary owed. In KSA, Article 80 terminations lose EOSA only if the specific Article 80 grounds apply.

### Mass redundancies require additional procedures
Collective dismissals (typically defined by headcount thresholds, e.g., UAE: 5% or more of workforce simultaneously) may require advance notification to the Ministry of Human Resources and Emiratisation, a consultation period, and a redeployment assessment before individual terminations can proceed.

### Sponsor cancellation for non-citizens (UAE and KSA)
The employer is the residency sponsor for expatriate employees in UAE and KSA. The letter should initiate or reference the visa/work permit cancellation process. Delays in cancellation result in fines. The employee must either transfer their visa to a new sponsor or depart the country within the grace period (UAE: 30 days after work permit cancellation; KSA: 30 days after residency permit expiry). Coordinate HR and legal to ensure cancellation is completed on time.

## Common Mistakes

- **No factual basis for cause dismissal** — "poor performance" without documentation of targets, reviews, and warnings; courts reverse these
- **Wrong effective date** — using the letter date as the termination date when the statutory notice period has not been served
- **Omitting EOSG/EOSA from the final settlement** — employers sometimes omit these assuming "for cause" means no EOSG; check jurisdiction-specific rules
- **Failing to give the entretien préalable (France)** — procedural flaw renders the dismissal procedurally flawed (licenciement irrégulier) even if the grounds are substantively valid
- **Letter written in English for a KSA national employee** — while not legally void, presenting a termination letter in a language the employee may not understand creates procedural risk; use Arabic for KSA and LB-based employees

## Related skills

- [[draft-severance-agreement]]
- [[draft-warning-letter]]
- [[draft-employment-contract]]
- [[kb-employment-law-mena]]
