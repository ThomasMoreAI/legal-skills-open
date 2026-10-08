---
name: wa-commercial-disputes-codearranger
title: Washington Commercial Disputes — Subject-Matter Bundle
description: Use when handling a Washington commercial-disputes matter — breach of contract (common law + UCC sales), Washington CPA (RCW 19.86) as the unfair-competition statute with Hangman Ridge 5-element test and treble damages, Business Corporation Act (RCW 23B) covering shareholder/director duties and judicial dissolution, LLC Act (RCW 25.15), partnership (RCW 25.05), UCC (RCW 62A), Mandatory Arbitration of Civil Actions (RCW 7.06), and statute of frauds (RCW 19.36). Triggers include "commercial dispute", "breach of contract", "CPA", "Hangman Ridge", "dissolution corporation", "dissenter's rights", "judicial dissolution", "MAR", "UCC".
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-commercial-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
---

# Washington Commercial Disputes — Subject-Matter Bundle

> **NOT LEGAL ADVICE.** Commercial-law statutes have been
> amended over time (notably the 2009 WBCA amendments and
> the 2016 LLC Act overhaul). This skill names the
> controlling chapters and describes doctrinal
> frameworks; **current treble-damages cap, MAR
> jurisdictional cap, SOL day counts, and section-level
> rules live in the references corpus** at `wa-law-
> references/references/wa-rcw-debt/`.

## At a glance

- **Contracts**: common law + UCC sales (RCW 62A.2);
  statute of frauds at RCW 19.36 + UCC at RCW 62A.2-201
- **Business entities**: WBCA at RCW 23B, LLC Act at RCW
  25.15, partnership at RCW 25.05
- **UCC**: codified at RCW 62A (Articles 1, 2, 3, 4, 7,
  8, 9A — Article 6 bulk transfers repealed nationally)
- **CPA**: RCW 19.86 — Washington's combined antitrust +
  consumer-protection statute (despite the name, covers
  B2B disputes); treble damages + mandatory fees
- **MAR**: RCW 7.06 — Mandatory Arbitration of Civil
  Actions for cases below a jurisdictional cap in
  participating counties

## Chapter pointers

| Topic | Chapter | Reference file |
|---|---|---|
| Contracts (statute of frauds) | RCW 19.36 | `RCW-19_36.md` |
| Washington CPA (RCW 19.86) | RCW 19.86 | `RCW-19_86.md` |
| Business corporations (WBCA) — shareholders | RCW 23B.06 | `RCW-23B_06.md` |
| WBCA — directors and officers | RCW 23B.08 | `RCW-23B_08.md` |
| WBCA — dissenters' rights | RCW 23B.13 | `RCW-23B_13.md` |
| WBCA — dissolution | RCW 23B.14 | `RCW-23B_14.md` |
| Partnership (Revised UPA) | RCW 25.05 | `RCW-25_05.md` |
| Limited liability companies | RCW 25.15 | `RCW-25_15.md` |
| UCC — General Provisions | RCW 62A.1 | `RCW-62A_1.md` |
| UCC — Sales | RCW 62A.2 | `RCW-62A_2.md` |
| UCC — Negotiable Instruments | RCW 62A.3 | `RCW-62A_3.md` |
| UCC — Bank Deposits | RCW 62A.4 | `RCW-62A_4.md` |
| UCC — Documents of Title | RCW 62A.7 | `RCW-62A_7.md` |
| UCC — Investment Securities | RCW 62A.8 | `RCW-62A_8.md` |
| UCC — Secured Transactions | RCW 62A.9A | `RCW-62A_9A.md` |
| MAR | RCW 7.06 | `RCW-7_06.md` |

For the CPA treble-damages cap, the SOL on each cause of
action, the MAR jurisdictional cap, and section-level
rules, **read the relevant chapter file**.

## Washington CPA — doctrinal framework

The CPA at RCW 19.86 is Washington's flagship unfair-
competition + deceptive-act statute. Modeled on the FTC
Act. Covers B2B disputes as well as consumer disputes.

### Hangman Ridge 5-element test

*Hangman Ridge Training Stables v. Safeco Title Ins. Co.*,
105 Wn.2d 778 (1986), sets the controlling test for a
private CPA claim:

1. Unfair or deceptive act or practice
2. Occurring in trade or commerce
3. Public interest impact
4. Injury to plaintiff's business or property
5. Causation linking act to injury

### Damages

- Actual damages
- Treble damages up to a statutory cap (court's
  discretion)
- Mandatory attorney's fees + costs for prevailing
  plaintiff (no fee for prevailing defendant)
- Equitable relief — injunction, restitution

For the current treble-damages cap, see `RCW-19_86.md`.

### Insurance bad-faith CPA

A unique Washington feature: first-party bad-faith
insurance claims are explicitly CPA claims per *Coventry
Assocs. v. Am. States Ins. Co.* Insurer violation of
WAC 284-30 unfair-claims-handling regs = per se CPA
violation (per *Industrial Indem. Co. of the Nw. v.
Kallevig*).

