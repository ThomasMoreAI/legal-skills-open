---
name: telecom-isp-mx-lahh1986
title: telecom-isp-mx — Cumplimiento regulatorio para ISPs en México
description: 'Usar cuando alguien esté lanzando o operando un ISP (fibra, cable, inalámbrico)

  en México y necesite ayuda con REGULACIÓN TELECOM: Concesión Única bajo CRT,

  obligaciones LMTR 2025, compartición de infraestructura (postes Telnor/CFE),

  NOM-184 contratos de adhesión, NOM-208 homologación de equipo, retención de

  datos de tráfico, carta de derechos del usuario, calidad de servicio, neutralidad

  de red, registro de tarifas, reglamentos municipales La Paz BCS, leyes BCS.

  Anclado en corpus oficial descargado (CRT, ATDT, DOF, Diputados, CFE LAPEM,

  INEGI, Ayuntamiento La Paz, Congreso BCS) — 64 archivos, 96 MB.


  Triggers: "concesión única", "concesión telecom", "Tipo A comercial", "ISP México",

  "ATDT", "CRT", "comisión reguladora telecomunicaciones", "LMTR", "Ley Materia

  Telecomunicaciones", "compartición infraestructura", "oferta de referencia

  Telmex", "Telnor postes BCS", "adosamiento CFE", "NOM-184 contratos telecom",

  "NOM-208 homologación", "retención datos tráfico", "carta derechos usuarios",

  "calidad servicio fijo", "neutralidad red", "registro tarifas SERT", "SNII

  infraestructura", "interconexión", "fibra óptica La Paz", "reglamento imagen

  urbana La Paz", "postería La Paz", "obras vía pública BCS", "WISP México",

  "lanzar ISP", "Fibrium".'
author: lahh1986
author_url: https://github.com/lahh1986/sistemia-skills-mx/tree/main/skills/telecom-isp-mx
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: mx
practice: consumer
language: es
---

# telecom-isp-mx — Cumplimiento regulatorio para ISPs en México

> Wrapper sobre el corpus telecom oficial MX (~96 MB, 64 archivos) que vive en
> `~/sistemia-skills-mx/research/telecom/`.
> Para mapa temático del corpus: [`research/telecom-INDEX.md`](../../research/telecom-INDEX.md).
> Para bitácora de cómo se construyó (5 rondas LLM): [`telecom-LLM-ROUNDS-RAW.md`](../../research/telecom-LLM-ROUNDS-RAW.md).
> Caso de uso primario: **Fibrium** (ISP fibra óptica en La Paz, BCS).

## Cuándo activarte

- El usuario está lanzando un ISP en México y pregunta qué necesita para operar legalmente
- Quiere obtener Concesión Única ante CRT y pregunta requisitos/proceso/tarifa
- Quiere colgar fibra en postes ajenos (Telnor, CFE) y pregunta cómo
- Está armando contratos de servicio para clientes y pregunta qué NOM/lineamientos aplican
- Quiere saber cómo entrega obligatoriamente la Carta de Derechos al usuario
- Pregunta sobre retención de logs de tráfico, geolocalización, oficios de autoridad
- Tiene dudas sobre neutralidad de red, gestión de tráfico, calidad de servicio
- Quiere registrar tarifas o paquetes antes de comercializar (SERT)
- Tiene obra física en La Paz, BCS y necesita reglamentos municipales aplicables
- Quiere saber qué operadores activos hay en BCS (RPC) y cómo mapear competencia
- Está armando un Aviso de Privacidad bajo la nueva LFPDPPP (SABG, no INAI)

**NO actives si:**

- El usuario necesita litigio o representación legal en juicio telecom → refiere a abogado especializado.
- El usuario pregunta sobre **autorización de espectro radioeléctrico** específica (eso requiere proceso aparte de la Concesión Única, fuera del scope v1).
- El usuario opera un servicio de **radiodifusión** (TV/radio) — el corpus es ISP-céntrico aunque la LMTR cubre ambos.
- La pregunta es sobre regulación de telecom de **otro país**.

## 🔑 Marco regulatorio vigente 2026 (LEE ESTO PRIMERO)

La reforma constitucional de Simplificación Orgánica (DOF 20-dic-2024) y la nueva LMTR (DOF 16-jul-2025, vigor 17-jul-2025) cambiaron toda la arquitectura. **Si encuentras documentos que hablan de "IFT", "LFTR" o "INAI", probablemente sigan vigentes en lo sustantivo, pero la autoridad cambió:**

