---
skill: krypto-mikar/casp-zulassung-uebergang
fact_pattern: |
  Eine Frankfurter GmbH betreibt seit 2021 eine Handelsplattform für
  Kryptowerte und verwahrt Kundenbestände; sie hatte am 29.12.2024 eine
  Erlaubnis für das Kryptoverwahrgeschäft nach § 32 KWG. Ein
  MiCAR-Zulassungsantrag wurde nie gestellt, weil die Geschäftsführung
  davon ausging, das Bestandsgeschäft dürfe nach Art. 143 Abs. 3 MiCAR
  bis zum 01.07.2026 weiterlaufen. Es ist August 2026. Kundenbestände
  werden auf Sammel-Wallets ohne Trennung vom Eigenbestand gehalten. Die
  BaFin hat um Stellungnahme gebeten und eine Untersagung angekündigt.
  Ein zweites Konzernunternehmen ohne jede Erlaubnis vermittelt seit 2023
  Kryptogeschäfte und hat der BaFin nie etwas angezeigt.

must_cite:
  - "Art. 59"
  - "Art. 60"
  - "Art. 63"
  - "Art. 70"
  - "Art. 143"
  - "§ 5 KMAG"
  - "§ 9 KMAG"
  - "§ 45 KMAG"
  - "§ 50 KMAG"
  - "§ 32 KWG"

must_appear:
  - "31. Dezember 2025"
  - "1. Juli 2026"
  - "verkürzt"
  - "vereinfachte"
  - "Gesellschaftern"
  - "sofort vollziehbar"
  - "Aussonderung"
  - "Trennung"
  - "legal_calc"

must_flag:
  - "Mit dem 01.07.2026 aus Art. 143 Abs. 3 MiCAR gerechnet"
  - "Übergangsrecht auf Unternehmen ohne die in § 50 Abs. 1 genannten Erlaubnisse erstreckt"
  - "Anzeige nach § 50 Abs. 4 KMAG"
  - "Aufschiebende Wirkung des Rechtsbehelfs angenommen"
  - "Kundenbestände nicht getrennt"
---

# Test — casp-zulassung-uebergang

Struktureller Smoke-Test. Die Ausgabe muss die Annahme, das Bestandsgeschäft dürfe bis zum 01.07.2026 weiterlaufen, ausdrücklich korrigieren: Nach § 50 Abs. 2 Nr. 3 KMAG erlosch die fortbestehende Erlaubnis spätestens mit Ablauf des 31.12.2025, weil Deutschland von der Verkürzungsbefugnis des Art. 143 Abs. 3 MiCAR Gebrauch gemacht hat. Für die GmbH mit KWG-Erlaubnis ist das vereinfachte Verfahren nach § 50 Abs. 3 KMAG zu prüfen; für das Konzernunternehmen ohne Erlaubnis greift § 50 Abs. 1 nicht, und die versäumte Anzeige nach Abs. 4 ist zu benennen. Die Sammel-Wallets sind an Art. 70 und Art. 75 MiCAR sowie § 45 KMAG zu messen, und es ist klarzustellen, dass Maßnahmen nach § 5 KMAG sofort vollziehbar sind und § 9 KMAG auch Gesellschafter und Organe erfasst.

Run: `python ../../../scripts/eval.py --skill krypto-mikar/skills/casp-zulassung-uebergang`
