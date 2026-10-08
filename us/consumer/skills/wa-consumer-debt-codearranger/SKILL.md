---
name: wa-consumer-debt-codearranger
title: Washington Consumer-Debt Defense
description: Use this skill for Washington consumer-debt defense — debt-buyer suits, original-creditor collection, FDCPA claims, or CFPB Regulation F / Washington Collection Agency Act (RCW 19.16) / Washington CPA (RCW 19.86) issues in debt collection. Triggers include "debt buyer", "I was sued on a credit card", "collection agency sued me", "FDCPA", "validation notice", "Regulation F", "RCW 19.16", "RCW 19.86", "CPA counterclaim", "statute of limitations on this debt", "time-barred debt", "chain of title", "original cardholder agreement", "Certificate of Indebtedness". Covers substantive law, fact-pattern triage, chain-of-title doctrine, and discovery targeting plaintiff's elements.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-consumer-debt
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: consumer
language: en
sources:
- title: Chain Of Title
  path: references/chain-of-title.md
- title: Evidence Debt Buyer
  path: references/evidence-debt-buyer.md
- title: Fact Patterns
  path: references/fact-patterns.md
- title: Fdcpa
  path: references/fdcpa.md
- title: Fees Consumer Debt
  path: references/fees-consumer-debt.md
- title: Interrogatories Debt Buyer
  path: references/interrogatories-debt-buyer.md
- title: Key Cases
  path: references/key-cases.md
- title: Meet And Confer Debt Buyer
  path: references/meet-and-confer-debt-buyer.md
- title: Online Sources Consumer Debt
  path: references/online-sources-consumer-debt.md
- title: Recent Decisions
  path: references/recent-decisions.md
- title: Reg F
  path: references/reg-f.md
- title: Rfa Debt Buyer
  path: references/rfa-debt-buyer.md
- title: Rfp Debt Buyer
  path: references/rfp-debt-buyer.md
- title: Ucc Article 9
  path: references/ucc-article-9.md
- title: Wa Consumer Protection
  path: references/wa-consumer-protection.md
- title: Wa Statutes Of Limitations
  path: references/wa-statutes-of-limitations.md
---

# Washington Consumer-Debt Defense

The subject-matter bundle for Washington consumer-debt cases. This
skill is the container for the substantive law, fact patterns,
discovery banks, and case catalog that apply when the matter is
debt collection — whether the plaintiff is a debt buyer, a
collection law firm, or the original creditor.

> **NOT LEGAL ADVICE.** These notes are drafting aids, not legal
> advice. Every citation should be verified against the current
> statute, rule, or opinion before filing. See
> `wa-fact-check` and `wa-law-references/references/online-sources.md`
> for verification workflow.

## How this skill is organized

This is a **subject-matter bundle**. It sits alongside the
procedural skills (`wa-first-30-days`, `wa-discovery`,
`wa-law-references`, `wa-hearings`, etc.) and supplies the
debt-specific content those procedural skills delegate to.

```
wa-consumer-debt/
├── SKILL.md                       ← you are here
└── references/
    ├── chain-of-title.md          UCC Article 9 chain analysis
    ├── ucc-article-9.md           RCW 62A.9A mechanics
    ├── fdcpa.md                   15 U.S.C. § 1692 et seq.
    ├── reg-f.md                   12 C.F.R. Part 1006
    ├── wa-consumer-protection.md  RCW 19.16, RCW 19.86, Hangman Ridge
    ├── wa-statutes-of-limitations.md  RCW 4.16 applied to debt
    ├── fees-consumer-debt.md      FDCPA, CPA, RCW 19.16.450 fee-shifting
    ├── evidence-debt-buyer.md     ER 803/901/1002 applied to debt records
    ├── online-sources-consumer-debt.md  canonical URLs for debt sources
    ├── fact-patterns.md           ten recurring debt-buyer patterns
    ├── key-cases.md               debt-specific case catalog
    ├── recent-decisions.md        recent on-point decisions
    ├── rfp-debt-buyer.md          RFP banks for chain / damages / CPA
    ├── interrogatories-debt-buyer.md
    ├── rfa-debt-buyer.md
    ├── meet-and-confer-debt-buyer.md
    └── examples/                  synthetic sample filings
        ├── README.md
        ├── example-answer.md
        ├── example-motion-to-compel.md
        ├── example-declaration.md
        ├── example-proposed-order.md
        ├── example-meet-and-confer.md
        └── example-certificate-of-service.md
```

