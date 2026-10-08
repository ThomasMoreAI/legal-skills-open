# Instructivo: qué hacer ante cada situación (runbooks)

Manual operativo para consultar cuando pase algo. La skill lo incluye en el output
(`<repo>/.compliance/INSTRUCTIVO.md`). El founder ejecuta esto **solo**; el abogado solo entra en la
representación de una fiscalización (caso reactivo).

---

## A. Llega un derecho del titular (acceso, rectificación, supresión, oposición, portabilidad, bloqueo)
**Plazo: 30 días corridos, prorrogable una sola vez por 30 días más** (avisando al titular).
**Gratuidad:** rectificación, supresión y oposición siempre gratis; acceso gratis al menos una vez por
trimestre (se puede cobrar si pide acceso/portabilidad más de una vez en el trimestre).
1. Registra la solicitud (fecha, quién, qué pide) y verifica identidad.
2. Ubica sus datos (BD, backups, proveedores).
3. Ejecuta: **acceso/portabilidad** → exporta en formato estructurado (JSON/CSV);
   **supresión** → borra o anonimiza (no solo soft-delete); **rectificación/oposición/bloqueo** → aplica.
4. Responde por escrito y **guarda evidencia**.

## B. Brecha de seguridad (acceso no autorizado, fuga, pérdida, alteración)
**Plazo: notificar a la Agencia sin dilaciones indebidas** (Art. 14 sexies; la ley NO fija 72h).
1. **Contén:** aísla, revoca accesos, rota credenciales. Abre bitácora.
2. **Evalúa:** qué datos, cuántos titulares, nivel de riesgo. Si fue un proveedor, exígele la info.
3. **Notifica:** a la **Agencia** (naturaleza, datos, volumen, consecuencias, medidas); a los **titulares**
   si hay riesgo alto o si afecta datos **sensibles, económicos/financieros/bancarios o de niños/niñas**.
   Si eres encargado, avisa también al **cliente responsable**.
4. **Registra** la vulneración en `registro-vulneraciones.md` aunque no la notifiques.
5. **Cierra:** causa raíz + fix + actualiza RAT y este plan. No notificar deliberadamente = gravísima.

## C. Te fiscaliza la Agencia de Protección de Datos
Este es el único caso donde conviene un **[ABOGADO]** (la representación es reservada por ley).
1. Designa un contacto único. Todo por escrito.
2. **Identifica la etapa:** ¿solicitud de información (preliminar) o **pliego de cargos** (formal)?
3. **Reúne los antecedentes:** RAT, evidencia de consentimiento, medidas de seguridad, registro de
   vulneraciones, DPA, EIPD → ya están en `<repo>/.compliance/`.
4. **Responde en plazo, cargo por cargo**, mostrando debida diligencia y remediación.
5. **Atenuantes:** MIPYME tiene gracia el primer año; el MPD/MPI y la corrección rápida ayudan.
6. **Nunca:** ocultar o destruir documentos, ni ignorar plazos.

## D. Cambia la ley o sale un reglamento (ej. DS 662)
1. Actualiza el corpus en `sources/` (re-descarga, ver `sources/FUENTES.md`).
2. Ajusta el pack afectado y los controles.
3. Re-corre `/compliance-cl` → el `state.json` muestra qué cambió.

## E. Calendario de revisión
| Cuándo | Qué | Quién |
|---|---|---|
| Anual (o ante cambios) | Revisar y actualizar el **RAT** | Responsable de datos |
| Anual | **Supervisión externa del MPD** (21.595, obligatoria) | consultor/tercero independiente |
| Anual | Capacitación del equipo | Responsable |
| Al firmar/renovar proveedor | DPA + anexo de transferencia (cláusulas modelo) | Responsable |
| Cada release relevante | Re-correr `/compliance-cl` (drift) | Dev |

---
*Guía operativa de compliance-cl. No es asesoría legal.*
