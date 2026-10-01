# APP 5 collection notice

The most routinely omitted obligation in Australian privacy practice, because teams assume the privacy policy covers it. It does not. Status as at 2026-08-05. Source: OAIC, *APP Guidelines* Chapter 5.

## The obligation

APP 5.1: at or before the time an APP entity collects personal information about an individual, or if that is not practicable as soon as practicable after, the entity must take such steps as are reasonable in the circumstances to notify the individual of the APP 5.2 matters, or to ensure the individual is aware of them.

It applies to information collected **from the individual** and to information collected **about the individual from someone else** — the second case is the one that gets missed, and it is why buying or appending a contact list creates an immediate notification obligation.

## APP 5.2 — the matters

| | Matter |
|---|---|
| (a) | the entity's identity and contact details |
| (b) | if the information is collected from someone else, or the individual may not be aware that it has been collected, the fact and the circumstances of collection |
| (c) | if the collection is required or authorised by or under an Australian law or a court or tribunal order, that fact and the name of the law or order |
| (d) | the purposes of collection |
| (e) | the main consequences for the individual if all or some of the information is not collected |
| (f) | any other APP entity, body or person, or the kinds of them, to which the entity usually discloses information of that kind |
| (g) | that the entity's APP privacy policy contains information about how to access and seek correction of personal information |
| (h) | that the privacy policy contains information about how to complain about a breach of the APPs and how the entity will deal with a complaint |
| (i) | whether the entity is likely to disclose the information to overseas recipients |
| (j) | if so, the countries in which those recipients are likely to be located, if practicable to specify them |

Only (g) and (h) may be discharged by pointing at the privacy policy. Everything else has to be said at the point of collection.

## Placement

The notice belongs where the collection happens and must be visible before the person acts:

- **Contact form** — a short notice above or beside the submit control, not in a tooltip.
- **Account signup** — on the form, before the create-account control.
- **Checkout** — at the point where customer details are entered, covering payment processing and delivery disclosures.
- **Newsletter signup** — combined with the consent wording, but distinct from it. Consent under the Spam Act and notice under APP 5 are different things and both are required.
- **Job applications** — covers referees, background checks and the fact that information will be collected from third parties.
- **Telephone and in person** — a spoken short-form notice, with the full notice available afterwards.
- **Analytics and server logs** — where the entity treats the data as personal information, the notice sits in the layered notice reachable from every page; see `cookies-and-tracking.md`.

A layered approach is acceptable: a short notice at the point of collection carrying (a), (d), (e), (f) and (i), with a link to the full notice carrying the rest. A link alone is not.

## Templates

**Short notice — contact form**

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<p class="collection-notice">
  [[Entity name]] (ABN [[ABN]]) collects the details you enter here so we can respond to
  your enquiry. If you do not provide them we cannot reply. We disclose these details to
  our email and hosting providers, [[named]], located in [[countries]]. Our
  <a href="/privacy">Privacy Policy</a> explains how to access or correct your information
  and how to make a privacy complaint.
</p>
```

**Checkout notice**

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<p class="collection-notice">
  We collect your name, contact details and delivery address to process and deliver your
  order, and your payment details are collected directly by [[payment provider]]. Without
  them we cannot complete the order. We disclose your details to [[payment provider]],
  [[delivery carrier]] and [[fraud prevention provider]]; [[named recipients]] are located
  in [[countries]]. See our <a href="/privacy">Privacy Policy</a> for access, correction
  and complaints.
</p>
```

**Newsletter signup — notice plus Spam Act consent, kept separate**

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<label>
  <input type="checkbox" name="marketing-consent" value="yes">
  Yes, send me [[what: product updates and offers]] by email from [[entity name]].
  You can unsubscribe at any time.
</label>
<p class="collection-notice">
  [[Entity name]] (ABN [[ABN]]) collects your email address to send you the messages you
  ask for. We disclose it to our email provider [[name]] in [[country]]. Our
  <a href="/privacy">Privacy Policy</a> explains access, correction and complaints.
</p>
```

The checkbox must not be pre-ticked and must not be bundled with acceptance of terms.

**Collection from a third party**

```html
<!-- DRAFT – NOT LEGALLY APPROVED -->
<p>
  [[Entity name]] (ABN [[ABN]]) obtained your contact details from [[source]] on
  [[date]] in order to [[purpose]]. We usually disclose details of this kind to
  [[recipients]] in [[countries]]. You can ask us to stop contacting you at any time by
  [[route]]. Our <a href="/privacy">Privacy Policy</a> explains how to access or correct
  your information and how to complain.
</p>
```

## What a collection notice is not

- Not a cookie consent banner. There is no consent requirement to notify against.
- Not the privacy policy. The policy is APP 1.4; the notice is APP 5.2; both are required.
- Not a terms-of-service acceptance. Bundling the notice into a tick-to-accept control makes it harder to argue the person was made aware of it, and creates unfair contract term risk in the terms themselves.
- Not a one-time event. A new collection for a materially new purpose needs a new notice.

## Checkpoints

- [ ] A notice exists at every point of collection, listed against the actual forms in the codebase
- [ ] Each notice carries the APP 5.2 matters other than (g) and (h), or links to a full notice that does
- [ ] Consequences of not providing the information stated concretely, not as "we may be unable to assist"
- [ ] Usual recipients named by entity or by kind, matching the vendor list
- [ ] Overseas recipients and countries stated
- [ ] Third-party collection notified, including list purchases, enrichment and referral programs
- [ ] Notice appears before the submit control, not after submission
- [ ] Marketing consent is a separate, unticked control from the notice
- [ ] Every `[[…]]` resolved or reported as `[[MISSING: …]]`