## When to use this skill

Invoke `wa-consumer-debt` when any of the following apply:

- The plaintiff is a **debt buyer** (Velocity, Portfolio Recovery,
  LVNV, Midland, Cavalry, Jefferson Capital, CACH, Unifund,
  Palisades, Resurgent, etc.)
- The complaint alleges default on a **credit-card, consumer-loan,
  medical-debt, or utility account**
- The plaintiff relies on a **Certificate of Indebtedness**, a
  **bill of sale with a redacted schedule**, or a **specimen
  cardholder agreement** instead of the specific documents
- The user wants to **counterclaim under the FDCPA, Reg F, RCW
  19.16, or the CPA**
- The debt may be **time-barred**, **re-aged**, or collected by an
  **unlicensed** entity

For non-debt civil matters (landlord-tenant, family, PI, etc.),
use the procedural skills directly; this bundle does not apply.

## The debt-buyer case — what the plaintiff must prove

A Washington debt-buyer plaintiff has to establish each of these
by admissible evidence. Every debt-specific discovery request,
affirmative defense, and motion in this skill targets one of these
elements:

1. **Standing** — plaintiff owns *this specific account*. Requires
   a complete chain from the originator with account-level
   identification. See `references/chain-of-title.md` and
   `references/ucc-article-9.md`.

2. **The agreement** — defendant agreed to *this specific
   contract*. The original cardholder agreement (not a specimen)
   must be authenticated. See `references/evidence-debt-buyer.md`
   (ER 901, 902, 1002 applied to debt records) and
   `references/fdcpa.md` (verification-stage challenges).

3. **Performance** — plaintiff / predecessors provided the credit.
   Usually stipulated but occasionally contested.

4. **Breach** — defendant defaulted. Monthly statements establish
   the default date and amount.

5. **Damages** — specific amount, calculated correctly, timely.
   Charged-off balance vs. post-charge-off interest and fees are
   frequently inflated. See
   `references/wa-statutes-of-limitations.md` for the timeliness
   piece.

## Fact-pattern triage

Match the complaint's attachments against
`references/fact-patterns.md`. The ten recurring patterns:

1. Generic pool schedule / redacted bill of sale
2. Missing monthly statements
3. No original cardholder agreement
4. Remote-custodian affidavit (*Ziegler* / *Discover Bank v.
   Bridges* problem)
5. Account-stated vs. written-contract confusion (SOL trap)
6. Time-barred suit (Reg F § 1006.26 + FDCPA § 1692e/f)
7. Unlicensed collection agency (*Gray v. Suttell* / RCW 19.16)
8. Naming-churn / chain-of-title gaps
9. Default-judgment trap (CR/CRLJ 60 vacation)
10. Zombie / re-aged debt (FCRA + RCW 19.16)

The pattern is informational — it maps a recurring fact pattern to
the procedural options the rules make available: (a) the choice
between an MTD and an answer, (b) the affirmative defenses that
fit the pattern, (c) the counterclaims the pattern raises, and
(d) the discovery the pattern points toward. Which of these the
litigant pursues remains the litigant's decision (and any counsel
the litigant retains).

## Affirmative defenses commonly in play

Plead every one that fits; unpleaded defenses are waived (CR 8(c) /
CRLJ 8(c)). For a typical debt-buyer case:

- Statute of limitations (RCW 4.16 — see
  `references/wa-statutes-of-limitations.md` for the day count
  applicable to the cause of action pleaded)
- Lack of standing (CR 17(a), real-party-in-interest)
- Lack of capacity to sue (RCW 19.16 licensing requirement —
  *Gray v. Suttell*; see `references/wa-consumer-protection.md`)
