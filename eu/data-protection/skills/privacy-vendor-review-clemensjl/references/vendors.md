# Vendor snapshot — infrastructure, analytics, payments, ad platforms

**Snapshot date: 2026-08-05.** Every entry was read from the vendor's own current legal or documentation page on that date, with the page's own "last updated" date recorded where it was shown. **This file is a lead, not a finding.** Vendor terms, sub-processor lists, regions and retention defaults change without notice. Re-verify the specific lines you rely on, and re-date the entry.

**Cross-cutting caveat:** **no DPF status below was verified against the official list.** Every DPF line is the vendor's own self-assertion on its own page. The list at `dataprivacyframework.gov/list` is the only authority; look up the exact contracting entity there, note which of the three frameworks it is Active under and for which covered-data scope, and record the check date before writing anything into a ROPA. See `transfers.md` for how. Several vendors publish their DPA or sub-processor list only as PDF; those points are marked UNVERIFIED here.

For email, support, embeds, forms and workplace tools see `vendors-saas.md`. For LLM and AI APIs see `ai-vendors.md`.

---

### Stripe
- **Entity:** Stripe Payments Europe, Limited outside the Americas (DPA, updated 18.11.2025). For EEA end customers the controller is Stripe Technology Company, Limited (Irish); SPEL is joint controller for regulated payment services (`stripe.com/legal/privacy-center`).
- **Role:** Split and explicit — processor on the customer's behalf, **and controller** with "sole and exclusive authority to determine the purposes and means" for fraud monitoring, prevention and detection.
- **Transfers:** Data Transfers Addendum (`stripe.com/legal/dta`) incorporated into the DPA; SCC **Modules 1 and 2**; DPF asserted; UK IDTA referenced. Default processing geography: **UNVERIFIED** — neither the DPA nor the privacy center states it, and no EU-only option was found.
- **DPA:** Auto-incorporated, "forms part of the Agreement". Sub-processors: `stripe.com/legal/service-providers` (20.12.2025), **30 days' notice, 30-day objection window**, email subscription via dashboard preferences.
- **Device:** Yes. Stripe.js collects device characteristics and activity signals (mouse movement, time on page), transmits to `m.stripe.com`, and may load hCaptcha on every page where Stripe.js is present. Stripe recommends embedding it site-wide, not only at checkout. `?advancedFraudSignals=false` disables it, but has no effect on Stripe-hosted Checkout and does not stop Elements interaction logging or 3DS2 device data. Stripe classifies these as strictly necessary "without necessarily requesting consent" (cookie policy, 20.06.2024).
- **Retention:** Five or more years from the end of the business relationship or the last transaction, whichever is later; biometric data max 1 year. Not configurable.
- **Gotcha:** Site-wide Stripe.js is a fingerprinting-grade device read performed for a purpose where **Stripe is its own controller** — outside your Art 28 DPA — and it fires before consent. Assess the Art 5(3) necessity claim yourself; do not adopt Stripe's.

### Sentry
- **Entity:** Functional Software, Inc. d/b/a Sentry, San Francisco. **No EU contracting entity.** EU affiliates appear only as sub-processors (Functional Software GmbH, Vienna; Sentry Software Netherlands B.V.).
- **Role:** Processor.
- **Region:** US (Iowa) or EU (Frankfurt, `de.sentry.io`). **Storage-region only.** User accounts, notification settings, 2FA authenticators, integration metadata, access tokens, org settings, audit logs, cron check-ins, project metadata, DSN keys and usage data are "always in US regardless of selection"; support-ticket data is US. **Region cannot be changed after org creation.**
- **Transfers:** SCC **Modules 2 and 3**, deemed signed; DPF asserted; UK Addendum; Swiss modifications.
- **DPA:** **Must be separately executed.** ToS § 4.4: "Unless Customer and Sentry have entered into a DPA, Customer will not submit any Personal Data to the Service." `sentry.io/legal/dpa/`, v5.1.0, 29.05.2024. Sub-processors: `sentry.io/legal/subprocessors/` (01.06.2026), **30 days' notice**, RSS subscription only; list includes **Anthropic PBC and OpenAI L.L.C.** as all-product sub-processors.
- **Device:** **UNVERIFIED** — no Sentry page states whether the browser SDK writes cookies or localStorage. Session Replay is offered; assume DOM capture and verify yourself.
- **Retention:** **UNVERIFIED** numeric default. Server-side data scrubbing is on by default; IP-address storage can be disabled.
- **Gotcha:** Stack traces routinely carry personal data. Sending any without a separately executed DPA breaches Sentry's own ToS and leaves you with **no Art 28 contract at all**.

