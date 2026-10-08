# 01: Lei, Fundamentos, Princípios, Definições

> Fonte canônica: [Lei 13.709/2018 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm). Esta página é uma síntese operacional, em caso de dúvida sobre redação literal, sempre voltar ao Planalto.

## Cronologia

| Norma | Data | O que mudou |
|---|---|---|
| **Lei 13.709** (LGPD) | 14/08/2018 | Texto original |
| **Lei 13.853** | 08/07/2019 | Criou a ANPD |
| **MP 1.137 → Lei 15.352** | 17/09/2025 → 25/02/2026 | Transformou ANPD em **agência reguladora autônoma** (Lei 13.848/2019) |

## Art. 1º: Objeto

Dispõe sobre o tratamento de dados pessoais, inclusive em meios digitais, por pessoa natural ou jurídica de direito público ou privado, com o objetivo de proteger:

- direitos fundamentais de liberdade e privacidade
- livre desenvolvimento da personalidade da pessoa natural

Normas gerais de interesse nacional, observadas por União, Estados, DF, Municípios.

## Art. 2º: Fundamentos

A disciplina tem como fundamentos:

1. Respeito à privacidade
2. **Autodeterminação informativa** (o titular controla seus próprios dados)
3. Liberdade de expressão, informação, comunicação, opinião
4. Inviolabilidade da intimidade, honra, imagem
5. Desenvolvimento econômico, tecnológico, inovação
6. Livre iniciativa, livre concorrência, defesa do consumidor
7. Direitos humanos, livre desenvolvimento da personalidade, dignidade, exercício da cidadania

## Art. 3º: Aplicação territorial (extraterritorial mitigada)

A LGPD se aplica a qualquer operação de tratamento, independentemente do meio, do país de sede do controlador ou do país onde os dados estejam, desde que:

- **I.** a operação seja realizada **no território nacional**, OU
- **II.** a atividade tenha por objetivo **oferta de bens/serviços** ou tratamento de dados de **indivíduos localizados no Brasil**, OU
- **III.** os dados tenham sido **coletados no território nacional** (titular estava aqui no momento da coleta).

Prática: startup brasileira hospedada na AWS Virgínia → LGPD se aplica. SaaS estrangeiro com usuários no Brasil → LGPD se aplica.

## Art. 4º: Quando NÃO se aplica

- **I.** Pessoa natural com fins **exclusivamente particulares e não econômicos** (agenda telefônica privada).
- **II.** Fins exclusivamente **jornalísticos, artísticos** ou **acadêmicos** (acadêmico aplica arts. 7º e 11).
- **III.** Segurança pública, defesa nacional, segurança do Estado, investigação penal, regidos por legislação específica. **Entes privados não podem tratar nesse regime.**
- **IV.** Dados de fora do Brasil que não tenham comunicação/transferência com o BR, desde que o país de origem tenha grau de proteção adequado.

## Art. 5º: Definições críticas (redação literal)

| Inciso | Termo | Definição |
|---|---|---|
| I | **Dado pessoal** | Informação relacionada a pessoa natural identificada ou identificável |
| II | **Dado pessoal sensível** | Dado sobre origem racial/étnica, convicção religiosa, opinião política, filiação sindical/religiosa/filosófica/política, dado referente à saúde, vida sexual, genético ou biométrico, quando vinculado a pessoa natural |
| III | **Dado anonimizado** | Dado relativo a titular que **não possa ser identificado**, considerando meios técnicos razoáveis e disponíveis na ocasião |
| V | **Titular** | Pessoa natural a quem se referem os dados |
| VI | **Controlador** | Pessoa natural ou jurídica a quem competem **as decisões** sobre o tratamento |
| VII | **Operador** | Pessoa natural ou jurídica que **realiza o tratamento** em nome do controlador |
| VIII | **Encarregado (DPO)** | Pessoa indicada para atuar como canal entre controlador, titulares e ANPD |
| X | **Tratamento** | TODA operação com dados pessoais: coleta, produção, recepção, classificação, utilização, acesso, reprodução, transmissão, distribuição, processamento, arquivamento, armazenamento, eliminação, avaliação, controle, modificação, comunicação, transferência, difusão, extração |
| XI | **Anonimização** | Uso de meios técnicos razoáveis pelos quais o dado **perde possibilidade de associação** direta ou indireta a indivíduo |
| XII | **Consentimento** | Manifestação **livre, informada e inequívoca** pela qual o titular concorda com tratamento para finalidade determinada |
| XV | **Transferência internacional** | Transferência de dados pessoais para país estrangeiro ou organismo internacional |
| XVI | **Uso compartilhado** | Comunicação, difusão, transferência internacional, interconexão ou tratamento compartilhado de bancos de dados |
| XVII | **RIPD** | Relatório de Impacto à Proteção de Dados Pessoais |
| XIX | **Autoridade Nacional** | ANPD |

> **Cuidado:** "dado anonimizado" só sai do escopo da LGPD quando a anonimização é **irreversível** considerando o estado da arte. O art. 12 §1º deixa claro: dado pseudonimizado/reversível continua sendo dado pessoal.

