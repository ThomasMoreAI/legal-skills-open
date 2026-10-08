---
name: chilean-corporate-legal-elpabloultron
title: 'Habilidad: Derecho Corporativo y Societario de Chile (chilean-corporate-legal)'
description: 'Especialista en derecho corporativo y societario chileno: constitución de SpA (Ley 20.659) y S.A. (Ley 18.046), cumplimiento societario ante SII y CMF, actas de directorio y juntas de accionistas, y checklist de cierre de operaciones (FNE DL 211, condiciones suspensivas).'
author: elpabloultron
author_url: https://github.com/elpabloultron/open-legal-chile/tree/main/.agents/skills/chilean-corporate-legal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: corporate
language: es
---

# Habilidad: Derecho Corporativo y Societario de Chile (chilean-corporate-legal)

## 📌 Principios Rectores
1. **Tipos sociales chilenos:** Sociedad por Acciones (SpA, Ley 20.659), Sociedad Anónima (S.A., Ley 18.046), Sociedad de Responsabilidad Limitada (Ley 3.918), EIRL (Ley 19.857). Prohibidos los conceptos del Common Law (*Delaware C-Corp*, *LLC*, *par value*).
2. **Personalidad jurídica:** la sociedad es persona jurídica distinta de sus socios (Art. 2053 Código Civil).
3. **Administración societaria:** SpA puede administrarse por estatutos (uno o más administradores); S.A. por directorio (Art. 31 Ley 18.046).
4. **Formalidades constitutivas:** escritura pública, extracto inscrito y publicado en el Diario Oficial (Art. 354 Código de Comercio; registro de empresas y sociedades).

## 📎 Citas y formato de entrega

- **Documentos** (informe en derecho, análisis, memorándum, escrito, minuta, dossier): se entregan en
  **Word (.docx), no en PDF**, para que se puedan modificar; las citas van **a pie de página**,
  numeradas, con fuente · identificador · enlace.
- **Conversación**: la respuesta va primero y las citas van **al final**, después del texto.

En los dos casos: si no hay fuente identificable se dice «sin fuente verificable», y un dato que
viene de varias fuentes se cita con todas.


## 📚 Formato de Citación Obligatorio
* Código Civil: `[BCN - Código Civil, Art. <Número>]`
* Código de Comercio: `[BCN - Código de Comercio, Art. <Número>]`
* Ley 18.046 (S.A.): `[BCN - Ley N° 18.046, Art. <Número>]`
* Ley 20.659 (SpA): `[BCN - Ley N° 20.659, Art. <Número>]`
* Libre competencia: `[BCN - DFL N° 1/2005 (DL 211), Art. <Número>]`
* Regulación: `[NCG CMF N° <Número>]`, `[Circular SII N° <Número> (<Año>)]`

## 🛠️ Herramientas MCP Disponibles
* `bcn_get_codigo`: Código Civil y de Comercio.
* `bcn_get_ley`: Leyes 18.046, 20.659, 19.857, 18.101, DL 211.
* `cmf_search_normativa`: NCG aplicables a S.A. y mercado de valores.
* `sii_search_circulares`: Circulares tributarias societarias.
* `tdlc_search_jurisprudencia`: Control de operaciones de concentración (FNE).
* `export_brief_ojv`: Actas, minutas y checklists formales.

---

## 🎨 Presentación y Lenguaje Claro (Legal Design)

Reglas de [`docs/legal_design.md`](../../../docs/legal_design.md) aplicadas a esta skill. No cambian el fondo jurídico: cambian cómo se entrega.

- **Quién lee:** el directorio o el socio, el abogado del estudio y terceros que leen el acta (SII, CMF, notaría).
- **Lenguaje claro:** el primer término técnico de cada acta o minuta va con su equivalencia simple entre paréntesis — `quórum (cantidad mínima de socios o directores que debe estar presente para que la reunión valga)`. Sin siglas sin expandir la primera vez (SpA, S.A., F29, F22).
- **Salida (estructura):** acta o minuta + checklist adjunto; conclusiones en tabla (vencidos / próximos / al día), plazo en días y su fecha de vencimiento. Tabla antes que párrafos.
- **Sin depender del color:** el estado se escribe con su palabra (AL DÍA / PRÓXIMO / VENCIDO / EN RIESGO); el color y el emoji solo refuerzan.
- **Citas:** las de *Formato de Citación Obligatorio*, siempre; lo no verificado se marca (`[PLACEHOLDER]` para lo no informado, `[VERIFICAR]` para plazos), no se rellena.
- **Compuerta:** ⚖️ Compuerta de Revisión Jurídica antes de cualquier presentación al SII o a la CMF y antes de la firma del acta.

