# Clasificación de datos — catálogo chileno

Antes de aplicar cualquier checklist, clasifica el dato. La clasificación decide
todo lo demás: base de licitud exigible, si necesitas consentimiento expreso,
severidad de un hallazgo, y si el campo entra al inventario.

## Las cuatro clases

```
INTERNO     No identifica a una persona natural, o identifica a la organización.
            Ej.: id de producto, configuración del sistema, métricas agregadas
            sin desagregar bajo el umbral k (ver derechos-y-ciclo-de-vida.md).

PERSONAL    Identifica o hace identificable a una persona natural, sin caer en
            ninguna categoría sensible.
            Ej.: nombre, email, teléfono, dirección, RUT, fecha de nacimiento,
            IP, geolocalización puntual, historial de compras.

SENSIBLE    Categoría reforzada del art. 2 letra g) de la ley. Exige
            consentimiento expreso salvo excepción acotada (ver
            bases-y-consentimiento.md). Ver catálogo completo abajo.

NNA         Transversal a las dos anteriores: el dato es de un niño, niña o
            adolescente. Régimen propio (art. 16 quáter). No sustituye la
            clasificación PERSONAL/SENSIBLE, se le suma.
```

Un dato puede ser `SENSIBLE` y de un titular `NNA` a la vez — es el caso de
mayor exigencia y el que primero hay que resolver bien.

Un cambio que solo toca datos `INTERNO` no requiere Privacy Review ni entra al
inventario. Esa es la salida rápida que hace que el resto del triaje no se
convierta en burocracia para cada PR.

## Catálogo de datos sensibles (art. 2 letra g)

La lista legal, con el campo típico que la dispara en un sistema chileno:

| Categoría legal | Campos típicos que la disparan |
|---|---|
| Origen étnico o racial | `etnia`, `pueblo_originario`, `nacionalidad` (con cautela: nacionalidad sola no siempre basta, revisa el uso) |
| Afiliación política, sindical o gremial | `afiliacion_sindical`, `partido`, `gremio` |
| Situación socioeconómica | `renta`, `sueldo`, `ingreso`, `tramo`, `deuda`, `morosidad`, `dicom`, `score`, `scoring`, `subsidio`, `ficha_social`, `isapre`, `fonasa`, `prevision`, `afp`, `beca` |
| Convicciones ideológicas, filosóficas o religiosas | `religion`, `creencia`, `ideologia` |
| Datos de salud | `diagnostico`, `enfermedad`, `medicamento`, `alergia`, `discapacidad`, `licencia_medica`, `ficha_clinica`, campos libres en módulos clínicos |
| Datos biométricos y perfil biológico humano | `huella`, `reconocimiento_facial`, `iris`, `adn`, `genetic*`, plantillas biométricas de cualquier tipo |
| Vida sexual, orientación sexual e identidad de género | `orientacion_sexual`, `identidad_genero` |

> **La situación socioeconómica es la trampa para equipos que vienen de GDPR.**
> Un CRM con campo `renta`, un módulo de cobranza con `dias_mora`, o un motor de
> scoring crediticio son, en Chile, tratamiento de datos sensibles — no
> tratamiento ordinario. Ver `marco-legal.md`.

## Datos económicos, financieros, bancarios y comerciales

No están en la lista de sensibles, pero tienen régimen propio (ver
`marco-legal.md` y Ley 20.575). En la práctica, trátalos con el mismo nivel de
cuidado que un dato sensible: consentimiento o base específica, minimización
estricta, prohibido en logs.

Campos típicos: `numero_tarjeta`, `cuenta_bancaria`, `iban`, `historial_pago`,
`historial_crediticio`, `linea_credito`, `deuda_total`.

## Campos de texto libre

`observaciones`, `notas`, `comentarios`, `detalle`, `descripcion` no tienen
clasificación fija: depende de qué reciben en la práctica, no de su nombre.

Regla práctica: si el módulo es clínico, de RRHH, de cobranza o de beneficios,
trata el campo de texto libre como `SENSIBLE` por defecto, aunque el esquema no
lo declare. Nadie audita el contenido real de un `TEXT` hasta que ya está lleno
de diagnósticos.

## Identificadores

El RUT merece mención aparte porque el reflejo de un equipo chileno es tratarlo
como un id técnico más.

- El RUT es dato **PERSONAL** (identifica). No es sensible por sí solo, pero es
  el identificador más reutilizado del sistema y el más peligroso para
  enumeración: el espacio de RUT es finito y el dígito verificador se calcula,
  no se adivina al azar.
- No lo uses como identificador expuesto en URLs ni como clave primaria visible
  al cliente. Usa un id opaco (UUID) y guarda el RUT como atributo, no como
  llave.
- Hashear el RUT **no es anonimizar** (ver `derechos-y-ciclo-de-vida.md`): el
  espacio es enumerable y el hash se revierte por fuerza bruta en minutos.

## NNA — qué preguntar antes de clasificar

No existe un único "dato de NNA": lo que cambia es el titular, no el tipo de
dato. Antes de clasificar, responde:

1. ¿El titular es menor de 18 al momento del tratamiento? Necesitas poder
   calcular la edad, lo que exige almacenar fecha de nacimiento, no un flag.
2. ¿El tramo de edad importa para este tratamiento? El art. 16 quáter
   diferencia niños/niñas de adolescentes con reglas distintas —el corte exacto
   y su alcance por tipo de dato es `REVISIÓN LEGAL REQUERIDA`, no lo deduzcas
   de este archivo.
3. ¿Hay representación legal involucrada? Modélala explícitamente
   (`representante_legal_id`, no una casilla declarativa) — ver
   `bases-y-consentimiento.md`.

## Cómo clasificar un campo nuevo

Ante un campo que no aparece en el catálogo, en este orden:

```
1. ¿Identifica o hace identificable a una persona natural?
   No → INTERNO. Termina aquí.
   Sí → sigue.

2. ¿Cae en alguna categoría del art. 2 letra g), incluida situación
   socioeconómica?
   Sí → SENSIBLE.
   No → sigue.

3. ¿Es un dato económico, financiero, bancario o comercial?
   Sí → régimen propio, trátalo como SENSIBLE en la práctica.
   No → PERSONAL.

4. ¿El titular puede ser menor de edad en este contexto?
   Sí → agrega NNA a la clasificación anterior.
```

Anota la clasificación en el esquema (comentario de columna o convención del
ORM) y en `docs/privacidad/inventario.md`. Un campo sin clasificación anotada
es, para efectos de la próxima auditoría, un campo sin clasificar — aunque
alguien lo haya pensado bien una vez.