### PostHog
- **Entity:** PostHog, Inc., San Francisco. No EU entity.
- **Role:** Processor.
- **Region:** EU Cloud = Frankfurt (AWS Germany); US Cloud = Virginia. Sub-processors split by region, but **Cloudflare is listed as global edge locations regardless**, and every sub-processor entity is US-incorporated. On EU Cloud, IP capture is disabled by default for new projects.
- **Transfers:** SCC **Module 2**, UK SCCs with Addendum, Swiss-adapted SCCs; EU-US DPF, UK Extension and Swiss-US DPF asserted.
- **DPA:** **The published DPA is explicitly "not binding on its own."** A countersigned DPA must be generated at `app.posthog.com/legal`. Sub-processors: `posthog.com/subprocessors` — **14 days' notice, 7-day objection window** (the shortest in this file).
- **Device:** Yes, aggressively. Defaults in `posthog.com/docs/libraries/js/config`: `persistence: "localStorage+cookie"`, `autocapture: true`, `capture_pageview: true`, `disable_session_recording: false`, `opt_out_capturing_by_default: false`. A bare `posthog.init()` writes to the device and captures clicks and page views **before any consent**.
- **Retention:** **UNVERIFIED** — no default stated.
- **Gotcha:** Self-serve customers routinely believe the website DPA binds. It does not. Combined with autocapture and session recording on by default, an unconfigured install is both contract-less and consent-less.

### Plausible Analytics
- **Entity:** Plausible Insights OÜ, Tartu, Estonia. **EU-native.**
- **Role:** Processor (`plausible.io/dpa`, 03.2026).
- **Region:** Visitor data processed and stored in the EU on Hetzner (DE), Bunny (SI) and UpCloud (FI) — genuinely regional; "visitor data does not leave the EU". **Account and support data is a different story**: Paddle, Postmark, Gravatar, Help Scout, hCaptcha, Algolia, optionally Google, Anthropic and Mailchimp. Transfer mechanism for that slice: **UNVERIFIED**.
- **DPA:** Auto-accepted; use of the service constitutes acceptance. **No sub-processor list page, no notice period and no objection mechanism** stated in the DPA — the weakest Art 28(2)/(4) paper trail in this file.
- **Device:** No storage or access claimed. Unique visitors derived as `hash(daily_salt + domain + ip + user_agent)` with 24-hour salt rotation; raw IP and UA not retained.
- **Retention:** **UNVERIFIED**.
- **Gotcha:** "No consent needed" is the vendor's legal opinion, not a regulator's. The Art 5(3) analysis may well hold, but the IP-plus-UA hash is still processing that needs an Art 6 basis with a documented legitimate-interest assessment. And the missing sub-processor mechanics leave you with no contractual objection right.

