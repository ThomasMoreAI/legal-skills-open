# Server-side tagging, first-party cookies and CNAME cloaking

Authoritative basis: Article 5(3) ePD; WebKit Tracking Prevention announcements (webkit.org/blog/11338, 12 November 2020). Status as at 2026-08-05.

## Server-side tagging does not remove the consent requirement

The pitch is that moving the container to `gtm.example.com` makes the tag first-party. Three things are true and one is not.

True:

- The cookie is now set by your host and can be set via the `Set-Cookie` response header.
- The browser's third-party-cookie restrictions apply differently.
- Ad blockers that work from hostname lists see a hostname they do not know.

Not true: that Article 5(3) stops applying. The provision covers **any** storage on, or access to, the terminal equipment that is not strictly necessary for a service the user explicitly requested. It contains no first-party exemption. EDPB Guidelines 2/2023 v2.0 paras 36–38 make the point structurally: storage counts regardless of who instructed it, on what medium, for how long. A first-party analytics cookie set by your own server for your own analytics still needs consent unless it meets the strictly-necessary test.

What changes legally is only the controller/processor picture: with server-side tagging you decide what is forwarded onward, so you carry responsibility for those onward transfers rather than the browser handing data straight to the vendor. That is a reason to prefer it after consent — not a reason to fire before it.

**Implementation rule.** The web container still loads in the browser, and the browser still sends the first request to your tagging host. Gate that request exactly as you gate any other: no `gtm.example.com` request before a consent signal.

## Cookie lifetimes: `Set-Cookie` versus `document.cookie`

| Written by | Mechanism | Safari/ITP treatment |
|---|---|---|
| Server, same registrable domain | `Set-Cookie` response header | Not capped by the script-writeable-storage rule |
| JavaScript | `document.cookie` | Capped at 7 days — WebKit's "7-day cap on all script-writeable storage", announced March 2020 |
| Server, but the hostname is a CNAME to a third party | `Set-Cookie` in a "third-party CNAME-cloaked HTTP response" | Capped at 7 days — announced 12 November 2020 with Safari 14 |

GA4 by default writes `_ga` and `_ga_<container>` from JavaScript via `document.cookie`, so on Safari those identifiers expire after seven days regardless of the configured `cookie_expires`. Server-side tagging can issue the identifier via `Set-Cookie` from your own host instead, which is the actual measurement reason to adopt it.

GA4 client-side cookie controls, for completeness: `cookie_domain`, `cookie_expires` (seconds), `cookie_prefix`, `cookie_flags` (e.g. `'SameSite=None;Secure'`), `cookie_update`. None of them defeats the ITP cap, because the cap is applied at write time by the browser, not read from the attribute.

**Chrome caps cookie lifetime at 400 days.** In force since **Chrome M104 (August 2022)**, per Chrome's own developer documentation (`developer.chrome.com/blog/cookie-max-age-expires`, read 05.08.2026): "cookies can no longer set an expiration date more than 400 days in the future". Three properties of the cap that decide how you handle it:

- It **clamps, it does not reject**. A cookie asking for 730 days is set with a 400-day expiry, silently. Your consent record will therefore quietly outlive nothing — but it will expire earlier than your own documentation claims, which is the compliance-facing risk if you promise a 12-month consent lifetime and derive it from the cookie.
- It applies **at write time**, so re-writing the cookie on each visit rolls the window forward. That is the ordinary way to keep a long-lived consent record alive, and it is also why an inactive user's consent record disappears at 400 days.
- **Session cookies are unaffected** — those without `Max-Age` or `Expires` are cleared at the end of the browsing session as before.

The 400-day cap is Chrome-side and independent of the seven-day Safari ITP cap on JavaScript-written cookies; a `Set-Cookie` from your own host escapes ITP but not this.

## The CNAME cloaking problem

CNAME cloaking means pointing `analytics.example.com` at a CNAME that resolves into the tracker's own domain, so the browser treats the request as first-party. It has four distinct problems and only the first is about consent.

1. **It is designed to defeat a user protection.** Presenting a third party as first-party in order to escape browser restrictions is hard to reconcile with the fairness principle in Article 5(1)(a) GDPR, and it does nothing about Article 5(3), which never depended on the hostname.
2. **Every cookie scoped to the parent domain is sent to the tracker.** A request to `analytics.example.com` carries all cookies set on `.example.com` — session identifiers, CSRF tokens, authentication cookies — to a party that should never see them. This is the concrete security failure, and it has been demonstrated repeatedly in the wild.
3. **Safari caps it anyway.** Cookies set in CNAME-cloaked third-party responses are capped at seven days, so the measurement benefit largely evaporates on Safari.
4. **You now own the TLS certificate and the subdomain.** Delegating a subdomain to a third party creates takeover risk if the delegation outlives the contract.

**Correct alternative**: a server-side container that you actually run, on your own infrastructure, on a subdomain that resolves to your own servers. You terminate TLS, you choose what is forwarded, you set the cookie, and you can enforce the consent state server-side.

## Transmitting consent state to the server container

The server must not assume. Send the state explicitly and make the container refuse to forward when it is absent.

```js
// client: attach state to every event forwarded to the server container
const c = getConsent();
gtag('set', {
  ad_storage: c?.categories.marketing ? 'granted' : 'denied',
  analytics_storage: c?.categories.analytics ? 'granted' : 'denied'
});
```

Google's server-side tagging passes consent state through with the incoming request; the server container's tags respect their own consent settings. Configure the server container so that:

- every tag has explicit consent requirements, not "not set";
- the default when the signal is missing is *deny*, not *forward*;
- onward vendors receive the state too, where their API supports it.

Then verify by inspecting what the container forwards, not by reading its configuration screen.

## Setting a first-party identifier correctly

If you set your own identifier server-side after consent:

```
Set-Cookie: sid=[[OPAQUE_RANDOM]]; Max-Age=[[SECONDS]]; Path=/; Secure; HttpOnly; SameSite=Lax
```

- `HttpOnly` where JS does not need it — it also keeps the value out of `document.cookie` audits and out of XSS reach.
- `Secure` always.
- `SameSite=Lax` unless a genuine cross-site flow requires `None`, which then requires `Secure`.
- Opaque random value, no derivation from email, IP or user agent — a hashed persistent identifier is still an identifier, and hashing on the device does not take it out of Article 5(3) scope (Guidelines 2/2023 §3.5).
- Do not set it at all before consent, including "just a session id for analytics".

## Checkpoints

- [ ] The request to the server-side tagging host is gated like any third-party request
- [ ] The tagging hostname resolves to infrastructure you control, not a CNAME into a vendor
- [ ] No parent-domain cookies are exposed to a vendor-controlled subdomain
- [ ] Server container tags have explicit consent requirements; default is deny
- [ ] Consent state is transmitted with each event and is logged server-side
- [ ] Identifiers are opaque and random, never derived from personal data
- [ ] `Secure`, `HttpOnly` and `SameSite` set on every first-party identifier cookie
- [ ] Safari behaviour measured, not assumed — 7-day cap on JS-written cookies verified
- [ ] Subdomain delegation reviewed for takeover risk and certificate ownership
- [ ] `[[MISSING: …]]` raised where the onward vendor list for the server container is unknown
