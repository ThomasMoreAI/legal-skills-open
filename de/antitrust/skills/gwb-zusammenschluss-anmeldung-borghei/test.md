---
skill: kartellrecht/gwb-zusammenschluss-anmeldung
fact_pattern: |
  Mandantin (deutsche Maschinenbau-Holding, weltweiter Konzernumsatz
  800 Mio. EUR, Inlandsumsatz 90 Mio. EUR) plant den Erwerb von 100 %
  der Anteile an einer deutschen Zielgesellschaft (Inlandsumsatz
  20 Mio. EUR, keine EU-Auslandstätigkeit). Kaufpreis 60 Mio. EUR.
  Signing in 4 Wochen, Closing geplant in 8 Wochen. Bitte Anmelde-
  pflicht §§ 35, 37 GWB prüfen, Verhältnis zur EU-FK-VO klären, Frist-
  Kalender (Vorprüfung/Hauptprüfung § 40 GWB) sowie Vollzugsverbot
  § 41 GWB und Gun-Jumping-Risiko adressieren.

must_cite:
  - "§ 35 GWB"
  - "§ 37 GWB"
  - "§ 39 GWB"
  - "§ 40 GWB"
  - "§ 41 GWB"
  - "§ 81"
  - "VO (EG) Nr. 139/2004"

must_appear:
  - "Zusammenschluss"
  - "Aufgreifschwellen"
  - "Transaktionswert"
  - "One-Stop-Shop"
  - "Vorprüfung"
  - "Hauptprüfung"
  - "Vollzugsverbot"
  - "Gun-Jumping"
  - "SIEC"
  - "OLG Düsseldorf"

must_flag:
  - "Closing vor Freigabe"
  - "Bußgeld"
  - "10 %"
  - "verbundene Unternehmen"
---

# Test — gwb-zusammenschluss-anmeldung

Struktureller Smoke-Test. Output muss Schwellen-Berechnung (§ 35 I und § 35 Ia GWB) durchführen, das Verhältnis zur EU-FK-VO klären, einen Frist-Kalender (Vorprüfung 1 Monat / Hauptprüfung 4 Monate) ausweisen und Gun-Jumping als 🔴 BLOCKER markieren.

Run: `python ../../../scripts/eval.py --skill kartellrecht/skills/gwb-zusammenschluss-anmeldung`
