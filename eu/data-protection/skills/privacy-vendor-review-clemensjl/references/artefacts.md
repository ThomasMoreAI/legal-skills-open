# Question 6 — the artefacts the review must produce

An approval that produces no document is not an approval. Six outputs, every time. Anything not known is `[[MISSING: …]]`; nothing here may be plausibly filled in.

Status as at 2026-08-05.

## 1. Record of processing activities entry (Art 30 GDPR)

A vendor is almost never a processing activity of its own. It is a **recipient inside an existing activity** ("customer support", "order processing", "website operation"). Add it to the existing entry; create a new entry only if the vendor enables a genuinely new purpose.

Art 30(1) requires, for a controller:

| Art 30(1) | Field |
|---|---|
| (a) | Name and contact details of the controller, any joint controller, the representative and the DPO |
| (b) | The purposes of the processing |
| (c) | A description of the categories of data subjects and of the categories of personal data |
| (d) | The categories of recipients to whom the data have been or will be disclosed, **including recipients in third countries or international organisations** |
| (e) | Where applicable, transfers to a third country or an international organisation, **including the identification of that third country**, and — for transfers under the second subparagraph of Art 49(1) — the documentation of suitable safeguards |
| (f) | Where possible, the envisaged time limits for erasure of the different categories of data |
| (g) | Where possible, a general description of the technical and organisational security measures referred to in Art 32(1) |

Art 30(2) sets the processor's record, if you are also a processor to your own customers. Art 30(3): the record must be in writing, including electronic form. Art 30(5) exempts organisations under 250 employees — but not where the processing is likely to result in a risk to rights and freedoms, is not occasional, or includes Art 9 or Art 10 data. A website with continuous analytics is not occasional; the exemption almost never applies in practice, and relying on it removes your ability to answer an authority under Art 30(4).

```yaml
# ropa/[[activity-slug]].yaml
activity: [[e.g. Website operation and product analytics]]
controller:
  name: [[legal entity]]
  contact: [[address, e-mail]]
  dpo: [[name/contact or "not appointed – Art 37 assessment dated …"]]
  joint_controllers: [[entity + Art 26 arrangement reference, or "none"]]
purposes:
  - [[purpose in one sentence]]
data_subjects:
  - [[website visitors / customers / employees]]
categories_of_data:
  - [[online identifiers, IP address, device and browser data]]
  - [[usage events, page URLs, referrer]]
legal_basis:
  - purpose: [[purpose]]
    basis: [[Art 6(1)(a) consent | (b) contract | (c) legal obligation | (f) legitimate interests]]
    note: [[LIA reference if (f); ePrivacy consent also required if the device is touched]]
recipients:
  - name: [[exact contracting entity]]
    role: [[processor | independent controller | joint controller]]
    purpose: [[what they do with it]]
    contract: [[Art 28 DPA dated … | Art 26 arrangement … | data-sharing terms §…]]
    country: [[country of processing]]
    subprocessors_url: [[url]]
transfers:
  - recipient: [[entity]]
    third_country: [[country]]
    mechanism: [[adequacy decision (name it) | SCCs Module [[n]] dated … | Art 49 derogation (name it)]]
    tia: [[reference + date, or "not required – adequacy"]]
    supplementary_measures: [[list, or "none – adequacy"]]
retention:
  - category: [[category]]
    period: [[period]]
    trigger: [[what starts the clock]]
    enforced_by: [[vendor setting name | scheduled job | manual]]
security_measures: [[reference to the TOM document]]
review:
  approved_on: [[date]]
  approved_by: [[name]]
  re_review_due: [[date — no approval without one]]
  vendor_terms_snapshot: [[archive path + vendor "last updated" date]]
```

## 2. Privacy notice paragraph

The published wording belongs to the `legal-*` skills. What this review produces is the **factual content** those texts consume: who receives what, why, on which basis, where it goes and under which safeguard. Art 13(1)(e) requires the recipients or categories of recipients; Art 13(1)(f) requires, for a transfer, the reference to the appropriate safeguards and the means by which to obtain a copy of them; Art 13(2)(a) requires the retention period or the criteria.

```html
<!-- DRAFT – not legally approved -->
<h3>[[Vendor / service name]]</h3>
<p>
  Purpose: [[purpose in plain language]].<br>
  Recipient: [[exact legal entity]], [[address]], acting as [[processor on our behalf | separate controller | joint controller with us]].<br>
  Data: [[categories]].<br>
  Legal basis: [[Art 6(1)(…) GDPR — plus: your consent under [[national ePrivacy provision]] for the storage of and access to information on your device]].<br>
  Transfer: [[none – processing in the EEA | to [[country]] on the basis of [[adequacy decision … | standard contractual clauses under Commission Implementing Decision (EU) 2021/914, Module [[n]]]]. A copy of the safeguards can be obtained at [[contact]].]]<br>
  Retention: [[period]].<br>
  Provider's own privacy information: <a href="[[url]]">[[url]]</a>
</p>
```

