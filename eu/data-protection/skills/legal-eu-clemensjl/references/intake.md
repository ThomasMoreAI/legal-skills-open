# Intake

Answer before drafting anything. Unanswered items become `[[MISSING: …]]` in the draft and in the report back to the user. Never guessed, never plausibly filled in.

The EU layer is only half the answer. Question 1 decides which national skill has to run afterwards; question 2 decides whether EU law reaches the operator at all.

## Reach and establishment

1. **Member state(s) of establishment.** Which one is the main establishment (GDPR Art 4(16))? If none, is there an establishment anywhere in the EU?
2. **If no EU establishment:** are goods or services offered to data subjects in the Union, or is their behaviour monitored (GDPR Art 3(2))? If yes, an Art 27 representative is needed unless Art 27(2) applies.
3. **Target member states and languages.** Determines which consumer regimes apply on top and which national transposition governs the withdrawal period, the guarantee period and the ADR body.
4. **Sectors served** — consumers, businesses, public bodies, or a mix. Consumer directives apply only to B2C.
5. **Company size:** headcount, annual turnover, balance sheet total. Decides the DSA Art 19 micro/small exemption, the EAA microenterprise exemption for services, the GDPR Art 30(5) records carve-out and the P2B and NIS2 thresholds.

## Legal entity and disclosures

6. Exact legal name, legal form, registered office address (geographic, not a PO box).
7. Commercial register name, number and court, where registered.
8. VAT identification number, where held.
9. Names of the persons authorised to represent the entity.
10. Regulated activity or profession? If yes: professional title, granting member state, supervisory authority, applicable professional rules and where they can be consulted.
11. Contact channels: an email address plus at least one further channel allowing rapid and direct communication.

## Data processing

12. What data is collected, in which context — server logs, contact form, account, order, newsletter, support, telemetry, uploads?
13. Purpose and legal basis under Art 6(1) for **each** processing. Not one basis for the whole site.
14. Where legitimate interest is claimed: the interest, the necessity, and the balancing (Art 6(1)(f)).
15. Retention period, or the criteria used to set one, per category.
16. Recipients and categories of recipient: hosting, CDN, payment, shipping, email, analytics, CRM, support, cloud, AI vendors.
17. Transfers outside the EEA: which countries, which providers, which Chapter V basis for each.
18. Processor contracts under Art 28(3) concluded — with whom, held where?
19. Joint controllership with anyone (Art 26)? Arrangement in place?
20. Special categories under Art 9(1) — health, biometrics for identification, religion, political opinion, trade union membership, sex life, sexual orientation, racial or ethnic origin, genetic data?
21. Criminal convictions and offences data (Art 10)?
22. Profiling, automated individual decision-making, scoring (Art 22)?
23. Children as users or as a target group? Which member states — the digital consent age varies from 13 to 16 (Art 8).
24. Data protection officer appointed, or required under Art 37(1)?
25. Records of processing maintained (Art 30)? Breach procedure defined (Art 33/34)? DPIA screening done (Art 35)?

## Terminal equipment and marketing

26. Every cookie, `localStorage`, `sessionStorage`, IndexedDB entry, pixel, beacon, fingerprinting technique and embedded third-party resource, listed with purpose.
27. Which of those are claimed as strictly necessary, and on what reasoning per item?
28. Consent management platform in use, and how consent is logged.
29. Email or SMS marketing planned? Is a soft opt-in relationship being relied on (Art 13(2) ePrivacy Directive)?
30. Any cookie wall or pay-or-consent model?

## Selling

31. Goods, digital content, digital services, subscriptions, or services performed in person?
32. Is personal data accepted as counter-performance instead of money (Art 3(1) Dir (EU) 2019/770)?
33. Prices: total price including taxes, delivery charges, and how they are displayed before the order button.
34. Price reduction announcements or "was/now" pricing used?
35. Consumer reviews displayed? Is authenticity verified, and how?
36. Personalised pricing based on automated decision-making?
37. Subscription with automatic renewal? Renewal term, notice period, termination route?
38. Delivery times, delivery restrictions, payment methods.
39. Digital content with immediate access — is the express prior consent plus acknowledgement flow built (loss of withdrawal right)?
40. Commercial guarantee offered on top of the statutory conformity regime?

## Platform and product

41. Does the service host third-party content — comments, forum, reviews, uploads, listings, marketplace?
42. Does it allow consumers to conclude distance contracts with traders (triggers DSA Art 30)?
43. Are ads shown? Are they targeted? Are minors among the recipients?
44. Are ranking, recommendation or search results ordered by parameters the user does not set?
45. Are physical products placed on the EU market (GPSR)? Who is the responsible person established in the Union?
46. Is the service an online intermediation service or online search engine used by business users (P2B)?
47. Is any AI system used, and in what role — provider or deployer? Any generative output shown to users? Any chatbot?
48. Connected products or related services generating data (Data Act)? Cloud or data processing services offered (switching duties)?
49. Does the entity fall in an Annex I or Annex II sector of NIS2 and above the size cap?

## Accessibility

50. Is a service listed in Art 2(2) of Directive (EU) 2019/882 provided to consumers — in particular e-commerce, e-books, banking, transport or electronic communications?
51. Microenterprise status claimed for the EAA service exemption? Headcount below 10 **and** annual turnover or balance sheet total not exceeding EUR 2 million — documented?
52. Are products in EAA scope (consumer terminal equipment, e-readers, self-service terminals) placed on the market? The microenterprise exemption does not cover products.