### SOL

CPA SOL runs longer than the general tort 3-year SOL.
Day-count in `RCW-19_86.md`.

## Breach of contract — doctrinal framework

### Elements

Existence of a valid contract; breach; damages caused by
breach.

### SOL nuances

Different SOL day counts for:
- Written contract
- Oral contract
- UCC Article 2 sales contract
- Negotiable-instruments suits

See `RCW-4_16.md` (general SOL chapter) and the relevant
UCC chapter for cause-of-action-specific SOLs.

### Statute of frauds

Writing required for promises to pay another's debt, sale
of land, promises not performable within 1 year, goods
above a threshold dollar amount, and several other
categories. See `RCW-19_36.md` and `RCW-62A_2.md` (for
the UCC-goods threshold).

### Choice of law + forum selection

Washington generally enforces choice-of-law and forum-
selection clauses if reasonable (*Voicelink Data
Servs.*). But CPA claims may not be waivable by choice-
of-law clauses (per *McKee v. AT&T*).

## WBCA — corporate doctrinal framework

### Director duties

- **Duty of care**: codified at RCW 23B.08.300 — the care
  an ordinarily prudent person in a like position would
  exercise
- **Duty of loyalty + good faith**: common-law /
  fiduciary overlay
- **Business judgment rule**: codified — directors
  entitled to rely on information from officers,
  professionals, committees

### Derivative actions

RCW 23B.07.400 requires plaintiff to be a contemporaneous
shareholder; demand on board required unless excused;
special-litigation-committee dismissal available.

### Dissenters' rights

Shareholders dissenting from major corporate actions
(merger, share exchange, sale of substantially all
assets, etc.) may demand appraisal at fair value. The
procedure has tight deadlines — payment demand before
vote, vote against the action, post-action statutory
process. See `RCW-23B_13.md` for the procedural
mechanics.

### Judicial dissolution

Court may dissolve a corporation on shareholder showing
of director / shareholder deadlock causing irreparable
injury, directors acting illegally / oppressively /
fraudulently, or waste of corporate assets. The
**oppression standard** in close corporations applies
the **reasonable-expectations** test from majority /
minority shareholder relationships (per *Scott v.
Trans-System, Inc.*).

For procedural mechanics, see `RCW-23B_14.md`.

## Washington LLC Act — doctrinal framework

### 2016 overhaul

The WA LLC Act was comprehensively rewritten in 2016
(SB 5030), aligning with the 2006 Revised Uniform LLC
Act. Pre-2016 LLC case law must be reread against the
new statute.

### Member duties

Default duties of loyalty and care unless modified by
operating agreement. The operating agreement may NOT
eliminate the loyalty core, the care gross-negligence
floor, or good-faith-and-fair-dealing.

### Judicial dissolution

Same general framework as WBCA — deadlock, oppression,
waste. (Citation: *Phillips v. Hayes-Phillips*.) See
`RCW-25_15.md`.

### Charging order — asset protection

A member's creditor can obtain a charging order against
the member's distributional interest only — no
foreclosure on membership interest itself. Strong asset-
protection feature.

## Partnership — RCW 25.05 (Revised UPA)

Formation automatic — no filing required for general
partnership. All property acquired by partnership =
partnership property. Partners have right to demand
accounting. Wrongful-dissociation and winding-up
procedures statutorily defined. See `RCW-25_05.md`.

## UCC — doctrinal framework

Washington's UCC at RCW 62A covers:

- **Article 1** — General provisions, definitions,
  choice of law
- **Article 2** — Sales of goods (statute of frauds
  threshold; battle of the forms; implied warranty of
  merchantability + fitness for particular purpose;
  warranty disclaimers; perfect tender rule)
- **Article 3** — Negotiable instruments (negotiability;
  holder-in-due-course; transfer)
- **Article 4** — Bank deposits and collections
- **Article 7** — Documents of title (warehouse
  receipts, bills of lading)
- **Article 8** — Investment securities
- **Article 9A** — Secured transactions (attachment vs.
  perfection; filing; priority; default / foreclosure;
  commercially-reasonable-disposition)

See the individual chapter files for section-level rules.

## MAR — Mandatory Arbitration of Civil Actions

Civil cases at or below the statutory jurisdictional cap
are subject to mandatory arbitration in participating
counties (King, Pierce, Snohomish, Spokane, Thurston,
Clark, Kitsap, Whatcom, Yakima). Awards may be tried de
novo on demand. Sanctions if trial de novo result is no
better. See `RCW-7_06.md`.

## Composition with other wa- skills

- `wa-statewide-format` — caption + GR 14
- `wa-discovery` — discovery in commercial cases
- `wa-first-30-days` — answer + affirmative defenses
- `wa-fact-check` — citation verification
- `wa-consumer-debt` — consumer-credit overlap
- `wa-kcsc` — King County Commercial cases routing
