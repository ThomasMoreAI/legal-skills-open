---
skill: geldwaesche-aml-kyc/gwg-risikoanalyse
fact_pattern: |
  Mandantin (BaFin-lizenzierte Vermögensverwaltung, 120 Mio. AuM,
  internationales Privatkundengeschäft inkl. Schweiz und VAE,
  vereinzelt Krypto-Verwahrung) hat seit zwei Jahren keine
  Risikoanalyse aktualisiert. Letzte BaFin-Sonderprüfung hat
  Dokumentationsmängel festgestellt. Geschäftsleitung möchte eine
  GwG-konforme Risikoanalyse nach § 5 GwG mit Risikofaktoren-
  matrix und Ableitung des Pflichtenniveaus.

must_cite:
  - "§ 4 GwG"
  - "§ 5 GwG"
  - "§ 6 GwG"
  - "§ 10 GwG"
  - "§ 15 GwG"
  - "§ 56 GwG"

must_appear:
  - "Risikoanalyse"
  - "Kunde"
  - "Produkt"
  - "Vertriebsweg"
  - "geografisch"
  - "Pflichtenniveau"
  - "Aktualisierung"
  - "PEP"
  - "AMLR"
  - "AMLA"
  - "10.07.2027"
  - "Gap-Mapping"
  - "vollharmonisierend"

must_flag:
  - "Schubladendokument"
  - "nicht pauschal"
  - "Aktualisierung"
  - "AMLR bereits heute als Prüfungsmaßstab verwendet"
  - "Vollharmonisierung unterschätzt"
---

# Test — gwg-risikoanalyse

Struktureller Smoke-Test. Die vier Risikokategorien (Kunde / Produkt / Vertriebsweg / Geografie) müssen sämtlich im Output erscheinen; Aktualisierungsturnus jährlich + anlassbezogen muss adressiert werden; Bußgeldrisiko § 56 GwG ist zu erwähnen.

**Aktualitäts-Assertions (Stand 2026-07).** Die frühere pauschale Formulierung „ab Anwendungsbeginn `[unverifiziert – 2027]`" ist durch datierte Angaben ersetzt: **AMLA seit 01.07.2025 in Frankfurt operativ**, **AMLD6 Art. 11–13, 15 Umsetzungsfrist 10.07.2026**, **AMLR unmittelbar anwendbar ab 10.07.2027**. Rechtsgrundlage der Risikoanalyse bleibt bis dahin **§ 5 GwG**.

Der Skill muss zudem das **Gap-Mapping GwG → AMLR** als konkrete Arbeitsaufgabe und den **vollharmonisierenden** Charakter der AMLR abbilden — Letzteres, weil das Mapping auch **entfallende** nationale Zusatzpflichten ausweisen muss, nicht nur Lücken. Die `must_flag`-Einträge sichern beide Fehlannahmen ab.

Run: `python ../../../scripts/eval.py --skill geldwaesche-aml-kyc/skills/gwg-risikoanalyse`