German variant for publication in a German-language notice:

```html
<!-- ENTWURF – juristisch nicht freigegeben -->
<h3>[[Dienst]]</h3>
<p>
  Zweck: [[Zweck]].<br>
  Empfänger: [[exakte Rechtsperson]], [[Anschrift]], als [[Auftragsverarbeiter | eigenständig Verantwortlicher | gemeinsam Verantwortlicher]].<br>
  Daten: [[Kategorien]].<br>
  Rechtsgrundlage: [[Art 6 Abs 1 lit … DSGVO]][[; zusätzlich Ihre Einwilligung nach § 165 Abs 3 TKG 2021 für das Speichern von und den Zugriff auf Informationen auf Ihrem Endgerät]].<br>
  Übermittlung: [[keine – Verarbeitung im EWR | in [[Land]] auf Grundlage [[Angemessenheitsbeschluss … | Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914, Modul [[n]]]]. Eine Kopie der Garantien erhalten Sie unter [[Kontakt]].]]<br>
  Speicherdauer: [[Dauer]].<br>
  Datenschutzinformation des Anbieters: <a href="[[url]]">[[url]]</a>
</p>
```

## 3. Consent-manager category assignment

One line per **purpose**, not per vendor. Feeds the CMP configuration directly.

```
vendor:            [[name]]
purpose:           [[purpose]]
category:          [[strictly necessary | functional | analytics | marketing]]
justification:     [[why this category — for "strictly necessary", the service the user explicitly requested]]
blocking method:   [[script not injected until consent | CMP template | click-to-load placeholder]]
hosts to block:    [[host list from the pre-consent capture]]
cookies/storage:   [[names and keys, with lifetimes]]
verified pre-consent silence on: [[date]]
```

## 4. Sub-processor list entry

Two directions, both required:

- **Inbound:** the vendor's own sub-processor list URL, the retrieval date, and the named person subscribed to its change notifications.
- **Outbound:** if you act as a processor for your own customers, this vendor becomes *your* sub-processor and must appear on your published list with its purpose and location, under the notice mechanics your own DPA promises (Art 28(2), Art 28(4)).

```
| Sub-processor | Entity | Purpose | Location | Transfer mechanism | Added |
|---|---|---|---|---|---|
| [[name]] | [[legal entity]] | [[purpose]] | [[country]] | [[mechanism]] | [[date]] |
```

Adding a sub-processor to your own list starts *your* notice period to *your* customers. Do not deploy before the notice period has run.

## 5. Retention statement

```
data at the vendor:   [[category]]
retention:            [[period]]
clock starts at:      [[event]]
enforced by:          [[named vendor setting | scheduled deletion job | manual process + owner]]
backups:              [[backup expiry window]]
end of contract:      [[deletion or return per Art 28(3)(g) — which was chosen]]
verified on:          [[date]]
```

If no vendor setting exists and the terms name no period, the value is `[[MISSING: retention period — no vendor control found]]`. "As long as necessary" is not a retention period and cannot go into Art 30(1)(f) or Art 13(2)(a).

## 6. DPIA trigger result

One line: triggered or not, with the reasoning and the criteria hit. See `dpia.md`. A "not triggered" result is itself the record that the assessment was made — Art 5(2).

## Checkpoints

- [ ] ROPA entry added to the correct existing activity, not created as a duplicate activity
- [ ] Art 30(1)(a) to (g) all populated or explicitly `[[MISSING: …]]`
- [ ] Third country identified by name in (e), and the safeguard named, not described as "appropriate"
- [ ] Legal basis recorded per purpose, not per vendor
- [ ] Notice paragraph names the exact legal entity, not the brand
- [ ] Notice states both the Art 6 basis and, where the device is touched, the ePrivacy consent
- [ ] Art 13(1)(f) "means to obtain a copy" of the safeguards is answerable by a real contact
- [ ] Consent category justified against the service the user explicitly requested
- [ ] Blocking method and host list recorded, and pre-consent silence verified on a date
- [ ] Inbound sub-processor notification has a named subscriber
- [ ] Outbound sub-processor list updated and the customer notice period observed before deployment
- [ ] Retention period tied to a named setting or a named job, not to a sentence
- [ ] DPIA trigger result recorded either way
- [ ] Approval carries a re-review date and an archived snapshot of the vendor terms
- [ ] Draft marker still present until sign-off