## Art. 6º: PRINCÍPIOS (todo tratamento deve respeitar)

> *"As atividades de tratamento de dados pessoais deverão observar a **boa-fé** e os seguintes princípios:"*

| # | Princípio | Tradução prática |
|---|---|---|
| I | **Finalidade** | Propósitos legítimos, específicos, explícitos, informados ao titular. Sem reaproveitamento incompatível |
| II | **Adequação** | Compatibilidade do tratamento com as finalidades informadas |
| III | **Necessidade** | Mínimo necessário; pertinentes, proporcionais, não excessivos. **Princípio do data minimization** |
| IV | **Livre acesso** | Consulta facilitada e gratuita do titular sobre forma, duração e integralidade dos dados |
| V | **Qualidade dos dados** | Exatidão, clareza, relevância, atualização |
| VI | **Transparência** | Informações claras, precisas, facilmente acessíveis sobre tratamento e agentes, respeitados segredos comercial/industrial |
| VII | **Segurança** | Medidas técnicas e administrativas contra acesso não autorizado, destruição, perda, alteração, comunicação ou difusão |
| VIII | **Prevenção** | Medidas pra prevenir danos antes que ocorram |
| IX | **Não discriminação** | Vedado tratamento para fins discriminatórios ilícitos ou abusivos |
| X | **Responsabilização e prestação de contas** | **Accountability**: demonstrar adoção de medidas eficazes e capazes de comprovar cumprimento |

> **Como aplicar na auditoria:** toda decisão de produto envolvendo dado pessoal precisa passar nesse filtro de 10 princípios. Se uma feature falha em qualquer um, redesenhar.

## ANPD: Autoridade Nacional

- **Site oficial:** [gov.br/anpd](https://www.gov.br/anpd/pt-br)
- **Notificação de incidente (SEI!):** [sei.anpd.gov.br](https://sei.anpd.gov.br/)
- **Atribuições principais (art. 55-J):**
  - zelar e fiscalizar cumprimento da LGPD
  - editar normas e diretrizes
  - aplicar sanções
  - decidir sobre interpretação da LGPD
  - cooperar com autoridades estrangeiras
  - elaborar relatórios anuais

### Guias e resoluções que importam (sempre consultar versão atual)

- **Resolução CD/ANPD nº 1/2021**: Regimento Interno
- **Resolução CD/ANPD nº 2/2022**: Agentes de Pequeno Porte (ATPP), `references/07-pequeno-porte.md`
- **Resolução CD/ANPD nº 4/2023**: Dosimetria de Sanções
- **Resolução CD/ANPD nº 15/2024**: Comunicação de Incidente de Segurança, `references/05-incidente-runbook.md`
- **Resolução CD/ANPD nº 18/2024**: Indicação de Encarregado de Dados
- **Resolução CD/ANPD nº 19/2024**: Transferência Internacional (período de graça terminou em 23/08/2025)
- **Guia Orientativo "Agentes de Tratamento e Encarregado"**, v2.0 de 26/04/2024
- **Guia Orientativo "Cookies e Proteção de Dados Pessoais"**, 22/11/2024, atualizado 23/01/2025, `references/06-cookies-guia-anpd.md`
- **Guia de Segurança da Informação para ATPP**, jun/2024, atualizado jan/2025

## Sanções (art. 52)

A ANPD pode aplicar, isolada ou cumulativamente:

1. **Advertência** com prazo para correção
2. **Multa simples** de até **2% do faturamento** do grupo no Brasil no último exercício, **limitada a R$ 50 milhões por infração**
3. **Multa diária**, observado o teto acima
4. **Publicização** da infração após apurada e confirmada
5. **Bloqueio** dos dados objeto da infração até regularização
6. **Eliminação** dos dados objeto da infração
7. **Suspensão parcial** do banco de dados (até 6 meses, prorrogável)
8. **Suspensão do exercício** da atividade de tratamento (até 6 meses, prorrogável)
9. **Proibição parcial ou total** do exercício de atividades de tratamento

Critérios de dosimetria → **Resolução CD/ANPD nº 4/2023**: gravidade, boa-fé, vantagem auferida, condição econômica, reincidência, dano, cooperação, mecanismos internos, política de boas práticas, governança, medidas corretivas, proporcionalidade.

**Histórico real:** 1ª multa privada aplicada em jul/2023 (Telekall: R$ 14.400). Em 2024, nenhuma multa nova a empresas privadas (5 processos contra órgãos públicos, que não pagam multa). Tendência de aceleração da fiscalização em 2025-2026.

## Referências externas

- [Texto integral LGPD (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
- [ANPD institucional](https://www.gov.br/anpd/pt-br)
- [Guia Agentes de Tratamento (PDF)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/2021.05.27GuiaAgentesdeTratamento_Final.pdf)
- [CNMP (Fundamentos e Princípios)](https://www.cnmp.mp.br/portal/transparencia/lei-geral-de-protecao-de-dados-pessoais-lgpd/a-lgpd/fundamentos-e-principios)
