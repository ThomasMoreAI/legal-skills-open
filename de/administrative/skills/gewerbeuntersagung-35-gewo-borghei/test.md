---
skill: gewerberecht/gewerbeuntersagung-35-gewo
fact_pattern: |
  Mandant betreibt als Einzelunternehmer einen Kfz-Handel mit angeschlossener
  Werkstatt und ist zugleich Geschäftsführer einer GmbH im Baunebengewerbe.
  Das Finanzamt hat Rückstände von 96.000 EUR mitgeteilt; Umsatzsteuer-
  voranmeldungen fehlen seit vierzehn Monaten. Bei der Einzugsstelle stehen
  18.000 EUR offen. Am 12.03.2026 hat die Behörde die Untersagung des
  Kfz-Handels sowie aller weiteren Gewerbe und der Tätigkeit als
  Geschäftsführer verfügt und die sofortige Vollziehung angeordnet; zur
  Begründung des Sofortvollzugs wiederholt sie wörtlich die
  Untersagungsgründe. Die IHK wurde nicht angehört. Nach Erlass der
  Verfügung hat der Mandant eine Ratenvereinbarung mit dem Finanzamt
  geschlossen und alle Voranmeldungen nachgeholt.

must_cite:
  - "§ 35 GewO"
  - "§ 45 GewO"
  - "§ 148 GewO"
  - "§ 28 VwVfG"
  - "§ 39 VwVfG"
  - "§ 70 VwGO"
  - "§ 74 VwGO"
  - "§ 80 VwGO"
  - "§ 266a StGB"

must_appear:
  - "Prognose"
  - "erweiterte Untersagung"
  - "Erforderlichkeit"
  - "letzte Behördenentscheidung"
  - "Industrie- und Handelskammer"
  - "Gefahr im Verzug"
  - "Wiedergestattung"
  - "eines Jahres"
  - "Stellvertreter"
  - "legal_calc"

must_flag:
  - "§ 35 GewO trotz Sperrwirkung des Abs. 8 angewandt"
  - "Maßgeblichen Beurteilungszeitpunkt verkannt"
  - "Erweiterte Untersagung ohne eigenständige Begründung"
  - "Kammeranhörung nach Abs. 4 nicht gerügt"
  - "Sofortvollzugsbegründung nicht angegriffen"
  - "Wiedergestattung erst nach Jahren geplant"
---

# Test — gewerbeuntersagung-35-gewo

Struktureller Smoke-Test. Die Ausgabe muss zuerst die Sperrwirkung des § 35 Abs. 8 GewO prüfen, die Ratenvereinbarung und die nachgeholten Voranmeldungen als **nach** dem maßgeblichen Beurteilungszeitpunkt liegend einordnen und auf den Wiedergestattungsantrag nach § 35 Abs. 6 GewO mit Jahressperre verweisen, die erweiterte Untersagung nach Abs. 1 S. 2 als begründungsbedürftige Ermessensentscheidung angreifen, die unterbliebene IHK-Anhörung nach Abs. 4 rügen, die Untersagung gegen den Geschäftsführer Abs. 7a zuordnen und die Sofortvollzugsbegründung an § 80 Abs. 3 VwGO messen. Widerspruchs- und Klagefrist sind ab dem 12.03.2026 zu berechnen.

Run: `python ../../../scripts/eval.py --skill gewerberecht/skills/gewerbeuntersagung-35-gewo`
