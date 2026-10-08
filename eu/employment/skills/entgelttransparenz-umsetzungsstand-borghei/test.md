---
skill: entgelttransparenz-eu/entgelttransparenz-umsetzungsstand
fact_pattern: |
  Zwei Mandanten fragen im August 2026 dasselbe: Ein kommunales
  Klinikum in der Rechtsform einer GmbH, deren Anteile vollständig
  von einem Landkreis gehalten werden und die unter Landesaufsicht
  steht, sowie eine private Softwarefirma mit 180 Beschäftigten. Beide
  haben Stellenausschreibungen ohne Entgeltangabe veröffentlicht und
  fragen Bewerber regelmäßig nach dem bisherigen Gehalt. In den
  Arbeitsverträgen beider steht eine Klausel, wonach das Entgelt
  gegenüber Kolleginnen und Kollegen geheim zu halten ist. Eine
  Mitarbeiterin des Klinikums verlangt Auskunft über die
  Durchschnittsentgelte ihrer Vergleichsgruppe. Ein deutsches
  Umsetzungsgesetz ist nicht verkündet.

must_cite:
  - "Art. 5"
  - "Art. 7"
  - "Art. 9"
  - "Art. 34"
  - "Art. 157 AEUV"
  - "§ 3 EntgTranspG"
  - "§ 10 EntgTranspG"
  - "§ 15 AGG"

must_appear:
  - "7. Juni 2026"
  - "unmittelbare Wirkung"
  - "horizontale"
  - "staatlich"
  - "richtlinienkonform"
  - "Staatshaftung"
  - "hinreichend genau"
  - "unbedingt"
  - "legal_calc"

must_flag:
  - "Richtlinienpflichten als geltendes deutsches Recht dargestellt"
  - "Unmittelbare Wirkung pauschal bejaht"
  - "Art. 157 AEUV übersehen"
  - "Richtlinienkonforme Auslegung vergessen"
  - "Umsetzungsstand nicht geprüft"
---

# Test — entgelttransparenz-umsetzungsstand

Struktureller Smoke-Test. Die Ausgabe muss die beiden Mandanten unterschiedlich behandeln: Für das kommunale Klinikum ist die Zurechnung zum Staat zu begründen und die unmittelbare Wirkung je Bestimmung zu prüfen (Art. 5 Abs. 2 und Art. 7 Abs. 5 eher ja, Art. 9 und Art. 10 eher nein); für die private Softwarefirma ist die horizontale Wirkung zu verneinen und stattdessen auf Art. 157 AEUV, das geltende EntgTranspG und die richtlinienkonforme Auslegung abzustellen. Die Verschwiegenheitsklauseln sind an Art. 7 Abs. 5 zu messen, die Frage nach dem bisherigen Gehalt an Art. 5 Abs. 2. Die Staatshaftung ist mit dem Erfordernis eines bezifferten Kausalschadens darzustellen, und es ist auszuweisen, dass der Umsetzungsstand gegen das BGBl. zu prüfen ist.

Run: `python ../../../scripts/eval.py --skill entgelttransparenz-eu/skills/entgelttransparenz-umsetzungsstand`
