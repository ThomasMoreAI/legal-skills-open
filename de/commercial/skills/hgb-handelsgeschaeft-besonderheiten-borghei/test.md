---
skill: handelsrecht/hgb-handelsgeschaeft-besonderheiten
fact_pattern: |
  Mandantin (Maschinenbau-GmbH) hat am 02.04. von einer Zulieferin
  (ebenfalls Kaufmann) eine Charge Wälzlager bezogen (Kaufpreis
  85.000 EUR). Eingangsstichprobe ergab keine Auffälligkeiten. Bei
  Verbau am 28.04. fielen Riefen an der Mantelfläche auf, die bei
  sorgfältiger Sichtprüfung schon bei Wareneingang erkennbar gewesen
  wären. Mandantin hat am 03.05. schriftlich gerügt und Nacherfüllung
  verlangt. Zulieferin lehnt unter Berufung auf § 377 HGB ab. Bitte
  prüfen, ob die Rüge rechtzeitig war und welche Ansprüche bleiben.

must_cite:
  - "§ 343 HGB"
  - "§ 344 HGB"
  - "§ 377 HGB"
  - "§ 378 HGB"
  - "§ 121 BGB"

must_appear:
  - "beidseitiges Handelsgeschäft"
  - "unverzüglich"
  - "Untersuchung"
  - "Rüge"
  - "offener Mangel"
  - "verdeckter Mangel"
  - "Genehmigung"
  - "Beweislast"

must_flag:
  - "Pauschale Rüge"
  - "Arglist"
  - "Garantie"
---

# Test — hgb-handelsgeschaeft-besonderheiten

Struktureller Smoke-Test. Vorfrage Kaufmannseigenschaft und beidseitiges Handelsgeschäft müssen geklärt sein; § 377 HGB Untersuchungs- und Rügepflicht in den drei Stufen (offen / verdeckt / Aliud § 378) durchgeprüft; Folge "Genehmigungsfiktion" und Beweislast Käufer benannt; Ausnahmen (Arglist Abs. 5, Garantie, Deliktsansprüche) erwähnt.

Run: `python ../../../scripts/eval.py --skill handelsrecht/skills/hgb-handelsgeschaeft-besonderheiten`
