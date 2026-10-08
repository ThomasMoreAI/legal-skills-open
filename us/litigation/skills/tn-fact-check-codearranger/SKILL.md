---
name: tn-fact-check-codearranger
title: Fact-Check Tennessee Court Filings
description: 'This skill should be used to fact-check a Tennessee court filing before it is filed. Triggers include "fact-check this Tennessee filing", "verify citations in my motion", "check the Tenn. R. Civ. P. citations in this brief", "check Tenn. Code Ann. citations", "audit this Tennessee pleading", "review my pro se filing before I file it in Tennessee", "check that my numbers are consistent across the packet", "verify the case cites in my Davidson Chancery brief". Runs four passes: (1) citation verification against canonical Tennessee sources (Tenn. Code Ann., Tenn. R. Civ. P./Evid., cases in S.W.3d, Tenn. Sup. Ct. R. 4 on unpublished opinions); (2) internal consistency within a single document (dates, dollar amounts, defined terms); (3) packet consistency across motion + affidavit + proposed order + certificate of service; (4) sworn- versus-argued consistency between affidavit facts and memorandum assertions.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Tennessee Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently
> against current rules and case law before filing.

Use this skill before any Tennessee court filing leaves the desk. It
runs four passes. It is the deeper evidentiary-citation pass;
`tn-quality-check` is the lighter format-and-content pass.

## Pass 1 — Citation verification

For every rule, statute, and case citation in the document, verify:

- **Rule cited**: exists and says what the brief claims. Use the
  current **Tenn. R. Civ. P.** or **Tenn. R. Evid.** text. Confirm
  the subsection — e.g., a motion to dismiss for failure to state a
  claim is **Tenn. R. Civ. P. 12.02(6)**. Tennessee uses dot-decimal
  rule numbering (Rule 12.02, 56.04, 59.04), not the federal
  parenthetical style.
- **Statute cited**: exists at the cited subsection. Tennessee
  statutes are **Tenn. Code Ann. § NN-N-NNN** (or **T.C.A. §**).
  Confirm against an authoritative source; flag any section the
  brief invented or mis-numbered.
- **Federal statute cited**: exists at the cited subsection (e.g.,
  FDCPA at 15 U.S.C. § 1692 et seq.). Pull from the federal corpus.
- **Case cited**: exists; the reporter citation is correct; the
  proposition stands for what the brief claims; the case has not been
  overruled. Tennessee appellate cases run in the **South Western
  Reporter** (S.W., S.W.2d, S.W.3d).

### Tennessee citation format checks

- Tennessee Supreme Court: `[Party A] v. [Party B], [###] S.W.3d
  [###] (Tenn. [YEAR])`
- Court of Appeals: `[Party A] v. [Party B], [###] S.W.3d [###]
  (Tenn. Ct. App. [YEAR])`
- Court of Criminal Appeals: `(Tenn. Crim. App. [YEAR])`
- Statutes: `Tenn. Code Ann. § XX-X-XXX` (use the section symbol)
- Rules: `Tenn. R. Civ. P. XX.XX` / `Tenn. R. Evid. XXX` (no `§` for
  rules)
- Style: standard **Bluebook**; Tennessee has no separate mandatory
  style manual.

### Unpublished-opinion caution (Tenn. Sup. Ct. R. 4)

**Tenn. Sup. Ct. R. 4** governs publication and citation of opinions:

- **Published** opinions are controlling authority.
- **Unpublished** opinions are persuasive, not controlling, and an
  opinion **designated "Not for Citation"** must not be cited.
- Flag any unpublished opinion the brief relies on **as if it were
  controlling** — soften to persuasive, and confirm it is not marked
  not-for-citation. Verify the precise contours of Rule 4 against its
  current text.

### Watch-items specific to Tennessee substance

When the brief touches these areas, double-check the citation because
the law shifted recently:

- **Summary-judgment standard.** *Hannan v. Alltel Publishing Co.*,
  270 S.W.3d 1 (Tenn. 2008), was **overruled** by *Rye v. Women's
  Care Center of Memphis, MPLLC*, 477 S.W.3d 235 (Tenn. 2015), which
  restored the Celotex-style standard alongside Tenn. Code Ann.
  § 20-16-101. A brief still citing *Hannan* as the governing
  standard is a **FAIL** — flag it.
- **Debt-buyer default proof.** Tenn. Code Ann. § 20-6-104 (added by
  2024 Tenn. Acts ch. 914, eff. July 1, 2024) requires a subsequent
  creditor / debt-buyer plaintiff to present documentation of
  authority to collect plus at least one document showing the debt's
  existence before any default judgment. Confirm currency and that it
  is applied only to subsequent creditors, not original creditors.
- **TCPA-and-debt-collection.** *Pursell v. First American National
  Bank*, 937 S.W.2d 838 (Tenn. 1996), holds the act of collecting a
  debt / enforcing a security interest is generally not "trade or
  commerce" under the Tennessee Consumer Protection Act (Tenn. Code
  Ann. § 47-18-101 et seq.). Treat categorical statements as
  fact-specific; verify no intervening authority before relying on
  it.
