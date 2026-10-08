# Chile 🇨🇱 — Property Due-Diligence Playbook

ISO2: `cl`. Status: ✅ Fully populated (researched 2026-04 / verified 2026-05-01).

## Country profile

- **Postcode (Código Postal)**: 7 digits (e.g., `7550000` Las Condes, `2340000` Valparaíso). Implemented by CorreosChile; not always required on listings.
- **Admin levels**: 16 regiones → 56 provincias → 346 comunas. The **comuna** is the administrative unit equivalent to municipality and is the level at which Contribuciones, plan regulador, DOM permits and avalúo are managed.
- **Currency**:
  - **CLP** (peso chileno) — daily transactions, salaries, retail
  - **UF** (Unidad de Fomento) — **most property prices, mortgages and notarial sums**. UF is a daily-indexed inflation unit set by Banco Central de Chile (BCCh) per `https://www.bcentral.cl/inicio/-/asset_publisher/8Ki7yegxnFpW/content/uf-1`. Convert at transaction date.
  - **USD** — sometimes used in commercial / luxury Santiago listings
- **Languages**: Spanish (official). English usable in Las Condes/Vitacura/Lo Barnechea finance and STR market; rare elsewhere.
- **Cadastre / registry**:
  - **Conservador de Bienes Raíces (CBR)** — territorial title registry (one per jurisdicción, ~70 nationally). Records Dominio (ownership), Hipotecas y Gravámenes (mortgages/encumbrances), Prohibiciones e Interdicciones. Title identifier: **Foja / Número / Año** in the relevant CBR.
  - **Servicio de Impuestos Internos (SII)** — fiscal property roll, maintains **avalúo fiscal** + **rol de avalúo** (comuna-rol-subrol). Portal: `https://www.sii.cl/servicios_online/1039-.html`.
- **Identifier**: **Rol SII** (comuna code + rol + subrol) for tax; **Foja/N°/Año CBR** for title.
- **Recent reforms**:
  - **Ley 21.210 (2020)** — introduced **sobretasa** on aggregate residential property > 670 UTA (originally 0.075–0.275 %; raised to **0.275–0.425 %** post-ajustes).
  - **Ley 21.442 (D.O. 13-Abr-2022; Reglamento DS N°7 MINVU D.O. 9-Ene-2025)** — new Copropiedad Inmobiliaria, replaced Ley 19.537.
  - **Ley 21.435 (2022)** + **Ley 21.727 (D.O. 18-Feb-2025, plazos DAA → 6-Abr-2027)** (Ley 21.604 (2023) no re-verificada — verify at bcn.cl) — Reforma del Código de Aguas; uso prioritario consumo humano; nuevos DAA con plazo.
  - **NCh 433 Of.96 mod. 2009 + DS 61/2011** — post-2010 Maule revision; reforzó estándar diseño sísmico.

---

## Section: `--price`

### Primary sources

- **SII Avalúo Fiscal & Rol** (FREE, official — fiscal value, NOT market):
  - `https://www.sii.cl/servicios_online/1039-1184.html` — consulta avalúo fiscal por rol
  - `https://www4.sii.cl/mapasui/internet/#!/buscarRol` — mapa rol
  - Returns: avalúo fiscal (CLP), avalúo terreno, avalúo construcción, exenciones, contribuciones semestrales.
  - **Trap**: avalúo fiscal is typically **40–70 % below market** ("comercial") and revalued every 4-6 yrs (last general reaviorization residential 2022; non-agricultural revaluation cycle per Ley 17.235 art. 3).
- **Conservador de Bienes Raíces** (territorial — fee per certificate, ~CLP 5,000-15,000):
  - Locator: `https://conservadores.cl/` (national directory of CBRs)
  - Santiago CBR online: `https://www.conservador.cl/portal/`
  - Documents to pull: Certificado de Dominio Vigente, Certificado de Hipotecas y Gravámenes, Copia de Inscripción de Dominio.
- **Banco Central de Chile (BCCh) Índice Real de Precios de Vivienda (IRPV)**:
  - `https://si3.bcentral.cl/Indicadoressiete/secure/IndicadoresDiarios.aspx` — UF, IRPV series
  - Quarterly index, base 2008 = 100. Tracks national + Gran Santiago real (UF-deflated) prices.
- **INE Índice de Precios de Vivienda (IPV)**:
  - `https://www.ine.gob.cl/estadisticas/economia/edificacion-y-vivienda/indice-de-precios-de-vivienda`
  - Quarterly nominal index, residential transactions registered in CBR, methodology 2014 base.
- **CChC (Cámara Chilena de la Construcción)**:
  - `https://cchc.cl/centro-de-informacion/indicadores` — informe MACh, índice de actividad de la construcción, trimestral oferta inmobiliaria Gran Santiago.
- **MINVU — Centro de Estudios, Ciudad y Territorio (CECT)** (formerly the Observatorio Habitacional):
  - `https://centrodeestudios.minvu.gob.cl` — déficit habitacional (cuantitativo y cualitativo), programas ministeriales, and a comunal data viewer covering demografía, instrumentos de planificación, vivienda, campamentos y subsidios.
- **INE — permisos de edificación**:
  - `https://www.ine.gob.cl/estadisticas-por-tema/industria-energia-y-construccion` — superficie autorizada de permisos de edificación, serie mensual (2026 data, source INE; 2026-09-18 verified).

### Listing platforms

- **Portal Inmobiliario** — largest, owned by Mercado Libre: `https://www.portalinmobiliario.com/`
  - URL pattern: `https://www.portalinmobiliario.com/venta/<tipo>/<comuna>-<region>/`
- **Toctoc.com** — strong Santiago analytics + valuation tool: `https://www.toctoc.com/`
- **Yapo.cl** (Adevinta) — privates: `https://www.yapo.cl/`
- **Mercado Libre Inmuebles**: `https://inmuebles.mercadolibre.cl/`
- **Mi Buen Vecino**: `https://www.mibuenvecino.cl/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — comuna-level evaluación.
- **Zoominmobiliario**: `https://www.zoominmobiliario.com/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row

