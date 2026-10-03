# beA-Endproduktion: Recht, Technik und verifizierte Entscheidungen

## 1. Quellenstatus

Diese Referenz trennt verbindliche Rechtsnormen, amtliche technische Bekanntmachungen, lokale Organisationshinweise und Rechtsprechung. Vor jeder fristgebundenen Einreichung ist zu prüfen, ob eine neuere ERVB, eine gerichtliche Verfügung oder eine Änderung der einschlägigen Verfahrensordnung gilt.

Kanzleiveröffentlichungen und Fachbeiträge dienen nur als Rechercheanstoß. Eine tragende Aussage wird erst verwendet, wenn sie anhand des amtlichen Normtexts oder einer amtlichen Entscheidungsfassung geprüft ist.

## 2. Verbindliche Normen und technische Bekanntmachung

| Quelle | Arbeitsbedeutung | Amtlicher Link |
| --- | --- | --- |
| ZPO Paragraf 130 | notwendige und zweckmäßige Angaben in vorbereitenden Schriftsätzen, einschließlich Anlagenbezeichnung | https://www.gesetze-im-internet.de/zpo/__130.html |
| ZPO Paragraf 130a | elektronisches Dokument, Signaturwege, Eingang, Behandlung ungeeigneter Dokumente | https://www.gesetze-im-internet.de/zpo/__130a.html |
| ZPO Paragraf 130d | Nutzungspflicht, vorübergehende technische Unmöglichkeit und Ersatzeinreichung | https://www.gesetze-im-internet.de/zpo/__130d.html |
| ERVV Paragraf 2 | PDF oder ausnahmsweise TIFF sowie technische Eignung | https://www.gesetze-im-internet.de/ervv/__2.html |
| ERVB 2025 | Dateiformate, Signaturen, Dateinamen, maximal 1000 Dateien und 200 MB je Nachricht | https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf |
| Amtlicher ERV-Leitfaden | Nachrichtenaufbau, Ein-Verfahren-Prinzip, Einzel-PDFs, Strukturdaten, Eingangsbestätigung und Paketgrenzen | https://justiz.de/ervvoe/leitfaden_erv_pdf.pdf |

Die ERVB 2025 nennt für Dateinamen maximal 90 Zeichen einschließlich Dateiendung. Sie lässt insbesondere deutsche Buchstaben, Umlaute und das Eszett zu. Ein ASCII-Dateiname mit höchstens 60 Zeichen ist daher ein strengerer Kanzleistandard, kein bundesrechtliches Muss.

Nach dem amtlichen ERV-Leitfaden betrifft eine EGVP-Nachricht genau ein Verfahren. Schriftsätze und Anlagen werden als einzelne PDF-Dateien eingereicht; ZIP-Archive sind für diesen Versand nicht zulässig. Zusätzliche Verschlüsselung, Kennwortschutz und eingeschränkte Leserechte sind zu vermeiden. Die Sendeanwendung muss die erforderlichen XJustiz-Strukturdaten zur Nachricht erzeugen; Empfänger, Aktenzeichen und Dokumentart sind vor Versand zu kontrollieren.

## 3. Gerichtliche Organisationshinweise

### 3.1 Berlin

Die Hinweise des Kammergerichts empfehlen:

1. jedes Hauptdokument und jede Anlage als eigene Datei,
2. `00` für das Hauptdokument und `01` fortlaufend für Anlagen,
3. Datum und schlagwortartigen Inhalt im Dateinamen,
4. keine Umlaute, kein Eszett und keine Sonderzeichen,
5. höchstens 60 Zeichen,
6. Anlagenbezeichnung auf sämtlichen Seiten, möglichst oben rechts.

Quelle: https://www.berlin.de/gerichte/kammergericht/service/hinweise-zur-elektronischen-einreichung-von-schriftsaetzen-und-anlagen-bei-den-ordentlichen-gerichten-berlins_final2.pdf

### 3.2 Nordrhein-Westfalen

Die E-Akte-Justiz-Hinweise empfehlen die Verfahrensrolle nur beim Hauptdokument, etwa `K_`, `B_`, `AS_`, `AG_` oder `InsoVerwalter_`. Sie enthalten fachbereichsspezifische Dokumenttypen wie `Klage`, `Klageerwiderung`, `Schriftsatz_mit_Antraegen`, `Anlage_01` und `Berufungsbegruendung`.