### Google Analytics 4
- **Entity:** Google LLC or **Google Ireland Limited**, determined by the underlying agreement (Ads Data Processing Terms v8.0, 30.05.2024). GA and GA360 are confirmed covered services (`business.safety.google/adsservices/`, 23.10.2025).
- **Role:** Processor under those terms. But Google's Controller-Controller Data Protection Terms (v11, effective 07.05.2026) make each party an **independent controller** for the products that incorporate them. Which GA4 features trip that — data-sharing settings, Google signals — is **UNVERIFIED**; the controller-terms page does not name them.
- **Region:** EU **first hop only**. Data from EU/CH/UK devices is collected through EU/CH/UK domains and servers and IP addresses are dropped before logging, but analysis and storage happen on Analytics servers. **No EU data residency for the processed data.**
- **Transfers:** SCCs C2P, P2C, P2P and P2P (Google Exporter), plus an "Alternative Transfer Solution". Google LLC asserts EU-US DPF, UK Extension and Swiss-US DPF (`policies.google.com/privacy/frameworks`, 23.08.2025).
- **DPA:** **Not auto-incorporated** — the terms apply only where "Customer clicked to accept or the parties otherwise agreed", i.e. you must accept the Data Processing Terms in the Analytics admin. Sub-processors: `business.safety.google/adssubprocessors/`, **at least 30 days' notice** to the Notification Email Address, objection = terminate for convenience within 90 days. Notice depends on that email address being set.
- **Device:** Yes: `_ga` (2 years), `_gid` (24h), `_gat*` (1 min), `_gac_<wpid>` (90 days), `FPID` (2 years), `AMP_TOKEN` (`business.safety.google/adscookies/`). Fires on page load unless blocked.
- **Retention:** User- and event-level 2 or 14 months for standard properties (26/38/50 in 360). **Factory default value UNVERIFIED** — Google states the options but never the default. Fixed: signed-in data expires after 26 months; age, gender and interest data always 2 months.
- **Gotcha:** A property whose owner never clicked accept in the Analytics admin has **no Art 28 contract with Google at all**. Separately, the EU-first-hop architecture is what Google offers *instead of* EU residency; it does not support a claim that GA4 data is stored in the EU. See `enforcement.md` for the DPA decisions.

### Google Tag Manager
- **Entity and terms:** Same instrument as GA4; GTM and GTM 360 are confirmed covered services (23.10.2025). Processing geography: **UNVERIFIED**.
- **Device:** GTM's own footprint is small and documented: only `_dc_gtm_<property-id>` (1 minute, shared with Analytics). Google states GTM collects aggregated tag-firing data without visitor IP addresses or measurement identifiers, and does not collect information about visitors to customers' properties.
- **Retention:** Standard HTTP request logs deleted within 14 days. Not configurable.
- **Gotcha:** GTM is not the risk; what it loads is. The consent gate must sit on **tag firing**, not on the container. The classic failure is a banner that blocks the container and then releases everything at once on accept.

### Meta Pixel / Meta Business Tools
- **Entity:** Meta Platforms Ireland Limited, Dublin (Business Tools Terms effective 03.11.2025; Meta Data Processing Terms effective 23.08.2025).
- **Role:** **Split and formally documented.** For event data from user interactions on the advertiser's site or app the parties "recognise and agree to be **joint controllers**" under **Art 26 GDPR**. For matching, measurement and analysis Meta Ireland is processor. The Data Processing Terms cover only the processor leg.
- **Transfers:** EU, UK and Global Data Transfer Addenda incorporated by reference. SCC module numbers and processing geography: **UNVERIFIED**.
- **DPA:** Auto-incorporated by accepting the Business Tools Terms. There is no negotiated Art 26 arrangement — the allocation is dictated. Sub-processors: **no public list URL found; no notice period in days — UNVERIFIED.**
- **Device:** Yes. Meta's cookie policy confirms it places cookies when users visit third-party sites using Meta products, "without any further action on your part". Fires on page load. Individual cookie names and lifetimes: **UNVERIFIED** — Meta publishes no cookie inventory and the first-party-cookie developer page 404s.
- **Retention:** **UNVERIFIED.**
- **Gotcha:** Joint controllership means you owe data subjects the essence of the Art 26 arrangement and you are directly liable for your share. A privacy notice listing Meta as a mere processor is wrong **on Meta's own terms**. Sending events server-side through the Conversions API does not change the joint controllership — it is the same event data under the same clause.

