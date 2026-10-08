---
name: boe-cli-zepelinmad
title: BOE CLI — Guía de M&A para Agentes IA
description: BOE CLI skill para M&A en España. Guía completa para que un agente AI consulte legislación española relevante para operaciones de fusiones y adquisiciones usando la API del BOE (Boletín Oficial del Estado).
author: zepelinmad
author_url: https://github.com/zepelinmad/boe-cli
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# BOE CLI — Guía de M&A para Agentes IA

## ¿Qué es el BOE CLI?

El BOE CLI (`./boe`) es una herramienta Go que consulta la API de datos abiertos del BOE español para obtener legislación consolidada vigente. Devuelve el texto actualizado de leyes, incluyendo todas sus modificaciones históricas anotadas.

**Ubicación del binario:** `/Users/santiagoquintana/clawd/projects/boe-cli/boe`

---

## Comandos Disponibles

```bash
# Buscar legislación
./boe search "query"                          # búsqueda general
./boe search "texto:palabra"                  # busca en el texto
./boe search "titulo:nombre ley"              # busca en el título

# Consultar una ley específica
./boe law BOE-A-XXXX-XXXXX                    # metadatos de la ley
./boe law BOE-A-XXXX-XXXXX --index            # índice/estructura de la ley
./boe law BOE-A-XXXX-XXXXX --block <id>       # artículo/bloque específico

# Ejemplos reales
./boe law BOE-A-2010-10544 --block a107       # LSC art. 107
./boe law BOE-A-2015-11430 --block a44        # ET art. 44
./boe law BOE-A-2014-12328 --block a21        # LIS art. 21
```

### Notas sobre búsquedas:
- Búsquedas multi-palabra se expanden automáticamente con AND
- Usa `titulo:` para afinar a leyes específicas (menos ruido)
- Los IDs de bloques suelen seguir el patrón `a<número>` (art. 107 → `a107`)
- Algunos artículos tienen IDs especiales: `a348bis`, `a15-2` (art. 15 bis)
- El CLI devuelve JSON; el texto del artículo está en el campo `text`

---

## Marco Legal M&A en España: Referencia Completa

### Leyes Core de M&A

| Ley | BOE ID | Descripción |
|-----|--------|-------------|
| **LSC** — Ley de Sociedades de Capital | `BOE-A-2010-10544` | Derecho corporativo; SL y SA; transmisión de participaciones, quórums, separación |
| **ET** — Estatuto de los Trabajadores | `BOE-A-2015-11430` | Sucesión de empresa, contratos laborales, convenios colectivos |
| **LME** — Modificaciones Estructurales | `BOE-A-2023-15135` | Fusiones, escisiones, transformaciones, cesiones globales (RDL 5/2023) |
| **LDC** — Ley de Defensa de la Competencia | `BOE-A-2007-12946` | Control de concentraciones, umbrales CNMC, notificación obligatoria |
| **CC** — Código Civil | `BOE-A-1889-4763` | Contratos, obligaciones, base del SPA, resolución, saneamiento |
| **CdeC** — Código de Comercio | `BOE-A-1885-6627` | Grupos de sociedades (art. 42), contabilidad, deberes mercantiles |

### Leyes Fiscales

| Ley | BOE ID | Descripción |
|-----|--------|-------------|
| **LIS** — Impuesto sobre Sociedades | `BOE-A-2014-12328` | Régimen fiscal neutral fusiones (art. 76-89), exención participaciones (art. 21) |
| **LIRPF** — IRPF | `BOE-A-2006-20764` | Ganancias patrimoniales para vendedores personas físicas (art. 33) |
| **LITPAJD** — ITP y AJD | `BOE-A-1993-25359` | Exención transmisión acciones, excepción inmobiliaria anti-fraude |
| **LGT** — Ley General Tributaria | `BOE-A-2003-23186` | Prescripción, responsabilidad tributaria, recargos |

### Leyes Regulatorias y Otras