### UF/m² benchmarks — Gran Santiago + key regions (Q1-Q2 2026 listing observation)

> **Caveat**: Listing UF/m² ≠ realized transaction price. Cross-check with toctoc valuation and CChC informe MACh for the trimestre. UF/m² presented as `est.` ranges based on listing platform observation and CChC MACh 2025 data; verify with current trimester data.

| Comuna / zona | Tipo dominante | UF/m² listing (est. range) |
|---|---|---:|
| Vitacura | depto + casa premium | ~80–150 |
| Las Condes | depto premium | ~70–130 |
| Lo Barnechea (incl. La Dehesa) | casa | ~60–120 |
| Providencia | depto | ~60–90 |
| Ñuñoa / La Reina | depto / casa | ~50–85 |
| Santiago Centro / Macul / Peñalolén | depto | ~40–70 |
| Maipú / Puente Alto periferia | depto inicial | ~35–55 |
| Viña del Mar / Concón | depto vista mar | ~40–100 |
| Concepción / La Serena / Coquimbo | depto | ~35–70 |
| Pucón / Villarrica / Puerto Varas | casa lago | ~30–90 |

Source: Portal Inmobiliario + Toctoc listing scrape pattern + CChC informe MACh 2025-Q4 reference range. Date-stamp: 2026-04 listing observation.

### Compute

1. **Listing UF total = listing CLP / UF del día (BCCh)** — always normalize to UF.
2. **UF/m² = UF total / m² útiles** (clarify "útiles" vs "totales con balcón/terraza"; Chile listings often report m² útiles + m² totales separately).
3. Compare to comuna median from Toctoc / Portal Inmobiliario filtros.
4. Cross-check **avalúo fiscal vs precio comercial gap**: typical 30–60 % gap; >70 % gap → consider whether the property has had a major modificación not registered con SII (riesgo de catastro).
5. Pull **CBR Certificado de Dominio Vigente** to confirm titular y libre de gravámenes before any oferta.

**Confidence**: HIGH for primary sources (BCCh UF, SII rol, INE IPV, MINVU) — all are active state sources. MEDIUM for UF/m² listing ranges (sample-based, not transactional median).

---

## Section: `--traffic`

### Primary sources

