---
skill: verbandsklage-vdug/verbandsklage-zulaessigkeit
fact_pattern: |
  Ein qualifizierter Verbraucherverband erhebt gegen eine Energieversorgerin
  mit Sitz in Köln Abhilfeklage wegen einer als unwirksam gerügten
  Preisanpassungsklausel. Betroffen sein sollen rund 40.000 Haushaltskunden
  sowie etwa 900 Kleinstgewerbetreibende mit je unter zehn Beschäftigten.
  Der Verband bezieht 9 Prozent seiner Mittel aus Zuwendungen von
  Unternehmen der Branche und wird von einem Prozessfinanzierer getragen,
  dem 18 Prozent des Erlöses zugesagt sind; die Finanzierungsvereinbarung
  wurde nicht vorgelegt. Die Klage ist beim Landgericht Köln eingereicht.
  Gegen dieselbe Versorgerin ist seit drei Monaten eine Musterfeststellungs-
  klage eines anderen Verbands zum selben Lebenssachverhalt anhängig.

must_cite:
  - "§ 1 VDuG"
  - "§ 2 VDuG"
  - "§ 3 VDuG"
  - "§ 4 VDuG"
  - "§ 6 VDuG"
  - "§ 8 VDuG"
  - "§ 4 UKlaG"
  - "§ 13 BGB"

must_appear:
  - "Oberlandesgericht"
  - "50 Verbrauchern"
  - "5 Prozent"
  - "10 Prozent"
  - "kleine Unternehmen"
  - "Drittfinanzierung"
  - "Sperrwirkung"
  - "Anhängigkeit"
  - "Offenlegung"
  - "legal_calc"

must_flag:
  - "Landgericht angerufen"
  - "Finanzierungsrüge nicht erhoben"
  - "Quorum als Beweisfrage behandelt"
  - "Kleine Unternehmen übersehen"
  - "Sperrwirkung mit Rechtshängigkeit verwechselt"
---

# Test — verbandsklage-zulaessigkeit

Struktureller Smoke-Test. Die Ausgabe muss die Einreichung beim Landgericht an der ausschließlichen OLG-Zuständigkeit des § 3 Abs. 1 VDuG scheitern lassen, die 9-Prozent-Unternehmenszuwendungen an § 2 Abs. 1 Nr. 1 lit. b VDuG messen und die Offenlegung nach § 2 Abs. 2 VDuG verlangen, die 18-prozentige Erfolgsbeteiligung als Unzulässigkeitsgrund nach § 4 Abs. 2 Nr. 3 VDuG behandeln und die fehlende Vorlage der Vereinbarung nach § 4 Abs. 3 VDuG rügen, die Kleinstgewerbetreibenden über § 1 Abs. 2 VDuG als Verbraucher einbeziehen und die Sperrwirkung des § 8 VDuG an der Anhängigkeit der früheren Verbandsklage prüfen.

Run: `python ../../../scripts/eval.py --skill verbandsklage-vdug/skills/verbandsklage-zulaessigkeit`
