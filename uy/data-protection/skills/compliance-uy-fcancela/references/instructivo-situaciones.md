# Instructivo: qué hacer ante cada situación (runbooks)

Manual operativo para consultar cuando pase algo. La skill lo incluye en el output
(`<repo>/.compliance/INSTRUCTIVO.md`). El founder ejecuta esto **solo**; el abogado solo entra en la
representación de una inspección o un habeas data judicial (caso reactivo).

---

## A. Llega un derecho del titular (acceso, rectificación, actualización, inclusión, supresión)
**Plazos:** **rectificación/actualización/inclusión/supresión → 5 días hábiles** para resolver o explicar por
qué no procede (Art. 15). **Acceso → gratuito a intervalos de 6 meses** (Art. 14).
1. Registrá la solicitud (fecha, quién, qué pide) y **verificá identidad** (documento de identidad o poder, Art. 14).
2. Ubicá sus datos (BD, backups, encargados/proveedores).
3. Ejecutá: **acceso** → entregá copia clara; **rectificación/actualización/inclusión** → corregí/completá y
   **notificá a los destinatarios**; **supresión** → eliminá o disociá (salvo obligación legal de conservar, p.
   ej. registros de LA/FT o tributarios).
4. Respondé por escrito y **guardá evidencia**.
> Uruguay **no** tiene portabilidad/oposición/bloqueo como derechos legales: no los ofrezcas como obligación.

## B. Vulneración de seguridad / brecha (acceso no autorizado, filtración, pérdida, alteración)
**Plazo: comunicar a la URCDP en un plazo máximo de 72 horas** desde que se conoce (Decreto 64/020 art. 4).
1. **Contené:** aislá, revocá accesos, rotá credenciales. Abrí bitácora (el reloj de 72h ya corre).
2. **Evaluá:** qué datos, cuántos titulares, si hay **afectación significativa**. Si fue un encargado, exigile la info.
3. **Comunicá:** a la **URCDP** (naturaleza, datos, volumen, consecuencias, medidas); a los **titulares** si hay
   afectación significativa, en lenguaje claro. Si sos encargado, avisá también al **responsable**.
4. **Registrá** la vulneración en `registro-vulneraciones.md`.
5. **Cerrá:** causa raíz + fix + **informe detallado a la URCDP** + actualizá RAT y este plan.

## C. Te inspecciona la URCDP (datos) o SENACLAFT (LA/FT)
Único caso donde conviene un **[ABOGADO]** (la representación es reservada por ley).
1. Designá un contacto único. Todo por escrito.
2. **Identificá la etapa:** ¿pedido de información o procedimiento sancionatorio formal?
3. **Reuní los antecedentes:** RAT, comprobante de inscripción de bases, evidencia de consentimiento, medidas
   de seguridad, registro de vulneraciones, DPA, DPIA → ya están en `<repo>/.compliance/`. (LA/FT: programa,
   matriz, DD, ROS, capacitación, conservación.)
4. **Respondé en plazo**, mostrando debida diligencia y remediación.
5. **Recordá las sanciones:** datos (Art. 35) — observación, apercibimiento, **multa hasta 500.000 UI**,
   suspensión 5 días, clausura. LA/FT (Ley 19.574 art. 13) — apercibimiento, observación, **multa 1.000 a
   20.000.000 UI**, suspensión.
6. **Nunca:** ocultar o destruir documentos, ni ignorar plazos.

## D. Operación sospechosa (solo si sos sujeto obligado de LA/FT)
1. Quien detecta comunica al **Oficial de Cumplimiento** (no alertes al cliente — **reserva**, Ley art. 22).
2. El Oficial analiza contra el perfil y la matriz de riesgo.
3. Si hay sospecha, presenta el **ROS a la UIAF del BCU** (no se requiere certeza de delito).
4. Conservá el ROS y su respaldo en forma reservada (mín. 5 años). Reportar de buena fe **no genera
   responsabilidad** (Ley art. 23).

## E. Cambia la ley o sale una resolución (URCDP / SENACLAFT)
1. Actualizá el corpus en `sources/` (re-descarga, ver `sources/FUENTES.md`).
2. Ajustá el pack afectado y los controles.
3. Re-corré `/compliance-uy` → el `state.json` muestra qué cambió.

## F. Calendario de revisión
| Cuándo | Qué | Quién |
|---|---|---|
| Antes de operar una base / ante cambios | Inscribir/actualizar bases en la **URCDP** | Responsable de datos |
| Anual (o ante cambios) | Revisar y actualizar el **RAT** y la **DPIA** | Responsable / DPO |
| Anual | Capacitación del equipo (datos y, si aplica, LA/FT) | Responsable / Oficial de Cumplimiento |
| Permanente | **Seguimiento continuo** de clientes (si sos sujeto obligado LA/FT) | Oficial de Cumplimiento |
| Al firmar/renovar proveedor | DPA + anexo de transferencia (Art. 23) | Responsable |
| Cada release relevante | Re-correr `/compliance-uy` (drift) | Dev |

---
*Guía operativa de compliance-uy. No es asesoría legal.*
