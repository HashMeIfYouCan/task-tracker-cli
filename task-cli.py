import json
import sys
from enum import Enum
from datetime import datetime
from typing import List, Dict, Any

TASK_FILE = 'tasks.json'

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class Command(Enum):
    ADD = "add"
    LIST = "list"
    MARK = "mark"
    HELP = "--help"

class Task(Enum):
    ID = "id"
    DESCRIPTION = "description"
    STATUS = "status"
    CREATED_AT = "createdAt"
    UPDATED_AT = "updatedAt"


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
    return max((task['id'] for task in tasks), default=1) + 1

def help():
    ...

def add_task(description: str) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_id: int = generate_task_id(tasks)
    time_now: str = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

    new_task: dict = {
        Task.ID.value: task_id,
        Task.DESCRIPTION.value: description,
        Task.STATUS.value: Status.TODO.value,
        Task.CREATED_AT.value: time_now,
        Task.UPDATED_AT.value: None
    }

    tasks.append(new_task)

    save_tasks(tasks)

def main():
    ...
    


if __name__ == '__main__':
    add_task(input())