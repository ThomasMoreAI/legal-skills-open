---
skill: ki-vo-compliance/gpai-pflichten
fact_pattern: |
  Ein Start-up bietet ein großes Sprachmodell als Foundation Model an, das von
  Dritten in eigene Anwendungen integriert wird. Das Training erfolgte mit aus
  dem Web gescrapten Texten und Bildern, teils urheberrechtlich geschützt; die
  Trainingsrechenleistung liegt oberhalb von 10^25 FLOP. Eine technische
  Dokumentation oder Urheberrechtsstrategie existiert nicht. Welche Pflichten
  treffen das Start-up nach der KI-VO?
must_cite:
  - "Art. 53 KI-VO"
  - "Art. 55 KI-VO"
  - "Art. 101 KI-VO"
  - "Anhang XI"
  - "Anhang XII"
must_appear:
  - "technische Dokumentation"
  - "systemischem Risiko"
  - "Urheberrechtsstrategie"
  - "Code of Practice"
  - "Bußgeldrisiko"
must_flag:
  - "Falsche Einstufung"
  - "Urheberrecht"
  - "Dokumentationslücke"
  - "Bußgeldrisiko"
---

# Test — gpai-pflichten

Run: `python3 scripts/eval.py --skill ki-vo-compliance/skills/gpai-pflichten`
