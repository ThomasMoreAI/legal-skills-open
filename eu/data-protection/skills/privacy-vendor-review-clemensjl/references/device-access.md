# Question 5 — device access, consent gating, CMP category

This is the single most common vendor-review error: treating the consent question as a *cookie* question, and treating it as a *personal data* question. It is neither.

**Art 5(3) Directive 2002/58/EC (ePrivacy):** Member States shall ensure that "the storing of information, or the gaining of access to information already stored, in the terminal equipment of a subscriber or user" is only allowed on condition that the user has given consent, having been provided with clear and comprehensive information — subject to two exemptions: transmission of a communication over an electronic communications network, or strict necessity for a service explicitly requested by the user.

The rule bites on **information**, not personal data, and on **storage or access**, not cookies. Applies in parallel with the GDPR: the ePrivacy consent is required *in addition to* an Art 6 GDPR basis for whatever happens with the data afterwards.

National transposition decides the exact wording and the enforcing authority. In Austria the transposition is **§ 165 Abs 3 TKG 2021**.

Status as at 2026-08-05.

## What the EDPB actually said

**EDPB Guidelines 2/2023 on Technical Scope of Art. 5(3) of ePrivacy Directive, Version 2.0, adopted 7 October 2024.** Three cumulative criteria (para 6):

- **Criterion A** — the operations relate to *information*. Para 6: "It should be noted that the term used is not 'personal data', but 'information'." Para 12: "the notion of information includes both non-personal data and personal data, regardless of how this data was stored and by whom".
- **Criterion B** — the operations involve *terminal equipment* of a subscriber or user (B.1), connected or connectable to a public communications network (B.2). Para 17: not limited to a physically enclosed device — smartphones, laptops, NAS, connected cars, connected TVs, smart glasses.
- **Criterion C** — the operations constitute *storage* (C.1) or a *gaining of access* (C.2). The two are alternative, and para 6 notes they need not be performed by the same party.

The CJEU statement the guidelines rely on (para 10, quoting Planet49, CJEU 01.10.2019, C-673/17): "That protection applies to any information stored in such terminal equipment, **regardless of whether or not it is personal data**".

Consequences the guidelines spell out:

- **Read-only access counts.** Quoting WP29 Opinion 9/2014: it is not correct to say a third party needs no consent because it did not store the information. Reading an existing value is access.
- **Instructing the device to generate and send information counts as storage** (para 36), including via established protocols such as browser cookie storage, and regardless of who created or installed the software.
- **No minimum duration or size** (para 37). `sessionStorage`, a single ETag, an in-memory value written to RAM — all within scope.
- **Purely local use is out of scope, until it leaves** (para 44): an application using information strictly inside the device is not "gaining access" — but "when this information or any derivation of this information is accessed, Article 5(3) ePD would apply". This is the test for on-device AI, local fingerprint computation and client-side scoring: the derivation leaving the device is the trigger.
- **Routing, session and protocol identifiers are in scope** (paras 42-43): MAC and IP addresses, session identifiers, authentication tokens, HTTP header context data such as `user-agent` and `accept`, ETag caching, HSTS — relied on for fingerprinting or resource tracking, they trigger Art 5(3).

Use cases analysed in section 3: **URL and pixel tracking; local processing; tracking based on IP only; intermittent and mediated IoT reporting; unique identifier.** The list is expressly non-exhaustive.

## Applying it to a vendor claim

| Vendor claim | Assessment |
|---|---|
| "Cookieless — we use localStorage" | In scope. Storage of information on terminal equipment. |
| "No cookies, we fingerprint" | In scope, and doubly so: reading `user-agent`, fonts, canvas and screen metrics is gaining access (paras 43, WP29 Opinion 9/2014). |
| "Only a 1×1 tracking pixel" | In scope. Section 3.1 addresses pixel tracking directly. |
| "We only log the IP server-side" | Section 3.3 analyses IP-only tracking. Where the IP is obtained by instructing the terminal to establish a connection it would not otherwise make, Art 5(3) is engaged. Assess the specific mechanism, do not assume either way. |
| "The computation happens on the device" | Out of scope only while nothing leaves. The moment the result or any derivation is transmitted, in scope (para 44). |
| "It is first-party" | Irrelevant. Art 5(3) does not distinguish first from third party. |
| "It is anonymous" | Irrelevant to Art 5(3). Criterion A is information, not personal data. |
| "Consent Mode / consent signals are enabled" | A signal sent to the vendor is not the same as not contacting the vendor. Verify with the capture in `data-inventory.md` whether the request still fires. |

## The two exemptions, applied honestly

Art 5(3) second sentence exempts storage or access that is (i) for the sole purpose of carrying out the transmission of a communication over an electronic communications network, or (ii) **strictly necessary** in order for the provider of an information society service **explicitly requested by the subscriber or user** to provide that service.

"Strictly necessary" is measured against the service *the user asked for*, not the service you want to run. Reliable outcomes:

