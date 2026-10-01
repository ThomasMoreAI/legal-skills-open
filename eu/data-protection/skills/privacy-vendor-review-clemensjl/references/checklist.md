# Pre-approval checklist

Run before the integration ships, before a contract is signed, and again at every re-review. Every item produces a finding with the article and the location, or it is not answered. "Looks fine" is not an answer.

Status as at 2026-08-05.

## Technical first — this produces half the findings in minutes

1. Load the product in a fresh profile with the network log running. List every third-party host contacted **before** any consent interaction.
2. Application tab: every cookie, localStorage key, sessionStorage key, IndexedDB store and service worker present before the consent decision.
3. Repeat both after **refusing**. Anything new is a finding.
4. Grep the repository for the vendor's SDK initialisation and read the options actually set, not the defaults in the docs.
5. Retrieve the vendor's DPA, sub-processor list and security annex, and archive them with today's date.
6. Look up the exact contracting entity on `dataprivacyframework.gov/list` if the vendor claims DPF, and record the status shown.

## Question 1 — what is transmitted

- [ ] Data categories established by observation, with a capture date
- [ ] Identifiers enumerated (cookie ID, user ID, device ID, IP, hashed e-mail)
- [ ] Full URL and referrer transmission checked on account, checkout and any sensitive route
- [ ] Free-text exposure answered explicitly
- [ ] Art 9 and Art 10 possibility answered explicitly, including via URL paths
- [ ] Server-side flows and webhook payloads inspected, not only the browser
- [ ] Volume of data subjects and events estimated

## Question 2 — role

- [ ] Each flow assessed separately
- [ ] Main terms read alongside the DPA for reserved use rights
- [ ] Any "improve our services", "aggregated insights" or "model training" clause quoted with its reference
- [ ] Payment, fraud, AML and KYC flows split from the payment-execution flow
- [ ] Pixels, tags and social embeds assessed under Art 26, with the Fashion ID limitation stated (CJEU 29.07.2019, C-40/17)
- [ ] Where joint controllership applies: Art 26(1) arrangement identified and the Art 26(2) essence actually reachable by data subjects
- [ ] Art 28(10) considered where the contractual label and the conduct diverge

## Question 3 — Art 28 contract

- [ ] DPA in force, with the acceptance mechanism named: incorporated by reference (clause §) or signed (date)
- [ ] Contracting entity on the DPA matches the entity on the invoice
- [ ] All eight Art 28(3) letters mapped to clause numbers; gaps named
- [ ] Breach notification wording compared against Art 33(2) "without undue delay"
- [ ] Deletion or return at the controller's choice per Art 28(3)(g); backup expiry window stated
- [ ] Sub-processor authorisation model, notice channel, notice period and objection consequence recorded (Art 28(2))
- [ ] A named person is subscribed to sub-processor change notifications
- [ ] Audit narrowing recorded as a deviation; the substitute report obtained and its scope checked (Art 28(3)(h))
- [ ] DPA, security annex and sub-processor list archived with the retrieval date

## Question 4 — transfers

- [ ] Every country of processing identified, including support and on-call access
- [ ] Mechanism named per recipient: adequacy decision (named), SCC module (numbered), or an Art 49 derogation (named and justified)
- [ ] SCC module matches the actual relationship
- [ ] Transfer impact assessment completed and dated where the mechanism is SCCs
- [ ] Supplementary measures listed, or the absence justified
- [ ] Where DPF is relied on: the exact entity checked on `dataprivacyframework.gov/list`, with its status, its covered-data scope (HR / non-HR), which of the three frameworks (EU-U.S., UK Extension, Swiss-U.S.) it is Active under, and the check date
- [ ] DPF reliance paired with a documented fallback mechanism
- [ ] Sub-processor layer covered by its own mechanism, not assumed to inherit yours
- [ ] UK and Swiss variants addressed where those data subjects are in scope
- [ ] "EU region" claims tested against where support, logs, account data and sub-processors actually sit

## Question 5 — device access and consent

- [ ] Art 5(3) assessed on the basis of *information*, not personal data
- [ ] Storage **and** read-only access both considered
- [ ] localStorage, sessionStorage, IndexedDB, Cache API, service workers, ETag and fingerprinting all inspected
- [ ] Any "strictly necessary" claim written out against the service the user explicitly requested
- [ ] National transposition identified (Austria: § 165 Abs 3 TKG 2021)
- [ ] Consent category assigned per purpose with the reasoning recorded
- [ ] Pre-consent capture shows zero requests to the vendor
- [ ] Tag manager itself gated; no downstream tag fires pre-consent
- [ ] Third-party embeds behind click-to-load, not autoloading iframes
- [ ] Banner loads nothing on dismissal or scroll
- [ ] Refuse is as prominent and as easy as accept
- [ ] Consent log records timestamp, banner/policy version, categories and withdrawal path (Art 7(1))
- [ ] Withdrawal permanently reachable and no harder than granting (Art 7(3))
- [ ] Where the product has US visitors: the same tags are gated, for CIPA reasons

