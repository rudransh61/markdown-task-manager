import os

class FileUtils:
    @staticmethod
    def create_task_file(file_name, gitignore):
        directory = './.md-task/'
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory {directory}")

        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("# Tasks\n\n")
            print(f"{file_path} created.")
        else:
            print(f"{file_path} already exists.")
        
        if gitignore:
            FileUtils.add_to_gitignore(file_path)

    @staticmethod
    def add_to_gitignore(file_path):
        gitignore_path = '.gitignore'
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'a') as f:
                f.write(f'\n{file_path}')
            print(f"Added {file_path} to .gitignore.")
        else:
            with open(gitignore_path, 'w') as f:
                f.write(f'{file_path}\n')
            print(f"Created .gitignore and added {file_path}.")
