"""Task service module for managing CRUD operations in Taskflow CLI."""

from datetime import date, datetime
from typing import Optional

from models.tasks import Priority, Status, Task
from storage.repository import read, write


class TaskServices:
    """Service class for handling task operations including CRUD and search."""

    def __init__(self) -> None:
        """Initialize TaskServices and load tasks from storage."""
        self._tasks: list[Task] = read()

    def search_by_id(
        self, task_id: str, tasks: list[Task]
    ) -> Optional[Task]:
        """
        Search for a task by ID recursively through task hierarchy.

        Args:
            task_id: The ID of the task to search for.
            tasks: The list of tasks to search through.

        Returns:
            The Task object if found, None otherwise.

        Note:
            Time complexity is O(n). Future versions should use a database
            for better performance with large task sets.
        """
        for task in tasks:
            if task.id == task_id:
                return task

            found = self.search_by_id(task_id, task.subtasks)
            if found is not None:
                return found

        return None

    def create(
        self,
        title: str,
        priority: Priority,
        status: Status,
        end_date: Optional[date] = None,
        father_id: Optional[str] = None,
        subtasks: Optional[list[Task]] = None,
    ) -> None:
        """
        Create a new task based on input received via CLI.

        Args:
            title: The title of the task.
            priority: The priority level of the task.
            status: The status of the task.
            end_date: Optional end date for the task.
            father_id: Optional parent task ID for subtask relationships.
            subtasks: Optional list of subtasks.

        Note:
            TODO: This implementation has O(n) search complexity. When scaling
            to handle many tasks, consider migrating to a database backend
            for improved performance.
        """
        task = Task(
            title=title,
            priority=priority,
            status=status,
            end_date=end_date,
            father_id=father_id,
        )

        if father_id is not None:
            father_task = self.search_by_id(father_id, self._tasks)
            if father_task is not None:
                father_task.subtasks.append(task)
        else:
            self._tasks.append(task)

        # Persist changes to storage
        write(self._tasks)

    def update_status(self, task_id: str, new_status: Status) -> None:
        """
        Update the status of a task by its ID.

        Args:
            task_id: The ID of the task to update.
            new_status: The new status to set.
        """
        task = self.search_by_id(task_id, self._tasks)
        if task is not None:
            task.status = new_status
            write(self._tasks)

    def read_task(self, task_id: str) -> None:
        """
        Retrieve and display a task by its ID.

        Args:
            task_id: The ID of the task to read.

        Note:
            This is a preliminary implementation that prints to CLI.
            Future versions should return the task object instead.
        """
        task = self.search_by_id(task_id, self._tasks)
        print(task)


if __name__ == "__main__":
    creator = TaskServices()
    creator.read_task("994de100")



