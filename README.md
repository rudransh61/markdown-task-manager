# Markdown-based Task Manager

A flexible and user-friendly task manager that leverages Markdown files for task management. Features include task creation, completion, deletion, and listing, with support for tags and a basic web interface. This project also supports AI-powered task prioritization and customizable templates.

## Features

- **Task Management**: Add, complete, delete, and list tasks.
- **Tagging**: Add tags to tasks for better organization.
- **AI-Powered Prioritization**: Get intelligent task prioritization and suggestions (experimental).
- **Customizable Templates**: Create and use task templates.
- **Web Interface**: Manage tasks via a simple web UI styled with Bootstrap.
- **Real-Time Updates**: Collaborate with others with real-time task updates (experimental).

## Installation

### Prerequisites

- Python 3.7+
- Virtualenv

### Setting Up the Project

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/rudransh61/markdown-task-manager.git
    cd markdown-task-manager
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Web Server:**
    ```bash
    python app.py
    ```

## Usage

### Command-Line Interface (CLI)

- **Initialize a New Task File:**
    ```bash
    python cli.py init [--gitignore]
    ```
    Creates a `.md-task/tasks.md` file for task management. Optionally add the file to `.gitignore`.

- **Add a New Task:**
    ```bash
    python cli.py add "Task description" [--tag TAG]
    ```
    Adds a new task with an optional tag.

- **Complete a Task:**
    ```bash
    python cli.py complete "Task description"
    ```
    Marks the specified task as completed.

- **Delete a Task:**
    ```bash
    python cli.py delete "Task description"
    ```
    Deletes the specified task.

- **List All Tasks:**
    ```bash
    python cli.py list
    ```
    Lists all tasks from the task file.

### Web Interface

1. **Open Your Web Browser:**
   - Navigate to `http://127.0.0.1:5000` to access the web interface.

2. **Interact with Tasks:**
   - Use the web interface to view, add, complete, and delete tasks.

## Advanced Features (Experimental)

- **AI-Powered Task Prioritization:** 
  Get intelligent suggestions for task priorities. 

- **Real-Time Collaboration:**
  Collaborate with others and see updates in real-time.

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. **Fork the Repository:**
    - Click the "Fork" button on GitHub to create a copy of the repository under your account.

2. **Clone Your Fork:**
    ```bash
    git clone https://github.com/rudransh61/markdown-task-manager.git
    ```

3. **Create a New Branch:**
    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Your Changes:**
    - Implement your changes or new features.

5. **Commit Your Changes:**
    ```bash
    git add .
    git commit -m "Add feature or fix bug"
    ```

6. **Push to Your Fork:**
    ```bash
    git push origin feature/your-feature-name
    ```

7. **Create a Pull Request:**
    - Go to the "Pull Requests" tab on GitHub and click "New Pull Request". Follow the instructions to submit your changes.

## Documentation

For detailed documentation and guides, please visit our [Wiki](https://github.com/rudransh61/markdown-task-manager/wiki).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Bootstrap](https://getbootstrap.com) for the web interface styling.
- [NLP Model](https://huggingface.co/models) for AI-powered prioritization (if applicable).

---

Feel free to reach out with any questions or suggestions. Thank you for your interest in the Markdown-based Task Manager!

