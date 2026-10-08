# Como contribuir

Obrigado por querer melhorar o LGPD Enterprise Auditor. Este guia resume o fluxo de contribuição e as regras que mantêm o framework consistente.

## Antes de começar

- **Mudanças não triviais começam por uma issue.** Novas verificações, mudanças de severidade/score, novos módulos, cenários ou ferramentas: abra uma issue e descreva a proposta antes de escrever código. Correções de digitação e ajustes pequenos podem ir direto para PR.
- **Atualizações normativas são especialmente bem-vindas.** Nova resolução da ANPD, decreto ou lei? Use o modelo de issue "Atualização normativa" e cite sempre a fonte oficial ([Planalto](https://www.planalto.gov.br/), [DOU](https://www.in.gov.br/), [gov.br/anpd](https://www.gov.br/anpd/)). Notícias e blogs não bastam como fonte.
- **Nunca inclua dados pessoais, segredos ou trechos de relatórios confidenciais** em issues, PRs, exemplos ou testes.

## Fluxo

1. Faça um fork e crie uma branch a partir de `main` (ex.: `feat/novo-check-cookies`, `fix/instalador-windows`).
2. Faça as alterações seguindo as regras abaixo.
3. Rode os testes (seção [Testes](#testes)).
4. Abra o PR preenchendo o checklist do modelo e referencie a issue (`Closes #123`).

## Regras do framework

O repositório distribui o mesmo auditor em duas formas, ambas atuais: a **skill** (`SKILL.md`) e o **framework modular** (`.agents/lgpd-enterprise-auditor/`). Não use as designações "V1", "V2", "legado" ou "monolito" para elas.

- **Paridade.** Toda mudança de lógica de auditoria (item de checklist, regra de severidade, peso de score, campo de relatório) deve ser avaliada nas duas formas. Se a cobertura mudar, atualize `validation/parity-checklist.md` (e `validation/traceability-matrix.md` se um domínio mudar de módulo).
- **Catálogo de itens.** Os itens do checklist ficam nas tabelas "Checklist atômico" dos módulos, com ID fixo, domínio, criticidade, agravante ou atenuante, tipo de controle e fundamento. Item novo ganha o próximo número do prefixo do arquivo; ID nunca é renumerado nem reaproveitado. O catálogo da `SKILL.md` é gerado a partir dos módulos: depois de mexer numa tabela, rode `scripts/update-skill-catalog.sh` e nunca edite o bloco entre os marcadores `CATALOGO` à mão.
- **Só norma vigente gera achado.** Apenas normas em vigor produzem `finding` ou status `NAO_CONFORME`. Projetos de lei, consultas públicas e minutas ficam em seções "Em monitoramento" e só podem alimentar `recomendacoes_tecnicas`.
- **Evidência e fundamento.** Todo `finding` cita o artigo aplicável da LGPD (ou da norma correlata) e classifica a evidência nos dois eixos independentes: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`). Nada é `CONFORME` sem evidência `ENCONTRADA`.
- **Contratos só no `core/`.** Severidade, score e formato de relatório são definidos apenas em `.agents/lgpd-enterprise-auditor/core/`. Nenhum módulo os redefine localmente.
- **Convenção de IDs.** IDs de módulo usam kebab-case (`ai-llm`); IDs de área de score usam snake_case (`ai_llm`). Não unifique.
- **Cenários.** Os IDs de cenário devem ser idênticos em `orchestrator/router.md`, `orchestrator/activation-matrix.md`, no `README.md` do framework e em cada `commands/*.md`. `core` e `legal` são sempre obrigatórios; `full_audit` ativa todos os módulos.
- **Instaladores andam juntos.** `scripts/install.sh` (compatível com o bash 3.2 do macOS) e `scripts/install.ps1` (PowerShell 5.1 e 7) são funcionalmente equivalentes: mesmas ações, opções, destinos e formato de manifesto. Alterou um, altere o outro. `install.ps1` e `tests/test-install.ps1` precisam manter o BOM UTF-8.

## Idioma

- READMEs: `README.md` (português, canônico) e `README.en.md` (inglês) mantidos em sincronia.
- Internos do framework (`.agents/`, `SKILL.md`, `commands/`): português do Brasil.
- Todo texto em português usa acentuação completa e correta, inclusive em `commands/*.md` (a descrição dos comandos aparece no menu dos assistentes). Identificadores entre crases (IDs de cenário, de módulo, de área e valores como `NAO_CONFORME`) ficam sem acento. Títulos dos arquivos do framework em português: `# Núcleo — …`, `# Módulo X — …`, `# Manifesto — \`id\`` e `# Modelo — …`.

## Changelog e data de sincronização

- Toda mudança visível ao usuário ganha uma entrada em `## [Não lançado]` no `CHANGELOG.md` (seções `Adicionado`, `Alterado`, `Corrigido`, `Removido`), no mesmo PR.
- Mudanças normativas ou substantivas no framework atualizam a linha "Última sincronização" / "Last synchronization" nos dois READMEs para o mês atual (`AAAA-MM`), com o mesmo valor.
- Não altere `metadata.version` nem crie tags: isso faz parte do processo de release do mantenedor.

## Testes

Rode a partir da raiz do clone. Um comando roda tudo o que o CI roda:

```bash
scripts/tests/run-all.sh
```

Ou cada suíte em separado:

```bash
scripts/tests/test-framework.sh     # catálogo, paridade skill/framework, cenários, manifestos
scripts/tests/test-html-report.sh   # modelo HTML e relatório de exemplo (usa python3 para validar os dados)
scripts/tests/test-install.sh
scripts/tests/test-versions.sh
```

Se a mudança altera o cálculo do score, o formato do relatório ou o catálogo, atualize o relatório de exemplo (`examples/saas-demo/`, `.md` e `.html`) no mesmo PR; `scripts/validate-report.py` confere os dados.

Se tiver o PowerShell disponível:

```bash
pwsh ./scripts/tests/test-install.ps1
```

O CI também roda ShellCheck nos scripts bash, os testes no Ubuntu, no macOS (`/bin/bash` 3.2) e no Windows (PowerShell 7 e 5.1), e confere que nenhum commit traz assinatura de agente de IA.

## Mensagens de commit

Use [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/), com escopo quando fizer sentido:

```text
feat(eca-digital): adiciona verificação de supervisão parental
fix(installer): corrige caminho da skill no Windows
docs(readme): atualiza tabela de resoluções da ANPD
```

## Conduta

Ao participar, você concorda com o [Código de Conduta](./CODE_OF_CONDUCT.md). Vulnerabilidades devem ser relatadas conforme a [Política de Segurança](./SECURITY.md), nunca em issues públicas.
