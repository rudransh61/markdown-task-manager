from flask import Flask, render_template, request, redirect, url_for, flash
from .task_manager import TaskManager

app = Flask(__name__)
app.secret_key = "supersecretkey"
task_manager = TaskManager()

@app.route('/')
def index():
    try:
        tasks = task_manager.list_tasks()
    except FileNotFoundError:
        flash("Task file not found. Please initialize the task manager.", "danger")
        tasks = []
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form.get('task')
    task_tag = request.form.get('tag')
    try:
        task_manager.add_task(task_description, task_tag)
        flash("Task added successfully.", "success")
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for('index'))

@app.route('/complete/<task>')
def complete_task(task):
    try:
        task_manager.complete_task(task)
        flash("Task completed successfully.", "success")
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for('index'))

@app.route('/delete/<task>')
def delete_task(task):
    try:
        task_manager.delete_task(task)
        flash("Task deleted successfully.", "success")
    except ValueError as e:
        flash(str(e), "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
