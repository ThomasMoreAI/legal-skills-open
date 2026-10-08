---
skill: datenwirtschaftsrecht/data-act-nutzerdatenzugang
fact_pattern: |
  Ein Flottenbetreiber verlangt am 10.02.2026 von der Herstellerin
  vernetzter Nutzfahrzeuge Zugang zu sämtlichen Telemetrie- und
  Fehlerspeicherdaten seiner 40 Fahrzeuge und deren laufende Weitergabe
  an eine freie Werkstattkette. Die Herstellerin bietet bislang nur ein
  PDF-Reporting an, verweist auf Sicherheitsrisiken beim Zugriff auf
  Bremsdaten, hält die Fehlercode-Übersetzungstabelle für ein
  Geschäftsgeheimnis (bislang nicht gekennzeichnet) und möchte für die
  Bereitstellung ein Entgelt vom Flottenbetreiber verlangen. Die
  Werkstattkette gehört mehrheitlich zu einem nach der VO (EU) 2022/1925
  benannten Torwächter.

must_cite:
  - "Art. 3"
  - "Art. 4"
  - "Art. 5"
  - "Art. 6"
  - "Art. 11"
  - "Art. 38"
  - "§ 2 DADG"
  - "§ 15 DADG"
  - "§ 2 GeschGehG"
  - "Art. 6 DSGVO"

must_appear:
  - "ohne Weiteres verfügbar"
  - "maschinenlesbar"
  - "unentgeltlich"
  - "Metadaten"
  - "Torwächter"
  - "Kennzeichnung"
  - "Bundesnetzagentur"
  - "Mitteilung"
  - "Streitbeilegung"
  - "legal_calc"

must_flag:
  - "Zugang pauschal verweigert"
  - "Geschäftsgeheimnis ohne Kennzeichnung"
  - "Entgelt vom Nutzer verlangt"
  - "Torwächtersperre übersehen"
  - "Rechtsprechung erfunden"
---

# Test — data-act-nutzerdatenzugang

Struktureller Smoke-Test. Die Ausgabe muss das PDF-Reporting als nicht formatkonform verwerfen, die Sicherheitsausnahme des Art. 4 Abs. 2 an die Mitteilung an die Bundesnetzagentur koppeln, den Geschäftsgeheimnisschutz an der fehlenden Kennzeichnung nach Art. 4 Abs. 6 scheitern lassen, das Entgeltverlangen gegenüber dem Nutzer zurückweisen und die Weitergabe an die torwächternahe Werkstattkette an Art. 5 Abs. 3 messen. Der Datenkatalog muss feldweise geführt werden.

Run: `python ../../../scripts/eval.py --skill datenwirtschaftsrecht/skills/data-act-nutzerdatenzugang`
