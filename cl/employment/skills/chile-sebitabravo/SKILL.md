---
name: chile-sebitabravo
title: Chile — contexto legal, tributario y laboral
description: Marco legal, tributario y laboral chileno para decisiones de negocio. Cubre SII (IVA, F29, F22, Pro-Pyme, boletas de honorarios), Dirección del Trabajo (Ley 40 Horas, reforma de pensiones, finiquitos, Ley Karin), estructuras societarias (SpA, EIRL, SRL, S.A.), contratos bajo ley chilena, costo real de contratación y flujo de caja con IVA, y la transición Ley 19.628 a Ley 21.719. Usar cuando la tarea involucre impuestos chilenos, sueldos, cotizaciones, despidos, contratos, constitución de sociedad, costo de nómina, pricing con retención, o cifras en UF/UTM/CLP. Para generar documentación de cumplimiento (RAT, DPA, EIPD, política de privacidad, Modelo de Prevención de Delitos), usar `compliance-cl`.
author: sebitabravo
author_url: https://github.com/sebitabravo/dotfiles/tree/main/config/claude/skills/chile
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: employment
language: es
---

# Chile — contexto legal, tributario y laboral

Datos verificados a mayo 2026. **Las cifras cambian todos los años.** Antes de
entregar un número que el usuario vaya a usar para pagar, declarar o despedir,
confírmalo en la fuente oficial y di de dónde salió.

| Tema | Fuente oficial |
|---|---|
| Impuestos, facturación | <https://homer.sii.cl> |
| Leyes (texto vigente) | <https://www.leychile.cl> |
| Laboral | <https://www.dt.gob.cl> |
| Pensiones | <https://www.spensiones.cl> |
| Sociedades, mercado | <https://www.cmfchile.cl> |
| UF, TPM, tipo de cambio | <https://www.bcentral.cl> |
| IPC | <https://www.ine.gob.cl> |

## Tributario (SII)

### Tasas 2026

- **IVA**: 19%. F29 vence el día 12 de cada mes.
- **Primera Categoría, régimen general**: 27%. Crédito 65% para socios residentes.
- **Pro-Pyme (art. 14 D N°3)**: 12,5% transitorio (Ley 21.755), ingresos bajo ~USD 2,8M, PPM a la mitad. Escalonamiento: 2027 12,5% → 2028 15% → 2029+ converge a ~23%.
- **Global Complementario**: 0%–40% progresivo. Exento hasta ~CLP 11,2M anuales.
- **Retención boletas de honorarios**: 15,25% en 2026 (llega a 17% en 2028).
- **Impuesto Adicional**: 35% sobre pagos al exterior. Hay 35+ tratados de doble tributación.

### Obligaciones

- Inicio de actividades obligatorio desde el 2 de enero de 2026.
- Facturación electrónica obligatoria.
- F29 mensual (día 12), F22 anual (30 de abril).
- Certificado de cumplimiento tributario semestral (Circular N°38).
- DJ 1960-1964: transacciones financieras, activos digitales, leasing.

### Economía digital

- Retención de IVA a vendedores no residentes: 19% desde el 1 de junio de 2026.
- No hay umbral de venta a distancia: todo paga 19% de IVA.
- Plataformas digitales: verificación de cumplimiento cada 6 meses (Res. Ex. SII N°168).

### Transfronterizo

- Exportación de servicios: DIN 500. Exenta de IVA si califica (DL 825 art. 12 letra E).
- Precios de transferencia: documentación obligatoria con partes relacionadas en el exterior.

### Startups

- Ley I+D: crédito tributario. CORFO: subsidios no tributables.
- Patente municipal: 0,25%–0,5% del capital propio, anual.

**El SII cruza datos de forma automática.** Las inconsistencias entre F29, F22 y
factura electrónica gatillan fiscalización. Reconcilia siempre antes de declarar.

### Indicadores de referencia

