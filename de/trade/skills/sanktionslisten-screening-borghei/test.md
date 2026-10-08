---
skill: aussenwirtschaft-zoll-sanktionen/sanktionslisten-screening
fact_pattern: |
  Beim Onboarding eines neuen B2B-Kunden (Zypern-GmbH) zeigt das
  Screening-Tool einen möglichen Treffer auf einen Geschäftsführer in
  der konsolidierten EU-Liste (Anhang I VO 269/2014, Russland-Maßnahmen).
  Name und Staatsangehörigkeit stimmen überein, Geburtsdatum weicht um
  wenige Tage ab. Die Zypern-GmbH hält 60 % an einer deutschen
  Vertriebs-GmbH, die als Kunde eingebunden werden soll. Mandantin
  (Exporteur, Maschinenbau) fragt, ob Vertragsschluss zulässig ist,
  welche Meldepflichten greifen und welche Strafbarkeitsrisiken bestehen.

must_cite:
  - "VO (EU) 269/2014"
  - "Art. 2"
  - "AWG"
  - "§ 18 AWG"
  - "Art. 215 AEUV"

must_appear:
  - "Bereitstellungsverbot"
  - "False positive"
  - "indirekt"
  - "wirtschaftliche Ressource"
  - "Frostung"
  - "Bundesbank"
  - "BAFA"
  - "Stand der Liste"

must_flag:
  - "Mehrheitsbeteiligung"
  - "indirekte Bereitstellung"
  - "Strafbarkeitsrisiko § 18 AWG"
---

# Test — sanktionslisten-screening

Struktureller Smoke-Test. Bereitstellungsverbot Art. 2 (direkt/indirekt) muss adressiert sein; Frostung und Meldepflichten an Bundesbank/BAFA müssen explizit erwähnt werden; § 18 AWG-Strafbarkeitshinweis ist Pflicht; > 50%-Kontrollregel ist zu adressieren.

Run: `python ../../../scripts/eval.py --skill aussenwirtschaft-zoll-sanktionen/skills/sanktionslisten-screening`