| Ley | BOE ID | Descripción |
|-----|--------|-------------|
| **TRLC** — Ley Concursal | `BOE-A-2020-4859` | Insolvencia, acciones rescisorias, acuerdos de refinanciación |
| **LMV** — Ley Mercado de Valores | `BOE-A-2023-22765` | OPAs, exención ITP transmisión valores, información privilegiada |
| **LIVA** — IVA | `BOE-A-1992-28740` | Exención art. 20.18 en transmisión de valores; IVA en asset deals |
| **Blanqueo** — Ley 10/2010 | `BOE-A-2010-6737` | Obligaciones KYC para asesores, identificación del beneficiario real |
| **LOPDGDD** — Protección de Datos | `BOE-A-2018-16673` | Due diligence RGPD, transferencia de datos en M&A, DPO |
| **Inversiones Exteriores** | `BOE-A-1999-2725` | Screening de inversiones extranjeras (mecanismo de control desde 2020) |

---

## Artículos Clave por Área M&A

### 1. TRANSMISIÓN DE PARTICIPACIONES / SHARE DEAL

#### LSC — Régimen de transmisión

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 107 | `a107` | Régimen de transmisión voluntaria de participaciones SL inter vivos | **Crítico**: sistema de consentimiento de JG + derecho de adquisición preferente de socios; cualquier SPA de SL lo debe respetar o estatutos deben modificarlo |
| Art. 108 | `a108` | Cláusulas estatutarias prohibidas | Nulas cláusulas que hagan "prácticamente libre" la transmisión; lock-up máx. 5 años |
| Art. 123 | `a123` | Transmisión forzosa de participaciones | Régimen para ventas judiciales/embargos |
| Art. 124 | `a124` | Transmisión mortis causa | Sucesión; estatutos pueden establecer régimen especial |

**Flujo de una transmisión SL sin previsión estatutaria especial:**
1. Socio comunica a administradores: nº participaciones, identidad adquirente, precio y condiciones
2. JG (mayoría ordinaria) vota: consiente o deniega
3. Si deniega: debe identificar adquirente alternativo (socios preferentes)
4. Si no comunica adquirente en 3 meses → libre transmisión
5. Precio en operaciones a título oneroso distinto de compraventa: experto independiente

#### LSC — Competencias JG y quórums

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 160 | `a160` | Competencia de la JG | **Activos esenciales (>25% balance) requieren JG**; fusiones y escisiones también |
| Art. 199 | `a199` | Mayorías reforzadas SL | >50% para modificar estatutos; **≥2/3 para fusión, escisión, cesión global activo** |
| Art. 200 | `a200` | Mayorías SA en JEO | Consultar para SA targets |
| Art. 188 | `a188` | Derecho de voto | 1 participación = 1 voto en SL (salvo estatutos); SA no puede alterar proporcionalidad voto/nominal |

---

### 2. PROTECCIÓN DE SOCIOS Y DERECHOS DE SEPARACIÓN

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| LSC Art. 346 | `a346` | Causas legales de separación | Socios que no votaron a favor tienen derecho de separación por: sustitución objeto social, prórroga, reactivación, modificación régimen transmisión (SL) |
| LSC Art. 347 | `a347` | Causas estatutarias de separación | Pueden ampliar causas; verificar estatutos en due diligence |
| LSC Art. 348 bis | `a348bis` | Separación por falta de dividendos | Desde año 5: si JG no distribuye ≥25% beneficios → derecho de separación en 1 mes; **riesgo latente con socios minoritarios** |
| LSC Art. 352 | `a352` | Valoración de las participaciones | Auditor o experto independiente nombrado por Registro Mercantil |
| LSC Art. 363 | `a363` | Causas de disolución | Patrimonio neto <50% capital social; cese actividad >1 año; **red flag due diligence** |

---

### 3. DERECHO LABORAL — SUCESIÓN DE EMPRESA

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| ET Art. 44 | `a44` | Sucesión de empresa | **Solo aplica en asset deals**: nuevo titular se subroga en contratos; responsabilidad solidaria cedente-cesionario 3 años |
| ET Art. 42 | `a42` | Contrata y subcontrata | Responsabilidad en cadena; relevante si target externaliza servicios |
| ET Art. 51 | `a51` | ERE — Despidos colectivos | Procedimiento de consultas; relevante en restructuraciones post-cierre |

