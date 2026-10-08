# legal-compliance-checker — Dominio

## Por qué existe esta skill

Las obligaciones de compliance en España son heterogéneas y cambian con frecuencia. Esta skill centraliza los requerimientos de las normas más frecuentes (RGPD, LO 3/2018, ET) para auditar procesos y documentos con criterios uniformes y priorizados por el historial sancionador de la AEPD e Inspección de Trabajo.

## Obligaciones RGPD / LO 3/2018 (LOPD-GDD)

### Documentación obligatoria
| Documento | Obligatorio para | Consecuencia de ausencia |
|---|---|---|
| RAT (Registro Actividades Tratamiento) | Toda organización que trate datos | Infracción grave (hasta 10M€ o 2% facturación) |
| DPA (Data Processing Agreement) | Encargados de tratamiento (art. 28) | Infracción grave |
| DPIA (Evaluación Impacto) | Tratamientos alto riesgo (lista AEPD) | Infracción muy grave si es obligatorio y no realizado |
| Política de privacidad | Toda web/app que recoja datos | Infracción leve-grave según omisión |
| Cláusulas informativas (art. 13-14) | En cada recogida de datos | Infracción grave |

### DPO (Delegado de Protección de Datos)
- **Obligatorio** en: AA.PP., entidades que traten a gran escala datos sensibles (salud, religión, penal), entidades que traten a gran escala y monitoricen sistemáticamente personas
- **Recomendado** en: empresas >250 empleados con tratamientos complejos
- **Capacitación**: conocimiento jurídico + técnico demostrable

### Derechos ARCO+
| Derecho | Plazo respuesta | Gratuito | Excepción |
|---|---|---|---|
| Acceso | 1 mes (prorrogable 2) | Sí | Frecuencia excesiva |
| Rectificación | 1 mes | Sí | Inexactitud no demostrada |
| Supresión (olvido) | 1 mes | Sí | Interés legítimo/legal |
| Oposición | Inmediato (cese tratamiento) | Sí | Interés legítimo prevalente |
| Portabilidad | 1 mes | Sí | Solo si base = consentimiento o contrato |
| Limitación | Inmediato (congelar) | Sí | Impugnación exactitud |

### Notificación de brechas de seguridad
- **A AEPD**: en 72 horas desde conocimiento (si riesgo para derechos y libertades)
- **A afectados**: sin dilación indebida (si riesgo alto para sus derechos)
- **Contenido mínimo**: naturaleza brecha, categorías afectados, volumen, DPO contacto, consecuencias, medidas adoptadas
- **Excepción de notificación a afectados**: si datos cifrados con clave no comprometida

### Infracciones más sancionadas por AEPD (histórico)
1. Falta de legitimación del tratamiento (art. 6 RGPD) — recurrente en marketing
2. Ausencia de DPA con proveedores cloud (art. 28 RGPD)
3. Videovigilancia sin cartelería ni base legitimadora
4. Conservación de datos más allá del plazo (principio de limitación)
5. Transferencias internacionales sin garantías (Capítulo V RGPD)
6. Falta de medidas técnicas y organizativas (art. 32 RGPD)

## Estatuto de los Trabajadores (ET) — Artículos clave

| Artículo | Contenido | Riesgo de incumplimiento |
|---|---|---|
| Art. 8 | Forma del contrato (escrito para >4 sem) | Contrato indefinido por presunción |
| Art. 14 | Período de prueba (máximos legales) | Nulidad del exceso |
| Art. 15 | Contratos temporales (causas tasadas) | Conversión a indefinido |
| Art. 21 | Pacto de no competencia y dedicación | Nulidad si sin compensación |
| Art. 26 | Salario y complementos (especie ≤30%) | Infracción art. 7 LISOS |
| Art. 34 | Jornada máxima (40h sem ordinarias) | Sanción 626-6.250€ |
| Art. 49-56 | Extinción y despido (forma, causas, indemnización) | Improcedencia o nulidad |
| Art. 64 | Derechos de información del comité empresa | Nulidad de medidas sin consulta |

## Código de Comercio (CCom) — Elementos esenciales

- Art. 51: forma de los contratos mercantiles (libertad de forma, pero prueba documental)
- Art. 57: obligatoriedad del cumplimiento de los contratos
- Art. 62: plazo de prescripción (varía por tipo: 3 años servicios, 10 años documentos públicos)
- Art. 241-243: responsabilidad de administradores societarios

## Niveles de infracción RGPD

| Nivel | Tipo de infracción | Sanción máxima |
|---|---|---|
| Leve | Incumplimientos formales menores | Apercibimiento o hasta 10M€ / 2% |
| Grave | Falta base legitimadora, DPA ausente | Hasta 10M€ o 2% facturación global |
| Muy grave | Transferencias ilegales, vulneración derechos masiva | Hasta 20M€ o 4% facturación global |

*Las sanciones se determinan por el mayor de los dos importes.*
