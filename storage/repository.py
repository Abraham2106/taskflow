"""Repository module for persisting and retrieving task data."""

import datetime as dt
import json

from models.tasks import Priority, Status, Task

JSON_PATH = "tasks.json"


def task_to_dict(task: Task) -> dict:
    """
    Convert a Task object to a dictionary representation.

    Args:
        task: The Task object to convert.

    Returns:
        A dictionary containing all task data and its subtasks.
    """
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
    """
    Convert a dictionary representation back to a Task object.

    Args:
        data: The dictionary containing task data.

    Returns:
        A Task object reconstructed from the dictionary.
    """
    task = Task(
        title=data["title"],
        priority=Priority[data["priority"]],
        status=Status[data["status"]],
        end_date=dt.date.fromisoformat(data["end_date"])
        if data["end_date"]
        else None,
        father_id=data["father_id"],
        id=data["id"],
    )
    task.subtasks = [dict_to_task(t) for t in data["subtasks"]]

    return task


def read() -> list[Task]:
    """
    Read all tasks from the JSON file.

    Returns:
        A list of Task objects. Returns an empty list if file doesn't exist.
    """
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    return [dict_to_task(task_data) for task_data in data]


def write(tasks: list[Task]) -> None:
    """
    Write all tasks to the JSON file.

    Args:
        tasks: The list of Task objects to persist.
    """
    data = [task_to_dict(task) for task in tasks]

    with open(JSON_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    print(read())