**DISTINCIÓN CRÍTICA:**
- **Share deal** (compra de participaciones): no hay cambio de empleador → art. 44 NO aplica. El comprador hereda todos los contratos, convenios y pasivos laborales tal cual estaban.
- **Asset deal** (compra de activos): art. 44 SÍ aplica si se transmite una unidad económica con su identidad.

---

### 4. MODIFICACIONES ESTRUCTURALES (FUSIONES, ESCISIONES)

Ley aplicable: **LME — RDL 5/2023 (BOE-A-2023-15135)**

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 4 | `a4` | Proyecto de modificación estructural | Documento mínimo obligatorio: forma jurídica, tipo operación, calendario, derechos socios, garantías acreedores, compensaciones |
| Art. 5 | `a5` | Informe del órgano de administración | Secciones separadas para socios y trabajadores; disponible ≥1 mes antes de la JG |
| Art. 6 | `a6` | Informe de experto independiente | Cuando corresponda; ratio de canje en fusiones |
| Art. 7 | `a7` | Protección de acreedores | Derecho a garantías adicionales |
| Art. 8 | `a8` | Aprobación por la JG | Quórum legal: ≥2/3 en SL (LSC art. 199) |

**Procedimiento fusión por absorción (SL):**
1. Proyecto de fusión (art. 4 LME)
2. Informe administradores (art. 5 LME)
3. Publicación/depósito proyecto (1 mes antes de JG)
4. Aprobación JG con ≥2/3 votos (LSC art. 199)
5. Escritura pública + inscripción Registro Mercantil
6. Efectos: transmisión universal del patrimonio

---

### 5. CONTROL DE CONCENTRACIONES

Ley aplicable: **LDC — Ley 15/2007 (BOE-A-2007-12946)**

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 7 | `a7` | Concepto de concentración económica | Qué operaciones son concentración |
| Art. 8 | `a8` | Umbrales de notificación obligatoria | **≥30% cuota mercado** O **>240M€ volumen combinado en España + dos partícipes >60M€ c/u** |
| Art. 9 | `a9` | Obligación de notificación y suspensión | Notificar a CNMC ANTES del cierre; suspensión de ejecución hasta autorización |
| Art. 57 | `a57` | Sanciones | Multas hasta 10% volumen negocios por incumplimiento |

**Fases de control CNMC:**
- **Fase I:** 1 mes (prorrogable 10 días hábiles) → autorización tácita o expresa
- **Fase II:** 3 meses adicionales (prorrogable 1 mes) → análisis en profundidad
- **Comisión Europea:** si supera umbrales del Reglamento 139/2004 (volumen mundial >5.000M€ + UE >250M€ c/u), jurisdicción exclusiva CE

**Condición precedente estándar en SPA:**
> "El cierre de la operación quedará condicionado a la obtención de la autorización o no oposición de la Comisión Nacional de los Mercados y la Competencia (CNMC) en relación con la concentración económica derivada de la presente operación."

---

### 6. FISCALIDAD M&A

#### LIS — Impuesto sobre Sociedades (BOE-A-2014-12328)

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 21 | `a21` | Exención dividendos y ganancias en transmisión de participaciones | Exención si ≥5% participación mantenida ≥1 año; reducción 5% por gastos gestión; no aplica a entidades patrimoniales |
| Art. 76 | `a76` | Definiciones: fusión, escisión, rama de actividad, canje de valores | Definiciones fiscales para acceder al régimen neutro |
| Art. 77 | `a77` | Régimen fiscal de la entidad adquirente | Subrogación en bienes y derechos; neutralidad en amortizaciones |
| Art. 80 | `a80` | Canje de valores | Sin tributación inmediata si cumple requisitos |
| Art. 89 | `a89` | Aplicación del régimen: comunicación AEAT | Aplicación automática (opt-out); comunicar tipo de operación; sanción 10.000€/operación por no comunicar |

