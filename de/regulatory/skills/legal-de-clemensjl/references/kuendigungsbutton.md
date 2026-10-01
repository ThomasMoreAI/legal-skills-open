# Kündigungsbutton — § 312k BGB

The genuinely German-specific obligation. No Austrian, Swiss or US template contains it, and no generic EU checklist produces it. Status as at 05.08.2026. In force since **01.07.2022** (Gesetz für faire Verbraucherverträge).

## Scope

§ 312k BGB applies where a trader enables consumers to conclude, on a website, a contract for a **continuing obligation against payment** (Dauerschuldverhältnis). Subscriptions, memberships, SaaS plans, streaming, gym contracts, hosting, box schemes, paid communities.

It does not depend on the payment pattern. **BGH, 22.05.2025, I ZR 161/24**: a one-off payment does not take the contract outside § 312k BGB where the trader owes performance continuously over the term. Design the decision around whether the trader's performance is continuous, not around the invoice.

It applies regardless of whether the consumer concluded the contract through the website in the individual case — the trigger is that the website offers that route.

## The two buttons

**Kündigungsschaltfläche.** Labelled with nothing other than **"Verträge hier kündigen"** or an equivalent unambiguous formulation.

**Bestätigungsschaltfläche.** On the confirmation page, labelled with nothing other than **"jetzt kündigen"** or an equivalent unambiguous formulation.

Both buttons and the confirmation page must be **ständig verfügbar sowie unmittelbar und leicht zugänglich** — permanently available, immediately and easily accessible.

## The confirmation page

The confirmation page must let the consumer state:

- the type of termination and, in the case of extraordinary termination, the reason
- their identification
- an identification of the contract
- the date on which the termination is to take effect
- an electronic address for the acknowledgement

After activating the confirmation button, the trader must send an acknowledgement on a durable medium without undue delay, stating the content of the declaration and the **date and time** of receipt, and must make the declaration storable in a form that can be reproduced.

**BGH, 16.07.2026, I ZR 200/25** (preceding instance OLG Düsseldorf, 18.09.2025, 20 UKl 1/25): the confirmation page may contain **nothing beyond what § 312k BGB provides**. Notices about alternatives to termination — pausing the contract free of charge, downgrade offers, retention discounts — are not permitted there. Anything that distracts the consumer or is designed to steer them to a different decision belongs elsewhere or nowhere.

## Placement

- No login before the Kündigungsschaltfläche. Requiring credentials to reach it is incompatible with "unmittelbar und leicht zugänglich".
- Reachable from the page where the contract can be concluded, and in practice from a permanent footer link.
- Not hidden inside a help centre, an FAQ, or a contact form.
- Not behind the consent banner.

## Consequence of getting it wrong

**§ 312k Abs 6 BGB:** where the trader does not provide a compliant Kündigungsbutton, the consumer may terminate the contract **at any time and without observing a notice period**. That is materially worse than a fine: the entire subscriber base can walk out on the day the defect is noticed, and a competitor or Verbraucherzentrale can enforce it by Unterlassungsklage.

## Template

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<!-- Footer link, present on every page, no login in front of it -->
<a href="/kuendigung">Verträge hier kündigen</a>

<!-- /kuendigung — confirmation page, nothing else on it -->
<h1>Vertrag kündigen</h1>
<form method="post" action="/kuendigung/bestaetigen">
  <fieldset>
    <legend>Art der Kündigung</legend>
    <label><input type="radio" name="art" value="ordentlich"> Ordentliche Kündigung</label>
    <label><input type="radio" name="art" value="ausserordentlich"> Außerordentliche Kündigung</label>
    <label for="grund">Kündigungsgrund (bei außerordentlicher Kündigung)</label>
    <textarea id="grund" name="grund"></textarea>
  </fieldset>
  <label for="name">Name</label><input id="name" name="name">
  <label for="vertrag">Bezeichnung des Vertrags / Kundennummer</label><input id="vertrag" name="vertrag">
  <label for="termin">Kündigung zum</label><input id="termin" name="termin" type="date">
  <label for="mail">E-Mail-Adresse für die Bestätigung</label><input id="mail" name="mail" type="email">
  <button type="submit">jetzt kündigen</button>
</form>
<!-- No retention offer, no pause option, no discount, no "Are you sure?" upsell.
     BGH, 16.07.2026, I ZR 200/25. -->
```

## Checkpoints

- [ ] Classification documented: is the contract a Dauerschuldverhältnis against payment concluded via the website
- [ ] One-off payment not used as a reason to skip the button (BGH I ZR 161/24)
- [ ] Button labelled "Verträge hier kündigen" or an unambiguous equivalent, and nothing else
- [ ] Confirmation button labelled "jetzt kündigen" or an unambiguous equivalent
- [ ] Both permanently available, no login, not behind the consent banner, not buried in an FAQ
- [ ] Confirmation page carries all five input fields required by § 312k BGB
- [ ] Confirmation page carries nothing else — no retention offer, pause option or discount (BGH I ZR 200/25)
- [ ] Acknowledgement sent on a durable medium with date and time of receipt
- [ ] Declaration storable and reproducible by the consumer
- [ ] Not confused with the § 356a BGB Widerrufsfunktion or the § 312j Abs 3 BGB order button
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
