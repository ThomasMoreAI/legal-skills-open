# Roteador de módulos

## Objetivo
Ativar apenas módulos relevantes ao contexto do projeto, preservando cobertura completa no modo `full_audit`.

## Levantamento de contexto
Antes de perguntar, ler o que o projeto já documenta: `CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependência (`package.json`, `requirements.txt`, `pubspec.yaml` etc.) e arquivos de infraestrutura e CI. Apresentar o contexto inferido, pedir confirmação e perguntar só o que faltar. As entradas abaixo são obrigatórias; as que não puderem ser inferidas com segurança devem ser perguntadas logo no início. Na mesma rodada, perguntar sempre o formato de saída do relatório (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `core/reporting-engine.md`, salvo se o pedido já disser.

## Arquivos de cada módulo
Cada manifesto em `orchestrator/manifests/` lista em `files` os arquivos do módulo. Ler os arquivos dos módulos ativos e só eles: a pasta `legal/` guarda três módulos (`legal`, `eca-digital` e `plataformas-digitais`), e ler a pasta inteira traz para a auditoria regras de módulos que não foram ativados. Além deles: os arquivos de `core/` valem sempre; `reports/html-report.md` e o modelo `reports/html-report-template.html` são usados quando o formato escolhido inclui o `.html`; os modelos de `templates/` são lidos quando um item os cita. Uma referência entre colchetes duplos a arquivo de módulo que não foi ativado não precisa ser seguida: a linha do item no catálogo traz o requisito e o fundamento por inteiro (é o caso de `GV-06`, `GV-07` e `IN-04`, que citam [[plataformas-digitais]]).

## Entradas mínimas
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e existência de tratamento de alto risco — define se há modulação de severidade (`core/severity-model.md`), se valem a forma simplificada do registro e a dispensa de indicação do encarregado, se o serviço é provedor de aplicações sujeito ao MCI art. 15 e se a LGPD se aplica (art. 4º, I);
- papel do auditado em cada fluxo de dados: **controlador**, **operador** ou ambos (ex.: um SaaS B2B costuma ser operador dos dados que seus clientes inserem e controlador dos dados das contas e de cobrança) — define quais obrigações são dele e quais ficam `NAO_APLICAVEL` (`legal/legal-bases-engine.md`);
- stack (frontend/backend/mobile);
- cloud provider, PaaS ou hospedagem (ex.: AWS, Vercel, hospedagem compartilhada);
- integrações de terceiros;
- presença de IA/LLM;
- maturidade de DevSecOps;
- faixa etária do público: serviço direcionado a menores, de acesso provável por eles ou com cadastro sem bloqueio etário (insumo do gatilho normativo de `eca-digital`).

## Regras de ativação

### Regra global
`core` e `legal` são sempre obrigatórios.

### Cenários base
- `saas_web`: `core`, `legal`, `governance`, `appsec`, `cloud`, `devsecops`.
- `web_site`: `core`, `legal`, `governance`, `appsec`, `cloud`.
- `mobile_app`: `core`, `legal`, `governance`, `mobile`, `appsec`, `cloud`.
- `ai_llm_system`: `core`, `legal`, `governance`, `ai-llm`, `appsec`.
- `devsecops_pipeline`: `core`, `legal`, `devsecops`, `cloud`, `appsec`.
- `eca_digital_platform`: `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.
- `digital_platform`: `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.

### Gatilhos técnicos adicionais
- Se usar `Firebase` ou storage cloud, adicionar `cloud`.
- Se houver API pública, adicionar `appsec`.
- Se houver chamada a provedor ou SDK de LLM ou de IA generativa (ex.: OpenAI, Anthropic, Google), modelo próprio, embeddings, RAG, banco vetorial ou fine-tuning, adicionar `ai-llm`.
- Se houver app iOS/Android (nativo, Flutter, React Native), adicionar `mobile`.
- Se houver Kubernetes ou CI/CD ativo, adicionar `devsecops`.

### Gatilho normativo — público infantojuvenil
Adicionar `eca-digital` a **qualquer** cenário quando houver indício de usuários menores de 18 anos:
- serviço direcionado a crianças ou adolescentes;
- serviço provavelmente acessado por menores (rede social, vídeo, jogo, mensageria, fórum, marketplace);
- cadastro que aceite ou não bloqueie usuários menores de 18 anos;
- jogos eletrônicos, itens virtuais pagos ou monetização por engajamento;
- app classificado para faixa etária inferior a 18 anos nas lojas.

Bloqueio etário baseado só em idade ou data de nascimento **autodeclarada não afasta** o gatilho quando houver qualquer outro indício desta lista: a autodeclaração isolada é insuficiente (arts. 10, 12 e 14 do ECA Digital; LGPD art. 14, §5º). Sem nenhum outro indício (ex.: serviço B2B ou profissional, sem atrativo para menores), o módulo não é ativado e a decisão vai para o escopo excluído, com a justificativa.

Esse gatilho é **normativo, não técnico**: na dúvida sobre a presença de menores, ativar o módulo e registrar a incerteza como evidência `PARCIAL`.

### Gatilho normativo — plataformas digitais
Adicionar `plataformas-digitais` a **qualquer** cenário quando o auditado for provedor de aplicações de internet que:
- intermedeie conteúdo gerado por terceiros com difusão pública (rede social, vídeo, fórum, comentários públicos, marketplace com anúncios de usuários, grupos abertos);
- ofereça, mediante pagamento, ferramentas de anúncio ou impulsionamento de conteúdo;
- disponibilize IA ou recurso equivalente capaz de gerar ou alterar imagem ou som de pessoas.

Serviços exclusivamente de e-mail, mensageria interpessoal ou videoconferência restrita estão fora dos arts. 16-B a 16-J (art. 16-O do Decreto nº 8.771/2016). Mesmo sem o módulo ativo, os deveres gerais do art. 16-A e a guarda de registros de acesso (MCI art. 15) são verificados por `governance` e `cloud` em todo provedor de aplicações.

## Auditoria completa
`full_audit` ativa todos os módulos (cobertura em `orchestrator/full-audit.md`):
`core`, `legal`, `eca-digital`, `plataformas-digitais`, `governance`, `cloud`, `appsec`, `mobile`, `devsecops`, `ai-llm`.

## Saída do roteador
- lista de módulos ativos;
- justificativa de ativação por módulo;
- escopo excluído explicitamente: cada módulo não acionado, com a evidência de que o objeto dele não existe (o que permite marcar a área como `NAO_APLICAVEL`) ou a indicação de que ficou fora do escopo mesmo existindo (a área fica com cobertura insuficiente, sem virar não aplicável — `core/scoring-engine.md`);
- domínios fora do escopo do cenário, para a marca **escopo direcionado** do relatório.

## Convenção de nomes
- O roteador ativa módulos por ID de módulo (kebab-case), ex.: `ai-llm`.
- O cálculo de score usa IDs de área (snake_case), ex.: `ai_llm`.
