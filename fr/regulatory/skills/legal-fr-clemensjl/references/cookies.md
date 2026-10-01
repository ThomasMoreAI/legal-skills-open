# Cookies et traceurs

Trackers are governed by **article 82 de la loi n° 78-17**, not by RGPD article 6. The operative doctrine is the CNIL's: **délibération n° 2020-091 du 17 septembre 2020** (lignes directrices) and **délibération n° 2020-092 du 17 septembre 2020** (recommandation). Enforcement runs on article 82, which is why the CNIL can fine a company established outside France through its French establishment without going through the one-stop-shop.

## Article 82 de la loi n° 78-17

Status as at 2026-08-05. Version en vigueur depuis le 1er juin 2019.

The subscriber or user of an electronic communications service must be informed, in a clear and complete manner, by the controller or its representative, of the **purpose** of any action seeking to access information already stored in their terminal equipment or to write information into it, and of the **means available to object**. Such access or writing may only occur once the user has expressed consent, after having received that information.

Two exemptions, and only two:

1. access or writing whose exclusive purpose is to allow or facilitate communication by electronic means;
2. access or writing strictly necessary to provide an online communication service **expressly requested by the user**.

Everything else — analytics, advertising pixels, A/B testing, session replay, social buttons, third-party maps, third-party video, third-party fonts, captchas that profile — requires consent before the first request leaves the browser.

## CNIL doctrine that a generic banner fails

- **Refusal as easy as acceptance, on the first layer.** A « Tout refuser » control at the same level and with the same prominence as « Tout accepter », or an equivalent solution. Two clicks to refuse against one to accept is the defect the CNIL has fined most often.
- **Continued browsing is not consent.** Scrolling, clicking through, or closing the banner cannot be read as acceptance. Silence equals refusal.
- **No pre-ticked boxes.** Consent requires a clear affirmative act, per purpose.
- **First-layer information.** The purposes must be listed clearly on the first layer, with the identity of the controllers, the consequences of refusal, and a route to withdraw.
- **Withdrawal as easy as giving.** A permanent, reachable control — footer link or a persistent widget.
- **Storing the choice.** The CNIL treats retaining the user's choices for **six months** as good practice; re-prompting a user who refused, on every visit, is the pattern the recommandation targets. This is a recommendation, not a statutory deadline.
- **Proof.** The controller must be able to demonstrate consent (RGPD article 7(1)). Keep, per consent: timestamp, the purposes accepted, the banner version and text version shown, and the mechanism used.

## Cookie walls

The Conseil d'État, in its decision of **19 June 2020, n° 434684**, annulled the CNIL's earlier blanket prohibition of cookie walls: the CNIL could not derive a general ban by way of soft law. Cookie walls are therefore assessed case by case. The CNIL published evaluation criteria in 2022: consent must remain free, which in practice requires a genuine and fair alternative to accepting trackers, and where that alternative is paid, a reasonable price. Consent-or-pay remains contested at EU level; do not present a paywall alternative as safe. [[UNVERIFIED: the exact publication date and current wording of the CNIL cookie-wall evaluation criteria, and whether the CNIL updated them after EDPB Opinion 08/2024 on consent or pay — check cnil.fr before relying on specific criteria]]

## Audience measurement exempted from consent

The CNIL exempts strictly limited audience-measurement trackers under article 82. Conditions, as published by the CNIL:

- the purpose is **strictly limited to audience measurement** for the exclusive account of the site or app publisher;
- the output is anonymous statistics only;
- no cross-referencing with other processing, and no transmission of non-anonymised data to third parties;
- no tracking of the person across several sites or apps through the same identifier — no cross-domain tracking, no reach measurement;
- **cookie lifetime capped at 13 months**, not silently renewed on a return visit;
- **data collected through the tracker retained for at most 25 months**;
- the exemption is reassessed periodically.

The CNIL does not certify or validate specific products, and there is no CNIL list that makes a given tool automatically lawful. A tool is exempt because of how it is configured, not because of its name. Google Analytics in its standard configuration is not exempt.

## Enforcement

Fines are imposed under article 82 by the CNIL's formation restreinte, without the one-stop-shop. The landmark decisions on the refusal button are those of **31 December 2021**: 150 million € against Google and 60 million € against Meta (Facebook), precisely because refusing took more clicks than accepting. Enforcement has not slowed: the CNIL's published sanctions list shows a 50 million € fine against a telecoms operator on **14 November 2024** covering cookies and prospection, and a continuing series of cookie fines through 2025 and into 2026 ranging from a few thousand euros for small publishers to several hundred thousand for larger ones. The practical lesson is that small sites are now sanctioned too. Check `cnil.fr/fr/les-sanctions-prononcees-par-la-cnil` for the current state before advising on risk.

## Banner requirements, condensed

| Element | Requirement | Norm |
|---|---|---|
| Before consent | No non-exempt request fires | art. 82 loi 78-17 |
| First layer | « Tout accepter » and « Tout refuser » equally prominent | délib. 2020-092 |
| Purposes | Listed on the first layer, granular choice available | délib. 2020-091 |
| Default state | All optional categories off, no pre-ticked boxes | délib. 2020-091 |
| Closing the banner | Must not be read as acceptance | délib. 2020-091 |
| Withdrawal | Permanent control, as easy as giving consent | RGPD art. 7(3) |
| Proof | Timestamp, purposes, banner version, mechanism | RGPD art. 7(1) |
| Exempt measurement | 13-month cookie, 25-month data, no cross-site ID | CNIL criteria |

## Template — cookie policy section

```html
<!-- BROUILLON – non validé juridiquement -->
<h1>Cookies et traceurs</h1>
<p>Le dépôt et la lecture de traceurs sur votre terminal sont régis par l'article 82
de la loi n° 78-17 du 6 janvier 1978. Les traceurs non strictement nécessaires ne
sont déposés qu'après votre consentement, que vous pouvez retirer à tout moment.</p>

<h2>Traceurs déposés</h2>
<table>
  <tr><th>Nom</th><th>Éditeur</th><th>Finalité</th><th>Durée</th>
      <th>Consentement requis</th></tr>
  <tr><td>[[nom]]</td><td>[[éditeur]]</td><td>[[finalité]]</td><td>[[durée]]</td>
      <td>[[oui / non — exemption art. 82]]</td></tr>
</table>

<h2>Retirer votre consentement</h2>
<p><a href="[[URL ou déclencheur du gestionnaire de consentement]]">Modifier mes
choix</a>. Vos choix sont conservés [[durée]] puis vous êtes à nouveau sollicité.</p>
```

## Checkpoints

- [ ] Load the site in a fresh profile with the network tab open: no non-exempt third-party request before a decision
- [ ] Application tab: no non-exempt cookie, localStorage or IndexedDB entry before a decision
- [ ] « Tout refuser » on the first layer, same size, same contrast, same position level as « Tout accepter »
- [ ] Purposes listed on the first layer with granular choice
- [ ] No pre-ticked categories, closing the banner does not consent
- [ ] Withdrawal control permanently reachable from the footer
- [ ] Cookie table matches the network capture, not the tag manager configuration
- [ ] Consent log stores timestamp, purposes, banner version and mechanism
- [ ] Fonts served locally, or behind consent
- [ ] Maps, video and captcha behind consent or click-to-load
- [ ] Audience measurement claimed as exempt actually meets all CNIL criteria, including the 13-month and 25-month limits
- [ ] No claim that a tool is "CNIL certified" — the CNIL certifies no tracker
