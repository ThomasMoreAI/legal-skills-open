# 09: Termos de Uso: Marco Civil, Responsabilidade, UGC

> **ATENÇÃO:** o STF concluiu em **26/06/2025** o julgamento do **Tema 987** (RE 1.037.396 / RE 1.057.258) e declarou o **art. 19 do MCI parcialmente inconstitucional**, criando regime **escalonado** de responsabilidade de provedores. Esta referência incorpora a nova interpretação.

## Definições críticas (art. 5º MCI)

| Conceito | Definição | Quem é |
|---|---|---|
| **Provedor de conexão** | Fornece acesso à internet | ISP, telco (Vivo, Claro, NET) |
| **Provedor de aplicação** | "Conjunto de funcionalidades acessadas por terminal conectado à internet" | **Todo SaaS, todo site, todo app, toda API pública** |
| **Registros de conexão** | Data/hora de início/fim + IP (art. 5º VI) | Mantido pelo provedor de conexão |
| **Registros de acesso a aplicações** | Data/hora de uso de uma aplicação a partir de um IP (art. 5º VIII) | Mantido pelo provedor de aplicação |

**Na prática:** um app é sempre **provedor de aplicação**. Conteúdo institucional do app → responsabilidade direta (CC + CDC). Conteúdo postado por usuário (UGC) → regime dos arts. 19 e 21 com leitura do STF/2025.

## Direitos do usuário de internet (art. 7º)

Direitos garantidos por **lei**, qualquer cláusula em contrário é nula (art. 8º). Os relevantes pra Termos:

| Inciso | Direito | Implicação pra Termos |
|---|---|---|
| I | Inviolabilidade da intimidade e vida privada (+ indenização) | Sigilo de dados pessoais; vedado divulgar sem consentimento |
| II | Sigilo do **fluxo** de comunicações (salvo ordem judicial) | Não interceptar transmissão em tempo real |
| III | Sigilo das **comunicações privadas armazenadas** (salvo ordem judicial) | App não pode ler DMs/chats sem ordem |
| VI | Informações claras sobre coleta/uso/armazenamento/tratamento de dados | Replicado pela LGPD art. 9º |
| VIII | Dados usados só pra finalidades especificadas em contrato/termos | Princípio da finalidade |
| IX | Consentimento expresso, **destacado** das demais cláusulas | Anti-genérico, anti-pre-marcado |
| X | Exclusão definitiva dos dados ao término da relação (ressalvada guarda obrigatória) | Reforça LGPD art. 18 VI |
| XI | Publicidade e clareza sobre políticas de uso | Termos devem ser públicos e claros |

## Guarda de logs: **prazos** (cuidado pra não inverter)

| Norma | Quem | Dado | Prazo |
|---|---|---|---|
| **Art. 13** | Provedor de **conexão** | Registros de **conexão** | **1 ano (12 meses)** |
| **Art. 15** | Provedor de **aplicação** PJ com fim econômico | Registros de **acesso à aplicação** | **6 meses** |

**Para apps (todos provedores de aplicação): 6 meses, contados da data do acesso.**

Regras gerais:
- Sob **sigilo**, em ambiente controlado e seguro.
- Autoridade policial, MP ou administrativa pode requerer guarda por prazo **superior** (com pedido judicial em até 60 dias).
- Acesso ao **conteúdo** dos logs exige **ordem judicial** (arts. 22-23).
- **Importante:** o art. 15 manda guardar **registros de acesso**, NÃO conteúdo. Guardar conteúdo das comunicações "porque a lei manda" é interpretação errada e viola LGPD (princípio da necessidade).

**Pros Termos:** declarar expressamente que o app coleta e guarda registros de acesso por 6 meses (base legal LGPD art. 7º II, obrigação legal), e que **não há acesso ao conteúdo** das comunicações privadas salvo ordem judicial.

## Responsabilidade civil por conteúdo de terceiros (art. 19 + Tema 987 STF/2025)

### Texto original do art. 19
Provedor de aplicação só responde por conteúdo de terceiros se, **após ordem judicial específica**, não tomar providências pra tornar o conteúdo indisponível.

### O que mudou em 26/06/2025

O STF criou **regime escalonado** com 4 níveis:

#### Nível 1: Art. 19 puro (precisa de ordem judicial)
**Crimes contra a honra** (calúnia, difamação, injúria). Plataforma só responde se descumprir ordem judicial específica. **Mas:** nada impede que ela remova com base em notificação extrajudicial se quiser.

#### Nível 2: Notice & takedown (art. 21 expandido)
**Demais ilícitos em geral.** Plataforma responde se, **após notificação extrajudicial** do interessado, não remover em tempo razoável. Antes do Tema 987, esse regime era restrito ao art. 21 (nudez não consentida); agora se aplica amplamente.