| Purpose | Exempt? |
|---|---|
| Session cookie, authentication token, CSRF token | Yes |
| Shopping cart, load balancing, user-interface state the user set (language, dark mode) | Yes |
| Consent-record storage itself | Yes |
| Security: rate limiting, bot detection needed to deliver the requested service | Generally yes; document the necessity and keep it narrow |
| Audience measurement / analytics | No, by default. Some authorities operate a narrow exemption for strictly first-party, non-shared audience measurement under conditions; that is a national position and must be checked against the local authority before relying on it. |
| Error and crash telemetry | No. Useful to you, not requested by the user. |
| Session replay, heatmaps, scroll tracking | No |
| A/B testing and personalisation | No |
| Marketing pixels, conversion tracking, remarketing | No |
| Embedded video, maps, fonts, captcha loaded from a third-party host | No, unless the user actively requested the specific embedded content |

## Consent quality, briefly

Consent under Art 5(3) is GDPR consent (Art 2(f) ePrivacy refers to Directive 95/46, read via Art 94(2) GDPR as Art 4(11) GDPR). So: freely given, specific, informed, unambiguous, by a clear affirmative act; as easy to withdraw as to give (Art 7(3)); pre-ticked boxes and scrolling do not qualify (Planet49, C-673/17). Refusal must be available at the same level and with the same effort as acceptance — the position taken by every EU authority that has ruled on banner design, and the basis of the pending cookie-banner complaint stream at the EDPB (see `enforcement.md`).

For consent-or-pay walls, see `enforcement.md`; that is a business-model question, not a vendor question, and it does not change whether the vendor's tag needs consent.

## Consent-manager category assignment

Assign per **purpose**, not per vendor, and record the reasoning. If the vendor serves two purposes, it appears twice.

| Category | Contents | Gate |
|---|---|---|
| Strictly necessary | Only what survives the table above | Loads before any interaction; no opt-out offered |
| Functional / preferences | User-set state that is not strictly necessary | Blocked until opted in |
| Analytics / performance | Product analytics, error telemetry, session replay, heatmaps | Blocked until opted in |
| Marketing / advertising | Pixels, conversion APIs, remarketing, ad measurement | Blocked until opted in |

Implementation findings to record:

- The tag is **not loaded** before consent, rather than loaded and told not to fire. A blocked script is a network request that never happens.
- Tag managers are themselves gated or configured so that no downstream tag fires pre-consent. A tag manager container that loads pre-consent and then loads tags is the most common leak.
- Third-party embeds use a click-to-load placeholder, not an autoloading iframe.
- The banner does not load anything on dismissal or on scroll.
- Consent is logged with a timestamp, the banner/policy version, the categories chosen, and the mechanism for withdrawal — Art 7(1) requires you to be able to demonstrate consent.
- Withdrawal is reachable permanently, not only on first visit.

## Watch item — the consent-signal proposal

The Commission's Digital Omnibus package proposed a new **Art 88b** that would replace site-level banners with an automated, machine-readable consent signal exchanged between the device, the user and the website, still on a per-site and per-purpose basis. **It is not law.** The Council's position paper of 18.06.2026 removed Art 88b entirely, with Germany, France and Poland opposed; the Parliament had not adopted a position and the trilogue was still open (`noyb.eu/en/eu-member-states-and-google-suddenly-want-keep-cookie-banners`, 23.06.2026 — advocacy source reporting the institutional positions).

Consequence for a review today: **nothing changes.** Design the gate to Art 5(3) as it stands. Do not defer a consent implementation on the strength of a proposal that the Council has already stripped out, and re-check the state of play before quoting it to anyone.

## Non-EU exposure on the same tags

US state wiretap and pen-register claims (California Invasion of Privacy Act §§ 631 and 638.51) target the same pixels and session-replay scripts, independently of the GDPR. Where the product has US visitors, the consent gate is also the mitigation there. Detail and citations in `enforcement.md`.

## Checkpoints

- [ ] Art 5(3) assessed on the basis of *information*, not personal data
- [ ] Storage **and** access both considered, including read-only access to existing values
- [ ] localStorage, sessionStorage, IndexedDB, Cache API, service workers and ETag/HSTS mechanisms all inspected, not only cookies
- [ ] Fingerprinting assessed as access, not dismissed as "no storage"
- [ ] For on-device processing: verified whether any result or derivation leaves the device
- [ ] Exemption claim, if any, written out against the service the user explicitly requested
- [ ] National transposition identified (for Austria: § 165 Abs 3 TKG 2021)
- [ ] Category assigned per purpose, with the reasoning recorded
- [ ] Pre-consent capture from `data-inventory.md` shows zero requests to the vendor
- [ ] Tag manager itself gated; no downstream tag fires pre-consent
- [ ] Consent log records timestamp, version, categories, withdrawal path
- [ ] Withdrawal permanently reachable and no harder than granting
