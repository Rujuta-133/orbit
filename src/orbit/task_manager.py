from orbit.models import Task
import json

class TaskManager:
    def __init__(self, storage_path = "tasks.json"):
        self.storage_path = storage_path
        self.task_list: list[Task] = []
        self._load_from_file()
        
        
    def add_task(self, description: str):
        next_id = max((task.id for task in self.task_list), default=0) + 1
        task = Task(next_id, description)
        self.task_list.append(task)
        self._save_to_file()
        return task
    
    def list_current_tasks(self):
        current_tasks = self.task_list[:]
        return current_tasks
    
    def _load_from_file(self):
        try:
            with open(self.storage_path, "r") as file:
                stored_tasks = json.load(file)
                self.task_list = [Task.from_dict(task_data) for task_data in stored_tasks]
        except FileNotFoundError:
            pass

    def _save_to_file(self):
        serialized_tasks = [task.to_dict() for task in self.task_list]
        with open(self.storage_path, "w") as file:
            json.dump(serialized_tasks, file)   





