---
name: consent-and-tracking-arttuan
title: Consent and Tracking
description: Inventory everything that touches the user's device, decide what is strictly necessary, and build a consent mechanism that actually gates the scripts
author: ArttuAn
author_url: https://github.com/ArttuAn/eu-compliance-skills/tree/main/skills/consent-and-tracking
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# Consent and Tracking

The most commonly broken rule in European software, and the one with the
cheapest fix if you do it before launch. ePrivacy Art. 5(3) requires consent
before **storing or accessing information on a user's terminal equipment**,
unless it is strictly necessary to provide the service the user explicitly
requested.

Two things make this go wrong. It is much broader than cookies — `localStorage`,
pixels, third-party fonts, SDK identifiers and fingerprinting are all in scope.
And most consent banners do not actually gate anything: the analytics script is
in the page, it runs on load, and the banner sets a flag afterwards.

The engineering test is simple and brutal: **open the site in a clean browser,
click nothing, and look at the network tab and the storage inspector.** Whatever
happened there, happened without consent.

> **Not legal advice.** Whether a given technology is strictly necessary, and
> whether a consent flow is valid, are legal judgements — and national
> authorities differ. This skill produces the inventory, the gating and the
> evidence.

```
  clean browser · click nothing
        │
        ▼
  inventory: every cookie · storage key · network call · pixel · font
        │
        ▼
  strictly necessary?  ──yes──► may run before consent (document why)
        │ no
        ▼
  blocked until an affirmative signal  ──► and rejecting is as easy as accepting
        │
        ▼
  withdrawal actually stops it · consent record kept (Art. 7(1))
```

## Use this when

- Before the first analytics, error-tracking, session-replay, A/B testing, chat
  widget, map, embedded video or web font ships.
- Before a mobile SDK that sets an advertising or device identifier is added.
- When a cookie banner exists but nobody has verified it gates anything —
  which is the normal state.

**Do not use this when** the product genuinely writes nothing to the device
beyond a session cookie needed to log in, and loads nothing from a third-party
origin. Verify that in a browser rather than accepting it; a self-hosted font is
a different answer from a Google Font.

## Ask first

Do the inventory yourself first, then ask about what you cannot see from
outside.

1. **"Open the site in a private window, click nothing, and tell me what is in
   Application → Storage and in the Network tab."**
   Or do it yourself with a headless browser. This is the ground truth and it
   frequently contradicts what the team believes.
2. **"For each of these, what breaks for the user if it is not there?"**
   The strictly-necessary test, asked as an engineering question. "We lose
   analytics" means not necessary.
3. **"Is rejecting as easy as accepting — same number of clicks, same
   prominence, same layer?"**
   A "Reject all" button hidden behind "Manage preferences" is the single most
   common finding.
4. **"When someone withdraws consent, what actually stops? Show me."**
   Usually nothing stops — the flag changes and the script stays loaded.
5. **"Do you keep a record of who consented, to what, and when?"**
   Art. 7(1) GDPR requires you to be able to demonstrate it.
6. **"Does any of this run on mobile? Which SDKs, and what identifiers do they
   set?"**
   The mobile side is usually scoped separately and usually forgotten.

## What the law requires

**ePrivacy Directive 2002/58/EC Art. 5(3)** — consent before storing or gaining
access to information stored on a user's terminal equipment, except where
strictly necessary for a service explicitly requested by the user. Transposed
nationally, so enforcement and detail vary by Member State.

**The consent standard is GDPR's** (Arts. 4(11), 7): freely given, specific,
informed, unambiguous, and given by a clear affirmative action. Which rules out:

- Pre-ticked boxes, implied consent, "by continuing to browse you agree".
- Bundled consent covering several purposes in one click.
- Consent that cannot be withdrawn as easily as it was given (Art. 7(3)).

**EDPB Guidelines 2/2023 on Art. 5(3)** confirm the scope extends well beyond
cookies: URL and pixel tracking, local processing instructions, IP-only
tracking in some configurations, and identifiers in mobile apps.

**Where consent is also the GDPR basis for the subsequent processing**, you need
both — the Art. 5(3) consent to store, and an Art. 6 basis to process what you
collected. They are usually the same consent event; they are not the same
requirement.

### Strictly necessary — the short list

Necessary for a service *the user explicitly requested*:

- Session and authentication cookies.
- Security tokens: CSRF, fraud prevention, rate limiting.
- Load balancing and session affinity.
- User-interface state the user chose: language, dark mode, cookie preference
  itself.
