# Referência: Playbook Completo de Análise de Erros Médicos

> Este arquivo contém a base de conhecimento detalhada para análise de erros médicos.
> Fonte: `data/deep-research/2026-03-15-metodologias-analise-erros-medicos.md`
>
> **Leia este arquivo quando precisar de:**
> - Detalhes sobre frameworks (Reason, Vincent, Rasmussen, Croskerry)
> - Taxonomias de classificação (ICPS, AHRQ, NCC MERP, Clavien-Dindo)
> - Enquadramento jurídico brasileiro detalhado
> - Glossário de termos técnicos
> - Bibliografia e referências

Para acessar o conteúdo completo:

```
Read: data/deep-research/2026-03-15-metodologias-analise-erros-medicos.md
```

## Índice do Playbook Completo

| Parte | Conteúdo | Relevância |
|-------|----------|------------|
| I | Fundamentos Conceituais | Taxonomia de erros, distinção erro/iatrogenia/complicação, modelos teóricos, MBE |
| II | Frameworks e Classificação | ICPS/OMS, AHRQ, Swiss Cheese, PRISMA, RCA, FMEA |
| III | Metodologia de 10 Etapas | **CORE** - triagem a síntese conclusiva |
| IV | Elementos Probatórios | Prontuário, consentimento, guidelines, laudo pericial |
| V | Enquadramento Jurídico BR | Subjetiva/objetiva, meio/resultado, ônus prova, perda de chance |
| VI | Mapa Decisório para IA | Árvore decisão, checklist integrado, scoring, regras saída |
| VII | Referências | Bibliografia, bases de dados, ferramentas |

## Resumo dos Frameworks Principais

### Swiss Cheese Model (Reason, 1990)
Paradigma dominante: acidentes ocorrem quando falhas em múltiplas camadas de defesa se alinham. Distingue falhas ativas (profissional) de condições latentes (organizacionais). Usado para guiar RCA.

### Framework de Vincent (7 Níveis, 1998/2003)
Extensão do modelo de Reason para saúde:
1. Contexto institucional
2. Fatores organizacionais/gerenciais
3. Ambiente de trabalho
4. Fatores de equipe
5. Fatores individuais (profissional)
6. Fatores da tarefa
7. Características do paciente

### Teoria do Processo Dual (Croskerry)
Sistema 1 (intuitivo/rápido) vs Sistema 2 (analítico/deliberado). Vieses cognitivos relevantes: anchoring, confirmation, availability, premature closure, representativeness, framing.

### Rasmussen SRK (Skill-Rule-Knowledge)
- Skill-based: ações automáticas → deslizes/lapsos
- Rule-based: procedimentos → enganos por regra errada
- Knowledge-based: raciocínio em situação nova → enganos por modelo mental falho

## Distinção Fundamental (Quadro Decisório)

| Categoria | Prevenível? | Desvio? | Responsabilidade? |
|-----------|-------------|---------|-------------------|
| Erro médico | Sim | Sim | Sim (se dano) |
| Iatrogenia sem erro | Não necessariamente | Não | Não (regra) |
| Complicação previsível | Parcialmente | Não | Não (se consentimento + prevenção) |
| Reação idiossincrática | Não | Não | Não (imprevisível) |

**Testes objetivos:**
1. Prevenibilidade: resultado evitável com conduta adequada?
2. Desvio: conduta afastou-se do standard of care?
3. Informação: paciente informado dos riscos?
4. Resposta: complicação foi identificada e tratada tempestivamente?

## Enquadramento Jurídico Brasileiro (Resumo)

- **Responsabilidade médica é SUBJETIVA** (art. 951 CC, art. 14 §4º CDC) — exige prova de culpa
- **Obrigação de MEIO** (regra geral) — exceto cirurgia estética (resultado)
- **Inversão ônus da prova** — quando verossimilhança + hipossuficiência técnica (CDC art. 6, VIII)
- **Perda de uma chance** — quando erro reduziu chances reais de cura (chance séria e real)
- **Culpa:** negligência (omissão), imprudência (ação temerária), imperícia (falta técnica)
- **Hospital:** responsabilidade objetiva, mas depende de culpa do médico para atuação técnica
- **Estado/SUS:** responsabilidade objetiva (art. 37 §6º CF)

## Hierarquia de Evidências (Pirâmide)

1. Meta-análises e revisões sistemáticas (topo)
2. Ensaios clínicos randomizados (RCT)
3. Estudos de coorte
4. Estudos caso-controle
5. Séries/relatos de caso
6. Opinião de especialista (base)

## Never Events (Exemplos)

- Cirurgia em local/lado/paciente errado
- Corpo estranho retido após cirurgia
- Reação adversa com alergia documentada no prontuário
- Troca de sangue incompatível
- Morte materna em procedimento de baixo risco
