# TEST-CASES — /frontend-privacy/consentimiento

> Verificar estos casos antes de publicar cambios a la skill.  
> El score debe estar dentro de ±3 pts del esperado.

---

## C1 — Checkbox pre-marcado, sin granularidad, sin revocación

**Input:**
```
/frontend-privacy/consentimiento "Formulario de registro con un checkbox 
pre-marcado 'Acepto términos y política de privacidad'. Opera en México."
```

**Cálculo esperado:**
- Pre-marcado → +15 (inválido)
- No granular → +15 (única finalidad)
- Sin revocación → +10 (no mencionada)
- Sin registro → +10 (no mencionado)
- F_rigor = 1.00 (MX)
- Raw = (15+15+10+10) × 1.00 = 50 → **Score: 50 🚨**

**Hallazgos esperados (top 3):**
1. 🔴 Checkbox pre-marcado por defecto (+15)
2. 🔴 Sin consentimiento granular por finalidad (+15)
3. 🟡 Sin mecanismo de revocación (+10)

**Acción prioritaria esperada:** Reemplazar el checkbox pre-marcado por uno vacío y separar las finalidades en toggles individuales.

---

## C2 — Toggles granulares + revocación + sin registro

**Input:**
```
/frontend-privacy/consentimiento "Tres toggles en el registro: servicio 
(obligatorio), analytics (opcional), marketing (opcional). Sección 
'Privacidad' en el perfil para revocar. No guardamos el historial de 
consentimientos en la base de datos. Brasil."
```

**Cálculo esperado:**
- Granularidad → 0 (tres toggles separados ✅)
- Revocación → 0 (sección de privacidad fácil de encontrar ✅)
- Sin registro → +10
- F_rigor = 1.25 (Brasil)
- Raw = 10 × 1.25 = 12.5 → **Score: 13 🟡**

**Hallazgos esperados:**
1. 🟡 Sin registro de consentimiento con versión de política (+10)

**Acción prioritaria esperada:** Crear tabla `user_consents(user_id, purpose, notice_version, granted_at, revoked_at)`.

---

## C3 — Datos de salud + consentimiento mezclado con newsletter

**Input:**
```
/frontend-privacy/consentimiento "App de salud. Un solo checkbox 
'Acepto la política de privacidad' que cubre el tratamiento de 
diagnósticos médicos, el newsletter y el análisis de comportamiento. 
Opera en Colombia."
```

**Cálculo esperado:**
- No granular → +15
- Datos sensibles sin consentimiento específico destacado → +15
- F_rigor = 1.00 (CO)
- Raw = 30 × 1.00 = 30 → **Score: 30 🔴**

**Hallazgos esperados:**
1. 🔴 Sin consentimiento granular (+15)
2. 🔴 Datos sensibles sin consentimiento específico (+15)

**Acción prioritaria:** Separar el consentimiento de datos de salud en un paso propio, posterior al registro, con aviso destacado.

---

## C4 — Consentimiento conforme

**Input:**
```
/frontend-privacy/consentimiento "Toggles separados: servicio (pre-aceptado, 
no desmarcable), analytics (vacío, opcional), marketing (vacío, opcional). 
Revocación desde Configuración > Privacidad en 2 clics con confirmación. 
Se guarda: user_id, purpose, versión de política 'v3.0', timestamp, IP. 
Colombia."
```

**Cálculo esperado:**
- Granularidad → 0 ✅
- Revocación → 0 ✅ (2 clics = fácil)
- Registro → 0 ✅ (completo)
- F_rigor = 1.00
- Raw = 0 → **Score: 0 🟢**

**Output esperado:** Panel limpio sin hallazgos, confirmar que la skill no genera falsos positivos en un sistema conforme.

---

## C5 — Re-consentimiento al cambiar política (caso límite)

**Input:**
```
/frontend-privacy/consentimiento "Al actualizar la política de privacidad 
se muestra un modal que dice 'Actualizamos nuestros términos. Al continuar 
usando la app aceptas los nuevos términos.' Sin describir qué cambió. 
Usuarios en Brasil y Colombia."
```

**Cálculo esperado:**
- Re-consentimiento implícito (continuar = aceptar) → +15 (inválido bajo LGPD)
- Sin descripción de cambios específicos → no penalizador adicional, pero supuesto marcado
- F_rigor = 1.25 (Brasil)
- Raw = 15 × 1.25 = 18.75 → **Score: 19 🟡**

**Supuesto a marcar:** La skill debe indicar: "⚠️ Supuesto: el re-consentimiento por 'continuar usando' no es válido bajo LGPD — se requiere acción activa y descripción de qué cambió."

---

## Criterio de éxito

| Criterio | Umbral |
|---|---|
| Score dentro de ±3 pts del esperado | 5/5 |
| Hallazgo #1 correcto | 5/5 |
| C4 (conforme) no genera falsos positivos | Sí |
| C3 (sensible) detecta el gap de datos de salud | Sí |
| C5 marca supuesto de re-consentimiento inválido | Sí |
