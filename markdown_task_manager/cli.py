import argparse
from .task_manager import TaskManager
from .file_utils import FileUtils

def main():
    parser = argparse.ArgumentParser(description="Manage tasks in Markdown files.")
    parser.add_argument('command', choices=['init', 'a', 'c', 'l'], help="Command to run")
    parser.add_argument('-f', '--file', default='tasks.md', help="Markdown file to manage")
    parser.add_argument('-t', '--task', help="Task description")
    parser.add_argument('--gitignore', action='store_true', help="Add tasks file to .gitignore")

    args = parser.parse_args()

    task_manager = TaskManager(args.file)
    if args.command == 'init':
        FileUtils.create_task_file(args.file, args.gitignore)
    elif args.command == 'a':
        task_manager.add_task(args.task)
    elif args.command == 'c':
        task_manager.complete_task(args.task)
    elif args.command == 'l':
        task_manager.list_tasks()

if __name__ == "__main__":
    main()
