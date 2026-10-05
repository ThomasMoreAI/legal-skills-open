# Otros países: cómo investigar los requisitos

Cuando el responsable del sitio no reside en México (o el sitio se dirige a personas de otros
países), la skill investiga antes de redactar. **Nada se escribe sin fuente.**

## Procedimiento

1. **Identifica las leyes aplicables:** país (y estado o provincia) del responsable, y países de
   las personas a las que se dirige el sitio (idioma, moneda, envíos). Si el sitio se dirige a
   personas en la UE, aplica el RGPD aunque el responsable esté fuera.
2. **Busca solo en fuentes oficiales:**
   - El texto de la ley en el diario o boletín oficial, o en el portal legislativo del país.
   - Las guías de la autoridad de protección de datos (suelen tener guías de cookies y modelos
     de aviso).
   - No uses blogs, generadores de políticas ni despachos como fuente: como mucho, para saber
     qué buscar.
3. **Arma un checklist** con el formato de [mexico.md](mexico.md): autoridad, contenido mínimo
   del aviso, consentimiento, datos sensibles, derechos y plazos, transferencias
   internacionales, cookies (consentimiento previo o no, plazo máximo recomendado para volver a
   preguntar) y comercio electrónico. Cada punto con su enlace y artículo.
4. **Decide el consentimiento de cookies** con lo que encontraste:
   - Consentimiento previo para cookies no necesarias → `consent.mode: "opt-in"`.
   - Basta informar y permitir rechazar → `"opt-out"`.
   - Si la autoridad recomienda un plazo máximo para volver a preguntar, ponlo en
     `consent.renewal` y cítalo.
5. **Usa el checklist en la verificación final** y entrégalo en el reporte con sus fuentes.
6. Si el país se repetirá en otros proyectos, propón guardarlo como `references/<pais>.md`.

## Puntos de partida (verifícalos siempre)

| Jurisdicción                | Norma principal                                                                 | Autoridad                                      |
| --------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------- |
| Unión Europea               | Reglamento General de Protección de Datos (RGPD) y Directiva ePrivacy (cookies) | Autoridad nacional de cada país                |
| España                      | RGPD, LOPDGDD y LSSI (aviso legal y cookies)                                    | Agencia Española de Protección de Datos (AEPD) |
| Colombia                    | Ley 1581 de 2012                                                                | Superintendencia de Industria y Comercio (SIC) |
| Argentina                   | Ley 25.326                                                                      | Agencia de Acceso a la Información Pública     |
| Chile                       | Ley 19.628 y su reforma (Ley 21.719)                                            | Agencia de Protección de Datos Personales      |
| Perú                        | Ley 29733                                                                       | Autoridad Nacional de Protección de Datos      |
| Estados Unidos (California) | CCPA modificada por la CPRA                                                     | California Privacy Protection Agency           |

Esta tabla solo orienta la búsqueda: las leyes cambian y algunas reformas tienen entrada en vigor
diferida. Confirma vigencia y artículos en la fuente oficial.

## Documentos que suelen variar por país

- **Aviso legal** (identificación del titular del sitio): obligatorio en España (LSSI) y otros.
- **Política de cookies** separada del aviso de privacidad: habitual en la UE.
- **Enlace "No vender ni compartir mi información"**: California, si aplica por tamaño o
  actividad del negocio.
- **Libro de reclamaciones:** Perú, para negocios que venden al consumidor.