Quelle: https://www.justiz.nrw/sites/default/files/imported/files/2022-11/Namenskonvention-fuer-Externe-Nutzer.pdf

Diese Hinweise sind Benennungshilfen. Sie ersetzen weder ERVV und ERVB noch eine konkrete gerichtliche Verfügung.

## 4. Signatur und sicherer Übermittlungsweg

| Entscheidung | Verifizierter Arbeitssatz | Amtliche Quelle |
| --- | --- | --- |
| BGH, Beschluss vom 7. Mai 2024, VI ZB 22/23 | Bei einfacher Signatur müssen verantwortende Person und tatsächlicher Versender über das persönlich zugeordnete Postfach übereinstimmen. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024&Gericht=bgh&Seite=17&Sort=2062&anz=2887&pos=528 |
| BGH, Beschluss vom 4. September 2024, IV ZB 31/23 | Das Postfach eines anderen Anwalts wird nicht dadurch zum sicheren Übermittlungsweg, dass die verantwortende Prozessbevollmächtigte dessen Zugang benutzt. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024-9&Gericht=bgh&Seite=8&anz=267&nr=87960&pos=252 |
| BGH, Beschluss vom 27. März 2025, V ZB 27/24 | Ein zugelassener Rechtsanwalt kann auch im eigenen gerichtlichen Verfahren der elektronischen Nutzungspflicht unterliegen, wenn er ein Rechtsmittel einlegt; die private Beteiligtenrolle eröffnet dann nicht ohne Weiteres den Papierweg. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Blank=1&Datum=2025-3&Gericht=bgh&anz=237&nr=89661&pos=21 |
| BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23 | Versand durch einen Mitarbeiter erzeugt keinen vertrauenswürdigen Herkunftsnachweis; ohne persönlichen Versand ist die qualifizierte elektronische Signatur erforderlich. | https://www.bundesarbeitsgericht.de/entscheidung/7-abr-23-23/ |

## 5. Eingang und Ausgangskontrolle

| Entscheidung | Verifizierter Arbeitssatz | Amtliche Quelle |
| --- | --- | --- |
| KG, Beschluss vom 22. August 2023, 27 U 40/23 | Eingang mit Speicherung auf der für das Gericht bestimmten Empfangseinrichtung; eine verspätete interne Zuordnung wegen falschen Aktenzeichens ändert den Eingangszeitpunkt nicht. | https://gesetze.berlin.de/bsbe/document/NJRE001603142 |
| OLG Brandenburg, Beschluss vom 23. August 2022, 12 U 113/22 | Eine wirksame Ausgangskontrolle verlangt die Prüfung der gerichtlichen Eingangsbestätigung auf `request executed` und den Übermittlungsstatus `erfolgreich`; ein interner Vermerk `versendet` trägt die Fristlöschung nicht. | https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/20827 |
| BGH, Beschluss vom 30. Januar 2024, VIII ZB 85/22 | Fristgebundener beA-Versand erfordert eine organisierte Ausgangskontrolle anhand der gerichtlichen Eingangsbestätigung. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Blank=1&Datum=2024-1-30&Gericht=bgh&Sort=14&anz=45&nr=86036&pos=6 |
| BGH, Beschluss vom 24. April 2025, III ZB 12/24 | Die Eingangsbestätigung muss abgerufen und kontrolliert werden; der Zeitpunkt kann organisatorisch gewählt werden, wenn eine ausreichende Reaktionsreserve bleibt. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2025-4-24&Gericht=bgh&Sort=2051&anz=18&nr=89777&pos=11 |

## 6. Ersatzeinreichung und Formfehler

