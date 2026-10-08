---
name: legal-pyme-mx-lahh1986
title: legal-pyme-mx — Cumplimiento legal federal para PyMEs
description: 'Usar cuando el usuario tenga una PyME mexicana y necesite ayuda con

  CUMPLIMIENTO LEGAL FEDERAL: validar RFC/CURP/CFDI, checar si un proveedor

  está en lista 69-B SAT (riesgo de no deducibilidad), generar Aviso de

  Privacidad LFPDPPP 2025, auditar compliance e-commerce (LFPC reforma

  2025), entender obligaciones IMSS/INFONAVIT/STPS, NOM-035, REPSE,

  LFPIORPI Antilavado, calcular Impuesto Sobre Nómina por estado.

  Anclado en corpus oficial descargado (SAT, INAI, STPS, Diputados, RENAPO).


  Triggers: "valida este RFC", "valida CURP", "este proveedor está en 69-B",

  "lista negra SAT", "facturera", "EFOS", "aviso de privacidad", "LFPDPPP",

  "datos personales", "e-commerce México obligaciones", "PROFECO LFPC",

  "suscripción recurrente cancelación", "NOM-035", "riesgo psicosocial",

  "REPSE", "outsourcing legal", "subcontratación", "antilavado", "LFPIORPI",

  "actividad vulnerable", "ISN estado", "Impuesto Sobre Nómina", "abrir

  empresa México obligaciones", "cumplimiento PyME".'
author: lahh1986
author_url: https://github.com/lahh1986/sistemia-skills-mx/tree/main/skills/legal-pyme-mx
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: mx
practice: regulatory
language: es
---

# legal-pyme-mx — Cumplimiento legal federal para PyMEs

> Wrapper sobre el corpus legal oficial MX (~120 MB, 30+ archivos) que vive
> en `~/sistemia-skills-mx/research/{sat,inai,stps,diputados,renapo}/`.
> Para mapa temático del corpus: [`research/legal-INDEX.md`](../../research/legal-INDEX.md).

## Cuándo activarte

- El usuario te pasa un RFC y pregunta si es válido o si está en lista 69-B
- El usuario tiene una PyME y quiere saber qué obligaciones legales tiene
- El usuario va a abrir e-commerce y necesita checklist de cumplimiento LFPC/LFPDPPP
- El usuario va a contratar empleados y pregunta sobre IMSS/INFONAVIT/NOM-035
- El usuario hace outsourcing o presta servicios y pregunta sobre REPSE
- El usuario hace negocio sensible (joyería, autos, inmuebles, préstamos) y se pregunta sobre antilavado
- El usuario menciona PROFECO, contratos de adhesión, distintivo digital
- El usuario quiere registrar marca y pregunta sobre IMPI / similitud

**NO actives si:** el usuario pide asesoría legal específica que requiera abogado (litigio, juicio mercantil, demanda laboral particular). El skill da **información de cumplimiento**, no consejo legal personalizado. Avisa al usuario y refiere a abogado.

## Módulos disponibles (v1.0)

| Módulo | Script | Resuelve |
|---|---|---|
| 1. RFC validator | `scripts/validate_rfc.py` | Estructura + lista 69-B + listas 69 CFF |
| 2. CURP validator | `scripts/validate_curp.py` | Estructura + algoritmo RENAPO |
| 3. Lista 69-B checker | `scripts/check_69b.py` | Busca RFC en 6 listas SAT |
| 4. Aviso de Privacidad generator | `scripts/generate_aviso_privacidad.py` | Plantillas corto/simplificado/integral |
| 5. ISN por estado | `data/isn_por_estado.json` | Impuesto Sobre Nómina 1-3% por entidad |
| 6. Catálogo de fuentes | `data/catalogo_fuentes.json` | Index machine-readable de las 30 fuentes |

## Workflow

### Paso 1: Identifica intent

