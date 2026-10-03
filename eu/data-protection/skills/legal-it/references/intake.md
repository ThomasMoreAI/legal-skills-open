# Intake questionnaire

Answer before the first legal text is drafted. Unanswered items become `[[MISSING: …]]` in the draft and in the report back to the user. Never guessed, never plausibly filled in.

Italian identification duties are unusually granular — partita IVA, REA number, capitale sociale, PEC, socio unico. A template that omits one of them is not "mostly right", it is formally defective under art. 2250 Codice Civile and art. 7 D.Lgs 70/2003.

## Legal person

1. Legal form — ditta individuale, libero professionista, S.r.l., S.r.l.s., S.p.A., S.n.c., S.a.s., società cooperativa, associazione, ente non commerciale, private individual?
2. Full denominazione or ragione sociale exactly as registered, including the legal-form suffix
3. Registered office (*sede legale*): via, numero civico, CAP, comune, provincia, country. Also the operational office if different
4. **Partita IVA** — the eleven-digit number. If none, say so explicitly and state why (private individual, occasional activity, regime forfettario still has one)
5. **Codice fiscale** — for a company often identical to the partita IVA; for a ditta individuale it is the owner's personal code and its publication is a decision to take consciously
6. **Registro delle imprese**: which Camera di Commercio, the iscrizione number, and the **numero REA** with its province prefix
7. **Capitale sociale**: amount subscribed and amount paid in (*versato*), for companies where art. 2250 c.c. requires it
8. **Socio unico** — is there a single shareholder? This must be disclosed
9. **Stato di liquidazione** — is the company in liquidation? This must be disclosed
10. Legal representatives (*amministratore unico*, *consiglio di amministrazione*), and *direttore responsabile* if the site carries an editorial product
11. **PEC / domicilio digitale** registered in INI-PEC
12. Email address and a second channel through which a user can reach the provider rapidly and directly (telephone, or a form plus a published address)

## Regulated activity and supervision

13. Is the activity subject to authorisation, licence or a professional register (albo)? If yes: the albo, the region or province of registration, the registration number, the professional title and the state that conferred it
14. Supervisory authority, if the activity is supervised
15. Has a SCIA been filed with the SUAP of the comune for online selling, or is the activity outside that duty? Record the date and protocol number if filed
16. Sector-specific regimes: food, alcohol, supplements, cosmetics, medical devices, financial services, gambling, tobacco. Any of these adds duties this skill does not cover

## Processing of personal data

17. What is collected — contact form, account, order, newsletter, support ticket, server logs, session recording?
18. Purpose and **legal basis per processing** (contract, legal obligation, legitimate interest, consent). Do not default to consent
19. Retention period, or the criterion that determines it, per category
20. Recipients: hosting, payment provider, carrier, mailing platform, analytics, CRM, cloud, accountant
21. Transfers outside the EEA: to which country, on which basis (adequacy decision, standard contractual clauses, derogations)
22. Data processing agreements under Art 28 GDPR — signed with whom, filed where
23. Profiling, automated decision-making, scoring?
24. Special categories under Art 9 GDPR (health, religion, biometrics, sex life, trade union, political opinion) or criminal data under Art 10?
25. **Are minors under 14 in the audience?** Article 2-quinquies Codice Privacy sets the Italian digital consent age at 14, not 16
26. Is a DPO (*responsabile della protezione dei dati*) appointed or required? If appointed, have the contact details been notified to the Garante?
27. **Employees or collaborators using company IT?** Email, MDM, VPN logs, badge systems, analytics on internal tools all engage art. 4 Statuto dei Lavoratori
28. Has a *registro delle attività di trattamento* been created (Art 30 GDPR)?

## Selling

29. Sale to consumers, to businesses, or to both? The Codice del Consumo applies only to the B2C leg
30. Goods, digital content, digital services, subscriptions, or services performed on site?
31. Target countries and languages — determines which additional consumer law bites
32. Payment methods and payment service providers
33. Delivery costs, delivery times, delivery restrictions — all three must be disclosed before the order
34. Digital content with immediate access? Then the consumer's express request and acknowledgement of loss of the withdrawal right must be captured separately
35. Subscription with automatic renewal? Renewal terms, notice periods, cancellation route
36. Commercial guarantee (*garanzia convenzionale*) offered on top of the *garanzia legale di conformità*?
37. Second-hand goods sold to consumers? The conformity period can be shortened only within the limits the Codice del Consumo allows and only by express agreement
38. Price reduction announcements, sales, "prezzo consigliato" comparisons? Then the 30-day lowest-price rule applies
39. Consumer reviews displayed? Then the authenticity-verification statement is mandatory
40. Marketplace hosting third-party sellers?

## Size and special regimes

41. Headcount and annual turnover or balance sheet total — decides the microenterprise exemption for services under the European Accessibility Act, and feeds the Legge Stanca EUR 500 million threshold
42. Are products manufactured, imported or distributed? The microenterprise exemption covers services only
43. User-generated content, comments, forum, marketplace, hosting for third parties? Then DSA duties apply
44. Newsletter, SMS, telephone marketing planned?
45. Influencer or affiliate collaborations planned? Follower counts of the collaborators matter for the AGCOM regime
46. Existing legal texts on the site — where did they come from? A German or generic-EU origin means rewrite, not patch

## Immediate red flags

Ask these first; a "yes" changes the whole workload:

- German norms in an existing text (`§ 5 TMG`, `DDG`, `Widerrufsrecht`, `Amtsgericht`, `Impressum`)
- a link to the EU ODR platform anywhere in the project
- tracking scripts firing before a consent decision
- an order button not labelled with a payment obligation
- consent asked for processing that runs on contract or legal obligation
- children under 14 in the audience