- Shopping-cart contents.

**Not** strictly necessary, however routine:

- Analytics of any kind, including privacy-focused and self-hosted ones. (Some
  national authorities have signalled leniency for strictly anonymous,
  first-party, non-tracking measurement — **that is a national question, verify
  it, do not assume it.**)
- Error tracking and session replay.
- A/B testing.
- Advertising, retargeting, conversion pixels.
- Third-party fonts, maps and embedded video — these disclose the user's IP to a
  third party on load.
- Chat widgets, unless the user opened the chat.

### Dark patterns

EDPB Guidelines 03/2022, DSA Art. 25 where it applies, and the Unfair Commercial
Practices Directive all converge on the same thing:

- Reject must be **equally easy** — same layer, same click count, comparable
  visual weight.
- No pre-selection of non-essential purposes.
- No nagging: re-asking after a refusal, in a short window, undermines "freely
  given".
- "Pay or consent" models are under active scrutiny (EDPB Opinion 08/2024) —
  treat as a legal question, not a design choice.

## What to produce

**1. The inventory**, generated from a real browser session, not from a
spreadsheet:

```python
async def inventory(url: str) -> list[dict]:
    """Load with a clean profile, interact with nothing, record everything."""
    async with browser(clean_profile=True) as page:
        requests = []
        page.on("request", lambda r: requests.append(
            {"url": r.url, "origin": origin_of(r.url), "type": r.resource_type}))
        await page.goto(url, wait_until="networkidle")
        storage = await page.evaluate("""() => ({
            cookies: document.cookie,
            local: Object.keys(localStorage),
            session: Object.keys(sessionStorage),
        })""")
        return classify(requests, storage, first_party=origin_of(url))
```

Run it in CI against the deployed site. **The failing condition is any
third-party request or any non-essential storage key before consent** — that is
the whole test, and it is objective.

**2. A classification table**, one row per item, with the necessity decision and
its reasoning:

```yaml
- name: "_ga"
  kind: cookie
  set_by: "Google Analytics (third party, US)"
  purpose: "audience measurement"
  strictly_necessary: false
  necessity_reasoning: "the service functions fully without it"
  gated: true
  gate_implementation: "loaded by consent-manager after 'analytics' opt-in"
  retention: "2 years"
  transfer: {country: US, mechanism: scc, tia: "compliance/vendors/google-tia.md"}
  source: {kind: inferred, reasoning: "observed in a clean-profile page load"}
```

**3. Gating that actually gates.** The script must not be in the page until
consent exists:

```html
<!-- WRONG: the script runs, then checks a flag it set itself -->
<script src="https://cdn.example/analytics.js"></script>

<!-- RIGHT: nothing is fetched until an affirmative signal -->
<script type="text/plain" data-consent="analytics"
        data-src="https://cdn.example/analytics.js"></script>
```

The consent manager promotes `text/plain` to a real script tag only after the
user opts in. Anything that loads at parse time and checks a flag afterwards has
already contacted a third party and disclosed the user's IP.

**4. Withdrawal that stops things.** On withdrawal: stop the collectors, delete
the cookies and storage keys you set, call the vendor's deletion endpoint where
one exists, and record the withdrawal. A flag flip with no teardown is not
withdrawal.

**5. A consent record** for Art. 7(1): a per-user record of what was consented
to, when, the version of the notice shown, and the mechanism. Version your
notice — a consent given against a notice that has since changed does not cover
the new purposes.

**6. A CI test**, which is what keeps this from regressing the first time
someone adds a marketing tag:

```python
async def test_nothing_non_essential_before_consent(deployed_url):
    items = await inventory(deployed_url)
    violations = [i for i in items if not i["strictly_necessary"]]
    assert not violations, f"fired before consent: {[v['name'] for v in violations]}"
```

**Every assessment carries a certainty.** Each finding, each applicable or
ruled-out regime, and the headline of the brief carry `certainty` (0–100) — the
honest percent of the assessment that rests on verified sources and confirmed
facts rather than inference, open unknowns and interpretation. Wherever you
state an applicability, a classification, a citation-backed obligation or a
finding, show the percentage **and the single largest reason it is not higher**:
"ruled out NIS2 — certainty 66%: the national transposition was not read".
`references/certainty.md` holds the anchors; the rules that matter here: an
answer graded `UNKNOWN` caps anything resting on it at 70, an unread Directive
transposition caps at 60, a classification pending counsel caps at 50, and a
`100` requires every deciding fact SPECIFIC, every citation verified on EUR-Lex,
every transposition read and every regime screened. Certainty is visibility, not
a free pass — VAGUE stays rejected, an open blocker stays blocked.

