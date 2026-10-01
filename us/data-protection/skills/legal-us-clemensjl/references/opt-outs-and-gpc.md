# Opt-outs and the Global Privacy Control

Status as at 2026-08-05.

The US analogue to the EU consent banner is not a banner. It is an **opt-out**: a link, a request channel, and a browser signal the site must detect and act on. In the states that mandate it, honouring the signal is not optional and is not satisfied by a preference centre nobody visits. This is the single most testable compliance obligation in US privacy law, and the one most often shipped broken.

## What an opt-out preference signal is

A **universal opt-out mechanism** (UOOM), also called an **opt-out preference signal**, is a machine-readable statement of the user's choice sent by the browser or an extension. In practice it means the **Global Privacy Control (GPC)**, transmitted as the HTTP header `Sec-GPC: 1` and exposed to script as `navigator.globalPrivacyControl === true`.

The signal is not a cookie preference. It is a legal exercise of the right to opt out of sale, sharing, and in most states targeted advertising, made by the consumer without visiting the site's own interface. Detecting it and continuing to fire advertising tags is a violation on its face, whatever the banner says.

## Where it is mandatory — verified

| Jurisdiction | Authority | Position |
|---|---|---|
| California | Cal. Civ. Code § 1798.135(b), with the CCPA regulations at 11 CCR § 7001 et seq. | A business may comply with the opt-out obligation by honouring an opt-out preference signal "sent with the consumer's consent by a platform, technology, or mechanism", in the manner set out in the regulations. Under the regulations, processing the signal is required; the statutory choice is only whether the business may **also** rely on it in place of posting the links. Treat honouring GPC as mandatory. |
| Colorado | C.R.S. § 6-1-1306(1)(a)(IV); CPA Rules, 4 CCR 904-3 Rule 5.07 | **Mandatory since 1 July 2024.** The Attorney General maintains the official public list of recognised universal opt-out mechanisms at `coag.gov/uoom`. As at 2026-08-05 the list contains exactly one entry: **Global Privacy Control**. Privacy-policy disclosure of how the business responds is required by 4 CCR 904-3 Rule 6.03(4)(e). |
| Texas | Tex. Bus. & Com. Code § 541.055(e)–(f) | A consumer may designate an authorized agent through "a link to an Internet website, an Internet browser setting or extension, or a global setting on an electronic device". The controller must comply where it can verify the consumer's identity and the agent's authority with commercially reasonable effort. § 541.055(f) requires the technology to make the consumer's choice "affirmative, freely given, and unambiguous" and to be easy to use. In force since 1 July 2024. |

The Colorado AG's list is the practical reference point for the whole country: if a new mechanism is ever recognised, it will appear there first.

**States imposing the duty, with start dates:** California (11 CCR § 7025(b)), Colorado (1 July 2024), Connecticut (1 January 2025), Texas (§ 541.055(e), authorized-agent framing), Montana (1 January 2025), New Hampshire (1 January 2025), New Jersey (15 July 2025), Minnesota (31 July 2025), Delaware (1 January 2026), Oregon (1 January 2026). `[[UNVERIFIED: each individual start date except California, Colorado and Texas — verify against the state's statute or regulations before putting a date in client-facing text. Texas sources differ on whether the duty began with the act on 1 July 2024 or on 1 January 2025.]]`

**Two states that do NOT impose a duty to honour a signal**, and are commonly listed as if they did:

- **Maryland** — § 14-4607(f)(3) treats a universal opt-out mechanism as an **alternative compliance method**, not a mandatory one.
- **Nebraska** — the Data Privacy Act contains no universal opt-out mechanism at all. The words "universal opt-out mechanism" and "opt-out preference signal" do not appear in it. Neb. Rev. Stat. § 87-1111(5)–(6) uses the **authorized-agent** model instead: a consumer may designate an agent "using a technology, including a link to an Internet website, an Internet browser setting or extension, or a global setting on an electronic device". Operative since 1 January 2025.

**Scope differs from state to state and this matters for the build.** New Jersey (N.J.S.A. § 56:8-166.11(b)(1)) and Nebraska (§ 87-1107(2)(e)) extend the signal only to **targeted advertising and sale** — **profiling is excluded**. A signal handler that also suppresses profiling is harmless; one that assumes the signal covers everything, and therefore stops maintaining a separate profiling opt-out, is not.

`[[UNVERIFIED: whether California has enacted a statute requiring browsers themselves to offer an opt-out preference signal. A bill on this was introduced; verify its current status rather than assuming.]]`

