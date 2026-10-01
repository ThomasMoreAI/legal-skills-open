---
skill: sportrecht/dopingverfahren-verteidigung
fact_pattern: |
  Profi-Triathletin, Mitglied im RTP, A-Probe positiv auf Substanz der
  WADA-Liste S1 (anabole Wirkstoffe). NADA hat zur Anhörung geladen.
  Athletin trägt vor, die Substanz sei aus einem kontaminierten
  Nahrungsergänzungsmittel (Charge) gestammt; Charge-Nummer und ein
  Restbestand des Produkts sind vorhanden. Anhörungstermin in 14 Tagen.
  B-Probe-Frist läuft seit 4 Tagen. Parallel: StA hat Vorermittlungen
  nach § 4 IV AntiDopG aufgenommen. Mandantin will Sperre vermeiden
  oder mindern und Strafverfahren nicht durch Sportverfahren belasten.

must_cite:
  - "WADC Art. 2.1"
  - "Art. 10.6 WADC"
  - "WADC Art. 13"
  - "§ 4 AntiDopG"
  - "Art. 12 GG"
  - "§ 1059 ZPO"

must_appear:
  - "B-Probe"
  - "No Significant Fault"
  - "Kontamination"
  - "Whereabouts"
  - "21 Tage"
  - "Pechstein"
  - "CAS"
  - "Anhörung"
  - "Spitzensportler"

must_flag:
  - "Versäumte B-Probe-Frist"
  - "Abstrakte Kontaminationsbehauptung"
  - "Aussageabstimmung"
  - "21 Tage"
---

# Test — dopingverfahren-verteidigung

Struktureller Smoke-Test. Verteidigung muss verschuldensunabhängigen Verstoß Art. 2.1 WADC korrekt von Sanktionsmilderung Art. 10.5/10.6 trennen, das Parallelverfahren § 4 IV AntiDopG adressieren und alle einschlägigen Fristen (B-Probe, CAS 21 Tage, ZPO § 1059) in einem Fristkalender ausweisen.

Run: `python ../../../scripts/eval.py --skill sportrecht/skills/dopingverfahren-verteidigung`
