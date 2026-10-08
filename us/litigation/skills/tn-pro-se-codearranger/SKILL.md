---
name: tn-pro-se-codearranger
title: Pro Se Drafting for Tennessee
description: Use when drafting Tennessee court documents for a self-represented (pro se) litigant. Covers pro-se drafting framework (substantial-compliance-with-form standard; no substantive advocacy from bench); Tenn. R. Civ. P. 4/5 service mechanics; signature-block convention (pro se filers OMIT the attorney BPR number, add "Pro Se / Self-Represented"); practical differences between formal Circuit / Chancery forums (written motions, affidavits, memoranda, proposed orders; 30-day answer) vs. informal General Sessions forum (no formal pleadings; testimony at hearing; 10-day de novo appeal to Circuit); Tennessee self-help resources (tncourts.gov self-help center; AOC-approved forms where they exist). Composes with `tn-statewide-format`, `tn-draft- motion`, `tn-general-sessions`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Tennessee

> **NOT LEGAL ADVICE.** This skill helps unrepresented parties prepare
> paper and procedure. It does not substitute for advice from a
> licensed Tennessee attorney. Verify against current rules and local
> practice before filing.

Use this skill in addition to `tn-statewide-format` whenever the filer
is unrepresented. Tennessee courts use the terms "pro se" and
"self-represented" interchangeably.

## The pro-se drafting framework — adapted for Tennessee

Tennessee courts construe pro se filings with a measure of leniency on
form, but the court will **not act as the filer's lawyer** — it will
not supply missing elements of a claim or defense, reframe an argument,
or develop the record. The practical two-track takeaway:

1. **Substantial compliance with form.** Minor formatting slips are
   tolerated so long as the substantive components are present —
   caption, claim or defense, supporting facts, signature, and any
   required sworn support.
2. **No substantive advocacy from the bench.** The filer must clearly
   **name the relief sought**, **cite the rule or statute** that
   authorizes it, **state facts** supporting each element, and **sign**
   the document.

Apply this framework to every pro se filing:

1. State the relief clearly in the opening sentence.
2. Cite the rule or statute (Tenn. R. Civ. P. ____ / Tenn. Code Ann.
   § ____).
3. State the facts that satisfy each element, with record support from
   a sworn affidavit where facts must be proven (see
   `tn-draft-declaration`).
4. Apply the controlling Tennessee case law.
5. Conclude with the specific order sought.

## Signature block — pro se omits the BPR number

Tennessee-licensed attorneys must sign every pleading, motion, or other
paper under **Tenn. R. Civ. P. 11** and include their **Tennessee Board
of Professional Responsibility (BPR) number**. A **pro se filer omits
the BPR number** — that field is for licensed attorneys only — and adds
a clear self-represented designation on the last line.

```
Respectfully submitted this ___ day of __________, 20__.

                                        ____________________________
                                        Jane Q. Doe
                                        [Street address]
                                        [City, TN ZIP]
                                        Phone: (###) ###-####
                                        Email: jane@example.com
                                        Pro Se / Self-Represented
                                        Defendant
```

Use **"Pro Se"** or **"Self-Represented"** on the last line, paired
with the filer's role ("Pro Se Plaintiff", "Self-Represented
Defendant", etc.). Do **not** write "N/A" in place of a BPR number —
simply omit the field.

By signing under Rule 11, the filer certifies that the paper is not
presented for an improper purpose, that the legal contentions are
warranted, and that the factual contentions have evidentiary support.
Rule 11 sanctions apply to pro se filers, not just attorneys.

## Service — Tenn. R. Civ. P. 4 and Rule 5

- **Rule 4** governs service of the original **summons and
  complaint**. A pro se plaintiff cannot personally serve their own
  defendant — use the sheriff, a private process server, or, where
  authorized, service by mail through the clerk. The summons must
  generally be issued and returned within the time set by Rule 4
  (confirm the current 90-day issuance/return window).
- **Rule 5** governs service of **subsequent papers** (motions,
  notices, responses). Serve every filed paper on every other party.
  Methods include hand delivery, U.S. Mail to the last-known address,
  and — where the court and the parties permit — electronic service.
  When serving by mail, add **3 days** to any responsive deadline under
  Tenn. R. Civ. P. 6.05 (use `tn-deadlines`).

A **Certificate of Service** is required on every filed paper. See
`tn-statewide-format` for the certificate template.

## Circuit / Chancery vs. General Sessions — pick the right forum

Tennessee's trial courts differ sharply in formality, and a pro se
litigant should understand which forum the case is in:

| | Circuit / Chancery | General Sessions |
|---|---|---|
| Formality | Formal; Tenn. R. Civ. P. govern | Informal; Rules of Civil Procedure generally do **not** apply |
| Jurisdiction | General jurisdiction (Chancery = equity); divorce in both | Limited — civil cap **$25,000** (Tenn. Code Ann. § 16-15-501); **unlimited** for forcible entry & detainer (eviction) |
| Pleadings | Written complaint, answer, motions, memoranda | A civil warrant (a short form); no formal written pleadings required |
| Discovery | Full discovery as of right (Rules 26–37) | **No formal discovery as of right** |
| Sworn support | Notarized affidavits common (`tn-draft-declaration`) | Testimony at the hearing; affidavits less central |
| Appeal | To the Court of Appeals | **De novo to Circuit within 10 days** of judgment (Tenn. Code Ann. § 27-5-108) |

**Practical guidance for pro se filers:**

- **General Sessions** is the more accessible forum for small civil
  disputes and evictions — it is designed for quick, informal
  hearings. You generally appear and tell your side to the judge rather
  than filing briefs. See `tn-general-sessions`.
- If you **lose in General Sessions**, you have only **10 days** from
  entry of judgment to perfect a **de novo appeal to Circuit Court**,
  where the case is tried again under full civil rules (Tenn. Code Ann.
  § 27-5-108). This is a hard, uniform statewide deadline — calendar it
  immediately. See `tn-post-judgment`.
- In **Circuit or Chancery**, the formal rules apply: an **answer is
  due 30 days** after service (Tenn. R. Civ. P. 12.01), motions must
  state their grounds and relief (Rule 7.02), and many filings need a
  supporting affidavit and a proposed order.

## Self-help resources

- **Tennessee Courts self-help center** at **tncourts.gov** — the
  Administrative Office of the Courts (AOC) publishes self-help
  information and a set of **AOC-approved forms** for certain matters
  (verify which forms exist for your case type and county — coverage is
  not comprehensive across all matters).
- **Local rules** for the filing court are indexed on the AOC "Local
  Rules of Practice" page at tncourts.gov — read them before filing,
  because page limits, hearing-date procedures, and chambers-copy
  requirements are set locally (see `tn-statewide-format`).
- **County court clerks** (Circuit Court Clerk, Clerk & Master for
  Chancery, General Sessions Clerk) can explain filing mechanics and
  fees but cannot give legal advice.
- **Notarization**: Tennessee's default sworn support is a **notarized
  affidavit** (see `tn-draft-declaration`); notaries are available at
  banks, clerk's offices, and shipping stores.

## Common pro se pitfalls in Tennessee

1. **Missing the 10-day General Sessions appeal window** — de novo
   appeal to Circuit must be perfected within 10 days of entry (Tenn.
   Code Ann. § 27-5-108). Late = lost.
2. **Treating Circuit / Chancery like General Sessions** — the formal
   forums require written motions, memoranda, affidavits, and proposed
   orders. Showing up to "tell your story" is not how a motion is
   decided there.
3. **Forgetting the 30-day answer deadline** — Tenn. R. Civ. P. 12.01
   gives 30 days after service to answer in Circuit / Chancery;
   default can follow a missed deadline. See `tn-first-30-days`.
4. **Filing an unsworn statement where a notarized affidavit is
   needed** — do not assume an unsworn declaration is accepted; default
   to a notarized affidavit and verify (`tn-draft-declaration`).
5. **Counting deadlines wrong** — Tenn. R. Civ. P. 6.01 excludes the
   triggering day, includes the last day (rolling forward off a
   Saturday, Sunday, or legal holiday), and Rule 6.05 adds 3 days for
   mail service. Tennessee's § 15-1-101 holidays include Good Friday
   and Columbus Day. Use `tn-deadlines`.
6. **Writing "N/A" for the BPR number** — pro se filers omit the field
   entirely and add "Pro Se / Self-Represented" instead.

## Composition

- For statewide format and the signature block: `tn-statewide-format`
- For the General Sessions forum: `tn-general-sessions`
- For drafting motions: `tn-draft-motion`
- For affidavits: `tn-draft-declaration`
- For the Notice of Hearing: `tn-draft-note`
- For proposed orders: `tn-draft-order`
- For the answer and first responses: `tn-first-30-days`
- For consumer-debt defense as pro se: `tn-consumer-debt`
- For family-law matters as pro se: `tn-family-law`, `tn-family-court`
- For deadline math: `tn-deadlines`
- For the venue overlay: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`

## References

- `references/pro-se-drafting-framework.md` — Tennessee pro se
  construction conventions
- `references/circuit-chancery-vs-sessions.md` — choosing and
  navigating the forum
- `references/signature-block.md` — pro se vs. attorney (BPR) signature
  conventions
- `references/self-help-resources.md` — tncourts.gov self-help center
  and AOC-approved forms directory
