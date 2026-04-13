from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Any

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass
class StudyRecord:
    subject: str
    duration_minutes: int
    notes: str
    studied_at: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class StudyTracker:
    def __init__(self, data: dict[str, Any] | None = None) -> None:
        self.subjects: list[str] = []
        self.history: list[StudyRecord] = []

        if data:
            self.subjects = list(data.get("subjects", []))
            self.history = [StudyRecord(**item) for item in data.get("history", [])]

    def to_dict(self) -> dict[str, Any]:
        return {
            "subjects": self.subjects,
            "history": [record.to_dict() for record in self.history],
        }

    def add_subject(self, subject: str) -> str:
        normalized = subject.strip()
        if not normalized:
            raise ValueError("O nome da matéria não pode ser vazio.")
        if normalized in self.subjects:
            raise ValueError("A matéria já foi cadastrada.")

        self.subjects.append(normalized)
        self.subjects.sort()
        return normalized

    def list_subjects(self) -> list[str]:
        return list(self.subjects)

    def register_study(
        self,
        subject: str,
        duration_minutes: int,
        notes: str = "",
        studied_at: str | None = None,
    ) -> StudyRecord:
        normalized = subject.strip()
        if normalized not in self.subjects:
            raise ValueError("A matéria informada não está cadastrada.")
        if duration_minutes <= 0:
            raise ValueError("A duração do estudo deve ser maior que zero.")

        timestamp = studied_at or datetime.now().strftime(DATE_FORMAT)
        record = StudyRecord(
            subject=normalized,
            duration_minutes=duration_minutes,
            notes=notes.strip(),
            studied_at=timestamp,
        )
        self.history.append(record)
        return record

    def get_history(self) -> list[dict[str, Any]]:
        return [record.to_dict() for record in self.history]

    def total_minutes_by_subject(self, subject: str) -> int:
        normalized = subject.strip()
        return sum(
            record.duration_minutes
            for record in self.history
            if record.subject == normalized
        )
