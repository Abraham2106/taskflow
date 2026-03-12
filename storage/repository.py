import datetime as dt
import json

from ..models.tasks import Priority, Status, Task

JSON_PATH = "tasks.json"


def task_to_dict(task: Task) -> dict:
    return {
        "id": task.id,
        "title": task.title,
        "priority": task.priority.name,
        "status": task.status.name,
        "end_date": task.end_date.isoformat() if task.end_date else None,
        "father_id": task.father_id,
        "subtasks": [task_to_dict(t) for t in task.subtasks],
    }


def dict_to_task(data: dict) -> Task:
    task = Task(
        title=data["title"],
        priority=Priority[data["priority"]],
        status=Status[data["status"]],
        end_date=dt.date.fromisoformat(data["end_date"]) if data["end_date"] else None,
        father_id=data["father_id"],
        id=data["id"],
    )
    task.subtasks = [dict_to_task(t) for t in data["subtasks"]]

    return task


def read() -> list["Task"]:
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    return [dict_to_task(task_data) for task_data in data]


def write(tasks: list["Task"]) -> None:
    data = [task_to_dict(task) for task in tasks]

    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    print(read())
