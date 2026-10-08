---
skill: energierecht/enwg-netzanschluss
fact_pattern: |
  Mandantin (Projektentwicklerin Freiflächen-PV, 12 MWp) hat beim
  örtlichen VNB Netzanschluss im Mittelspannungsnetz beantragt. Der VNB
  verweist auf fehlende Kapazität und nennt eine Wartezeit von 36
  Monaten, ohne Anschlusszusage und ohne verbindlichen Realisierungs-
  plan. Eine BImSchG-Genehmigung ist hier nicht erforderlich (PV).
  Mandantin will Anschlussanspruch durchsetzen, hilfsweise BNetzA-
  Beschlussverfahren einleiten.

must_cite:
  - "§ 17 EnWG"
  - "§ 18 EnWG"
  - "§ 8 EEG"
  - "§ 12 EEG"
  - "§ 31 EnWG"
  - "§ 75 EnWG"

must_appear:
  - "Netzverknüpfungspunkt"
  - "kürzester"
  - "Netzausbaupflicht"
  - "Kapazitätsmangel"
  - "Beschlussverfahren"
  - "OLG Düsseldorf"

must_flag:
  - "Falsches Anschlussregime"
  - "Beschwerdefrist"
  - "BImSchG"
---

# Test — enwg-netzanschluss

Struktureller Smoke-Test. Das EEG-Anschlussregime (§§ 8, 12 EEG) muss als lex specialis vor § 17 EnWG erkannt werden; die Netzausbaupflicht § 12 EEG muss dem Kapazitätsmangel-Einwand entgegengehalten werden; das BNetzA-Beschlussverfahren §§ 31 ff. EnWG samt Beschwerde § 75 EnWG (1 Monat) muss als Rechtsweg adressiert werden.

Run: `python ../../../scripts/eval.py --skill energierecht/skills/enwg-netzanschluss`