## Failure modes

- **The banner does not gate.** The most common finding by a wide margin.
  Scripts load at parse time; the banner sets a flag afterwards. Test in a clean
  browser, always.

- **"Reject all" behind a second click.** Equal ease is the requirement, and
  this is the easiest thing for a regulator to check from the outside.

- **Third-party fonts, maps and embeds not counted.** Loading them discloses the
  user's IP address to the third party before any consent. A self-hosted font
  ends the problem entirely.

- **Analytics assumed exempt because it is privacy-focused.** Some national
  authorities have signalled leniency for narrowly-scoped first-party
  measurement; that is a national question with conditions attached. Verify it
  for your Member States rather than treating it as settled.

- **Consent bundled with terms acceptance.** Not specific, not freely given, and
  it contaminates the terms too.

- **Withdrawal that only flips a flag.** The collectors keep running. Tear down
  and delete.

- **No consent record.** Art. 7(1) requires you to demonstrate it. "The banner
  was up" is not a demonstration.

- **Mobile forgotten.** SDK identifiers, ATT on iOS, advertising IDs. Same rules,
  different surface, usually scoped separately and then not scoped at all.

- **Re-asking after a refusal.** Nagging undermines "freely given". Respect the
  refusal for a meaningful period.

## Verify

Follow `references/verification.md`. For this skill specifically:

1. **Tier 0** — install, `--help`, run the inventory against a fixture page.

2. **Tier 1** — `pytest -q`, offline against recorded sessions:

```python
def test_clean_load_fires_nothing_non_essential(recorded_session):
    assert [i for i in classify(recorded_session) if not i.strictly_necessary] == []


def test_third_party_font_is_not_strictly_necessary():
    item = classify_one(request("https://fonts.gstatic.com/s/inter.woff2"))
    assert item.strictly_necessary is False
    assert "discloses the user's IP" in item.necessity_reasoning


def test_analytics_is_never_classified_strictly_necessary():
    for name in ("_ga", "_hjSession", "mp_mixpanel", "plausible_ignore"):
        assert classify_one(cookie(name)).strictly_necessary is False


def test_session_cookie_is_strictly_necessary():
    assert classify_one(cookie("sid", first_party=True, session=True)).strictly_necessary


def test_reject_is_as_easy_as_accept(banner_dom):
    accept, reject = find_buttons(banner_dom)
    assert reject is not None
    assert reject.layer == accept.layer          # same layer, not behind "manage"
    assert reject.clicks_to_reach == accept.clicks_to_reach


def test_no_purpose_is_preselected(banner_state):
    assert all(not p.checked for p in banner_state.purposes if not p.essential)


def test_script_is_not_fetched_before_opt_in(page_fixture):
    assert "analytics.js" not in [r.url for r in page_fixture.requests_before_consent]


def test_withdrawal_tears_down(consent_manager, stores):
    consent_manager.grant("analytics")
    consent_manager.withdraw("analytics")
    assert stores.cookies_matching("_ga*") == []
    assert not consent_manager.collectors_running("analytics")
    assert consent_manager.vendor_deletion_called("analytics")


def test_consent_record_captures_notice_version(consent_manager):
    record = consent_manager.grant("analytics")
    for field in ("purposes", "granted_at", "notice_version", "mechanism"):
        assert getattr(record, field)


def test_notice_version_bump_invalidates_old_consent(consent_manager):
    consent_manager.grant("analytics")
    consent_manager.publish_notice(version="2026-10-01", adds_purpose="advertising")
    assert consent_manager.has_valid_consent("advertising") is False


def test_refusal_is_respected_for_a_period(consent_manager):
    consent_manager.reject_all()
    assert consent_manager.should_show_banner() is False
```

3. **Tier 2** — report, from a real clean-browser run: items fired before
   consent (must be zero), third-party origins contacted before consent (must be
   zero), click counts for accept versus reject, and whether withdrawal was
   observed to stop collection.

4. **Tier 3** — have someone open the deployed site in a private window with the
   network tab open and watch. This takes two minutes and finds more than any
   document review.

Then tell the user which necessity classifications rest on your reading rather
than confirmed advice — the analytics one especially, since it varies by Member
State — and name the national positions you could not verify.
