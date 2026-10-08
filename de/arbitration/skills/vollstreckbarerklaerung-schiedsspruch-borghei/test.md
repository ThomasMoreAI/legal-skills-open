---
skill: schiedsverfahren-adr/vollstreckbarerklaerung-schiedsspruch
fact_pattern: |
  Unsere Mandantin hat gegen eine türkische Gesellschaft einen
  ICC-Schiedsspruch mit Schiedsort Zürich über 850.000 EUR erstritten.
  Die Schuldnerin hat keinen Sitz in Deutschland, unterhält aber ein
  Guthaben bei einer Bank in Berlin und ein Warenlager in Hamburg. Sie
  hat in der Schweiz eine Aufhebungsklage erhoben, über die noch nicht
  entschieden ist, und macht geltend, sie sei über die Bestellung des
  Vorsitzenden nicht ordnungsgemäß unterrichtet worden. Der Schiedsspruch
  liegt in englischer Sprache als vom Sekretariat beglaubigte Abschrift
  vor. Die Mandantin will schnellstmöglich das Bankguthaben sichern.

must_cite:
  - "§ 1060 ZPO"
  - "§ 1061 ZPO"
  - "§ 1062 ZPO"
  - "§ 1063 ZPO"
  - "§ 1064 ZPO"
  - "§ 1065 ZPO"
  - "§ 794 ZPO"
  - "§ 829 ZPO"

must_appear:
  - "New Yorker Übereinkommen"
  - "Art. V"
  - "Art. VII"
  - "Meistbegünstigung"
  - "ordre public"
  - "Vermögen"
  - "Kammergericht"
  - "Sicherung"
  - "vorläufig vollstreckbar"
  - "legal_calc"

must_flag:
  - "Falsches Regime gewählt"
  - "Beweislast bei Art. V NYÜ verkannt"
  - "Meistbegünstigung nach Art. VII NYÜ übersehen"
  - "Ordre public international mit innerstaatlichem ordre public gleichgesetzt"
  - "Zuständigkeitsanker der Vermögensbelegenheit übersehen"
---

# Test — vollstreckbarerklaerung-schiedsspruch

Struktureller Smoke-Test. Die Ausgabe muss den Schiedsspruch wegen des Schiedsorts Zürich § 1061 ZPO iVm dem New Yorker Übereinkommen zuordnen, die Zuständigkeit über § 1062 Abs. 2 ZPO an der Vermögensbelegenheit in Berlin oder Hamburg festmachen (hilfsweise Kammergericht), die Rüge der fehlenden Unterrichtung Art. V Abs. 1 lit. b NYÜ mit Beweislast beim Antragsgegner zuordnen, die anhängige Schweizer Aufhebungsklage an Art. V Abs. 1 lit. e NYÜ messen, die Beglaubigungserleichterung des § 1064 Abs. 1 S. 2 ZPO über Art. VII NYÜ nutzbar machen und für die Sicherung des Bankguthabens § 1063 Abs. 3 ZPO sowie die anschließende Pfändung nach §§ 829, 835 ZPO benennen.

Run: `python ../../../scripts/eval.py --skill schiedsverfahren-adr/skills/vollstreckbarerklaerung-schiedsspruch`