| Antes (pre-2025) | Ahora (2026) | Notas |
|---|---|---|
| IFT (autónomo) | **ATDT** (política) + **CRT** (técnica) | CRT bajo ATDT. CRT operativo desde 17-oct-2025. |
| COFECE | **CNA** (Comisión Nacional Antimonopolios) | Competencia económica. |
| INAI | **SABG** (Secretaría Anticorrupción y Buen Gobierno) | Privacidad/datos. Nueva LFPDPPP DOF 20-mar-2025. |
| LFTR 2014 | **LMTR 2025** | LFTR abrogada 17-oct-2025. |

**Sitios oficiales:** portal.crt.gob.mx · gob.mx/crt · gob.mx/atdt
**Dominio legacy ift.org.mx sigue vivo** ahora con marca "Comisión Reguladora de Telecomunicaciones" — aloja la mayoría de lineamientos heredados que siguen vigentes en transición.

## Workflow

### Paso 1: Identifica intent y rutea al doc del corpus

| Intent del usuario | Doc en corpus |
|---|---|
| "Quiero operar un ISP, ¿qué necesito legalmente?" | Concesión Única comercial: `telecom/ift/concesion_unica_comercial.pdf` + `triptico_concesion_unica_comercial.pdf` + reforma 2021: `lineamientos_concesion_unica_reforma_2021.pdf` |
| "Texto de la ley vigente" | `telecom/sct-leyes/LMTR.pdf` (894 KB, único texto vigente) |
| "Cómo cuelgo fibra en postes Telnor/Telmex" | Marco AEP: `telecom/ift/marco_ofertas_referencia_aep.html` + listado 2026: `oferta_referencia_aep_telmex_2026_dir.html` + Lineamientos compartición: `telecom/dof/lineamientos_despliegue_comparticion_2020.html` |
| "Cómo cuelgo fibra en postes CFE" | `telecom/cfe-postes/lineamientos_telecom_distribucion_cfe.pdf` + especificación: `E0000-35_cables_fibra_para_postes.pdf` + acuerdo CRE: `telecom/dof/cre_acuerdo_postes_cfe_2018.html` |
| "Mi contrato de adhesión con cliente, qué NOM aplica" | **NOM-184-SCFI-2018** (no la 208): `telecom/ift/NOM-184-SCFI-2018_normasoficiales.html` + texto DOF: `telecom/dof/NOM_184_dof_5552286.html` |
| "Mi router/CPE WiFi necesita homologación" | **NOM-208-SCFI-2016** (aquí sí): `telecom/dof/NOM_208_dof_5471010.html` |
| "Qué carta entrego al cliente" | `telecom/ift/carta_derechos_minimos_usuarios_2023.pdf` (entrega obligatoria) |
| "Cuánto tiempo retengo logs de tráfico" | Lineamientos Colaboración: `telecom/dof/modificacion_lineamientos_colaboracion_2025.html` (~24 meses metadatos). Obligación nace en la LMTR, no en LFPDPPP. |
| "Aviso de privacidad LFPDPPP" | `telecom/sct-leyes/LFPDPPP.pdf` (nueva, DOF 20-mar-2025) + Reglamento: `Reg_LFPDPPP.pdf`. **Autoridad: SABG (no INAI).** |
| "Calidad de servicio QoS legal" | `telecom/ift/lineamientos_calidad_servicio_fijo_2020.pdf` |
| "Neutralidad de red, gestión tráfico" | `telecom/dof/lineamientos_neutralidad_red_2021.html` |
| "Registro de tarifas antes de vender" | Procedimiento DOF: `telecom/ift/registro_tarifas_dof_5374179.html` + `registro_tarifas_dof_5507819.html`. Sistema online: sert.ift.org.mx/tarifasVE/ |
| "Reportar mi infraestructura (SNII)" | `telecom/atdt/SNII_entrega_inicial.pdf` + `SNII_actualizacion.pdf` + Lineamientos: `telecom/ift/lineamientos_snii_2024.pdf` |
| "Reglamento de construcción La Paz BCS" | Aplica el estatal (La Paz NO tiene propio): `telecom/bcs-estatal/reglamento_construcciones_bcs.pdf` |
| "Postería visible / centro histórico La Paz" | `telecom/lapaz-municipal/reglamento_imagen_urbana_2017.pdf` (Art. 52 = subterráneo obligatorio en centro peatonalizado) |
| "Uso de suelo / derecho de vía La Paz" | `telecom/lapaz-municipal/PDUCP_lapaz_2018.pdf` (7 MB) |
| "Manejo de tránsito durante obra" | `telecom/lapaz-municipal/reglamento_transito_lapaz_2022.pdf` |
| "Zona Malecón La Paz" | `telecom/lapaz-municipal/reglamento_malecon_lapaz.pdf` |
| "Constitución BCS, leyes estatales" | `telecom/bcs-estatal/constitucion_politica_bcs.pdf` |
| "Cobertura internet en BCS, competencia" | ENDUTIH 2024: `telecom/inegi-conectividad/ENDUTIH_2024_RR.pdf` (BCS=90.4%, 3º nacional). Operadores activos: ver tabla abajo. |
| "Plan nacional de conectividad 2026-2030" | `telecom/atdt/plan_nacional_conectividad_2026-2030.html` |
| "Tarifas trámites concesión" | `telecom/sct-leyes/LFD_ley_federal_derechos.pdf` |

