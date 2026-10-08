---
skill: berufsrecht-anwaltschaft/brao-pflichtenpruefung
fact_pattern: |
  Mittelständische Sozietät (PartG mbB, 14 Berufsträger) bekommt
  Mandatsanfrage einer GmbH gegen ihren ehemaligen Geschäftsführer
  wegen Schadensersatzansprüchen (§ 43 GmbHG, § 93 AktG analog). Vor
  zwei Jahren hat ein Partner der Sozietät — inzwischen ausgeschieden —
  den damaligen GF in der Erstellung einer steuerlichen Gestaltung
  beraten, die jetzt Gegenstand des Vorwurfs ist. Die Sozietät plant
  außerdem, Aktenscans an einen US-Cloud-Anbieter auszulagern und ein
  generatives KI-Tool für die Schriftsatzvorbereitung einzusetzen.
  Bitte vollständige BRAO-Pflichtenprüfung mit Empfehlung
  Mandatsannahme/-ablehnung.

must_cite:
  - "§ 43a BRAO"
  - "§ 43a Abs. 2 BRAO"
  - "§ 43a Abs. 4 BRAO"
  - "§ 43e BRAO"
  - "§ 3 BORA"
  - "§ 203 StGB"
  - "§ 356 StGB"
  - "§ 74 BRAO"
  - "§ 115 BRAO"

must_appear:
  - "Verschwiegenheit"
  - "Interessenkollision"
  - "Sozietätszurechnung"
  - "dieselbe Rechtssache"
  - "Auslagerung"
  - "Mandatsablehnung"
  - "Parteiverrat"
  - "anwaltsgerichtliche"
  - "Verfolgungsverjährung"

must_flag:
  - "KI-Auslagerung ohne § 43e"
  - "Vorbefassung der Sozietät"
  - "1-Monatsfrist § 74 BRAO"
---

# Test — brao-pflichtenpruefung

Struktureller Smoke-Test. Verschwiegenheit (§ 43a II BRAO + § 203 StGB) muss als Pflichtpunkt 1, Interessenkollision (§ 43a IV BRAO + § 3 BORA) als Pflichtpunkt 2 erscheinen. Sozietätszurechnung muss expressis verbis adressiert werden. KI-/Cloud-Auslagerung muss § 43e BRAO + § 203 Abs. 4 StGB-Verpflichtung der Hilfsperson erwähnen. Empfehlung muss Mandatsablehnung oder dokumentierte Heilung enthalten.

Run: `python ../../../scripts/eval.py --skill berufsrecht-anwaltschaft/skills/brao-pflichtenpruefung`
