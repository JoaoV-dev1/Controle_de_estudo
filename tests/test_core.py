from controle_estudos.core import StudyTracker


def test_add_subject_successfully() -> None:
    tracker = StudyTracker()

    added = tracker.add_subject("Matemática")

    assert added == "Matemática"
    assert tracker.list_subjects() == ["Matemática"]



def test_add_subject_rejects_empty_name() -> None:
    tracker = StudyTracker()

    try:
        tracker.add_subject("   ")
        raise AssertionError("Era esperado ValueError para matéria vazia.")
    except ValueError as error:
        assert str(error) == "O nome da matéria não pode ser vazio."



def test_register_study_rejects_unknown_subject() -> None:
    tracker = StudyTracker()

    try:
        tracker.register_study("Física", 30)
        raise AssertionError("Era esperado ValueError para matéria não cadastrada.")
    except ValueError as error:
        assert str(error) == "A matéria informada não está cadastrada."



def test_register_study_stores_history() -> None:
    tracker = StudyTracker({"subjects": ["História"], "history": []})

    tracker.register_study("História", 45, "Revisão para prova", "2026-04-12 10:00:00")

    history = tracker.get_history()
    assert len(history) == 1
    assert history[0]["subject"] == "História"
    assert history[0]["duration_minutes"] == 45



def test_total_minutes_by_subject() -> None:
    tracker = StudyTracker({"subjects": ["Biologia"], "history": []})
    tracker.register_study("Biologia", 20, studied_at="2026-04-12 09:00:00")
    tracker.register_study("Biologia", 40, studied_at="2026-04-12 18:00:00")

    assert tracker.total_minutes_by_subject("Biologia") == 60
