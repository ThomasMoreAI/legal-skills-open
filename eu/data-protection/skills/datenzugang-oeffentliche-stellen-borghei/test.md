---
skill: datenwirtschaftsrecht/datenzugang-oeffentliche-stellen
fact_pattern: |
  Eine Landesbehörde fordert von einer Betreiberin von
  Mikromobilitätsflotten (140 Beschäftigte) mit Schreiben vom 09.03.2026
  sämtliche Fahrt-, Standort- und Nutzerdaten der letzten 24 Monate an.
  Als Zweck nennt sie "Verkehrsplanung"; eine Rechtsvorschrift, die ihr
  diese Aufgabe zuweist, ist nicht angegeben, ebenso wenig die Frist für
  eine Ablehnung. Ausgeführt wird lediglich, die Daten seien "am Markt zu
  teuer". Ein öffentlicher Notstand liegt nicht vor. Die Behörde kündigt
  an, die Daten an ein privates Beratungsunternehmen weiterzugeben, das
  auch eigene Mobilitätsdienste entwickelt. Die Mandantin will die
  Herausgabe abwehren, hilfsweise nur anonymisiert und gegen Ausgleich
  liefern.

must_cite:
  - "Art. 14"
  - "Art. 15"
  - "Art. 17"
  - "Art. 18"
  - "Art. 19"
  - "Art. 20"
  - "Art. 21"
  - "§ 2 DADG"
  - "§ 2 DGG"

must_appear:
  - "außergewöhnliche Notwendigkeit"
  - "öffentlicher Notstand"
  - "30 Arbeitstage"
  - "5 Arbeitstage"
  - "Anonymisierung"
  - "faire Gegenleistung"
  - "angemessenen Marge"
  - "Bundesnetzagentur"
  - "Datenvermittlungsdienste"
  - "legal_calc"

must_flag:
  - "Notstands- und Regelfall gleich behandelt"
  - "Formprüfung nach Art. 17 übersprungen"
  - "Ablehnungsfrist versäumt"
  - "Personenbezogene Daten ohne Anonymisierung"
  - "Ausgleich nicht geltend gemacht"
  - "DGA und Data Act vermengt"
---

# Test — datenzugang-oeffentliche-stellen

Struktureller Smoke-Test. Die Ausgabe muss den Fall der Fallgruppe des Art. 15 Abs. 1 Buchst. b zuordnen, das Verlangen wegen fehlender Angaben nach Art. 17 Abs. 1 Buchst. b, h und i als ablehnungsfähig nach Art. 18 Abs. 2 Buchst. c behandeln, die 30-Arbeitstage-Frist mit Feiertagsberücksichtigung berechnen, personenbezogene Daten über Art. 18 Abs. 4 der Anonymisierung unterstellen, den Ausgleich nach Art. 20 Abs. 2 einschließlich Marge geltend machen und die geplante Weitergabe an den Wettbewerber an Art. 19 Abs. 2 messen.

Run: `python ../../../scripts/eval.py --skill datenwirtschaftsrecht/skills/datenzugang-oeffentliche-stellen`
