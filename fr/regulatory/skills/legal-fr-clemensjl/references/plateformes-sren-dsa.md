# Plateformes, DSA et loi SREN

Anyone hosting third-party content — comments, reviews, a forum, a marketplace, user uploads — is an intermediary service provider under **règlement (UE) 2022/2065 (DSA)**. France implemented the DSA in national law through **loi n° 2024-449 du 21 mai 2024 (loi SREN)**, which rewrote the LCEN in the process.

## What the loi SREN did to the LCEN

Status as at 2026-08-05. The loi SREN restructured loi n° 2004-575:

- the publisher-identification duties moved out of article 6-III into **article 1-1**, with the criminal offence in **article 1-2** — see `mentions-legales.md`;
- **article 6** was rewritten and, in its current version, defines intermediary service providers (internet access providers, hosting services, search engines, online platforms, social networks, application stores) and their obligations on content moderation, data retention and reporting of illegal activity;
- the takedown provisions formerly in article 6-I-8 moved to **article 6-3**.

Any citation of "article 6-I" or "article 6-III de la LCEN" taken from a pre-2024 template is stale and must be re-checked against the current consolidated text before it is reproduced.

## DSA duties that land on a small site

Not every duty applies to every actor. The order of magnitude, for an ordinary French site hosting user content:

| Duty | Applies to | Where it goes |
|---|---|---|
| Single point of contact for authorities and for users, with the languages accepted | All intermediary services | Mentions légales or a dedicated page |
| Legal representative in the EU | Providers established outside the EU | Mentions légales |
| Terms and conditions stating the moderation rules, tools and human review, in clear language | All intermediary services | CGU |
| Notice and action mechanism, electronic and easy to use | Hosting services | Dedicated form, linked from the content |
| Statement of reasons for every restriction imposed on content or an account | Hosting services | Sent to the affected user |
| Internal complaint-handling system, out-of-court dispute settlement, trusted flaggers, measures against misuse | Online platforms | Product and CGU |
| Ban on dark patterns in the interface | Online platforms | Design review |
| Trader traceability, "know your business customer" | Platforms allowing consumers to conclude distance contracts with traders | Onboarding flow |
| No advertising profiling of minors, no profiling on special-category data | Online platforms | Ad stack |

Microenterprises and small enterprises are exempt from the platform-specific duties in section 3 of the DSA, but not from the baseline duties for hosting services — point of contact, terms, notice and action, statements of reasons.

## Enforcement in France

ARCOM is the French Digital Services Coordinator, working with the DGCCRF and the CNIL on their respective areas. Complaints about a French provider go to ARCOM.

## Age verification for pornographic content

The loi SREN empowers ARCOM to set a binding technical référentiel for verifying the age of users of services distributing pornographic content. ARCOM adopted **délibération n° 2024-20 du 9 octobre 2024** establishing that référentiel, after a favourable opinion of the CNIL of 26 September 2024, with a compliance deadline of three months from adoption. Self-declaration of age is not compliant; the référentiel requires a solution meeting a double-anonymity principle, so that the verifying party does not learn the site visited and the site does not learn the identity. [[UNVERIFIED: any suspension, annulment or amendment of the ARCOM référentiel in 2025 or 2026, and the current status of enforcement against non-EU-established services — check arcom.fr before advising an operator]]

If a project distributes adult content to users in France, this is a blocking issue and must be raised as such before anything else is drafted.

## CGU — what they must contain

CGU are not CGV. Minimum content for a service hosting user content:

- identification of the provider and the applicable law;
- conditions of access, account creation, and the age condition, aligned with article 45 de la loi 78-17 where minors are involved;
- the licence the user grants over content they upload, its scope and duration;
- the rules on prohibited content, stated concretely;
- the moderation policy: what is checked, by automated tools or by humans, with what effects;
- the notice and action route for illegal content;
- the procedure and the statement of reasons when content is removed or an account is restricted, and the internal complaint route;
- suspension and termination, on both sides;
- liability, without clauses that are void against consumers;
- how the CGU may be amended and how users are informed.

## Template — DSA contact and notice block

```html
<!-- BROUILLON – non validé juridiquement -->
<h2>Point de contact (règlement (UE) 2022/2065)</h2>
<p>
  Point de contact unique pour les autorités et pour les utilisateurs :
  <a href="mailto:[[adresse]]">[[adresse]]</a><br>
  Langues acceptées : français, anglais<br>
  [[fournisseur établi hors UE : représentant légal dans l'Union — nom et adresse]]
</p>

<h2>Signaler un contenu illicite</h2>
<p>Toute personne peut signaler un contenu qu'elle estime illicite au moyen du
formulaire [[lien]]. Le signalement précise : l'URL exacte du contenu, les motifs pour
lesquels il est estimé illicite, l'identité et les coordonnées du déclarant, et une
déclaration de bonne foi sur l'exactitude des informations.</p>
<p>Nous accusons réception du signalement, l'examinons et vous informons de la
décision prise ainsi que des voies de recours disponibles. L'auteur du contenu reçoit
un exposé des motifs en cas de restriction.</p>
```

## Checkpoints

- [ ] DSA classification recorded: intermediary, hosting, online platform, marketplace
- [ ] Point of contact published with the accepted languages
- [ ] EU legal representative named, where the provider is established outside the EU
- [ ] Notice and action mechanism reachable electronically and easy to use
- [ ] Statement of reasons issued for every removal or account restriction
- [ ] Moderation rules disclosed in the CGU in clear, plain language
- [ ] Marketplace: trader identification and traceability collected before listing
- [ ] No dark patterns in consent, cancellation, or subscription flows
- [ ] No advertising profiling of minors
- [ ] No stale citation of « article 6-I » or « article 6-III de la LCEN »
- [ ] Adult content: ARCOM age-verification référentiel addressed before launch
- [ ] CGU and CGV kept as separate documents
- [ ] All `[[…]]` placeholders resolved or explicitly reported as open
