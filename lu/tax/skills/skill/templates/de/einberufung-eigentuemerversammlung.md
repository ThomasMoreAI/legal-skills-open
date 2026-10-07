Wohnungseigentümergemeinschaft {{ residenz.name }}
{{ residenz.adresse }}
RCS: {{ residenz.rcs | default('—') }}

Verwalter: {{ verwalter.name }}
{{ verwalter.adresse }}
Tel.: {{ verwalter.telefon }} · E-Mail: {{ verwalter.email }}

{{ ort }}, den {{ datum }}

# Einladung zur ordentlichen Eigentümerversammlung

Sehr geehrte Eigentümerinnen und Eigentümer,

als Verwalter der Residenz {{ residenz.name }} lade ich Sie hiermit zur ordentlichen Eigentümerversammlung ein.

**Datum:** {{ versammlung.datum }}
**Uhrzeit:** {{ versammlung.uhrzeit }} Uhr
**Ort:** {{ versammlung.ort }}

## Tagesordnung

{% for punkt in tagesordnung %}
{{ loop.index }}. {{ punkt }}
{% endfor %}

## Beilagen

{% for beilage in beilagen %}
- {{ beilage }}
{% endfor %}

## Stimmrecht und Vertretung

- Jeder Miteigentümer verfügt über eine Stimmenanzahl, die seinem Tausendstelanteil am Gemeinschaftseigentum entspricht.
- Vertretung ist durch schriftliche Vollmacht möglich; ein Bevollmächtigter darf jedoch nicht mehr als drei Stimmen auf sich vereinen (außer wenn die Gesamtsumme weniger als 5 % der Stimmen beträgt).
- Rechtsgrundlage: Gesetz vom 16. Mai 1975 über das Wohnungseigentum (in seiner aktuellen Fassung).

## Hinweise

- Falls Sie nicht teilnehmen können, senden Sie uns Ihre Vollmacht bitte bis spätestens {{ vollmacht_frist }} per E-Mail oder Post zurück.
- Die Beschlüsse werden in einem Sitzungsprotokoll festgehalten und Ihnen anschließend zugestellt.

Mit freundlichen Grüßen

{{ verwalter.name }}
Verwalter der Residenz {{ residenz.name }}
