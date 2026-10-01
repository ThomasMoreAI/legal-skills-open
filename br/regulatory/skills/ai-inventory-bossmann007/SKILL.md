---
name: ai-inventory-bossmann007
title: /ai-inventory
description: Inventário de sistemas de IA por sistema (framework brasileiro) — rastreia o papel de cada sistema (fornecedor/desenvolvedor, operador/implementador, distribuidor) e o nível de risco (risco excessivo/proibido, alto risco, risco geral) sob o PL 2338/2023 e a sobreposição da LGPD (Art. 20 — decisão automatizada). Papel e nível são avaliados por sistema, não por empresa. Use quando o usuário disser "inventário de IA", "adicionar sistema de IA", "que sistemas temos", "classificar este sistema de IA", "registro do PL 2338" ou "registro de sistemas de IA".
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/ai-governance-legal/skills/ai-inventory
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: regulatory
language: pt
---

# /ai-inventory

## Quando isso roda

O usuário quer gerenciar o inventário de sistemas de IA sob o marco legal
brasileiro. A ideia central que a skill existe para reforçar: **papel e
nível de risco são por sistema, não por empresa.** A mesma organização pode
ser *fornecedora/desenvolvedora* do Sistema A, *operadora/implementadora* do
Sistema B. Cada combinação aciona um conjunto diferente de obrigações. O
inventário existe para que essas avaliações fiquem rastreáveis — as
obrigações em si são derivadas em conversa, não de uma tabela fixa.

**Contexto regulatório (verificar status atual a cada uso):**
- **PL 2338/2023** — aprovado no Senado em dezembro/2024, em tramitação na
  Câmara dos Deputados `[verificar status atual — pode ter sido sancionado,
  alterado, ou ainda pendente]`. Estrutura por níveis de risco (excessivo/
  proibido, alto risco, risco geral), inspirada no AI Act europeu mas com
  texto próprio — não presuma equivalência 1:1 de artigo.
- **LGPD (Lei 13.709/2018), Art. 20** — já em vigor, independe do PL 2338.
  Direito do titular a revisão de decisões tomadas unicamente com base em
  tratamento automatizado que afetem seus interesses, incluindo decisões
  destinadas a definir perfil pessoal, profissional, de consumo e de
  crédito. Aplica-se a QUALQUER sistema de decisão automatizada hoje,
  independentemente do PL 2338 ter sido sancionado.
- **Regulação setorial já vigente:** Resolução CMN/BCB nº 4.658 e correlatas
  (gestão de risco em instituições financeiras, inclui modelos de crédito/
  scoring); RDC Anvisa nº 657/2022 (software como dispositivo médico —
  SaMD, cobre triagem/diagnóstico assistido por IA); normas CVM para
  consultoria automatizada de investimentos (robo-advisors).
- **ABNT NBR ISO/IEC 42001** — norma técnica de sistema de gestão de IA,
  referência de boas práticas mesmo sem força de lei.

## O que fazer

