# Cookies, tracking and consent

Two layers apply at once. Access to the terminal device is governed by **§ 25 TDDDG**; what happens with the resulting personal data is governed by the DSGVO. Consent under § 25 TDDDG does not by itself legitimise the subsequent processing, and a DSGVO legal basis does not replace the § 25 consent.

Status as at 05.08.2026. The TTDSG was renamed **TDDDG** (Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz) with effect from 14.05.2024 by the DDG. The section numbers did not change; § 25 TTDSG is now § 25 TDDDG. A text citing "§ 25 TTDSG" or "§ 15 Abs 3 TMG" is stale.

## § 25 TDDDG — Schutz der Privatsphäre bei Endeinrichtungen

Verbatim, status as at 05.08.2026:

> **(1)** Die Speicherung von Informationen in der Endeinrichtung des Endnutzers oder der Zugriff auf Informationen, die bereits in der Endeinrichtung gespeichert sind, sind nur zulässig, wenn der Endnutzer auf der Grundlage von klaren und umfassenden Informationen eingewilligt hat. Die Information des Endnutzers und die Einwilligung haben gemäß der Verordnung (EU) 2016/679 zu erfolgen.
>
> **(2)** Die Einwilligung nach Absatz 1 ist nicht erforderlich, wenn der alleinige Zweck der Speicherung von Informationen in der Endeinrichtung des Endnutzers oder der alleinige Zweck des Zugriffs auf bereits in der Endeinrichtung des Endnutzers gespeicherte Informationen die Durchführung der Übertragung einer Nachricht über ein öffentliches Telekommunikationsnetz ist oder wenn die Speicherung von Informationen in der Endeinrichtung des Endnutzers oder der Zugriff auf bereits in der Endeinrichtung des Endnutzers gespeicherte Informationen unbedingt erforderlich ist, damit der Anbieter eines digitalen Dienstes einen vom Nutzer ausdrücklich gewünschten digitalen Dienst zur Verfügung stellen kann.

Two consequences that generators get wrong:

- **It is not limited to cookies.** LocalStorage, IndexedDB, Service Worker caches, device fingerprinting, pixel calls that read device characteristics — any storage on or reading from the terminal device falls under Abs 1.
- **It does not depend on the data being personal.** § 25 applies to "Informationen" in the device, personal or not. "The cookie is anonymous" is not an exemption.

Strictly necessary under Abs 2 covers, in practice: session ID for a logged-in area, shopping basket, load balancing, security tokens including CSRF, and the record of the consent decision itself. It does not cover analytics, A/B testing, marketing pixels, or "statistics we need for our business".

## Banner requirements

Consent must satisfy Art 4 Nr 11 and Art 7 DSGVO: freely given, specific, informed, unambiguous, by a clear affirmative action, and as easy to withdraw as to give (Art 7 Abs 3 Satz 4 DSGVO).

- Reject must be available on the **first layer**, with the same visual weight as accept. A first layer offering only "Akzeptieren" and "Einstellungen" is not a free choice.
- No pre-ticked boxes and no implied consent from scrolling or continued use (CJEU C-673/17, Planet49; BGH I ZR 7/16, 28.05.2020).
- Granular per purpose. A single "Alle akzeptieren" without a per-purpose alternative is not specific.
- Nothing fires before the decision. Verify with a fresh browser profile and the network tab, not with the tag manager configuration.
- Withdrawal must be permanently reachable, typically a footer link that reopens the settings.
- Log each consent: timestamp, banner and text version, the categories selected, and the identifier used. Art 7 Abs 1 DSGVO puts the burden of proof on the controller.
- The Impressum and the Datenschutzerklärung must be reachable **without** making a consent decision.

## § 26 TDDDG and the Einwilligungsverwaltungsverordnung

§ 26 TDDDG allows recognised **Dienste zur Einwilligungsverwaltung** — user-side consent management services — as an alternative to per-site banners. The **EinwV** (Verordnung über Dienste zur Einwilligungsverwaltung nach dem Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz) entered into force on **01.04.2025**. The BfDI recognises services under it.

Practical position as at 05.08.2026: the scheme exists but is not a substitute for a compliant banner. Recognitions are individual and few — the BfDI published its first recognition on **17.10.2025** (Consenter, Law & Innovation Technology GmbH). Check the BfDI's current list at `bfdi.bund.de` before telling anyone they can drop their banner. Using a recognised service is voluntary for the site operator; § 25 Abs 1 TDDDG consent is still required, it is merely obtained by another route. `[[UNVERIFIED: how many services are recognised as at today and whether any browser or OS honours them at scale — check the BfDI list before advising]]`

