---
name: motion-to-avoid-lien
title: Motion to Avoid Lien Under 11 U.S.C. § 522(f)
description: Drafts a Motion to Avoid Lien under 11 U.S.C. § 522(f) for bankruptcy proceedings. Produces a litigation-ready motion with caption, impairment calculations, legal argument, and prayer for relief. Use when filing lien avoidance motions in Chapter 7, 11, or 13 cases, stripping judicial liens or nonpossessory nonpurchase-money security interests that impair debtor exemptions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/motion-to-avoid-lien
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
---

# Motion to Avoid Lien Under 11 U.S.C. § 522(f)

Drafts a motion to avoid a lien impairing a debtor's exemptions, with statutory analysis and impairment calculation.

## Prerequisites

Gather before drafting:

1. **Case info** — case number, chapter (7/11/13), filing date, court district/division, assigned judge
2. **Property** — description (legal description or address), type (real/personal), current FMV, appraisals
3. **Lien** — lienholder name, type (judicial or nonpossessory NPMSI), originating judgment/agreement, recording date, amount
4. **Senior encumbrances** — all liens senior to challenged lien with amounts
5. **Exemption** — specific state or federal statute, dollar amount claimed per Schedule C
6. **Local rules** — formatting, notice periods, hearing requirements

## Output Structure

### 1. Caption

Include: full court name with district/division, case number, chapter, debtor name (as on petition), motion title, judge (if local rules require). Format per local rules.

### 2. Introduction

One to two paragraphs identifying: moving party, specific lien and lienholder, property subject to lien, statutory basis (§ 522(f)(1) for judicial liens or § 522(f)(2) for nonpossessory NPMSI), and core premise of exemption impairment.

### 3. Factual Background

Present chronologically: filing date/chapter, property description and FMV, lien origin and attachment, claimed exemption with statute and Schedule C amount, then the impairment calculation:

```
  Lien to be avoided:                    $________
+ All other liens on property:           $________
+ Debtor's claimed exemption:            $________
= Total:                                 $________
- Fair market value of property:         $________
= Impairment amount:                     $________
```

If Total exceeds FMV, the lien impairs the exemption per § 522(f)(2)(A).

### 4. Legal Argument

**Judicial liens — § 522(f)(1).** Establish three elements:

| Element | Standard |
|---------|----------|
| Judicial lien | Meets § 101(36) — obtained by judgment, levy, sequestration, or other legal/equitable process |
| Impairment | (Lien + all other liens + exemption) exceeds FMV per § 522(f)(2)(A) |
| Valid exemption | Debtor entitled under § 522(b) |

**Nonpossessory NPMSI — § 522(f)(2).** Lien must encumber: household goods/furnishings/appliances/jewelry for personal use, tools of the trade, or professionally prescribed health aids.

Cite binding circuit and district precedent. Address likely counterarguments on exemption validity, valuation, or lien classification.

### 5. Prayer for Relief

Request: (1) avoid the lien entirely or to extent of impairment, (2) declare lien void, (3) other just relief, (4) expedited consideration if appropriate.

### 6. Exhibits

- [ ] Judgment or security agreement creating the lien
- [ ] Evidence of lien recording/perfection
- [ ] Debtor's Schedule C
- [ ] Property appraisal or valuation evidence
- [ ] Debtor's declaration/affidavit (if applicable)

### 7. Certificate of Service

Serve on lienholder, trustee, and all parties in interest per local rules. Specify method (ECF/mail/personal), date, and addresses. Comply with FRBP 7004, 9014, and local rules. Sign with bar number or pro se contact information.

## Pitfalls

- **Math errors** — courts reject motions with incorrect impairment calculations; double-check arithmetic
- **Unclaimed exemption** — confirm the exemption is on Schedule C before filing; amend schedules first if not
- **Opt-out states** — verify whether jurisdiction uses state or federal exemptions; this determines which statute to cite
- **Partial impairment** — specify exact dollar amount avoided vs. amount surviving
- **Citations** — Bluebook format; mark unverified citations with [VERIFY]
- **Local rules** — formatting (margins, font, spacing, page limits) and notice periods vary by district
- **Schedule consistency** — motion facts must match bankruptcy schedules
