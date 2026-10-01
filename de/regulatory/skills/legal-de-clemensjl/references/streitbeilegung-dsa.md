# Consumer dispute resolution and DSA platform duties

Two unrelated topics that share one page because both end up in the footer. Status as at 05.08.2026.

## The ODR platform is dead

Regulation (EU) 2024/3228 repealed the ODR Regulation (EU) No 524/2013. The **EU ODR platform ceased operating on 20.07.2025**, and with it the Art 14 ODR-VO duty to link to it.

Consequences:

- Every link to `ec.europa.eu/consumers/odr` is a dead link.
- Keeping the text "Die EU-Kommission stellt eine Plattform zur Online-Streitbeilegung bereit" states something untrue about an available redress route, which can itself be an unfair commercial practice.
- Search the whole project — website, AGB, Widerrufsbelehrung, order confirmation e-mails, shipping e-mails, invoice templates, marketplace shop descriptions — for `odr`, `Online-Streitbeilegung`, `OS-Plattform`, `ec.europa.eu/consumers`.
- Never re-insert it, whatever a generator, plugin or template says.

## § 36 VSBG — Allgemeine Informationspflicht

The **VSBG** (Verbraucherstreitbeilegungsgesetz) duty survives the ODR repeal and is national law.

**Abs 1:** a trader who operates a website or uses AGB must inform the consumer, easily accessibly, clearly and comprehensibly,

1. of the extent to which they are **willing or obliged** to participate in a dispute resolution procedure before a Verbraucherschlichtungsstelle, and
2. where they are obliged to participate, of the competent Verbraucherschlichtungsstelle with its **address and website**, together with a statement that they participate.

**Abs 2:** the information must appear on the trader's website, where one exists, or be supplied together with the AGB.

**Abs 3:** the duty under Abs 1 Nr 1 does **not** apply to a trader who employed **ten or fewer persons on 31 December of the preceding year**. Note the wording: the exemption covers Nr 1 only. Where a trader is obliged to participate under other legislation, Nr 2 still applies.

**§ 37 VSBG — Informationen nach Entstehen der Streitigkeit:** where a dispute over a consumer contract could not be settled between the parties, the trader must point the consumer to a competent Verbraucherschlichtungsstelle, stating its address and website. The notice must be given **in Textform**. This is a duty in the individual case, not a website duty, and it applies regardless of the § 36 Abs 3 exemption.

The general-purpose body is the **Universalschlichtungsstelle des Bundes**; sector bodies exist for energy, telecommunications, transport, banking and insurance. Verify which body is competent before naming one — naming the wrong body is worse than the honest statement that participation is not undertaken.

### Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h2>Verbraucherstreitbeilegung</h2>
<p>[[Variant A — not participating, and not obliged to:]]
   Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer
   Verbraucherschlichtungsstelle teilzunehmen.</p>
<p>[[Variant B — participating or obliged to participate:]]
   Wir nehmen an Streitbeilegungsverfahren vor der folgenden Verbraucherschlichtungsstelle
   teil: [[name]], [[address]], [[website]].</p>
<!-- No ODR link. The EU platform was shut down on 20.07.2025. -->
```

## DSA and DDG — platform duties

Regulation (EU) 2022/2065 (DSA) applies directly. The **DDG** supplements it nationally; the **NetzDG was repealed on 14.05.2024** and no NetzDG reporting duties remain. The national Koordinator für digitale Dienste is the body established at the **Bundesnetzagentur** under § 12 DDG; the Landesmedienanstalten retain competence for the media-law aspects under § 10 DDG.

Classification decides the duty set:

| Role | Typical case | Core duties |
|---|---|---|
| Mere conduit, caching, hosting | ISP, CDN, cloud storage | Art 11, 12 DSA contact points; Art 14 DSA terms transparency; liability privileges Art 4 to 6 DSA and § 7 DDG |
| Hosting | comment section, forum, user uploads | additionally Art 16 DSA notice and action, Art 17 DSA statement of reasons, Art 18 DSA report of suspected criminal offences |
| Online platform | marketplace, social network, review site | additionally Art 20 to 22 DSA internal complaint handling and trusted flaggers, Art 26 advertising transparency, Art 27 recommender transparency, Art 25 dark-pattern prohibition |
| Online platform allowing consumer contracts | marketplace | additionally Art 30 DSA trader traceability, Art 31 compliance by design, Art 32 right to information |

Practical minimum for a small site with a comment section:

- publish an Art 11 DSA contact point for authorities and an Art 12 DSA contact point for users, with the languages accepted — in the Impressum
- provide an electronic notice mechanism that is easy to access and user-friendly, allowing a sufficiently substantiated notice (Art 16 DSA)
- give a statement of reasons to the affected user for every restriction — removal, demotion, account suspension — with the ground, the facts, the legal or contractual basis and the redress routes (Art 17 DSA)
- set out moderation rules, tools and human review in the terms and conditions, in clear and unambiguous language (Art 14 DSA)

**Art 19 DSA:** the obligations of Section 3 of Chapter III — the online-platform duties — do not apply to platforms that qualify as micro or small enterprises, unless they are designated as a VLOP. The Art 11, 12, 14, 16, 17 and 18 duties are not exempted.

The **Kleinstunternehmen exemption does not cover the hosting-level duties.** A hobby forum still needs a notice mechanism and a statement of reasons.

## Checkpoints

- [ ] Full-text search across the project for `odr`, `Online-Streitbeilegung`, `OS-Plattform`, `ec.europa.eu/consumers` returns nothing
- [ ] § 36 VSBG statement present in one of the two variants, easily accessible
- [ ] Where a body is named: verified as competent, with address and website
- [ ] § 36 Abs 3 VSBG exemption claimed only where headcount on 31 December of the previous year was ten or fewer, and documented
- [ ] § 37 VSBG Textform notice built into the complaints process, not just the website
- [ ] DSA classification documented for the actual service
- [ ] Art 11 and Art 12 DSA contact points published with the accepted languages
- [ ] Art 16 DSA notice mechanism reachable without an account
- [ ] Art 17 DSA statement of reasons issued for every restriction
- [ ] Moderation rules disclosed in the terms (Art 14 DSA)
- [ ] Marketplaces: Art 30 DSA trader data collected and verified before listing
- [ ] No NetzDG reference and no NetzDG transparency report
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
