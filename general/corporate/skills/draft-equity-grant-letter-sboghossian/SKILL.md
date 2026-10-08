---
name: draft-equity-grant-letter-sboghossian
title: Equity Grant Letter
description: Use when drafting an equity grant letter for employee stock options (ISO/NSO), RSUs, restricted stock, or SARs. Covers all required inputs, vesting schedule mechanics, acceleration (single vs. double trigger), type comparison table, post-termination exercise periods, tax notice obligations (83(b) election for US), and jurisdictional notes for UK EMI, France BSPCE/AGA, UAE, KSA, and DIFC/ADGM. Flags common pitfalls including missed 83(b) deadlines and ambiguous acceleration triggers.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-equity-grant-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Equity Grant Letter

## When to use this

An equity grant letter is the individual award document delivered to a grantee under a company equity plan (stock option plan, ESOP, EMI scheme, BSPCE, RSU plan, etc.). It sets out the specific terms of the grantee's individual award by reference to the plan and adds any grantee-specific terms.

Use this skill when:
- An employer is granting stock options, RSUs, or restricted stock to an employee or director as part of compensation.
- A startup is formalizing founder equity awards under a reverse-vesting structure.
- An M&A transaction triggers an acceleration review and replacement grant documentation is needed.
- An international company is issuing grants to employees in a MENA jurisdiction and needs to understand what modifications the local law requires.

The grant letter is not a standalone document — it operates by reference to the equity plan, which must exist before individual grants are made.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Grantee (full name, employee ID, role) | Identity of award recipient | — |
| Grant date | Start of vesting schedule; tax reporting date | Date of board approval |
| Grant size (number of shares / options / RSUs) | Core award quantum | — |
| Type (ISO / NSO / RSU / restricted stock / SAR) | Determines tax treatment and documentation requirements | — |
| Exercise / strike price (options only) | Must be at or above FMV on grant date to avoid adverse US tax; also relevant for other jurisdictions | FMV on grant date |
| Vesting schedule | Timeline for earning the award | 4-year / 1-year cliff (standard) |
| Cliff period | Period before any award vests | 12 months |
| Acceleration provisions | Vesting speed-up triggers | Double-trigger standard |
| Post-termination exercise period | How long after departure options can be exercised | 90 days (good leaver); 30 days (bad leaver) |
| Reference to equity plan | The plan governs; grant letter supplements | Company [Name] Stock Option Plan |

## Optional inputs
- 83(b) election notice (US only; for restricted stock; has 30-day deadline)
- RSU tax withholding instructions
- ROFR / co-sale rights applicable to vested shares
- Transfer restrictions cross-reference
- Drag-along rights cross-reference (from SHA)

## Type comparison

| Type | Who gets it | How it works | Key tax implication | When to use |
|---|---|---|---|---|
| **ISO** (US only) | US employees | Exercise option to buy shares at strike price | Tax-advantaged if holding periods met ($100K/year vest cap); no tax on exercise if AMT not applicable | US startup employees who are residents/employees |
| **NSO** | Employees, advisors, directors | Same exercise mechanic | Ordinary income on spread at exercise | Non-US employees; advisors; amounts above ISO cap |
| **RSU** | Employees | Shares delivered on vesting; no exercise | Ordinary income on vesting (FMV at vesting date); withholding required | Public companies; larger grants; simplicity preferred |
| **Restricted stock** | Founders, early employees | Shares issued now; forfeit unvested on departure | 83(b) election: pay tax now on FMV; no tax on vesting. No election: tax on FMV at vesting | Founders; very early hires where FMV is very low |
| **SAR** | Employees | Cash settlement of appreciation (share price minus strike) | Ordinary income at exercise | Where equity issuance is restricted; phantom equity |

## Document structure

### 1. Identification of grantor and grantee
Company name, grantee full name, role, and employee ID. Confirm the grantee is employed (or engaged as a service provider) by the company.

### 2. Reference to equity plan
> "This Grant Letter is subject to and incorporates the terms of the [Company Name] [Year] Equity Incentive Plan (the 'Plan'), a copy of which is attached as Exhibit A. In the event of any conflict, the Plan shall prevail."

