from orbit.task_manager import TaskManager
from orbit.storage import InMemoryStorage

def test_add_task():
    storage = InMemoryStorage()
    manager = TaskManager(storage)
    task = manager.add_task("Test Task")

    assert task.id == 1
    assert task.description == "Test Task"
    assert not task.completed 

  

def test_multiple_tasks():

    storage = InMemoryStorage()
    manager = TaskManager(storage)
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")

    assert task1.id == 1
    assert task2.id == 2
    assert task1.description == "Task 1"
    assert task2.description == "Task 2"
    assert not task1.completed
    assert not task2.completed
    assert len(manager.task_list) == 2

    

def test_delete_tasks():

    storage = InMemoryStorage()
    manager = TaskManager(storage)
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    task3 = manager.add_task("Task 3")
    deleted_task = manager.delete_task(1)

    assert deleted_task.id == 1
    assert len(manager.task_list) == 2

    remaining_ids = [task.id for task in manager.task_list]
    assert 1 not in remaining_ids


def test_delete_nonexistent_task():

    storage = InMemoryStorage()
    manager = TaskManager(storage)
    task = manager.add_task("Task 1")
    deleted = manager.delete_task(999)

    assert deleted is None



def test_mark_completed():

    storage = InMemoryStorage()
    manager = TaskManager(storage)
    task = manager.add_task("Task 1")
    updated = manager.mark_completed(1)

    assert updated is not None
    assert updated.id == 1
    assert updated.completed is True

    # check state inside manager
    assert manager.task_list[0].completed is True



def test_mark_completed_idempotent():
    storage = InMemoryStorage()
    manager = TaskManager(storage)

    manager.add_task("Task 1")

    first = manager.mark_completed(1)
    second = manager.mark_completed(1)

    assert first.completed is True
    assert second.completed is True


def test_mark_completed_nonexistent():
    storage = InMemoryStorage()
    manager = TaskManager(storage)

    result = manager.mark_completed(999)

    assert result is None


def test_update_task():
    storage = InMemoryStorage()
    manager = TaskManager(storage)

    task1 = manager.add_task("Test 1")
    updated = manager.update_task(1, "Test Task Updated")
    
    assert updated is not None
    assert task1.description == "Test Task Updated"
    assert task1.id == 1

    assert manager.task_list[0].description == "Test Task Updated"

def test_nonexistent_update_task():
    
    storage = InMemoryStorage()
    manager = TaskManager(storage)

    updated = manager.update_task(999, "Test Task Updated")

    assert updated is None







    


