# Pack normativo — Ley N° 18.331 (Uruguay)

Pack principal de `compliance-uy`. Conecta cada control con su base normativa, plazos y
definiciones. Todo cita `(Norma, art. — sources/archivo.md)`. Lo no verificable: `[verificar contra fuente oficial]`.

> **Disclaimer:** Este software no constituye asesoramiento legal ni garantiza cumplimiento.
> Genera borradores y diagnósticos técnicos fundados en fuentes oficiales para facilitar una
> primera implementación.

## Marco normativo cubierto

| Norma | Rol | Archivo |
|---|---|---|
| Ley N° 18.331 (11/08/2008) | Ley base de protección de datos / habeas data | `sources/ley-18331.md` |
| Decreto N° 414/009 | Reglamento de la Ley 18.331 | `sources/decreto-414-009.md` |
| Ley N° 19.670, arts. 37-40 (15/10/2018) | Extraterritorialidad, brechas, responsabilidad proactiva, DPO | `sources/ley-19670-arts-37-40.md` |
| Decreto N° 64/020 (17/02/2020) | Reglamenta arts. 37-40 de la Ley 19.670 | `sources/decreto-64-020.md` |
| Guías / Resoluciones URCDP | Criterio interpretativo de la autoridad de control | `sources/urcdp-guias.md` |

La autoridad de control es la **URCDP** (Unidad Reguladora y de Control de Datos Personales),
órgano desconcentrado de AGESIC.

## Definiciones operativas (Ley 18.331, art. 4 — `sources/ley-18331.md`)

- **Dato personal:** información de cualquier tipo referida a personas físicas o jurídicas determinadas o determinables.
- **Dato sensible:** datos que revelen origen racial y étnico, preferencias políticas, convicciones religiosas o morales, afiliación sindical, e informaciones referentes a la salud o a la vida sexual.
- **Responsable:** quien decide sobre la finalidad, contenido y uso de la base/tratamiento.
- **Encargado del tratamiento:** quien trata datos por cuenta del responsable.
- **Disociación:** tratamiento que impide vincular la información a persona determinada o determinable.

> La Ley uruguaya también alcanza a **personas jurídicas** determinadas o determinables, a
> diferencia de otros regímenes. `[verificar alcance exacto contra fuente oficial]`

## Principios (Ley 18.331, art. 5 y ss. — `sources/ley-18331.md`)

Legalidad (art. 6), veracidad / datos no excesivos (art. 7), finalidad (art. 8
`[verificar numeración]`), previo consentimiento informado (art. 9), seguridad (art. 12, en la
redacción del art. 39 de la Ley 19.670), reserva y responsabilidad.

## Plazos clave (citados)

| Plazo | Materia | Base |
|---|---|---|
| 5 días hábiles | Responder acceso / rectificación del titular | Ley 18.331, arts. 14-15 — `sources/ley-18331.md` `[verificar numeración]` |
| 24 horas | Iniciar minimización del impacto de un incidente | Decreto 64/020, art. 4 — `sources/decreto-64-020.md` |
| 72 horas | Notificar la vulneración a la URCDP | Decreto 64/020, art. 4 — `sources/decreto-64-020.md` |
| 90 días | Comunicar a la URCDP la designación/cese del DPO | Decreto 64/020, art. ~13 — `sources/decreto-64-020.md` |

## Mapa norma → control

| Control | Base normativa principal |
|---|---|
| C-01 Responsable/Encargado | Ley 18.331 arts. 4, 29; Decreto 414/009 |
| C-02 Consentimiento/base legítima | Ley 18.331 arts. 9, 18 |
| C-03 Información/transparencia | Ley 18.331 art. 13 `[verificar numeración]` |
| C-04 Finalidad | Ley 18.331 arts. 5, 8 `[verificar numeración]` |
| C-05 Minimización | Ley 18.331 art. 7; Decreto 64/020 arts. 7-9 |
| C-06 Seguridad | Ley 18.331 art. 12 (red. art. 39 Ley 19.670); Decreto 64/020 arts. 5, 7 |
| C-07 Derechos del titular | Ley 18.331 arts. 14, 15, 16 `[verificar numeración]` |
| C-08 Retención | Ley 18.331 art. 7; Decreto 64/020 art. 7 |
| C-09 Contratos con encargados | Ley 18.331 art. 29; Ley 19.670 (documentación por contrato) |
| C-10 Transferencias internacionales | Ley 18.331 art. 23; Decreto 414/009; Res. URCDP 63/2023, 70/2023 |
| C-11 Incidentes/brechas | Ley 19.670 art. 38; Decreto 64/020 arts. 3-4 |
| C-12 Datos sensibles | Ley 18.331 arts. 4, 18, 19; Decreto 64/020 art. 6 |
| C-13 DPO (condicional) | Ley 19.670 art. 40; Decreto 64/020 arts. 10-15 |
| C-14 Registro de bases (condicional) | Ley 18.331 art. 6; Decreto 414/009 |

## Transferencias internacionales (Ley 18.331, art. 23 — `sources/ley-18331.md`)

Regla general: **prohibición** de transferir a países/organismos sin nivel de protección
adecuado. Excepciones tasadas (paráfrasis, verificar texto): consentimiento inequívoco del
titular; ejecución de un contrato con el interesado; cooperación judicial internacional;
intercambio de datos médicos por razones de salud pública; transferencias bancarias/bursátiles;
tratados internacionales; cooperación entre organismos de inteligencia. Si no aplica una
excepción, se requiere **autorización de la URCDP** (procedimiento del Decreto 414/009).
Las Resoluciones URCDP 63/2023 y 70/2023 regulan el caso de EE. UU. (Marco de Privacidad
UE-EEUU) y deberes de información al titular. `[verificar resoluciones contra fuente oficial]`

## Sanciones (Ley 18.331, art. 35 — `sources/ley-18331.md`)

Apercibimiento/observación, multa, suspensión de la base (hasta 5 días) y clausura de la base
(medida más severa, con control judicial previo). `[verificar montos y graduación vigentes]`

## Evaluación de impacto — EIPD (Decreto 64/020, art. 6 — `sources/decreto-64-020.md`)

Obligatoria, **previa** al tratamiento, cuando: (a) se usen datos sensibles como negocio
principal; (b) tratamiento permanente/estable de datos especialmente protegidos o de
infracciones; (c) evaluación de aspectos personales para crear perfiles (rendimiento laboral,
situación económica, salud, intereses, comportamiento, solvencia, localización); entre otros.
Estructura sugerida en `templates/evaluacion-riesgo-privacidad.md` (alinear con la Guía URCDP).
