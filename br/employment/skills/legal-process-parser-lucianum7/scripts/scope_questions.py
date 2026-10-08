from __future__ import annotations

import argparse
import json


TASK_QUESTIONS: dict[str, list[str]] = {
    "ingest": [
        "Qual arquivo/processo deve ser preservado e ingerido?",
        "Você quer somente a base documental e a cobertura por página?",
        "Há sigilo, OCR ou revisão visual autorizada?",
    ],
    "analyze": [
        "Qual é a questão processual que deve orientar a análise?",
        "Qual profundidade e quais entregas deseja: cronologia, provas, decisões, riscos?",
        "Qual parte, órgão e número do processo?",
    ],
    "petition": [
        "Qual tipo de peça deve ser redigido?",
        "Qual órgão, processo, polo/parte e objetivo?",
        "Quais pedidos e fundamentos foram confirmados pelo usuário?",
        "Existe prazo informado e formato desejado?",
    ],
    "deadlines": [
        "Quais marcos ou intimações devem ser conferidos?",
        "Qual calendário e regra de contagem devem ser usados?",
        "Quem é o responsável pela providência?",
    ],
    "evidence": [
        "Qual fato controvertido ou hipótese deve ser mapeado?",
        "Deseja localizar, comparar ou avaliar apenas a existência das provas?",
        "Qual parte e qual intervalo de peças deve ser considerado?",
    ],
    "audit": [
        "Você autoriza a auditoria completa e todos os relatórios?",
        "Qual arquivo/processo, nível de detalhe e formato de saída?",
        "Há restrições de sigilo, OCR, visão ou compartilhamento?",
    ],
}


def questions_for_task(task: str) -> list[str]:
    if task not in TASK_QUESTIONS:
        raise ValueError(f"Tarefa desconhecida: {task}")
    return TASK_QUESTIONS[task]


def main() -> int:
    parser = argparse.ArgumentParser(description="Exibe perguntas de fallback para resolver ambiguidades de escopo.")
    parser.add_argument("task", choices=sorted(TASK_QUESTIONS))
    args = parser.parse_args()
    print(json.dumps({"task": args.task, "questions": questions_for_task(args.task)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