**Clave: Motivo Económico Válido**
El art. 89.2 LIS requiere que la reestructuración tenga **motivo económico válido** (no solo ventaja fiscal). Si no → AEAT puede denegar la neutralidad fiscal. Ejemplos válidos: racionalización actividades, concentración de gestión, acceso a financiación.

#### IRPF — Vendedores Personas Físicas (BOE-A-2006-20764)

| Artículo | Bloque CLI | Qué cubre | Por qué importa en M&A |
|----------|-----------|-----------|------------------------|
| Art. 33 | `a33` | Concepto de ganancia/pérdida patrimonial | Base imponible del ahorro (19-30% según tramo) |
| Art. 37 | `a37` | Normas de valoración específicas | Valor de transmisión; valor de adquisición |
| Art. 49 | `a49` | Base imponible del ahorro | Tipos aplicables a plusvalías |

#### ITP y AJD — Transmisión de Valores (BOE-A-1993-25359)

**Regla general:** Transmisión de acciones/participaciones → **EXENTA** de ITP y de IVA

**Excepción anti-fraude** (art. 314 LMV nueva = art. 108 antigua LMV):
- **SÍ tributa por ITP** si: la sociedad tiene activos inmobiliarios que representen >50% de su activo Y el adquirente obtiene el control de la sociedad.
- Tipo: el que correspondería a la transmisión directa del inmueble (6-11% según CCAA)

**Due diligence fiscal M&A:** Siempre verificar si el target es una "sociedad patrimonial inmobiliaria".

---

### 7. DUE DILIGENCE — ÁREAS LEGALES CLAVE

#### Protección de Datos (LOPDGDD — BOE-A-2018-16673)
- Verificar: existencia de DPO si corresponde, registros de tratamiento, PIA para tratamientos de alto riesgo
- En M&A: la propia due diligence puede implicar transmisión de datos personales → necesita base legal
- Post-cierre: notificación a interesados de cambio de responsable/encargado del tratamiento
- Brechas de seguridad no notificadas: responsabilidad del target; riesgo hasta 4% volumen negocio mundial

#### Blanqueo de Capitales (Ley 10/2010 — BOE-A-2010-6737)
- Asesores en operaciones M&A: **sujetos obligados**
- KYC obligatorio del cliente y del beneficiario real
- Identificar UBO (Ultimate Beneficial Owner): cualquier persona física con control directo/indirecto ≥25%
- Comunicar operaciones sospechosas al SEPBLAC
- **Due diligence**: verificar historial KYC del target, posibles vínculos con paraísos fiscales, estructura de propiedad opaca

#### Inversiones Extranjeras
- Desde 2020 (RDL 8/2020): inversiones extranjeras en sectores estratégicos requieren autorización previa
- Sectores: infraestructura crítica, tecnología, defensa, medios de comunicación, seguridad alimentaria, etc.
- Umbral: inversiones >10% o control de sociedad española desde países no UE/OCDE
- Desde 2023 (RD 571/2023): también aplica a países UE/OCDE en sectores críticos si supera 500M€

---

## Workflows M&A Completos

### Workflow 1: Due Diligence Rápida — Share Deal SL

```
Paso 1: Verificar tipo de sociedad y régimen de transmisión
→ ./boe law BOE-A-2010-10544 --block a107  (régimen transmisión participaciones SL)
→ ./boe law BOE-A-2010-10544 --block a108  (cláusulas estatutarias prohibidas)

Paso 2: Verificar competencia JG y quórums
→ ./boe law BOE-A-2010-10544 --block a160  (activos esenciales; fusiones necesitan JG)
→ ./boe law BOE-A-2010-10544 --block a199  (mayorías reforzadas SL: 2/3 para grandes ops)

Paso 3: Verificar derechos de separación y riesgo de salida de socios
→ ./boe law BOE-A-2010-10544 --block a346  (causas legales separación)
→ ./boe law BOE-A-2010-10544 --block a348bis (separación por dividendos: riesgo año 5+)

Paso 4: Verificar causas de disolución (estado patrimonial)
→ ./boe law BOE-A-2010-10544 --block a363  (pérdidas >50% capital, inactividad)

Paso 5: Verificar ausencia de insolvencia
→ ./boe law BOE-A-2020-4859 --block a1     (concepto de insolvencia)
→ ./boe law BOE-A-2020-4859 --block a2     (quién puede solicitar concurso)
```