### Vercel
- **Entity:** Vercel Inc., Delaware. **No EU entity and no EU representative named** in either the DPA or the privacy notice (01.06.2026).
- **Role:** Split — processor for Customer Data, **controller for "Service-Generated Data" and "Contact Data"**. Visitor request metadata lives in the controller slice, outside your DPA.
- **Region:** US by default; "primary processing facilities are in the United States" and data may be processed "anywhere else in the world". **No EU residency guarantee in the DPA.** Function regions are a routing choice, not a contractual commitment.
- **Transfers:** SCC **Modules 1, 2 and 3**; UK IDTA deemed entered into; Swiss FADP referenced. The DPA does not mention DPF; the privacy notice asserts EU-US DPF plus UK Extension and Swiss-US.
- **DPA:** Auto-incorporated; `vercel.com/legal/dpa`, updated 17.03.2026, effective 31.03.2026. Sub-processors: `vercel.com/legal/subprocessors` **404s**; the live list is `security.vercel.com/subprocessors`. Subscribe by e-mailing privacy@vercel.com. **Objection window: five calendar days**; remedy is termination for convenience with no refund and committed fees still due. Sub-processor locations are not published; recent additions are AI inference providers.
- **Device:** Vercel Web Analytics sets no cookies; visitors identified by a hash of the incoming request, session hash discarded after 24 hours (`vercel.com/docs/analytics/privacy-policy`, 26.06.2026).
- **Retention:** Web Analytics session hash 24 hours. Aggregate analytics and log retention: **UNVERIFIED.**
- **Gotcha:** A five-day objection window with no refund on termination is effectively unexerciseable, and new AI-inference sub-processors keep arriving under it.

### Netlify
- **Entity:** Netlify, Inc., San Francisco. No EU entity or representative named.
- **Role:** Controller for visitor and subscriber data; processor for enterprise customer data under the DPA.
- **Region:** **UNVERIFIED** — no EU residency statement on any reachable page.
- **Transfers:** SCCs under Decision 2021/914, modules unspecified; DPF asserted for Netlify, Inc. and Jamstack Innovation Fund.
- **DPA:** `netlify.com/gdpr-ccpa/` claims incorporation by reference, but **neither the Terms of Use nor the Self-Serve Subscription Agreement (unchanged since 08.09.2020) contains an incorporation clause** — the Self-Serve Agreement § 7 references only the Privacy Policy. The DPA is PDF-only, so its roles, SCC modules and notice periods are **UNVERIFIED**. Sub-processors: no public list; the trust centre shows logos only (Fivetran, CrowdStrike, WorkOS, Datadog, AWS) with detail behind an access request. **Notice and objection mechanics UNVERIFIED.**
- **Retention:** No period stated.
- **Gotcha:** A self-serve Netlify customer may have **no enforceable Art 28 contract**, and cannot read the sub-processor list without requesting access — which fails Art 28(2) transparency on its own.

