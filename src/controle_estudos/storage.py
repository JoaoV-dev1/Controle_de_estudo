from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_DATA = {"subjects": [], "history": []}


def ensure_data_file(path: str | Path) -> Path:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists():
        file_path.write_text(
            json.dumps(DEFAULT_DATA, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    return file_path


def load_data(path: str | Path) -> dict[str, Any]:
    file_path = ensure_data_file(path)
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_data(path: str | Path, data: dict[str, Any]) -> None:
    file_path = ensure_data_file(path)
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
