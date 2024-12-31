import json
import sys
from datetime import datetime
from typing import List, Dict, Any
from constants import Task, Command, Status

TASK_FILE = 'tasks.json'


def load_tasks() -> List[Dict[str, Any]]:
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def generate_task_id(tasks: List[Dict[str, Any]]) -> int:
    return max((task['id'] for task in tasks), default=0) + 1


def help():
    print("Usage: task-cli [command] [options]")
    print("\nCommands:")
    print("  add <description>         Add a new task")
    print("  list [status]             List all tasks or tasks with specific status")
    print("  update <id> <description> Update a task description")
    print("  delete <id>               Delete a task")
    print("  mark-todo <id>            Mark a task as todo")
    print("  mark-in-progress <id>     Mark a task as in progress")
    print("  mark-done <id>            Mark a task as done")
    print("  --help                    Show help")


def add_task(description: str) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_id: int = generate_task_id(tasks)
    time_now: str = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    new_task: dict = {
        Task.ID: task_id,
        Task.DESCRIPTION: description,
        Task.STATUS: Status.TODO,
        Task.CREATED_AT: time_now,
        Task.UPDATED_AT: None
    }

    tasks.append(new_task)

    save_tasks(tasks)


def list_tasks(status: str = None) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    if status is None:
        filtered_tasks: List[Dict[str, Any]] = tasks
    else:
        filtered_tasks: List[Dict[str, Any]] = [task for task in tasks if task[Task.STATUS] == status]

    len_largest_description: int = max((len(task[Task.DESCRIPTION]) for task in tasks), default=0)

    print(f"{'-' * (70 + len_largest_description)}")
    print(f"| {'ID':<5} | {'Description':<{len_largest_description}} | {'Status':<11} | {'Created At':<19} | {'Updated At':<19} |")
    print(f"{'-' * (70 + len_largest_description)}")

    for task in filtered_tasks:
        print(f"| {task[Task.ID]:<5} | {task[Task.DESCRIPTION]:<{len_largest_description}} "
              f"| {task[Task.STATUS]:<11} | {task[Task.CREATED_AT]:<19} "
              f"| {(task[Task.UPDATED_AT] if task[Task.UPDATED_AT] else 'No Update'):<19} |")

    print(f"{'-' * (70 + len_largest_description)}")


def get_task_index(task_id: int, tasks: List[Dict[str, Any]]) -> int:
    for task_index, task in enumerate(tasks):
        if task[Task.ID] == task_id:
            return task_index
    return -1


def update_task_description(task_id: int, new_description: str) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_index: int = get_task_index(task_id, tasks)

    if task_index == -1:
        print(f"Task with ID {task_id} not found")
        return

    if tasks[task_index][Task.STATUS] == Status.DONE:
        print(f"Task with ID {task_id} is already marked as done")
        return
    
    tasks[task_index][Task.DESCRIPTION] = new_description
    tasks[task_index][Task.UPDATED_AT] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    save_tasks(tasks)

    print(f"Task with ID {task_id} updated successfully")


def delete_task(task_id: int) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_index: int = get_task_index(task_id, tasks)

    if task_index == -1:
        print(f"Task with ID {task_id} not found")
        return

    del tasks[task_index]

    save_tasks(tasks)

    print(f"Task with ID {task_id} deleted successfully")


def mark_task(task_id: int, status: str) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_index: int = get_task_index(task_id, tasks)

    if task_index == -1:
        print(f"Task with ID {task_id} not found")
        return

    tasks[task_index][Task.STATUS] = status
    tasks[task_index][Task.UPDATED_AT] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    save_tasks(tasks)

    print(f"Task with ID {task_id} marked as {status}")


def main():
    if len(sys.argv) < 2:
        print("--Insufficient arguments, see help--")
        help()
        return
    
    if sys.argv[1] == Command.HELP:
        help()
    
    elif sys.argv[1] == Command.ADD:
        if len(sys.argv) < 3:
            print("Task description is missing")
            help()
            return
        add_task(sys.argv[2])
    
    elif sys.argv[1] == Command.LIST:
        list_tasks(sys.argv[2] if len(sys.argv) == 3 else None)
    
    elif sys.argv[1] == Command.DELETE:
        if len(sys.argv) < 3:
            print("Task ID is missing")
            help()
            return
        delete_task(int(sys.argv[2]))
    
    elif sys.argv[1] == Command.UPDATE:
        if len(sys.argv) < 4:
            print("Task ID or new description is missing")
            help()
            return
        update_task_description(int(sys.argv[2]), sys.argv[3])
    
    elif sys.argv[1][:4] == Command.MARK:
        if len(sys.argv) < 3:
            print("Task ID or status is missing")
            help()
            return
        if sys.argv[1][5:] not in [Status.TODO, Status.IN_PROGRESS, Status.DONE]:
            print("Status is not identified, see help")
            help()
            return
        mark_task(int(sys.argv[2]), sys.argv[1][5:])
    
    else:
        print("Command is not identified, see help")
        help()


if __name__ == '__main__':
    main()