| Intent | Acción |
|---|---|
| "valida este RFC" / "este RFC sirve" | `validate_rfc.py <RFC>` |
| "este proveedor es facturera" / "está en lista negra" | `check_69b.py <RFC>` |
| "valida esta CURP" | `validate_curp.py <CURP>` |
| "necesito aviso de privacidad" | `generate_aviso_privacidad.py --tipo=corto\|simplificado\|integral --negocio=...` |
| "cuánto ISN pago en X estado" | leer `data/isn_por_estado.json` |
| "qué obligaciones tengo si abro PyME en X giro" | leer `legal-INDEX.md` + responder estructurado |

### Paso 2: Si el caso es exploratorio ("qué obligaciones tengo"), aplica el árbol de decisión

```
Pregunta al usuario:
1. ¿Persona física o moral?
2. ¿Giro? (e-commerce, servicios, retail, restaurant, salud, autos, joyería, inmuebles, fintech…)
3. ¿Tienes empleados? ¿Cuántos?
4. ¿Subcontratas o te subcontratan?
5. ¿En qué estado opera?

Con base en eso, responde con tabla:

| Obligación | ¿Aplica? | Fuente | Si la ignoras (riesgo) |
| Alta RFC + régimen | Sí siempre | CFF + RMF Anexo 2 | No facturar, multas |
| CFDI 4.0 correcto | Sí siempre | Anexo 20 + 29 | Rechazo timbrado, pérdida deducibilidad |
| Aviso de Privacidad | Sí siempre | LFPDPPP 2025 | Multa INAI/SABG |
| LFPC cumplimiento e-commerce | Sí si vende online | LFPC + Reglamento | Quejas PROFECO, sanción |
| Distintivo Digital PROFECO | Opcional pero valioso | PROFECO | Sin sello = menos confianza |
| Alta patronal IMSS | Sí si tiene empleados | LSS | Capitales constitutivos |
| Alta patronal INFONAVIT | Sí si tiene empleados | LIFNVT | Recargos |
| NOM-035 Guía II o III | Sí si tiene 16+ empleados | NOM-035 STPS | Sanción STPS, multas |
| REPSE | Sí si presta servicios especializados | Reforma LFT 2021 | Multa $4M MXN |
| LFPIORPI antilavado | Sí si actividad vulnerable | LFPIORPI | Multas altas + clausura |
| ISN del estado | Sí si tiene nómina | Código Fiscal estatal | Multa hacienda estatal |
| Registro marca IMPI | Opcional, MUY recomendado | LFPPI | Pérdida marca por ocupación |
```

### Paso 3: Si el caso es "valida X específico", usa el script correspondiente

Los scripts en `scripts/` están diseñados para invocarse desde la línea de comandos del usuario o desde el skill. Devuelven JSON estructurado.

### Paso 4: Cierra con accionable

Siempre cierra con:
1. **El veredicto numérico/binario** ("RFC válido y NO está en 69-B")
2. **El riesgo si lo ignora** (en MXN cuando aplique)
3. **La fuente exacta** (path al archivo en el corpus)
4. **Cuándo refrescar** (lista 69-B → semanal; leyes → mensual; RMF → trimestral)

## Los 3 errores más caros de PyMEs MX (priorización del skill)

Estos son los errores que más cuestan a una PyME en su primer año:

### 1. CFDI / RFC mal validado
- **Síntoma:** RFC inexistente o cancelado, CP fiscal incorrecto, régimen receptor mal, uso CFDI mal, XML inválido contra Anexo 20.
- **Costo:** Pérdida de deducibilidad, rechazos masivos de timbrado, cancelaciones y reemisiones, riesgo fiscal acumulado.
- **Cómo lo previene este skill:** módulos #1 y #3 (`validate_rfc.py` + `check_69b.py`).
- **Fuente:** `sat/rmf-2026/Anexo-29-RMF-2026.pdf`, `sat/cfdi-4/catCFDI.xsd`, listas 69-B.