### Cloudflare
- **Entity:** Cloudflare, Inc., San Francisco, including for the self-serve agreement (12.09.2025). EU group companies exist but are not the self-serve contracting party.
- **Role:** Processor, or sub-processor where the customer is itself a processor.
- **Region:** Global anycast by default; the DPA addresses lawful transfers rather than residency. EU-only processing exists only as the **Data Localization Suite** — Regional Services, Customer Metadata Boundary, Geo Key Manager — an **Enterprise-only paid add-on** (`developers.cloudflare.com/data-localization/`, 05.05.2026). Support and sub-processor personnel are out of scope; sub-processors include Slack, Salesforce, CoreWeave, Anthropic, OpenAI, X.AI and Groq, all US.
- **Transfers:** SCC **Modules 2 and 3**; UK Addendum; Swiss adaptations; DPF asserted and relied on. Global CBPR/PRP certification.
- **DPA:** **Auto-incorporated, verified in the agreement itself** (§ 6.1). `cloudflare.com/cloudflare-customer-dpa/`, v6.4, effective 03.04.2026. Sub-processors: `cloudflare.com/gdpr/subprocessors/cloudflare-services/` (01.10.2025), **30 days' notice, 10-day objection window**, RSS at `cloudflare.com/gdpr/subprocessors/rss.xml/`.
- **Device:** Yes, on every proxied site, before any banner renders: `__cf_bm` (30 min), `cf_clearance`, `__cflb`, `__cfseq`, `__cfruid`, `cf_ob_info`/`cf_use_ob`, `__cfwaitingroom`, `_cfuvid`. Cloudflare classifies all as strictly necessary.
- **Retention:** **UNVERIFIED.**
- **Gotcha:** "Strictly necessary" is Cloudflare's assessment of its own product, not a per-site assessment. Security and bot-management storage is generally defensible under the Art 5(3) exemption, but **you** must document that assessment and list the cookies in your cookie disclosure; you cannot omit them because the vendor labelled them necessary.

### Supabase
- **Entity:** SUPABASE PTE. LTD., Singapore. No EU entity. Note the split: the ToS is governed by **California law with individual arbitration and a class-action waiver**, while the DPA's SCCs are governed by **Irish law and Irish courts**.
- **Role:** Processor, or sub-processor where the customer is a processor.
- **Region:** Per project. EU regions: Ireland, London, Paris, Frankfurt, Zurich, Stockholm. The DPA commits that data is "stored and **primarily** Processed" in the chosen region — "primarily" is the operative hedge. Which components (auth, storage, edge functions, logs, dashboard, support) are region-bound: **UNVERIFIED.**
- **Transfers:** SCC **Modules 2 and 3**, Clauses 17-18 Irish law; UK Addendum v.B.1.0; Swiss Addendum. **No DPF claim.**
- **DPA:** Auto-incorporated; acceptance of the Agreement has the same effect as signing the SCCs. Version 1, 01.08.2026. Sub-processors: `supabase.com/legal/customer-resources/subprocessor-list` (01.06.2026) — **the list itself is a PDF, so sub-processor identities and locations are UNVERIFIED.** **30 days' notice, 5-day objection window.**
- **Device:** Auth persists sessions client-side; the default storage mechanism and key name are **UNVERIFIED** from Supabase's own docs. Auth-session storage is generally strictly necessary under Art 5(3), so this is lower risk than analytics storage.
- **Retention:** Customer-controlled.
- **Gotcha:** "Primarily processed" is not a residency guarantee, and no page tells you which platform components leave the chosen EU region.

### Firebase (Google)
- **Entity:** Google LLC, **Google Ireland Limited**, or another affiliate (Firebase Data Processing and Security Terms, last modified 21.08.2024).
- **Role:** Processor.
- **Scope — critical:** these terms cover the Firebase Services. **Google Analytics for Firebase is not covered**: "Google Analytics is a separate service that can be used together with Firebase, and is subject to separate terms" (`firebase.google.com/support/privacy`, 18.02.2026).
- **Region:** "Unless a service or feature offers data location selection, Firebase may process and store your data anywhere Google or its agents maintain facilities." **Firebase Authentication processes exclusively in US data centres.** Location is per product, and the default-resources location is immutable. Whether European regions are offered per service: **partially UNVERIFIED.**
- **Transfers:** SCCs C2P, P2C, P2P and P2P (Google Exporter); DPF asserted for Google LLC.
- **DPA:** **Auto-incorporated** — unlike GA4. Sub-processors: `firebase.google.com/terms/subprocessors`, **at least 30 days' notice**, objection = terminate for convenience within 90 days.
- **Device:** Firebase Installation IDs, Crashlytics Installation UUIDs and random Session IDs are written to the device. Creation timing relative to consent, and the web SDK storage mechanism: **UNVERIFIED.**
- **Retention (verified):** Crashlytics 90 days; Performance Monitoring 30 days for IP-associated events and 60 days for installation data; Authentication IP addresses "a few weeks", other data 180 days after a deletion request. Not configurable.
- **Gotcha:** Google Analytics for Firebase is the piece everyone assumes is covered and is not. And any Firebase project with login has a **mandatory US transfer** regardless of where Firestore sits.