- **MOP — Dirección de Vialidad — Plan Nacional de Censos** (TMDA = Tránsito Medio Diario Anual):
  - Portal: `https://vialidad.mop.gob.cl/plan-nacional-de-censo-vial/`
  - **Plan Nacional de Censo Vial (PNCV)** — **biennial by half-country, not annual**: the **northern** regions (Arica y Parinacota → O'Higgins) are counted in **odd** years and the **southern** regions (Maule → Magallanes) in **even** years, with three seasonal samples each round (February/summer, June/winter, October/spring). As at 2026-09-18 the newest published rounds are **north 2025** and **south 2024** — **always name the round; a PNCV count is not a current-year TMDA** (2026 data, source MOP Dirección de Vialidad; 2026-09-18 verified).
  - Datos por tramo, with desglose vehículos livianos / buses / camiones.
- **MOP — Concesiones (autopistas urbanas y interurbanas)**:
  - `https://concesiones.mop.gob.cl/concesiones/concesiones-en-construccion/`
  - Operadoras con datos de tráfico: Autopista Central (Santiago N-S), Costanera Norte (E-W), Vespucio Norte / Sur, Acceso Sur, Túnel San Cristóbal, Ruta 5, Ruta 68 (Santiago-Valpo), Ruta del Sol.
- **SECTRA (Secretaría de Planificación de Transporte)**: `https://www.sectra.gob.cl/` — modelos de demanda urbana Santiago/Valpo/Concepción.
- **Fallback OSM**: `highway=motorway` (autopista concesionada), `trunk` (ruta nacional), `primary` (ruta regional), `secondary`, `residential`.

### Verdict bands (TMDA, vehicles/day per tramo)

- 🟢 < 1,000 v/d (rural, calle local)
- 🟡 1,000–5,000 v/d (calle barrio, pasaje)
- 🟠 5,000–20,000 v/d (avenida urbana, ruta secundaria)
- 🔴 > 20,000 v/d (autopista urbana, costanera, ruta nacional principal)

Reference: Autopista Central tramos urbanos Santiago > 100,000 v/d; Costanera Norte > 80,000 v/d (2023 operadora-reported, source: concesionarias annual reports).

---

## Section: `--tax`

### Annual property tax — Contribuciones de Bienes Raíces (Ley 17.235)

**Authority**: Servicio de Impuestos Internos (SII). Portal: `https://www.sii.cl/servicios_online/1039-.html`.

**Base imponible**: avalúo fiscal del inmueble (CLP) — generally well below comercial. Reaviorizaciones residenciales c/4-6 años; última general residencial 2022.

**Tasas (residencial habitacional, 2026)** — per SII tabla vigente:

| Tramo avalúo fiscal | Tasa anual |
|---|---:|
| Hasta UF 11,000 (no agrícola hab. exento) | **0 %** (exento de contribuciones) |
| Sobre UF 11,000 hasta UF 32,000 | aprox **0.933 %** sobre exceso (sujeto a tabla SII vigente) |
| Sobre UF 32,000 (residencial) | aprox **1.088 %** sobre exceso |

> Note: residential exemption threshold has been adjusted multiple times since 2018; the *exempt* portion applied to "habitación" is **UF 11,000-32,000** depending on tramo specific to the year (verify current at SII Tabla de Tasas for the year). For non-residential / no-habitacional and sitios eriazos, no exemption applies and tasa base differs.

**Pago**: 4 cuotas anuales (April, June, September, November) per SII calendario.

**Sobretasa Ley 21.210 — Impuesto Adicional sobre conjunto de bienes raíces**:

Aplica al titular cuya **suma de avalúos fiscales totales** supere **UTA 670** — **NOTE: tramos están en UTA (Unidades Tributarias Anuales = UTM × 12), NOT UF**. Cálculo SII automático; snapshot avalúos al **31 Dic del año anterior** al devengo.

| Tramo conjunto avalúo (UTA) | Tasa marginal anual |
|---|---:|
| Hasta 670 UTA | 0 % |
| 670–1,175 UTA | **0.075 %** |
| 1,175–1,510 UTA | **0.150 %** |
| > 1,510 UTA | **0.275 %** (o **0.425 %** en topes superiores) |

(2026-05-27 verified, source [SII Sobretasa](https://www.sii.cl/destacados/avaluaciones/sobretasa/2023/) + [Tesorería TGR](https://portal-ayuda.tgr.cl/ayuda/operativa-de-tramites/sobretasa-anual-de-impuesto-territorial). Prior playbook UF labels were a unit conflation — UTA and UF differ by ~12× scale.)

**Reform risk**: Ley 21.713 (cumplimiento tributario, **publicada 24 Oct 2024 en Diario Oficial**, vigencia general 1 Nov 2024 + ciertas disposiciones 2 Ene 2026 — parte del **Pacto Fiscal 2024-2025**, BCN `https://www.bcn.cl/leychile/navegar?idNorma=1207746`) and recent reforma tributaria proposals continue to revise sobretasa thresholds.

### Example — depto Las Condes 100 m² avalúo fiscal CLP 200,000,000 (≈ UF 5,200 a UF del día CLP 38,500)

- Avalúo UF 5,200 (asume <UF 32,000 tramo residencial)
- Tasa anual aprox 0.98 % efectiva sobre exceso UF 11,000... → **EXENTO** del impuesto principal porque avalúo <UF 11,000 in this case.
- Sobretasa: avalúo conjunto < 670 UTA ⇒ **0 sobretasa**
- **Contribuciones anuales: ~CLP 0** (dentro de exención hab.)

For a casa Lo Barnechea avalúo fiscal CLP 500,000,000 (≈ UF 13,000):
- Tasa sobre exceso UF (13,000 - 11,000) = UF 2,000 × 0.933 % ≈ UF 18.66 ≈ **CLP 700,000/año** (4 cuotas ≈ CLP 175,000 c/u)
- Sobretasa: convertir avalúo conjunto a **UTA** y comparar con el umbral **670 UTA** (la tabla de tramos está en UTA, NO UF — ver §contribuciones líneas 140-145); si el conjunto supera 670 UTA se aplica la tasa marginal del tramo (0.075 % en el primer tramo 670–1,175 UTA). No re-derivable a CLP aquí sin el valor UTA del año — verificar avalúo conjunto en UTA vía SII.

**Rebaja por adulto mayor / propietario único habitación principal** disponible (Ley 21.561 + DS); verificar requisitos en SII.

### Transaction taxes (one-time at purchase)

| Concepto | Tasa | Base | Pagado por |
|---|---|---|---|
| **IVA venta inmueble (vendedor habitual)** | **19 %** sobre precio | inmueble (nuevo o usado) vendido por **vendedor habitual** — Ley 20.780 + Circular SII Nº 42 de 5 Jun 2015; aplica desde 1 Ene 2016 a TODAS las ventas por habitual, no sólo new builds | comprador (incluido en precio escritura) — verificar IVA crédito fiscal constructora (2026-05-27 verified, source [Circular SII 42/2015](https://www.sii.cl/documentos/circulares/2015/circu42.pdf)) |
| **Notario** (escritura) | **1.2 % aplica IVA** sobre arancel notarial | escritura precio | comprador |
| **CBR Inscripción de Dominio** | escala **0.2–0.7 %** del precio (escala arancel CBR; tope nominal) | precio | comprador |
| **Impuesto al Mutuo / Timbre y Estampillas** | **0.8 %** del monto del crédito hipotecario | monto crédito | deudor (comprador) |
| **Estudio de Títulos** (abogado) | UF 30–80 negociable | — | comprador (si crédito, banco lo exige) |
| **Tasación banco** (si hipoteca) | UF 5–15 | — | comprador |
| **Comisión corretaje** | **2 % + IVA** cada parte (típico) | precio | cada parte |

**Total transacción comprador** (al contado, sin hipoteca): ~**1.5–2.5 %** del precio.
**Total transacción comprador** (con hipoteca): ~**3.5–5 %** del precio (timbre + tasación + estudio + comisión).

### Capital Gains Tax (CGT) — venta inmueble

Régimen Ley 21.210 (vigente desde 2020):

- **Personas naturales sin habitualidad**:
  - Primera vivienda con uso habitacional: **exenta hasta UF 8,000 de ganancia acumulada** (lifetime cap, no per-operación)
  - Sobre UF 8,000: opción **10 % impuesto único** o reliquidar como renta general (Global Complementario o Adicional 35 % no residente)
- **Habitualidad** (4+ inmuebles dentro 12 meses, o constructor): renta ordinaria.

### Inheritance / donation tax — Ley 16.271

Progresivo sobre asignación neta del heredero, según parentesco:

| Heredero | Tramo & tasa marginal |
|---|---|
| Cónyuge / hijos / padres | 1 % primer tramo → 25 % > UTM 1,200 (aprox) |
| Hermanos / sobrinos | recargo 20 % sobre tabla |
| Otros / no parentesco | recargo 40 % sobre tabla |

Exención básica ~600 UTM por heredero línea recta + cónyuge.

### Future reform risk

- Reforma tributaria **Ley 21.713 (parte del Pacto Fiscal 2024-2025, Min. Hacienda; publicada 24 Oct 2024, vigencia escalonada general 1 Nov 2024 + ciertas disposiciones 2 Ene 2026)** → más fiscalización avalúos. Próxima reaviorización residencial proyectada 2026-2028 (est. — fecha no confirmada oficialmente SII); expect avalúos al alza en zonas premium.
- Sobretasa thresholds historically tightened — monitor.

---

## Section: `--rental`

### Long-term residential — Ley 18.101 (Arrendamiento Predios Urbanos)

- **Sin plazo legal mínimo**, salvo arriendo amoblado < 1 año (modalidades especiales).
- **Garantía**: usualmente 1 mes (no hay tope legal explícito; mercado-establecido). **Ley 21.461 "Devuélveme mi Casa" (publicada 30 Jun 2022)** incorpora (i) **procedimiento monitorio** de cobro de rentas + restitución y (ii) **medida precautoria de restitución anticipada** — el arrendatario tiene 10 días corridos para oponerse; sin oposición fundada → restitución acelerada. Cubre también gastos comunes y servicios básicos. Fuente: [Ley 21.461 — BCN LeyChile](https://www.bcn.cl/leychile/Navegar?idNorma=1178004). Detalle adverse-possession + squatter en `shared/squatter.md` § CL (2026-05-27 verified).
- **Tributación renta arriendo (PN)**:
  - **DFL 2 vivienda económica ≤140 m²**: rentas EXENTAS de impuesto a la renta (hasta tope 2 viviendas DFL2 por persona desde Ley 20.455 / 2010).
  - Resto: renta presunta (si SII lo permite por encaje) o renta efectiva → Impuesto Global Complementario (escala 0–40 %) si residente; **Impuesto Adicional 35 %** retención si no residente sin convenio doble tributación.
  - Gastos efectivos rebajables si renta efectiva con contabilidad.
- **No hay IVA al arriendo de vivienda** sin amoblamiento; **arriendo amoblado IVA 19 %** desde Ley 21.420 (2022).

### Short-term rentals (STR / Airbnb / Booking)

**National-level**: no STR-specific national regulation as of 2026-07; STR sigue **legal, sin prohibición nacional**. **No existe ordenanza comunal STR-específica verificable** — el endurecimiento opera por dos vías: (a) **patente comercial de hospedaje** municipal + fiscalización de uso de suelo (zonificación), y (b) **reglamentos de copropiedad** que *limitan* (no prohíben totalmente) los arriendos cortos bajo **Ley 21.442 + su Reglamento — DS N°7 MINVU, [Diario Oficial 9-Ene-2025](https://www.minvu.gob.cl/nueva-ley-de-copropiedad-inmobiliaria)** (misma ficha Ley 21.442 más abajo — no duplicar). Las restricciones se dan **edificio-por-edificio** (bylaws) y **comuna-por-comuna** (zonificación), no vía ordenanza comuna-wide.

**Fiscalización / vías de restricción por comuna (2026 — vía patente + copropiedad + zonificación, no ordenanza STR-específica)**:
- **Las Condes** + **Providencia** — exigen **patente comercial de hospedaje**; operar sin patente arriesga multas de **hasta 5 UTM + clausura** del inmueble (confirmado vía fuentes secundarias — [Rentivo 2026](https://www.rentivo.app/recursos/regulacion-airbnb-chile) / [TheLatinvestor 2026](https://thelatinvestor.com/blogs/news/santiago-airbnb) — no vía texto de ordenanza municipal).
- **Santiago Centro** — sin restricción específica al 2026, alta presencia STR.
- **Vitacura** — endurecimiento STR-específico **no confirmado** en ninguna fuente (2026-07); tratar como no verificado, no como restricción vigente.
- **Viña del Mar / Pucón / Puerto Varas** — patente comercial/turística municipal + SERNATUR registro.

**Tributación STR**:
- Si habitualidad: **se considera servicio comercial → IVA 19 %** desde reforma Ley 21.420 (2022). Inicio actividades SII como servicio de alojamiento.
- Renta neta tributa Global Complementario / Adicional 35 % no residente.
- **Boleta electrónica obligatoria** por servicio.

**SERNATUR — Registro Nacional de Prestadores de Servicios Turísticos**:
- `https://serviciosturisticos.sernatur.cl/` — registro voluntario (mandatorio para algunas categorías) + clasificación calidad.

**Strategic notes**:
- Las Condes / Providencia: highest yield Santiago, **biggest 2026 STR-compliance risk** (patente hospedaje + reglamentos de copropiedad, no ordenanza comuna-wide).
- Pucón / Puerto Varas / Viña: strong seasonal yield (Dec-Mar peak) + sismic/volcanic disclosure obligation.
- DFL2 vivienda económica: strong tax shield for residential long-let.
- **Contra-precedente (uso residencial ≠ veto STR)**: la Corte Suprema validó el permiso DOM de **apart-hotel / hospedaje** como uso residencial permitido en **Lo Barnechea** bajo **OGUC art. 2.1.25** (el uso residencial incluye edificaciones de hospedaje sin servicios comerciales adjuntos) — una zona residencial no prohíbe automáticamente el STR (per legal-news — [DOE Actualidad Jurídica 2026](https://actualidadjuridica.doe.cl/corte-suprema-valida-modificacion-de-permiso-dom-para-apart-hotel-y-rechaza-reclamo-de-ilegalidad-municipal)).

**Confidence**: HIGH for national tax framework (Ley 18.101, IVA 21.420, DFL2). MEDIUM for comuna-level STR enforcement (patente hospedaje + reglamentos de copropiedad — no ordenanza STR-específica verificable; rapidly evolving). STR sub-section re-verified 2026-07-02.

---

## Section: `--work=<profession>`

### Job platforms

- **Trabajando.com**: `https://www.trabajando.com/` — main national portal.
- **Computrabajo Chile**: `https://www.computrabajo.cl/`
- **LinkedIn Chile** — strong Santiago corporate, finance, tech.
- **Laborum.cl** (Adevinta): `https://www.laborum.cl/`
- **Indeed Chile**: `https://cl.indeed.com/`
- **BNE — Bolsa Nacional de Empleo** (estatal SENCE): `https://www.bne.cl/`

### Self-employment regimes

- **Boleta de Honorarios electrónica** (independent profesional): retención provisional **2026: 14.5 %** (escalonamiento Ley 21.133 hasta 17 % en 2028); inicio actividades SII gratuita (segunda categoría); cotizaciones AFP + Salud + AFC + SIS obligatoriedad gradual hasta plena 2028.
- **Empresa en un Día** (`registrodeempresasysociedades.cl`) — constitución gratuita ~24-72h; tributación primera categoría.
- **Régimen General (semi-integrado)** — Primera Categoría **27 %** (Ley 21.210 art. 14 A) — tasa general, no 25 %.
- **Régimen Pyme Pro-Pyme General / Transparente** (Ley 21.210, ≤UF 75,000 ventas promedio últimos 3 años): tasa **25 %**; **transitoria 12.5 % para AT 2026-2028** (Ley 21.713, en vigor desde 2 Ene 2026, BCN `https://www.bcn.cl/leychile/navegar?idNorma=1207746`) + 50 % rebaja PPM desde Sept 2025 (2026-05-27 verified, source SII regímenes tributarios 2025).

### Salaried benchmarks (2025-2026)

- Sueldo medio mensual (CLP gross) estimado por INE ESI 2024 (`https://www.ine.gob.cl/estadisticas/sociales/ingresos-y-gastos/encuesta-suplementaria-de-ingresos`):
  - Mediana nacional: ~CLP 600,000–700,000
  - Santiago / Las Condes corporativo: ~CLP 1,500,000+
  - Profesional senior tech / fintech Santiago: CLP 3,000,000-6,000,000+
- **Sueldo Mínimo**: CLP **500,000** desde 2025-07 (Ley 21.578); revisión anual.

### Foreign worker visa pathways (SERMIG, Ley 21.325 / DS 296/2021)

Portal: `https://serviciomigraciones.cl/`.

- **Permanencia Transitoria** (90 días turismo, sin trabajo).
- **Visa Sujeta a Contrato** — empleador chileno con vínculo contractual.
- **Visa Temporal Profesional** — título universitario + oferta laboral.
- **Visa Temporal Inversionista** — proyecto inversión validado.
- **Permanente Definitiva** — tras 24 meses temporal sin lapsos.
- **Mercosur visa** — AR/BO/BR/PA/PE/UY/EC/CO/VE vía convenio.

---

## Section: `--risks`

### Primary national sources

| Riesgo | Fuente primaria | URL |
|---|---|---|
| **Sismicidad** (instrumental + histórica) | Centro Sismológico Nacional (CSN), Universidad de Chile | `https://www.sismologia.cl/` |
| **Sismicidad + tsunamis (oficial)** | SHOA (Servicio Hidrográfico y Oceanográfico Armada) | `https://www.shoa.cl/php/citsu.php` (Cartas de Inundación CITSU) |
| **Volcánico + remoción en masa + geología** | SERNAGEOMIN | `https://www.sernageomin.cl/` + RNVV ranking volcanes |
| **Hidrológico / sequía / DGA** | Dirección General de Aguas (MOP) | `https://dga.mop.gob.cl/` |
| **Inundación urbana / planes reguladores** | MINVU + DOM municipal | `https://www.minvu.gob.cl/` |
| **Emergencias multi-amenaza** | SENAPRED (ex-ONEMI desde Ley 21.364, 2021) | `https://www.senapred.gob.cl/` |
| **Mapa exposición incendios** | CONAF + SENAPRED | `https://www.conaf.cl/incendios-forestales/` |

### Sismicidad — riesgo dominante en Chile

Chile lies on the **subduction zone Nazca-Sudamericana** (Cinturón de Fuego del Pacífico). Históricos megatsuami / megaterremoto:
- **22 May 1960 Valdivia M 9.5** — récord mundial instrumental.
- **27 Feb 2010 Maule M 8.8** — disparó revisión NCh 433.
- **1 Apr 2014 Iquique M 8.2**.
- **16 Sep 2015 Illapel M 8.3**.

Norma sísmica chilena: **NCh 433 Of.96 mod. 2009** + **DS 61/2011 MINVU** (post-2010 revisión). Diferenciación crítica en build-era:

| Era construcción | Hazard sismic |
|---|---|
| **Pre-1972** | Sin norma sísmica formal robusta; alto riesgo, requiere evaluación estructural |
| **1972–1985** (NCh 433 original) | Norma básica; reforzar muros + columnas |
| **1985–2010** (NCh 433 Of.96) | Estándar moderno pre-Maule |
| **Post-2010** (NCh 433 mod. 2009 + DS 61) | Estándar reforzado post-Maule (diseño por capacidad, derivas más estrictas) |
| **Post-2015** (mod. recientes albañilería) | Estándares vigentes |

**Pregunta crítica al vendedor**: año de Recepción Final municipal (**Recepción Definitiva DOM**) y zonificación sísmica (Z) y suelo (S) del proyecto.

### Tsunami (CITSU SHOA)

- Toda la costa Pacífico chilena en exposición. **CITSU = Cartas de Inundación por Tsunami** (SHOA, oficial): `https://www.shoa.cl/php/citsu.php`.
- Ciudades con CITSU publicada: Arica, Iquique, Antofagasta, Coquimbo, Valparaíso, Viña del Mar, San Antonio, Talcahuano, Concepción, Puerto Montt, Castro, etc.
- **Cota de inundación** definida por SHOA; verificar si propiedad está bajo cota o sobre.
- Post-2010 + 2014: planes evacuación municipales obligatorios (PRN — Plan de Reducción de Riesgo de Desastres SENAPRED).

### Volcánico (RNVV SERNAGEOMIN)

- Chile tiene **~87–92 sistemas volcánicos geológicamente activos**, de los cuales **43 están bajo monitoreo instrumental 24/7** por la **Red Nacional de Vigilancia Volcánica (RNVV)** de SERNAGEOMIN, con niveles de alerta técnica verde / amarilla / naranja / roja. El **Ranking de Riesgo Específico de Volcanes Activos** se actualiza periódicamente y la edición vigente es la de **2023** — `https://www.sernageomin.cl/rnvv/` (2026 data, source SERNAGEOMIN RNVV, página editada 2026-09-03; 2026-09-18 verified).
- Top riesgo: **Villarrica** (Pucón), **Llaima** (Temuco/Conguillío), **Calbuco** (erupción 2015, Puerto Varas/Ensenada), **Nevados de Chillán**, **Lascar**, **Copahue**.
- Zonas turísticas Lagos (Pucón, Puerto Varas) **deben verificar mapa de peligro volcánico** antes de comprar.

### Aluvión / remoción en masa

- Andean valleys: **Santiago oriente** (Lo Barnechea, San José de Maipo), **norte chico** (Atacama 2015 aluvión Chañaral), **Andes secos** susceptibles.
- SERNAGEOMIN mapas de amenaza: `https://www.sernageomin.cl/geologia-general`.

### Sequía + Código de Aguas

- **Mega-sequía central-norte (desde 2010)**: déficit hídrico prolongado en Chile central (cuencas Maipo, Aconcagua, Limarí) — severidad actual no re-verificada 2026-09; verify decretos de escasez hídrica vigentes at DGA `https://dga.mop.gob.cl/`.
- **Reforma Código de Aguas** Ley 21.435 (publicada abr-2022 per DGA; Ley 21.604 (2023) no re-verificada 2026-09 — verify at bcn.cl/leychile): **uso prioritario consumo humano**; **derechos de aprovechamiento** ahora tienen plazo (no perpetuos para nuevos), caducidad por no uso, reasignación posible.
- **Para propiedades rurales / agrícolas**: verificar **derechos de aprovechamiento de aguas (DAA)** inscritos en CBR (separados del dominio del suelo) y registrados en el Catastro Público de Aguas DGA — plazo de inscripción/registro y de regularización hasta **6-Abr-2027** por **Ley 21.727 (D.O. 18-Feb-2025)** (2025 data, source DGA); DAA sin inscribir al vencimiento = riesgo de caducidad — `https://dga.mop.gob.cl/CPADGA/Paginas/CPA.aspx`.

### Mandatory diagnostics — documentos a exigir antes de oferta

| Documento | Emisor | Por qué |
|---|---|---|
| **Certificado de Dominio Vigente** | CBR jurisdicción | Confirma titular actual |
| **Certificado de Hipotecas, Gravámenes y Prohibiciones** | CBR | Detecta hipotecas, embargos, servidumbres, usufructos |
| **Certificado de Avalúo Fiscal** | SII | Avalúo + exenciones + situación contribuciones |
| **Certificado de Recepción Definitiva (Recepción Final)** | DOM municipal | Confirma obras construidas con permiso y recibidas |
| **Certificado de Informaciones Previas (CIP)** | DOM municipal | Zonificación, uso de suelo, restricciones (sísmica, inundación, patrimonio) |
| **Certificado de No Expropiación** | SERVIU + Municipalidad | Detecta proyectos viales / expropiación pendientes |
| **Certificado de Deuda de Contribuciones** | SII / Tesorería | Confirma sin deuda fiscal |
| **Reglamento de Copropiedad + Acta Asamblea** (si depto/condominio Ley 21.442) | Administración | Gastos comunes, fondo reserva, restricciones |
| **Patente comercial** (si se usa para STR/comercial) | Municipalidad | Verifica regularidad |
| **Certificado de Derechos de Aguas** (rural) | DGA + CBR | Verifica DAA existentes |

### Climate change (DGA + DMC + IPCC AR6 South America chapter)

- Chile central: **+1.5 to +3.0 °C** by 2050 (IPCC AR6 SSP2-4.5 to SSP5-8.5).
- **Mega-sequía proyectada extenderse**: déficit pluviométrico 20-40 % zona central by 2050 (DGA proyecciones + DMC).
- **Retroceso glaciar acelerado** (Andes central): impacto recursos hídricos verano.
- **Aumento intensidad incendios forestales** (RM, Valparaíso, Bío-Bío, Araucanía) — temporada cada vez más larga (Oct-Abr).

---

## Section: `--mains`

### Sanitary regulator

**SISS — Superintendencia de Servicios Sanitarios**: `https://www.siss.gob.cl/` — regulador de empresas sanitarias urbanas. Tarifas, calidad, cobertura.

### Major operators by region

| Operador | Región / cobertura |
|---|---|
| **Aguas Andinas** + subsidiaria **Aguas Cordillera** | RM Santiago + oriente (Las Condes, Vitacura, Lo Barnechea, La Reina) |
| **ESVAL** | Región Valparaíso (Valpo, Viña, Quilpué, Quillota) |
| **ESSBIO** | Bío-Bío + Maule + Ñuble (Concepción, Talca, Chillán) |
| **Aguas del Valle** / **Aguas Chañar** / **ADASA** / **Altiplano** | Coquimbo / Atacama / Antofagasta / Tarapacá+Arica |
| **Essal** / **Aguas Araucanía** / **Aguas Patagonia** / **Magallanes** | Los Lagos+Ríos / Araucanía / Aysén / Magallanes |

Cobertura urbana **>99 % agua potable, >97 % alcantarillado** zonas reguladas SISS (SISS Informe de Gestión 2023).

### Verification — listing language

- "**Agua potable y alcantarillado**" = mains agua + mains drains
- "**Pozo profundo / noria**" = pozo individual
- "**Fosa séptica**" = septic individual (no mains drains)
- "**Planta de tratamiento particular**" = WWTP individual
- **Rural** (parcelas, hijuelas): pozo + fosa séptica común; verificar permisos sanitarios DGA + Autoridad Sanitaria SEREMI.

### Costs

*est. ranges (CLP); verify with concesionaria presupuesto / driller quote — connection and perforation costs vary by year and operator.*

| Escenario | Costo (CLP) |
|---|---:|
| Conexión nueva agua (zona urbana, en frente concesionaria) | 300,000–800,000 |
| Conexión alcantarillado nuevo (zona urbana) | 500,000–1,500,000 |
| Construcción colector + arranque (rural fuera concesión) | 2,000,000–10,000,000+ |
| Pozo profundo (perforación 30-80 m) | 3,000,000–8,000,000 |
| Fosa séptica + drenaje (residencial) | 1,500,000–4,000,000 |
| Planta tratamiento aguas servidas particular | 5,000,000–15,000,000 |

---

## Cost benchmarks (CL 2026)

| Concepto | Costo |
|---|---:|
| Notario (escritura) | **1.2 % aplica IVA** |
| CBR inscripción dominio | **0.2–0.7 %** del precio (escala arancel) |
| Impuesto al Mutuo (timbre, si crédito) | **0.8 %** del crédito |
| Estudio de Títulos (abogado) | **UF 30–80** |
| Tasación (banco, si crédito) | **UF 5–15** |
| ITO (Inspector Técnico Obra, si construcción) | **UF 10–30** mensuales |
| Comisión corretaje (cada parte) | **2 % + IVA** |
| Contribuciones anuales residencial habitacional | **0 a UF 50+** según avalúo |
| Permiso edificación / Recepción Definitiva DOM | ~1.5 % / ~0.3 % costo construcción |
| **Total transacción comprador (al contado / con hipoteca)** | **~1.5–2.5 %** / **~3.5–5 %** del precio |

---

## Active fiscal incentives & programs (2025-2026)

- **DFL 2 vivienda económica** (≤140 m² superficie útil): exención total contribuciones primeros 5/10/15/20 años según m²; rentas de arriendo exentas (hasta 2 viviendas DFL2 por persona post-Ley 20.455).
- **Subsidio DS 01 (clase media)** — MINVU subsidio adquisición vivienda ≤ UF 2,200.
- **Subsidio DS 49 (sectores vulnerables)** — vivienda social.
- **Fondo Solidario Elección de Vivienda** — sin crédito hipotecario.
- **Programa de Subsidio al Arriendo (DS 52)** — apoyo al arrendatario.
- **Ley 21.701 / DS Eficiencia Energética** — calificación energética obligatoria nueva vivienda desde 2024 (CEV — Calificación Energética de Viviendas, MINVU + Minenergia).
- **Subsidio Sistemas Solares Térmicos (SST)** — Minenergia.
- **Ley REP 20.920** — Responsabilidad Extendida del Productor: reglamenta gestión residuos demolición (impacta proyectos remodelación/demolición).

---

## Common listing platforms

- **Portal Inmobiliario** — largest, includes mapa precios + filtros avanzados
- **Toctoc** — Santiago analytics + Toctoc Valor (estimación valor)
- **Yapo.cl** — privates Adevinta
- **Mercado Libre Inmuebles** — meta del mismo dueño (ML)
- **Mi Buen Vecino** — comuna ranking + listings
- **Zoominmobiliario** — corredores
- **Goplaceit** — premium

---

## Caveats unique to CL

- **UF pricing** — siempre convertir a UF a día transacción (BCCh `https://www.bcentral.cl/inicio/-/asset_publisher/8Ki7yegxnFpW/content/uf-1`); no comparar listings históricos sin reajustar UF.
- **Avalúo fiscal típicamente 30-60 % bajo comercial** — no usar avalúo como proxy de mercado.
- **NCh 433 watershed**: pre-1985 mucho más débil; post-2010 sustancialmente reforzado — exigir año Recepción Final.
- **Tsunami CITSU costa Pacífico** — verificar cota inundación SHOA en cualquier propiedad costera.
- **Mega-sequía + Reforma Código Aguas 2022 (Ley 21.435; plazos DAA hasta 6-Abr-2027 per Ley 21.727)** — DAA ahora con plazo, caducidad por no uso; rural sin DAA = limitación severa de uso.
- **Border-zone DL 1939/1977**: extranjeros nacionales de países limítrofes (PE, BO, AR) **no pueden adquirir** dominio en franja fronteriza (10 km de la línea) y zonas costeras según decretos por excepción presidencial. Verificar si el predio cae en franja vía DOM + Ministerio Defensa. Texto: `https://www.bcn.cl/leychile/navegar?idNorma=6778`.
- **Sobretasa conjunto > 670 UTA** — afecta a multipropietarios (residencial conjunto fiscal); actualizar tabla anual.
- **Ley 21.442 Copropiedad (D.O. 13-Abr-2022)** — nuevas reglas administración condominios; revisar reglamento copropiedad + acta asambleas + fondo reserva en compras de depto. Ley 21.842 (D.O. 23-Sep-2026) agrega Art. 43 bis: en unidades de vivienda sobre el primer piso donde residan niños de hasta 12 años o personas con necesidades especiales que presenten mayor riesgo de caída, el copropietario / arrendatario / ocupante debe instalar medidas de prevención de caídas, y el reglamento de copropiedad no puede prohibirlas (2026 data, source BCN LeyChile).
- **DFL 2** — escudo tributario potente ≤140 m² (exención contribuciones + rentas exentas).
- **Derechos de aguas separados del dominio del suelo** — siempre rastrear DAA en CBR + DGA en compras rurales.
- **Reaviorización SII residencial cada 4-6 años** — próxima ronda 2026-2028 puede subir contribuciones zonas premium.

---

## Reddit / forum sources

- **r/chile** — general nacional Spanish
- **r/santiago** — Santiago specific
- **r/Valparaiso**
- **r/Concepcion**
- **expat.cl** + **Internations Santiago** — expat communities
- Facebook: "Bienes Raíces Chile", "Vivir en Pucón / Puerto Varas / Viña"
- LinkedIn groups: CChC, Colegio Arquitectos Chile

---

## Verification authorities

| Autoridad | Cuándo llamar |
|---|---|
| **CBR jurisdicción** | Dominio vigente, hipotecas, gravámenes, copia inscripción |
| **SII** | Avalúo fiscal, rol, deuda contribuciones, sobretasa |
| **DOM municipal** | Recepción Final, CIP, permisos, zonificación, planes reguladores, no expropiación |
| **SERVIU regional** | Subsidios MINVU, expropiaciones viales |
| **SERNAGEOMIN** | Mapa peligro volcánico, remoción masa, sismicidad regional |
| **SHOA** | CITSU tsunami costera |
| **SENAPRED** (ex-ONEMI) | Planes emergencia, zonas riesgo multi-amenaza |
| **DGA (MOP)** | Derechos aprovechamiento aguas, sequía |
| **SISS** | Calidad y cobertura agua potable + alcantarillado |
| **MOP Vialidad** | TMDA carreteras, expropiaciones viales |
| **Servicio Nacional Migraciones (SERMIG)** | Visas residencia / trabajo |
| **BCCh** | UF, IPC, tasas referencia |
| **CMF (Comisión Mercado Financiero)** | Bancos, regulación hipotecaria |
| **CONAF** | Riesgo incendio forestal, terrenos forestales |
| **Bomberos comuna** | Hidrantes, accesibilidad |

---

## Quirks to know

- **UF** — unidad indexada inflación BCCh; propiedad cotizada en UF, valor diario.
- **Avalúo fiscal vs comercial gap** — 30-60 % típico; no usar como proxy.
- **Rol SII** ≠ **Foja/Número/Año CBR** — identificadores fiscales y registrales distintos; ambos requeridos.
- **Ley 21.442 (D.O. 13-Abr-2022) Copropiedad** — sustituye Ley 19.537; revisar reglamento + actas.
- **Sobretasa Ley 21.210** — adicional sobre conjunto > 670 UTA.
- **DFL 2 vivienda económica** — escudo tributario ≤140 m².
- **Border-zone DL 1939/1977** — restricción nacionales países limítrofes en franja fronteriza/costera.
- **Derechos de aguas (DAA) separados del suelo** — Reforma Código Aguas 2022 (Ley 21.435); inscripción CBR + registro DGA hasta 6-Abr-2027 (Ley 21.727).
- **Recepción Definitiva DOM** ≠ permiso edificación; sin Recepción Final, obras irregulares.
- **Red eléctrica**: 220V 50Hz, clavija tipo C/L.

---

## Source URL templates

| Source | URL pattern |
|---|---|
| CBR directorio nacional | `https://conservadores.cl/` |
| Conservador Bienes Raíces Santiago | `https://www.conservador.cl/portal/` |
| SII consulta avalúo fiscal | `https://www.sii.cl/servicios_online/1039-1184.html` |
| SII mapa rol | `https://www4.sii.cl/mapasui/internet/#!/buscarRol` |
| BCCh UF diaria | `https://www.bcentral.cl/inicio/-/asset_publisher/8Ki7yegxnFpW/content/uf-1` |
| BCCh series indicadores (IRPV) | `https://si3.bcentral.cl/Indicadoressiete/secure/IndicadoresDiarios.aspx` |
| INE IPV | `https://www.ine.gob.cl/estadisticas/economia/edificacion-y-vivienda/indice-de-precios-de-vivienda` |
| MINVU — Centro de Estudios, Ciudad y Territorio (CECT) | `https://centrodeestudios.minvu.gob.cl` |
| CChC indicadores | `https://cchc.cl/centro-de-informacion/indicadores` |
| SENAPRED | `https://www.senapred.gob.cl/` |
| SERNAGEOMIN | `https://www.sernageomin.cl/` |
| RNVV (volcanes) | `https://www.sernageomin.cl/rnvv/` |
| SHOA CITSU tsunami | `https://www.shoa.cl/php/citsu.php` |
| CSN sismología | `https://www.sismologia.cl/` |
| DGA aguas | `https://dga.mop.gob.cl/` |
| SISS sanitarias | `https://www.siss.gob.cl/` |
| MOP Vialidad censos TMDA | `https://vialidad.mop.gob.cl/plan-nacional-de-censo-vial/` |
| MOP Concesiones | `https://concesiones.mop.gob.cl/concesiones/concesiones-en-construccion/` |
| Servicio Nacional de Migraciones | `https://serviciomigraciones.cl/` |
| SERNATUR registro turísticos | `https://serviciosturisticos.sernatur.cl/` |
| Portal Inmobiliario | `https://www.portalinmobiliario.com/venta/<tipo>/<comuna>-<region>/` |
| Toctoc | `https://www.toctoc.com/` |
| Yapo | `https://www.yapo.cl/` |
| Mercado Libre Inmuebles | `https://inmuebles.mercadolibre.cl/` |
| Mi Buen Vecino | `https://www.mibuenvecino.cl/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row |
| Empresa en un Día | `https://www.registrodeempresasysociedades.cl/` |

---

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: **HIGH** for cadastre (CBR + SII), seismic standards (NCh 433 evolution), UF/BCCh system, Conservador process, DGA/SHOA/SERNAGEOMIN/SENAPRED hazard sources, and Ley 18.101 / Ley 21.442 / DFL 2 frameworks.
**MEDIUM** for: current 2026 sobretasa exact tramos (Ley 21.713 reform context — re-pull SII Circular each año), STR comuna-level enforcement (Las Condes / Providencia patente hospedaje + copropiedad bylaws in motion; Vitacura STR curbs unverified — no comuna-wide ordinance), boleta de honorarios retención escalonamiento (verify SII tabla annual).
**Last verified**: 2026-05-27 (price-source attribution, PNCV cadence and RNVV volcano counts corrected 2026-09-18 per MINVU CECT + INE + MOP Vialidad + SERNAGEOMIN). Ley 21.442 publication date (D.O. 13-Apr-2022, per MINVU Reglamento DS N°7) and Código de Aguas DAA deadline (Ley 21.727) re-verified 2026-09-24 in the October regwatch wave; copropiedad STR limb narrowed (no hospedaje provision in the Reglamento; municipal fines secondary-sourced only); drought severity not re-verified. Finance tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-comuna plan regulador URLs (top 50 metropolitanas)
- [ ] SII sobretasa exact 2026 tramos (re-pull Circular each año)
- [ ] Las Condes / Providencia / Vitacura STR ordinance final text
- [ ] Per-volcano RNVV peligro radius (top 15 active); CITSU cota per coastal city
- [ ] DAA caducidad proceso post-Ley 21.435 DGA scraping
- [ ] DFL2 calificación verification per DOM