| Entscheidung | Verifizierter Arbeitssatz | Amtliche Quelle |
| --- | --- | --- |
| BGH, Beschluss vom 19. Dezember 2024, IX ZB 41/23 | Nach Veranlassung der Ersatzeinreichung sind keine fortlaufenden elektronischen Neuversuche nötig; eine zuverlässige veröffentlichte Serverstörung kann die Glaubhaftmachung tragen. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2024&Gericht=bgh&anz=3204&pos=17 |
| BGH, Beschluss vom 25. Februar 2025, VI ZB 19/24 | Die technische und vorübergehende Unmöglichkeit ist geschlossen und laienverständlich darzustellen; Bedienungs- oder persönliche Ursachen müssen nachvollziehbar ausscheiden. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2025&Gericht=bgh&Seite=22&anz=1130&nr=89684&pos=685 |
| OLG Brandenburg, Urteil vom 28. April 2023, 11 U 244/22 | Eine pauschale Störungsmitteilung und ein nicht aussagekräftiger Bildschirmabzug genügen nicht. Dauer, betroffene Postfächer und Fortbestand der Störung beim Ersatzversand müssen nachvollziehbar dargelegt und unverzüglich glaubhaft gemacht werden. | https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/21911 |
| OLG Hamm, Beschluss vom 25. März 2022, 25 U 70/21 | Fehlende einsatzbereite Zugangsmittel können gegen eine nur vorübergehende technische Störung sprechen; jedenfalls ist die Störung bei der Ersatzeinreichung oder unverzüglich danach glaubhaft zu machen. | https://nrwe.justiz.nrw.de/pdfdownload/downloadEntscheidung.php?entscheidung=%2Fnrwe%2Folgs%2Fhamm%2Fj2022%2F25_U_70_21_Beschluss_20220325.html |
| LAG Berlin-Brandenburg, Beschluss vom 23. Dezember 2024, 5 Sa 982/24 | Eine pauschale Störungsangabe genügt nicht; eine mehr als einwöchige Nachholung der Glaubhaftmachung ist regelmäßig nicht unverzüglich. | https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/27083 |
| LG Hagen, Urteil vom 15. Oktober 2024, 4 O 209/24 | Eine ohne zulässige Ersatzeinreichung auf Papier erhobene Klage ist unwirksam und wird nicht durch beliebig spätere elektronische Nachreichung geheilt. | https://nrwe.justiz.nrw.de/lgs/hagen/lg_hagen/j2024/4_O_209_24_Urteil_20241015.html |
| BVerfG, Beschluss vom 16. Februar 2023, 1 BvR 1881/21 | Nach der damals maßgeblichen Rechtslage durfte ein Gericht eine technisch ordnungsgemäße Einreichung nicht wegen einer dort nicht vorgesehenen Dateinamensgrenze übergehen. Die Entscheidung ist wegen der später eingeführten ausdrücklichen 90-Zeichen-Grenze nur historisch einzuordnen. | https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/2023/02/rk20230216_1bvr188121.html |

## 7. Verfahrensspezifische Rechtsprechung

Die technische Endfertigung beginnt mit der richtigen Verfahrensordnung. ZPO Paragraf 130a und Paragraf 130d dürfen nicht schematisch auf andere Gerichtsbarkeiten übertragen werden.

