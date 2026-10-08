# LGPD Auditor Skill

Skill open-source para auditoria técnica de riscos de LGPD em SaaS, microSaaS, sistemas web, APIs e produtos digitais. Funciona como uma camada de revisão para agentes de IA, como Claude Code, ajudando times pequenos a encontrar pontos cegos de privacidade, segurança e produto antes do código entrar em produção.

A skill foca em achados acionáveis por arquivo e linha, classificados por severidade, separando claramente o que é correção técnica, o que é requisito de produto e o que é dúvida jurídica que precisa de revisão humana.

---

## Sobre o projeto

O nome do repositório é lgpd-auditor-skill. A pasta instalável da skill se chama lgpd-auditor.

A proposta é simples: a maior parte dos times brasileiros que lançam SaaS, microSaaS e ferramentas internas não tem um DPO dedicado, não tem orçamento para uma auditoria formal e ainda assim precisa lidar com dados pessoais de usuários, clientes e parceiros. Essa skill organiza um conjunto de verificações técnicas, operacionais e de produto que ajudam a antecipar problemas comuns: vazamento por log, ausência de exclusão de conta, multi-tenant mal isolado, banner de cookies decorativo, prompt de IA recebendo PII sem necessidade, política pública desalinhada do código, entre outros.

Ela foi escrita para ser usada em conjunto com o agente, lendo o código real do projeto, e não para gerar diagnósticos genéricos.

---

## Para quem é

Este projeto foi pensado para:

- Desenvolvedores independentes que mantêm produtos sozinhos.
- Founders técnicos lançando o primeiro SaaS ou microSaaS.
- Software houses e agências que entregam projetos para clientes.
- Times pequenos de produto e engenharia.
- Startups brasileiras em fase de pré-seed, seed ou bootstrapping.
- Projetos que tratam dados pessoais e ainda não têm um processo formal de privacidade.
- Times que querem rodar uma revisão antes de cada release importante.

Se a sua empresa já tem uma área jurídica madura, um DPO interno e um programa de privacidade estruturado, esta skill pode complementar o trabalho, mas não substitui a estrutura existente.

---

## O que a skill analisa

A skill cobre uma matriz ampla de controles técnicos e operacionais. Os pontos principais são:

Coleta de dados pessoais

- Mapeamento de PII comum, dados sensíveis, dados financeiros, dados de autenticação e dados de menores.
- Identificação de campos coletados sem finalidade clara.
- Verificação de minimização.

Tratamento e finalidade

- Cada fluxo é analisado quanto a finalidade declarada e uso real do dado.
- Reuso de dado para marketing, IA ou analytics sem transparência é sinalizado.

Bases legais

- Verificação se a base legal candidata é coerente com a finalidade.
- Sinalização de uso genérico de legítimo interesse ou consentimento.

Consentimento

- Granularidade, especificidade, revogabilidade e registro da escolha.
- Telas de cadastro, banners e fluxos de opt-in.

Cookies

- Classificação entre essenciais, funcionais, analytics e marketing.
- Verificação de Secure, HttpOnly, SameSite e escopo.
- Banners que apenas informam mas não controlam nada.

Analytics

- Disparo de scripts antes do consentimento quando aplicável.
- Identificação de usuário por e-mail, CPF ou outro dado pessoal sem necessidade.

Logs

- Dados pessoais, tokens, headers de Authorization, payloads de webhook e prompts de IA em log.
- Redação e mascaramento.

Autenticação, sessões e permissões

- Hash de senha, expiração de token, refresh, CSRF, cookies de sessão, rate limit em login e reset.

RBAC e multi-tenant

- Verificação de isolamento por userId, tenantId ou equivalente em todas as consultas.
- Endpoints de admin separados, auditados e com role check.

Banco de dados

- Migrations, índices, retenção por tabela, soft delete consciente, segredos fora do repositório.

Retenção e descarte

- Política de retenção por categoria, jobs de limpeza, anonimização irreversível.

Exportação e exclusão de dados

- Validação de identidade, escopo correto, tratamento de dados que não podem ser apagados por obrigação legal.

Integrações externas

