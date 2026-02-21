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
        
    else:
        print("Unknown command")

        

if __name__ == "__main__":
    main()



