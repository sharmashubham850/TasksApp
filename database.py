import sqlite3
from datetime import datetime


def create_table():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = '''CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                date TIMESTAMP NOT NULL
        )'''

        cursor.execute(command)
        conn.commit()


def add_task(task: str):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = "INSERT INTO tasks(task, date) VALUES(?, ?)"
        cursor.execute(command, (task, datetime.now()))
        conn.commit()


def update_task(task_id: int, task: str):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = "UPDATE tasks SET task= ?, date= ? WHERE id= ?"

        cursor.execute(command, (task, datetime.now(), task_id))

        conn.commit()


def delete_task(task_id: int):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = "DELETE from tasks WHERE id= ?"

        cursor.execute(command, (task_id,))

        conn.commit()


def get_all_tasks():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = "SELECT * FROM tasks"

        tasks = cursor.execute(command)

        return cursor.fetchall()
