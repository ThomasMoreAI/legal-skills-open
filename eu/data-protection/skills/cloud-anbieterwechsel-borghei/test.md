---
skill: datenwirtschaftsrecht/cloud-anbieterwechsel
fact_pattern: |
  Ein mittelständischer Versicherungsmakler betreibt sein
  Bestandsverwaltungssystem seit 2023 bei einem IaaS-Anbieter. Der
  Vertrag sieht eine Kündigungsfrist von sechs Monaten vor, gewährt nach
  Vertragsende einen Datenabruf von zehn Tagen, enthält keine
  Löschklausel und stellt für den Datenexport volumenabhängige
  Egress-Entgelte in Rechnung, die für den Gesamtbestand rund 38.000 EUR
  ergäben. Der Anbieter bezeichnet den Dienst als "individuell für den
  Kunden konfiguriert" und beruft sich auf eine Ausnahme; eine
  vorvertragliche Unterrichtung darüber gibt es nicht. Der Makler will
  zum 01.03.2026 zu einem anderen Anbieter wechseln. Als
  Versicherungsvermittler unterliegt er zudem aufsichtsrechtlichen
  Auslagerungsanforderungen.

must_cite:
  - "Art. 23"
  - "Art. 24"
  - "Art. 25"
  - "Art. 29"
  - "Art. 30"
  - "Art. 31"
  - "Art. 38"
  - "§ 2 DADG"
  - "§ 15 DADG"

must_appear:
  - "zwei Monate"
  - "30 Kalendertage"
  - "Abrufzeitraum"
  - "Löschung"
  - "exportierbare Daten"
  - "Funktionsäquivalenz"
  - "Wechselentgelt"
  - "12.01.2027"
  - "Bundesnetzagentur"
  - "legal_calc"

must_flag:
  - "Egress-Gebühren als Standarddienstentgelt"
  - "Kündigungsfrist über zwei Monate"
  - "Übergangs- und Abruffrist verwechselt"
  - "Werktage statt Kalendertage"
  - "Ausnahme nach Art. 31 behauptet"
  - "Löschgarantie nach Buchst. h übersehen"
---

# Test — cloud-anbieterwechsel

Struktureller Smoke-Test. Die Ausgabe muss die Sechsmonatsfrist an Art. 25 Abs. 2 Buchst. d scheitern lassen, den Zehn-Tage-Abruf an Buchst. g, die fehlende Löschklausel an Buchst. h und die Ausnahmebehauptung an der fehlenden Unterrichtung nach Art. 31 Abs. 3. Die Egress-Entgelte müssen als Wechselentgelte im Sinne des Art. 29 eingeordnet und der Stichtag 12.01.2027 genannt werden. Der Exit-Fahrplan muss die vollständige Fristenkette mit Kalendertagen ausweisen.

Run: `python ../../../scripts/eval.py --skill datenwirtschaftsrecht/skills/cloud-anbieterwechsel`
