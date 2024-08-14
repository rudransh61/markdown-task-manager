import unittest
from markdown_task_manager.task_manager import TaskManager
import os

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_tasks.md"
        with open(self.file_name, 'w') as f:
            f.write("# Tasks\n\n")

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_add_task(self):
        manager = TaskManager(self.file_name)
        manager.add_task("Write unit tests")
        with open(self.file_name, 'r') as f:
            content = f.read()
        self.assertIn("- [ ] Write unit tests", content)

    def test_complete_task(self):
        manager = TaskManager(self.file_name)
        manager.add_task("Write unit tests")
        manager.complete_task("Write unit tests")
        with open(self.file_name, 'r') as f:
            content = f.read()
        self.assertIn("- [x] Write unit tests", content)

if __name__ == '__main__':
    unittest.main()
