---
skill: reise-fluggastrecht/reisevermittlung-informationspflichten
fact_pattern: |
  Mandantin buchte auf einem Online-Portal in einem Vorgang Flug,
  Hotel und Mietwagen zu einem als Gesamtpreis dargestellten Betrag.
  Rechnung und Buchungsbestätigung stammen vom Portal; die AGB
  bezeichnen dieses als reinen Vermittler. Ein Formblatt nach
  Art. 250 EGBGB wurde nicht übermittelt. Der Hinflug wurde
  versehentlich auf den Vortag gebucht; die Umbuchung kostete
  380 EUR. Die Mandantin möchte die Buchung "widerrufen", weil sie
  online abgeschlossen wurde, und hat vom Portal einen Gutschein
  über 380 EUR angeboten bekommen.

must_cite:
  - "§ 651a BGB"
  - "§ 651v BGB"
  - "§ 651w BGB"
  - "§ 651x BGB"
  - "§ 651d BGB"
  - "§ 312g Abs. 2 Nr. 9 BGB"
  - "Art. 250 § 3 EGBGB"
  - "§ 280 BGB"

must_appear:
  - "Rollenabgrenzung"
  - "Reiseveranstalter"
  - "Reisevermittler"
  - "verbundene Reiseleistungen"
  - "Auftreten gegenüber dem Reisenden"
  - "Formblatt"
  - "Buchungsfehler"
  - "Fernabsatzvertrag"
  - "Gutschein"
  - "Erstattung in Geld"
  - "Anspruchsschreiben an den Vermittler"

must_flag:
  - "Widerruf empfohlen"
  - "Rolle nach der Selbstbezeichnung bestimmt"
  - "Verbundene Reiseleistungen als Pauschalreise behandelt"
  - "Formblatt nicht angefordert"
  - "Gutschein vorbehaltlos angenommen"
  - "Buchungsstrecke nicht archiviert"
---

# Test — reisevermittlung-informationspflichten

Struktureller Smoke-Test. Die Dreiteilung Veranstalter / Vermittler / verbundene Reiseleistungen muss als Tabelle mit den jeweiligen Haftungsfolgen erscheinen und die Zuordnung ausdrücklich am Auftreten gegenüber dem Reisenden festmachen, nicht an der Selbstbezeichnung. Die Informationspflichten des Art. 250 EGBGB einschließlich Formblatt und die Rechtsfolgen ihrer Verletzung müssen benannt sein, insbesondere die Haftung wie ein Veranstalter nach § 651w Abs. 4 BGB. Der Ausschluss des Widerrufsrechts nach § 312g Abs. 2 Nr. 9 BGB muss als eigener Prüfungsschritt und als Risiko auftauchen.

Run: `python ../../../scripts/eval.py --skill reise-fluggastrecht/skills/reisevermittlung-informationspflichten`
