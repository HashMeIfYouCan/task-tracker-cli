import unittest
from unittest.mock import patch, mock_open
from task_cli import (
    load_tasks, save_tasks, generate_task_id, add_task, list_tasks,
    update_task_description, delete_task, mark_task, get_task_index
)
from constants import Task, Status

class TestTaskCLI(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[]')
    def test_load_tasks(self, mock_file):
        tasks = load_tasks()
        self.assertEqual(tasks, [])
        mock_file.assert_called_once_with('tasks.json', 'r')

    @patch("builtins.open", new_callable=mock_open)
    def test_save_tasks(self, mock_file):
        tasks = [{"id": 1, "description": "Test Task"}]
        save_tasks(tasks)
        mock_file.assert_called_once_with('tasks.json', 'w')

    def test_generate_task_id(self):
        tasks = [{"id": 1}, {"id": 2}]
        new_id = generate_task_id(tasks)
        self.assertEqual(new_id, 3)

    @patch("task_cli.load_tasks", return_value=[])
    @patch("task_cli.save_tasks")
    def test_add_task(self, mock_save_tasks, mock_load_tasks):
        add_task("New Task")
        mock_save_tasks.assert_called_once()

    @patch("task_cli.load_tasks", return_value=[])
    def test_list_tasks(self, mock_load_tasks):
        with patch('builtins.print') as mocked_print:
            list_tasks()
            self.assertTrue(mocked_print.called)

    @patch("task_cli.load_tasks", return_value=[{"id": 1, "description": "Test Task", "status": Status.TODO}])
    @patch("task_cli.save_tasks")
    def test_update_task_description(self, mock_save_tasks, mock_load_tasks):
        update_task_description(1, "Updated Task")
        mock_save_tasks.assert_called_once()

    @patch("task_cli.load_tasks", return_value=[{"id": 1, "description": "Test Task"}])
    @patch("task_cli.save_tasks")
    def test_delete_task(self, mock_save_tasks, mock_load_tasks):
        delete_task(1)
        mock_save_tasks.assert_called_once()

    @patch("task_cli.load_tasks", return_value=[{"id": 1, "description": "Test Task", "status": Status.TODO}])
    @patch("task_cli.save_tasks")
    def test_mark_task(self, mock_save_tasks, mock_load_tasks):
        mark_task(1, Status.DONE)
        mock_save_tasks.assert_called_once()

    def test_get_task_index(self):
        tasks = [{"id": 1}, {"id": 2}]
        index = get_task_index(2, tasks)
        self.assertEqual(index, 1)

if __name__ == '__main__':
    unittest.main()
