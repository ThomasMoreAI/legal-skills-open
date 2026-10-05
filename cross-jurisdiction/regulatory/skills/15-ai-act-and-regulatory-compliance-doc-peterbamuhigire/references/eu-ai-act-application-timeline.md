# EU AI Act Application Timeline (as amended by the Digital Omnibus on AI)

Load when a feature carries an EU AI Act verdict and the compliance doc must state **when** each
obligation bites. Every verdict row in Section 1 of `AI_Act_And_Regulatory_Compliance_Doc.md`
carries an "Applies from" date taken from this table, and every open item in Section 7 carries the
date by which it must close.

## Dated timeline

| Obligation | Applies from | Status of evidence |
|---|---|---|
| Regulation (EU) 2024/1689 (AI Act) entry into force | 1 August 2024 | Unchanged since 2024; not re-checked this cycle |
| Prohibited practices, Art. 5 (prohibitions 1-8) and AI literacy, Art. 4 | 2 February 2025 | Verified (Commission) |
| General-purpose AI model obligations and governance | 2 August 2025 | Verified (Commission) |
| Digital Omnibus on AI, Regulation (EU) 2026/1744, entry into force | 27 July 2026 | Verified (Commission) |
| Digital Omnibus Official Journal publication | 24 July 2026 | `NOT_ASSESSED` from primary text; secondary: NicFab blog and Hunton Andrews Kurth, both July 2026 |
| General date of application; Art. 50 transparency obligations (chatbot disclosure, synthetic-content marking, deep-fake labelling) | 2 August 2026 | Verified (Commission states "August 2026"; the 2 August day is the unchanged general date of application) |
| Art. 50 marking grace for generative systems already on the market before 2 August 2026 | 2 December 2026 | `NOT_ASSESSED` from primary text; secondary: Hunton Andrews Kurth (2026) |
| New prohibition 9: AI systems generating non-consensual intimate imagery or child sexual abuse material | December 2026 | Month verified (Commission); exact day `NOT_ASSESSED` |
| High-risk obligations for stand-alone Annex III systems | 2 December 2027 | Verified (Commission) |
| High-risk obligations for AI embedded in Annex I regulated products | 2 August 2028 | Verified (Commission) |

## Decision rules

1. Take the date from the row matching the feature's verdict. A feature with two verdicts (for
   example an Annex III credit-scoring model that also produces generated text) carries both dates;
   the earlier one sets the first release gate.
2. A deferred date is not an exemption. For an Annex III feature, the SRS still states the Annex IV
   documentation, human-oversight and logging requirements now; the compliance doc records
   2 December 2027 as the date by which conformity evidence must exist.
3. Where the product is sold outside the EU only, record the EU dates as `not applicable` with the
   rollout-plan reference that proves it; do not delete the row.
4. Any row marked `NOT_ASSESSED` above is shown to counsel before sign-off. The compliance doc may
   plan against it but must not cite it as settled law.
5. Re-check this table against EUR-Lex before every baseline: the Omnibus also changed SME
   documentation duties, registration and sandbox provisions whose dates are not captured here.

## Worked example

A Kampala fintech plans an EU launch of a loan pre-screening assistant in March 2027. The scoring
model is Annex III point 5(b) (creditworthiness): applies from 2 December 2027. The chat front end
discloses AI interaction under Art. 50: applies from 2 August 2026, so it is already live law at
launch. Section 7 therefore lists the Art. 50 disclosure as a launch blocker and the Annex IV
evidence pack as due before 2 December 2027, with owners named.

## Evidence/currentness

Accessed 2026-09-24. Primary: European Commission, "AI Act | Shaping Europe's digital future"
(digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, page updated 3 August 2026),
which cites Regulation (EU) 2026/1744 and its 27 July 2026 entry into force. EUR-Lex
(eur-lex.europa.eu/eli/reg/2026/1744/oj) was not retrievable from this environment (bot challenge),
so the Official Journal text itself is `NOT_ASSESSED`. Secondary sources named in the table are
used only where marked. Review by 2027-03-24 or on any further amendment.