### Paso 2: Top 5 errores que cierran un ISP nuevo en México

Cuando el usuario pregunte "qué evito al lanzar", responde con esto:

1. **Operar sin Concesión Única inscrita en RPC.** Causal de clausura inmediata. No empezar "en lo que sale el papel".
2. **Vender un paquete antes de registrar tarifa en SERT** (mínimo 15 días de antelación). PROFECO multa fuerte.
3. **No designar Responsable de Colaboración con la Justicia 24/7.** Si Fiscalía pide IP por delito y no respondes oficio formal → responsabilidad penal del operador.
4. **Contrato pirata sin folio NOM-184** registrado ante PROFECO = clausura comercial.
5. **Colgar fibra en postes Telnor o CFE sin convenio.** Retiro forzoso del cable + veto del convenio. Para Telnor usa la **Oferta de Referencia regulada** (Agente Económico Preponderante).

### Paso 3: Operadores activos La Paz BCS — competencia confirmada

| Operador | Tipo | Rol estratégico para ISP nuevo |
|---|---|---|
| **Megacable** | Cable + fibra | Dominante urbano. Principal competidor directo. |
| **Telnor** | Cobre + fibra | Filial noroeste Telmex. **AEP** — sus postes/ductos arrendables bajo Oferta de Referencia regulada. **Doble rol: competidor + proveedor de infra.** |
| **izzi** | Cable + fibra | Presencia urbana. |
| **Totalplay** | Fibra | Presencia urbana. |
| **Blue Telecomm** | Inalámbrico fijo | Opción económica. |
| **Starlink** | Satelital | **Competidor en rural** (donde está la oportunidad). |
| **INTELVID** | (verificar RPC) | Reportado en RPC con cobertura BCS. |

**Conclusión estratégica:** zona urbana La Paz/Los Cabos saturada. **Oportunidad real = colonias periféricas + rural BCS.**

### Paso 4: Trámites La Paz BCS frecuentemente olvidados

1. **Dictamen Protección Civil La Paz** para el NOC (tierras físicas, extintores específicos, plan contingencia — crítico por temporada de huracanes BCS).
2. **Permiso de excavación/canalización municipal** + fianza ante Obras Públicas. Sin permiso → clausura de cuadrilla.
3. **Zonas protegidas** (Centro Histórico, Malecón, Centro Comercial) = canalización subterránea obligatoria.
4. **OOMSAPAS La Paz** visto bueno si la canalización cruza agua/drenaje.
5. **Permisos de vialidades estatales** (Blvd. Forjadores) — competencia estatal, no municipal.
6. **Impacto ambiental** si zanjas cerca de manglares/Balandra.
7. **Impuesto sobre nóminas estatal BCS** — gasto recurrente que olvidan al planear.

## Cross-skill: cuándo delegar a otro skill MX

Este skill se enfoca en regulación telecom. Para preguntas adyacentes, delega:

| Pregunta del usuario | Delegar a | Por qué |
|---|---|---|
| "Quiero constituir Fibrium como SAPI / abrir RFC / alta patronal IMSS" | [`legal-pyme-mx`](../legal-pyme-mx/SKILL.md) | Cumplimiento federal de apertura de empresa. |
| "Validar RFC de Telnor/proveedor antes de firmar convenio" | [`legal-pyme-mx`](../legal-pyme-mx/SKILL.md) — `check_69b.py` | Lista 69-B SAT (facturera/EFOS). |
| "ISN exacto en BCS para los técnicos" | [`legal-pyme-mx`](../legal-pyme-mx/SKILL.md) — `data/isn_por_estado.json` | Impuesto Sobre Nómina estatal. |
| "Aviso de Privacidad para clientes Fibrium" | [`legal-pyme-mx`](../legal-pyme-mx/SKILL.md) — `generate_aviso_privacidad.py` | LFPDPPP 2025. Anota que la **autoridad ya es SABG, no INAI** (ese skill puede tenerlo desactualizado — verificar). |
| "CFDI 4.0 cuando factures a clientes Fibrium" | [`contador-pyme-mx`](../contador-pyme-mx/SKILL.md) | XSDs CFDI, RMF 2026, Anexo 20/29. |
| "Precio óptimo que aceptan en colonias periféricas La Paz" | [`precios-mx`](../precios-mx/SKILL.md) + [`nse-mx`](../nse-mx/SKILL.md) | Datos PROFECO (10.5M registros) + NSE AMAI. |
| "NSE de colonias específicas de La Paz" | [`nse-mx`](../nse-mx/SKILL.md) + [`mercado-local-mx`](../mercado-local-mx/SKILL.md) | AMAI 2024 + corte local. |
| "Validar copy/landing de Fibrium antes de gastar ads" | [`focus-group-mx`](../focus-group-mx/SKILL.md) | 14 personas MX hand-crafted. |
| "Penetración internet + hábitos por edad/NSE" | [`habitos-digitales-mx`](../habitos-digitales-mx/SKILL.md) + ENDUTIH | Complementa lo que tenemos en `telecom/inegi-conectividad/`. |

