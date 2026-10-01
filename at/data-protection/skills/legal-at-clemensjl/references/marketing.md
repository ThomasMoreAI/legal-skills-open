# Marketing, Newsletter, Werbung

Zwei Regime greifen parallel: **§ 174 TKG 2021** regelt die Zulässigkeit der Zusendung, die **DSGVO** die Verarbeitung der Adressdaten. Beide müssen erfüllt sein.

## § 174 TKG 2021 — Unerbetene Nachrichten

Elektronische Post zu Zwecken der Direktwerbung ist ohne vorherige Einwilligung des Empfängers unzulässig. Das gilt für E-Mail, SMS, Messenger-Nachrichten und vergleichbare Kanäle. Betroffen sind auch Nachrichten an Unternehmer — anders als beim Datenschutz schützt das TKG nicht nur Verbraucher.

**Bestandskundenausnahme (§ 174 Abs 4 TKG 2021)**, Umsetzung von Art 13 Abs 2 ePrivacy-RL. Ohne vorherige Einwilligung zulässig, wenn **alle** Voraussetzungen kumulativ vorliegen:

1. Der Absender hat die Kontaktinformation im Zusammenhang mit dem Verkauf einer Ware oder Dienstleistung an seine Kunden erhalten
2. Die Nachricht dient der Direktwerbung für **eigene ähnliche** Produkte oder Dienstleistungen
3. Der Empfänger hat klar und deutlich die Möglichkeit erhalten, diese Nutzung **bei der Erhebung** und **zusätzlich bei jeder Übertragung** kostenfrei und problemlos abzulehnen

"Ähnlich" ist eng auszulegen: Zubehör zum gekauften Produkt ja, ein völlig anderes Sortiment nein. Eine bloße Newsletter-Anmeldung ohne Kauf begründet keine Bestandskundenbeziehung.

**Weitere Grenzen:**
- Absenderidentität darf nicht verschleiert oder verheimlicht werden
- Eine funktionierende Adresse für Abmeldung muss vorhanden sein
- Verwaltungsstrafen sind vorgesehen; zusätzlich drohen Unterlassungsansprüche nach UWG

**ECG-Liste.** Bei kommerzieller Kommunikation ist die von der RTR geführte Liste jener Personen zu berücksichtigen, die keine Zusendungen wünschen (rtr.at/ecg). Vor Versand abgleichen.

## Double-Opt-In

Rechtlich nicht ausdrücklich vorgeschrieben, praktisch alternativlos, weil die Beweislast für die Einwilligung beim Absender liegt (Art 7 Abs 1 DSGVO).

Ablauf und Dokumentation:
1. Anmeldeformular mit klarer Zweckangabe, nicht vorangekreuzt, getrennt von anderen Erklärungen
2. Bestätigungsmail mit einmaligem Link, keine Werbung im Bestätigungsmail
3. Speicherung von Zeitpunkt der Anmeldung, IP-Adresse, Zeitpunkt der Bestätigung, verwendetem Einwilligungstext und dessen Version
4. Abmeldelink in jeder Aussendung, ein Klick, ohne Login, ohne Begründung
5. Abmeldungen sofort umsetzen und in einer Sperrliste festhalten

**Kopplungsverbot:** Die Einwilligung darf nicht Bedingung für eine Leistung sein, die ohne sie erbracht werden könnte. Rabatt gegen Newsletter-Anmeldung ist im Einzelfall zulässig, aber nur bei echter Wahlfreiheit und Transparenz.

## Einwilligungstext

```markdown
[ ] Ich möchte den Newsletter von [[Firma]] erhalten und willige ein, dass
    meine E-Mail-Adresse zu diesem Zweck verarbeitet wird. Der Newsletter
    enthält Informationen zu [[Inhalte konkret benennen]] und erscheint
    [[Frequenz]]. Die Einwilligung kann ich jederzeit mit Wirkung für die
    Zukunft widerrufen, etwa über den Abmeldelink in jeder E-Mail oder per
    Nachricht an [[E-Mail]]. Nähere Informationen in der
    [Datenschutzerklärung](/datenschutz).
```

