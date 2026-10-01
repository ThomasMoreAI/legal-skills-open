---
name: cookie-consent-impl-clemensjl
title: Consent implementation
description: Use when wiring a cookie banner, consent manager or CMP into a site — blocking scripts before consent, gating embeds, Google Consent Mode, server-side tagging, consent records, Global Privacy Control — or when asked why trackers still fire before the click. Also use when a site already has a banner and needs an audit, when adding any third-party script, pixel, font, map or video embed, and before any release that touches analytics or advertising tags.
author: clemensjl
author_url: https://github.com/clemensjl/claude-skills/tree/main/skills/cookie-consent-impl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
sources:
- title: Audit
  path: references/audit.md
- title: Blocking Layer
  path: references/blocking-layer.md
- title: Cmp Decision
  path: references/cmp-decision.md
- title: Consent Mode Google
  path: references/consent-mode-google.md
- title: Consent Record
  path: references/consent-record.md
- title: Embeds
  path: references/embeds.md
- title: Frameworks
  path: references/frameworks.md
- title: Gpc Us
  path: references/gpc-us.md
- title: Intake
  path: references/intake.md
- title: Pre Ship
  path: references/pre-ship.md
- title: Server Side Tagging
  path: references/server-side-tagging.md
- title: Tcf
  path: references/tcf.md
- title: Ui Rules
  path: references/ui-rules.md
- title: Vendor Matrix
  path: references/vendor-matrix.md
---

# Consent implementation

How to make a consent banner actually control what loads. Governing rules: Article 5(3) of Directive 2002/58/EC (ePrivacy Directive, "ePD") and its national implementations, Articles 4(11), 7 and 12 GDPR, EDPB Guidelines 2/2023 v2.0, EDPB Guidelines 03/2022 v2.0, the EDPB Cookie Banner Taskforce report, plus vendor contracts (Google Consent Mode, IAB TCF) and US opt-out signal law.

## Core principle

**The obligation attaches when the script loads, not when it reports.** Article 5(3) ePD is triggered by storage on, or access to, the terminal equipment. Per EDPB Guidelines 2/2023 (Version 2.0, adopted 7 October 2024) para 50, distributing a tracking pixel or tracking link "does constitute storage, at the very least through the caching mechanism of the client-side software. As such, Article 5(3) ePD is applicable, even if this storage is not permanent." Para 51 adds that collecting the identifier back constitutes "gaining of access". Para 37: there is no lower limit on how long information must persist or how much of it there must be.

A `<script src>` to a third party therefore breaches the rule the moment the browser fetches it — before any cookie is written, before any event fires, whatever the vendor's "privacy mode" claims. So the only correct architecture is **deny-by-default at the loading layer**: no third-party script tag, no iframe, no font request, no pixel, no `localStorage` write until a consent signal exists. A banner rendered on top of an already-loaded Google Tag Manager is a banner over a violation.

## Limits

This skill decides whether an implementation honours a consent decision. It does not decide:

- **The wording.** Banner copy, cookie policy, privacy notice, category descriptions and legal bases belong to the `legal-*` skills. This skill assumes those texts exist and checks whether the code matches them.
- **Whether a given cookie is exempt.** The strictly-necessary test under Article 5(3) ePD is a legal assessment per purpose. The Cookie Banner Taskforce (para 27) records that authorities themselves treat this as hard. Propose a classification, never assert one.
- **National transposition.** Article 5(3) is a directive. Consent conditions, enforcement practice and re-prompt expectations differ by Member State (§ 165 Abs 3 TKG 2021 in Austria, art. 82 loi Informatique et Libertés in France). Get country-specific sign-off.
- **Sign-off.** Where the site sells, profiles, targets children, or runs programmatic advertising, a DPO or lawyer signs off before launch.

Every artefact this skill produces carries `<!-- CONSENT GATING – NOT VERIFIED AT NETWORK LEVEL -->` until the audit in `references/audit.md` runs green against the deployed page. Never remove the marker on the strength of reading the code.

## Workflow

1. **Intake first.** `references/intake.md`. Without the third-party inventory, every recommendation is a guess.
2. **Classify every third party** against `references/vendor-matrix.md`: category, blocking technique, whether a privacy-enhanced mode changes anything (it usually does not).
3. **Read the reference file for the layer you are touching** before writing code. The APIs move; recalled syntax is wrong syntax.
4. **Build the block, then the banner.** In that order. A banner wired to a tag that was already loaded cannot be fixed by UI work.
5. **Run `references/audit.md`** against the built page. The pass condition is a network-level assertion, not a screenshot.
6. **Run `references/pre-ship.md`** before release.

**Output shape.** Four parts, in this order:

1. the artefact — code, config or audit findings — carrying the draft marker
2. the `[[MISSING: …]]` list the user must supply
3. adjacent open items, one sentence each
4. the verification note: what was asserted at network level, and what was not

