class TaskManager:
    def __init__(self, file_name='.md-task/tasks.md'):
        self.file_name = file_name

    def normalize_task(self, task):
        """Normalize task string for comparison."""
        return task.strip().lower()

    def add_task(self, task, tag=None):
        if not task:
            raise ValueError("Task description cannot be empty.")
        tag_str = f" #{tag}" if tag else ""
        with open(self.file_name, 'a') as f:
            f.write(f'- [ ] {task}{tag_str}\n')

    def complete_task(self, task):
        normalized_task = self.normalize_task(task)
        task_found = False
        with open(self.file_name, 'r') as f:
            tasks = f.readlines()

        with open(self.file_name, 'w') as f:
            for line in tasks:
                # Extract the task description part for comparison
                if line.startswith('- [ ]'):
                    task_description = line[4:].strip()  # Remove the checkbox part
                    if self.normalize_task(task_description).startswith(normalized_task):
                        f.write(line.replace('- [ ]', '- [x]'))
                        task_found = True
                    else:
                        f.write(line)
                else:
                    f.write(line)

        if not task_found:
            raise ValueError(f"Task '{task}' not found.")

    def delete_task(self, task):
        normalized_task = self.normalize_task(task)
        deleted = False
        with open(self.file_name, 'r') as f:
            tasks = f.readlines()

        with open(self.file_name, 'w') as f:
            for line in tasks:
                # Extract the task description part for comparison
                if line.startswith('- [ ]') or line.startswith('- [x]'):
                    task_description = line[4:].strip()  # Remove the checkbox part
                    if self.normalize_task(task_description).startswith(normalized_task):
                        deleted = True
                        continue  # Skip writing this line
                f.write(line)

        if not deleted:
            raise ValueError(f"Task '{task}' not found.")

    def list_tasks(self):
        with open(self.file_name, 'r') as f:
            return f.readlines()
