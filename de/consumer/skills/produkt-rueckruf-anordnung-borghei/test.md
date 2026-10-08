---
skill: produktrecht/produkt-rueckruf-anordnung
fact_pattern: |
  Mandantin (Spielzeug-Importeur in DE) wurde mit Anhörungsschreiben
  der Landesmarktaufsichtsbehörde konfrontiert: Stichprobenuntersuchung
  einer Charge Kinderpuppen hat eine Phthalat-Belastung über dem
  Grenzwert ergeben. Die Behörde stellt eine Rückrufanordnung
  einschließlich Sofortvollzug in Aussicht. Mandantin fragt nach
  (a) Stellungnahme im Anhörungsverfahren, (b) Maßnahmenstufung
  (Rückruf zwingend oder Warnung/Reparatur möglich?), (c) paralleler
  zivilrechtlicher Rückrufpflicht, (d) Vorfallsmeldung Safety Business
  Gateway, (e) Rechtsbehelf, falls Anordnung ergeht.

must_cite:
  - "§ 823"
  - "Art. 36"
  - "Art. 20"
  - "§ 28 VwVfG"
  - "§ 80"
  - "§ 74 VwGO"
  - "Pflegebetten"

must_appear:
  - "Produktbeobachtung"
  - "Warnung"
  - "Reparatur"
  - "Rückruf"
  - "Vernichtung"
  - "Verhältnismäßigkeit"
  - "Anhörung"
  - "Sofortvollzug"
  - "Safety Business Gateway"

must_flag:
  - "unverzüglich"
  - "1 Monat"
  - "Versicherer"
---

# Test — produkt-rueckruf-anordnung

Struktureller Smoke-Test. Beide Rückruf-Dimensionen (zivilrechtlich aus § 823 BGB / „Pflegebetten" und öffentlich-rechtlich aus Art. 36 GPSR) müssen geprüft werden; Maßnahmenstufung (Warnung → Empfehlung → Reparatur → Rückruf → Vernichtung) muss vollständig erscheinen; § 28 VwVfG-Anhörung, § 80 VwGO-Sofortvollzug und § 74 VwGO-Klagefrist (1 Monat) müssen angesprochen werden.

Run: `python ../../../scripts/eval.py --skill produktrecht/skills/produkt-rueckruf-anordnung`
