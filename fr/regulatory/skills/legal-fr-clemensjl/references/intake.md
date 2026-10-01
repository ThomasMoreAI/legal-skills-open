# Intake

Answer before drafting any text. Missing answers become `[[MISSING: …]]` in the draft and in the report. Never guessed, never filled in with a plausible value.

## Legal entity

1. Legal form — entreprise individuelle, micro-entrepreneur, EURL, SARL, SAS, SASU, SA, SCI, association loi 1901, or a natural person acting non-professionally?
2. Full denomination or company name exactly as registered, plus any nom commercial or enseigne used on the site.
3. Geographic address of the establishment (street, number, postcode, commune, country). A boîte postale is not an address; a domiciliation contract is.
4. **Numéro unique d'identification (SIREN)** and the **SIRET** of the establishment. RCS registration: the city of the greffe. Registration in the **RNE** as an artisan, if applicable.
5. Capital social, for companies.
6. Numéro de TVA intracommunautaire, if the business is VAT-registered. Franchise en base de TVA changes the price display, see `cgv-vente-distance.md`.
7. Telephone number and email address. Article 1-1 I LCEN requires the telephone number; the Code de la consommation requires postal, telephone and electronic contact details (article L111-1 4°).
8. Name of the **directeur de la publication**, in the sense of article 93-2 de la loi n° 82-652 du 29 juillet 1982 — in practice the legal representative unless another person is designated. Responsable de la rédaction, if there is one.
9. Is the site published **à titre non professionnel**? Article 1-1 II LCEN then allows anonymity toward the public, provided the identification data has been given to the host.

## Hosting

10. Hébergeur: name or company name, full postal address, telephone number. Required by article 1-1 I 4° LCEN. The CDN, the domain registrar and the agency are not the hébergeur.
11. Any third party storing data processed in the course of publishing the service, even free of charge (article 1-1 I 5° LCEN).
12. Where are the servers, and does any processing leave the EU?

## Regulated activity

13. Regulated profession or activity subject to authorisation? If yes: professional title, the ordre or professional body, the member state that granted the title, the applicable professional rules and where they can be consulted.
14. Mandatory professional liability insurance? Insurer name, address, and the geographic coverage of the policy.
15. Any supervisory authority for the activity (ACPR, ARCEP, ANSM, ARCOM, AMF, DGCCRF).

## Data processing

16. What is collected — contact form, account, order, newsletter, support, server logs, analytics?
17. Purpose and legal basis per processing (contract, legal obligation, legitimate interest, consent).
18. Retention period or the criterion determining it, per category.
19. Recipients: hosting, payment, shipping, mailing, analytics, CRM, cloud, agencies.
20. Transfers outside the EU: where, and on what basis (adequacy decision, standard contractual clauses, derogations).
21. Sous-traitance contracts under RGPD article 28 signed, with whom, and where they are filed.
22. Profiling, automated decisions, scoring?
23. Special categories under RGPD article 9, or health data, or the NIR?
24. Audience under 15 years old (article 45 de la loi 78-17)? Audience of minors generally?
25. DPO appointed or required (RGPD article 37)? Name and contact details to publish.

## Trackers

26. Full inventory of what is loaded: analytics, tag manager, ads pixels, A/B testing, session replay, chat widget, maps, video embeds, fonts, captcha, social buttons.
27. Which of these can be exempted as audience measurement under CNIL's criteria, and which cannot?
28. Consent management platform in use, and how consent proof is stored.

## Selling

29. Sales to consumers, to professionals, or both?
30. Goods, digital content, digital services, subscriptions, or services performed on site?
31. Target countries and languages — decides which additional consumer law applies.
32. Payment methods and payment service provider; delivery costs, delivery times, delivery restrictions.
33. Automatic renewal? Notice periods? Contract concluded electronically, or capable of being concluded electronically (article L215-1-1)?
34. Digital content with immediate access, requiring the consumer's express prior request and acknowledgement of loss of the right of withdrawal (article L221-28 13°)?
35. Commercial guarantee offered on top of the garantie légale? Duration, scope, who honours it?
36. **Médiateur de la consommation**: which one is contracted, and is it on the CECMC list? Name, postal address, website.

## Size, sector, platform

37. Headcount and annual turnover or balance sheet total — decides the microenterprise exemption in article L412-13 du Code de la consommation (fewer than 10 persons **and** turnover or balance sheet total not exceeding 2 million €).
38. Annual turnover in France above 250 million € — triggers article 47 de la loi n° 2005-102 via décret n° 2019-768.
39. User-generated content, comments, forum, marketplace, hosting for third parties? Then the DSA layer applies, see `plateformes-sren-dsa.md`.
40. Content unsuitable for minors, in particular pornographic content? Then loi SREN and the ARCOM référentiel apply.
41. Physical products sold in France: packaging subject to the info-tri, electrical or electronic equipment subject to the indice de réparabilité or the indice de durabilité, textiles?
42. Influencer or affiliate campaigns planned (loi n° 2023-451)?

## Existing texts, where this is an audit rather than a first draft

43. Which legal pages exist today, at which URLs, and when were they last changed?
44. Where did they come from — a lawyer, a generator, a shop plugin, a translated German or English template, a competitor?
45. Are any of them translations? A translated Impressum is not a mentions légales, and a translated Widerrufsbelehrung is not a notice de rétractation.
46. Do the shop system, the payment provider, the newsletter tool and the marketplace listings carry their own legal strings that were never reviewed? These are where dead ODR links and German provisions survive longest.
47. Are the same texts reused on other domains, subdomains, landing pages or app stores?

## Languages and target markets

48. In which languages is the site published, and are the legal pages available in each of them?
49. Are consumers in other member states targeted — through language, currency, delivery zone or advertising? Their mandatory consumer protections may apply on top of French law.
50. Is there a separate app in the App Store or Google Play, with its own privacy labels that must match the published policy?

## Operational contacts

51. Who receives complaints, data-subject requests, DSA notices and cancellation notifications, and within what internal deadline?
52. Who has authority to sign off a legal text, and has a lawyer been engaged?
53. Where is the evidence kept — consent logs, order confirmations, processor contracts, audits?

## Checkpoints

- [ ] Every answer either supplied or recorded as `[[MISSING: …]]`
- [ ] Hébergeur identified with name, address and telephone number, not the registrar or the agency
- [ ] SIREN, RCS city and capital social confirmed against the actual registration, not from memory
- [ ] Médiateur named and verified against the CECMC list
- [ ] Tracker inventory produced from a real network capture, not from the tag manager configuration