#### Nível 3: Dever de cuidado (remoção proativa sem notificação)
Rol de **conteúdos manifestamente ilícitos e graves** que exigem remoção imediata, sem ordem nem notificação. A omissão sistêmica gera responsabilidade:

- Atos antidemocráticos (CP arts. 359-L a 359-T)
- Terrorismo (Lei 13.260/2016)
- Indução, instigação ou auxílio a suicídio e automutilação
- Racismo (Lei 7.716/89)
- Violência contra mulher por razão de gênero (incl. discurso de ódio misógino)
- Crimes sexuais contra vulneráveis, pornografia infantil, crimes graves contra crianças e adolescentes (ECA)
- Tráfico de pessoas

Plataforma se exime se provar que agiu com **diligência e em tempo razoável**.

#### Nível 4: Presunção de responsabilidade
Independente de notificação:
- **Conteúdo impulsionado pago / anúncios**, plataforma monetiza, então responde.
- **Distribuição artificial via bots / chatbots / rede inautêntica**.

#### Replicação de conteúdo já reconhecido como ilícito
Decisão judicial reconhece ilicitude → **todas as réplicas idênticas em todas as plataformas** devem ser removidas a partir de notificação (judicial OU extrajudicial), sem nova decisão pra cada cópia.

### Implicações práticas pros Termos

Apps com **UGC** precisam:

1. **Canal claro de denúncia/notificação extrajudicial** com SLA explícito (24-72h pra maioria; imediato pra urgências do Nível 3).
2. **Cláusula expressa** dizendo que a plataforma **pode remover proativamente** conteúdo do Nível 3, protege contra alegação de censura privada.
3. Pra apps com **boost pago / anúncios**: moderação prévia mais robusta (responsabilidade objetiva).
4. **Notificação reversa** ao publicador acusado (contraditório, 7 dias salvo urgência).
5. **Log imutável** de notificação → análise → ação.
6. **Relatório de transparência anual** (exigência consolidada pós-STF).

## Art. 21: Nudez/atos sexuais não consentidos

Exceção mantida (anterior ao Tema 987). Provedor responde **subsidiariamente** pela divulgação **não autorizada** de cenas de nudez ou atos sexuais de caráter **privado**, quando, após **notificação extrajudicial** do participante (ou representante), deixar de indisponibilizar diligentemente.

Requisitos cumulativos (STJ: REsp 1.930.256):
1. **Não consentimento** comprovado
2. **Natureza privada** das cenas (STJ exclui nudez produzida com fim comercial, esses casos voltam ao art. 19)
3. Violação efetiva à intimidade

Notificação deve identificar **especificamente** o material (URL exata, não denúncia genérica).

**Pros Termos:** fluxo de denúncia art. 21 **separado** do fluxo geral, com (a) campo URL, (b) declaração de não consentimento sob as penas da lei, (c) compromisso de remoção em 24-48h.

## Conteúdo Gerado pelo Usuário (UGC): propriedade e licença

### Propriedade
**Padrão BR: obra pertence ao autor.** Lei 9.610/98 art. 22. Termos que dizem "todo o conteúdo postado passa a ser de propriedade do app" são **nulos** (CDC art. 51 IV + Lei 9.610 art. 49, cessão exige instrumento escrito, específico, com objeto e prazo definidos).

### Licença válida: modelo

Cláusula juridicamente sólida:

> "O Usuário mantém integralmente a titularidade do conteúdo que envia. Ao publicar, o Usuário concede à [Empresa] uma licença **mundial, não exclusiva, gratuita, sublicenciável (apenas quando necessário à prestação do serviço: CDN, processadores, infraestrutura) e revogável mediante exclusão do conteúdo**, para hospedar, armazenar, exibir, distribuir, reproduzir, adaptar tecnicamente (transcoding, redimensionamento), indexar e disponibilizar o conteúdo dentro da plataforma e em comunicações operacionais sobre o serviço."

### Pontos críticos

- **NÃO ceder direitos morais**, são **inalienáveis e irrenunciáveis** (Lei 9.610/98 art. 27).
- **Limitar a finalidade** à prestação do serviço, licença genérica "pra qualquer fim, presente ou futuro" é frágil.
- **Garantir reversibilidade**, usuário deleta → licença cessa (ressalva técnica pra backups + cópias já compartilhadas por terceiros).
- **IA/treinamento de modelo** = finalidade distinta da prestação do serviço. Exige **consentimento específico e destacado**, em compliance com LGPD se houver dado pessoal embutido.
- **Validade no CDC:** cláusula precisa (i) estar em destaque, (ii) ser proporcional ao serviço, (iii) não criar vantagem unilateral excessiva, (iv) permitir revogação prática.

### Direitos autorais e canal de denúncia (DMCA-style brasileiro)

O Brasil não tem DMCA, mas o regime atual cria mecanismo análogo: art. 19 reformulado + Lei 9.610/98.

