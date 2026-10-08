---
name: ny-commercial-disputes-codearranger
title: New York Commercial Litigation
description: Use when drafting or filing a commercial-litigation action — breach of contract, fiduciary duty, business torts, fraud, account stated, UCC disputes, shareholder oppression, judicial dissolution. Triggers include '22 NYCRR 202.70 Commercial Division', 'CPLR 3016(b) fraud particularity', 'BCL 1104-a oppression', 'BCL 720 fiduciary duty', 'LLC Law 702 dissolution', 'Faithless Servant Doctrine', 'business divorce NY', 'judicial dissolution'. Covers **Commercial Division** at 22 NYCRR § 202.70 (separate procedural rule set, county-by-county thresholds, proportionality-in-discovery); BCL fiduciary duty and dissolution; Faithless Servant Doctrine; 9% pre-judgment interest under CPLR 5004; CPLR 3016(b) fraud-pleading particularity; and GOL §§ 5-1401 / 5-1402 choice-of-law / forum-selection ($250k/$1M thresholds make NY a destination forum).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-commercial-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# New York Commercial Litigation

> **NOT LEGAL ADVICE.** Commercial Division practice has
> rules that materially differ from general Supreme Court
> practice; verify the assigned Commercial Division Justice's
> Part Rules and the venue's Commercial Division threshold
> before filing.

## SOL catalog (the most-used)

| Claim | SOL | Citation |
|---|---|---|
| **Breach of contract (written or oral)** | **6 years** | CPLR 213(2) |
| **Breach of fiduciary duty** | **3 or 6 years** — depends on remedy sought (3 yr if damages; 6 yr if equitable / fraud-adjacent) | CPLR 214(4) / 213(7); *IDT Corp. v. Morgan Stanley* |
| **Fraud** | **6 years** (or 2 years from discovery, whichever is later) | CPLR 213(8) |
| **Account stated** | **6 years** (tracks the underlying contract) | CPLR 213(2) |
| **UCC Article 2 (sales) breach of warranty** | **4 years** | UCC § 2-725 |
| **UCC Article 3 negotiable instrument** | **6 years** | CPLR 213(2) / UCC § 3-118 |
| **Conversion** | **3 years** | CPLR 214(3) |
| **Tortious interference with K** | **3 years** | CPLR 214(4) |
| **Tortious interference with prospective economic advantage** | **3 years** | CPLR 214(4) |
| **Breach of fiduciary duty (in BCL § 720 derivative action)** | **6 years** | CPLR 213(7); BCL § 720 |
| **BCL § 1104-a oppression / judicial dissolution** | no SOL — equitable | BCL § 1104-a |

## The Commercial Division (22 NYCRR § 202.70)

The **Commercial Division** is a specialized Part within
Supreme Court Civil Term — a single Justice (or rotating
panel of designated Justices) hears commercial cases with
their own procedural rule set. **Different rules apply** to
Commercial Division cases than to regular Supreme Court
cases.

### County-by-county monetary thresholds

| County | Threshold |
|---|---|
| **New York County** | **$500,000** |
| **Westchester County** | **$200,000** |
| **Nassau County** | **$200,000** |
| **Queens / Kings / Bronx** | **$150,000** |
| **Erie / Suffolk** | **$100,000** |
| **Albany / Onondaga** | **$50,000** |
| **Monroe** | **$50,000** |

(Verify the current 22 NYCRR § 202.70(a) table before
filing — thresholds adjust periodically.)

### Subject-matter qualification (22 NYCRR § 202.70(b))

Commercial Division qualifying matters include (non-
exhaustive):

- Breach of contract / business dealings
- UCC transactions
- Transactions between commercial entities
- Joint venture / partnership disputes
- Internal-affairs disputes of business entities
- Breach of fiduciary duty by directors / officers
- Statutory shareholder oppression / dissolution
- Securities disputes (subject to federal preemption)
- Antitrust under NY Donnelly Act (Gen Bus Law § 340)
- Commercial real-property disputes (not residential L&T)

