# CMP versus hand-rolled

The question is not "is a banner hard to build". A banner is trivial. The question is what the banner must keep doing after launch, and who does that work.

## What a hand-rolled banner realistically must do

Everything below is a requirement, not a nice-to-have. If any line has no owner, the build-it decision is not yet made.

**Blocking**

1. Prevent every non-essential request before a decision, across markup, JS, CSS, iframes, workers and injected tags (`blocking-layer.md`).
2. Survive a new tag being added by someone who has not read this — CSP backstop plus CI assertion (`audit.md`).
3. Handle late-loading and idle-callback tags, not just the ones in the initial HTML.

**UI**

4. Reject on the first layer, visually equal to accept; no pre-ticked boxes; no nudging (`ui-rules.md`).
5. Granular per-category controls, with the categories matching the privacy notice.
6. Keyboard operable, focus-trapped, screen-reader labelled, contrast-compliant.
7. Localised into every language the site serves — "Language discontinuity" is a listed deceptive pattern.
8. Persistent reopen link on every route; reopened dialog shows current state.
9. Per-provider grants for click-to-load embeds, revocable individually.

**State and proof**

10. Durable storage of grants **and refusals**, first-party, surviving navigation and reload.
11. Server-side consent record with banner version, text version and code hash (`consent-record.md`).
12. Versioned, archived banner artefacts so old records stay interpretable.
13. Re-prompt interval respected per jurisdiction; no per-page-load prompting.
14. Withdrawal writes a record rather than deleting one.

**Signals**

15. Google Consent Mode default before update, all seven signals (`consent-mode-google.md`).
16. GPC read server-side and client-side, never as consent (`gpc-us.md`).
17. TCF only if contractually required — and if required, a certified CMP is effectively mandatory (`tcf.md`).

**Operations**

18. Vendor inventory kept current as marketing adds tools.
19. Cookie table in the policy kept in sync with the actual network trace.
20. Audit in CI, failing the build on regression.
21. Someone reads the CSP reports.

Items 18 to 21 are where hand-rolled implementations die. The code is a week; the maintenance is forever.

## When each answer is right

**Build it** when all of these hold:

- fewer than roughly ten third parties, and the list changes rarely;
- one or two languages;
- no programmatic advertising, so no TCF;
- a developer owns the site continuously and marketing cannot inject tags without review;
- the site is not a target for complaint campaigns.

Typical fit: a company site, a documentation site, a small shop with a fixed stack.

**Buy it** when any of these hold:

- programmatic advertising, so TCF and the Global Vendor List are in play;
- a tag manager that non-developers publish to;
- many locales;
- multiple domains or a group of brands needing consistent, auditable behaviour;
- regulated sector, or an entity that expects to be asked for proof;
- nobody owns items 18 to 21.

The honest framing for a stakeholder: a CMP is bought to outsource *maintenance and evidence*, not to outsource *blocking*. Blocking still has to be wired up in your code — which is why a CMP alone routinely fails the audit in `audit.md`.

## Categories of CMP, not a favourite

| Category | What it is | Trade-off |
|---|---|---|
| Tag-manager-native | A consent template running inside the tag manager, using its built-in consent checks | Cheapest path when everything already flows through the tag manager; controls nothing outside it |
| Standalone commercial CMP | Hosted banner, vendor database, auto-blocking by script scanning, consent logs, TCF support | Broadest coverage; auto-blocking is heuristic and needs verifying; introduces a third party that must itself load first |
| Open-source / self-hosted library | A banner and consent-store library you deploy | No extra vendor, no vendor lock-in; you still own maintenance items 18 to 21 |
| Platform-bundled | Consent features shipped with a CMS, shop platform or hosting provider | Zero integration effort; usually the weakest granularity and the least evidence |

Selection criteria that matter more than feature lists:

1. **Does it block, or only signal?** Ask for a network trace from their demo site with no interaction. If third-party hosts appear, it signals.
2. **Is the CMP script itself first-party or gated?** A CMP loaded from a vendor CDN before consent is a third-party request before consent. Some vendors offer a first-party proxy — ask.
3. **What exactly does the consent log contain?** If it lacks banner version and text version, it does not satisfy the proof requirement in `consent-record.md` on its own.
4. **Can you export the log?** If the records live only in the vendor's dashboard, you cannot produce evidence after you switch vendors.
5. **How does auto-blocking work?** Pattern matching on script sources breaks on bundled SDKs and on any tag whose host is not in their list. Verify against your own audit.
6. **Does it expose a stable API?** You need programmatic reads for `embeds.md` and `frameworks.md` integration, and events for state changes.
7. **Latency and failure mode.** If the CMP fails to load, the correct behaviour is deny — verify it, do not assume it.

## Migration note

Switching CMPs invalidates nothing legally if the categories and wording are unchanged, but it usually changes the storage key and the record format. Plan for: export old records, keep them readable, map old categories to new ones explicitly, and bump the banner version because the UI changed.

## Checkpoints

- [ ] The 21 requirements above each have a named owner
- [ ] Build/buy decision recorded with the reason
- [ ] If buying: vendor's demo site audited with `audit.md` before signing
- [ ] CMP script served first-party or verified as gated
- [ ] Consent log content checked against `consent-record.md` field list
- [ ] Log export path confirmed
- [ ] Auto-blocking verified against the project's own vendor list, not trusted
- [ ] Failure mode on CMP load error verified as deny
- [ ] CI audit in place regardless of build or buy
