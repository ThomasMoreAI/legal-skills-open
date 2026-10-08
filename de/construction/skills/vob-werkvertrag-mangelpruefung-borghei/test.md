---
skill: baurecht/vob-werkvertrag-mangelpruefung
fact_pattern: |
  Privater Bauherr (Verbraucher) beauftragt Generalunternehmer mit
  Errichtung eines Einfamilienhauses. Der Vertrag verweist pauschal
  auf die VOB/B und enthält daneben individuelle Klauseln zur
  Schlusszahlung und zur Bauzeitverlängerung. Förmliche Abnahme am
  14.03.2021. Im Februar 2026 zeigen sich erhebliche Risse im Estrich
  des Erdgeschosses. Bauherr verlangt Nacherfüllung; GU lehnt unter
  Verweis auf § 13 Nr. 4 VOB/B (4 Jahre) ab und behauptet Verjährung.
  Mandant: Bauherr. Bitte Vertragsregime, VOB/B-Wirksamkeit gegenüber
  Verbraucher, Verjährung und Reihenfolge der Mängelrechte mit
  Fristsetzung prüfen; Mängelrüge entwerfen.

must_cite:
  - "§ 633 BGB"
  - "§ 634 BGB"
  - "§ 634a BGB"
  - "§ 640 BGB"
  - "§ 650i BGB"
  - "§§ 305"

must_appear:
  - "Verbraucherbauvertrag"
  - "im Ganzen"
  - "AGB-Inhaltskontrolle"
  - "Nacherfüllung"
  - "Fristsetzung"
  - "Abnahme"
  - "5 Jahre"

must_flag:
  - "VOB/B-Privilegierung"
  - "Fristsetzung"
  - "Verjährung"
---

# Test — vob-werkvertrag-mangelpruefung

Struktureller Smoke-Test. Vertragsregime (Verbraucherbauvertrag § 650i) und VOB/B-„im Ganzen"-Falle (ggü. Verbraucher keine Privilegierung) müssen klar adressiert werden; Mängelrechte müssen in der gesetzlichen Reihenfolge mit ausdrücklicher Fristsetzung zur Nacherfüllung geprüft sein; Verjährung § 634a I Nr. 2 BGB (5 Jahre ab Abnahme) muss vorrangig vor § 13 Nr. 4 VOB/B greifen.

Run: `python ../../../scripts/eval.py --skill baurecht/skills/vob-werkvertrag-mangelpruefung`
