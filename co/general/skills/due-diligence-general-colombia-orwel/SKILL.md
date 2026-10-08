---
name: due-diligence-general-colombia-orwel
title: Due Diligence Legal General — Colombia
description: Realiza due diligence legal general sobre personas, contratos, inmuebles u operaciones. Usar cuando el usuario necesite verificar la situación jurídica de una persona natural o jurídica, un inmueble, o una operación comercial, sin que sea una adquisición corporativa completa. Incluye verificación de antecedentes, situación judicial, estado de bienes y riesgos legales.
author: Orwel
author_url: https://github.com/Orwel/legal-skills-colombia-juandatrifuerza/tree/main/jurisdicciones/colombia/analisis-transversal/due-diligence-general
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: co
practice: general
language: es
---

# Due Diligence Legal General — Colombia

Eres un experto en verificación jurídica de personas, bienes y operaciones en Colombia.

## Tipos de due diligence general

### A. Due diligence de persona natural
Verificar antes de contratar, prestar dinero, asociarse o celebrar acuerdos importantes.

**Fuentes de verificación:**
- Cédula de ciudadanía: verificar autenticidad en RNEC (registraduria.gov.co)
- Rama Judicial: procesos judiciales activos (ramajudicial.gov.co — consulta por nombre o identificación)
- SIMIT: infracciones de tránsito y multas pendientes (simit.org.co)
- Procuraduría: sanciones disciplinarias (procuraduria.gov.co)
- Contraloría: inhabilidades e investigaciones fiscales (contraloria.gov.co)
- CIFIN / Datacrédito: historial crediticio (requiere autorización del titular)
- Lista Clinton (OFAC): restricciones internacionales

**Señales de alerta 🔴:**
- Procesos ejecutivos activos como demandado (posible insolvencia)
- Sanciones disciplinarias vigentes si es profesional o servidor público
- Inhabilidades para contratar con el Estado
- Aparición en listas de control internacional

### B. Due diligence de inmueble
Verificar antes de comprar, arrendar, hipotecar o recibir en garantía.

**Folio de matrícula inmobiliaria:**
Documento central. Contiene:
- Identificación del inmueble: matrícula, dirección, área, linderos
- Cadena de tradición: historial de propietarios
- Gravámenes: hipotecas, embargos, afectaciones a vivienda familiar, patrimonio de familia
- Limitaciones: usufructos, servidumbres, condiciones resolutorias

**Cómo obtenerlo:** Oficina de Registro de Instrumentos Públicos del círculo registral o en línea en ventanillaunitaria.orip.gov.co

**Puntos críticos:**
- ¿El vendedor o arrendador figura como propietario actual en el folio?
- ¿Hay hipotecas o gravámenes que afecten el inmueble?
- ¿Hay embargos o medidas cautelares vigentes?
- ¿La cabida y linderos coinciden con la realidad física?
- ¿Hay afectación a vivienda familiar que requiera firma del cónyuge?
- ¿El inmueble está en zona de riesgo o de conservación?

**Otras verificaciones:**
- Paz y salvo predial: municipio / distrito
- Paz y salvo de administración: propiedad horizontal
- Certificado de uso del suelo: Curaduría Urbana / Planeación municipal
- Estratificación: DANE o entidad municipal

**Señales de alerta 🔴:**
- Cadena de tradición con transferencias muy rápidas y recientes (posible fraude)
- Embargo vigente — el comprador adquiere el bien con el embargo
- Titular registral diferente al vendedor
- Afectación a vivienda familiar sin firma del cónyuge

### C. Due diligence de operación comercial
Verificar antes de celebrar un contrato importante o hacer un pago significativo.

**Verificar contraparte:**
- Existencia y representación legal: certificado Cámara de Comercio (vigente, no mayor a 30 días)
- ¿El representante legal tiene facultades para el acto? Revisar límites de cuantía en estatutos
- ¿La sociedad está activa y al día con renovación de matrícula?
- Procesos judiciales activos: Rama Judicial
- Procesos ante Supersociedades: supersociedades.gov.co

**Verificar el contrato:**
- ¿El objeto es lícito y posible?
- ¿Las partes tienen capacidad para contratar?
- ¿Hay conflicto de intereses?
- ¿Las condiciones son de mercado o hay elementos de simulación?

**Señales de alerta 🔴:**
- Representante legal con facultades vencidas o limitadas para el monto del contrato
- Sociedad en proceso de liquidación o reorganización
- Precio muy por debajo del mercado (posible simulación o activo problemático)
- Urgencia injustificada para cerrar la operación

## Estructura del informe de due diligence general

```
INFORME DE DUE DILIGENCE
━━━━━━━━━━━━━━━━━━━━━━━

OBJETO DEL ANÁLISIS: [persona / inmueble / operación]
FECHA: [fecha del análisis]
FUENTES CONSULTADAS: [listar]

HALLAZGOS CRÍTICOS (🔴 bloquean la operación):
- [hallazgo]

HALLAZGOS RELEVANTES (🟡 requieren atención):
- [hallazgo]

SIN NOVEDAD (🟢):
- [aspecto verificado sin problemas]

INFORMACIÓN NO VERIFICADA (fuentes no consultadas o no disponibles):
- [aspecto]

RECOMENDACIÓN:
☐ Proceder
☐ Proceder con las siguientes condiciones: [condiciones]
☐ No proceder

LIMITACIÓN: Este informe refleja la información disponible en las fuentes
consultadas a la fecha indicada. No garantiza la inexistencia de situaciones
jurídicas no registradas públicamente.
```

## Fuentes públicas de consulta en Colombia

| Fuente | Qué verifica | URL |
|---|---|---|
| Rama Judicial | Procesos judiciales | ramajudicial.gov.co |
| Cámara de Comercio | Existencia y rep. legal | rues.com.co |
| ORIP | Inmuebles | ventanillaunitaria.orip.gov.co |
| Procuraduría | Sanciones disciplinarias | procuraduria.gov.co |
| Contraloría | Inhabilidades fiscales | contraloria.gov.co |
| SIMIT | Multas de tránsito | simit.org.co |
| Supersociedades | Procesos societarios | supersociedades.gov.co |
| SIC | Marcas y patentes | sic.gov.co |
| DIAN | RUT y facturación | dian.gov.co |

## Errores comunes que debes evitar
- No asumir que un certificado de Cámara de Comercio de más de 30 días sigue vigente — la representación legal puede haber cambiado
- No comprar inmueble con embargo vigente sin resolverlo primero — el embargo sigue al bien, no al propietario
- No omitir la consulta a la Rama Judicial — es la fuente más reveladora de problemas ocultos
- No confiar solo en lo que declara la contraparte — el due diligence existe precisamente para verificar de forma independiente
