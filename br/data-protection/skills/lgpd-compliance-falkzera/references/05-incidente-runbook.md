# 05: Runbook de Incidente de Segurança

> Base normativa: **art. 48 LGPD** + **Resolução CD/ANPD nº 15/2024** (publicada em 26/04/2024). Quando há incidente que possa causar risco ou dano relevante ao titular, notificar ANPD E titulares em **3 dias úteis** (6 se pequeno porte).

## Definição de incidente

**Qualquer evento adverso, confirmado ou suspeito**, relacionado à violação da segurança de dados pessoais, incluindo acidental, ilícito, não autorizado:

- destruição
- perda
- alteração
- vazamento / comunicação não autorizada
- acesso não autorizado

Inclui ransomware, exfiltração de dados, exposição de banco, leak por colaborador, perda de dispositivo, configuração indevida (S3 público, banco sem senha), bug que vaza dados, phishing bem-sucedido contra colaborador com acesso.

## Critério de comunicação à ANPD

Comunica quando o incidente puder acarretar **risco ou dano relevante aos titulares**. Critérios (Res. 15/2024):

- categoria e número de titulares afetados
- categoria dos dados (sensíveis = sempre relevante)
- consequências adversas (discriminação, fraude, dano patrimonial, abalo psicológico)
- existência de medidas técnicas que tornem dados ininteligíveis (criptografia forte = pode dispensar comunicação)
- período e local em que os dados ficaram expostos

> **Na dúvida, comunica.** Custo de comunicar é baixo; custo de não comunicar e a ANPD descobrir é altíssimo (dosimetria penaliza ocultação).

## Prazo (Res. 15/2024)

| Quem | Prazo da ciência | Onde |
|---|---|---|
| Controlador regime geral | **3 dias úteis** | ANPD via SEI! + titulares |
| Controlador pequeno porte | **6 dias úteis** (dobro) | Idem |
| Comunicação preliminar incompleta | +20 dias úteis pra complementar | Idem |
| Registro interno de TODOS incidentes (mesmo não comunicados) | Imediato | **Retenção 5 anos** |

## Fluxo (runbook)

```
                                  ┌──────────────────────┐
                                  │ T+0: ciência do      │
                                  │ incidente            │
                                  └──────────┬───────────┘
                                             ▼
                              ┌────────────────────────────┐
                              │ 1. Conter (em horas)       │
                              │  - isolar sistema afetado  │
                              │  - rotacionar credenciais  │
                              │  - snapshot pra forense    │
                              └──────────┬─────────────────┘
                                             ▼
                              ┌────────────────────────────┐
                              │ 2. Triagem (em ~24h)       │
                              │  - dados afetados          │
                              │  - n. de titulares         │
                              │  - data/janela de exposição│
                              │  - vetor                   │
                              └──────────┬─────────────────┘
                                             ▼
                              ┌────────────────────────────┐
                              │ 3. Decisão de comunicar?   │
                              │  Critério risco/dano       │
                              │  relevante                 │
                              └────┬───────────────┬───────┘
                                   │ SIM           │ NÃO
                                   ▼               ▼
                ┌──────────────────────────┐    ┌──────────────┐
                │ 4. Notificar ANPD (SEI!) │    │ Registro     │
                │    + titulares           │    │ interno      │
                │    em até 3 dias úteis   │    │ (5 anos)     │
                │    (6 se pequeno porte)  │    └──────────────┘
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │ 5. Mitigar e remediar    │
                │  - corrigir vetor        │
                │  - oferecer remediação   │
                │    aos titulares         │
                │    (monitoramento de     │
                │    crédito, troca de     │
                │    senha forçada)        │
                └──────────────┬───────────┘
                               ▼
                ┌──────────────────────────┐
                │ 6. Post-mortem (5-10d)   │
                │  - causa raiz            │
                │  - melhorias             │
                │  - retreinamento         │
                │  - atualizar RIPD/ROPA   │
                └──────────────────────────┘
```

## Onde notificar: SEI!ANPD

- URL: <https://sei.anpd.gov.br/>
- Login: **Gov.br** do responsável legal
- Tipo de processo: **"ANPD - Comunicados de Incidentes à Agência Nacional de Proteção de Dados"**
- Página oficial: <https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis>