### Workflow 2: Análisis Laboral — Asset Deal

```
Paso 1: Confirmar si aplica sucesión de empresa
→ ./boe law BOE-A-2015-11430 --block a44  
  → ¿Hay transmisión de "entidad económica que mantiene su identidad"?
  → Si sí: nuevo empresario se subroga; responsabilidad solidaria cedente-cesionario 3 años

Paso 2: Revisar obligaciones de información
→ ./boe law BOE-A-2015-11430 --block a44  (ap. 6-8: comunicación a representantes trabajadores)

Paso 3: Verificar si hay medidas laborales previstas
→ ./boe law BOE-A-2015-11430 --block a44  (ap. 9: periodo de consultas si hay medidas laborales)

Paso 4: Revisar ERE/ERTE si hay despidos post-cierre
→ ./boe law BOE-A-2015-11430 --block a51  (ERE colectivos: procedimiento y umbrales)

Preguntas clave para el cliente:
- ¿Cuántos empleados tiene el target?
- ¿Qué convenio colectivo aplica?
- ¿Hay compromisos de pensiones?
- ¿Hay pasivos laborales pendientes (inspecciones, demandas)?
```

### Workflow 3: Tax Check — Venta de Participaciones

```
Paso 1: Vendedor es sociedad → verificar exención LIS
→ ./boe law BOE-A-2014-12328 --block a21
  → ¿≥5% de participación? ¿Mantenida ≥1 año? → Exención (menos 5% gastos gestión)
  → ¿Entidad patrimonial? ¿Paraíso fiscal? → Posible no exención

Paso 2: Vendedor es persona física → verificar IRPF
→ ./boe law BOE-A-2006-20764 --block a33  (ganancia patrimonial = precio - coste adquisición)
  → Tributación en base del ahorro: 19% hasta 6.000€ / 21% de 6.000-50.000€ / 
    23% 50.000-200.000€ / 27% 200.000-300.000€ / 30% >300.000€

Paso 3: Verificar excepción inmobiliaria (ITP)
→ Consultar activo del target: ¿inmuebles >50% del activo?
→ Si sí: puede aplicar ITP en la transmisión (art. 314 LMV)

Paso 4: Verificar si aplica régimen de neutralidad
→ Solo aplica en fusiones/escisiones, no en share deals puros
→ ./boe law BOE-A-2014-12328 --block a76  (definiciones: ¿es "canje de valores"?)
→ ./boe law BOE-A-2014-12328 --block a89  (comunicación AEAT; motivo económico válido)
```

### Workflow 4: Control de Concentraciones (CNMC/CE)

```
Paso 1: Calcular umbrales
→ ./boe law BOE-A-2007-12946 --block a8
  Umbral 1: ¿adquirente o combinación tiene ≥30% cuota mercado relevante en España?
            Excepción: si target tiene <10M€ volumen en España Y partícipes <50% cuota
  Umbral 2: ¿volumen combinado en España >240M€? + ¿al menos 2 partícipes >60M€ c/u?

→ Si supera umbral europeo (Reg. 139/2004): notificar a CE en vez de CNMC

Paso 2: Si hay umbral → verificar obligación de notificación
→ ./boe law BOE-A-2007-12946 --block a9
  → Notificar ANTES del cierre
  → Stand-still obligation: no ejecutar hasta autorización
  → Excepción OPA: notificar en 5 días desde solicitud a CNMV

Paso 3: Drafting de la condición precedente en el SPA
  → Condition precedent: autorización CNMC (o no oposición)
  → Long-stop date: incluir período razonable (mínimo 6 meses para Fase I + Fase II)
  → Material Adverse Change: definir si la autorización con remedios materiales es MAC

Paso 4: Sanciones por incumplimiento
→ ./boe law BOE-A-2007-12946 --block a57
  → Multas hasta 10% volumen negocios total de las partícipes
```

### Workflow 5: Fusión por Absorción