### 3. Grant details table
| Item | Value |
|---|---|
| Grant type | ISO / NSO / RSU / Restricted Stock |
| Grant date | [Date] |
| Number of shares/options | [Number] |
| Exercise price (options) | $[Amount] per share |
| Vesting start date | [Date] (often same as grant date or employment start) |
| Vesting schedule | See Section 4 |
| Expiration date (options) | [Date] (typically 10 years from grant date) |

### 4. Vesting schedule
Standard: 25% vests after 12-month cliff, then 1/48 per month for the following 36 months.

**Cliff:** The cliff is the initial period during which no shares vest. If the grantee departs before the cliff, 0% of the grant has vested. After the cliff, the cliff tranche (typically 25%) vests in full on the cliff date.

State explicitly: "No shares shall be vested until the first anniversary of the Vesting Commencement Date (the 'Cliff Date'). On the Cliff Date, [25%] of the Total Grant shall vest. Thereafter, an additional [1/48th] of the Total Grant shall vest on each monthly anniversary of the Cliff Date, such that the Total Grant shall be fully vested on the fourth anniversary of the Vesting Commencement Date."

### 5. Acceleration provisions
Two models:

**Single trigger** (on change of control):
> "In the event of a Change of Control, [50% / 100%] of the then-unvested portion of this Grant shall vest immediately on closing of the Change of Control."

**Double trigger** (more common for employees; requires two events):
> "If, within 12 months following a Change of Control, the Grantee is Involuntarily Terminated Without Cause or resigns for Good Reason, 100% of the then-unvested portion of this Grant shall vest immediately on such termination."

Define "Change of Control", "Involuntary Termination Without Cause", and "Good Reason" precisely in the Plan or in the grant letter's definitions section.

Double trigger is preferred by investors and boards; single trigger can inflate dilution on acquisition and is disfavoured in VC-backed companies.

### 6. Post-termination exercise period
Critical: if an option holder departs and does not exercise within this window, the options expire worthless.

| Departure type | Standard period |
|---|---|
| Voluntary resignation (good leaver) | 90 days after last day of service |
| Termination without cause | 90 days after last day of service |
| Termination with cause (bad leaver) | 30 days or forfeiture on termination |
| Death or disability | 12 months |
| ISO to NSO conversion | Options held beyond 3 months after departure become NSOs (US tax rule) |

Advise grantees at departure: the post-termination window must be tracked; many departing employees lose their options by failing to exercise in time.

### 7. Good leaver / bad leaver treatment (for restricted stock and ESOP)
Define these terms with precision:

**Good leaver**: Termination without cause; resignation for good reason; death; disability; retirement above age threshold. Vested shares kept; unvested shares forfeited at FMV (for restricted stock) or lapse (for options).

**Bad leaver**: Termination for cause; voluntary resignation before cliff; material breach; non-compete violation. Vested shares may be repurchased at par or cost (below FMV in some structures); unvested shares forfeited without payment.

### 8. Tax notice
**US (83(b) election):**
> "If this award is of restricted stock or otherwise subject to a risk of forfeiture, Grantee may file an 83(b) election with the IRS within **30 days** of the Grant Date to include in gross income the FMV of the restricted stock at grant, rather than at vesting. This election deadline is strictly enforced; failure to file within 30 days is irrevocable. Consult your tax advisor before the deadline."

For ISO grants:
> "This Option is intended to qualify as an Incentive Stock Option under Section 422 of the US Internal Revenue Code, subject to the $100,000 ISO limitation per calendar year. You should consult a tax advisor regarding the tax consequences of exercising this Option."

### 9. Transfer restrictions
Vested shares are typically subject to:
- Right of first refusal (ROFR) in favour of the Company on any proposed transfer.
- Co-sale rights (tag-along) per the Shareholders' Agreement.
- Lock-up on IPO.

Include cross-reference to applicable SHA provisions.