**Heurística:** este skill da la respuesta regulatoria. Si la pregunta sale del scope regulatorio (impuestos, marketing, contabilidad), nombra el skill correcto y rutea.

## Lo que NO hace este skill

- **No es asesoría legal específica.** Es información de cumplimiento basada en corpus oficial. Para amparos, litigios, defensa ante CRT/PROFECO → abogado.
- **No tramita** la Concesión Única ni convenios. Solo orienta sobre qué pedir y a quién.
- **No estima costos exactos** (LFD, derechos La Paz, cuotas Telnor) — esos cambian anualmente. Refiere a tarifarios vigentes en DOF / portal CRT.
- **No cubre radiodifusión** (TV/radio) aunque la LMTR los regula juntos.
- **No cubre regulación de espectro** para enlaces inalámbricos punto-a-punto (concesión adicional).
- **No reemplaza al SNII** — solo orienta sobre qué reportar.

## Pendientes / v1.1

- **Oferta de Referencia Telnor 2026 PDF específica** — descarga manual desde portal.crt.gob.mx/docs-bin/ofertas-de-referencia/2026/ (SPA browser-only)
- **Tarifa de interconexión 2026 acuerdo anual** — buscar en DOF dic-2025
- **Catálogo de operadores RPC BCS** filtrado — requiere consulta interactiva a rpc.ift.org.mx
- **BIT mapas cobertura por colonia La Paz** — sistema online bit.ift.org.mx
- **Lista de WISPs locales activos** (más allá de los 7 confirmados)
- **Calculadora de costos Concesión Única** basada en LFD vigente
- **Lineamientos secundarios de la CRT bajo LMTR** — se irán emitiendo durante 2026 (plazo de armonización ~julio 2026)

## Fuentes (corpus descargado)

Ver `research/telecom-INDEX.md` para mapa temático completo. Resumen por institución:

- **Diputados (sct-leyes/):** LMTR, LFTR abrogada, LFD, LFPDPPP+Reglamento, LOAPF. ~9 MB.
- **CRT/IFT legacy (ift/):** Concesión Única (folleto, tríptico, Lineamientos 2021), Calidad servicio fijo 2020, SNII Lineamientos 2024, Portabilidad 2023, Carta Derechos 2023, Diagnóstico Internet 2024, NOM-184 landing, criterio NOM, marco AEP Ofertas Referencia. ~30 MB.
- **DOF (dof/):** Reforma Constitucional 2024, decreto LMTR 2025, Reglamento Interior CRT 2025, Lineamientos Despliegue 2020, Neutralidad Red 2021, CRE postes 2018, RPC, Modificación Colaboración Justicia 2025, NOM-184 + NOM-208 detalle, Carta Derechos detalle. ~11 MB.
- **ATDT (atdt/):** SNII Entrega + Actualización, Reglamento Interior ATDT, Plan Nacional Conectividad 2026-2030, Programa Cobertura Social 2026, portal CRT (normatividad, herramientas, sesiones). ~12 MB.
- **CFE (cfe-postes/):** E0000-35, E1000-21, Lineamientos administrativos CFE (13 MB doc operativo crítico). ~15 MB.
- **BCS estatal (bcs-estatal/):** Reglamento Construcciones BCS, Constitución Política BCS. ~2 MB.
- **La Paz municipal (lapaz-municipal/):** Imagen Urbana 2017, PDUCP 2018, Tránsito 2022, Malecón. ~8 MB.
- **INEGI (inegi-conectividad/):** ENDUTIH 2024 Resultados Regionales. ~2 MB.

Total: 64 archivos, ~96 MB.
