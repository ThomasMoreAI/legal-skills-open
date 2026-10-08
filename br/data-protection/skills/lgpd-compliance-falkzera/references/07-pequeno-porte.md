# 07: Regime de Pequeno Porte (Resolução CD/ANPD nº 2/2022)

> Fonte: [Resolução CD/ANPD nº 2, de 27/01/2022](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022). Define **agentes de tratamento de pequeno porte (ATPP)** e flexibiliza obrigações administrativas: **não dispensa** princípios, bases legais, direitos do titular nem segurança.

## Quem é ATPP (art. 2º + 3º)

**É** ATPP, **se cumprir TODOS os critérios:**

### Categoria de pessoa
- **Pessoas naturais** que tratam dados pessoais com **fins econômicos** (autônomos, profissionais liberais)
- **Microempresas** (LC 123/2006): faturamento até **R$ 360.000/ano**
- **Empresas de pequeno porte (EPP)**: faturamento entre **R$ 360.000 e R$ 4.800.000/ano**
- **MEI** (Microempreendedor Individual)
- **Startups** (LC 182/2021): faturamento até **R$ 16 milhões/ano** + até 10 anos de inscrição no CNPJ + dedicada à inovação
- **Pessoas jurídicas de direito privado sem fins lucrativos**
- **Entes despersonalizados** (condomínios, espólios)
- **Iniciativas empresariais de caráter incremental ou disruptivo** desde que se autodeclarem startups

### Restrições adicionais
- **NÃO integra grupo econômico** cujo faturamento global ultrapasse os limites acima
- **NÃO realiza tratamento de alto risco** (art. 4º, ver abaixo)

## Tratamento de ALTO RISCO (art. 4º Res. 2/2022): desqualifica do regime

ANY destes acionamentos **tira** o ATPP do regime simplificado:

1. Cumular **dois ou mais** critérios:
   - **(a)** Larga escala, número significativo de titulares, volume, duração, abrangência geográfica
   - **(b)** Significativo impacto a direitos e liberdades fundamentais

2. Ou **acionar UM dos critérios + a** abaixo:
   - **(b)** Uso de **tecnologias emergentes ou inovadoras** (IA, ML, blockchain pra identificação)
   - **(c)** **Vigilância ou controle sistemático** de área de acesso público
   - **(d)** Decisões tomadas com base em tratamento **automatizado** que afete direitos
   - **(e)** Tratamento de **dados pessoais sensíveis ou de natureza altamente pessoal** (orientação sexual, financeiros, localização)
   - **(f)** Tratamento de dados pessoais de **crianças, adolescentes ou idosos**

> **Tradução prática:** uma startup com 50k usuários que usa GPT pra inferir preferências = alto risco. Sai do ATPP, vai pra regime geral.

## O que MUDA no regime simplificado

### 1. Dispensa de Encarregado (DPO): art. 11
- **Dispensado** de **indicar** Encarregado formal.
- **MAS:** obrigatório **disponibilizar canal de comunicação com o titular** (e-mail, formulário, telefone). Esse canal deve estar visível na política.
- Boa prática: criar `privacidade@empresa.com.br` mesmo sem nomear DPO formal.
- Pode indicar DPO voluntariamente → vira **atenuante na dosimetria** (Res. 4/2023).

### 2. ROPA simplificado: art. 9º
- Pode usar o **modelo simplificado publicado pela ANPD** (Excel/PDF):
  - PDF: [Modelo ROPA ATPP](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/modelo_de_ropa_para_atpp.pdf)
  - Excel: [Modelo Excel](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/modelo_de_ropa_para_atpp-3.xlsx)
- Campos essenciais (8): identificação do agente, finalidade, descrição dos dados, base legal, destinatários, retenção, transferência internacional, segurança.

### 3. Política de Segurança simplificada: art. 12-13
- Permitida política simplificada considerando estrutura e custos.
- Guia ANPD: [Guia Orientativo de Segurança da Informação para ATPP](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-sobre-seguranca-da-informacao-para-agentes-de-tratamento-de-pequeno-porte), jun/2024.

