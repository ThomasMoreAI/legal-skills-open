---
name: consumer-credit-disputes-codearranger
title: Consumer Credit Disputes
description: 'Use this skill to help a consumer file a LAWFUL Fair Credit Reporting Act (FCRA) dispute directly with the credit reporting agencies — the step that actually triggers the reinvestigation duty (15 U.S.C. § 1681i) — and to escalate to regulators AFTER the dispute. Triggers include "dispute my credit report", "how do I dispute", "dispute letter", "609 letter", "611 dispute", "method of verification", "e-OSCAR", "certified mail dispute", "the bureau verified it", "reinvestigation", "identity theft block", "block this fraud account", "605B", "human trafficking block", "CFPB complaint", "bona fide error", "credit repair company", "restart my disputes". Core rule: a regulator complaint alone is NOT an FCRA dispute — the dispute must go directly to the CRA (e-OSCAR or certified mail) with documented proof; identity-theft affidavits are wet-ink signed, never eSigned.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-federal-laws/skills/consumer-credit-disputes
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Consumer Credit Disputes

> **NOT LEGAL ADVICE.** This skill produces drafting aids and checklists. It is not legal advice
> and does not create an attorney-client relationship. Verify every deadline, dollar threshold,
> and statutory citation against current law before relying on or filing anything.

## The one rule that decides cases

**A complaint to the CFPB, a state Attorney General, or the BBB is NOT an FCRA dispute.** It does
not trigger the credit reporting agency's reinvestigation duty under 15 U.S.C. § 1681i, and it does
not, by itself, create a private right of action. A lawful dispute must go **directly to the credit
reporting company** — through its **e-OSCAR**-backed dispute channel or, preferably, by **certified
mail, return receipt requested.**

Disputes must be **documented with proof** (certified-mail receipt, tracking, copies of the letter
and enclosures). Undocumented disputes are how defendants win **motions to dismiss and summary
judgment** — the consumer cannot prove the duty was ever triggered. Build the proof trail as you
draft, and route it to `consumer-harm-documentation`.

The canonical statutory text is in
[`../../references/federal-debt-laws/FCRA.md`](../../references/federal-debt-laws/FCRA.md). Cite to
it; do not paraphrase from memory.

## Before you draft — three threshold checks

1. **Were prior disputes lawfully filed?** If earlier disputes went only to a regulator, or were
   filed by a credit-repair company in a way the consumer cannot prove, the consumer may want to
   consider whether a clean, documented, direct-to-CRA dispute would produce a clearer record.
   The decision is the consumer's.
2. **Credit-repair-service considerations.** Disputes routed through credit-repair outfits can
   create proof problems — high-volume "shotgun" disputes can appear frivolous to a CRA, and the
   consumer often cannot document what was sent. If such services are used, one option is to
   have the dispute mailed from the consumer's own address in the consumer's name, with the
   consumer retaining the proof.
3. **Is this an identity-theft / fraud matter?** The **block** track (below) is the FCRA's
   dedicated procedure for that fact pattern, separate from the ordinary reinvestigation track.

## Track A — ordinary dispute (§ 1681i reinvestigation)

- Send a specific, itemized dispute to **each** CRA reporting the error (and consider a parallel
  direct dispute to the furnisher under § 1681s-2(b)).
- Identify each item, state precisely what is wrong, and enclose supporting proof.
- **Reinvestigation clock: 30 days** from receipt (extended to **45 days** if the consumer provides
  additional relevant information during the period — FACTA). Diary the deadline.
- If the CRA fails to respond, "verifies" without a real investigation, or reinserts deleted data
  improperly → send the **notice-of-failure / follow-up** letter and preserve it as evidence of a
  possible willful violation.

## Track B — identity-theft & trafficking blocks (the 4-business-day clock)

- **Identity theft (§ 1681c-2):** on receipt of an **identity theft report** plus proof of
  identity and identification of the fraudulent information, the CRA must **block** the information
  — and must do so **within 4 business days** of receiving the request.
- **Human trafficking (§ 1681c-3):** adverse information that resulted from trafficking must be
  blocked on submission of the required documentation.
- **The consumer's own wet-ink affidavit.** The identity-theft affidavit (e.g., the FTC Identity
  Theft Report / police report package) **is completed, read, and signed by the consumer** — the
  consumer is the affiant, swearing to the consumer's own facts. The consumer signs it **by hand
  on paper, NOT eSigned.** Wet-ink signing avoids the eSign-consent and authentication
  complications that an opposing party can exploit later. This skill provides the form scaffold;
  the consumer supplies the facts and the signature.

## After the dispute — multi-regulator escalation (optional)

Once the lawful dispute is on record, a consumer may choose to file regulator complaints to
raise the matter's visibility and create an additional record:

- CFPB, the consumer's **state Attorney General**, state **financial-protection / banking**
  agencies, the **BBB**, and **civil-rights bodies** where a protected-class angle exists.
- Function: a regulator-complaint paper trail can document a pattern of notice followed by
  continued misreporting — evidence that bears on a furnisher's or CRA's claim of **bona fide
  error** and on **willfulness** under § 1681n. Whether to pursue this layer is a decision for
  the consumer and any counsel the consumer retains.
- Every dispute, complaint, and response is **evidence** — preserve all of it via
  `consumer-harm-documentation`.

## Artifacts this skill drafts

- **§ 1681i dispute letter** — itemized, per-CRA, certified-mail-ready, with an enclosures list and
  a proof-of-mailing reminder.
- **§ 1681c-2 identity-theft block request** — paired with a wet-ink affidavit checklist and the
  4-business-day deadline called out.
- **Notice-of-failure / follow-up letter** — for missed deadlines or sham verifications.
- **Multi-regulator complaint packet** — coordinated CFPB / AG / BBB / civil-rights complaint
  scaffolds, to be filed *after* the direct dispute.

Each artifact ends with the `NOT LEGAL ADVICE` disclaimer.

## Related federal authority

- **Reg V (12 CFR Part 1022)** — the FCRA's implementing regulation:
  [`../../references/federal-debt-laws/Reg-V.md`](../../references/federal-debt-laws/Reg-V.md).
  §§ 1022.42–1022.43 set the **furnisher accuracy and reinvestigation duties** that a direct
  dispute to the furnisher (FCRA § 1681s-2(b)) triggers — pair them with the § 1681i dispute to the
  CRA.
- **FDCPA § 1692e(8)** —
  [`../../references/federal-debt-laws/FDCPA.md`](../../references/federal-debt-laws/FDCPA.md).
  A debt collector's **failure to communicate that a disputed debt is disputed** is an independent
  FDCPA violation; in a collection matter, plead it alongside the FCRA dispute.

## Composition

- Get the reports first → **`consumer-report-ordering`**.
- Fix PII, Date of First Delinquency, and the "disputed by consumer" flag → **`consumer-report-accuracy`**.
- Preserve proof and build damages → **`consumer-harm-documentation`**.
- Propagate corrections and keep monitoring → **`consumer-credit-monitoring`**.
- Underlying debt defense → the state **`*-consumer-debt`** bundle; pro-se mechanics → the state
  **`*-pro-se`** skill.
