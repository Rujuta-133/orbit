from orbit.task_manager import TaskManager


def main():
    print("Orbit running")
    manager = TaskManager()
    first_task = manager.add_task("First Task")
    second_task = manager.add_task("Second Task")
    tasks = manager.list_current_tasks()
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()



