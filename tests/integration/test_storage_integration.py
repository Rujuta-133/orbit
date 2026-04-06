from orbit.task_manager import TaskManager
from orbit.storage import JSONStorage
import os 

def test_storage_integration():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    storage = JSONStorage("test_tasks.json")
    manager = TaskManager(storage)

    manager.add_task("Test Task")

    manager1 = TaskManager(storage)

    tasks = manager1.list_current_tasks()
    
    assert len(tasks) == 1
    assert tasks[0].id == 1
    assert tasks[0].description == "Test Task"
    assert tasks[0].completed is False

    # Step 5: Cleanup after test
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")
    