---
name: doc-review-danielmc09
title: Doc Review
description: '[JURISDICTION] Audita documentos que la empresa ya tiene —terminos y condiciones, politica de datos, estatutos, contratos, avisos— contra el pack de su jurisdiccion, y reporta que falta, que sobra y que afirma sin respaldo. Usar cuando ya existen documentos y hay que revisarlos, no redactarlos desde cero.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/doc-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: es
---

# Doc Review

Casi ninguna empresa parte de cero. Parte de una plantilla que alguien
copió y nadie volvió a mirar.

## Frontera con doc-drafter

| `doc-drafter` | `doc-review` |
|---|---|
| No hay documento. Se genera | Ya hay documento. Se audita |
| De la norma a la cláusula | De la cláusula a la norma |
| Salida: borrador nuevo | Salida: hallazgos y correcciones puntuales |

Si el documento está tan mal que hay que rehacerlo, **este skill lo dice** y
manda a `doc-drafter`. No lo reescribe entero por su cuenta.

## Requiere

- El documento completo. **No un resumen, no una foto parcial**
- Las capas cargadas de la jurisdicción
- Verificar el semáforo. Si el pack está VENCIDO, detente

**Sin el documento completo, no hay revisión.** Opinar sobre cláusulas que
no leíste es exactamente lo que hace daño.

---

## Las cinco categorías de hallazgo

Cada hallazgo cae en una y solo una:

| # | Categoría | Qué significa |
|---|---|---|
| 1 | **FALTA** | La norma lo exige y el documento no lo tiene |
| 2 | **AFIRMA SIN RESPALDO** | Declara algo que probablemente no es cierto |
| 3 | **JURISDICCIÓN AJENA** | Viene de otro país y aquí no aplica |
| 4 | **VAGO** | Está, pero tan genérico que no cumple su función |
| 5 | **NO VERIFICABLE** | Depende de un hueco declarado del pack |

### Por qué la 2 va antes que las demás en el reporte

**Una omisión es un hueco. Una afirmación falsa es una declaración por
escrito.**

El caso típico: una política de datos que dice "ciframos toda la
información en reposo" cuando no se cifra nada. La omisión se corrige
agregando; la afirmación falsa ya está firmada y publicada.

Señales a buscar:
- Medidas de seguridad declaradas: **pregunta cuáles existen de verdad**
- "Cumplimos con la Ley X" — nadie debería afirmar cumplimiento
- Certificaciones mencionadas: ¿existen y están vigentes?
- Plazos de respuesta prometidos: ¿hay alguien que los cumpla?
- Disponibilidad prometida: ¿se mide?

---

## Detector de jurisdicción ajena

El hallazgo más frecuente y el que más rápido se detecta. Un documento
copiado de otro país tiene huellas:

| Huella | Origen probable |
|---|---|
| RGPD, GDPR, AEPD, "interés legítimo", DPO | España o Unión Europea |
| CCPA, FTC, Delaware, "arbitration", "as is" | Estados Unidos |
| LFPDPPP, INAI, "derechos ARCO" | México |
| LGPD, ANPD, "titular dos dados" | Brasil |
| Moneda o unidad tributaria de otro país | Varias |
| Tribunales o autoridades de otro país | Varias |

**Regla:** una referencia a una norma extranjera no es solo inútil aquí —
**puede crear obligaciones que la empresa no tiene por qué asumir**, o
generar confusión sobre a qué autoridad acude un titular.

Reporta cada huella con su ubicación exacta.

---

## Procedimiento

### 1. Identificar el documento
Qué es, de qué fecha, qué versión, y **contra qué norma se escribió**. Si
cita una norma derogada o anterior a una reforma, ese es el primer
hallazgo.

### 2. Determinar qué debería contener
Del pack, según el tipo de documento y la arquitectura del negocio. **Si es
multi-tenant, carga el módulo**: la lista de lo obligatorio cambia por
completo.

### 3. Recorrer cláusula por cláusula
Cada una: ¿qué norma la respalda? ¿o no la respalda ninguna?

### 4. Recorrer al revés — lo que falta
Cada obligación del pack: ¿está en el documento? Es el paso que más
hallazgos produce y el que se salta quien solo lee el documento.

### 5. Clasificar por severidad

| Severidad | Criterio |
|---|---|
| **ALTA** | Falta algo obligatorio, o afirma algo falso |
| **MEDIA** | Vago, desactualizado, o de jurisdicción ajena sin efecto directo |
| **BAJA** | Mejorable, sin consecuencia normativa |
| **REVISAR** | No lo entendiste. **Decláralo, no lo interpretes** |

### 6. Proponer corrección puntual

Por hallazgo de severidad alta o media:

```
### <Categoría> · <Severidad>
Dónde:      <cláusula o sección>
Dice:       <cita textual breve>
Problema:   <cuál>
Norma:      <la del pack, con URL> — o "ninguna" si es afirmación sin respaldo
Corrección: <texto propuesto> — o [REDACTAR CON ABOGADO]
```

**Cita textual del documento, no paráfrasis.** Quien lo revise después
tiene que poder ubicar la cláusula.

---

## Formato del reporte

```
## Resumen
<qué documento, qué fecha, contra qué jurisdicción se revisó>

## Afirma sin respaldo — verificar primero
## Falta y es obligatorio
## Jurisdicción ajena
## Vago
## No verificable — depende de huecos del pack
## Lo que está bien
## Requiere abogado
```

**La sección "lo que está bien" no es cortesía.** Sin ella, quien recibe el
reporte reescribe cosas que ya servían.

---

## Documentos que puede revisar

Términos y condiciones · política de tratamiento de datos · aviso de
privacidad · acuerdo de encargo · autorización de titular · estatutos ·
contratos con proveedores · contratos laborales · manual interno ·
política de retención

**Para estatutos**, el criterio cambia: se revisa contra el contenido
mínimo legal del tipo societario. Una omisión ahí no es un hallazgo menor —
el registro puede abstenerse de inscribir la reforma.

---

## Qué NO hacer

- **Nunca digas que el documento "cumple".** Di qué revisaste y qué no
- **No reescribas el documento entero.** Correcciones puntuales
- No inventes la norma que respalda una cláusula. Si no la encuentras en el
  pack, el hallazgo es "sin respaldo identificado"
- **No generes cláusulas de responsabilidad, indemnidad ni jurisdicción.**
  `[REDACTAR CON ABOGADO]`
- No conviertas una duda tuya en un hallazgo. Va a REVISAR
- No revises sobre un resumen del documento
- No omitas la sección de lo que está bien

## Cierre obligatorio

> Esta revisión contrasta el documento contra las capas cargadas,
> verificadas el <fecha>. **No es una revisión legal ni una certificación
> de cumplimiento.** Lo que el pack no registró no se revisó. Confírmalo
> con un abogado antes de publicar cambios.
