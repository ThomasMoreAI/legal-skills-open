# Pack: Ley 19.574 — Prevención de Lavado de Activos y Financiamiento del Terrorismo (LA/FT)

> **Ya vigente.** Régimen = **Ley 19.574 (2017)** + **Decreto 379/018** (sector **no financiero**, supervisa
> **SENACLAFT**) / Recopilación de Normas del **BCU** (sector financiero). Numeración verificada en
> `references/mapa-articulos-19574.md`.

## ⚠️ Antes que nada: ¿la empresa es "sujeto obligado"?
**Este marco NO aplica a toda empresa**, solo a los **sujetos obligados** (Ley 19.574 arts. 12-13). Un SaaS
común **no suele serlo**. Encuadrá primero:
- **Art. 12 — financieros:** personas bajo control del **BCU** (intermediación financiera, cambio, valores,
  transferencia de fondos, seguros de vida/inversión, AFAP, etc.).
- **Art. 13 — no financieros:** casinos; inmobiliarias/constructoras; **abogados, escribanos y contadores**
  (solo en operaciones tasadas, no por mero asesoramiento); rematadores; arte/metales/piedras preciosas;
  zonas francas; **proveedores de servicios societarios y fiduciarios (lit. H)**; OSFL (lit. I);
  **prestadores de servicios de administración, contabilidad o procesamiento de datos (lit. N)**;
  sociedades anónimas deportivas; fiduciarios no financieros.

→ Si la empresa **no** encuadra en ningún literal, **este pack no le aplica** (decílo y no generes los
documentos). Si encuadra, seguí con los controles y documentos de abajo.

> **Contraste con Chile (importante):** Uruguay **NO** tiene responsabilidad penal de la persona jurídica
> (rige *societas delinquere non potest*). No existe un "modelo de prevención de delitos" que exima de pena a
> la empresa; lo que existe es un **programa de prevención de LA/FT** para sujetos obligados, cuyo
> incumplimiento acarrea **sanciones administrativas** (no penales) y eventual **decomiso**. La responsabilidad
> penal por lavado recae en las personas físicas (directores, gerentes).

## Controles que exige (ver `references/controls.md`)
`gov-responsable` (oficial de cumplimiento), `gov-registro` (matriz de riesgo), `gov-politicas` (política +
manual LA/FT), `gov-capacitacion`, `gov-auditoria`, `gov-disciplinario`, `aml-debida-diligencia`,
`aml-beneficiario-final`, `aml-pep`, `aml-monitoreo`, `aml-ros`, `aml-conservacion`, `ctrl-interno`.

## Componentes mínimos del programa (Decreto 379/018, sector no financiero)
1. **Evaluación de riesgo / matriz** (art. 4): riesgo de cliente, geográfico y operacional; clasificación
   **alto/medio/bajo por escrito**.
2. **Política de administración del riesgo** (art. 5) y **manual de procedimientos de DD** (art. 6).
3. **Oficial de cumplimiento** (art. 16): designación obligatoria; **puede recaer en la propia persona del
   sujeto obligado**; enlace con UIAF/SENACLAFT, con **independencia y acceso irrestricto** (art. 17).
4. **Debida diligencia** (Ley arts. 14-15; Decreto art. 11): identificar y verificar al cliente y al
   **beneficiario final (≥ 15%)**; propósito de la relación; **seguimiento continuo**. Prohibidas cuentas anónimas.
   - **Simplificada** (riesgo reducido), **normal**, **intensificada** (no residentes, sin presencia física,
     efectivo, **PEP** — funciones públicas en los últimos **5 años**).
5. **Reporte de Operaciones Sospechosas (ROS)** a la **UIAF del BCU** (Ley arts. 12-13). **Reserva**: prohibido
   alertar al involucrado (art. 22). Reportar de buena fe **no genera responsabilidad** (art. 23).
6. **Capacitación** periódica del personal (art. 18).
7. **Conservación de registros**: **mínimo 5 años** tras finalizar la relación (Ley art. 21; Decreto art. 15).

> **Auditoría independiente del programa:** exigida explícitamente para el sector **financiero** (normas BCU).
> Para no financieros, SENACLAFT la requiere por vía de resoluciones/guías → tratarla como buena práctica y
> `[verificar]` contra la resolución vigente.

## Sanciones (Art. 13 — verificado)
Apercibimiento · observación · **multa de 1.000 UI a 20.000.000 UI** · suspensión (temporal ≤ 3 meses;
definitiva con venia judicial). Las aplica **SENACLAFT** (no financieros) o el **BCU** (financieros). Puede
alcanzar a directivos y alta gerencia. Criterios de graduación: Resolución SENACLAFT 016/022 `[verificar vigente]`.

## Documentos a generar (templates/ → `<repo>/.compliance/docs/` con prefijo `19574-`)
`programa-prevencion-laft.md`, `matriz-riesgos.md`, `acta-oficial-cumplimiento.md`,
`procedimiento-debida-diligencia.md`, `procedimiento-ros.md`, `codigo-conducta.md`.

## Nota
La parte central es **organizacional** (designar el oficial, aplicar la DD, monitorear, reportar, capacitar,
conservar). La skill genera los documentos base; la implementación operativa y los reportes los ejecuta la empresa.