### AWS
- **Entity:** **Amazon Web Services EMEA SARL** (Luxembourg) for customers in Europe, the Middle East or Africa excluding South Africa, per the contracting-party table in the AWS Customer Agreement § 12 (updated 01.06.2026). Assignment follows the customer's country automatically.
- **Role:** Processor. (Stated in the DPA, which is PDF-only — role wording, SCC module numbering and audit/deletion terms are **UNVERIFIED**.)
- **Region:** Customer data can be stored in European Regions including France, Germany, Ireland, Italy, Spain and Sweden. Region choice is a genuine boundary for the service itself; sub-processors and support are not region-bound. **AWS European Sovereign Cloud: UNVERIFIED** — the candidate URLs 404 and neither GDPR page mentions it.
- **Transfers:** Service Terms § 1.14.3 references Controller-to-Processor and Processor-to-Processor Clauses, applying automatically for transfers outside the EEA to a non-adequate country; UK via IDTA; Swiss per FDPIC amendments. **No DPF reliance is claimed anywhere on the AWS pages checked** — so SCCs plus a transfer impact assessment are mandatory, not optional, for non-EU region usage.
- **DPA:** Auto-incorporated, verified in the Service Terms themselves (§ 1.14.1). Sub-processors: `aws.amazon.com/compliance/sub-processors/` (28.07.2026), page updated "at least 30 days before engaging a new sub-processor", e-mail subscription available. **No objection right is stated on the page** — unusual; check against the PDF DPA.
- **Device:** Not applicable to infrastructure services by default; anything written to end-user devices comes from the customer's own application. Not formally asserted by AWS.
- **Retention:** Customer-controlled.
- **Gotcha:** The EU contracting entity is automatic, but the sub-processor set is global and the published sub-processor page grants **no objection right**.

---

## Patterns worth carrying forward

1. **Three vendors here do not give you a DPA by default:** Sentry (separately executed, and its ToS forbids sending personal data without one), PostHog (published text explicitly non-binding), Google Analytics and Tag Manager (terms apply only once accepted in the admin).
2. **Netlify's DPA incorporation is asserted only on a marketing page** and is absent from the contract documents.
3. **Objection windows that cannot realistically be exercised:** Vercel 5 days (no refund), Supabase 5 days (list is a PDF), PostHog 7 days, Cloudflare 10 days.
4. **"EU region" rarely means EU processing:** Sentry (accounts, tokens, audit logs and support always US, region immutable), Supabase ("primarily"), Cloudflare (Enterprise paid add-on with undocumented gaps), GA4 (EU first hop only), Firebase (Auth is US-only).
5. **Meta is a joint controller under Art 26 by its own terms** — the notice must say so.
6. **Nothing here was confirmed Active on the official DPF list.** Confirm the exact entity yourself.

## Checkpoints

- [ ] Entry re-verified against the vendor's live page and re-dated before use
- [ ] The exact contracting entity for **your** account confirmed, not the one in this file
- [ ] DPF status checked on `dataprivacyframework.gov/list` for that entity, with the check date
- [ ] Every `UNVERIFIED` above either resolved or carried into the assessment as `[[MISSING: …]]`
- [ ] DPA acceptance mechanism confirmed in the dashboard, not inferred from this file
- [ ] Sub-processor notification subscribed to, with a named owner
- [ ] Region setting confirmed in the account, and its documented scope limits recorded
- [ ] Device behaviour confirmed by your own pre-consent capture, not by this file
