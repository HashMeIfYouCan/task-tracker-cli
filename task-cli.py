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
    return max((task['id'] for task in tasks), default=1) + 1

def help():
    ...

def add_task(description: str) -> None:
    tasks: List[Dict[str, Any]] = load_tasks()

    task_id: int = generate_task_id(tasks)
    time_now: str = datetime.now().isoformat()

    new_task: dict = {
        Task.ID: task_id,
        Task.DESCRIPTION: description,
        Task.STATUS: Status.TODO,
        Task.CREATED_AT: time_now,
        Task.UPDATED_AT: None
    }

    tasks.append(new_task)

    save_tasks(tasks)

def main():
    if len(sys.argv) < 2:
        return help()
    


if __name__ == '__main__':
    add_task(description="Test description")