`[[UNVERIFIED: whether the New Jersey Division of Consumer Affairs has adopted UOOM technical specifications under N.J.S.A. § 56:8-166.11(c), and which mechanisms it recognises. Check the New Jersey Register and N.J.A.C. 13:45.]]`

## Building it correctly

1. **Detect on every request**, server side and client side. Read the `Sec-GPC` request header and `navigator.globalPrivacyControl`. Do not rely on a consent platform's default configuration — most ship with GPC handling off or limited to one jurisdiction.
2. **Apply it before the first advertising or analytics request fires**, not after page load. A tag that fires and is then "opted out" downstream has already transmitted the data.
3. **Apply it to the identified user too**, where the visitor is logged in. The signal opts out the consumer, not the browser session. Persist the choice to the account.
4. **Propagate to platforms.** Meta, Google, TikTok and the rest each have a restricted-data-processing or limited-data-use flag. Setting a local cookie without flipping the platform flag stops nothing.
5. **Do not ask for confirmation.** A dialog that says "we detected a signal, are you sure?" is a dark pattern; under the California regulations a dark-pattern interface does not produce valid consent, and here it does not produce a valid retraction of the opt-out either.
6. **Do not let the signal be overridden by an "accept all" banner click** unless the consumer separately and deliberately chose to. A banner that treats any interaction as consent, over a GPC signal, is the classic failure.
7. **Log it.** Record that the signal was seen and what was suppressed. A compliance claim you cannot evidence is not a defence.
8. **Disclose it.** State in the privacy policy whether the business honours GPC. Colorado requires the disclosure by rule; California requires the treatment of the signal to be described; CalOPPA separately requires a Do Not Track response disclosure, which is a different, older signal — answer both.

## Detection — the minimum implementation

```js
// Client side. Read before any tag manager or advertising script initialises.
const gpc = navigator.globalPrivacyControl === true;

// Server side (Node/Express example). The header is the authoritative signal
// for the first request, before any script runs.
//   req.get('Sec-GPC') === '1'
//
// Treat either as an opt-out of sale, sharing and targeted advertising, and
// suppress the corresponding tags for the whole response — do not load them
// and then "opt out" afterwards.
```

The signal must be consulted **before** the tag container initialises, which usually means server-side rendering of the container decision or a synchronous check ahead of the container script. A consent platform configured to evaluate GPC after page load has already leaked the request.

## The other opt-outs

The signal does not discharge the rest. Depending on the states in scope, the business must also provide:

- an opt-out of the **sale** of personal data;
- an opt-out of **sharing for cross-context behavioural advertising** or **targeted advertising** (the label differs by state);
- an opt-out of **profiling** in furtherance of decisions producing legal or similarly significant effects;
- in California, a right to **limit the use and disclosure of sensitive personal information** (Cal. Civ. Code § 1798.121), with its own link;
- a route for an **authorised agent** to submit requests on the consumer's behalf.

Opting out must be at least as easy as opting in, must not require an account, and must not be conditioned on providing more information than is needed to process the request.

## Testing it

Testing this takes five minutes and finds real defects in most implementations:

1. Install a GPC-enabled browser or extension, or send `Sec-GPC: 1` manually.
2. Load the site cold, network tab recording. Note every advertising and analytics request.
3. Confirm the requests that constitute a sale or share are absent, not merely flagged.
4. Confirm in each ad platform's own interface that the restricted-processing flag was received.
5. Log in and repeat. Confirm the opt-out persisted to the account.
6. Click the opt-out link with no GPC signal. Confirm the same suppression occurs and that a record is written.

## Checkpoints

- [ ] `Sec-GPC` header and `navigator.globalPrivacyControl` both read
- [ ] Signal applied before any advertising or analytics request is issued
- [ ] Platform-side restricted-processing flags actually set, verified in the platform console
- [ ] Signal persisted to the logged-in account, not just the browser
- [ ] No confirmation dialog, and no banner click silently overriding the signal
- [ ] Opt-out link present and functional independently of the signal
- [ ] Sensitive-information limitation link present where California applies
- [ ] Authorised agent route available
- [ ] Treatment of the signal disclosed in the privacy policy, alongside the separate CalOPPA Do Not Track disclosure
- [ ] Handling verified against the Colorado AG's current recognised-UOOM list, not against an assumption
- [ ] Log of signals seen and processing suppressed, retained
