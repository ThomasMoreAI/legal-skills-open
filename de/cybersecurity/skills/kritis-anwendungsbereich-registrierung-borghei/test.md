---
skill: kritis-resilienz/kritis-anwendungsbereich-registrierung
fact_pattern: |
  Mandantin ist ein kommunaler Versorger, der ein Wasserwerk, ein
  Gasverteilnetz und eine Siedlungsabfallverwertungsanlage betreibt.
  Die Schwellenwerte wurden für Wasserwerk und Gasnetz am 17.04.2026
  erstmals überschritten; für die Abfallanlage bereits 2025. Die
  Konzerntochter, die das Rechenzentrum betreibt, ist im Sektor
  Informationstechnik und Telekommunikation tätig. Eine
  Konzernbeteiligung an einer Sparkasse besteht ebenfalls; diese
  unterliegt DORA. Die Geschäftsführung meint, mit der bereits erfolgten
  NIS2-Registrierung beim BSI seien alle Pflichten erfüllt, und beruft
  sich für die Abfallanlage sowie das Rechenzentrum auf die
  Bereichsausnahme.

must_cite:
  - "§ 3 KRITISDachG"
  - "§ 4 KRITISDachG"
  - "§ 5 KRITISDachG"
  - "§ 8 KRITISDachG"
  - "§ 24 KRITISDachG"
  - "§ 1a KWG"

must_appear:
  - "physische"
  - "Bundesamt für Bevölkerungsschutz"
  - "drei Monate"
  - "Geltungszeitpunkt"
  - "Bereichsausnahme"
  - "Siedlungsabfallentsorgung"
  - "Bundesnetzagentur"
  - "getrennte"
  - "legal_calc"

must_flag:
  - "KRITIS-DachG und BSIG/NIS2 verwechselt"
  - "Bereichsausnahme des § 4 Abs. 2 auf das ganze Gesetz erstreckt"
  - "Dreimonatsfrist ab Behördenschreiben gerechnet"
  - "Schwellenwerte aus dem Gedächtnis zitiert"
  - "Sektorbehörde pauschal als BBK benannt"
---

# Test — kritis-anwendungsbereich-registrierung

Struktureller Smoke-Test. Die Ausgabe muss die NIS2-Registrierung beim BSI von der KRITIS-Registrierung beim BBK trennen, die Dreimonatsfrist des § 8 Abs. 1 KRITISDachG ab dem 17.04.2026 rechnen, die Bereichsausnahmen des § 4 Abs. 2 einzeln zuordnen — IT/TK vollständig, Siedlungsabfallentsorgung mit Ausnahme des § 12, DORA-Finanzunternehmen nach Nr. 1 — und in allen Fällen klarstellen, dass die Registrierungspflicht des § 8 **nicht** ausgenommen ist. Die sektorspezifische Zuständigkeit (Bundesnetzagentur für Gas) ist zu benennen und die Schwellenwerte auf die Rechtsverordnung nach § 5 Abs. 1 zu stützen.

Run: `python ../../../scripts/eval.py --skill kritis-resilienz/skills/kritis-anwendungsbereich-registrierung`