UF ~CLP 38.500 · UTM ~CLP 67.000 · UTA ~CLP 834.504. Son valores de referencia a
mayo 2026: para cualquier cálculo real, busca el valor del día.

## Laboral (Dirección del Trabajo)

### Jornada — Ley 40 Horas (Ley 21.561)

- Máximo 2026: **42 horas semanales** desde el 26 de abril de 2026. Llega a 40 en 2028.
- Sin reducción de sueldo. Los pactos de 44 horas **no** son válidos para 42: hay que renegociarlos.
- Jornada de 30 a 42 horas: ingreso mínimo completo.
- Art. 22 inc. 2°: excluye a gerentes y administradores sin supervisión inmediata.

### Cotizaciones 2026

- **AFP**: 10,58% + comisión ~1,15% (rango 0,46%–1,45%).
- **Salud**: 7% (Fonasa o Isapre).
- **Reforma de pensiones (Ley 21.735)**: aporte del empleador 8,5% gradual en 9 años; **en 2026 es 3,5%** de la renta imponible. FAPP opera desde julio de 2026; primera licitación AFP en agosto de 2027.
- **Seguro de cesantía**: 3% (permanente).
- **Ley 16.744 (mutual)**: 0,95% + tasa adicional, obligatorio.
- **Ley Sanna**: 0,03%.
- Tope imponible: 87,8 UF. PGU: CLP 250.000.

### Término de contrato

- **Art. 160**: sin indemnización (causa grave y probada). **Art. 161**: necesidades de la empresa (con indemnización).
- Indemnización por años de servicio: 30 días por año, tope 330 días / 11 años. Tope 90 UF.
- Recargos: 30% si el art. 161 es injustificado; 50%–100% si es discriminatorio o viola fuero.
- Fuero: maternal, sindical, accidente o enfermedad laboral. Requiere autorización judicial.
- Finiquito: ante notario o Inspección del Trabajo, con ratificación.
- Tutela laboral (art. 485-495): indemnización de 6 a 11 meses.

### Otras obligaciones

- **Trabajo remoto (Ley 21.220)**: el empleador provee equipos, compensa costos, y respeta el derecho a desconexión (12 horas continuas). Se registra en la DT.
- **Ley Karin (Ley 21.643)**: protocolo obligatorio contra acoso laboral, acoso sexual y violencia en el trabajo, con protección frente a represalias.
- **Ley 20.609 (antidiscriminación)**: las descripciones de cargo no pueden sesgar por categoría protegida.
- Multas: 1–60 UTM. Trabajador extranjero irregular: hasta 20 UTM.
- Foco fiscalizador DT 2026: trazabilidad de jornada, registro de asistencia y cumplimiento de las 42 horas.

## Societario y contractual

### Estructuras

| Tipo | Cuándo | Notas |
|---|---|---|
| **SpA** | Recomendada para startups | Un accionista basta, flexible, sin directorio bajo 500 accionistas, capital desde $1 |
| **EIRL** | Dueño único | Menos flexible, capital debe estar pagado |
| **SRL** | 2 a 50 socios | Restricciones para ceder derechos |
| **S.A.** | Abierta (CMF) o cerrada | Directorio obligatorio |

### Contratos bajo ley chilena

- Jurisdicción: tribunales chilenos o arbitraje CAM Santiago.
- Perjuicios: Código Civil art. 1556-1558 (daño emergente + lucro cesante).
- Cláusula penal: debe ser explícita. La no competencia está limitada por la libertad de trabajo (Constitución art. 19 N°16).
- Bilingüe: prevalece el español salvo pacto expreso en contrario.
- Firma electrónica: simple en la mayoría de los casos, avanzada cuando se requiere equivalencia notarial.

### Otras regulaciones relevantes

