# Intake

Answer before writing any consent code. Unanswered items become `[[MISSING: …]]` in the artefact and in the report back to the user. Never invent an inventory — enumerate it from the built page, not from the repo, because tag managers inject at runtime.

## 1. What actually loads

Run the audit in `audit.md` first if the site exists. Otherwise list from the design.

1. Every third-party host the page contacts, from a clean profile, with no interaction. Hosts, not vendor names.
2. Which of those come from a tag manager container rather than the codebase.
3. Every iframe: video, map, social, scheduling, payment, chat, captcha.
4. Every font source. Local, self-hosted, or remote (`fonts.googleapis.com`, `use.typekit.net`, `fonts.bunny.net`).
5. Every image or pixel served from a domain you do not control.
6. Which scripts write to `localStorage`, `sessionStorage`, `IndexedDB` or `document.cookie`.
7. Whether a service worker is registered, and what it caches.

## 2. Ownership and control

8. Who can publish in the tag manager? Anyone able to add a tag can bypass the gate in `blocking-layer.md` unless GTM consent settings are enforced (`consent-mode-google.md`).
9. Is there an existing CMP? Name, version, and whether it is configured in "block until consent" mode or only signalling mode.
10. Is the consent banner script served first-party or from a vendor CDN?
11. Where does the consent state currently live — cookie, `localStorage`, server session, none?

## 3. Purposes and categories

12. Which categories will the banner offer? The usual split is strictly necessary / functional / analytics / marketing, but the categories must match the purposes in the privacy notice — the wording of which belongs to the `legal-*` skills.
13. For each third party: which category, and who decided. A classification with no owner is a finding.
14. Which items are claimed as strictly necessary, and on what reasoning? The Cookie Banner Taskforce (para 30, citing WP29 Opinion 04/2012) treats cookies retaining user preferences as essential; analytics and advertising are not.
15. Is there any consent-or-pay or cookie-wall arrangement? If yes, escalate — that is a legal question, not an implementation one.

## 4. Jurisdiction and audience

16. Which countries does traffic come from? EU/EEA and UK trigger prior consent; US states trigger opt-out signals (`gpc-us.md`).
17. Is the operator established in the EU, or targeting it?
18. Are there national specifics to respect — for example the Italian Garante's six-month re-prompt rule (`consent-record.md`)?
19. Is the site directed at children? Age of consent for information society services varies by Member State.
20. Does the site run programmatic display advertising with third-party demand? If no, do not adopt TCF (`tcf.md`).

## 5. Google stack

21. Which Google products are in use — GA4, Google Ads, Floodlight, Google Signals, Merchant Center, Customer Match?
22. Is Consent Mode already implemented? Basic or advanced? Verify against the network trace, not against the GTM UI.
23. Is there a server-side GTM container? On which hostname, and is it a subdomain of the site (`server-side-tagging.md`)?
24. Are conversion imports or offline uploads in play? Those carry their own consent fields.

## 6. Framework and delivery

25. Framework and rendering mode — Next.js App Router, Nuxt, SvelteKit, Astro, plain static, WordPress, Shopify.
26. Is any part server-rendered or streamed? If yes, read the SSR trap in `frameworks.md`.
27. Is there a CDN or edge layer that could serve a cached HTML page containing an already-unblocked script tag?
28. Is a Content-Security-Policy already deployed? Report-only or enforcing? Nonce or hash based?

## 7. Who else can add tags

29. Which marketing, SEO or agency tools have publish rights anywhere in the stack?
30. Is there a review step before a tag goes live? If not, the CSP and the CI audit in `audit.md` are the only controls that will hold.
31. Are there A/B testing, personalisation or heatmap tools? They write to storage on every visitor and are almost never strictly necessary.
32. Does any third party inject further third parties (a tag that loads a tag)? List the second-order hosts observed in the trace.

## 8. Proof and retention

33. Where will consent records be stored, and who can read them?
34. Is the banner versioned? How is a version bump released and recorded?
35. How long are records kept, and what is the deletion trigger?
36. Is there an existing re-prompt interval? What resets it?
37. Can the consent log be exported if the CMP is replaced?
38. Who signs off before launch — DPO, lawyer, neither? Record the name, not the role.

## Checkpoints

- [ ] Third-party host list produced from a real network trace, not from source
- [ ] Every host mapped to a category and an owner
- [ ] Tag-manager-injected tags separated from code-injected tags
- [ ] Fonts, iframes and pixels enumerated separately from scripts
- [ ] Storage writes (`localStorage`, `IndexedDB`, service worker) enumerated
- [ ] Jurisdictions listed; US traffic flagged for `gpc-us.md`
- [ ] Google product list confirmed against the network trace
- [ ] Framework and rendering mode recorded
- [ ] Existing CMP mode recorded (blocking vs signalling)
- [ ] Publish rights and second-order tag injection mapped
- [ ] Sign-off owner named
- [ ] All `[[MISSING: …]]` items reported back rather than assumed
