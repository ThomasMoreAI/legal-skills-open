---
skill: krypto-mikar/krypto-whitepaper-angebot
fact_pattern: |
  Ein Emittent plant ab März 2026 ein öffentliches Angebot eines Utility
  Tokens an Privatanleger in Deutschland. Der Whitepaper-Entwurf enthält
  Projektbeschreibung, Team und Risiken, aber keine Angaben zu den
  nachteiligen Auswirkungen des Konsensmechanismus auf Klima und Umwelt
  und keine Erklärung des Leitungsorgans. Die Marketingkampagne wirbt mit
  "BaFin-geprüftes Whitepaper" und mit einer Kurszielprognose. Ein
  Widerrufsrecht ist nicht vorgesehen, weil eine Listung an einer
  Handelsplattform erst für Ende 2026 geplant ist. Parallel soll ein an
  den Euro gekoppelter Stablecoin durch dieselbe GmbH ausgegeben werden.

must_cite:
  - "Art. 4"
  - "Art. 6"
  - "Art. 7"
  - "Art. 8"
  - "Art. 13"
  - "Art. 15"
  - "Art. 48"
  - "§ 15 KMAG"
  - "§ 17 KMAG"
  - "§ 19 KMAG"

must_appear:
  - "Übermittlung"
  - "keine"
  - "Klima"
  - "Leitungsorgan"
  - "Widerrufsrecht"
  - "Marketingmitteilungen"
  - "E-Geld-Token"
  - "Kreditinstitut"
  - "legal_calc"

must_flag:
  - "Whitepaper für gebilligt gehalten"
  - "E-Geld-Token ohne Kreditinstituts"
  - "Klima- und Umweltangaben weggelassen"
  - "Widerrufsrecht des Art. 13 übersehen"
  - "Haftung nur nach Art. 15 geprüft"
  - "Marketingmitteilungen nicht mit dem Whitepaper abgeglichen"
---

# Test — krypto-whitepaper-angebot

Struktureller Smoke-Test. Die Ausgabe muss die Werbeaussage "BaFin-geprüftes Whitepaper" als unzutreffend zurückweisen, weil nach Art. 8 MiCAR nur eine Übermittlung und keine Billigung erfolgt, und sie zugleich an Art. 7 sowie § 17 KMAG messen. Die fehlenden Klima- und Umweltangaben sowie die fehlende Erklärung des Leitungsorgans sind als Verstöße gegen Art. 6 zu benennen. Das Widerrufsrecht nach Art. 13 ist zu bejahen, solange keine Handelszulassung besteht. Der Euro-Stablecoin ist als E-Geld-Token einzuordnen und am Emittentenvorbehalt des Art. 48 zu messen. Die Haftung ist getrennt nach Art. 15 MiCAR und § 19 KMAG zu führen.

Run: `python ../../../scripts/eval.py --skill krypto-mikar/skills/krypto-whitepaper-angebot`