## Conteúdo OBRIGATÓRIO da notificação (Res. 15/2024 art. 5º)

1. **Natureza e categoria** dos dados pessoais afetados (comum / sensível / criança).
2. **Número aproximado** de titulares afetados (separar BR / exterior).
3. **Medidas de segurança** vigentes **antes** do incidente.
4. **Riscos** relacionados ao incidente e **impactos potenciais** aos titulares.
5. **Motivos** de eventual atraso na comunicação.
6. **Medidas adotadas ou planejadas** pra reverter ou mitigar.
7. **Data da descoberta** do incidente.
8. **Contato do DPO** ou canal alternativo.

## Comunicação aos titulares: modelo

```
Assunto: Comunicado importante sobre seus dados em [{{APP_NOME}}]

Olá,

Em {{DATA_INCIDENTE}} identificamos um incidente de segurança que pode ter
afetado dados pessoais que você nos confiou. Estamos te comunicando em
cumprimento ao art. 48 da LGPD.

O que aconteceu
{{DESCRICAO_CURTA_DO_INCIDENTE}}

Quais dados foram afetados
- {{LISTAR}}

Quais NÃO foram afetados
- senhas em forma legível (estavam protegidas por hash)
- dados de pagamento (não armazenamos)
- {{ETC}}

O que estamos fazendo
- {{CONTENÇÃO}}
- {{CORREÇÃO}}
- {{MONITORAMENTO}}

O que recomendamos a você
- trocar sua senha em {{APP_NOME}} agora
- atenção a tentativas de phishing usando seu nome/e-mail
- monitorar movimentações em sua conta

Você tem direito a (LGPD art. 18):
- confirmar exatamente quais dados seus foram afetados
- solicitar correção, anonimização ou eliminação
- reclamar à ANPD (gov.br/anpd)

Nosso canal de privacidade: {{DPO_CONTATO}}

Atenciosamente,
{{CONTROLADOR_NOME}}
```

**Forma de envio:** preferencialmente individual (e-mail, app push). Se inviável, meios de comunicação ampla (site, redes sociais, imprensa). Res. 15/2024 permite formas combinadas.

## Pre-requisitos no app (antes do incidente acontecer)

- [ ] **Logs centralizados** que permitam reconstruir o que vazou
- [ ] **Inventário atualizado** (ROPA), saber rapidamente quais titulares têm qual dado
- [ ] **Lista de processadores** com canal de incidente de cada um (AWS, Vercel, Mailgun, etc.)
- [ ] **Cadeia de comando definida**: quem detecta → quem comunica → quem decide → quem fala com a ANPD
- [ ] **Template de e-mail aos titulares** já redigido e revisado
- [ ] **Acesso ao SEI!ANPD configurado** (login Gov.br do responsável + nível Bronze suficiente)
- [ ] **Política de senhas + 2FA** vigente (atenuante na dosimetria)
- [ ] **Criptografia em trânsito e em repouso** (atenuante grande)
- [ ] **Backup testado** (restore funciona, não basta existir)
- [ ] **Treinamento de equipe** mínimo anual (atenuante)
- [ ] **DPA com cada processador** incluindo cláusula de notificação de incidente em prazo compatível

## Atenuantes na dosimetria de sanção (Res. CD/ANPD nº 4/2023)

Ter os itens abaixo formalizados **antes** do incidente reduz multa:

- Política de Privacidade e Segurança publicada
- ROPA atualizado
- RIPD onde aplicável
- Programa de governança de privacidade
- Treinamento documentado
- Pronta adoção de medidas corretivas após o incidente
- Cooperação com a ANPD (não esconder, não dificultar)
- Boa-fé demonstrável

Agravantes:
- Reincidência
- Lucratividade obtida pela infração
- Ocultação ou tentativa de ocultação
- Falta de cooperação
- Gravidade do dano

## Referências externas

- [LGPD Art. 48 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art48)
- [Resolução CD/ANPD nº 15/2024 (PDF)](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis)
- [Canal CIS no portal ANPD](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis)
- [SEI! ANPD](https://sei.anpd.gov.br/)
- [Resolução CD/ANPD nº 4/2023 (Dosimetria)](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd)