### 10. Dispute resolution
Typically arbitration, consistent with the employment agreement and company equity plan.

### 11. Acknowledgment and signature
Grantee must sign acknowledging receipt, understanding of the vesting schedule, tax notice, and plan terms. Keep countersigned copy in personnel file.

## Jurisdictional notes

### UK — EMI (Enterprise Management Incentives)
- Tax-advantaged option scheme for qualifying SMEs (gross assets ≤ £30M; certain excluded activities).
- EMI options: no income tax on grant; CGT (not income tax) on exercise if shares held 2+ years after grant.
- Require HMRC notification within 92 days of grant.
- Option agreement must comply with EMI requirements; strike price at HMRC-agreed AMV.

### France — BSPCE and AGA (Free Shares)
- **BSPCE** (Bons de Souscription de Parts de Créateur d'Entreprise): tax-advantaged warrants for qualifying young companies; strict eligibility criteria; favorable CGT rate on gains.
- **AGA** (Attribution Gratuite d'Actions): free share grants; subject to 1-year minimum holding period; favorable tax on gains after 2-year holding; employer social charges apply.
- Both require extraordinary general assembly authorization; strict procedural requirements.
- Options not as common in France as BSPCE/AGA; if used, they are BSA (Bons de Souscription d'Actions).

### UAE
- No individual income tax; options and RSUs generate no personal income tax liability on vesting or exercise.
- Options can be issued from an offshore entity (Cayman or DIFC holding company) with UAE subsidiary employees as grantees.
- DIFC / ADGM entities: full English-law conventions; DIFC Companies Law and ADGM Companies Regulations accommodate standard option pool mechanics.
- Consider UAE residency visa implications: if option gain is repatriated, UAE source rules may be relevant for the grantee's home country tax.

### KSA
- No individual income tax for most employees.
- Equity participation is emerging in practice; sukuk-linked equity hybrids exist for Sharia compliance.
- For Saudi-listed companies, CAMA (Capital Market Authority) regulations govern equity compensation plans.
- Consider Sharia compliance analysis for equity instruments that include interest-bearing components or speculative pay structures.

### DIFC / ADGM
- Full common-law framework; English market-standard option documentation applicable.
- DIFC Employment Law 4/2021 does not restrict equity compensation structure.
- ADGM Employment Regulations 2024 similarly accommodating.

## Common pitfalls

1. **Missing 83(b) election deadline** (US): 30 days from grant date; strictly enforced by IRS; no exceptions. If the grantee does not file in time and the restricted stock is ultimately worth more than its FMV at grant, the grantee pays ordinary income tax on the full spread at vesting — often a very large and unexpected tax bill.

2. **Vesting acceleration ambiguity**: if the acceleration clause says "vest on a change of control" without specifying whether unvested shares vest 100% or pro-rata, the parties will fight about it. Be precise.

3. **Strike price below FMV at grant** (US ISOs): a below-FMV strike price means the option is "in the money" at grant; ISOs granted in-the-money do not qualify for ISO tax treatment. Get a proper 409A valuation before granting.

4. **Post-termination window too short**: a 30-day post-termination exercise window for ISOs is particularly damaging because departing employees rarely have the liquidity to exercise options in 30 days. Consider 6–12 months for senior employees.

5. **Single trigger acceleration without board discussion**: single-trigger acceleration is expensive for acquirers (they are acquiring already-vested employees who can leave immediately); most VCs push for double-trigger. Discuss with board and existing investors before granting.

6. **No tax notice for UK / France**: failing to file HMRC EMI notification within 92 days disqualifies the option as EMI; failing to obtain AGM authorization for French BSPCE/AGA invalidates the grants.

## Related skills

- [[draft-founders-agreement]] — founders' equity arrangements using reverse vesting
- [[draft-shareholders-agreement]] — ROFR and tag-along rights applicable to vested shares
- [[draft-vesting-schedule]] — standalone vesting schedule document for option plans
- [[review-cap-table]] — reviewing the cap table post-grant for dilution analysis
- [[draft-safe]] — convertible instruments as an alternative to upfront equity
