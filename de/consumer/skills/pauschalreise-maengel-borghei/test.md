---
skill: reise-fluggastrecht/pauschalreise-maengel
fact_pattern: |
  Mandanten buchten bei einem deutschen Reiseveranstalter eine
  14-tägige Pauschalreise (Flug, Hotel, Transfer) zum Gesamtpreis von
  4.200 EUR; die Reise sollte vertragsgemäß am 24.08.2024 enden. Vor
  Ort wurden sie in einem anderen als dem gebuchten Hotel
  untergebracht. Vom dritten Tag an bestand Baulärm von 7 bis 18 Uhr,
  der Pool war sechs Tage gesperrt, die Klimaanlage war während der
  gesamten Reise defekt. Die Reiseleitung wurde am dritten Tag
  mündlich informiert, ein Mängelprotokoll wurde nicht ausgehändigt.
  Abhilfe erfolgte nicht. Die Mandanten fragen nach Minderung,
  Schadensersatz und entgangener Urlaubsfreude.

must_cite:
  - "§ 651a BGB"
  - "§ 651i BGB"
  - "§ 651j BGB"
  - "§ 651k BGB"
  - "§ 651l BGB"
  - "§ 651m BGB"
  - "§ 651n BGB"
  - "§ 651o BGB"

must_appear:
  - "Reiseveranstalter"
  - "Reisemangel"
  - "Abhilfeverlangen"
  - "Anzeigeobliegenheit"
  - "Selbstabhilfe"
  - "Minderung"
  - "Frankfurter Tabelle"
  - "Orientierungshilfe ohne Bindungswirkung"
  - "entgangene Urlaubsfreude"
  - "Tagesreisepreis"
  - "legal_calc"
  - "Mängelanzeige und Forderungsschreiben"

must_flag:
  - "Mängelanzeige unterblieben"
  - "Abhilfefrist nicht gesetzt"
  - "Frankfurter Tabelle als Rechtsgrundlage zitiert"
  - "Minderungsquoten addiert"
  - "Verjährung § 651j BGB verkannt"
---

# Test — pauschalreise-maengel

Struktureller Smoke-Test. Der Anspruchsgegner muss der Reiseveranstalter sein und von Leistungsträger und Vermittler abgegrenzt werden. Anzeige nach § 651o BGB und Abhilfeverlangen nach § 651k BGB müssen als Obliegenheiten vor den Rechtsfolgen stehen. Die Minderung muss über § 651m BGB als Rechtsgrundlage laufen; die Frankfurter Tabelle ist ausdrücklich als Orientierungshilfe ohne Bindungswirkung zu kennzeichnen. Die Verjährung nach § 651j BGB muss vom vertraglichen Reiseende aus gerechnet und der Rechner dafür verdrahtet sein.

Run: `python ../../../scripts/eval.py --skill reise-fluggastrecht/skills/pauschalreise-maengel`