1. **Leia a configuração.** Leia
   `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.
   Se não existir ou ainda tiver marcadores `[PLACEHOLDER]`, direcione o
   usuário para `/ai-governance-legal:cold-start-interview` primeiro.

2. **Leia o inventário.** Fica em
   `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/ai-systems.yaml`.
   Se não existir, crie com uma lista `systems:` vazia quando o primeiro
   `add` rodar.

3. **Dispatch pelo argumento:**

   - Sem argumento, ou `list` → mostra a tabela do inventário (ver **Listar** abaixo).
   - `add` → roda o fluxo **Adicionar**.
   - `edit <id>` → mostra o registro atual, pergunta o que mudar, atualiza
     um campo, confirma, grava.
   - `classify <id>` → roda o **Roteiro de classificação** num registro
     existente, atualizando role, tier, role_basis e tier_basis.
   - `show <id>` → mostra o registro completo.

4. **No list, ofereça o dashboard:**
   "Quer o dashboard completo? Filtro por status / nível / vínculo com o
   Brasil / responsável. É só falar."

5. **Feche toda ação com um gancho para o trabalho do advogado.**
   Depois de qualquer gravação, diga:
   > Registrado. Quando quiser percorrer as obrigações deste sistema, é só
   > pedir — eu faço em conversa e sinalizo onde o mapeamento do PL
   > 2338/2023 (ou da regulação setorial) precisa da sua verificação. Não
   > derivo obrigações de uma tabela porque o mapeamento é complexo e o PL
   > ainda está mudando.

## Formato de listagem

Renderize como tabela compacta:

| ID | Nome | Responsável | Status | Vínculo BR | Papel | Nível | Próxima revisão |
|----|------|-------------|--------|------------|-------|-------|------------------|
| sys-001 | Triagem de currículos | RH / Jamie | em_produção | sim | operador | alto_risco | 2026-08-01 |
| sys-002 | Assistente de redação de e-mail | TI / Priya | em_produção | não | operador | risco_geral | 2026-12-01 |

Abaixo da tabela, mostre contagem por nível e uma linha: "N sistemas
sinalizados para revisão nos próximos 30 dias."

## Fluxo de adição (entrevista)

Pergunte um campo por vez (ou aceite colar tudo de uma vez). Os campos
obrigatórios são `name`, `owner`, `description`, `status`, `br_nexus`. O
resto pode ficar pendente — diga isso explicitamente: "você pode voltar
para classificar com `/ai-governance-legal:ai-inventory classify <id>`."

1. **Nome.** Rótulo curto do sistema.
2. **Responsável.** Pessoa ou time responsável no dia a dia.
3. **Descrição.** Uma ou duas frases. O que o sistema faz, e sobre quais dados?
4. **Status.** `planejado | em_desenvolvimento | em_produção | descontinuado`.
5. **Vínculo com o Brasil (`br_nexus`).** O sistema afeta titulares de dados
   no Brasil, é oferecido a usuários no Brasil, ou está sujeito a regulação
   setorial brasileira (BCB, Anvisa, CVM)? Se sim, a análise do marco
   brasileiro se aplica — independentemente de onde o sistema foi
   desenvolvido.
6. **Envolve decisão automatizada sobre pessoa física?** Se sim, marque
   `lgpd_art20: true` — o direito a revisão humana e explicação do Art. 20
   da LGPD se aplica já, com ou sem o PL 2338.
7. **Prosseguir para classificação?** Ofereça rodar o roteiro agora, ou
   pular e voltar depois.

Atribua um ID: `sys-NNN` onde NNN é o próximo inteiro no arquivo.

## Roteiro de classificação

O roteiro produz `role`, `role_basis`, `tier`, `tier_basis`. Ambas as bases
são marcadas `[verificar contra texto vigente do PL 2338/2023 e regulação
setorial]` — não porque a skill está se protegendo, mas porque o
mapeamento é complexo e o PL ainda está em tramitação (pode ter sido
alterado, sancionado ou vetado entre a redação desta skill e o uso). O
advogado é dono da verificação.

### Passo 1: Papel

> **Quem faz o quê com este sistema?**

Opções, com o teste distintivo:

- **Fornecedor/desenvolvedor** — você desenvolve o sistema (ou manda
  desenvolver) e o coloca em operação ou disponibiliza sob sua marca.
- **Operador/implementador** — você usa o sistema sob sua própria
  autoridade, para atividade profissional (não uso pessoal). É o mais
  comum dentro de empresas.
- **Distribuidor** — você disponibiliza um sistema de IA no mercado sem
  ser o fornecedor original.

**Sinalização de papel duplo.** Se o usuário modifica substancialmente um
sistema de terceiro (faz fine-tuning com dados próprios, muda a finalidade
pretendida, rebrand), ele pode se tornar **fornecedor/desenvolvedor** do
sistema modificado mesmo tendo começado como operador. Chame atenção
quando o usuário descrever qualquer modificação além de configuração.
`[verificar contra texto vigente do PL 2338/2023 — dispositivo de
responsabilidade solidária/modificação substancial]`

Escreva o papel. Escreva `role_basis` em uma frase.

### Passo 2: Nível de risco

> **O que o sistema faz, e o caso de uso cai numa categoria regulada?**

Verifique nesta ordem:

**A. Práticas de risco excessivo (proibidas).** `[verificar contra texto
vigente do PL 2338/2023]`

Resumos, não texto definitivo — o PL 2338/2023 lista como prática de risco
excessivo (sujeita a mudança até sanção):
- Técnicas subliminares ou manipulação capazes de distorcer materialmente
  o comportamento de uma pessoa, causando dano
- Exploração de vulnerabilidades (idade, deficiência, situação
  socioeconômica) para distorcer materialmente comportamento
- Avaliação ou classificação de pessoas com base em comportamento social
  ou características de personalidade levando a tratamento prejudicial
  (scoring social)
- Identificação biométrica remota em espaços públicos para fins de
  segurança pública (exceções restritas, sujeitas a autorização judicial)
- Classificação biométrica inferindo origem racial ou étnica, convicção
  religiosa, opinião política, filiação sindical, orientação sexual, dados
  de saúde

Se enquadrado → nível é `excessivo`. Sinalize o caso de uso como stop e
roteie para o fluxo de práticas proibidas do time de governança.

**B. Áreas de alto risco.** `[verificar contra texto vigente do PL
2338/2023]`

Resumos — hipóteses típicas de alto risco no PL 2338/2023:
1. Saúde (diagnóstico, triagem, priorização de atendimento) — atenção:
   sobreposição direta com RDC Anvisa 657/2022 se o sistema for SaMD
2. Segurança pública e sistema de justiça (avaliação de risco, apoio a
   decisões judiciais, meios de prova)
3. Educação (acesso, avaliação, monitoramento de comportamento)
4. Emprego, seleção, gestão e monitoramento de trabalhadores (recrutamento,
   avaliação de desempenho, alocação de tarefas, demissão)
5. Serviços essenciais públicos e privados (benefícios sociais, concessão
   de crédito e scoring — atenção: sobreposição com Res. CMN/BCB 4.658 —,
   precificação de seguro de vida/saúde)
6. Infraestrutura crítica (energia, água, transporte, telecomunicações)
7. Migração e controle de fronteira
8. Processos eleitorais e democráticos

Se enquadrado → nível é `alto_risco`. Anote a hipótese e o setor
específico, e se há sobreposição com regulação setorial (BCB/Anvisa/CVM) —
nesse caso, ambos os regimes se aplicam cumulativamente, não um substitui
o outro.

**C. Risco geral (transparência).** Chatbots interagindo com pessoas
naturais, conteúdo sintético/deepfake, sistemas de reconhecimento de
emoção fora do escopo de risco excessivo — obrigações de transparência se
aplicam (informar a pessoa que está interagindo com IA).

**D. Sobreposição LGPD Art. 20 (independente do nível PL 2338).** Se o
sistema toma ou apoia decisão automatizada que afeta a pessoa (crédito,
perfil de consumo, seleção de emprego, etc.), o direito a revisão humana e
a explicação dos critérios se aplica **hoje**, sob a LGPD, mesmo que o
sistema seja classificado como risco geral no PL 2338. Marque
`lgpd_art20: true` sempre que aplicável — este campo é independente do
`tier`.

Escreva o nível. Escreva `tier_basis` em uma frase, citando o dispositivo
do PL ou a norma setorial que se enquadrou, marcado `[verificar contra
texto vigente]`.

### Passo 3: Recomendações

Ofereça três próximos passos:
1. "Quer que eu percorra as obrigações deste sistema? Faço em conversa —
   não derivo de uma tabela."
2. "Quer rodar `/ai-governance-legal:aia-generation` para produzir uma
   avaliação de impacto completa?"
3. "Quer definir uma data de próxima revisão? Eu adiciono ao inventário."

## Formato do registro

```yaml
systems:
  - id: sys-001
    name: "Ferramenta de triagem de currículos"
    owner: "RH / Jamie"
    description: "Filtra currículos recebidos contra critérios de vaga"
    status: em_producao            # planejado | em_desenvolvimento | em_producao | descontinuado
    br_nexus: true                 # afeta titulares no Brasil ou sujeito a regulação setorial BR
    lgpd_art20: true                # decisão automatizada que afeta pessoa física — direito a revisão (LGPD Art. 20)
    role: operador                  # fornecedor | operador | distribuidor
    role_basis: "Licenciamos da VendorX e operamos internamente [verificar contra texto vigente do PL 2338/2023]"
    tier: alto_risco                 # excessivo | alto_risco | risco_geral
    tier_basis: "Hipótese de alto risco — emprego/recrutamento/seleção [verificar contra texto vigente do PL 2338/2023]"
    obligations_assessed: false
    obligations_note: "A avaliar: como operador de sistema de alto risco — supervisão humana, qualidade dos dados de entrada, monitoramento, registro, informar aos trabalhadores, revisão humana sob LGPD Art. 20 [verificar contra texto vigente do PL 2338/2023]"
    next_review: "2026-08-01"
    review_trigger: "em modificação substancial ou anualmente, ou na sanção do PL 2338/2023"
    created: "2026-05-11"
    updated: "2026-05-11"
