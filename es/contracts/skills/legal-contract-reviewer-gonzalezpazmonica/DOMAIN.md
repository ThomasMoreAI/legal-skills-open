# legal-contract-reviewer — Dominio

## Por qué existe esta skill

Los contratos en España presentan riesgos jurídicos específicos derivados del marco normativo local (ET, CCom, RGPD, LO 3/2018). Una revisión sistemática con matriz RAG permite a no juristas identificar exposición antes de involucrar asesoría externa, optimizando tiempo y coste.

## Tipos de contratos cubiertos

| Tipo | Marco normativo principal | Plazo revisión mínimo |
|---|---|---|
| NDA (acuerdo de confidencialidad) | CCom art. 57-63, Ley Secr. Emp. 1/2019 | Antes de firma |
| Contrato de servicios | CCom + CC | Antes de firma |
| Due diligence (compraventa empresa) | CCom, LSC, ET | Proceso estructurado |
| Contrato laboral | ET, Conv. Colectivo sectorial | Antes de alta SS |
| Contrato de distribución/agencia | Ley 12/1992 Agencia Comercial | Antes de inicio relación |

## Marco normativo relevante (España)

### RGPD y LO 3/2018 (LOPD-GDD)
- Base legitimadora de tratamiento (art. 6 RGPD)
- Cláusula DPA obligatoria en contratos con acceso a datos personales (art. 28 RGPD)
- Derechos ARCO+ (acceso, rectificación, supresión, oposición, portabilidad, limitación)
- Notificación de brechas: 72h a AEPD + sin dilación a afectados si riesgo alto

### Estatuto de los Trabajadores (ET)
- Art. 8: forma del contrato
- Art. 14: período de prueba (máx. 6 meses titulados, 2 meses resto; 3 meses PYMES <25)
- Art. 21: pacto de no competencia (máx. 2 años titulados, 6 meses resto; compensación obligatoria)
- Art. 49-56: extinción y despido
- Art. 82-92: convenios colectivos

### Código de Comercio (CCom)
- Art. 51-63: contratos mercantiles, forma y prueba
- Art. 241-243: sociedad colectiva y responsabilidad

## Cláusulas red flag por tipo de contrato

### NDAs — Red flags
- **Unilateral sin límite temporal**: nulidad potencial si supera estándares de mercado
- **Definición de confidencialidad ilimitada**: incluir excepciones de dominio público y conocimiento previo
- **Ausencia de jurisdicción pactada**: riesgo de forum shopping adverso
- **Penalización desproporcionada**: cláusulas penales > 10x valor contrato son cuestionables
- **Ausencia de destrucción/devolución**: obliga a retención indefinida

### Contratos de servicios — Red flags
- **SLA sin penalización**: compromisos de nivel de servicio sin consecuencias jurídicas = sin valor
- **Propiedad intelectual ambigua**: ausencia de cesión expresa en trabajos por encargo
- **Exclusiva unilateral no retribuida**: potencial competencia desleal
- **Limitación de responsabilidad por dolo o culpa grave**: nula conforme al CC art. 1102
- **Subcontratación sin límite**: permite externalización total sin control

### Contratos laborales — Red flags
- **Periodo de prueba > máximos legales**: nulo el exceso; subsiste el contrato
- **No competencia sin compensación económica**: nula la cláusula
- **Salario en especie > 30% total**: infracción art. 26 ET
- **Jornada sin límite horario**: vulnera art. 34 ET y Directiva 2003/88/CE

## Formato matriz de riesgos

```
| Cláusula | Riesgo identificado | Probabilidad | Impacto | Score | RAG | Recomendación |
|---|---|---|---|---|---|---|
| Texto cláusula | Descripción riesgo | A/M/B | A/M/B | 1-9 | 🔴/🟡/🟢 | Acción concreta |
```

**Criterios de puntuación:**
- Probabilidad × Impacto = Score (A=3, M=2, B=1)
- RAG: 🔴 Score 7-9 (acción inmediata), 🟡 Score 4-6 (negociar), 🟢 Score 1-3 (aceptable)

## Formato memorandum legal

```
MEMORANDUM DE REVISIÓN CONTRACTUAL
Contrato: [tipo] entre [parte A] y [parte B]
Fecha de revisión: [fecha]
Perfil de riesgo: [conservador/moderado/agresivo]

1. RESUMEN EJECUTIVO (3-5 párrafos)
2. HALLAZGOS MATERIALES
   - Red flags bloqueantes
   - Cláusulas a negociar
   - Observaciones menores
3. MATRIZ DE RIESGOS (tabla)
4. ENMIENDAS SUGERIDAS (redlines)
5. RECOMENDACIÓN: FIRMAR / NO FIRMAR / FIRMAR CON CONDICIONES
   Condiciones: [lista]

[DISCLAIMER LEGAL]
```
