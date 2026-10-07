---
skill: sportrecht/athletenvertrag
fact_pattern: |
  Tennisspielerin (WTA-Ranking 80–120) erhält Entwurf eines dreijährigen
  Vermarktungs- und Förderungsvertrags mit einem Ausrüster. Zentrale
  Klauseln: weltweite Exklusivität, "umfassende und zeitlich unbegrenzte"
  Übertragung der Bildrechte, Bonusrückzahlung bei jeder Doping-Sperre
  unabhängig vom Verschulden, einseitige außerordentliche Kündigung
  zugunsten des Ausrüsters bei "Imageverlust", Schiedsklausel zugunsten
  einer vom Ausrüster benannten ad hoc-Stelle. Spielerin verfügt über
  einen eigenen Manager, aber keine anwaltliche Verhandlungsmacht. Bitte
  AGB-Kontrolle und Klauselbausteine.

must_cite:
  - "§ 305"
  - "§ 307"
  - "§ 308"
  - "§ 309"
  - "§ 22 KUG"
  - "§ 23 KUG"
  - "Art. 9 DSGVO"
  - "Art. 101 AEUV"

must_appear:
  - "AGB"
  - "Transparenzgebot"
  - "Bildrechte"
  - "Exklusivität"
  - "Bosman"
  - "Verschuldensanknüpfung"
  - "Pechstein"
  - "Schiedsklausel"

must_flag:
  - "umfassende"
  - "verschuldensunabhängig"
  - "einseitige"
---

# Test — athletenvertrag

Struktureller Smoke-Test. Mindestens drei rote Klauseln (Bildrechte "umfassend", Bonusrückzahlung verschuldensunabhängig, einseitige Kündigungsrechte) müssen als § 307/§ 308/§ 309 BGB-problematisch markiert werden; KUG-Bezug muss konkretisiert sein; Schiedsklausel an Pechstein-Linie gemessen; Diarra-/Bosman-Linie für Exklusivitätsklausel kurz erwähnt.

Run: `python ../../../scripts/eval.py --skill sportrecht/skills/athletenvertrag`
