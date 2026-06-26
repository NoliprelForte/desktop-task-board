class Task:
    def __init__(self, title: str, status: str = "Backlog") -> None:
        self.title = title
        self.status = status

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, task_data: dict) -> "Task":
        return cls(
            title=task_data["title"],
            status=task_data.get("status", "Backlog")
        )