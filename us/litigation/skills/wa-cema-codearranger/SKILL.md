---
name: wa-cema-codearranger
title: Washington CEMA — Commercial Electronic Mail Act (RCW 19.190)
description: Use this skill for Washington Commercial Electronic Mail Act (CEMA, RCW 19.190) matters — claims or defense over commercial spam e-mail and text messages with false/misleading subject lines or misrepresented transmission paths. Triggers include "CEMA", "Commercial Electronic Mail Act", "RCW 19.190", "spam email lawsuit", "spam text message", "false subject line", "misleading subject line", "$500 per email", "commercial electronic mail", "CAN-SPAM", "Brown v. Old Navy". Covers CEMA elements, the Brown v. Old Navy subject-line construction, per se CPA route, $500 statutory damages per message (no actual-damages requirement), common defenses (CAN-SPAM preemption, commercial-purpose gate, consent), and fact-pattern triage.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-cema
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Brown V Old Navy
  path: references/Brown-v-Old-Navy.md
- title: Cema Statute
  path: references/cema-statute.md
---

# Washington CEMA — Commercial Electronic Mail Act (RCW 19.190)

The subject-matter skill for Washington anti-spam matters under the
**Commercial Electronic Mail Act**, RCW 19.190. It supplies the
substantive law, the controlling *Brown v. Old Navy* construction,
the elements, defenses, and fact-pattern triage for a case that turns
on a commercial e-mail (or commercial text message) sent to a
Washington resident with a false/misleading subject line or a
misrepresented transmission path.

> **NOT LEGAL ADVICE.** These notes are drafting aids, not legal
> advice. Verify every citation against the current statute, rule, or
> opinion before filing — and note the **pending 2026 amendment** to
> RCW 19.190.020 / .040 flagged in `references/cema-statute.md`. See
> `wa-fact-check` and `wa-law-references/references/online-sources.md`.

## How this skill is organized

This is a **subject-matter skill**. It sits alongside the procedural
skills (`wa-first-30-days`, `wa-discovery`, `wa-law-references`,
`wa-hearings`, the `wa-draft-*` scaffolders) and supplies the
CEMA-specific content they delegate to. It also composes with
`wa-consumer-debt`, which holds the broader Washington Consumer
Protection Act (CPA) framework that a CEMA claim rides into.

```
wa-cema/
├── SKILL.md                  ← you are here
└── references/
    ├── cema-statute.md        operative RCW 19.190 provisions (curated)
    └── Brown-v-Old-Navy.md    Wash. Sup. Ct., Apr. 17, 2025 — the
                               controlling subject-line construction
```

## What CEMA prohibits

CEMA reaches only messages sent for a **commercial purpose** —
"promoting real property, goods, or services for sale or lease"
(RCW 19.190.010(2)). Within that gate it regulates two channels:

- **Commercial e-mail** — RCW 19.190.020 / .030.
- **Commercial text messages (SMS)** — RCW 19.190.060.

The e-mail prohibition (RCW 19.190.020(1)) has **two truthfulness
requirements** for a message sent from a Washington computer, or to an
address the sender knew or had reason to know is held by a Washington
resident:

- **(1)(a) Transmission-path / origin:** must not use a third party's
  internet domain name without permission, or otherwise misrepresent or
  obscure the point of origin or transmission path.
- **(1)(b) Subject line:** must not contain false or misleading
  information.

## The controlling case — *Brown v. Old Navy* (Wash. 2025)

*Brown v. Old Navy, LLC*, No. 102592-1 (Wash. Apr. 17, 2025) (en banc),
answering a certified question from the W.D. Wash., **holds that RCW
19.190.020(1)(b) prohibits a commercial e-mail subject line containing
*any* false or misleading information — not only deception about the
message's commercial nature.** González, J.; Madsen, J., dissenting
(reading (1)(b) to reach only subject lines that conceal the e-mail's
commercial purpose). Full headnote + cleaned opinion text in
`references/Brown-v-Old-Navy.md`.

