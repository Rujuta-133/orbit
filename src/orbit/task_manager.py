from orbit.models import Task


class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.task_list  = self.storage.load()
        
        
        
    def add_task(self, description: str):
        next_id = max((task.id for task in self.task_list), default=0) + 1
        task = Task(next_id, description)
        self.task_list.append(task)
        self.storage.save(self.task_list)
        return task
    
    def list_current_tasks(self):
        current_tasks = self.task_list[:]
        return current_tasks


    
    def delete_task(self, task_id: int):
        task_to_delete = None
        for task in self.task_list:
            if task.id == task_id:
                task_to_delete = task
                break
        
        if task_to_delete is not None:
            self.task_list.remove(task_to_delete)
            self.storage.save(self.task_list)
            return task_to_delete
        else:
            return None
        

    def mark_completed(self, task_id: int):
        for task in self.task_list:
            if task.id == task_id:
                if not task.completed:
                    task.completed = True
                    self.storage.save(self.task_list)
                    return task
                else:
                    return task
    
        return None
    
    def update_task(self, task_id: int, description: str):
        for task in self.task_list:
            if task.id == task_id:
                task.description = description
                self.storage.save(self.task_list)
                return task
        return None