- Failure to state a claim (CR 12(b)(6), preserved)
- Failure of consideration (Article 9 attachment deficiency)
- Unclean hands / FDCPA violations
- Set-off (FDCPA / CPA damages offset any judgment)
- Waiver / estoppel / laches (fact-specific)
- Accord and satisfaction (if prior settlement)
- Payment
- Reservation of additional defenses pending discovery

## Counterclaims commonly in play

Every fact supporting an affirmative defense in a debt-buyer case
usually also supports a counterclaim:

- **FDCPA** — 15 U.S.C. § 1692 et seq. Federal claim cognizable in
  state court; SOL is short and runs from violation
  (*Rotkiske v. Klemm*). See
  `../wa-law-references/references/federal-debt-laws/` for current
  statutory text.
- **Regulation F** — 12 C.F.R. Part 1006, enforced through FDCPA
- **WA Collection Agency Act** — RCW 19.16; see
  `references/wa-consumer-protection.md` for the per-se WA-CPA
  pathway and the current licensing-violation framework.
- **WA Consumer Protection Act** — RCW 19.86. RCW 19.16 violations
  can supply a per-se pathway that bypasses the *Hangman Ridge*
  public-interest element; see `references/wa-consumer-
  protection.md` for the elements and the current treble-damages
  cap.
- **FCRA** (if re-aging / credit reporting involved — Pattern 10)

**Prayer for relief** should include: dismissal; actual damages;
FDCPA statutory damages; treble CPA damages (subject to the
statutory cap); reasonable attorney fees (see
`references/fees-consumer-debt.md` for the debt-specific
fee-shifting grounds, and
`../wa-law-references/references/fees-and-costs.md` for the
general RCW 4.84 and rule-based grounds); costs; such further
relief. For current statutory-damages amounts and the CPA
treble-damages cap, consult the references corpus — those
figures are amended by statute.

## Discovery — target the elements

Every RFP, IROG, and RFA maps to one of the five plaintiff-must-
prove elements above. See the banks in `references/`:

- `references/rfp-debt-buyer.md` — requests for production
- `references/interrogatories-debt-buyer.md` — interrogatories
- `references/rfa-debt-buyer.md` — requests for admission
- `references/meet-and-confer-debt-buyer.md` — CRLJ 26(f) /
  CR 26(i) meet-and-confer paragraphs for debt-buyer deficiencies

Sequence discovery in rounds (see `wa-discovery/SKILL.md` for the
general cadence):

- **Round 1** — standing and chain of title
- **Round 2** — damages and account history
- **Round 3** — predicate acts for FDCPA / CPA counterclaim

## Composition

This bundle composes with:

- `wa-first-30-days` — initial response workflow (calls into this
  skill's fact-patterns, affirmative defenses, and counterclaims
  for debt-buyer cases)
- `wa-discovery` — procedural discovery framework (this skill
  supplies the debt-specific request banks)
- `wa-law-references` — civil rules, evidence rules, fees-and-
  costs, local rules, online-sources, general key-cases, citation
  format
- `wa-statewide-format` — GR 14 formatting
- `wa-kcdc` — King County District Court specifics
- `wa-pro-se` — pro-se drafting framework, service protocol
- `wa-fact-check` — citation verification before filing
- `wa-file-packet` — packet assembly
- `wa-draft-motion`, `wa-draft-declaration`, `wa-draft-order`,
  `wa-draft-note` — document scaffolding

## Notes

- **Not legal advice.** This skill supplies drafting aids. The
  user owns every word filed.
- **Shepardize / KeyCite** every case before citing. Washington
  business-records foundation doctrine has evolved; debt-buyer
  standing doctrine is still developing.
- **Verify statutes and rules** against the current RCW text and
  current court-rule text. Use
  `wa-law-references/references/online-sources.md` for canonical
  URLs and `wa-fact-check` before filing.
- **Federal backstops state.** Always pair FDCPA with RCW 19.16 so
  the state statute catches any federal-scope gap (e.g., debt
  buyers collecting "for their own account" outside FDCPA's
  primary definition under *Henson v. Santander*).
