from orbit.models import Task

class TaskManager:
    def __init__(self):
        self.task_list: list[Task] = []
        
        
    def add_task(self, description: str):
        next_id = len(self.task_list) + 1
        task = Task(next_id, description)
        self.task_list.append(task)
        return task
    
    def list_current_tasks(self):
        current_tasks = self.task_list[:]
        return current_tasks
