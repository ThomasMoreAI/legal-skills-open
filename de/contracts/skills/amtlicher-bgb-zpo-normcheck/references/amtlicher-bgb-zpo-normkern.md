# Amtlicher BGB/ZPO-Normkern

Dieser Referenzanker verdichtet die bereitgestellten XML-Fassungen des BGB und der ZPO aus Gesetze im Internet. Er dient der Faktenhygiene: Skills sollen Normnummern, Normtitel, Reformhinweise und Prozessschnittstellen nicht aus Modellwissen erraten, sondern den aktuellen amtlichen Gesetzestext prüfen.

## XML-Stand

| Gesetz | XML-Dokument | Builddate | Rechtsstandhinweise aus der XML-Fassung |
| --- | --- | --- | --- |
| BGB | `BJNR001950896` | 2026-06-02 21:55:07 | zuletzt geändert durch Art. 1 G vom 29.03.2026 I Nr. 83; Änderung durch Art. 1 G vom 12.05.2026 I Nr. 139 textlich nachgewiesen, dokumentarisch noch nicht abschließend bearbeitet; Änderung durch Art. 2 Abs. 1 G vom 12.05.2026 I Nr. 143 berücksichtigt |
| ZPO | `BJNR005330950` | 2026-05-26 21:55:06 | zuletzt geändert durch Art. 8 G vom 10.12.2025 I Nr. 320; Änderungen durch Gesetze vom 22.12.2025 I Nr. 349 und 20.05.2026 I Nr. 152 textlich nachgewiesen, dokumentarisch noch nicht abschließend bearbeitet |

Vor tragenden Aussagen: aktuelle HTML/XML-Fassung bei Gesetze im Internet prüfen:

- BGB: https://www.gesetze-im-internet.de/bgb/
- ZPO: https://www.gesetze-im-internet.de/zpo/

## BGB AT: Normcluster

| Thema | Normen | Prüfachse |
| --- | --- | --- |
| Personen, Verbraucher, Unternehmer | §§ 1, 2, 7, 11-14 BGB | Rechtsfähigkeit, Volljährigkeit, Wohnsitz, Verbraucher-/Unternehmerrolle |
| Geschäftsfähigkeit Minderjähriger | §§ 104-113 BGB | Nichtigkeit, Einwilligung/Genehmigung, rechtlicher Vorteil, Taschengeld, Erwerbsgeschäft, Dienst-/Arbeitsverhältnis |
| Willenserklärung | §§ 116-124 BGB | geheimer Vorbehalt, Scheingeschäft, Scherz, Irrtum, falsche Übermittlung, Täuschung/Drohung, Fristen |
| Form | §§ 125-129 BGB | Formnichtigkeit, Schriftform, elektronische Form, Textform, notarielle Beurkundung, öffentliche Beglaubigung |
| Zugang | § 130 BGB | Abgabe, Machtbereich, gewöhnliche Kenntnisnahmemöglichkeit, Widerruf vor/mit Zugang |
| Auslegung, Verbot, Sittenwidrigkeit | §§ 133, 134, 138, 139, 140, 141 BGB | Auslegung vor Anfechtung, Verbotszweck, Wucher, Teilnichtigkeit, Umdeutung, Bestätigung |
| Vertragsschluss | §§ 145-157 BGB | Antrag, Annahmefrist, verspätete/abändernde Annahme, Annahme ohne Erklärung, Dissens, Auslegung |
| Bedingung und Zeitbestimmung | §§ 158-163 BGB | aufschiebend/auflösend, Bedingungsvereitelung, Zeitbestimmung |
| Stellvertretung | §§ 164-181 BGB | eigene Erklärung, fremder Name, Vertretungsmacht, Wissenszurechnung, Vollmacht, Rechtsschein, Vertreter ohne Vertretungsmacht, § 181 |
| Zustimmung und Nichtberechtigtenverfügung | §§ 182-185 BGB | Einwilligung, Genehmigung, Rückwirkung, Widerruflichkeit, Verfügung eines Nichtberechtigten |
| Fristen und Termine | §§ 186-193 BGB | Ereignisfrist, Beginn, Ende, Monats-/Jahresfristen, Sonnabend/Sonntag/Feiertag |
| Verjährung | §§ 194-218 BGB | Anspruch, regelmäßige Frist, Beginn, Hemmung, Ablaufhemmung, Neubeginn, Einrede, Nebenrechte |

## ZPO-Schnittstellen für BGB AT

| Problem | ZPO-Normen | Warum wichtig |
| --- | --- | --- |
| Elektronische Einreichung | §§ 130a, 130d ZPO | elektronisches Dokument, anwaltliche Nutzungspflicht |
| Materielle Formfiktion im Schriftsatz | § 130e ZPO | empfangsbedürftige Willenserklärung in vorbereitendem Schriftsatz mit Zustellung/Mitteilung |
| Zustellung | §§ 166-190 ZPO | Zustellungsarten, elektronische Zustellung, Ersatzzustellung, Heilung |
| Fristen | § 222 ZPO i. V. m. §§ 186-193 BGB | ZPO verweist für Fristberechnung auf BGB-Regeln |
| Wiedereinsetzung | §§ 233 ff. ZPO | Fristversäumnis gesondert von materieller Verjährung prüfen |
| Urkunden/elektronische Dokumente | §§ 371a, 415 ff. ZPO | Beweiskraft elektronischer Dokumente und öffentlicher Urkunden |

## Arbeitsregel für Skills

1. Erst Rechtsfrage und Normcluster bestimmen.
2. Dann aktuelle Norm live prüfen, wenn die Norm tragend ist.
3. Reformhinweise aus dem XML-Stand nicht verschweigen, wenn eine Norm gerade geändert wurde oder dokumentarisch noch nicht abschließend bearbeitet ist.
4. BGB-Formwirksamkeit und ZPO-Einreichungs-/Zustellungswirksamkeit getrennt halten.
5. Keine Rechtsprechung aus Modellwissen ergänzen; Entscheidungen nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.