- Inventário de operadores e suboperadores: hospedagem, banco, pagamentos, e-mail, analytics, observabilidade, IA, storage, Open Finance.

Pagamentos e webhooks

- Assinatura, idempotência, sem payload sensível em log.

E-mails transacionais

- Conteúdo, dados expostos, provedor utilizado, links assinados.

Uso de IA e LLMs

- Minimização do prompt, transparência, retenção pelo provedor, treinamento, revisão humana em decisões relevantes.

Políticas públicas

- Política de privacidade e termos de uso comparados com o código real.

Resposta a incidentes

- Runbook, contatos, severidade, preservação de evidências e processo de comunicação.

Requisitos funcionais de privacidade

- A skill aponta funcionalidades que faltam no produto, não apenas falhas no código existente.

A matriz completa fica em references/lgpd-control-matrix.md.

---

## O que a skill não faz

É importante deixar claro o que está fora do escopo:

- Não garante conformidade total com a LGPD.
- Não substitui análise jurídica.
- Não substitui o trabalho de um DPO ou encarregado de dados.
- Não envia documentos para a ANPD.
- Não emite parecer legal.
- Não deve ser usada como única fonte de decisão em situações jurídicas concretas.
- Não resolve compliance sozinha.
- Não atualiza automaticamente quando a ANPD publica novas resoluções.

A skill identifica riscos técnicos, lacunas de produto e pontos que precisam de revisão. Toda interpretação legal deve ser validada com profissionais qualificados e fontes oficiais.

---

## Instalação no Claude Code

A skill pode ser instalada de forma global, disponível para todos os seus projetos, ou local, ficando restrita a um único repositório.

Estrutura esperada após a instalação:

Global

    ~/.claude/skills/lgpd-auditor/SKILL.md
    ~/.claude/skills/lgpd-auditor/references/
    ~/.claude/skills/lgpd-auditor/templates/
    ~/.claude/skills/lgpd-auditor/scripts/

Por projeto

    .claude/skills/lgpd-auditor/SKILL.md
    .claude/skills/lgpd-auditor/references/
    .claude/skills/lgpd-auditor/templates/
    .claude/skills/lgpd-auditor/scripts/

Observe que o repositório se chama lgpd-auditor-skill, mas a pasta instalada precisa se chamar lgpd-auditor para o Claude Code reconhecer a skill.