### 2. Patrón sin alta correcta IMSS/INFONAVIT
- **Síntoma:** Alta tardía, salario base incorrecto, bajas omitidas, descuentos INFONAVIT mal enterados, simulación laboral (honorarios cuando hay subordinación).
- **Costo:** **Capitales constitutivos** (cobro retroactivo de cuotas + recargos + multas), problemas laborales. Puede tumbar una PyME.
- **Cómo lo previene este skill:** árbol de decisión paso 2 + alerta cuando giro implica empleados.
- **Fuente:** `diputados/leyes/LSS.pdf`, `diputados/leyes/LIFNVT.pdf`, `diputados/leyes/LFT.pdf`.

### 3. E-commerce sin reglas LFPC / LFPDPPP
- **Síntoma:** Sin aviso de privacidad correcto, sin términos claros, sin política cancelación/devolución/garantía, sin contrato de adhesión registrado en RCAL, suscripciones recurrentes sin botón claro de cancelación (reforma DOF 12-12-2025).
- **Costo:** Quejas PROFECO, mala defensa ante reclamaciones, riesgo sanciones por datos personales.
- **Cómo lo previene este skill:** módulo #4 (generador Aviso Privacidad) + checklist LFPC paso 2.
- **Fuente:** `diputados/leyes/LFPC.pdf`, `diputados/leyes/LFPDPPP.pdf`, `inai/ManualAvisoPrivacidad.pdf`.

## Lo que NO hace este skill

- **No es asesoría legal personalizada.** Es información de cumplimiento basada en corpus oficial. Para litigios, juicios, demandas laborales específicas, refiere a abogado/contador.
- **No predice si SAT/INAI/PROFECO va a sancionar.** Solo identifica obligaciones formales.
- **No reemplaza al PAC** para emisión real de CFDI. Solo valida estructura y catálogos.
- **No cubre obligaciones estatales / municipales completas** (licencias funcionamiento, uso suelo, protección civil, anuncios). Para eso refiere a CONAMER.
- **No cubre verticales especializadas:** COFEPRIS (salud/alimentos), CONDUSEF (fintech), IFT (telecom). Quedan para v1.1.

## Refresco del corpus

```bash
# Refresco completo (raro, solo cuando cambien leyes)
./scripts/download_corpus.sh

# Refresco solo listas SAT 69-B (recomendado semanal)
./scripts/download_corpus.sh --only=69b

# Refresco solo leyes Diputados (cuando se publique reforma)
./scripts/download_corpus.sh --only=diputados

# Solo reporta qué bajaría
./scripts/download_corpus.sh --report
```

Estado del último refresco: ver `data/last_refresh.txt`.

## Pendientes / verticales en v1.1

- COFEPRIS (alimentos, cosméticos, farma, suplementos)
- CONDUSEF (fintech, créditos, seguros)
- IFT (telecom, distribución SIMs)
- Marco normativo STPS completo (NOM-001 edificios, NOM-002 incendios, NOM-019 seguridad, NOM-025 iluminación, NOM-030 servicios preventivos)
- DOF API/RSS para detectar reformas
- Anexo 20 PDF y Guía REPSE (omawww.sat.gob.mx caído al 2026-05-29; descarga manual)
- Formato IMPI-00-001 para solicitud de marca

## Fuentes (corpus descargado)

Ver `research/legal-INDEX.md` para mapa temático completo. Resumen por institución:

- **SAT:** CFDI 4.0 XSDs, RMF 2026 + Anexos 1/2/29, 11 listas (69-B + 69 CFF). ~94 MB.
- **Diputados:** CFF, LFPDPPP (2025), LFPC (reforma 2025), LSS, LIFNVT, LFT, LFPPI, LFPIORPI, Reglamento LFPC. ~17 MB.
- **STPS:** NOM-035-STPS-2018 con Guías I-V. ~0.7 MB.
- **INAI:** Manual de Aviso de Privacidad con modelos integral/simplificado/corto. ~8 MB.
- **RENAPO:** Reglas oficiales para asignación CURP (algoritmo). ~0.5 MB.

Total: 30 archivos, ~119 MB.
