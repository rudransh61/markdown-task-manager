import unittest
from markdown_task_manager.file_utils import FileUtils
import os

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.file_name = "test_tasks.md"

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                lines = f.readlines()
            with open('.gitignore', 'w') as f:
                for line in lines:
                    if line.strip() != self.file_name:
                        f.write(line)

    def test_create_task_file(self):
        FileUtils.create_task_file(self.file_name, gitignore=False)
        self.assertTrue(os.path.exists(self.file_name))

    def test_add_to_gitignore(self):
        FileUtils.create_task_file(self.file_name, gitignore=True)
        with open('.gitignore', 'r') as f:
            content = f.read()
        self.assertIn(self.file_name, content)

if __name__ == '__main__':
    unittest.main()
