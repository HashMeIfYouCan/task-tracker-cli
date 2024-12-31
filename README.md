# Task Tracker CLI

A simple command-line interface (CLI) tool for managing tasks. This tool allows you to add, list, update, delete, and mark tasks with different statuses.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SanthoshDatturi/task-tracker-cli.git
    ```
2. Navigate to the project directory:
    ```sh
    cd task-tracker-cli
    ```
3. Build the executable (assuming you have PyInstaller installed):
    ```sh
    pyinstaller --onefile task_cli.py
    ```

## Usage

Run the CLI tool using the following command:
```sh
task_cli [command] [options]
```

### Commands

- `add <description>`: Add a new task with the given description.
- `list [status]`: List all tasks or tasks with a specific status (`todo`, `in-progress`, `done`).
- `update <id> <description>`: Update the description of a task with the given ID.
- `delete <id>`: Delete the task with the given ID.
- `mark-todo <id>`: Mark the task with the given ID as "todo".
- `mark-in-progress <id>`: Mark the task with the given ID as "in-progress".
- `mark-done <id>`: Mark the task with the given ID as "done".
- `--help`: Show help information.

### Examples

- Add a new task:
    ```sh
    task_cli add "Finish the report"
    ```

- List all tasks:
    ```sh
    task_cli list
    ```

- List tasks with a specific status:
    ```sh
    task_cli list todo
    ```

- Update a task description:
    ```sh
    task_cli update 1 "Finish the report and send it to the manager"
    ```

- Delete a task:
    ```sh
    task_cli delete 1
    ```

- Mark a task as "in-progress":
    ```sh
    task_cli mark-in-progress 1
    ```

## Project URL
     ```sh
    [Task Tracker Project](https://roadmap.sh/projects/task-tracker)
     ```