## Decision matrix

| Situation | What applies | Reference |
|---|---|---|
| Third-party script must not run before consent | Type-swapping, dynamic injection, CSP backstop | `blocking-layer.md` |
| Video, map, social or scheduling embed on the page | Click-to-load placeholder, no iframe before consent | `embeds.md` |
| Google Fonts, Adobe Fonts or any remote font | Self-host; a font request is a third-country transfer plus terminal access | `embeds.md` |
| GA4, Google Ads, Floodlight, GTM in use | Consent Mode v2 signals, `default` before `update` | `consent-mode-google.md` |
| Tagging moved to own domain or subdomain | Consent still required; ITP caps; CNAME cloaking | `server-side-tagging.md` |
| Need to prove consent was given | Art 7(1) GDPR record shape, retention, banner versioning | `consent-record.md` |
| Banner design under review | First-layer reject, no nudging, withdrawal parity | `ui-rules.md` |
| Site runs programmatic display advertising | IAB TCF, vendor list, TC String | `tcf.md` |
| Site has US traffic or US-facing entity | GPC signal, state opt-out laws, pixel litigation exposure | `gpc-us.md` |
| Next.js, Nuxt, SvelteKit or static site | Script strategy, hydration order, SSR unknown-state trap | `frameworks.md` |
| Existing site, unknown state | Scripted network + storage audit | `audit.md` |
| Deciding build vs buy | What a hand-rolled banner must actually do | `cmp-decision.md` |

## Hard rules

- **Gate at load, not at report.** No third-party request may leave the browser before a consent signal exists. EDPB Guidelines 2/2023 v2.0 para 50: distribution of a tracking pixel or link is already storage via client-side caching, "even if this storage is not permanent."
- **Deny by default in code, not only in the UI.** Cookie Banner Taskforce report (adopted 17 January 2023) para 7: "by default, no cookies which require consent can be set without a consent and that consent must be expressed by a positive action on the part of the user."
- **Legitimate interest is not available for the read/write itself.** Same report, para 24: "the legal basis for the placement/reading of cookies pursuant to Article 5(3) cannot be the legitimate interests of the controller." A tag configured to fire on legitimate interest is a tag firing without a legal basis.
- **A reject control belongs on the first layer.** Same report, para 8: a vast majority of authorities hold that the absence of a refuse/reject option on any layer carrying a consent button is an infringement. Para 14: a bare text link labelled "continue without accepting", with no visual support, does not save it.
- **Never pre-tick.** Same report, para 10, citing GDPR Recital 32: silence, pre-ticked boxes and inactivity do not constitute consent. This includes toggles rendered on by default in the settings layer.
- **Withdrawal must be reachable from every page.** GDPR Art 7(3); Cookie Banner Taskforce para 34 states three cumulative conditions — withdrawal possible, at any time, as easy as giving. Para 35: no specific mechanism can be imposed, so a persistent footer link is acceptable, but no mechanism at all is not.
- **Advanced Consent Mode is not a blocking mechanism.** Google's own documentation: in the advanced version "Google tags load when a user opens the website or app" and "while consent is `denied`, the Google tags send measurements without cookies." Loading the tag is already terminal-equipment access under Art 5(3) ePD.
- **Moving the tag to your own domain changes nothing about consent.** Server-side tagging changes who sets the cookie and how long it survives, not whether Article 5(3) applies to the initial client-side request.
- **`youtube-nocookie.com` is not consent-free.** Google's own description is limited to personalisation: the view "will not be used to personalize the YouTube browsing experience". The iframe still loads from a third party. Same logic for Vimeo `dnt=1` and Maps embeds.
- **Verify at the network layer.** No implementation is done until an automated load with zero interaction produces zero requests to non-essential hosts. Visual inspection of a banner proves nothing.

## Pending law, not current law

The Digital Omnibus proposal COM(2025) 837 final of 19.11.2025 (CELEX 52025PC0837, procedure 2025/0360(COD)) would move the terminal-equipment rule out of the ePrivacy Directive and into the GDPR as a new Art 88a, add machine-readable consent signals as a new Art 88b, and bar re-asking within six months. **None of it is law.** Status as at 2026-08-05: awaiting committee decision in joint ITRE/LIBE, draft report PE786.818 of 22.06.2026, amendments tabled 27.07.2026; no committee vote, no Parliament position, no Council general approach, no trilogue. The EDPB and EDPS jointly opposed parts of it in Joint Opinion 2/2026 of 10.02.2026.

Until it is published in the Official Journal, every rule in this skill stands unchanged and consent still runs through Art 5(3) ePrivacy as transposed nationally. Do not soften a gating requirement because a proposal might relax it. `[[UNVERIFIED: the article-by-article mapping above rests on the Commission staff working document and the EDPB–EDPS joint opinion, not on the enacting text; re-check before quoting the proposed wording]]`

