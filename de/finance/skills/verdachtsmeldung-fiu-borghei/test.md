---
skill: geldwaesche-aml-kyc/verdachtsmeldung-fiu
fact_pattern: |
  Bei einer Immobilien-Beurkundung beim Notar (Verpflichteter nach
  § 2 I Nr. 10 GwG) bietet der Käufer eine Anzahlung in Höhe von
  80.000 EUR in bar an. Käufer ist über eine Briefkastenkonstruktion
  auf den BVI zwischengeschaltet; der wirtschaftlich Berechtigte ist
  trotz Nachfrage nicht klar benennbar. Der Beurkundungstermin steht
  unmittelbar bevor. Bitte prüfen, ob Meldepflicht nach § 43 GwG
  besteht, Meldetext für goAML entwerfen, § 46 Stillhaltepflicht und
  § 47 Tippoff-Verbot beachten. Berufsrechts-Sondervorschrift § 43 II
  GwG iVm § 14a BNotO ist zu adressieren.

must_cite:
  - "§ 43 GwG"
  - "§ 46 GwG"
  - "§ 47 GwG"
  - "§ 48 GwG"
  - "§ 261 StGB"
  - "§ 14a BNotO"

must_appear:
  - "unverzüglich"
  - "Stillhaltepflicht"
  - "Tippoff"
  - "goAML"
  - "Berufsgeheimnis"
  - "wirtschaftlich Berechtigt"
  - "drei Werktage"
  - "Tatsachen"

must_flag:
  - "Tippoff"
  - "verspätete Meldung"
  - "Rechtliche Subsumtion in der goAML-Meldung"
---

# Test — verdachtsmeldung-fiu

Struktureller Smoke-Test. Pflicht-Blocker § 43 (Unverzüglichkeit), § 46 (3 Werktage Stillhaltepflicht), § 47 (Tippoff-Verbot) müssen explizit adressiert werden; Berufsrechts-Sondervorschrift § 43 II GwG iVm § 14a BNotO muss subsumiert werden; der Output darf keine Formulierung enthalten, die bei Weitergabe an den Käufer die Meldung offenbaren würde.

Run: `python ../../../scripts/eval.py --skill geldwaesche-aml-kyc/skills/verdachtsmeldung-fiu`