## Third-party embeds

- **Google Fonts.** Serve locally. LG München I, 20.01.2022, 3 O 17493/20 awarded €100 damages under Art 82 Abs 1 DSGVO for dynamic embedding without consent, on the reasoning that local hosting is an available alternative so no legitimate interest under Art 6 Abs 1 lit f DSGVO exists. Local hosting removes the § 25 TDDDG question entirely.
- **Google Maps, YouTube, Vimeo, reCAPTCHA, Instagram and social plugins.** Either behind consent or behind a click-to-load placeholder that transfers nothing until the user activates it. The placeholder itself must not preload the provider's script.
- **Tag managers.** The container script itself normally needs consent because it reads and writes on the device. Loading it "empty" before consent is still access under § 25 Abs 1 TDDDG.
- **Fonts, CDNs and icon libraries from third-party hosts.** Same analysis as Google Fonts. Self-host.

## Cookie table

The declaration needs a table verified against the actual application state, not against the vendor's documentation.

| Name | Provider | Purpose | Category | Storage type | Duration |
|---|---|---|---|---|---|
| `[[name]]` | `[[provider]]` | `[[purpose]]` | necessary / preferences / statistics / marketing | Cookie / LocalStorage / IndexedDB | `[[duration]]` |

## Template — first banner layer

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<div role="dialog" aria-modal="true" aria-labelledby="cc-title">
  <h2 id="cc-title">Einwilligung in den Zugriff auf Ihr Endgerät</h2>
  <p>
    Wir setzen Cookies und ähnliche Technologien ein. Technisch notwendige Zugriffe
    erfolgen ohne Einwilligung (§ 25 Abs. 2 TDDDG). Für alle weiteren Zwecke
    — [[list the purposes actually used, e.g. Reichweitenmessung, Marketing]] —
    benötigen wir Ihre Einwilligung nach § 25 Abs. 1 TDDDG. Die damit verbundene
    Verarbeitung personenbezogener Daten stützen wir auf Art. 6 Abs. 1 lit. a DSGVO.
    [[where applicable: Dabei werden Daten an Empfänger in [[country]] übermittelt.]]
    Sie können Ihre Einwilligung jederzeit mit Wirkung für die Zukunft widerrufen.
  </p>
  <!-- Both buttons identical in size, colour, contrast and position weight. -->
  <button type="button" data-action="accept-all">Alle akzeptieren</button>
  <button type="button" data-action="reject-all">Alle ablehnen</button>
  <button type="button" data-action="settings">Einstellungen</button>
  <p>
    <a href="/datenschutz">Datenschutzerklärung</a> ·
    <a href="/impressum">Impressum</a>
  </p>
</div>
```

Second layer, one unticked switch per purpose:

```html
<fieldset>
  <legend>Zwecke</legend>
  <label><input type="checkbox" checked disabled> Technisch notwendig (§ 25 Abs. 2 TDDDG)</label>
  <label><input type="checkbox" name="zweck" value="praeferenzen"> Präferenzen</label>
  <label><input type="checkbox" name="zweck" value="statistik"> Reichweitenmessung</label>
  <label><input type="checkbox" name="zweck" value="marketing"> Marketing</label>
</fieldset>
```

Permanent footer entry for withdrawal, on every page:

```html
<a href="#" data-action="open-consent-settings">Cookie-Einstellungen ändern</a>
```

Click-to-load placeholder for a third-party embed:

```html
<div class="embed-placeholder">
  <p>
    Dieser Inhalt wird von [[provider]] geladen. Dabei werden Daten an
    [[provider]] übertragen [[, including a transfer to [[country]]]].
  </p>
  <button type="button" data-load="[[provider]]">Inhalt laden</button>
</div>
<!-- The provider's script is injected only inside the click handler.
     No preconnect, no dns-prefetch, no preload before the click. -->
```

## Checkpoints

- [ ] Fresh profile, network tab: no third-party request before a consent decision
- [ ] Application tab: no non-essential cookie, LocalStorage or IndexedDB entry before the decision
- [ ] Reject present on the first layer, same visual weight as accept
- [ ] No pre-ticked categories, no consent by scrolling
- [ ] Granular choice per purpose
- [ ] Withdrawal as easy as consent, permanent footer link
- [ ] Consent log with timestamp, text version and selection
- [ ] Impressum and Datenschutzerklärung reachable without deciding
- [ ] Google Fonts and all web fonts served locally
- [ ] Maps, video, captcha, social embeds behind consent or click-to-load
- [ ] Cookie table verified against the running application
- [ ] Citation says § 25 TDDDG, not § 25 TTDSG and not § 15 TMG
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