Instalação global em Linux ou macOS

    git clone https://github.com/mairinkdev/lgpd-auditor-skill.git
    mkdir -p ~/.claude/skills/lgpd-auditor
    cp -R lgpd-auditor-skill/* ~/.claude/skills/lgpd-auditor/
    chmod +x ~/.claude/skills/lgpd-auditor/scripts/lgpd_scan.sh

Instalação por projeto em Linux ou macOS

    mkdir -p .claude/skills/lgpd-auditor
    cp -R lgpd-auditor-skill/* .claude/skills/lgpd-auditor/
    chmod +x .claude/skills/lgpd-auditor/scripts/lgpd_scan.sh

Instalação no Windows com PowerShell

    git clone https://github.com/mairinkdev/lgpd-auditor-skill.git
    New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills\lgpd-auditor"
    Copy-Item -Recurse -Force lgpd-auditor-skill\* "$env:USERPROFILE\.claude\skills\lgpd-auditor\"

Depois de copiar os arquivos, reinicie o Claude Code para que a skill seja indexada.

---

## Como usar

A skill é acionada por comandos diretos no Claude Code. Os modos disponíveis são:

Auditoria rápida

    /lgpd-auditor auditoria-rapida

Faz uma varredura inicial focando em riscos óbvios: PII em log, falta de autenticação, segredos expostos, multi-tenant frágil, ausência de exclusão de conta.

Auditoria completa

    /lgpd-auditor auditoria-completa

Gera um diagnóstico técnico, funcional e operacional usando a matriz completa de controles. Indicada antes de lançamentos relevantes.

Revisão de diff antes de deploy

    /lgpd-auditor diff

Lê o git diff atual e foca apenas no que foi alterado, dando atenção a auth, pagamentos, analytics, IA, logs, migrations e políticas públicas.

Revisão de uma feature nova

    /lgpd-auditor feature "nova integração com pagamentos"
    /lgpd-auditor feature "cadastro de paciente com upload de exame"
    /lgpd-auditor feature "chat de suporte com IA"

Avalia uma feature específica antes ou depois da implementação, exigindo minimização e checando base legal candidata, consentimento e transparência.

Revisão de políticas públicas

    /lgpd-auditor politicas

Compara a política de privacidade, os termos de uso e o aviso de cookies com o comportamento real do código, apontando promessas que o sistema não cumpre e lacunas de transparência.

Você também pode passar um caminho opcional para limitar o escopo:

    /lgpd-auditor auditoria-rapida apps/web
    /lgpd-auditor feature "exportar dados do usuário" apps/api/src/users

---

## Estrutura do projeto

A árvore do repositório segue o padrão das skills do Claude Code:

    lgpd-auditor-skill/
        README.md
        SKILL.md
        references/
            lgpd-control-matrix.md
        templates/
            relatorio-lgpd.md
            plano-correcao.md
        scripts/
            lgpd_scan.sh

SKILL.md contém o prompt principal da skill, regras de severidade, procedimento por tipo de tarefa, padrões de busca e formato de saída.

A pasta references guarda materiais que a skill carrega apenas quando precisa de profundidade, como a matriz completa de controles.

A pasta templates contém o template de relatório final e o template do plano de correção.

A pasta scripts contém um shell script opcional de varredura estática que pode ser executado fora da skill para gerar um relatório inicial de padrões suspeitos.

---

## Exemplo de saída esperada

A skill devolve sempre um relatório com a mesma estrutura. Um exemplo resumido fica assim:

Veredito

Bloqueado para produção.

Escopo analisado

apps/web, apps/api, prisma/schema.prisma, política de privacidade pública, banner de cookies, integração com Stripe e PostHog.

Resumo executivo

- Token de sessão sendo gravado em localStorage no frontend.
- Webhook do Stripe sem verificação de assinatura.
- Rota de exclusão de conta sem checagem do dono do recurso.
- Logs do backend imprimindo o objeto completo do usuário, incluindo e-mail e CPF.
- PostHog identificando usuários por e-mail antes do consentimento.
- Política de privacidade não menciona Stripe, PostHog e Resend.

Achados P0

- ID P0-001, em apps/api/src/users/delete.ts linha 42, exclusão de conta sem checar userId do solicitante. Risco direto de exclusão indevida de contas alheias.
- ID P0-002, em apps/api/src/webhooks/stripe.ts linha 18, webhook aceito sem validação de assinatura. Permite forjar eventos de pagamento.

Achados P1

- ID P1-001, em apps/web/src/lib/auth.ts linha 27, token de sessão em localStorage. Substituir por cookie HttpOnly e Secure.
- ID P1-002, em apps/api/src/lib/logger.ts linha 12, falta de redação de campos sensíveis em produção.

Arquivos afetados

apps/api/src/users/delete.ts, apps/api/src/webhooks/stripe.ts, apps/web/src/lib/auth.ts, apps/api/src/lib/logger.ts, public/privacy.md.

Impacto e recomendação técnica

Cada achado vem com a evidência, o risco em termos de LGPD, a correção sugerida e o teste recomendado.

Requisitos funcionais faltantes

- Tela de exportação de dados do usuário.
- Tela de gestão de consentimento de cookies.
- Página pública listando operadores e suboperadores.

Pontos para revisão jurídica

- Validar base legal para retenção de comprovantes de pagamento após exclusão da conta.
- Validar texto do banner de cookies com o jurídico.
- Avaliar necessidade de RIPD para a integração de IA.

Checklist de release

A skill devolve também o checklist mínimo para liberar o sistema em beta fechado ou produção, conforme o caso.

O template completo está em templates/relatorio-lgpd.md e o plano de correção em templates/plano-correcao.md.

---

## Boas práticas recomendadas

Algumas orientações que ajudam a tirar o máximo da skill no dia a dia:

- Rode a skill antes de deploys importantes, principalmente os que envolvem auth, pagamentos, integrações novas ou mudanças em coleta de dados.
- Rode a skill sempre que criar uma feature que coleta, transforma ou compartilha dados pessoais.
- Rode a skill ao adicionar qualquer integração externa, especialmente as que recebem PII ou dados financeiros.
- Revise cookies e analytics em intervalos regulares, não apenas na primeira implementação.
- Revise logs periodicamente. É comum aparecerem novos pontos de vazamento conforme o produto evolui.
- Mantenha a política de privacidade, os termos de uso e o aviso de cookies atualizados em relação ao comportamento real do sistema.
- Sempre valide achados jurídicos com fontes oficiais e profissionais qualificados.
- Documente decisões de privacidade no próprio repositório, em arquivos de ADR ou notas técnicas, para facilitar futuras auditorias.
- Trate falsos positivos do scanner como oportunidade para melhorar a busca, não para silenciar o alerta.

---

## Fontes oficiais recomendadas

Toda interpretação legal mencionada pela skill deve ser confirmada nas fontes oficiais. As referências mais úteis são:

- Lei Geral de Proteção de Dados consolidada no portal do Planalto: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Site oficial da Autoridade Nacional de Proteção de Dados: https://www.gov.br/anpd/pt-br
- Materiais educativos e publicações da ANPD: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes
- Regulamentações vigentes da ANPD: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd
- Página oficial sobre comunicação de incidentes de segurança: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis

Recomenda-se também acompanhar guias publicados pela ANPD sobre temas específicos como cookies, legítimo interesse, encarregado, segurança da informação e agentes de tratamento de pequeno porte, conforme estiverem disponíveis no momento da consulta.

Datas, prazos, sanções e obrigações específicas mudam com o tempo. Sempre consulte a fonte oficial atualizada antes de tomar decisões.

---

## Roadmap

Direções que estão no horizonte do projeto:

- Melhorar exemplos de relatórios reais anonimizados.
- Adicionar mais templates de auditoria para cenários específicos.
- Criar um modo focado em SaaS financeiro e Open Finance.
- Criar um modo focado em produtos de saúde digital.
- Criar um modo focado em educação e plataformas com público infanto-juvenil.
- Criar checklist específico para uso de IA e LLMs em produto.
- Criar checklist específico para marketplaces e relacionamento controlador/operador.
- Melhorar o script de varredura estática.
- Adicionar exemplos reais anonimizados, com antes e depois.
- Documentar uso da skill com outras ferramentas de agente além do Claude Code.
- Internacionalização opcional, mantendo o foco principal em português do Brasil.

Sugestões de novos itens de roadmap são bem-vindas via issue.

---

## Contribuição

Contribuições são bem-vindas. Algumas formas de ajudar:

- Abrir issue descrevendo problemas, dúvidas ou sugestões.
- Sugerir melhorias na matriz de controles.
- Enviar pull request com correções, novos templates ou novos modos.
- Propor novos controles relevantes para realidades específicas.
- Corrigir referências e links de fontes oficiais.
- Melhorar a clareza dos templates de relatório e plano de correção.
- Reportar problemas de execução em diferentes sistemas operacionais.

Antes de abrir um pull request grande, vale abrir uma issue para alinhar a direção.

---

## Segurança e privacidade nas contribuições

Por favor, ao abrir issues, pull requests ou discussões públicas, não compartilhe:

- Dados pessoais de clientes, funcionários ou terceiros.
- Chaves de API, tokens, senhas ou segredos.
- URLs internas sensíveis.
- Dumps de banco de dados.
- Logs com dados reais.
- Conteúdo de prompts ou respostas com PII.
- Documentos internos confidenciais.

Se precisar reportar uma vulnerabilidade ou um risco sensível, prefira contato privado com o mantenedor antes de abrir uma issue pública.

---

## Aviso importante

Esta skill é uma ferramenta auxiliar de auditoria técnica. Ela ajuda a identificar riscos, lacunas e pontos que merecem revisão, mas não emite parecer jurídico, não substitui o trabalho de advogados, encarregados ou DPOs, e não garante conformidade legal com a LGPD ou com qualquer outra norma aplicável.

Todas as interpretações legais devem ser validadas com fontes oficiais e com profissionais qualificados. Decisões de produto, engenharia e jurídicas são responsabilidade dos times que usam a skill.

---

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
