---
skill: bankrecht/zahlungsdiensthaftung
fact_pattern: |
  Vom Konto des Mandanten wurden per Online-Banking 9.800 EUR in drei
  Überweisungen an unbekannte Empfänger abgebucht. Der Mandant hatte zuvor auf
  einer täuschend echten Bank-Phishing-Seite Zugangsdaten eingegeben, jedoch
  keine TAN bewusst freigegeben; das Institut nutzte ein veraltetes
  TAN-Verfahren ohne starke Kundenauthentifizierung. Die Bank verweigert die
  Erstattung mit dem Hinweis auf grobe Fahrlässigkeit. Haftungsverteilung
  gewünscht.
must_cite:
  - "§ 675c BGB"
  - "§ 675j BGB"
  - "§ 675u BGB"
  - "§ 675v BGB"
  - "§ 675w BGB"
must_appear:
  - "Autorisierung"
  - "Erstattungsanspruch"
  - "Kundenhaftung"
  - "starke Kundenauthentifizierung"
  - "grobe Fahrlässigkeit"
must_flag:
  - "Autorisierung"
  - "Erstattungsfrist"
  - "Grobe Fahrlässigkeit"
  - "Starke Kundenauthentifizierung"
---

# Test — zahlungsdiensthaftung

```
python3 scripts/eval.py --skill bankrecht/skills/zahlungsdiensthaftung
```
