{{ glaeubiger.name }}
{{ glaeubiger.adresse }}
USt-IdNr.: {{ glaeubiger.ust_id }}

{{ ort }}, den {{ datum }}

EINSCHREIBEN MIT RÜCKSCHEIN
{{ schuldner.name }}
{{ schuldner.adresse }}

Betreff: {{ mahnstufe | default('Erste Mahnung') }} – Rechnung Nr. {{ rechnung.nummer }} vom {{ rechnung.datum }}

Sehr geehrte Damen und Herren,

trotz unserer Rechnung Nr. **{{ rechnung.nummer }}** vom {{ rechnung.datum }} über einen Bruttobetrag von **{{ rechnung.betrag_eur }} EUR**, fällig am **{{ rechnung.faellig_am }}**, konnten wir bis heute keinen Zahlungseingang feststellen.

Wir fordern Sie daher hiermit auf, den ausstehenden Betrag von

**{{ rechnung.betrag_eur }} EUR**

bis spätestens **{{ neue_frist }}** auf folgendes Konto zu überweisen:

- Bank: {{ glaeubiger.bank }}
- IBAN: {{ glaeubiger.iban }}
- BIC: {{ glaeubiger.bic }}
- Verwendungszweck: Rechnung {{ rechnung.nummer }}

## Verzugszinsen

Gemäß Artikel 1153 des luxemburgischen Zivilgesetzbuches und der ministeriellen Verordnung über den gesetzlichen Zinssatz fallen ab dem ursprünglichen Fälligkeitsdatum Verzugszinsen in Höhe von **{{ verzugszins_satz | default('8') }} %** pro Jahr an. Bei Geschäften zwischen Unternehmen kommt zusätzlich eine pauschale Beitreibungsentschädigung von **40 EUR** hinzu (Gesetz vom 18. April 2004 über Zahlungsfristen).

## Weiteres Vorgehen bei Nichtzahlung

Sollte der Betrag nicht innerhalb der oben genannten Frist eingehen, sehen wir uns gezwungen, ohne weitere Ankündigung gerichtliche Schritte einzuleiten. Sämtliche daraus entstehenden Kosten (Anwalts-, Gerichts- und Vollstreckungskosten) gehen zu Ihren Lasten.

Falls Sie die Zahlung bereits veranlasst haben, betrachten Sie dieses Schreiben bitte als gegenstandslos.

Mit freundlichen Grüßen

{{ glaeubiger.unterzeichner }}
{{ glaeubiger.funktion }}
{{ glaeubiger.name }}
