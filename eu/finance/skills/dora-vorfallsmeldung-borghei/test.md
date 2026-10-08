---
skill: dora/dora-vorfallsmeldung
fact_pattern: |
  BaFin-reguliertes Zahlungsinstitut entdeckt am 12.05.2026 um 09:00 einen
  Ransomware-Angriff, der das Kernzahlungssystem (kritische Funktion) lahmlegt.
  Rund 40.000 Kunden können keine Überweisungen ausführen; erste Hinweise auf
  Datenexfiltration. Klassifizierung als schwerwiegend erfolgt um 11:00. Welche
  Meldepflichten und Fristen greifen nach DORA?
must_cite:
  - "Art. 17 DORA"
  - "Art. 18 DORA"
  - "Art. 19 DORA"
  - "Art. 23 DORA"
  - "RTS 2024/1772"
must_appear:
  - "Klassifizierung"
  - "Erstmeldung"
  - "Zwischenmeldung"
  - "Abschlussbericht"
  - "Kundeninformation"
  - "schwerwiegend"
must_flag:
  - "4-Stunden-Frist"
  - "Klassifizierungsschwelle"
  - "Doppelmeldung"
  - "Kundeninformation"
---

# Test — dora-vorfallsmeldung

Run: `python3 scripts/eval.py --skill dora/skills/dora-vorfallsmeldung`
