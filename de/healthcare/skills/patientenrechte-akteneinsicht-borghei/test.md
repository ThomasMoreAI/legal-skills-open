---
skill: medizinrecht/patientenrechte-akteneinsicht
fact_pattern: |
  Patient ist nach mehrwöchiger stationärer Behandlung im Krankenhaus
  verstorben (Verdacht auf nosokomiale Sepsis nach Hüftendoprothese).
  Beide Kinder als gesetzliche Erben verlangen vollständige Einsicht
  in die Behandlungsakte (inkl. OP-Berichten, Pflegedokumentation,
  Mikrobiologie, Antibiotika-Verordnungen). Klinik verweigert mit der
  Begründung, der Verstorbene habe sich zu Lebzeiten mehrfach
  verschlossen über seine Erkrankung gezeigt, was auf einen
  „mutmaßlichen Geheimhaltungswillen" hindeute. Eine
  Schweigepflichtentbindung existiere nicht. Außerdem sei die
  Schweigepflicht nach § 203 StGB postmortal fortwirkend.

must_cite:
  - "§ 630g BGB"
  - "§ 630f BGB"
  - "Art. 15 DSGVO"
  - "Art. 9 DSGVO"
  - "§ 22 BDSG"
  - "§ 203 StGB"
  - "§ 811 BGB"

must_appear:
  - "unverzüglich"
  - "vollständige"
  - "therapeutische Gründe"
  - "Rechte Dritter"
  - "Erben"
  - "vermögensrechtlicher Interessen"
  - "mutmaßlicher Wille"
  - "Anspruchskonkurrenz"
  - "kostenfreie erste Kopie"

must_flag:
  - "Pauschale Verweigerung"
  - "restriktive Anwendung"
  - "Beweislast"
---

# Test — patientenrechte-akteneinsicht

Struktureller Smoke-Test. Erwartet wird (i) ausdrückliche Behandlung des Erbenanspruchs § 630g III BGB, (ii) klare Aussage zur Beweislast der Klinik für den mutmaßlichen Geheimhaltungswillen, (iii) parallele Prüfung Art. 15 DSGVO und (iv) Klarstellung, dass § 630g III BGB Befugnisnorm iSv § 203 StGB ist.

Run: `python ../../../scripts/eval.py --skill medizinrecht/skills/patientenrechte-akteneinsicht`
