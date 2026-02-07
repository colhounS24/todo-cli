import json
from typing import List, Dict, Optional
from datetime import date


class ToDoList:
    def __init__(self, path: str = "tasks.json"):
        self.path = path
        self.tasks: List[Dict] = []
        self.load()

    def load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2, ensure_ascii=False)

    def add(self, title: str, due: Optional[str] = None) -> None:
        # `due` should be an ISO date string (YYYY-MM-DD) or None
        self.tasks.append({"title": title, "done": False, "due": due})
        self.save()

    def list(self) -> List[Dict]:
        return self.tasks

    def complete(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save()
            return True
        return False

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()
            return True
        return False

    def clear(self) -> None:
        self.tasks = []
        self.save()

    def overdue(self) -> List[Dict]:
        today = date.today()
        overdue = []
        for t in self.tasks:
            d = t.get("due")
            if d and not t.get("done"):
                try:
                    if date.fromisoformat(d) < today:
                        overdue.append(t)
                except Exception:
                    continue
        return overdue