| Gerichtsbarkeit | Entscheidung oder Norm | Verifizierter Arbeitssatz | Amtliche Quelle |
| --- | --- | --- | --- |
| Arbeitsgericht | BAG, Beschluss vom 22. Januar 2025, 7 ABR 23/23 | Ein nur einfach signiertes Dokument muss vom verantwortenden Postfachinhaber selbst versandt werden; Mitarbeiter-Versand verlangt eine qualifizierte elektronische Signatur. | https://www.bundesarbeitsgericht.de/entscheidung/7-abr-23-23/ |
| Sozialgericht | BSG, Urteil vom 27. September 2023, B 2 U 1/23 R | Bei einfacher Signatur müssen verantwortende und versendende Person identisch sein. Krankheit ist keine technische Störung nach SGG Paragraf 65d. | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2023/2023_09_27_B_02_U_01_23_R.html |
| Sozialgericht | BSG, Urteil vom 21. November 2024, B 8 SO 5/23 R | Eine konkret dargestellte und belegte gerichtsseitige Großstörung kann eine Ersatzeinreichung nach SGG Paragraf 65d tragen. | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2024/2024_11_21_B_08_SO_05_23_R.html |
| Verwaltungsgericht | BVerwG, Beschluss vom 17. Januar 2023, 9 B 23.22 | Beschwerde und Begründung eines Anwalts müssen nach VwGO Paragraf 55d elektronisch eingehen; eine formwidrige Übermittlung wahrt die Frist nicht. | https://www.bverwg.de/170123B9B23.22.0 |
| Verwaltungsgericht | BVerwG, Beschluss vom 19. Dezember 2023, 8 B 26.23 | Bei erkennbarer technischer Unmöglichkeit muss der zulässige Ersatzweg rechtzeitig genutzt und die Störung nach VwGO Paragraf 55d belegt werden. | https://www.bverwg.de/de/191223B8B26.23.0 |
| Verwaltungsgericht | BVerwG, Beschluss vom 16. Mai 2025, 5 B 8.25 | Ein Signaturprotokoll belegt weder Versand noch Eingang; maßgeblich ist die automatisierte gerichtliche Eingangsbestätigung. | https://www.bverwg.de/de/160525B5B8.25.0 |
| Finanzgericht | BFH, Urteil vom 8. April 2025, VII R 4/24 | Auch beim besonderen elektronischen Steuerberaterpostfach setzt der sichere Weg bei einfacher Signatur Personenidentität zwischen Signierendem und tatsächlichem Versender voraus. | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202520201/ |
| Finanzgericht | BFH, Beschluss vom 8. Mai 2024, II R 3/23 | Ein eingerichteter sicherer Übermittlungsweg begründet die elektronische Nutzungspflicht; organisatorisch verspätete Einrichtung trägt die Papier- oder Faxeinreichung nicht. | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202450078/ |
| Strafgericht | BGH, Beschluss vom 9. August 2023, 6 StR 210/23 | Die schriftliche Revision eines Verteidigers ist nach StPO Paragraf 32d Satz 2 elektronisch zu übermitteln; Telefax ist grundsätzlich formunwirksam. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Blank=1&Datum=2023-8-9&Gericht=bgh&anz=10&nr=85712&pos=6 |
| Strafgericht | BGH, Beschluss vom 10. Juni 2025, 6 StR 146/25 | Eine per Telefax eingelegte Revision ist ohne gleichzeitige Darlegung einer vorübergehenden technischen Unmöglichkeit unzulässig. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2025&Gericht=bgh&Seite=43&Sort=3&anz=2541&pos=1312 |
| Strafgericht | BGH, Urteil vom 31. August 2023, 5 StR 447/22 | Die zwingende Übermittlungspflicht des StPO Paragrafen 32d Satz 2 gilt für Verteidiger und Rechtsanwälte, nicht ohne Weiteres für die Staatsanwaltschaft; dort ist StPO Paragraf 32b zu prüfen. | https://juris.bundesgerichtshof.de/cgi-bin/bgh_notp/document.py?Art=en&Datum=2023&Gericht=bgh&Seite=61&Sort=12&anz=2747&pos=1859 |
| Familiensache | BGH, Beschluss vom 17. Januar 2024, XII ZB 88/23 | Eine Ersatzeinreichung verlangt eine aus sich heraus verständliche, geschlossene Schilderung; persönliche oder organisatorische Hindernisse sind keine technische Störung. | https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Art=en&Blank=1.pdf&Datum=2024-1&Gericht=bgh&Seite=6&anz=362&nr=136591&pos=208 |
| Bundesverfassungsgericht | BVerfGG Paragrafen 23a bis 23c | Seit 1. August 2024 müssen Anwälte Schriftsätze und Anlagen elektronisch übermitteln; Bürger dürfen weiterhin auch schriftlich oder per Telefax einreichen. | https://www.bundesverfassungsgericht.de/DE/ERV/HaeufigGefragt/_functions/_erv_hinweistext.html |

## 8. Europäische Gerichte

Direkte Klagen beim Gericht der Europäischen Union werden über e-Curia eingereicht. Die veröffentlichte Anleitung nennt PDF, maximal 30 MB je Datei, keine notwendige handschriftliche Unterschrift und eine elektronische Einreichungsbestätigung.

- Einreichung beim Gericht: https://curia.europa.eu/site/jcms/d2_5113/de/
- e-Curia: https://curia.europa.eu/site/jcms/d2_5115/de/e-curia
- Verfahrensvorschriften und Muster: https://curia.europa.eu/site/jcms/d2_5114/de/verfahrensvorschriften

## 9. Entscheidungslogik für den Produktionslauf

1. Verfahrensordnung bestimmen.
2. Gericht und konkrete Verfügung prüfen.
3. ERVV und aktuelle ERVB prüfen.
4. Lokales Namensprofil nur als zusätzliche Organisationshilfe anwenden.
5. Signaturweg vor der Dateiproduktion festlegen.
6. Versanddateien erzeugen und technisch prüfen.
7. Automatisierte Eingangsbestätigung kontrollieren und sichern.

ZPO Paragraf 130a Absatz 6 ist kein Ersatzweg bei beA-Ausfall. Er betrifft die Behandlung eines bereits eingereichten, technisch ungeeigneten elektronischen Dokuments. Die Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit steht in ZPO Paragraf 130d Sätze 2 bis 4.
