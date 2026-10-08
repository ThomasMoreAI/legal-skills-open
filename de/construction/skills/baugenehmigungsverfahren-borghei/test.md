---
skill: baurecht/baugenehmigungsverfahren
fact_pattern: |
  Mandantin (Eigentümerin eines Bestandsgebäudes in Nordrhein-Westfalen)
  möchte ihr Grundstück in faktischem Mischgebiet (§ 34 II BauGB iVm § 6
  BauNVO) um eine Gewerbeeinheit erweitern. Ein qualifizierter B-Plan
  existiert nicht. Die Gemeinde hat ihr Einvernehmen nach § 36 BauGB
  unter Verweis auf "Wahrung des Wohncharakters" verweigert. Die untere
  Bauaufsichtsbehörde hat über den Bauantrag seit vier Monaten nicht
  entschieden. Bitte materielle Zulässigkeit (Einfügen, Art und Maß,
  Stellplätze nach BauO NRW), Rechtmäßigkeit der Einvernehmensverweigerung,
  Verfahrensart und Rechtsbehelfsstrategie (Verpflichtungsklage, ggf.
  § 75 VwGO Untätigkeit) prüfen.

must_cite:
  - "§ 29 BauGB"
  - "§ 34 BauGB"
  - "§ 36 BauGB"
  - "§ 42 VwGO"
  - "§ 74 VwGO"
  - "§ 75 VwGO"

must_appear:
  - "Vorhaben"
  - "Einfügen"
  - "faktisches"
  - "Mischgebiet"
  - "Einvernehmen"
  - "Rücksichtnahmegebot"
  - "Abstandsflächen"
  - "Verpflichtungsklage"

must_flag:
  - "Einvernehmen"
  - "§ 212a"
  - "1 Monat"
---

# Test — baugenehmigungsverfahren

Struktureller Smoke-Test. Vorhabenbegriff § 29 BauGB, planungsrechtliche Zulässigkeit nach § 34 II BauGB iVm BauNVO, Einvernehmen § 36 BauGB, LBO-Vorgaben (Abstandsflächen, Stellplätze) und Rechtsbehelfsstrategie (Verpflichtungsklage + § 75 VwGO) müssen vollständig adressiert sein; Sofortvollzug § 212a BauGB muss benannt werden, falls eine BauG bereits ergangen ist.

Run: `python ../../../scripts/eval.py --skill baurecht/skills/baugenehmigungsverfahren`
