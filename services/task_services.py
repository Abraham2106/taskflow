from models.tasks import Task, Priority, Status
from storage.repository import read, write
import typing 
from datetime import date, datetime

"""
CRUD de Taskflow CLI
"""
class TaskServices: 
    def __init__(self):
        self._tasks: list[Task] = read()

    def search_by_id(self, task_id : str, tasks  :list[Task] ) -> Task | None: 
        
        for task in tasks:
            if task.id == task_id:
                return task
            
            found = self.search_by_id(task_id, task.subtasks)
             
            if found != None:
                return found
            
        return None 
        
    def create(
            self,
            title: str,
            priority: Priority,
            status: Status,
            end_date : date | None,
            father_id : str | None,
            subtasks : list['Task'] | None = None,
        ) -> None:
        """ Creates a task based on the input received via CLI """
        
        task = Task(
        title=title,
        priority=priority,
        status=status,
        end_date=end_date,
        father_id=father_id
        )

        if father_id != None: 
            father_task = self.search_by_id(father_id, self._tasks)
            if father_task != None:
                father_task.subtasks.append(task)
        else:
            self._tasks.append(task)

        # Persistencia
        write(self._tasks)


    def update_status(self, task_id : str, new_status : Status) -> None:
        """ """ 
        task = self.search_by_id(task_id, self._tasks) 
        if task is not None:
            #  Set new status 
            task.status = new_status
        
        write(self._tasks)


    def read_task(self, task_id : str) -> None:
        """ Preliminar version of a read, for now it's just a simple print on the cli """
        task = self.search_by_id(task_id, self._tasks) 
        print(task)


if __name__ == "__main__": 

    creator = TaskServices()
    creator.read_task("994de100")