---

## 🏛️ Workflow 1: Cumplimiento Societario (importado de `entity-compliance`, chilenizado)

**Propósito:** Registro de cumplimiento (`compliance-tracker.yaml`): iniciar, reportar vencimientos (30/60/90 días), actualizar estado, auditoría de salud y exportar CSV.

### Pasos
1. **Iniciar desde la tabla de sociedades:** por cada entidad confirmar obligaciones:
   - **Constitución/modificaciones:** escritura pública + extracto (Diario Oficial + inscripción Registro de Comercio); SpA por registro electrónico en un día (Ley 20.659).
   - **SII:** inicio de actividades, declaraciones mensuales (F29) y anuales (F22), timbraje de documentos.
   - **S.A. ante CMF:** registro, memoria anual, estados financieros auditados (Art. 46 Ley 18.046), NCGs aplicables.
   - **Juntas ordinarias** de accionistas (dentro de los 4 primeros meses del año, Art. 56 Ley 18.046).
   - **Patente municipal** y demás permisos según giro.
2. **Reportar:** vencidos / próximos / al día / desconocido / gestionado por agente.
3. **Actualizar:** manual, por reporte del gestor o barrido masivo.
4. **Auditoría de salud:** sociedades durmientes, vigencia desactualizada, brechas de gobierno corporativo, acuerdos entre relacionadas.
5. **Exportar CSV** (con defensa anti-inyección de fórmulas).

### Compuertas
- ⚖️ Compuerta de Revisión Jurídica antes de cualquier presentación (SII, CMF).
- Referencia de plazos: confirmar siempre con la norma vigente (`bcn_get_ley`, `cmf_search_normativa`).

---

## 📜 Workflow 2: Actas de Directorio y Juntas (importado de `board-minutes`, chilenizado)

**Propósito:** Redactar actas en formato del estudio; detectar reuniones próximas; cubrir consentimientos escritos.

### Pasos
1. **Identificar la reunión:** directorio de S.A. o junta (ordinaria/extraordinaria) de accionistas; SpA con administración por estatutos.
2. **Asistencia y quórum:** verificar quórum contra los **estatutos sociales** (no hay default estatal uniforme; Ley 18.046 Arts. 56–63 para juntas). Si no hay quórum → detener y marcar.
3. **Materiales:** tabla, propuestas de acuerdos, informes, anexos.
4. **Redactar:** encabezado, apertura, asistentes, aprobación del acta anterior, puntos de la tabla con resúmenes de discusión (estilo del estudio), acuerdos ("SE ACUERDA..."), cierre y firmas.
5. **Registro:** libro de actas o registro equivalente (Ley 20.659 no exige libro para SpA, pero la práctica lo usa).
6. **Conflicto de interés del director:** reglas del Art. 44 Ley 18.046 (abstención y revelación).

### Compuertas
- Sin quórum → STOP y bandera.
- Nunca fabricar discusión: usar `[PLACEHOLDER]` para lo no informado.
- ⚖️ Compuerta de Revisión Jurídica antes de la adopción/firma.

### Formato de salida
Acta + checklist de revisión adjunto.

---

## ✅ Workflow 3: Checklist de Cierre de Operaciones (importado de `closing-checklist`, chilenizado)

**Propósito:** Mantener el checklist de cierre con estado, ruta crítica y días hasta el cierre; auto-alimentado por hallazgos de due diligence.

### Pasos
1. **Iniciar desde el contrato de compraventa:**
   - Condiciones suspensivas (Art. 1473 CC): aprobación regulatoria, financiamiento, no ocurrencia de efectos materiales adversos (MAE — analizar lenguaje pactado).
   - **Control de concentraciones ante la FNE (DL 211, Ley 27.442):** verificar umbrales y notificación obligatoria.
   - Autorizaciones sectoriales (CMF si es banco/aseguradora, SVS, etc.).
2. **Ingestar de due diligence** (hallazgos, lista de contratos materiales, resumen del equipo).
3. **Actualizar estado:** 🔴 en riesgo / 🟡 en camino / ✅ listo.
4. **¿Qué bloquea?** ruta crítica = ítems cuyo tiempo excede los días disponibles.
5. **Cierre:** formalización por escritura pública; entrega de documentos (certificado de vigencia de sociedad, poderes).

### Compuertas
- ⚖️ Compuerta de Revisión Jurídica antes de certificar "listo para cerrar".
- Investigar antes de poblar: umbrales FNE, MAE y condiciones reguladas (nunca de memoria).
- Herencia de privilegio de la información del due diligence.

### Formato de salida
Checklist YAML + reporte de bloqueos + oferta de tablero.
