from orbit.task_manager import TaskManager
import sys


def main():
    if len(sys.argv) < 2:
        print("Please write a command as 'orbit <command>'")
        print("Example: 'orbit list'")
        sys.exit()

    command = sys.argv[1]
    manager = TaskManager()
    if command == "list":
        
        tasks = manager.list_current_tasks()
        if len(tasks) == 0:
            print("No tasks found")
        else:
            for task in tasks:
                print(task)
    elif command == "add":
        if len(sys.argv) < 3:
            print("Description Required")
            sys.exit()
            
        description = sys.argv[2]
        task = manager.add_task(description)
        print(f"Added task: {task.id} {task.description}")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Task ID required")
            sys.exit()
        
        task_id_str = sys.argv[2]
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Task ID must be an integer")
            sys.exit()
        delete_task_object = manager.delete_task(task_id)
        if delete_task_object is None:
            print("Task not found")
        else:
            print(f"Deleted Task: {delete_task_object.id} {delete_task_object.description}")

    elif command == "complete":
        if len(sys.argv) < 3:
            print("Task ID required")
            sys.exit()

        task_id_str = sys.argv[2]
        try:
            task_id = int(task_id_str)
        except ValueError:
            print("Task ID must be an integer")
            sys.exit()
        complete_task_object = manager.mark_completed(task_id)
        if complete_task_object is None:
            print("Task not found")
        else:
            print("Task marked as completed")

    else:
        print("Unknown command")

        

if __name__ == "__main__":
    main()