**Excluded** even if over the threshold: PI, wrongful death,
matrimonial, residential L&T, criminal, consumer-debt
collection.

### Commercial Division-specific rules

The Comm Div has its own rule set at 22 NYCRR § 202.70 with
**Appendix A** containing 36 specific rules. Highlights:

- **Rule 1 (Appearance by Designated Counsel)** — partner /
  designated attorney must appear at conferences
- **Rule 8 (Consultation Prior to Preliminary Conference)** —
  meet-and-confer on the scheduling order template
- **Rule 11-a (25-Question Interrogatory Cap)** — even more
  restrictive than CPLR 3130's 25-question default
- **Rule 11-c (Proportionality in Discovery)** — the
  proportionality test for ESI / document production
- **Rule 11-d (Privilege Logs)** — categorical privilege
  logs accepted instead of document-by-document
- **Rule 16 (Direct Testimony By Affidavit)** — bench-trial
  direct examination by affidavit
- **Rule 17 (Length of Papers)** — **25 pages** for memos
  of law (more than the 22 NYCRR § 202.8-b 10-page default
  in regular Supreme Court); **5 pages** for affirmations
  in support; **35 pages** for memos on dispositive motions
- **Rule 19 (Adjournments)** — strict adjournment policy
- **Rule 33 (Accelerated Adjudication)** — opt-in expedited
  procedure with discovery limits + early-trial scheduling

## Substantive frameworks

### CPLR 3016(b) — heightened fraud pleading

Fraud allegations must be pled with **particularity** under
CPLR 3016(b). The complaint must specify:

- The **specific misrepresentation** (precise words, date,
  speaker, audience)
- The **falsity** of the statement
- The **scienter** (knowledge of falsity or reckless
  disregard)
- The **reliance** (justifiable)
- The **damages** caused by reliance

A complaint that pleads fraud in general terms is subject
to dismissal under CPLR 3211(a)(7) for failure to state a
cause of action.

### BCL § 720 — derivative action for fiduciary breach

Shareholders may bring a **derivative action** on behalf of
the corporation against directors and officers for:

- Breach of fiduciary duty
- Self-dealing / conflict of interest
- Waste of corporate assets

Demand requirement: under *Marx v. Akers*, 88 N.Y.2d 189
(1996), the shareholder must either make a demand on the
board or plead demand-futility with particularity.

### BCL § 1104-a — judicial dissolution / shareholder oppression

Holders of 20%+ shares in a closely-held corporation can
petition for **judicial dissolution** on grounds of:

- **Illegal, fraudulent, or oppressive** actions toward the
  petitioner
- **Looting, wasting, or diverting** of corporate assets

The corporation can avoid dissolution by **electing to
purchase the petitioner's shares** at fair value under BCL
§ 1118 — a procedural escape valve used in many cases.

### LLC Law § 702 — LLC judicial dissolution

LLCs have an analogous dissolution remedy under LLC Law
§ 702 — judicial dissolution available when it is **"not
reasonably practicable"** to carry on the LLC business.
*Matter of 1545 Ocean Avenue LLC*, 72 A.D.3d 121 (2d Dep't
2010), is the leading interpretation.

### Faithless Servant Doctrine

NY recognizes the **Faithless Servant Doctrine** — an
employee who commits substantial disloyalty during
employment **forfeits all compensation** paid during the
period of disloyalty, even if some work was actually
performed. *Phansalkar v. Andersen Weinroth & Co.*, 344
F.3d 184 (2d Cir. 2003) is the key articulation.

### Pre-judgment interest (CPLR 5001 / 5004)

NY pre-judgment interest in contract cases is **9% per
annum** (CPLR 5004) — substantially higher than market
rates. The interest accrues from the date of breach. The
plaintiff in a long-running contract dispute may recover
substantial interest at trial.

For tort claims, pre-judgment interest runs from the date
the cause of action accrues (CPLR 5001(a)) — but is **not**
available for personal-injury pain-and-suffering damages.

