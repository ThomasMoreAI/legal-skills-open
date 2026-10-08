# Skills

Skills internas para catalogar, analizar, vigilar vigencia, extraer currículo y publicar el portal. Cuándo cargar cada una: `AGENTS.md` §6.

El origen canónico es `.agents/skills/`. `.claude/skills/` es una copia completa de esta carpeta, sin enlaces simbólicos. Al cambiar un skill local:

```bash
rsync -a --delete --exclude .DS_Store --exclude .venv .agents/skills/ .claude/skills/
```

Cada skill es un directorio con `SKILL.md`. `name` coincide con el directorio. `description` dice qué hace y cuándo usarla: es el texto que el modelo ve antes de abrir el fichero.

La skill pública para asistentes externos está en `skills/experto-normativa-educativa-canaria/SKILL.md`, no en esta carpeta. No es una de estas skills internas.