## Question 6 — artefacts

- [ ] ROPA entry added to the correct existing activity; Art 30(1)(a) to (g) populated or `[[MISSING: …]]`
- [ ] Third country named in Art 30(1)(e), safeguard named rather than described as "appropriate"
- [ ] Legal basis recorded per purpose
- [ ] Notice paragraph drafted with the exact legal entity, the Art 6 basis and, where applicable, the ePrivacy consent
- [ ] Art 13(1)(f) "means to obtain a copy" of the safeguards answerable by a real contact
- [ ] Consent-manager entry written with the host list and blocking method
- [ ] Sub-processor entry added inbound and, if you are a processor, outbound with the customer notice period observed
- [ ] Retention statement tied to a named setting or a named job
- [ ] DPIA trigger result recorded either way, with the WP248 criteria count
- [ ] Approval carries an owner, a date and a re-review date

## Blocking findings

Any one of these stops the approval. They are not remediation items to ship alongside.

| Finding | Article |
|---|---|
| No Art 28 contract in force, and the vendor is a processor | Art 28(3) |
| Vendor cannot name a Chapter V mechanism for a third-country transfer | Art 44 |
| SCCs relied on with no transfer impact assessment | Art 46(1), CJEU C-311/18 |
| Tag touches the device before consent and no exemption applies | Art 5(3) ePrivacy |
| Vendor's terms permit an own-purpose use that was not assessed and has no basis | Art 6, Art 28(10) |
| Special-category data reaches the vendor with no Art 9(2) condition | Art 9 |
| DPIA required, residual high risk, no Art 36 prior consultation | Art 36(1) |
| The exact contracting entity cannot be established | Art 30(1)(d) |

## If rejected — the nearest compliant alternative

A rejection names one blocking finding and one direction of fix. These are **directions**, not endorsements: any replacement goes through the same six questions and the same snapshot discipline.

| Blocking finding | Nearest fix, in order of preference |
|---|---|
| Remotely loaded fonts, icon sets or JS libraries | Self-host the files. Removes the transfer, the Art 5(3) question and the notice entry in one step |
| Third-party analytics with an unresolvable transfer | Self-hosted analytics, or an EU-established provider whose EU claim survives the sub-processor check |
| Embedded video or map loading on page load | Click-to-load placeholder that fetches nothing until the user acts; or self-host the asset |
| Captcha that phones a third country before consent | A provider whose challenge can be served from the EEA, or a non-network control (honeypot, rate limit, proof-of-work) for low-risk forms |
| Session replay or heatmaps on authenticated pages | Restrict to unauthenticated pages, or drop it. Suppression rules are a mitigation, not a cure — they run after capture in most products |
| Ad pixel firing pre-consent | Strict consent gating; server-side conversion sending does not remove the Art 26 joint controllership |
| Vendor with no DPA in force | Execute the DPA before any personal data flows; if the vendor offers none, that is the end of the assessment |
| Vendor with an unresolvable own-purpose clause | Negotiate the clause out, disable the feature if it is switchable, or treat the vendor as an independent controller with its own basis and notice — and check whether that basis exists |
| US LLM API with no acceptable retention or residency | A regionally pinned deployment of the same model through a cloud provider that contracts on EU processing, with cross-region inference disabled — see `ai-vendors.md` |
| Free-tier AI service that trains on inputs | Move to the API or business tier of the same provider; verify the training default on the tier actually in use |

## Findings format

Worst first.

| Severity | Location | Article | Finding | Fix |
|---|---|---|---|---|
| blocking / high / medium | file:line, URL, or clause reference | Art / § | what is missing or wrong | the concrete step |

**Blocking** means: the processing has no lawful basis or no lawful mechanism, or the contract required by the GDPR does not exist. Everything else is high or medium.

## Approval note

```
<!-- DRAFT – not legally approved -->
Vendor:            [[name]] / [[exact contracting entity]]
Integration:       [[what, where, which tier]]
Decision:          [[approved | approved with conditions | rejected]]
Conditions:        [[list, each with an owner and a date]]
Blocking finding:  [[only if rejected — one finding, named]]
Alternative:       [[only if rejected — nearest compliant option and what changes]]
Six answers:       Q1 [[…]] Q2 [[…]] Q3 [[…]] Q4 [[…]] Q5 [[…]] Q6 [[…]]
Artefacts:         [[ROPA ref, notice paragraph ref, CMP entry, sub-processor entry, retention statement, DPIA result]]
Open items:        [[MISSING: …]]
Snapshot archived: [[path]], vendor page dates [[…]]
Approved by:       [[name]] on [[date]]
Re-review due:     [[date]]
Sign-off needed:   [[DPO / counsel / supervisory authority — or none]]
```
