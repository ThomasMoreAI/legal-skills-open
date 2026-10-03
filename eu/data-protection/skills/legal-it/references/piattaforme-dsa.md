# Platforms, hosting and the DSA

Applies as soon as the site stores or transmits content supplied by third parties: comments, reviews, a forum, a marketplace, file uploads, user profiles, a chat.

## Which category

Regulation (EU) 2022/2065 (Digital Services Act) is directly applicable — there is no Italian transposition to look up for the substantive duties. It layers duties cumulatively:

| Category | Typical example | Duties |
|---|---|---|
| Intermediary service | any of the below | contact point, legal representative if not established in the EU, terms transparency, transparency reporting |
| Hosting service | comment section, file upload, review section | + notice and action mechanism, statement of reasons for every restriction, reporting suspicion of criminal offences |
| Online platform (hosting that disseminates to the public) | forum, marketplace, social feature | + internal complaint-handling system, out-of-court dispute settlement, trusted flaggers, measures against misuse, no dark patterns, advertising transparency, protection of minors, no ads to minors based on profiling |
| Online marketplace | third-party sellers | + trader traceability (know your business customer) |

**Micro and small enterprises are exempt from the online-platform-specific duties** (fewer than 50 persons and annual turnover or balance sheet total not exceeding EUR 10 million), unless designated as a very large online platform. The hosting-level duties — notice and action, statement of reasons — remain. Record the headcount and turnover figures with a date if the exemption is relied on.

A shop's own review section, where reviews are written by customers and displayed publicly, is hosting at minimum. A shop that lists third-party sellers is a marketplace.

## Italian enforcement

The **Autorità per le garanzie nelle comunicazioni (AGCOM)** is Italy's **Digital Services Coordinator** under the DSA. Confirmed on the European Commission's official list of Digital Services Coordinators. Status as at 2026-08-05.

Practical effect: complaints about an Italian provider's DSA compliance land at AGCOM, and AGCOM can request information and act on orders. AGCOM publishes an annual DSA report.

[[UNVERIFIED: the Italian norm that formally designated AGCOM as Digital Services Coordinator and conferred its national enforcement powers. AGCOM's designation itself is confirmed by the Commission's DSC list; the designating Italian act could not be read from an official source. Verify on agcom.it or normattiva.it before citing a law number.]]

## Liability of intermediaries — the articles everybody still cites are gone

**Articles 14, 15, 16 and 17 of D.Lgs 9 aprile 2003 n. 70** — *mere conduit*, *caching*, *hosting*, *assenza dell'obbligo generale di sorveglianza* — were **abrogated by D.Lgs 25 marzo 2024 n. 50, with effect from 2 May 2024**. All four articles now carry only the abrogation note in the consolidated text on normattiva.it. Verified 2026-08-05.

This matches DSA art. 89, which deleted artt. 12 to 15 of Directive 2000/31/EC. The liability regime for intermediaries is now **artt. 4, 5, 6 and 8 of Regulation (EU) 2022/2065**, directly applicable, with nothing to look up in Italian law.

Any text, terms page or memo citing "art. 16 D.Lgs 70/2003" for hosting liability, or "art. 17 D.Lgs 70/2003" for the absence of a general monitoring obligation, is citing an abrogated provision. Rewrite it against the DSA articles; do not patch the number.

[[UNVERIFIED: the specific article of D.Lgs 25 marzo 2024 n. 50 that enacts the abrogation. The abrogation itself is stated four times in the consolidated text of D.Lgs 70/2003 with the date 02.05.2024, so treat it as settled; only the abrogating provision's number is open. D.Lgs 50/2024 is the correttivo to the TUSMA (D.Lgs 208/2021).]]

Note that **art. 7 D.Lgs 70/2003 (general information duties) and art. 21 (sanctions) remain in force** — the abrogation hit only the liability chapter. See `identificazione-sito.md`.

Two things that do not change:

- **there is no liability privilege for the provider's own content.** The exemptions protect the storage or transmission of information supplied by a recipient of the service. Product descriptions, blog posts, the shop's own claims: full liability.
- **actual knowledge ends the exemption.** Once a sufficiently precise and adequately substantiated notice arrives, the provider must act expeditiously. An unread abuse inbox is not a defence.

## Statement of reasons

Every restriction imposed on user content — removal, demotion, demonetisation, account suspension — requires a statement of reasons to the affected user, and it must be specific: which content, which ground in the terms or in law, whether automated means were used, and how to complain. A generic "violates our guidelines" does not satisfy it.

Standard terms must therefore actually contain the moderation rules the provider intends to enforce. Terms that say nothing about moderation cannot support a statement of reasons that cites them.

## Template — platform section for the site

```html
<!-- BOZZA – non approvata legalmente -->
<h2>Segnalazione di contenuti illegali</h2>
<p>
  Chiunque può segnalare la presenza di contenuti che ritiene illegali
  utilizzando il modulo disponibile all'indirizzo [[URL del modulo]] oppure
  scrivendo a <a href="mailto:[[indirizzo]]">[[indirizzo]]</a>.
</p>
<p>La segnalazione deve contenere:</p>
<ul>
  <li>la motivazione per cui il contenuto è ritenuto illegale;</li>
  <li>l'indicazione esatta della posizione del contenuto, di norma l'URL;</li>
  <li>il nome e l'indirizzo e-mail del segnalante, salvo i casi in cui non sono richiesti;</li>
  <li>una dichiarazione di buona fede sulla completezza e accuratezza della segnalazione.</li>
</ul>
<p>
  Confermiamo il ricevimento della segnalazione e comunichiamo la decisione
  adottata, con la relativa motivazione, senza indebito ritardo.
</p>

<h2>Punto di contatto</h2>
<p>
  Punto di contatto per le autorità e per i destinatari del servizio:
  <a href="mailto:[[indirizzo]]">[[indirizzo]]</a>.<br>
  Lingue di comunicazione: italiano, inglese.
</p>

<h2>Reclami contro le nostre decisioni</h2>
<p>
  Contro le decisioni di rimozione, limitazione, sospensione o disattivazione è
  possibile presentare reclamo entro sei mesi scrivendo a
  <a href="mailto:[[indirizzo]]">[[indirizzo]]</a>. Il reclamo è esaminato da
  personale qualificato e non esclusivamente con mezzi automatizzati.
</p>

<h2>Moderazione dei contenuti</h2>
<p>
  [[Descrizione delle regole di moderazione effettivamente applicate, degli
  strumenti automatizzati impiegati e dei relativi criteri]]
</p>
```

## Checkpoints

- [ ] Category determined and written down: intermediary, hosting, online platform, marketplace
- [ ] Micro/small exemption, if relied on, documented with headcount and turnover as at a stated date
- [ ] Contact point published and actually monitored
- [ ] Legal representative appointed if the provider is not established in the EU
- [ ] Notice and action mechanism reachable without an account
- [ ] Statement of reasons produced for every restriction, naming the specific ground
- [ ] Internal complaint mechanism available for six months after the decision, with human review
- [ ] Moderation rules disclosed in the terms, in the form actually applied
- [ ] Marketplace: seller identity, contact details and self-certification collected before listing
- [ ] No dark patterns in the interface
- [ ] No advertising targeted at minors on the basis of profiling
- [ ] Advertising clearly labelled, with the payer identified
- [ ] No liability privilege claimed for the provider's own content
- [ ] No citation of artt. 14-17 D.Lgs 70/2003 anywhere in the project — abrogated 02.05.2024
- [ ] All `[[…]]` placeholders resolved or reported as open
