from orbit.task_manager import TaskManager
import sys


def main():
    if len(sys.argv) < 2:
        print("Please write a command as 'orbit <command>'")
        print("Example: 'orbit list'")
        sys.exit()

    command = sys.argv[1]
    commands = {
        "list" : handle_list,
        "add" : handle_add,
        "delete" : handle_delete,
        "complete" : handle_complete
    }
    

    handler = commands.get(command)
    
    if handler:
        manager = TaskManager()
        handler(manager, sys.argv[2:])
        return
    else:
        print("Unknown command")



def handle_list(manager, args):
    if len(args) != 0:
        print("List command does not take any arguments")
        sys.exit()

    tasks = manager.list_current_tasks()
    if len(tasks) == 0:
        print("No tasks found")
    else:
        for task in tasks:
            print(task)

def handle_add(manager, args):
    if len(args) < 1:
        print("Description required")
        sys.exit()

    description = args[0]
    task = manager.add_task(description)
    print(f"Added task: {task.id} {task.description}")

def handle_delete(manager, args):
    if len(args) < 1:
            print("Task ID required")
            sys.exit()

    task_id_str = args[0]
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

def handle_complete(manager, args):
    if len(args) < 1:
        print("Task ID required")
        sys.exit()
    
    task_id_str = args[0]
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



if __name__ == "__main__":
    main()



