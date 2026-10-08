# Catálogo de modelos: onde está

O arquivo real, `references/catalogo-modelos.md`, **não é versionado neste repositório**, que é público. Ele indexa os modelos reais de representação do usuário e, ao descrever quando usar cada um, revelaria tática operacional da unidade.

Fonte de verdade (repositório **privado** `delegacia-claude-workspace`):

- Catálogo: `~/Documents/DELEGACIA/MODELOS-REPRESENTACAO/catalogo-modelos.md`
- Modelos: `~/Documents/DELEGACIA/MODELOS-REPRESENTACAO/*.md`

Numa máquina nova, depois de sincronizar as skills (o sync também traz o repo privado), restaure os dois destinos locais:

```powershell
$src = "$env:USERPROFILE\Documents\DELEGACIA\MODELOS-REPRESENTACAO"
$sk  = "$env:USERPROFILE\.claude\skills\representacao-cautelar"
Copy-Item "$src\catalogo-modelos.md" "$sk\references\" -Force
Copy-Item "$src\*.md" "$sk\assets\modelos\" -Force
Remove-Item "$sk\assets\modelos\catalogo-modelos.md" -ErrorAction SilentlyContinue
```

Sem o catálogo, a skill ainda funciona: ela cai nas references genéricas
(`preventiva-temporaria.md`, `busca-apreensao.md`, `quebra-sigilo.md`) e no
`templates/modelo_base.md`, apenas sem a fraseologia real do usuário.
