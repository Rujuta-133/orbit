from orbit.models import Task
import json


class InMemoryStorage:
    def __init__(self):
        self.storage_list = []

    def load(self):
        return self.storage_list[:]
        
    def save(self, tasks):
        self.storage_list = tasks[:]

class JSONStorage:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        try:
            with open(self.filepath, "r") as file:
                stored_tasks = json.load(file)
                task_list = [Task.from_dict(task_data) for task_data in stored_tasks]
                return task_list
        except FileNotFoundError:
            return [] 
        
    def save(self, tasks):
        serialized_tasks = [task.to_dict() for task in tasks]
        with open(self.filepath, "w") as file:
            json.dump(serialized_tasks, file)



