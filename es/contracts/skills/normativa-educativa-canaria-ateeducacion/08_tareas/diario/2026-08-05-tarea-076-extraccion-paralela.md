# Diario — 2026-08-05: extracción curricular en paralelo (TAREA-076)

## Hecho

Ejecutadas en paralelo las tareas curriculares pendientes, en siete ramas independientes, cada
una limitada a sus propias fichas `CUR` para que no se pisaran entre sí. La consolidación
—índices, `status.yaml`, estados de tarea— se hizo después, desde un solo punto.

## Los agentes tenían razón y la herramienta estaba mal

Los dos agentes de Bachillerato reportaron que el auditor marcaba su trabajo como divergente y
lo atribuían a fallos de la herramienta. Es exactamente el tipo de afirmación que no conviene
aceptar sin comprobar. Comprobada punto por punto: **tenían razón en los tres casos**.

1. **La comparación se rompió con `DEC-0008`.** El auditor seguía tratando `descriptores` como
   lista plana, así que al migrar al mapa por curso comparaba códigos contra nombres de curso.
   Toda ficha migrada salía divergente. Bug mío, introducido al migrar sin actualizar el auditor.
2. **Los subcódigos decimales se truncaban.** Bachillerato usa `CPSAA1.1`, `CCEC3.2` y
   similares —197 apariciones de `CPSAA1.1` solo en el decreto consolidado— y la expresión
   regular los reducía a `CPSAA1`.
3. **Las variantes por curso se colapsaban.** Sin cabecera de curso a la vista, todas las
   apariciones caían bajo la clave `?` y `setdefault` se quedaba con la primera. Era la causa de
   que `CUR-009` pareciera divergir desde el principio: sus descriptores «sobrantes» son los de
   **2.º de ESO**, y el auditor nunca llegaba a verlos.

Ese tercer punto resuelve retroactivamente una parte de lo que `TAREA-072` había dado por
divergencia real.

Corregidos los tres, y añadida la búsqueda en los textos por materia para las cuatro materias
propias de Canarias, que no figuran en el decreto consolidado.

## Verificación

**229 de 230 competencias verifican contra la fuente oficial: 99,6 %.** La restante, `CUR-057`
C5, se comprobó a mano y también es correcta; el anclaje falla porque un número de página parte
la frase en la conversión del PDF.

El reparto de extracción curricular pasa de 26 completadas y 32 parciales a **38 y 20**.

## Tres hallazgos que no estaban previstos

**En Infantil no existen los descriptores operativos.** Cero apariciones de «descriptor», de
«perfil de salida» y de códigos numerados en todo el Decreto 196/2022. No es una carencia del
corpus: el Perfil de salida es de la enseñanza básica, y el Anexo 1 describe las competencias
clave solo en prosa. `TAREA-069` se cierra por no proceder, y el cuarto elemento de `DEC-0004`
no aplica a esta etapa.

**La copia local del decreto de Primaria no contiene el currículo.** Sus anexos se publican como
PDF o imagen y la conversión desde el HTML los sustituyó por un marcador. `TAREA-067` queda
bloqueada y `TAREA-077` recoge la re-exportación desde el PDF oficial.

**`FTE-051` declara una resolución que no existe** como norma diferenciada. La única de esa
fecha es la 73/2025, ya catalogada como `FTE-049`, verificada por su sello de registro
electrónico. Parece un desdoblamiento por etapas, mismo patrón que `NOR-046` y `NOR-049`. Queda
como `PREG-009`: cualquier salida cambia la identidad de una fuente y afecta a fichas de otras
tareas.

## IDs consumidos

`TAREA-076`, `TAREA-077`, `PREG-009`.

## Pendiente

- `PREG-009`: identidad de `FTE-051`.
- `TAREA-077`: re-exportar el anexo de Primaria, que desbloquea `TAREA-067`.
- Las 7 fichas de Bachillerato que siguen en `parcial` tienen las competencias completas pero
  `criterios_evaluacion` y `saberes_basicos` como muestra, no como anexo íntegro.
