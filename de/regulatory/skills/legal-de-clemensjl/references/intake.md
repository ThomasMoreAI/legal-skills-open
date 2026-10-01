# Intake questionnaire

Answer before the first legal text is written. Missing answers become `[[MISSING: …]]` in the draft — never guessed.

Ask in blocks, not one question at a time. Where the project already has legal texts, run the "Existing texts" block first: it usually shortens the rest and it surfaces the stale-template problem immediately.

## Existing texts

0a. Are there existing Impressum, Datenschutzerklärung, AGB, Widerrufsbelehrung or cookie texts? Where do they live — CMS page, shop system, plugin, hard-coded template, e-mail template?
0b. Where did they come from — a generator, an agency, a lawyer, another country's site, an older project? Name the source.
0c. Do they cite § 5 TMG, § 25 TTDSG, § 55 RStV, the NetzDG, the EU ODR platform, or any Austrian norm? Any of these means the text is rewritten, not patched.
0d. When were they last reviewed, and by whom?

## Legal entity

1. Legal form — Einzelunternehmen, GbR, OHG, KG, GmbH, UG (haftungsbeschränkt), AG, eG, e.V., private individual?
2. Full name or Firma exactly as registered, in that spelling
3. Geographic address of the place of establishment (street, number, postcode, town, country). A PO box does not satisfy § 5 Abs 1 Nr 1 DDG.
4. Handelsregister: registering Amtsgericht and number (HRA for Personengesellschaften, HRB for Kapitalgesellschaften). Vereinsregister number and Amtsgericht for an e.V., Genossenschaftsregister for an eG.
5. Vertretungsberechtigte: all Geschäftsführer (§ 35a Abs 1 GmbHG), Vorstand and chair of the Aufsichtsrat (§ 80 Abs 1 AktG), Vorstand of the Verein
6. USt-IdNr. under § 27a UStG (format DE plus nine digits) — or Wirtschafts-Identifikationsnummer. Kleinunternehmer under § 19 UStG usually have neither; then the field is omitted, not invented.
7. E-mail address and a second channel for fast contact (telephone, callback form)
8. Is the company in Liquidation or Abwicklung? § 5 Abs 1 Nr 7 DDG requires the statement for certain company forms.

## Regulated activity

9. Does the activity require an official Zulassung (§ 5 Abs 1 Nr 3 DDG)? If so: which supervisory authority, with address and website.
10. Regulated profession under Richtlinie 2005/36/EG — Rechtsanwalt, Steuerberater, Arzt, Architekt, Versicherungsvermittler, Immobilienmakler, Handwerk requiring Meisterpflicht? Then: Kammer, Berufsbezeichnung, state that conferred it, applicable Berufsrecht and where it can be accessed (§ 5 Abs 1 Nr 5 DDG).
11. Gewerbeanmeldung / Handwerksrolle / § 34c GewO or § 34d GewO permit — issuing authority and register entry.

## Media law

12. Does the site carry journalistic-editorial content (blog, magazine, news section, curated editorial output)? If yes, § 18 Abs 2 MStV requires a named Verantwortlicher.
13. Name and address of that Verantwortlicher — a natural person, permanently resident in Germany, with full legal capacity and prosecutable (§ 18 Abs 2 Satz 2 MStV).
14. Are posts on a social-media telemedium generated automatically by a program controlling the account? § 18 Abs 3 MStV requires labelling.

## Data processing

15. What data is collected — contact form, account, order, newsletter, support, server logs?
16. Purpose and legal basis per processing operation (Art 6 Abs 1 DSGVO: contract, legal obligation, legitimate interest, consent)
17. Retention period per category, or the criterion used to determine it
18. Recipients: hosting, payment provider, shipping, mail delivery, analytics, CRM, cloud
19. Third-country transfers — where to and on what basis (adequacy decision, SCC plus transfer impact assessment)
20. Auftragsverarbeitungsverträge under Art 28 DSGVO concluded — with whom, filed where?
21. Profiling, automated decisions, scoring?
22. Special categories under Art 9 DSGVO?
23. Target audience under 16? Art 8 Abs 1 DSGVO applies unchanged in Germany.
24. Headcount of persons regularly and permanently engaged in automated processing — decides the § 38 Abs 1 BDSG DPO threshold of 20.
25. Employee data processed beyond payroll — § 26 BDSG, works agreements, works council involvement?

## Selling

26. Consumers, businesses, or both?
27. Goods, digital content, digital services, subscriptions, or on-site services?
28. Target countries and languages — determines which additional consumer law applies
29. Payment methods and payment service provider
30. Shipping costs, delivery times, delivery restrictions
31. Digital content with immediate access? Then the two declarations under § 356 Abs 5 BGB are needed before the withdrawal right lapses.
32. Subscription or other continuing obligation concluded online? Then § 312k BGB applies.
33. Manufacturer or seller guarantee planned in addition to the statutory Gewährleistung?
34. Is a third-party online marketplace operated (§ 312l BGB, Art 246d EGBGB)?

## Size and special regimes

35. Headcount and annual turnover or balance sheet total — decides the Kleinstunternehmen exemption in § 3 Abs 3 BFSG (fewer than 10 persons and turnover or balance sheet total of at most 2 million euro) and the § 36 Abs 3 VSBG exemption (ten or fewer persons on 31 December of the previous year)
36. Products manufactured, imported or traded? The BFSG micro-enterprise exemption covers services only, not products.
37. Packaging shipped to end users? Then registration in the Verpackungsregister LUCID precedes the first shipment.
38. Electricals, batteries, or textiles sold? Then stiftung ear, BattDG and TextilKennzG duties apply.
39. User-generated content, comments, forum, marketplace, hosting for third parties? Then DSA duties apply.
40. Newsletter or other electronic direct advertising planned?

## Technical stack

41. Hosting provider and the location of the servers
42. CDN, image service, font source, map service, video embeds, captcha, chat widget, error tracking
43. Analytics and tag management, and whether anything currently fires before a consent decision
44. Consent management platform in use, and whether the reject option is on the first layer
45. Shop or booking system, payment service provider, e-mail delivery service
46. Which of these are configured as Auftragsverarbeiter and where the contracts are filed

## Practical constraints

47. Who signs off legally — an in-house lawyer, an external firm, nobody yet? Until sign-off, every draft keeps the marker.
48. Go-live date, and which obligations have a hard external date attached — § 356a BGB since 19.06.2026, BFSG since 28.06.2025, VerpackDG from 12.08.2026
49. Is the operator willing to publish a home address, or does a business address need to be arranged first? This is a decision, not a wording problem.
50. Languages the site is published in — every mandatory text must exist in each language actually offered to consumers
