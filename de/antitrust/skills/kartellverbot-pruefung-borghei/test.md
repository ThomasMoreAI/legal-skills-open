---
skill: kartellrecht/kartellverbot-pruefung
fact_pattern: |
  Mandant (Hersteller von Markenprodukten, Marktanteil 20 % im sach-
  lich relevanten Markt) plant ein Selektivvertriebssystem mit folgen-
  den Klauseln: (1) Händler dürfen die UVP nicht unterschreiten,
  (2) Verkauf an nicht autorisierte Händler ist untersagt, (3) Ver-
  kauf über Drittplattformen (Amazon, eBay) ist autorisierten Händ-
  lern untersagt, (4) nachvertragliches Wettbewerbsverbot 24 Monate.
  Bitte § 1 GWB / Art. 101 I AEUV prüfen, Vertikal-GVO 2022/720-
  Sicherheitshafen analysieren (insb. Art. 4 Kernbeschränkungen,
  Art. 5 nicht freigestellte Beschränkungen), Einzelausnahme § 2 GWB
  / Art. 101 III AEUV erörtern und Rechtsfolgen (Nichtigkeit, Bußgeld,
  Schadensersatz) darstellen.

must_cite:
  - "§ 1 GWB"
  - "§ 2 GWB"
  - "§ 134 BGB"
  - "Art. 101"
  - "VO (EU) 2022/720"

must_appear:
  - "Vereinbarung"
  - "Wettbewerbsbeschränkung"
  - "Zweck"
  - "Hardcore"
  - "Spürbarkeit"
  - "De-minimis"
  - "Sicherheitshafen"
  - "Kernbeschränkung"
  - "Einzelausnahme"
  - "Effizienz"
  - "Unerlässlichkeit"
  - "Nichtigkeit"

must_flag:
  - "Preisbindung"
  - "Drittplattform"
  - "nachvertragliche Wettbewerbsverbote"
  - "Bußgeld"
---

# Test — kartellverbot-pruefung

Struktureller Smoke-Test. Output muss die vierstufige Subsumtion (Tatbestand → Spürbarkeit → GVO-Sicherheitshafen → Einzelausnahme) sichtbar machen, Klausel (1) als Hardcore-Preisbindung Art. 4 lit. a Vertikal-GVO identifizieren, Klausel (3) im Lichte Coty bewerten, Klausel (4) als Art. 5-Beschränkung (Wettbewerbsverbot > 1 Jahr nachvertraglich) markieren und die vier kumulativen Voraussetzungen des Art. 101 III AEUV explizit durchgehen.

Run: `python ../../../scripts/eval.py --skill kartellrecht/skills/kartellverbot-pruefung`