```
Paso 1: Verificar que la fusión requiere aprobación por JG
→ ./boe law BOE-A-2010-10544 --block a160  (letra g: fusión = competencia JG)
→ ./boe law BOE-A-2010-10544 --block a199  (letra b: ≥2/3 votos en SL)

Paso 2: Elaborar proyecto de fusión
→ ./boe law BOE-A-2023-15135 --block a4    (contenido mínimo del proyecto)

Paso 3: Elaborar informe de administradores
→ ./boe law BOE-A-2023-15135 --block a5    (sección socios + sección trabajadores)

Paso 4: Tax neutrality
→ ./boe law BOE-A-2014-12328 --block a76   (verificar que es "fusión" según LIS)
→ ./boe law BOE-A-2014-12328 --block a89   (comunicar a AEAT; motivo económico válido)

Paso 5: Protección laboral
→ ./boe law BOE-A-2015-11430 --block a44   (información a representantes de trabajadores)
  → En fusiones: antes de publicar convocatoria de JG (ap. 8)

Paso 6: Control competencia
→ ./boe law BOE-A-2007-12946 --block a8    (verificar umbrales)
→ ./boe law BOE-A-2007-12946 --block a9    (suspensión de ejecución si hay umbral)
```

### Workflow 6: Revisión de Pacto de Socios

```
Paso 1: Verificar límites para cláusulas de transmisión
→ ./boe law BOE-A-2010-10544 --block a108  (prohibiciones: ≤5 años lock-up; no hacer "prácticamente libre")

Paso 2: Tag along / drag along
→ Verificar artículos 107-108 LSC: mecanismos deben respetar el régimen legal supletorio
→ Las cláusulas drag-along se admiten si existe proporcionalidad en el precio y causa objetiva

Paso 3: Quórums reforzados en el pacto
→ ./boe law BOE-A-2010-10544 --block a199  (mínimos legales de quórum que no se pueden reducir en estatutos)

Paso 4: Anti-dilución
→ No hay regulación específica; se configura contractualmente
→ Verificar: ¿el pacto puede afectar al régimen legal de aumento de capital?
→ ./boe law BOE-A-2010-10544 --block a296  (derechos de suscripción preferente en ampliaciones)

Paso 5: Derecho de separación
→ ./boe law BOE-A-2010-10544 --block a346  (no modificable por debajo del mínimo legal)
→ ./boe law BOE-A-2010-10544 --block a348bis (no se puede eliminar; requiere consentimiento unánime)

Paso 6: Deadlock mechanisms
→ Sin regulación específica; mecanismos de desbloqueo (Russian Roulette, Texas Shootout) se configuran contractualmente
→ Verificar compatibilidad con quórums LSC
```

---

## Queries de Búsqueda para Investigación M&A

```bash
# Buscar jurisprudencia y doctrina
./boe search "titulo:sociedades capital transmision participaciones"
./boe search "titulo:modificaciones estructurales fusión"
./boe search "texto:concentraciones economicas notificacion"
./boe search "titulo:impuesto sociedades reestructuracion"
./boe search "texto:sucesion empresa trabajadores"
./boe search "titulo:defensa competencia concentraciones"
./boe search "texto:blanqueo capitales sujetos obligados"
./boe search "titulo:inversiones exteriores autorizacion"
./boe search "texto:valoracion participaciones experto independiente"
./boe search "texto:datos personales transmision empresa"
```

---

## Tips para Agentes AI

### 1. Siempre leer el artículo, no solo el índice
El BOE incluye todas las versiones históricas de un artículo con la fecha de vigencia. La **última versión** es la aplicable. Verifica la fecha `[Vigente desde: XX/XX/XXXX]` al final del resultado.

### 2. Bloques de índice con IDs especiales
```bash
# Artículo 15 bis → bloque a1-2 (puede variar)
# Artículo 30 bis → bloque a3-3
# Disposición adicional primera → bloque da
# Disposición transitoria única → bloque dt
./boe law BOE-A-XXXX-XXXXX --index  # siempre consultar índice primero si tienes dudas
```

### 3. Share deal vs. Asset deal: diferencias críticas

