# Pack: Ley 18.331 — Protección de Datos Personales (Uruguay)

> **Ya vigente.** Régimen = **Ley 18.331 (2008)** + **Decreto 414/009** + **Ley 19.670 arts. 37–40 (2018)**
> + **Decreto 64/020 (2020)**. Aplica a todo responsable/encargado establecido en Uruguay, **sin umbral**
> (el umbral de 35.000 personas solo activa la obligación de **DPO**, no la de cumplir la ley). Uruguay
> tiene **adecuación UE** (Decisión 2012/484/UE) y ratificó el **Convenio 108+**. Numeración verificada en
> `references/mapa-articulos-18331.md`.

## Controles que exige (ver `references/controls.md`)
`gov-responsable` (DPO si aplica), `gov-registro-urcdp` (inscripción de bases), `gov-rat`,
`gov-politicas`, `data-licitud`, `data-consent-text`, `data-derechos`, `data-info`, `data-minimizacion`,
`data-dpa`, `data-transfer`, `data-dpia`, `data-privacy-by-design`, `data-pseudonym`, `sec-tls`,
`sec-rest`, `sec-passwords`, `sec-mfa`, `sec-logs`, `sec-tenant`, `sec-secrets`, `sec-backups`, `inc-brechas`.

## Obligaciones clave (resumen, con artículo)
- **Roles:** responsable de la base/tratamiento (decide fines) vs **encargado** (trata por cuenta del
  responsable). Definiciones en **Art. 4**.
- **Consentimiento (Art. 9):** **libre, previo, expreso e informado**, y **debe documentarse**. Excepciones
  tasadas (fuente pública, relación contractual, funciones del Estado, etc.). Procedimiento de captura en
  **Decreto 414/009 art. 6** (claro, gratuito, opciones no premarcadas; el silencio tras 10 días hábiles = negativa).
- **Deber de información al recabar (Art. 13):** finalidad y destinatarios; existencia de la base e identidad
  y **domicilio** del responsable; carácter obligatorio/facultativo; consecuencias; **derechos (arts. 14-16)**;
  existencia de **transferencias internacionales**; criterios de las **decisiones automatizadas** (Art. 16).
- **Derechos del titular:** **acceso (Art. 14)** — gratuito a intervalos de 6 meses; **rectificación,
  actualización, inclusión o supresión (Art. 15)** — el responsable resuelve en **5 días hábiles**.
  ⚠️ Uruguay **no** consagra portabilidad/oposición/bloqueo al estilo RGPD: no ofrecerlos como derechos legales.
- **Datos sensibles (Art. 18):** consentimiento **expreso y escrito**; recolección prohibida salvo excepciones.
  Definición en **Art. 4 lit. E** (origen racial/étnico, preferencias políticas, convicciones religiosas o
  morales, afiliación sindical, salud, vida sexual).
- **Seguridad (Art. 10 + Decreto 64/020 art. 3):** medidas técnicas/organizativas; referencia al **Marco de
  Ciberseguridad de AGESIC**. **Reserva/secreto (Art. 11).**
- **Privacidad por diseño y por defecto (Decreto 64/020 arts. 8 y 9):** disociación, seudonimización,
  minimización; por defecto solo los datos necesarios.
- **Brechas (Decreto 64/020 art. 4 / Ley 19.670 art. 38):** comunicar a la **URCDP en un plazo máximo de
  72 horas**; a los **titulares** si hay afectación significativa, en lenguaje claro. Informe posterior a la URCDP.
- **Responsabilidad proactiva / accountability (Decreto 64/020 art. 5; art. 12 Ley 18.331 según art. 39 Ley
  19.670):** medidas documentadas, revisadas y a disposición de la URCDP.
- **Inscripción registral (Art. 29):** OBLIGACIÓN URUGUAYA ESPECÍFICA — inscribir **toda base de datos** en el
  **Registro de Bases de Datos de la URCDP** (Decreto 414/009 arts. 15-20).
- **DPO (Ley 19.670 art. 40 + Decreto 64/020 art. 10):** obligatorio para (a) entidades públicas; (b) privadas
  que traten **datos sensibles como negocio principal**; (c) privadas con **grandes volúmenes = +35.000
  personas**. Si no aplica, lo asume el responsable.
- **DPIA / Evaluación de Impacto (Decreto 64/020 arts. 6-7):** **previa** al tratamiento si hay perfiles,
  grupos vulnerables (menores), grandes volúmenes, datos sensibles como giro, o transferencia a país sin
  protección adecuada.
- **Transferencias internacionales (Art. 23 + Decreto 414/009 arts. 34-35):** lícitas hacia países con
  **nivel adecuado**; en su defecto, **autorización de la URCDP** aportando los contratos/garantías
  (cláusulas contractuales), o una excepción tasada del Art. 23.

## Sanciones (Art. 35 — verificado)
(1) Observación · (2) apercibimiento · (3) **multa de hasta 500.000 UI** · (4) suspensión de la base por
**5 días** · (5) **clausura** de la base. Se gradúan por gravedad, reiteración y reincidencia. Fiscaliza la **URCDP**.

## Documentos a generar (templates/ → `<repo>/.compliance/docs/` con prefijo `18331-`)
`rat.md`, `politica-privacidad.md`, `consentimiento.md`, `canal-derechos.md`, `dpa.md`,
`anexo-transferencias.md`, `plan-respuesta-brechas.md`, `registro-vulneraciones.md`,
`inscripcion-bases-urcdp.md`, `dpia.md` (si los supuestos del Decreto 64/020 art. 6 la hacen obligatoria).