- **Relocation framework.** Tenn. Code Ann. § 36-6-108 was amended
  effective July 1, 2018, replacing the old 100-mile / petition-
  burden framework. Pre-2018 sources are stale — flag any brief
  citing the superseded standard.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Dates**: every date is consistent across all appearances (date of
  service, date of contract, date of last payment, date judgment was
  entered). The 10-day de novo appeal window from General Sessions to
  Circuit (Tenn. Code Ann. § 27-5-108) and the non-extendable 30-day
  Rule 59 motion-to-alter-or-amend window run from **entry of
  judgment** — confirm the stated entry date supports any timeliness
  argument.
- **Dollar amounts**: every amount is consistent and the totals add
  up (principal + interest + fees + costs = total demanded). If the
  matter is in General Sessions, confirm the demand respects the
  **$25,000** civil jurisdictional cap (Tenn. Code Ann. § 16-15-501),
  noting that forcible entry & detainer (eviction) is unlimited and
  attorney's fees / costs are excluded from the cap.
- **Defined terms**: any term defined with `(the "Account")` is used
  consistently (no slipping into "the loan" or "the debt").
- **Party names**: each party named consistently.
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to a real location.
- **Numbered paragraphs**: sequential without gaps or duplicates —
  Tenn. R. Civ. P. 10.02 requires each averment in a numbered
  paragraph limited to a single set of circumstances.

## Pass 3 — Packet consistency

Across the multi-document packet (motion + supporting affidavit +
proposed order + certificate of service):

- **Caption identical** in every document: court (Circuit / Chancery
  / General Sessions), county, party names, and docket number must
  match exactly (Tenn. R. Civ. P. 10.01).
- **Document title** matches in the motion's certificate of service
  and the proposed order's title.
- **Dates align**: the certificate-of-service date should match the
  signature date on the motion; the affidavit's jurat date should
  align with when it was sworn.
- **Relief sought matches**: the motion's prayer ("WHEREFORE, movant
  respectfully requests ____") must mirror the proposed order's
  ordering language ("IT IS THEREFORE ORDERED ____"), item by item.
- **Exhibits** referenced in the motion are described in the affidavit
  and physically attached — Tenn. R. Civ. P. 10.03 requires attaching
  a copy of a written instrument that is an exhibit.
- **Hearing timing**: for a Rule 56 motion, confirm the Notice of
  Hearing sets the hearing **at least 30 days** after service of the
  motion (Tenn. R. Civ. P. 56.04).
- **Page limits / typography** are a **local-rule** matter in
  Tennessee — there is no statewide page or margin rule. Verify the
  venue's current local rules and flag any limit you cannot confirm.

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting affidavit against what is
argued in the motion or memorandum:

- Every **factual assertion** in the argument should be (a) supported
  by a citation to a paragraph of the affidavit, (b) admitted in the
  pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the memorandum **not** supported by
  the affidavit — a gap to fix before filing.
- Identify any sworn fact **not used** in the memorandum — consider
  whether it belongs in the affidavit at all.
- Verify the affidavit's **personal-knowledge foundation** and, for a
  business-records affidavit, that it satisfies the custodian /
  qualified-witness requirement of **Tenn. R. Evid. 803(6)** and any
  self-authentication under **Tenn. R. Evid. 902** (verify the exact
  902 sub-paragraph numbering against current text). Flag paragraphs
  that begin "I believe" or "I understand" without a foundation.

## Output format

When invoked on a packet, produce a structured report:

```
FACT-CHECK REPORT — [Document title / Docket number]

Pass 1 (Citations)
  PASS  Tenn. R. Civ. P. 12.02(6)       — exists; correct subsection
  WARN  Tenn. Code Ann. § 47-2-725      — verify 4-yr UCC SOL vs.
        6-yr contract SOL (§ 28-3-109) applies to these goods
  FAIL  Hannan v. Alltel, 270 S.W.3d 1  — overruled by Rye (2015);
        do not cite as governing SJ standard

Pass 2 (Internal consistency)
  PASS  Defined terms used consistently
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, affidavit, proposed order
  FAIL  Notice of Hearing sets SJ hearing 21 days out; Rule 56.04
        requires service at least 30 days before the hearing

Pass 4 (Sworn vs. argued)
  FAIL  Memorandum p.3 asserts "the collector held a license"; no
        corresponding affidavit paragraph

Summary: 7 PASS / 2 WARN / 3 FAIL — DO NOT FILE until FAILs resolved.
```

## Composition

- For format checks: `tn-statewide-format` + `scripts/format-check.py`
  on the generated document
- For deadline arithmetic checks (Rule 6.01 computation, Rule 6.05
  3-day mail add-on, Tenn. Code Ann. § 15-1-101 holidays):
  `tn-deadlines`
- For the lighter pre-filing format-and-content pass:
  `tn-quality-check`
- For canonical statute / rule text: `tn-law-references`
- For consumer-debt substance (chain of title, § 20-6-104 default
  proof): `tn-consumer-debt`

## References

- `tn-law-references` for canonical Tenn. Code Ann., Tenn. R. Civ. P.,
  and Tenn. R. Evid. text
- Confirm all citations against current authoritative sources before
  filing; this skill flags suspect citations but does not warrant
  their accuracy. Verify current local rules of the filing court.
