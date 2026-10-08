---
skill: krypto-mikar/krypto-marktmissbrauch
fact_pattern: |
  Der Emittent eines zum Handel zugelassenen Utility Tokens verhandelt seit
  April 2026 über eine Übernahme durch einen Konzern; am 04.05.2026 wird
  ein Term Sheet unterzeichnet. Zwei Tage später storniert der
  Finanzvorstand eine bereits erteilte Verkaufsorder über eigene Token und
  kauft stattdessen zu. Ein Mitarbeiter der Rechtsabteilung erwähnt die
  Verhandlungen gegenüber einem befreundeten Journalisten. Auf der
  Handelsplattform fallen zeitgleich zahlreiche kleine Kauf- und
  Verkaufsorders zwischen zwei verbundenen Konten auf, die den Kurs
  stützen; die Plattform hat keine Handelsüberwachung. Die
  Geschäftsführung will die Übernahmeverhandlungen bis zur Unterschrift
  geheim halten, hat dazu aber nichts dokumentiert.

must_cite:
  - "Art. 86"
  - "Art. 87"
  - "Art. 88"
  - "Art. 89"
  - "Art. 90"
  - "Art. 91"
  - "Art. 92"
  - "§ 31 KMAG"
  - "§ 32 KMAG"
  - "§ 47 KMAG"

must_appear:
  - "Insiderinformation"
  - "präzise"
  - "Zwischenschritt"
  - "Aufschub"
  - "Stornierung"
  - "Wash Trading"
  - "Verdachtsmeldung"
  - "Verschwiegenheit"
  - "legal_calc"

must_flag:
  - "MAR-Praxis unbesehen übertragen"
  - "Aufschub ohne Dokumentation"
  - "Stornierung oder Änderung eines Auftrags nicht als Insidergeschäft erkannt"
  - "Marktmanipulation nach Marktjargon statt nach Fallgruppen subsumiert"
  - "Kein System nach Art. 92 aufgebaut"
  - "Verschwiegenheitspflicht des § 32 KMAG verletzt"
---

# Test — krypto-marktmissbrauch

Struktureller Smoke-Test. Die Ausgabe muss das unterzeichnete Term Sheet als möglichen präzisen Zwischenschritt einer Insiderinformation nach Art. 87 MiCAR prüfen, die fehlende Dokumentation des Aufschubs nach Art. 88 beanstanden, die Stornierung der Verkaufsorder und den anschließenden Zukauf unter Art. 89 fassen, die Weitergabe an den Journalisten unter Art. 90, die Orders zwischen verbundenen Konten anhand der Fallgruppen des Art. 91 einordnen (nicht bloß als "Wash Trading" bezeichnen) und die fehlende Handelsüberwachung der Plattform an Art. 92 messen. Die Verschwiegenheitspflicht des § 32 KMAG bei aufsichtlichen Maßnahmen ist zu benennen, ebenso die Sanktionen der §§ 46, 47 KMAG am Wortlaut statt nach WpHG.

Run: `python ../../../scripts/eval.py --skill krypto-mikar/skills/krypto-marktmissbrauch`
