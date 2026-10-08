---
skill: schiedsverfahren-adr/schiedsverfahren-fuehrung
fact_pattern: |
  In einem DIS-Schiedsverfahren mit Schiedsort München vertreten wir die
  Beklagte. Die Schiedsklage ging am 15.01.2026 zu. Die Klägerin hat
  ihren Schiedsrichter benannt; unsere Mandantin hat bislang niemanden
  benannt. Am 05.03.2026 wurde bekannt, dass der von der Klägerin
  benannte Schiedsrichter seit drei Jahren regelmäßig als Berater für
  deren Muttergesellschaft tätig ist; offengelegt wurde das nie. In der
  ersten Verfahrenskonferenz hat das Schiedsgericht unseren Antrag auf
  Vernehmung zweier Zeugen ohne Begründung zurückgewiesen und erklärt,
  eine mündliche Verhandlung sei entbehrlich. Die Klägerin hat beim
  Schiedsgericht zugleich eine Sicherungsanordnung über ein Bankkonto
  erwirkt und will daraus unmittelbar vollstrecken.

must_cite:
  - "§ 1034 ZPO"
  - "§ 1035 ZPO"
  - "§ 1036 ZPO"
  - "§ 1037 ZPO"
  - "§ 1041 ZPO"
  - "§ 1042 ZPO"
  - "§ 1047 ZPO"
  - "§ 1054 ZPO"
  - "§ 1057 ZPO"
  - "§ 1062 ZPO"
  - "§ 204 BGB"

must_appear:
  - "Offenlegung"
  - "rechtliches Gehör"
  - "zwei Wochen"
  - "eines Monats"
  - "Vollziehung"
  - "Oberlandesgericht"
  - "protokolliert"
  - "Aufhebungsgrund"
  - "Kostenschiedsspruch"
  - "legal_calc"

must_flag:
  - "Gehörsverstoß nicht sofort gerügt"
  - "Ablehnungsfristen versäumt"
  - "Anordnung des Schiedsgerichts nach § 1041 ZPO für vollstreckbar gehalten"
  - "Schiedsspruch ohne Angabe von Tag und Schiedsort"
  - "Verjährungshemmung falsch datiert"
---

# Test — schiedsverfahren-fuehrung

Struktureller Smoke-Test. Die Ausgabe muss die unterbliebene Offenlegung an § 1036 Abs. 1 ZPO messen, die Zweiwochenfrist des § 1037 Abs. 2 ZPO ab 05.03.2026 und die Monatsfrist des § 1037 Abs. 3 ZPO berechnen, die Zurückweisung der Beweisanträge und die Ablehnung der mündlichen Verhandlung als Gehörsproblem nach § 1042 Abs. 1 und § 1047 ZPO mit sofortiger protokollierter Rüge behandeln, die Sicherungsanordnung als nicht unmittelbar vollstreckbar einordnen und auf § 1041 Abs. 2 ZPO iVm § 1062 Abs. 1 Nr. 3 ZPO verweisen sowie die Verjährungshemmung auf den Zugang der Schiedsklage am 15.01.2026 datieren. Die eigene Schiedsrichterbenennung und die Folgen des § 1035 Abs. 3 ZPO sind zu adressieren.

Run: `python ../../../scripts/eval.py --skill schiedsverfahren-adr/skills/schiedsverfahren-fuehrung`