```

## Por que esta skill NÃO deriva obrigações automaticamente

O inventário guarda papel, nível e a base de cada um. NÃO contém uma
tabela fixa papel × nível → obrigações.

Quando o usuário perguntar "quais são minhas obrigações para o Sistema
X?", a skill faz a análise **em conversa**, marcada `[verify]`, e roteia
para `/ai-governance-legal:aia-generation` para a avaliação de impacto
formal se necessário.

Isso é deliberado:
- O PL 2338/2023 ainda está em tramitação — pode ser alterado, sancionado
  com vetos, ou substituído até você ler este texto.
- A regulação setorial (BCB, Anvisa, CVM) muda por resolução
  administrativa, sem o mesmo aviso público que uma lei.
- Confiante-e-errado numa obrigação de compliance acaba num memorando de
  conselho.
- O inventário é um registro para o advogado. O advogado é dono da análise
  de obrigações.

## Guardrails

- **Nunca classifique silenciosamente.** O roteiro de classificação deve
  ser visível; não classifique automaticamente a partir de uma descrição
  do sistema.
- **As tags `[verify]` ficam.** Não são hedging — são o ponto. Não remova
  nos outputs.
- **Sinalize modificação substancial.** Sempre que um sistema for
  modificado além de configuração, avise o usuário para rodar
  `/ai-inventory classify` de novo — modificação pode mudar o papel.
- **Não declare obrigações a partir de uma tabela.** Se perguntado, faça a
  análise em conversa e roteie para `/aia-generation` para qualquer coisa
  que precise de registro formal.
- **Trate LGPD Art. 20 como piso, não teto.** Mesmo que o PL 2338/2023
  nunca seja sancionado, ou classifique o sistema como risco geral, a
  obrigação de revisão humana sob decisão automatizada da LGPD já existe
  hoje e não desaparece.