| Aspecto | Share Deal | Asset Deal |
|---------|-----------|------------|
| Sucesión laboral (ET art. 44) | NO aplica | SÍ aplica |
| Pasivos ocultos | Heredados por comprador | Solo los asumidos expresamente |
| ITP transmisión | Exento (regla general) | Depende del tipo de activo |
| IVA | No sujeto | Depende (exento si empresa en funcionamiento) |
| Step-up fiscal activos | NO (base histórica) | SÍ (precio pagado = nueva base) |
| Responsabilidad tributaria | Solidaria si hay deudas previas | Solo activos/pasivos asumidos |

### 4. Para due diligence: artículos de "red flag"

Artículos que debes verificar SIEMPRE en cualquier target español:

```bash
# Estado patrimonial crítico
./boe law BOE-A-2010-10544 --block a363  # ¿causas de disolución activas?

# Situación concursal
./boe law BOE-A-2020-4859 --block a1     # ¿hay insolvencia declarada o inminente?

# Pasivos laborales ocultos
./boe law BOE-A-2015-11430 --block a44   # sucesión si es asset deal

# Derechos de separación activos
./boe law BOE-A-2010-10544 --block a348bis # ¿acumulan años sin dividendos?

# Restricciones a la transmisión
./boe law BOE-A-2010-10544 --block a107   # ¿tiene consentimiento la JG?
```

### 5. Estructura jerárquica del índice
Los IDs del índice siguen esta lógica:
- `ti`, `tii`, `tiii` → Título I, II, III
- `ci`, `cii` → Capítulo I, II (dentro de un título)
- `s1`, `s2` → Sección 1, 2
- `a1`, `a2`, `a107` → Artículo 1, 2, 107
- `pr` → Preámbulo
- `da`, `da-2` → Disposiciones adicionales
- `dt` → Disposición transitoria
- `df` → Disposición final

### 6. El BOE CLI devuelve JSON
El output es JSON. Para parsear en shell:
```bash
./boe law BOE-A-2010-10544 --block a107 | python3 -c "
import json, sys
data = json.load(sys.stdin)
print(data['text'])
"
```

Para navegar el índice:
```bash
./boe law BOE-A-2010-10544 --index | python3 -c "
import json, sys
data = json.load(sys.stdin)
blocks = data['data'][0]['bloque']
for b in blocks:
    if b.get('titulo'):
        print(f\"{b['id']:20} {b['titulo']}\")
"
```

---

## Referencia Rápida: Artículos TOP para M&A

| Situación | Ley | Bloque | Pregunta que responde |
|-----------|-----|--------|----------------------|
| SPA básico SL | LSC | `a107` | ¿Qué proceso seguir para transmitir participaciones? |
| Quórum JG para fusión | LSC | `a199` | ¿Qué mayoría se necesita? (2/3) |
| Activos esenciales | LSC | `a160` | ¿Se necesita JG para vender activos? (>25% balance) |
| Derechos socios minoritarios | LSC | `a346`, `a348bis` | ¿Pueden separarse? ¿Cuándo? |
| Sucesión laboral | ET | `a44` | ¿Qué pasa con los empleados en asset deal? |
| Fusión por absorción | LME | `a4`, `a5` | ¿Qué documentos son obligatorios? |
| Control concentraciones | LDC | `a8`, `a9` | ¿Hay que notificar a CNMC? |
| Tax en venta corporativa | LIS | `a21` | ¿Está exenta la plusvalía? (≥5% + ≥1 año) |
| Tax neutralidad en fusión | LIS | `a76`, `a89` | ¿Cómo aplicar régimen neutro? |
| IRPF vendedor persona física | IRPF | `a33` | ¿Cómo tributa la ganancia? |
| Disolución forzosa | LSC | `a363` | ¿Tiene causas de disolución activas? |
| Insolvencia target | TRLC | `a1` | ¿Está en concurso o puede estarlo? |

---

## Cambios Recientes Relevantes (2023-2026)

1. **RDL 5/2023 (LME)** — Nueva regulación de modificaciones estructurales transpone directivas UE:
   - Nuevas obligaciones de información a trabajadores
   - Separación entre secciones del informe de administradores
   - Derecho de enajenación de socios en modificaciones estructurales

