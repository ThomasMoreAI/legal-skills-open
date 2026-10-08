---
skill: produktrecht/prodhaftg-herstellerhaftung
fact_pattern: |
  Verbraucherin (Privathaushalt) wurde durch einen berstenden Akku
  eines Haushaltsgeräts der Marke X am Arm verletzt (Verbrennungen
  zweiten Grades, ambulante Behandlung, Arbeitsausfall 3 Wochen).
  Inverkehrbringen des Geräts: 03/2022. Schadensereignis: 11/2024.
  Hersteller sitzt in DE; Akku-Zulieferer in CN. Erste Hinweise auf
  ähnliche Vorfälle in einem Online-Forum bereits 04/2024. Hersteller
  hat keine Warnung oder Rückrufaktion durchgeführt. Mandantin
  (Geschädigte) will Schmerzensgeld und Schadenersatz geltend machen.

must_cite:
  - "§ 1 ProdHaftG"
  - "§ 3 ProdHaftG"
  - "§ 4 ProdHaftG"
  - "§ 12 ProdHaftG"
  - "§ 13 ProdHaftG"
  - "§ 823"
  - "§ 253"
  - "Hühnerpest"

must_appear:
  - "Konstruktionsfehler"
  - "Fabrikationsfehler"
  - "Instruktionsfehler"
  - "Produktbeobachtung"
  - "Beweislastumkehr"
  - "Schmerzensgeld"
  - "Anspruchskonkurrenz"
  - "Risikosphäre"
  - "08.12.2026"
  - "RL (EU) 2024/2853"
  - "Übergangsrecht"

must_flag:
  - "Erlöschen"
  - "Versicherer"
  - "Produktbeobachtungspflicht"
  - "Stichtag 08.12.2026 nicht geprüft"
  - "85-Mio.-EUR-Höchstgrenze auf Neuprodukte angewandt"
  - 'Software als „kein Produkt" abgetan'
---

# Test — prodhaftg-herstellerhaftung

Struktureller Smoke-Test. Beide Anspruchsgrundlagen (§ 1 ProdHaftG und § 823 BGB) müssen parallel geprüft werden; die Fehlertypologie (Konstruktion / Fabrikation / Instruktion / Produktbeobachtung) muss explizit erscheinen; Schmerzensgeld muss auf § 253 II BGB gestützt werden; Verjährung und Erlöschen § 12 / § 13 ProdHaftG müssen sauber getrennt sein.

**Regime-Weichenstellung.** Das Gerät des Sachverhalts wurde 03/2022 in Verkehr gebracht, also **vor dem Stichtag 08.12.2026** — es gilt das **ProdHaftG 1989**, einschließlich der 85-Mio.-EUR-Höchstgrenze des § 10. Die Prüfung muss diese Weichenstellung jedoch **ausdrücklich vornehmen** und darf sie nicht stillschweigend unterstellen; für Produkte ab dem 09.12.2026 gilt das neue Recht der **RL (EU) 2024/2853** (Software als Produkt, Wegfall der Höchstgrenze, Offenlegungspflicht Art. 9, Beweisvermutungen).

Die Assertions zur Höchstgrenze und zum Produktbegriff wurden um die Stichtagsbedingung ergänzt, weil sie zuvor das ProdHaftG 1989 unbefristet als geltendes Recht unterstellten.

Run: `python ../../../scripts/eval.py --skill produktrecht/skills/prodhaftg-herstellerhaftung`