## Choice of law + forum selection (GOL §§ 5-1401, 5-1402)

NY General Obligations Law makes NY especially friendly to
commercial parties choosing NY law / NY forum:

- **GOL § 5-1401**: a NY choice-of-law clause is enforceable
  in contracts involving **at least $250,000** even if the
  contract has no other NY contact
- **GOL § 5-1402**: a NY choice-of-forum clause is
  enforceable in contracts involving **at least $1,000,000**
  even if the parties have no other NY contact

These rules make NY a **destination forum** for sophisticated
commercial contracts — many M&A agreements, large financing
arrangements, and tech deals choose NY law and forum
specifically for the GOL §§ 5-1401 / 5-1402 enforceability.

## Account stated — debt-collection adjacent

In commercial-debt-collection actions, the **account stated**
doctrine is a major cause of action. The elements:

- Account rendered (typically by invoice or statement)
- Express or implied **acknowledgment** of the account by
  the debtor
- Failure to object within a **reasonable time** (silence
  may be acknowledgment)

The 6-year SOL under CPLR 213(2) governs. Default-judgment
practice in commercial collections often combines breach of
contract + account stated for redundant pleading.

## BCL § 624 — books-and-records inspection

Shareholders can compel a corporation to permit inspection
of books and records by **proper purpose** demand under BCL
§ 624. Common in lead-up to derivative actions or shareholder
oppression petitions.

## Composition with other ny- skills

- `ny-statewide-format` — caption + Notice of Motion format
- `ny-discovery` — CPLR Article 31; **Commercial Division
  proportionality rule + privilege log + interrogatory cap
  are stricter than general Supreme Court**
- `ny-first-30-days` — Answer + CPLR 3211(a) pre-answer
  motions
- `ny-deadlines` — SOL + 22 NYCRR § 202.8-b page limits
  (vs. Comm Div Rule 17 25/35-page rules)
- `ny-hearings` — motion practice and trial structure
- `ny-fact-check` — citation patterns (*Marx v. Akers*;
  *1545 Ocean Avenue*; *IDT Corp. v. Morgan Stanley*;
  *Reed, Roberts Associates*)
- `ny-nyco` (1st JD Comm Div $500k threshold), `ny-kings`
  ($150k threshold), `ny-bronx`, `ny-nassau` ($200k
  threshold), `ny-queens` ($150k threshold) — venue
  selection for Commercial Division
- `ny-pro-se` — pro se practice in Comm Div is rare due to
  the $50k-$500k thresholds + complexity

## High-yield commercial checks

1. **Commercial Division eligibility?** Monetary threshold
   + subject-matter qualification + statement at filing?
2. **CPLR 3016(b) particularity** met for fraud claims?
3. **CPLR 213(2) 6-year breach** vs **CPLR 213(8) 6/2-year
   fraud discovery rule**?
4. **GOL §§ 5-1401 / 5-1402** forum/choice-of-law for
   contract enforceability?
5. **BCL § 720** derivative-action demand requirement
   or demand-futility pleading?
6. **BCL § 1104-a / LLC § 702** dissolution petition with
   § 1118 buyout-election triage?
7. **Comm Div Appendix A** rule-set differences (25-page
   memo limit, proportionality, designated counsel,
   accelerated adjudication)?
8. **Pre-judgment interest 9%** under CPLR 5004 calculated
   from breach date?
9. **Faithless Servant Doctrine** applicable to a
   disloyal-employee fact pattern?

## Pro-se resources

Commercial Division pro se practice is uncommon — the
$50k-$500k thresholds plus the complexity of Comm Div Rules
mean most parties retain counsel. For solo / pro se inquiries:

- **NYS Bar Association Commercial and Federal Litigation
  Section** — referral
- **NYC Bar Lawyer Referral Service** — Commercial Division
  panel
- **Comm Div Justices' Part Rules** — published at
  `nycourts.gov/courts/comdiv/`
