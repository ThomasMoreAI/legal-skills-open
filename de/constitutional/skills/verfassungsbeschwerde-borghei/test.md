---
skill: verfassungsrecht/verfassungsbeschwerde
fact_pattern: |
  Mandant wurde durch BGH-Revisionsurteil rechtskräftig zur Unterlassung
  einer Äußerung verurteilt. Letzte Entscheidung wurde dem Mandanten am
  10.03.JJJJ zugestellt. Anhörungsrüge wurde fristgerecht erhoben und
  zurückgewiesen. Mandant sieht Art. 5 Abs. 1 GG verletzt. Bitte
  Verfassungsbeschwerde vorbereiten: Zulässigkeit vollständig prüfen
  (insbesondere Frist § 93 BVerfGG, Subsidiarität, Substantiierung) und
  Begründetheit am 3-Stufen-Schema.

must_cite:
  - "Art. 93 Abs. 1 Nr. 4a GG"
  - "§ 90 BVerfGG"
  - "§ 92 BVerfGG"
  - "§ 93 BVerfGG"
  - "§ 93a BVerfGG"
  - "§ 31 BVerfGG"
  - "Art. 5 Abs. 1 GG"

must_appear:
  - "Beschwerdefähigkeit"
  - "Beschwerdegegenstand"
  - "Beschwerdebefugnis"
  - "Rechtswegerschöpfung"
  - "Subsidiarität"
  - "Monatsfrist"
  - "Annahmeverfahren"
  - "Schutzbereich"
  - "Eingriff"
  - "Rechtfertigung"
  - "Verhältnismäßigkeit"

must_flag:
  - "Zustelldatum"
  - "Anhörungsrüge"
  - "Heck'sche Formel"
  - "unverifiziert"
---

# Test — verfassungsbeschwerde

Struktureller Smoke-Test. Alle sieben Zulässigkeitsstufen müssen im Output auftauchen, das 3-Stufen-Schema der Grundrechtsprüfung muss erkennbar sein, § 31 BVerfGG nur als ausdrückliche Ausnahme zur Präjudizienbindung referenziert werden.

Run: `python ../../../scripts/eval.py --skill verfassungsrecht/skills/verfassungsbeschwerde`
