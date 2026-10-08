# Plantilla: Tabla de fuentes verificadas

Usar este formato para cada tabla de fuentes en `jurisprudencia/fuentes-*.md`.
El nombre puede ser `fuentes-[identificador].md` (fecha, número de expediente, tipo de escrito).

---

# Fuentes verificadas · [Identificador del caso/escrito]

**Caso:** [Carátula o número]  
**Escrito(s) asociado(s):** [Nombre de archivos en escritos/]  
**Última actualización:** [YYYY-MM-DD HH:MM]  
**Responsable de actualización:** [Nombre/iniciales del abogado]

---

## Tabla de fuentes

| Norma/Fallo                  | Cita textual    | UUID SAIJ         | URL SAIJ                | Vigencia / Obs.         | Secciones usadas |
| ---------------------------- | --------------- | ----------------- | ----------------------- | ----------------------- | ---------------- |
| Ley N° 27043                 | Art. 15         | `abc-def-ghi-123` | https://saij.gob.ar/... | Vigente. Reforma 2020   | §I.A.2, §III.B.1 |
| CSJN, Fallos T.340:1313      | Considerando 5  | `jkl-mno-pqr-456` | https://saij.gob.ar/... | Jurisprudencia pacífica | §II.C            |
| Resolución AFIP N° 4567/2023 | Art. 3, inc. a) | `stu-vwx-yz0-789` | https://saij.gob.ar/... | Vigente                 | §IV.D            |

---

## Notas sobre cada fuente

### Ley N° 27043

- **Texto completo:** [Resumen breve del contenido relevante del artículo citado]
- **Verificación:** Consultado en SAIJ, vigencia confirmada.
- **Riesgos:** Reforma de 2020 cambió redacción de Art. 15; usar versión actual.

### CSJN, Fallos T.340:1313

- **Carátula:** [Carátula exacta del fallo si se conoce]
- **Año:** [Año del fallo]
- **Relevancia:** [Por qué se cita / qué establece]
- **Verificación:** Consultado en SAIJ, disponible en texto completo.

### Resolución AFIP N° 4567/2023

- **Tema:** [Asunto de la resolución]
- **Verificación:** Consultado en AFIP, vigente.
- **Riesgos:** Resoluciones administrativas pueden modificarse frecuentemente.

---

## Cómo usar esta tabla en auditoría

1. **En argentina-bucles (Paso 2 & Paso 6):**
   - Paso 2: conforme investigas en SAIJ, agrega nuevas filas a esta tabla.
   - Paso 6: toda cita del escrito final debe estar en esta tabla (o marcada 🔲).

2. **En argentina-diagnostico (Sección G):**
   - Corre skill argentina-auditoria-citas con esta tabla.
   - Confirma que toda cita en el escrito aparece aquí.

3. **Mantenimiento:**
   - Agregar filas conforme se citan nuevas normas/fallos.
   - Actualizar "Última actualización" cada vez que edites.
   - Si una norma se reforma, agregar nueva fila (no reemplazar) y aclarar vigencia.

---

## Cuidados

- ⚠️ **UUID SAIJ:** obtener de la URL o del header de SAIJ (`saij_documento(uuid)`).
- ⚠️ **URL:** usar URL permanente de SAIJ, no acortada.
- ⚠️ **Secciones usadas:** anotar TODAS las referencias en el escrito (§I.A.2 = Sección 1, subsección A, párrafo 2).
- ⚠️ **Vigencia:** si hay dudas sobre vigencia/reforma, anotarlo; la auditoría mostrará ⚠️.
- ⚠️ **Citas sin verificar:** NO agregarlas a esta tabla. Marcar en el escrito con 🔲 y decidir si se verifica luego o se elimina.

---

## Estado de la tabla

- [ ] Todas las citas del escrito final están aquí
- [ ] Todos los UUIDs SAIJ confirmados
- [ ] Todas las URLs funcionan
- [ ] Vigencia de cada norma confirmada
- [ ] Secciones usadas anotadas correctamente
- [ ] Abogado/a responsable confirmó la tabla antes de presentación

---

_Última auditoría: [Fecha/resultado de argentina-auditoria-citas]_