### 4. Prazos em DOBRO

| Obrigação | Regime geral | ATPP |
|---|---|---|
| Resposta a titular, confirmação simplificada (art. 19 I) | Imediata | até 15 dias |
| Resposta a titular, declaração completa (art. 19 II) | 15 dias | **30 dias** |
| Comunicação de incidente à ANPD (Res. 15/2024) | 3 dias úteis | **6 dias úteis** |
| Resposta a requerimentos da ANPD | Padrão | Dobro do prazo padrão |

### 5. Política de Privacidade
- **Não é dispensada**. ATPP precisa publicar política contendo todos os itens do art. 9º LGPD.
- **Pode** listar canal genérico (`privacidade@`) ao invés de DPO nomeado.

## O que NÃO muda: substância integral

- **Princípios (art. 6º)**, todos aplicam.
- **Bases legais (art. 7º + 11)**, toda finalidade precisa de base.
- **Direitos do titular (art. 18)**, todos aplicam, com prazos dobrados.
- **Segurança (art. 46-49)**, aplica em versão simplificada, mas obrigatório.
- **Comunicação de incidente (art. 48)**, obrigatória, prazo dobrado.
- **Sanções (art. 52)**, aplicam, mas com atenuante de pequeno porte na dosimetria (Res. 4/2023).
- **Transferência internacional (art. 33 + Res. 19/2024)**: SCC obrigatória.

## Decisão da skill: ATPP ou regime geral?

```
SE pessoa natural com fins econômicos
   OU MEI / ME / EPP (≤ R$ 4,8M/ano)
   OU startup (≤ R$ 16M/ano + ≤ 10 anos)
   OU PJ sem fins lucrativos
   OU ente despersonalizado

E NÃO integra grupo econômico que estoura limite

E NÃO faz alto risco (matriz art. 4º):
   - larga escala + impacto significativo (a + b)
   - larga escala + tech emergente (a + c?)
   - vigilância sistemática + qualquer outro
   - decisões automatizadas que afetem direitos
   - dados sensíveis em larga escala
   - dados de crianças/adolescentes/idosos em larga escala

ENTÃO ATPP → ativar regime simplificado
SENÃO regime geral
```

## Como a skill aplica o regime simplificado

Quando a auditoria conclui que o projeto é ATPP, a geração ajusta:

1. **Política de Privacidade**: omite nome do DPO, usa `{{DPO_CONTATO}}` genérico tipo `privacidade@empresa.com.br`.
2. **ROPA**: copia o modelo simplificado da ANPD (`templates/ropa.csv`) e preenche.
3. **Runbook de incidente**: prazo de **6 dias úteis** explícito.
4. **Política de Segurança**: versão simplificada.
5. **Prazos de SLA aos titulares** declarados como **15-30 dias** (regime ATPP).
6. **Indicar opcionalmente DPO voluntário** com nota de atenuante.

## Risco: deixar de ser ATPP

ATPP **muda dinamicamente**. Skill deve alertar:

- A cada **6 meses**, reavaliar enquadramento.
- Se o app passar a tratar dados de crianças → re-enquadrar (geral).
- Se introduzir IA que decide algo sobre usuário → re-enquadrar.
- Se faturar acima de R$ 4,8M (ou 16M se startup) → re-enquadrar.

Quando perder o regime simplificado, **atualizar todos os artefatos** (DPO formal, ROPA completo, política de segurança, prazos padrão).

## Referências externas

- [Resolução CD/ANPD nº 2/2022 (texto)](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-2-de-27-de-janeiro-de-2022)
- [Modelo ROPA ATPP (PDF)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/modelo_de_ropa_para_atpp.pdf)
- [Modelo ROPA ATPP (Excel)](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/modelo_de_ropa_para_atpp-3.xlsx)
- [Guia de Segurança para ATPP](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-sobre-seguranca-da-informacao-para-agentes-de-tratamento-de-pequeno-porte)
- [LC 123/2006 (ME/EPP)](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm)
- [LC 182/2021 (Marco Legal das Startups)](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp182.htm)
