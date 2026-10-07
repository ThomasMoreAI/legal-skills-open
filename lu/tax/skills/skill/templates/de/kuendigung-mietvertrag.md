{{ mieter.name }}
{{ mieter.adresse }}

{{ ort }}, den {{ datum }}

EINSCHREIBEN MIT RÜCKSCHEIN
{{ vermieter.name }}
{{ vermieter.adresse }}

Betreff: Kündigung des Mietvertrags vom {{ vertrag.datum }} betreffend die Wohnung in {{ wohnung.adresse }}

Sehr geehrte/r {{ vermieter.anrede | default('Damen und Herren') }},

hiermit kündige ich den am {{ vertrag.datum }} zwischen Ihnen und mir abgeschlossenen Mietvertrag betreffend die oben genannte Wohnung fristgerecht zum

**{{ kuendigung_zum }}**.

Die vertragliche bzw. gesetzliche Kündigungsfrist von **{{ frist_monate | default('3') }} Monaten** wird hiermit eingehalten.

## Wohnungsübergabe

Ich schlage vor, die Wohnungsübergabe am **{{ uebergabe.datum }} um {{ uebergabe.uhrzeit }} Uhr** vor Ort vorzunehmen. Ein gemeinsames Wohnungsabnahmeprotokoll wird dabei erstellt und von beiden Parteien unterzeichnet.

Falls dieser Termin Ihnen nicht passt, bitte ich um einen Gegenvorschlag innerhalb von 8 Tagen.

## Kaution

Ich gehe davon aus, dass die hinterlegte Kaution in Höhe von **{{ kaution.betrag }} EUR** abzüglich etwaiger berechtigter Abzüge gemäß Artikel 5 des Gesetzes vom 21. September 2006 über den Wohnraummietvertrag innerhalb eines Monats nach der Wohnungsübergabe auf folgendes Konto zurückerstattet wird:

- IBAN: {{ mieter.iban }}
- Inhaber: {{ mieter.name }}

## Neue Anschrift

Ab dem {{ kuendigung_zum }} bin ich unter folgender Adresse erreichbar:

{{ mieter.neue_adresse }}

Mit freundlichen Grüßen

{{ mieter.name }}
Mieter
