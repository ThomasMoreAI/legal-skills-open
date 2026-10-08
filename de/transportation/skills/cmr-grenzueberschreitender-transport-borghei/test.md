---
skill: transportrecht/cmr-grenzueberschreitender-transport
fact_pattern: |
  Beförderung Lyon (FR) → Stuttgart (DE) per LKW durch französischen
  Frachtführer F. Bei Ablieferung am 09.04. Wassereintritt, 12 von 18
  Kartons beschädigt (320 kg Bruttogewicht, Schaden 22.000 EUR).
  Empfängerin (Mandantin) hat den Schaden zwei Tage nach Ablieferung
  schriftlich gerügt. Frachtbrief enthält weder Wertangabe noch Interesse-
  Klausel. Bitte Anwendbarkeit CMR, Haftung Art. 17 ff., Höchstbetrag
  Art. 23 III, Rechtzeitigkeit Schadensanzeige Art. 30, Verjährung
  Art. 32 und Gerichtsstandwahl Art. 31 prüfen.

must_cite:
  - "Art. 1 CMR"
  - "Art. 17 CMR"
  - "Art. 18 CMR"
  - "Art. 23 CMR"
  - "Art. 29 CMR"
  - "Art. 30 CMR"
  - "Art. 31 CMR"
  - "Art. 32 CMR"

must_appear:
  - "Anwendungsbereich"
  - "Vertragsstaat"
  - "Obhutshaftung"
  - "8,33"
  - "SZR"
  - "Bruttogewicht"
  - "Schadensanzeige"
  - "Gerichtsstand"
  - "Verjährung"

must_flag:
  - "Anwendungsvorrang"
  - "Tageskurs"
  - "gleichgestelltes Verschulden"
---

# Test — cmr-grenzueberschreitender-transport

Struktureller Smoke-Test. Anwendungsbereich Art. 1 CMR muss positiv durchgeprüft sein. Höchstbetrag muss methodisch (8,33 SZR × kg) berechnet, der SZR/EUR-Tageskurs datiert ausgewiesen werden. Tatfrist Art. 30 CMR und Verjährung Art. 32 CMR mit konkretem Anfangs- und Endtag. Gerichtsstandwahl Art. 31 CMR muss als Wahl des Klägers dargestellt sein, nicht als Rangordnung.

Run: `python ../../../scripts/eval.py --skill transportrecht/skills/cmr-grenzueberschreitender-transport`
