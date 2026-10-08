# Changelog

Todas as mudanças relevantes deste projeto são documentadas neste arquivo.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o versionamento segue [Semantic Versioning](https://semver.org/lang/pt-BR/). A versão do projeto é a `metadata.version` do `SKILL.md`, repetida em todos os `commands/*.md`; cada versão publicada tem uma tag `vX.Y.Z` correspondente.

## [Não lançado]

## [1.8.1] - 2026-10-05

### Alterado
- Relatório em HTML: o botão de tema passa a mostrar um ícone e o tema para o qual a página muda (lua e "tema escuro" no tema claro, sol e "tema claro" no escuro), no lugar do texto "tema".

## [1.8.0] - 2026-10-05

Quatro pontos que o terceiro teste de ponta a ponta ainda mostrou depender de julgamento (a v1.7.0 coincidiu com o exemplo em 104 dos 108 itens).

### Adicionado
- Item `BL-04`, de minimização (art. 6º, III): os dados coletados em cada formulário, cadastro ou integração se limitam ao necessário para a finalidade. Nos fluxos em que o auditado é só operador, a escolha dos campos é do controlador.
- Lista fechada de dependências entre itens, escrita nos módulos no formato "`GV-05` depende de `GV-02`" e gerada para a skill junto com o catálogo. Com o item de que depende reprovado, o dependente fica `NAO_APLICAVEL`; fora da lista não há dependência. `scripts/validate-report.py` passa a conferir.

### Alterado
- Item com elementos verificáveis e elementos fora do alcance: se um verificável falha, vale a falha; se todos atendem, o item fica `NAO_VERIFICADO`, com o que já foi comprovado registrado. A v1.7.0 dava `CONFORME` com confiança `MEDIA` nesse caso, o que contradizia a regra de que todo `CONFORME` exige evidência `ENCONTRADA` e dava nota cheia a controle visto pela metade.
- `IN-08` passa a tratar só de armazenamento de objetos e de arquivos enviados por usuários; a exposição de outros ativos é avaliada em `IN-09` e `IN-05`.
- Relatório de exemplo (`examples/saas-demo`) refeito: 109 itens, score 20. A queda vem da regra do item misto: `IN-02`, `SE-09` e `DS-11` saem do cálculo como `NAO_VERIFICADO`, e a área `infraestrutura` fica com cobertura baixa.

## [1.7.0] - 2026-10-05

Regras que dois testes de ponta a ponta mostraram depender de julgamento. Em cada teste, um agente sem contexto auditou o projeto de demonstração só com o que o instalador coloca nele. Com estas regras, duas auditorias sobre as mesmas evidências tendem ao mesmo status por item, e não só ao mesmo conjunto de itens.

### Adicionado
- Régua única de status, aplicada em ordem: controle inexistente; controle existente com a violação que ele deveria impedir; contagem dos elementos que o item enumera (todos, pelo menos a metade, menos da metade); cobertura incompleta. Vestígio que não cumpre a função do controle não conta, e documento em rascunho ou não publicado prova o conteúdo, não a vigência.
- Critério de decisão do tratamento de alto risco (Res. CD/ANPD nº 2/2022, art. 4º): critério específico e critério geral, com três situações verificáveis para "impacto significativo", larga escala nunca presumida e decisão conservadora na dúvida. Definição de "exposição explorável confirmada".
- Prazo máximo do achado pela severidade (`CRITICO` imediato, `ALTO` 30 dias, `MEDIO` 90, `BAIXO` 180); pode ser mais curto, nunca mais longo.
- `scripts/tests/run-all.sh`: roda localmente tudo o que o CI roda, para liberar commit, push e release sem esperar o GitHub Actions.

### Alterado
- Severidade do achado de item `PARCIAL`: sempre um nível abaixo da criticidade do item, sem escolha caso a caso. `scripts/validate-report.py` passa a conferir isso e o prazo máximo.
- Dado que revela informação sensível (art. 11, §1º) conta como sensível em todos os itens, e não só nas regras de operador; o agravante vale só quando a condição está no objeto que o item avalia.
- Aplicabilidade pelos fatos do tratamento, não pela documentação: os itens de consentimento valem quando o sistema coleta consentimento na prática ou quando o tratamento só pode se apoiar nele, ainda que nenhuma base legal esteja registrada.
- Limite entre `NAO_VERIFICADO` e `NAO_CONFORME`: controle sem representação em arquivo do repositório (proteção de branch, MFA do painel) é `NAO_VERIFICADO`; controle que costuma ser declarado em arquivo (varreduras no CI, cabeçalhos na configuração da hospedagem) e não está lá é `NAO_CONFORME`. Item com parte verificável e parte fora do alcance é avaliado pela parte verificável.
- Contagem única: critério para decidir quando um item depende de outro (não poderia ser atendido enquanto o outro controle continuar ausente).
- Fronteiras entre itens que se sobrepunham: `BL-01`, `BL-02` e `OP-02`; `CK-02`, `CK-03` e `CK-08`; `SE-02` e `IN-01`; `IN-06` e `IN-12`; e o que cabe ao cliente em `IN-09` e `IN-16` quando a hospedagem é PaaS. O texto de `IN-12` passa a dizer "além das nativas do provedor".
- Agravante de `SE-03` e `SE-05`: "falha explorável que permita ler ou extrair dados pessoais de terceiros", sem exigir exploração real nem incidente.
- Grau da evidência quando a análise encontra a violação: `AUSENTE` se nada do controle existe, `PARCIAL` se parte existe. Com mais de uma evidência, vale a confiança da mais fraca.
- Relatório de exemplo (`examples/saas-demo`) refeito com essas regras: score 25, com duas falhas que o relatório anterior não trazia — a rota pública de agendamento permite, a quem souber o CPF de um paciente, obter nome e data de nascimento e trocar os contatos dele (`SE-03`, `CRITICO`), e o projeto está fixado num runtime fora de suporte (`IN-16`).

## [1.6.1] - 2026-10-05

### Corrigido
Ajustes vindos do primeiro teste de ponta a ponta da v1.6.0 (auditoria feita só com o que o instalador coloca no projeto):
- Marca **classificação limitada por achado crítico**: o núcleo e a skill mandavam mostrá-la sempre que houvesse achado crítico, e o modelo HTML só quando o teto reduz a classificação. Vale a segunda regra nos três.
- Regra "ler só os arquivos de `files`" completada: `core/` vale sempre, `reports/html-report.md` e o modelo são usados quando há `.html`, e referência a módulo não ativado não precisa ser seguida.
- Relatório em `.md`: a célula `Item` do checklist passa a trazer `ID · criticality · control_type`, sem os quais o score não pode ser refeito, e o bloco "Contexto e escopo" antes da seção 1 fica previsto no formato.
- `GV-02` e `GV-11` deixam de poder contar a mesma falta: o texto diz qual dos dois vale em cada caso.
- `reports/html-report.md`: onde registrar a evidência de item `NAO_APLICAVEL` e de onde vem `framework_version`.
- Pasta do relatório fora do `.gitignore`: a auditoria avisa no resumo e não altera o arquivo.

### Alterado
- Comandos de instalação dos READMEs passam a baixar o instalador da última release (`releases/latest/download/`), e não mais da branch `main`: o script executado é o da mesma versão do framework que ele instala, e pode ser conferido com o `SHA256SUMS` da release.

## [1.6.0] - 2026-10-05

### Adicionado
- Catálogo de itens: os checklists dos módulos viram tabelas com ID fixo (ex.: `SE-03`), domínio, criticidade, agravante ou atenuante, tipo de controle e fundamento. A auditoria avalia todos os itens dos módulos ativos, e a criticidade deixa de ser escolhida caso a caso, o que torna o score reproduzível e permite comparar auditorias. Problema sem item correspondente entra como item extra (`EX-nn`).
- Catálogo da skill gerado a partir dos módulos (`scripts/update-skill-catalog.sh`), com conferência no CI: as duas formas passam a ter os mesmos itens e os mesmos pesos.
- Teto de classificação: com achado `CRITICO` aberto, a classificação não passa de `PARCIALMENTE_CONFORME`, qualquer que seja o score.
- Áreas de score `eca_digital` e `plataformas_digitais` (10% cada), aplicáveis só com os respectivos módulos ativos. As sete áreas anteriores mantêm a proporção entre si, então auditorias sem esses módulos chegam ao mesmo score de antes.
- Marca **escopo direcionado** nos relatórios de cenário diferente de `full_audit`, com a lista dos domínios não auditados.
- Campo `files` nos manifestos: cada módulo lista os arquivos que o compõem, e a auditoria lê só os dos módulos ativos.
- Novos itens de auditoria: segredos no histórico do git, permissões do pipeline, proteção de branch e dados reais em ambientes de teste (DevSecOps); TLS, declarações de privacidade nas lojas, eliminação de conta e backup do sistema (mobile); envenenamento de dados, isolamento de memória entre sessões, dado pessoal na saída do modelo, permissões de agentes, contrato com o provedor e transparência (IA/LLM); política de segurança e treinamento (governança).
- Modelos: registro das operações de tratamento (art. 37), teste de balanceamento do legítimo interesse, ato de indicação do encarregado e política de retenção.
- `scripts/validate-report.py`: confere um relatório contra o framework (seções, valores permitidos, IDs do catálogo, relação entre itens e achados e cálculo do score).
- `scripts/tests/test-framework.sh` e workflow `framework.yml`: catálogo, paridade mecânica entre a skill e o framework, cenários e módulos entre router, matriz, README e comandos, manifestos e data de sincronização.
- Workflow `release.yml`: ao publicar uma tag, envia `install.sh`, `install.ps1` e `SHA256SUMS` para a release. Workflow `attribution.yml`: reprova commit com assinatura de agente de IA.

### Alterado
- Pesos das áreas: `bases_legais` 12, `seguranca` 20, `direitos_titular` 12, `governanca` 12, `infraestrutura` 8, `apis_integracoes` 8, `ai_llm` 8, `eca_digital` 10 e `plataformas_digitais` 10. Os domínios 16 (ECA Digital) e 17 (plataformas digitais) saem de `governanca` para as áreas próprias.
- Área `NAO_APLICAVEL` passa a exigir evidência de que o objeto não existe; o cenário não ter ativado o módulo deixa de bastar.
- Gatilho do módulo `ai-llm`: qualquer chamada a provedor ou SDK de LLM ou de IA generativa, e não só embeddings, RAG ou fine-tuning. Os comandos `/lgpd-saas`, `/lgpd-web`, `/lgpd-mobile` e `/lgpd-devsecops` passam a citar o gatilho.
- Contagem única reescrita: o item pontua pelo que resta do seu requisito, fica `NAO_APLICAVEL` quando depende de um controle inexistente e é reprovado quando o requisito inteiro falha.
- Deveres gerais de provedor de aplicações (art. 16-A, I e II) avaliados só em `governance` (`GV-06` e `GV-07`), com o módulo `plataformas-digitais` ativo ou não.
- Arredondamento do score global definido: inteiro mais próximo, com 0,5 para cima.
- Modelos de política de privacidade, RIPD e DPA completados com o que o próprio checklist exige (forma e duração do tratamento, responsabilidades dos agentes, os direitos do art. 18, conteúdo mínimo do art. 38, instruções do controlador).
- Relatório de exemplo (`examples/saas-demo`) refeito com o catálogo completo: 108 itens, score 33.
- Workflows com `permissions: contents: read` e actions fixadas pelo hash do commit.

### Corrigido
- Instalador: falha ao consultar a última versão (sem rede ou limite da API do GitHub) não instala mais a branch `main` em silêncio. No modo interativo o instalador pergunta; com `--non-interactive`, para e pede `--version`.
- Skill: o "Modo de operação" passa a cobrir os 17 domínios; antes citava o domínio 17 e omitia ECA Digital, mobile, cookies, logs, governança, compartilhamento e retenção.

### Removido
- Regra "dados sensíveis elevam a cobertura para `full_audit`", que só existia na matriz de ativação e não era seguida pelo router, pelos comandos nem pela skill.
- Campo `score_partial` do `module_output`: o score é sempre por área, calculado pelo núcleo.

## [1.5.0] - 2026-10-03

### Adicionado
- Escolha do formato de saída: a auditoria pergunta sempre, logo no início, se o relatório deve ser gravado em `.md`, em `.md` e `.html`, ou só em `.html`; sem resposta, grava o `.md`.
- Relatório em HTML: a auditoria pode gravar um `.html` para leitura no navegador, com score e medidor, score por área, checklist e não conformidades com filtro e busca, plano por prazo, tema claro e escuro e versão para impressão ou PDF. É um arquivo único, offline, sem recursos externos.
- Modelo `reports/html-report-template.html` e especificação `reports/html-report.md`: a auditoria copia o modelo e preenche só um bloco de dados em JSON; o modelo recalcula o score a partir do checklist e alerta quando os números declarados não batem.
- Versão em HTML do relatório de exemplo (`examples/saas-demo/relatorio-auditoria-lgpd.html`) e imagem dele nos READMEs.
- Teste `scripts/tests/test-html-report.sh` e workflow `html-report.yml` (modelo preenchível e offline; exemplo em dia com o modelo), e `scripts/update-example-report.sh` para reaplicar o modelo ao exemplo.

### Alterado
- `core/reporting-engine.md`, a skill e os comandos passam a definir os arquivos gerados; quando os dois são gravados, têm o mesmo nome base e os mesmos dados, e em divergência vale o `.md`.
- Com arquivo gravado, a resposta em tela traz só o resumo (score, classificação, cobertura, não conformidades por severidade, "o que fazer agora" e o caminho dos arquivos), sem repetir o relatório inteiro.

## [1.4.0] - 2026-10-03

### Adicionado
- Aplicabilidade por item do checklist: `APLICAVEL`, `NAO_APLICAVEL` (objeto inexistente ou obrigação de outro agente) e `NAO_VERIFICADO` (fora do alcance do auditor), com tabela de itens fora do cálculo, indicador de cobertura, marca de **score parcial** quando a cobertura global fica abaixo de 80% e de **cobertura baixa** para área abaixo de 50% (#17).
- Mais de uma evidência por item, origem `TECNICA + DOCUMENTAL` e confiança da evidência (`ALTA | MEDIA | BAIXA`) no checklist, nos achados e no relatório; lista de verificações pendentes que podem alterar o score (#18).
- Papel do auditado em cada fluxo de dados (controlador, operador ou ambos), com as obrigações do operador (art. 39) e o que deixa de ser achado dele (#19).

### Alterado
- Gatilho do ECA Digital: bloqueio por idade ou data de nascimento autodeclarada não afasta a ativação do módulo quando há outro indício de acesso por menores (#20).
- Evidência no relatório passa ao formato `GRAU (ORIGEM), confiança NIVEL: descrição`.
- Relatório de exemplo (`examples/saas-demo`) refeito com as regras desta versão.

## [1.3.2] - 2026-10-03

### Corrigido
- Skill: os quatro exemplos de não conformidade registravam a evidência como `ENCONTRADA (TECNICA)`, contrariando a regra de que item `NAO_CONFORME` exige grau `PARCIAL` ou `AUSENTE`; passam a usar `AUSENTE (TECNICA)`.
- Regra de evidência explicitada na skill e em `core/evidence-engine.md`: o grau mede a comprovação do controle exigido, não a prova do problema.

## [1.3.1] - 2026-10-02

### Alterado
- Comandos (`commands/*.md`) com acentuação completa, inclusive nas descrições exibidas no menu dos assistentes, e citações legais padronizadas (`nº`, `§`).
- Títulos dos arquivos do framework em português (`Núcleo — …`, `Módulo X — …`, `Manifesto — …`, `Modelo — …`).

## [1.3.0] - 2026-10-02

Mudanças motivadas pelo primeiro uso em projeto real e pela preparação para o lançamento público.

### Adicionado
- Cálculo do score fechado e reproduzível: `CONFORME` = 1, `PARCIAL` = 0,5, `NAO_CONFORME` = 0, com peso do item pela criticidade (4/3/2/1) (#4).
- Mapa de áreas por domínio: cada item do checklist pontua em uma única área; novos campos `score_area`, `criticality` e `control_type` no `check_item` (#5).
- Modulação de severidade por porte e exposição (Res. CD/ANPD nº 2/2022), limitada a um nível e vedada nos casos graves (#6).
- Score técnico e score documental, informativos, ao lado do score global (#7).
- Natureza do agente de tratamento como entrada inicial obrigatória do router, dos comandos e da skill (#8).
- Dados de acesso público e manifestamente públicos (art. 7º, §§ 3º, 4º e 7º), incluindo dado sensível divulgado por órgão oficial (#9).
- Registro de risco aceito no achado (quem, quando, justificativa e revisão), sem efeito no score (#11).
- Relatório: "o que fazer agora" com esforço `P | M | G`, coluna `Área` no checklist, glossário, aviso legal fixo e marcação de confidencialidade (#12, #13, #15).
- Exemplo público em `examples/saas-demo/`: SaaS fictício com falhas propositais e relatório completo (#16).
- Arquivos de comunidade: `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, modelos de issue (bug, atualização normativa, melhoria) e de PR (#16).

### Alterado
- Antes de perguntar, a auditoria lê o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, README, `docs/`) e pergunta só o que falta (#14).
- Módulo de cloud generalizado para PaaS e hospedagem compartilhada, com validação das respostas de produção; `cloud/aws-audit.md` passa a ser `cloud/cloud-audit.md` (#10).
- Regras de consistência apontadas ao gerar o exemplo: itens `PARCIAL` também geram achado (severidade da lacuna, limitada à criticidade); contagem única de uma mesma falha; precedência da regra de severidade mais específica; transferência internacional distingue mecanismo comprovadamente ausente (`CRITICO`) de não evidenciado (`ALTO`); dispensa de encarregado e registro simplificado não valem para pequeno porte com tratamento de alto risco; severidade explícita para encarregado/RIPD, resposta a incidentes e DPA com operadores; `IMEDIATO` definido como até 7 dias.
- `README.md` passa a ser em português (canônico) e a versão em inglês vai para `README.en.md`, com resumo do produto, badges, link para o exemplo e aviso legal (#15, #16).

## [1.2.0] - 2026-10-02

### Adicionado
- `CHANGELOG.md` e verificação de versão única (`scripts/tests/test-versions.sh` e workflow `versions.yml`): `SKILL.md`, `commands/*.md`, changelog e tag precisam ter a mesma versão.
- Framework modular com as verificações da skill que faltavam:
  - `appsec`: HTTPS/HSTS/CSP, segregação e trilha de auditoria no backend, JWT/OAuth com escopos mínimos, exposição excessiva de dados, inventário de APIs públicas, API keys fora do código e criptografia em trânsito;
  - `cloud`: criptografia em repouso, backups e réplicas, WAF, IDS/IPS e SIEM;
  - `mobile`: detecção de jailbreak/root e validação de deep links;
  - `devsecops`: varredura de infraestrutura como código (IaC);
  - `governance`: retenção e eliminação (arts. 15 e 16), com eliminação automática, descarte seguro e retenções legais.
- Orientação para incluir `.lgpd-auditor-backup/` no `.gitignore`, nos instaladores e nos READMEs.

### Alterado
- Checklist de paridade entre a skill e o framework verificado item a item (39 de 39), com data da verificação.
- Definição de dado sensível completa, igual ao art. 5º, II ("quando vinculado a uma pessoa natural"), na skill e no framework.
- Adequação da União Europeia (Res. CD/ANPD nº 32/2026) com a ressalva de que dispensa apenas o mecanismo do art. 33, também na skill, no template de DPA e em `anpd-guidelines.md`.
- Skill: base correta da vedação à autodeclaração de idade, os três cortes etários sem unificação, art. 7º, §1º do Decreto nº 12.976/2026, arts. 16-I e 16-P, e exemplos com evidência e fundamento.
- Relatórios por público (`reports/`) passam a remeter ao relatório canônico; normas em monitoramento ficam só em `recomendacoes_tecnicas`.
- `ai-llm`: rotulagem de conteúdo sintético movida para "Em monitoramento"; orientações preliminares da ANPD no `eca-digital` marcadas como não vinculantes.
- README do framework lista os cenários `web_site` e `full_audit`; evidências de teste esperadas incluem `digital_platform`.
- Instaladores: a pergunta do assistente passa a ser "Instalar também a skill?", com o mesmo texto na ajuda de `--with-skill` / `-WithSkill`.
- Terminologia unificada: o projeto deixa de usar designações de versão, "legado" e "monolítica" para suas partes e passa a falar em skill (`SKILL.md`) e framework modular (`.agents/lgpd-enterprise-auditor/`), inclusive na descrição do comando `lgpd-full-audit`, nos títulos dos arquivos e nos READMEs.

### Removido
- Pasta `legacy/` do framework: a cobertura do `full_audit` passa a ficar em `orchestrator/full-audit.md`; a matriz de rastreabilidade foi renomeada para `validation/traceability-matrix.md`.

### Corrigido
- `commands/lgpd-plataformas-digitais.md` estava na versão `1.0.0`; alinhado em `1.1.0`.

## [1.1.0] - 2026-10-02

### Adicionado
- Instalador interativo por projeto: `scripts/install.sh` (macOS, Linux, WSL, Git Bash) e `scripts/install.ps1` (Windows PowerShell 5.1 e PowerShell 7), com as ações `install`, `update`, `uninstall` e `check`, modo `--non-interactive` e manifesto por ferramenta em `.agents/lgpd-enterprise-auditor/.install/`.
- Ferramentas suportadas pelo instalador: `claude`, `cursor`, `vscode`, `opencode` e `agents` (Codex, Gemini CLI e similares); a skill é opcional, exceto em `agents`.
- Testes de regressão dos dois instaladores (`scripts/tests/`) e CI no Ubuntu, no macOS (`/bin/bash` 3.2) e no Windows (PowerShell 7 e 5.1).
- Frontmatter YAML no `SKILL.md` (`name`, `description`, `license`, `metadata`), permitindo instalá-lo como skill.
- Módulo `plataformas-digitais` (Decretos nº 12.975/2026 e nº 12.976/2026): `legal/plataformas-digitais.md`, manifesto, cenário `digital_platform`, gatilho normativo no router, domínio 17 da skill e comando `lgpd-plataformas-digitais`.
- Módulo `eca-digital` (Lei nº 15.211/2025) com templates de relatório semestral de transparência e checklist de aferição de idade.
- Comando `lgpd-web` e cenário `web_site` para sites e landing pages.
- Regra de área `NAO_APLICAVEL` com redistribuição proporcional dos pesos do score (skill e framework).
- Checklists de consentimento (art. 8º), transparência (art. 9º), prazos de atendimento ao titular (art. 19), registro das operações (art. 37, com forma simplificada para pequeno porte), cookies e tracking, e dados pessoais em logs.

### Alterado
- Evidência classificada em dois eixos independentes: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`), na skill e no framework.
- Base normativa atualizada com as resoluções da ANPD e a Lei nº 15.352/2026 (ANPD como Agência); itens com prazo revisados.
- READMEs com seção de instalação; a documentação do `full_audit` aponta para os locais de instalação da skill.

## [1.0.0] - 2026-05-15

### Adicionado
- Versão inicial: skill autocontida (`SKILL.md`) e framework modular em `.agents/lgpd-enterprise-auditor/` (contratos do core, módulos especialistas, orquestrador por cenário, relatórios, templates e validação de paridade).
- Comandos `lgpd-full-audit`, `lgpd-saas`, `lgpd-mobile`, `lgpd-ai-llm` e `lgpd-devsecops`.
- READMEs em inglês e português e licença MIT.

[Não lançado]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.8.1...HEAD
[1.8.1]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.8.0...v1.8.1
[1.8.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.7.0...v1.8.0
[1.7.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.6.1...v1.7.0
[1.6.1]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.6.0...v1.6.1
[1.6.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.3.2...v1.4.0
[1.3.2]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.3.1...v1.3.2
[1.3.1]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.3.0...v1.3.1
[1.3.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/releases/tag/v1.1.0
[1.0.0]: https://github.com/BrunoLagoa/lgpd-enterprise-auditor/commit/8e4f21b
