from __future__ import annotations

from pathlib import Path

from controle_estudos.core import StudyTracker
from controle_estudos.storage import load_data, save_data

DATA_FILE = Path("data/study_data.json")


def show_menu() -> None:
    print("\n=== Controle de Estudos ===")
    print("1 - Adicionar matéria")
    print("2 - Listar matérias")
    print("3 - Registrar estudo")
    print("4 - Ver histórico")
    print("5 - Ver total de minutos por matéria")
    print("0 - Sair")


def add_subject_flow(tracker: StudyTracker) -> None:
    subject = input("Digite o nome da matéria: ")
    added = tracker.add_subject(subject)
    print(f"Matéria '{added}' cadastrada com sucesso.")



def list_subjects_flow(tracker: StudyTracker) -> None:
    subjects = tracker.list_subjects()
    if not subjects:
        print("Nenhuma matéria cadastrada.")
        return

    print("\nMatérias cadastradas:")
    for index, subject in enumerate(subjects, start=1):
        print(f"{index}. {subject}")



def register_study_flow(tracker: StudyTracker) -> None:
    subject = input("Digite a matéria estudada: ")
    duration_text = input("Digite a duração do estudo em minutos: ")
    notes = input("Observações (opcional): ")

    duration = int(duration_text)
    record = tracker.register_study(subject, duration, notes)
    print(
        "Estudo registrado com sucesso: "
        f"{record.subject} - {record.duration_minutes} minutos."
    )



def show_history_flow(tracker: StudyTracker) -> None:
    history = tracker.get_history()
    if not history:
        print("Nenhum estudo registrado até o momento.")
        return

    print("\nHistórico de estudos:")
    for index, item in enumerate(history, start=1):
        notes = item["notes"] if item["notes"] else "Sem observações"
        print(
            f"{index}. {item['subject']} | {item['duration_minutes']} min | "
            f"{item['studied_at']} | {notes}"
        )



def show_total_minutes_flow(tracker: StudyTracker) -> None:
    subject = input("Digite a matéria para consultar o total estudado: ")
    total = tracker.total_minutes_by_subject(subject)
    print(f"Total estudado em {subject.strip()}: {total} minutos.")



def main() -> None:
    tracker = StudyTracker(load_data(DATA_FILE))

    actions = {
        "1": add_subject_flow,
        "2": list_subjects_flow,
        "3": register_study_flow,
        "4": show_history_flow,
        "5": show_total_minutes_flow,
    }

    while True:
        show_menu()
        option = input("Escolha uma opção: ").strip()

        if option == "0":
            save_data(DATA_FILE, tracker.to_dict())
            print("Dados salvos. Até logo!")
            break

        action = actions.get(option)
        if action is None:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            action(tracker)
            save_data(DATA_FILE, tracker.to_dict())
        except ValueError as error:
            print(f"Erro: {error}")
        except Exception as error:  # pragma: no cover - defensive fallback
            print(f"Ocorreu um erro inesperado: {error}")


if __name__ == "__main__":
    main()