Two instruments are routinely confused with this file and are not it: Regulation (EU) 2026/1744 (OJ 24.07.2026) amends the AI Act, not the GDPR or the ePrivacy Directive; and Omnibus IV, COM(2025) 501, concerns the GDPR Art 30(5) record-keeping exemption and is likewise not adopted.

## False friends

| Plausible wrong assumption | Actual position |
|---|---|
| "The Digital Omnibus abolished cookie banners" — from 2025 press coverage of the proposal | A Commission proposal is not law. It is still in committee; Art 5(3) ePD applies unchanged. |
| "Consent Mode v2 replaces blocking" — from Google's marketing framing of advanced mode | Advanced mode loads the tag before the choice and sends cookieless pings. It is a measurement-continuity feature, not a gate. See `consent-mode-google.md`. |
| "Server-side tagging removes the consent requirement" — from vendor pitches about first-party data | The browser still requests your endpoint and the endpoint still writes to the device. Art 5(3) is unchanged. |
| "It's first-party, so it's exempt" | Article 5(3) ePD does not distinguish first from third party. It distinguishes strictly necessary from not. |
| "Legitimate interest covers analytics" — imported from GDPR Art 6(1)(f) reasoning | The storage/access step under Art 5(3) has no legitimate-interest route (Cookie Banner Taskforce para 24). |
| "It only sets `localStorage`, not cookies" | Storage means any physical storage medium; the ePD sets no limit on medium, duration or amount (Guidelines 2/2023 paras 37, 38). |
| "No cookie is set, so no consent needed" — from cookie-centric CMP UIs | Fingerprinting, pixel-only tracking and IP-based tracking are in scope (Guidelines 2/2023 §3.1, §3.3). |
| "US-style opt-out is enough" — from CCPA-shaped vendor defaults | Opt-out is the US model. The EU model is prior opt-in for anything not strictly necessary. |
| "We use a certified CMP, so we comply" | A CMP that is installed but not wired to the loading layer produces a compliant-looking banner over an uncontrolled page. |
| "TCF is required for advertising" | TCF is required by specific ad-tech contracts, not by law. Sites without programmatic demand should not adopt it. See `tcf.md`. |

## Common mistakes

| Mistake | Why it is wrong |
|---|---|
| GTM loaded in `<head>`, banner blocks tags inside GTM | The GTM container itself is a third-party request and writes to the device |
| `type="text/plain"` swap done, but `preconnect`/`dns-prefetch` hints left in place | Resource hints open connections to the third party before any consent |
| Consent read from a cookie during SSR | Server does not know the client's state; renders the wrong tree and hydrates trackers |
| `document.write` used by a legacy tag after page load | Wipes the document; also defeats attribute-based blocking |
| Cookie banner script itself loaded from a third-party CDN | The consent tool must be first-party or strictly necessary, and must never be the first violation |
| Consent stored, banner version not stored | Old records become uninterpretable; proof under Art 7(1) collapses |
| Re-prompting on every page load after a refusal | Deceptive design pattern "Continuous prompting" (EDPB Guidelines 03/2022 v2.0 §4.1.1) |
| Reject button present but grey-on-grey | Cookie Banner Taskforce para 18: unreadable contrast on the alternative is manifestly misleading |
| Consent state kept only in memory | Lost on navigation; produces both re-prompting and accidental firing |
| Audit done by clicking around in one browser | Extensions, cache and prior consent contaminate the result; use a clean automated profile |

## Reference files

- `references/intake.md` — inventory and questions to answer before writing code
- `references/blocking-layer.md` — script type swapping, dynamic injection, CSP backstop, leak sources
- `references/embeds.md` — click-to-load for video, maps, social, scheduling; self-hosted fonts
- `references/consent-mode-google.md` — Consent Mode v2 signals, ordering, basic vs advanced
- `references/server-side-tagging.md` — sGTM, cookie lifetimes, ITP caps, CNAME cloaking
- `references/consent-record.md` — Art 7(1) proof, record shape, retention, re-prompt intervals
- `references/ui-rules.md` — enforcement-magnet UI rules and the EDPB do-not-build list
- `references/tcf.md` — IAB TCF mechanics, when it is needed, the IAB Europe case
- `references/gpc-us.md` — Global Privacy Control, US state opt-out signals, pixel litigation
- `references/frameworks.md` — Next.js App Router, Nuxt, SvelteKit, static; the SSR trap
- `references/audit.md` — runnable Playwright audit and the manual DevTools method
- `references/cmp-decision.md` — build versus buy, and what a hand-rolled banner must do
- `references/vendor-matrix.md` — third party to consent category to blocking technique
- `references/pre-ship.md` — pre-ship checklist ending in a network-level assertion
