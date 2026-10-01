# Cookies and tracking

Switzerland has no consent requirement for cookies. It has an information duty with a refusal option, plus the general data protection rules on top. Getting this right in both directions is the point: do not import ePrivacy opt-in logic, and do not tell a client that Swiss law lets them track freely.

## Art. 45c FMG — the operative provision

Wording, FMG Stand am 1. Juni 2026. Status as at 2026-08-05:

> Art. 45c Daten auf fremden Geräten
> Das Bearbeiten von Daten auf fremden Geräten durch fernmeldetechnische Übertragung ist nur erlaubt:
> a. für die Fernmeldedienste und ihre Abrechnung; oder
> b. wenn die Benutzerinnen und Benutzer über die Bearbeitung und ihren Zweck informiert und darauf hingewiesen werden, dass sie die Bearbeitung ablehnen können.

Two elements, both mandatory: information about the processing and its purpose, and a notice that the user can refuse. Refusal must be possible — a notice that says "by using this site you agree" without a mechanism does not satisfy lit. b.

The provision covers any processing of data on a third party's device by telecommunications transmission. That reaches cookies, local storage, IndexedDB, web beacons and tracking pixels, device fingerprinting and advertising identifiers alike. It applies regardless of whether the data is personal data.

## The DSG layer

Where the tracking processes personal data, the DSG applies in addition. Art. 30 Abs. 2 lit. a DSG: processing contrary to the principles of Art. 6 and 8 DSG infringes personality. Art. 31 Abs. 1 DSG: such an infringement is unlawful unless justified by consent, by an overriding private or public interest, or by law.

So a private operator has three routes for non-essential cookies: rely on an overriding private interest after a genuine balancing exercise; obtain consent; or reduce the severity of the interference by granting a right to object — which Art. 45c lit. b FMG makes mandatory anyway.

Art. 6 Abs. 7 DSG requires **express** consent for besonders schützenswerte Personendaten and for Profiling mit hohem Risiko by a private person. That is where opt-in becomes mandatory in Switzerland.

## EDÖB position

The EDÖB Merkblatt "Verwendung von Cookies und ähnlichen Technologien im Zusammenhang mit Online-Tracking" of 27 March 2026 states the rule directly: while European law requires prior express consent for cookies other than necessary ones, Swiss law places the emphasis on transparent information and the user's right to object. Users must be informed about non-necessary cookies and their purpose and must be able to refuse — in principle **before the cookies are activated**. Prior express consent is required where the processing can be classified as unexpected or high-risk, or concerns besonders schützenswerte Personendaten.

The EDÖB Leitfaden "Datenbearbeitungen mittels Cookies und ähnlichen Technologien" V. 1.1 of 6 October 2025 fills in the detail:

- **Necessary cookies.** No objection right under Art. 45c FMG is available against cookies that are technically necessary; storing a consent or opt-out decision, session handling and load balancing count as necessary.
- **Default settings.** Art. 7 Abs. 3 DSG requires appropriate defaults so that cookie use is limited to the minimum needed for the purpose until the user has actually had the chance to take note and exercise the objection right.
- **Placement.** The objection option must be displayed prominently, recognisable and exercisable in a few clicks, on the first and on subsequent visits.
- **High interference intensity.** Where non-essential cookies operate in the context of besonders schützenswerte Personendaten or lead to Profiling mit hohem Risiko, neither an overriding private interest nor an opt-out design suffices — **express consent must be obtained in advance**. The Leitfaden names cookie-supported geolocation that yields precise movement profiles as an example, and treats a third party embedded across many websites and paid for access to personal information as capable of high-risk profiling.
- **Unexpected use.** Cookie use that clearly contradicts the purpose of the main processing must be flagged with particular clarity. Commercial cookies on sites with political, trade-union or religious content are treated as connected to besonders schützenswerte Personendaten and require express consent.
- **Personalised advertising in e-commerce** is generally regarded as customary and therefore not unexpected in a commercial context. That does not dispense with the Art. 45c FMG objection right.
- **Withdrawal.** After consent is given, the site must show on every visit, at a prominent place, that consent can be withdrawn at any time, and must route the user there with simple navigation.

## When an EU-style consent banner is nevertheless required

Whenever Art. 3(2) GDPR applies — the site offers goods or services to people in the EU, or monitors their behaviour there — the GDPR and the national ePrivacy implementations apply to that processing. Then prior, informed, freely given, unambiguous consent is required for non-essential cookies, "reject" must be as easy as "accept", nothing may fire before the decision, and consent must be logged. Language versions, EUR prices, EU delivery zones and EU-targeted advertising are the usual triggers.

A Swiss shop that serves both markets has two workable designs: run one GDPR-grade banner for everyone, or geo-differentiate. One banner for everyone is simpler and always defensible. Geo-differentiation is defensible too, but the Swiss variant still has to meet Art. 45c lit. b FMG and Art. 7 Abs. 3 DSG.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Cookies und ähnliche Technologien</h2>
<p>Wir setzen auf dieser Website Cookies und vergleichbare Technologien ein. Notwendige
Cookies sind für den Betrieb der Website erforderlich. Nicht notwendige Cookies
verwenden wir zu folgenden Zwecken:</p>
<ul>
  <li>[[Zweck]] – Anbieter: [[Anbieter]] – Speicherdauer: [[Dauer]]</li>
</ul>
<p>Sie können die Verwendung nicht notwendiger Cookies jederzeit ablehnen
(Art. 45c lit. b des Fernmeldegesetzes). Ihre Einstellungen ändern Sie hier:
<a href="[[Link]]">Cookie-Einstellungen</a>.</p>
<p>[[Falls ausdrückliche Einwilligung nach Art. 6 Abs. 7 DSG erforderlich:
Beschreibung der Bearbeitung und Hinweis auf den jederzeitigen Widerruf.]]</p>
```

The banner itself must expose the refusal option at the first level, not behind a "Settings" detour, and must carry a link to this section.

## Checkpoints

- [ ] Non-essential cookies do not fire before the user has had the chance to refuse (Art. 7 Abs. 3 DSG)
- [ ] The refusal option is on the first banner level and reachable in a few clicks on every later visit
- [ ] Purposes are named per cookie category, not as a single sentence
- [ ] Cookie table verified technically against a fresh-profile network and storage trace, not against the CMP's own list
- [ ] Assessed whether any processing is besonders schützenswert or Profiling mit hohem Risiko; if so, express opt-in implemented (Art. 6 Abs. 7 DSG)
- [ ] Withdrawal path shown prominently on every visit after consent
- [ ] Third-party fonts, maps, video and captcha either self-hosted or behind the refusal mechanism
- [ ] Art. 3(2) GDPR tested; if met, a GDPR-grade consent banner with logging is in place
- [ ] Datenschutzerklärung and Impressum reachable without interacting with the banner
- [ ] No claim in the text that Swiss law requires consent, and none that it requires nothing