- **Ley 19.496 (consumidor)**: garantía legal 6 meses, retracto de 10 días en e-commerce, SERNAC.
- **Ley 20.720 (insolvencia)**: reorganización y liquidación judicial.
- **Ley 20.393 (responsabilidad penal de la persona jurídica)**: exige programa de cumplimiento. Delitos base: lavado de activos, cohecho, tributarios, ambientales.

## Financiero

Decisiones de pricing, flujo de caja y costo de contratación con las reglas
chilenas de arriba. No reemplaza modelado financiero general (runway, CAC/LTV,
cap table): eso no depende del país y no es contenido de esta skill.

### Costo real de contratar

El sueldo bruto no es el costo empresa. AFP (10,58% + comisión) y salud (7%)
las descuenta el empleador del bruto pero las paga el trabajador — no suman al
costo empresa. Lo que sí aporta el empleador, encima del bruto:

- Reforma de pensiones (Ley 21.735): 3,5% en 2026, gradual a 8,5% en 9 años.
- Seguro de cesantía (Ley 19.728): contrato indefinido y contrato a plazo fijo
  tienen tasas de aporte patronal distintas — confírmalo en <https://www.afc.cl>
  antes de cotizar un costo de contratación.
- Ley 16.744 (mutual): 0,95% base + tasa adicional según riesgo del cargo.
- Ley Sanna: 0,03%.
- Gratificación legal si aplica: 25% de lo devengado, tope 4,75 ingresos
  mínimos mensuales al año.
- Tope imponible 87,8 UF: sobre ese monto las cotizaciones no siguen subiendo.

### Flujo de caja e IVA

- El débito fiscal (IVA de tus ventas) se declara y paga en el F29 del día 12,
  hayas cobrado la factura o no. Si tus clientes pagan a 30-60 días, ese
  desfase te descala caja.
- El crédito fiscal (IVA de tus compras) se resta en el mismo F29 — alinear
  fechas de facturación de proveedores (no de pago) con tu ciclo de cobro
  suaviza el desfase.
- Pro-Pyme (12,5% en 2026, PPM a la mitad) libera caja mensual frente al 27%
  general, pero el escalonamiento converge a ~23% en 2029: no lo trates como
  tasa fija de largo plazo al proyectar.

### Pricing con retención

Boletas de honorarios retienen 15,25% en 2026: quien emite recibe ~84,75% del
bruto. Si estás cotizando "en limpio" (el número que el proveedor necesita
recibir), grossea el bruto en vez de aplicar la retención sobre el neto.

### Límites

Esto no reemplaza un CFO ni un contador. Para pricing complejo (SaaS
multi-mercado, ronda de inversión, estructura de cap table), usa modelado
financiero general — fuera del alcance de esta skill.

## Datos personales — transición en curso

- **Hasta el 30 de noviembre de 2026**: rige la Ley 19.628. Consentimiento expreso, finalidad declarada, derechos ARCO.
- **Desde el 1 de diciembre de 2026**: rige la **Ley 21.719**. Crea la APDP. Multas de hasta 20.000 UTM o 2–4% de los ingresos anuales. Derechos nuevos: portabilidad y oposición a decisiones automatizadas. Exige registro de actividades de tratamiento, evaluación de impacto para datos sensibles, protocolo de brechas en 72 horas, encargado de protección de datos y transferencias internacionales adecuadas.

Para **producir** los artefactos de cumplimiento (RAT, DPA, EIPD, política de
privacidad, protocolo de brechas, Modelo de Prevención de Delitos), carga la
skill `compliance-cl`: trae los textos legales oficiales en `sources/`, así que
cita ley + artículo + archivo fuente en vez de apoyarte en el resumen de arriba.

## Límites

Esto es contexto para tomar decisiones informadas y preparar borradores, no
asesoría profesional. Deriva a un especialista humano —abogado laboral, abogado
corporativo o contador— antes de firmar un finiquito, cerrar un contrato o
presentar una declaración. Dilo en el entregable, no solo en el chat.
