# Precedentes AEPD y horquillas sancionadoras

Lista curada de sanciones relevantes para calibrar el informe. Al citarlas en el informe, usa siempre texto del tipo "La AEPD ha sancionado conductas similares como en el caso [X] con [Y]€", no atribuyas cuantías a la web auditada.

## Horquillas legales aplicables

| Norma | Tipo | Rango |
|---|---|---|
| RGPD art. 83.5 (muy grave) | Infracciones principios, consentimiento, derechos, transferencias | Hasta 20M€ o 4% facturación anual global |
| RGPD art. 83.4 (grave) | Medidas técnicas, RAT, encargados, DPO | Hasta 10M€ o 2% facturación |
| LOPDGDD art. 72 (muy grave) | Paralelas a 83.5 | Hasta 20M€ o 4% |
| LOPDGDD art. 73 (grave) | Paralelas a 83.4 | 40.001–300.000€ |
| LOPDGDD art. 74 (leve) | | Hasta 40.000€ |
| LSSI art. 39.1.a (muy grave) | Reincidencia, lucro importante | 150.001–600.000€ |
| LSSI art. 39.1.b (grave) | Cookies (art. 22.2), comunicaciones comerciales | 30.001–150.000€ |
| LSSI art. 39.1.c (leve) | Info del prestador (art. 10) | Hasta 30.000€ |
| Ley 11/2023 EAA (muy grave) | Accesibilidad muy grave | 100.001–600.000€ |

## Criterios de graduación (art. 83.2 RGPD)

Once criterios. Los más relevantes en la práctica:

- **a** — naturaleza, gravedad y duración de la infracción
- **b** — intencionalidad o negligencia
- **c** — medidas adoptadas para paliar daños
- **d** — grado de responsabilidad
- **k** — **beneficios financieros obtenidos** o pérdidas evitadas

El (k) es el que convierte una multa "pequeña" en una multa del 4% de facturación cuando hay lucro cuantificado vinculado al tratamiento.

## Precedentes recientes (usa como referencia, verifica antes de citar)

### Art. 13 RGPD — información al interesado

| Entidad | Multa | Hecho |
|---|---|---|
| BBVA | 5.000.000 € | Formulario web sin cláusula informativa adecuada (arts. 6, 13 y 14 RGPD) |
| PYME anónima | 5.000 € | Recogida de datos sin cláusula informativa |
| PYME anónima | 3.000 € | Art. 13 + desatención a requerimiento AEPD |

### Art. 22.2 LSSI — cookies sin consentimiento

| Entidad | Multa | Hecho |
|---|---|---|
| Empresa con 3 dominios (AEPD verano 2024) | 90.000 € | Múltiples brechas: sin banner, sin rechazar, sin información |
| SEAT (septiembre 2024) | 16.000 € | Cookies funcionalidad/segmentación sin consentimiento |
| Vodafone (2023) | 70.000 € | Cookies sin consentimiento adecuado |
| Twitter/X (AEPD) | 150.000 € | Cookies publicitarias sin consentimiento |
| Openbank (AEPD) | 120.000 € | Gestión de consentimiento deficiente |

### Transferencias internacionales

| Entidad | Multa | Hecho |
|---|---|---|
| TikTok (DPC Irlanda abr-2023, vinculante UE) | 530.000.000 € | Transferencias a China sin base legal |
| Meta Platforms (DPC Irlanda may-2023) | 1.200.000.000 € | Transferencias a EE.UU. tras Schrems II |

### Derechos del interesado

| Entidad | Multa | Hecho |
|---|---|---|
| Caixabank | 6.000.000 € | Bases legales inadecuadas |

## Cómo construir escenarios

Para el informe, usa **3 escenarios por cada URL auditada** y **un agregado**. Fórmula de cálculo rápida:

```
conservador = suma de mínimos de infracciones leves/graves detectadas
medio       = suma de multas típicas 2024-2025 para conductas equivalentes
agravado    = aplica criterio art. 83.5 (hasta 4% facturación) o art. 83.2.k (beneficio obtenido)
```

Si el responsable ha aportado cifra de facturación vinculada al tratamiento ilícito:

```
exposición mínima 4% = facturación declarada × 0,04
exposición agravada  = max(multa_típica × nº_infracciones, 4% facturación)
```

Siempre acompañar con la frase:
> "Estas horquillas son orientativas. La cuantía final depende de la modulación que la AEPD realice en función de los 11 criterios del art. 83.2 RGPD y de las circunstancias del expediente."

## Fuentes permanentes

- **Registro de resoluciones AEPD**: https://www.aepd.es/es/informes-y-resoluciones
- **EDPB — Directrices y decisiones vinculantes**: https://edpb.europa.eu/
- **Enforcement Tracker**: https://www.enforcementtracker.com/ (GDPR fines EU)
- **CMS Law Tracker**: https://cms.law/en/int/publication/gdpr-enforcement-tracker

Al auditar, si tienes acceso a web, consulta el enforcementtracker con el stack/proveedor del sitio para encontrar precedentes recientes específicos.

## Mantenimiento

Cuando detectes una resolución nueva útil, añádela a la tabla correspondiente con formato:
`| Entidad | Cuantía | Hecho | Fecha/Ref resolución |`
