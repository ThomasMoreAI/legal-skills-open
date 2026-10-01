# Google Consent Mode v2

Authoritative basis: Google's tag platform documentation (`developers.google.com/tag-platform/security/guides/consent`, `/security/concepts/consent-mode`, `/tag-manager/templates/consent-apis`) and Google Analytics Help 9976101. Status as at 2026-08-05. Verify the API surface again before shipping — Google has changed it twice since 2023.

## The seven consent types

Google's Tag Manager consent API documents seven, with these descriptions:

| Signal | Google's description |
|---|---|
| `ad_storage` | "Enables storage, such as cookies, related to advertising." |
| `ad_user_data` | "Sets consent for sending user data to Google for online advertising purposes." |
| `ad_personalization` | "Sets consent for personalized advertising." |
| `analytics_storage` | "Enables storage, such as cookies, related to analytics (for example, visit duration)." |
| `functionality_storage` | "Enables storage that supports the functionality of the website or app such as language settings." |
| `personalization_storage` | "Enables storage related to personalization such as video recommendations." |
| `security_storage` | "Enables storage related to security such as authentication functionality, fraud prevention, and other user protection." |

The gtag.js reference documents only the four advertising and analytics signals plus `wait_for_update`; the other three are consumed by tag templates. Send all seven anyway — an unset signal is not the same as a denied one for every consumer.

Map them to your categories explicitly, and record the mapping in the consent record (`consent-record.md`):

| Your category | Signals granted |
|---|---|
| strictly necessary | `security_storage` (always granted) |
| functional | `functionality_storage`, `personalization_storage` |
| analytics | `analytics_storage` |
| marketing | `ad_storage`, `ad_user_data`, `ad_personalization` |

## Default before update

```html
<!-- FIRST script on the page. Before gtag.js, before GTM, before the CMP. -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}

  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    functionality_storage: 'denied',
    personalization_storage: 'denied',
    security_storage: 'granted',
    wait_for_update: 500
  });
</script>
```

After the user decides:

```js
gtag('consent', 'update', {
  ad_storage: c.marketing ? 'granted' : 'denied',
  ad_user_data: c.marketing ? 'granted' : 'denied',
  ad_personalization: c.marketing ? 'granted' : 'denied',
  analytics_storage: c.analytics ? 'granted' : 'denied',
  functionality_storage: c.functional ? 'granted' : 'denied',
  personalization_storage: c.functional ? 'granted' : 'denied',
  security_storage: 'granted'
});
```

Google's own warning on ordering: "The order of the code here is vital. If your consent code is called out of order, consent defaults won't work."

- `wait_for_update` takes **milliseconds**; Google's example uses `500`. It tells the tag how long to hold measurement while an asynchronous CMP resolves. Omit it and a slow CMP loses the update entirely.
- `region` scopes a default to territories using ISO 3166-2 codes, e.g. `region: ['ES', 'US-AK']`. A regional default overrides the global default for matching users. Do not use regional defaults to grant by default outside the EEA unless the US analysis in `gpc-us.md` supports it.
- `ads_data_redaction: true` redacts ad click identifiers while `ad_storage` is denied. `url_passthrough: true` carries ad and session information in URL parameters when cookies are denied. Both are Google measurement features, not consent mechanisms — enabling them does not change what may be loaded.

Inside Google Tag Manager, template code uses `setDefaultConsentState` and `updateConsentState` rather than the gtag commands; Google's template documentation states this is because of processing-queue timing. If your CMP is a GTM template, use the template APIs.

## Basic versus advanced

Google's definitions, quoted:

- **Basic**: "you prevent Google tags from loading until a user interacts with a consent banner"; "This setup transmits no data to Google prior to user interaction with the consent banner."
- **Advanced**: "Google tags load when a user opens the website or app"; "While consent is `denied`, the Google tags send measurements without cookies."

Those cookieless pings, per Google Analytics Help 9976101, may include: user agent, screen resolution, IP address, timestamp, referrer, a boolean consent state, and a random number generated on each page load.

**The legal reading.** Advanced mode loads a third-party script before any consent decision. Under EDPB Guidelines 2/2023 v2.0 paras 50–51 that is already storage (cache) and gaining of access (identifier collection), so Article 5(3) ePD is engaged and, absent an exemption, consent was required before it happened. The pings additionally transmit an IP address that originates from the terminal equipment — the exact situation the Guidelines address at §3.3, where they conclude Article 5(3) applies "unless the entity can ensure that the IP address does not originate from the terminal equipment of a user or subscriber".

**When advanced mode is defensible.** Only outside the scope of Article 5(3) — for traffic from jurisdictions with no prior-consent rule, scoped with `region`. Inside the EEA and the UK, treat advanced mode as a violation with better modelling. If a stakeholder wants advanced mode for conversion modelling, the honest framing is: it improves reporting, it increases legal exposure, and the decision is not the developer's to make. Escalate it, do not implement it silently.

Basic mode is the implementation that matches the core principle: the tag is blocked by `blocking-layer.md`, and Consent Mode signals then tell Google what the user chose.

## Deadlines

| Date | What changed | Source |
|---|---|---|
| November 2023 | `ad_user_data` and `ad_personalization` added to consent mode | Google tag platform consent guide |
| March 2024 | For EEA users, both `ad_user_data` and `ad_personalization` must be `GRANTED` for Customer Match lists to be usable; missing or `UNSPECIFIED` consent is treated as not consented and the data cannot be used for personalisation | Google Ads Help 14310715 |

`[[UNVERIFIED: any Google Consent Mode deadline after March 2024 — Google's help pages consulted on 2026-08-05 list no later enforcement date; re-check the EEA consent requirements page before relying on this.]]`

## Verifying it works

Signals are easy to get wrong silently. Check all three of these, in this order:

1. **Network.** With no interaction, there must be no request to `googletagmanager.com`, `google-analytics.com`, `googleadservices.com`, `doubleclick.net`, `google.com/ads`. If there is, the block failed and consent mode is irrelevant.
2. **`dataLayer`.** In the console, `dataLayer.filter(x => x[0] === 'consent')` must show the `default` entry before any tag entry, and exactly one `update` per decision.
3. **Tag behaviour.** After granting, GA4 requests carry `gcs=G1` style consent state parameters. `gcs=G100` means both storage signals denied; `G111` means both granted. Compare against what the user actually chose.

## Checkpoints

- [ ] `consent default` is the first executed script on the page
- [ ] All seven signals set in `default`, everything except `security_storage` denied
- [ ] `wait_for_update` present with a millisecond value
- [ ] Exactly one `update` call per user decision, with all seven signals
- [ ] Category-to-signal mapping documented and stored with the consent record
- [ ] Basic mode in use for EEA/UK traffic; advanced mode escalated in writing if requested
- [ ] `region` defaults reviewed against the jurisdiction list from `intake.md`
- [ ] GTM tags use consent settings, not only the CMP's own blocking
- [ ] No Google host contacted before a decision — asserted by `audit.md`
- [ ] `gcs` parameter on GA4 hits matches the recorded choice