Nicht vorangekreuzt, kein Sammelhäkchen mit AGB oder Datenschutzerklärung, kein "Mit dem Absenden erklären Sie sich einverstanden".

## UWG — Lauterkeitsrecht

- **§ 1 UWG:** Generalklausel gegen unlautere Geschäftspraktiken
- **§ 2 UWG:** Irreführung über Verfügbarkeit, Preis, Beschaffenheit, Auszeichnungen
- **§ 1a UWG:** aggressive Geschäftspraktiken
- **Anhang zum UWG:** Schwarze Liste jedenfalls unzulässiger Praktiken, darunter unrichtige Angaben zur Verfügbarkeit, Lockangebote, getarnte Werbung

Praktisch relevante Fälle:

| Praxis | Bewertung |
|---|---|
| Streichpreis gegen Fantasie-UVP | Irreführend; Bezugsgröße ist der niedrigste Preis der letzten 30 Tage |
| "Nur noch 2 verfügbar" ohne Deckung | Irreführung über Verfügbarkeit |
| Countdown, der bei Reload neu startet | Aggressive Praktik |
| Gekaufte oder gefilterte Bewertungen | Verboten; wer Bewertungen anzeigt, muss offenlegen, ob und wie er die Echtheit prüft |
| "Kostenlos" mit versteckten Folgekosten | Irreführung |
| Influencer-Beitrag ohne Kennzeichnung | Getarnte Werbung; Kennzeichnung deutlich, in der Sprache des Beitrags, am Anfang, nicht in Hashtag-Wolken versteckt |
| Vergleichende Werbung | Zulässig unter den Voraussetzungen des § 2a UWG, aber sachlich und nachprüfbar |

## Bewertungen und Testimonials

Wer Verbraucherbewertungen zugänglich macht, muss informieren, ob und wie sichergestellt wird, dass die Bewertungen von Verbrauchern stammen, die die Ware tatsächlich erworben oder genutzt haben. Das Unterdrücken negativer Bewertungen bei gleichzeitiger Darstellung als vollständiges Bild ist irreführend.

## Gewinnspiele

- Teilnahmebedingungen vollständig und vorab: Veranstalter, Teilnahmezeitraum, Teilnahmebedingungen, Gewinne, Ermittlung, Verständigung
- Keine Kopplung der Teilnahme an eine Newsletter-Einwilligung ohne echte Alternative
- Kein Kaufzwang, wenn das Gewinnspiel als kostenlos beworben wird
- Bei Glücksspielelementen mit Einsatz: Glücksspielgesetz prüfen, Konzessionsfrage
- Datenschutz: Zweckbindung auf das Gewinnspiel, Löschung nach Abwicklung, getrennte Einwilligung für Werbenutzung

## Affiliate und Werbekennzeichnung

Bezahlte Inhalte, Affiliate-Links und Kooperationen sind als Werbung zu kennzeichnen. Auf der eigenen Website gehört ein Hinweis in unmittelbare Nähe des Links, nicht ausschließlich in eine Fußzeile. Bei Medien mit redaktionellem Charakter kommt zusätzlich § 26 MedienG (Kennzeichnung entgeltlicher Veröffentlichungen) ins Spiel.

## Prüfpunkte

- [ ] Newsletter-Einwilligung getrennt, nicht vorangekreuzt, Zweck konkret
- [ ] Double-Opt-In aktiv, Bestätigungsmail werbefrei
- [ ] Einwilligungsnachweis mit Zeitstempel, IP und Textversion gespeichert
- [ ] Abmeldelink in jeder Aussendung, ein Klick
- [ ] Bestandskundenwerbung: alle drei Voraussetzungen des § 174 Abs 4 dokumentiert
- [ ] Ablehnungsmöglichkeit bereits bei Erhebung angeboten
- [ ] ECG-Liste vor Versand abgeglichen
- [ ] Absenderidentität nicht verschleiert, Impressum in der Aussendung
- [ ] Rabattaussagen mit 30-Tage-Bezugsgröße belegt
- [ ] Bewertungen: Echtheitsprüfung offengelegt
- [ ] Affiliate- und Kooperationsinhalte gekennzeichnet