Practical effect: a fabricated discount, a false "order status" framing,
or a manufactured sense of urgency in the subject line of a promotional
e-mail can satisfy (1)(b) even though it says nothing false about the
message being an advertisement.

## Elements (subsection (1)(b) theory)

1. A **commercial electronic mail message** — sent for the purpose of
   promoting real property, goods, or services for sale or lease
   (RCW 19.190.010(2)).
2. Sent **from a Washington computer** OR **to an address the sender
   knew / had reason to know is held by a Washington resident**.
3. The subject line **contains false or misleading information**
   (RCW 19.190.020(1)(b)) — *any* such information after *Brown*.

(For a (1)(a) theory, swap element 3 for misrepresentation/obscuring of
the origin or transmission path.)

## Remedy — the per se CPA route + statutory damages

- A CEMA e-mail violation is a **per se Consumer Protection Act
  violation** (RCW 19.190.030(1), .100; ch. 19.86 RCW) — so it enters
  the CPA's private right of action without separately proving the five
  *Hangman Ridge* elements (see `wa-consumer-debt/references/wa-consumer-protection.md`).
- **Statutory damages: $500 per offending message or actual damages,
  whichever is greater** (RCW 19.190.040(1)); $1,000 (or actual) for an
  interactive computer service (RCW 19.190.040(2)).
- **No actual-damages showing required** — the injury is *receiving* the
  violating message (*Brown*, slip op. at 4; cf. RCW 19.86.090). This is
  what makes CEMA a class-action vehicle (per-message statutory damages ×
  a class of recipients).
- CPA remedies that ride along once liability attaches: attorney's fees
  and costs, and the discretionary treble-damages enhancement (capped) —
  see the CPA reference.

## Defense checklist

- **Commercial-purpose gate:** Is the message actually "for the purpose
  of promoting … for sale or lease"? Transactional, relationship, or
  informational messages may fall outside RCW 19.190.010(2).
- **Subject line truth:** Is the challenged subject line actually false
  or misleading (an objective, recipient-perspective inquiry)? Puffery vs.
  a verifiable misrepresentation.
- **Washington nexus:** Sent from a WA computer, or to an address the
  sender knew/had reason to know is a WA resident's? Litigate the
  "reason to know" scienter.
- **CAN-SPAM preemption (15 U.S.C. § 7707(b)(1)):** The federal CAN-SPAM
  Act preempts state spam statutes **except** those prohibiting *falsity
  or deception*. CEMA's falsity-based prohibitions are designed to fit
  that savings clause — but test the specific theory against it.
- **Consent / established business relationship**, standing, and class
  certification issues.
- **Pending 2026 amendment** to RCW 19.190.020 / .040 (2274-S.SL) — the
  operative text and damages may change; confirm as of the filing date.

## Fact-pattern triage

| If the facts are… | Theory / focus |
|---|---|
| Promotional blast e-mail with a fake urgency / fake discount subject | RCW 19.190.020(1)(b) under *Brown* (any false/misleading subject line) |
| Spoofed "From" / forged header / borrowed domain | RCW 19.190.020(1)(a) transmission-path theory |
| Marketing **text** messages to a WA cell number | RCW 19.190.060 commercial-text-message prohibition |
| Class of WA recipients, each got the same blast | $500 × recipients under RCW 19.190.040(1); class certification |
| Defendant invokes CAN-SPAM | § 7707(b)(1) falsity savings-clause analysis |

## Composition

- **`wa-first-30-days`** — answer / counterclaim posture if you are the
  defense; complaint elements if you are bringing the claim.
- **`wa-consumer-debt`** — the CPA / *Hangman Ridge* framework and CPA
  remedies the per se violation feeds into.
- **`wa-discovery`** — targeting send logs, recipient lists, subject-line
  A/B test data, the sender's WA-resident knowledge, and consent records.
- **`wa-draft-motion` / `wa-draft-declaration`** — scaffolders.
- **`wa-law-references`** — civil rules, evidence, fees, online sources.
- **`wa-statewide-format`** — GR 14 formatting; **`wa-fact-check`** —
  citation + 2026-amendment currency check before filing.