2. **Ley 6/2023 (nueva LMV)** — Refunde Ley del Mercado de Valores:
   - Art. 314: mantiene exención ITP en transmisión de valores + excepción inmobiliaria
   - Nuevo régimen de OPAs

3. **LIS art. 21 (desde 2021)** — Reducción del 5% de la exención en concepto de gastos de gestión:
   - Desde enero 2021: solo exento el 95% de dividendos/plusvalías (resto tributa)
   - Excepción: si el perceptor tiene INCN <40M€ y la filial fue creada tras 1/1/2021

4. **Screening inversiones extranjeras (2020-2023)**:
   - Desde marzo 2020: autorización previa para inversiones no UE en sectores estratégicos
   - Desde 2023: extiende a inversiones UE/OCDE en activos críticos >500M€

---

## Semantic Search — Notas Técnicas

### Index Enriquecido (v2, marzo 2026)

El índice semántico (`~/.boe/index-v2.bin`, 74MB) contiene embeddings enriquecidos de 12,228 leyes usando `text-embedding-3-small` de OpenAI (1536 dims).

**Enriquecimiento:** En lugar de embeber solo el título formal, las ~44 leyes más importantes tienen descripciones ricas con keywords, abreviaturas comunes y lenguaje coloquial. El resto se auto-enriquece con nombre corto + tipo de norma. Esto cierra el gap semántico entre títulos burocráticos y queries naturales.

**Rendimiento:**
- v1 (títulos crudos): 88% hit rate (22/25)
- v2 (enriched): 92-96% hit rate (23-24/25)
- Key improvements: "me han robado" → Código Penal (#1), "fusiones y adquisiciones" → LME (#1), "pacto de socios" → LSC (#1)

### Cómo funciona el enriquecimiento

1. **44 leyes clave** tienen descripciones manuales: LSC, CC, CP, ET, LGT, LAU, LME, etc. — con sinónimos, abreviaturas y lenguaje coloquial
2. **12,184 leyes restantes** se auto-enriquecen: extracción de nombre corto + tipo de norma (regex)
3. Se embebe el texto enriquecido pero el index almacena el título original (para display)

### Construcción del índice

```bash
# Requisitos: OPENAI_API_KEY en env
# Coste: ~$0.01 (menos de 1 céntimo)
# Tiempo: ~15 min (API rate limits)

# Desde index JSON existente (recomendado, más rápido):
python3 scripts/rebuild_from_existing.py

# Desde cero (descarga del BOE + embeddings):
python3 scripts/build_enriched_index.py
```

### Test de calidad

```bash
# Ejecutar benchmark de 25 queries
python3 scripts/test_semantic_np.py ~/.boe/index-v2.bin

# Comparar con index viejo
python3 scripts/test_semantic_np.py ~/.boe/index-v1.bin
```

### Mejoras implementadas vs pendientes

**✅ Implementado:**
- Document enrichment at index time (44 leyes manuales + auto-enrich)
- Benchmark test suite (25 queries diversas, natural language + legal terms)
- Binary index format compatible con Go CLI

**⏳ Pendiente:**
- HyDE (Hypothetical Document Embeddings) — generar query hipotética con LLM antes de buscar
- Query expansion — expandir queries con sinónimos legales antes de embeber
- Integración del index-v2 en el Go binary (actualmente lee v1)

### Limitaciones conocidas

- "prescripción de deudas" sigue sin matchear el Código Civil (el CC es demasiado genérico)
- Queries muy abstractas (ej: "quiero montar un negocio") tienen scores bajos
- El threshold actual (0.3) es muy permisivo; considerar subir a 0.35-0.40
- Para queries difíciles, el sistema de aliases + sinónimos del CLI es más fiable que semantic search

---

*Generado por Sabio 🔮 con investigación directa del BOE CLI + Exa search*
*Fuentes: Artículos leídos directamente del BOE API + ICLG Spain M&A 2025-2026, Baker McKenzie Private M&A Guide Spain, Borderless Lawyers Spain M&A Guide*
