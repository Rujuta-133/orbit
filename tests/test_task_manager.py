from orbit.task_manager import TaskManager
import os

def test_add_task():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")
    task = manager.add_task("Test Task")

    assert task.id == 1
    assert task.description == "Test Task"
    assert not task.completed 

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

def test_multiple_tasks():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")

    assert task1.id == 1
    assert task2.id == 2
    assert task1.description == "Task 1"
    assert task2.description == "Task 2"
    assert not task1.completed
    assert not task2.completed
    assert len(manager.task_list) == 2

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

def test_delete_tasks():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    task3 = manager.add_task("Task 3")
    deleted_task = manager.delete_task(1)

    assert deleted_task.id == 1
    assert len(manager.task_list) == 2

    remaining_ids = [task.id for task in manager.task_list]
    assert 1 not in remaining_ids

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")


def test_delete_nonexistent_task():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")
    task = manager.add_task("Task 1")
    deleted = manager.delete_task(999)

    assert deleted is None

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")



def test_mark_completed():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")

    task = manager.add_task("Task 1")
    updated = manager.mark_completed(1)

    assert updated is not None
    assert updated.id == 1
    assert updated.completed is True

    # check state inside manager
    assert manager.task_list[0].completed is True

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")


def test_mark_completed_idempotent():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")

    manager.add_task("Task 1")

    first = manager.mark_completed(1)
    second = manager.mark_completed(1)

    assert first.completed is True
    assert second.completed is True

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")


def test_mark_completed_nonexistent():
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")

    manager = TaskManager("test_tasks.json")

    result = manager.mark_completed(999)

    assert result is None

    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")



    


