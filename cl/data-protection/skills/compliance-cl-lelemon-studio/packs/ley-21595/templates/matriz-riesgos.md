# Matriz de Riesgos de Delitos — [RAZÓN SOCIAL]

**Fecha:** [FECHA] · **Versión:** 1.0 · **Responsable:** [ENCARGADO DE PREVENCIÓN]

> Identifica, por proceso, dónde puede ocurrir un delito de la Ley 21.595, su nivel de riesgo y
> el control que lo mitiga. Actualizar al menos anualmente.

| Proceso | Delito potencial | Probabilidad | Impacto | Nivel | Control mitigante | Control técnico (id) | Estado |
|---|---|---|---|---|---|---|---|
| Pagos a proveedores | Lavado / cohecho | [baja/media/alta] | [alto] | [medio] | Autorización por monto + doble firma | `ctrl-interno` | [ ] |
| Facturación / tributario | Delito tributario | | | | Facturación electrónica + respaldo | — | [ ] |
| Contratación con el Estado | Cohecho / fraude licitaciones | | | | Debida diligencia + registro | `ctrl-interno` | [ ] |
| Acceso a sistemas/datos de clientes | Delitos informáticos | | | | MFA + logs + segregación por tenant | `sec-mfa`,`sec-logs`,`sec-tenant` | [ ] |
| Gastos / reembolsos | Administración desleal / fraude | | | | Política de gastos + revisión | `ctrl-interno` | [ ] |
| Contrataciones / RRHH | Conflicto de interés | | | | Declaración de conflictos | — | [ ] |

## Notas
- Niveles: combinar probabilidad × impacto (bajo/medio/alto).
- Los controles técnicos enlazan con `references/controls.md` (se evalúan en la auditoría del repo).
- Para procesos sin control aún, ese es el plan de remediación.

---
*Borrador generado con compliance-cl (pack ley-21595). No constituye asesoría legal; revisar con un abogado.*
