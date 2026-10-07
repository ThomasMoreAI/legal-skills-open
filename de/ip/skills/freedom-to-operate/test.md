---
skill: patentrecht/freedom-to-operate
fact_pattern: |
  Mandantin (deutscher Medizingerätehersteller) plant in 6 Monaten
  Markteintritt mit einem neuen chirurgischen Instrument in DE und
  weiteren EU-Ländern. Vor Marktstart soll geklärt werden, ob das
  geplante Produkt fremde Patente / Gebrauchsmuster verletzt. Es
  ist nicht klar, ob Wettbewerber bereits Schutzrechte angemeldet
  haben; jüngere Anmeldungen können wegen § 32 V PatG noch nicht
  öffentlich sein. Es besteht der Wunsch, im Fall eines Treffers
  Handlungsoptionen (Designaround, Lizenz, Nichtigkeitsantrag)
  rechtssicher abzuwägen.

must_cite:
  - "§ 14 PatG"
  - "§ 32 PatG"
  - "§ 59 PatG"
  - "§ 81 PatG"
  - "Art. 69 EPÜ"
  - "Art. 99 EPÜ"
  - "Art. 138 EPÜ"

must_appear:
  - "DEPATISnet"
  - "Espacenet"
  - "Patentscope"
  - "Merkmalsgliederung"
  - "Äquivalenz"
  - "Schneidmesser"
  - "Designaround"
  - "Nichtigkeitsantrag"
  - "Einspruch"
  - "18-Monats"
  - "Lebensphase"

must_flag:
  - "Recherchestand"
  - "Re-Check vor Markteintritt"
  - "§ 32 V PatG-Geheimhaltungsfrist"
---

# Test — freedom-to-operate

Struktureller Smoke-Test. Recherchemethodik muss Datenbanken, Klassifikation und Stichwortstrategie nennen; § 32 V PatG-Begrenzung muss ausdrücklich erscheinen; Schutzbereichsanalyse je Treffer muss Merkmalsgliederung + Wortlaut + Äquivalenz nach BGH-Trias enthalten; Lebensphasen müssen unterschieden werden; Handlungsoptionen (Designaround / Lizenz / Nichtigkeit § 81 PatG / Einspruch § 59 PatG / Verzicht / Risikoakzeptanz) müssen aufgelistet sein; Pflicht-Disclaimer zum Recherchestand muss vorhanden sein.

Run: `python ../../../scripts/eval.py --skill patentrecht/skills/freedom-to-operate`