**Canal precisa exigir:**
- Identificação do titular ou representante (CPF/CNPJ, contato)
- Prova mínima de titularidade
- URL específica do conteúdo
- Declaração sob as penas da lei (art. 299 CP)
- **Contranotificação** do usuário acusado (espelha DMCA counter-notice), permite restabelecer se acusação for contestada e denunciante não buscar via judicial.

## Suspensão e exclusão de conta: exigência de ampla defesa

Jurisprudência consolidada (TJSP, TJPR, TJMT + STJ): bloqueio, suspensão ou exclusão **sumária** de conta, sem notificação prévia e sem possibilidade de defesa, é **abusiva** e gera dano moral.

Princípios aplicados:
- **Eficácia horizontal dos direitos fundamentais** (contraditório/ampla defesa entre particulares)
- **CDC art. 51 IV** (desvantagem exagerada) e **XI** (cancelamento unilateral)

**Receita pros Termos:**

1. **Listar de forma objetiva** as condutas que ensejam suspensão/exclusão.
2. **Gradação:** alerta → suspensão temporária → exclusão.
3. **Notificação prévia**, exceto em risco iminente (fraude ativa, conteúdo do Nível 3 STF, risco à segurança de outros).
4. **Canal de contestação** com prazo razoável (5-15 dias úteis).
5. **Permitir exportação dos dados** antes da exclusão (LGPD art. 18 V).
6. **Conta inativa:** prazo claro (mercado 12-24 meses), notificação prévia, prazo de retomada, só então excluir. Manter conta inativa indefinidamente viola **princípio da necessidade** (LGPD art. 6º III).

## Condutas proibidas: modelo executável

Pra cada item da seção "Condutas Proibidas" funcionar juridicamente:

1. **Específico** (não "qualquer conduta inadequada"; sim "envio automatizado > X req/min")
2. **Vinculado a consequência clara** (notificação → suspensão → exclusão)
3. **Reproduzível em prova** (logs do art. 15 servem)

Lista mínima:

- Crimes do rol "dever de cuidado" do Tema 987 (terrorismo, racismo, etc.)
- Conteúdo art. 21 (nudez/sexual não consensual)
- Violação de PI de terceiros
- Spam, scraping não autorizado, automação não autorizada
- Engenharia reversa, descompilação, contorno de proteções (Lei 9.609/98 art. 6º)
- Abuso de API
- Tentativas de invasão (Lei 12.737/2012, "Carolina Dieckmann")
- Personificação, fake accounts, manipulação de métricas
- Uso comercial fora do tier contratado

Cada item amarrado à autorização pra suspensão/exclusão **com direito de contestação**.

## Neutralidade de rede (art. 9º)

Em geral **NÃO se aplica** a SaaS, mira ISPs e backbones. Relevante quando:
- App oferece tiers que o leigo confunde com "internet diferente"
- App integra CDN/edge próprio e quer evitar enquadramento como provedor de conexão
- App faz zero-rating ou parceria com telco (art. 9º §§1º-2º + Decreto 8.771/2016)

Pra Termos comuns, cláusula simples afirmando que o app é provedor de aplicação (não de conexão) basta.

## Referências externas

- [Lei 12.965/2014 (Marco Civil (Planalto))](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm)
- [Lei 9.610/1998 (Direitos Autorais)](https://www.planalto.gov.br/ccivil_03/leis/l9610.htm)
- [Lei 9.609/1998 (Lei do Software)](https://www.planalto.gov.br/ccivil_03/leis/l9609.htm)
- [STF (Tema 987 Repercussão Geral)](https://portal.stf.jus.br/jurisprudenciaRepercussao/tema.asp?num=987)
- [STF (Andamento Tema 987 / RE 1.037.396)](https://portal.stf.jus.br/jurisprudenciaRepercussao/verAndamentoProcesso.asp?incidente=5160549)
- [Nota técnica STF (art. 19 MCI)](https://www.stf.jus.br/arquivo/cms/noticiaNoticiaStf/anexo/Informac807a771oa768SociedadeArt19MCI_vRev.pdf)
- [STJ (Art. 21 requisitos (REsp 1.930.256: Dizer o Direito))](https://buscadordizerodireito.com.br/jurisprudencia/8812)
- [STJ (Art. 21 não-consensual privado vs comercial)](https://buscadordizerodireito.com.br/jurisprudencia/10138)
- [Artigo 19 Brasil (Nota técnica decisão STF 2025)](https://artigo19.org/2025/08/15/nota-tecnica-decisao-do-stf-sobre-o-artigo-19-do-marco-civil-da-internet/)
- [TJDFT (Marco Civil)](https://www.tjdft.jus.br/institucional/imprensa/campanhas-e-produtos/direito-facil/edicao-semanal/marco-civil-da-internet)
