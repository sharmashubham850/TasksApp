from flask import Flask, request, render_template, url_for, redirect
import database
from helpers import date_to_str
app = Flask(__name__)


# Custom filter
app.jinja_env.filters["date_to_str"] = date_to_str

database.create_table()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form.get('content')
        if not task:
            return render_template('apology.html', msg='No task provided!'), 404

        database.add_task(task=task)
        return redirect('/')

    else:
        tasks = database.get_all_tasks()
        return render_template('index.html', tasks=tasks)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        new_task = request.form.get('content')

        if not new_task:
            return render_template('apology.html', msg='No task provided!'), 404

        database.update_task(id, new_task)
        return redirect('/')

    else:
        task = database.get_task(task_id=id)
        return render_template('update.html', task=task)


@app.route('/delete/<int:id>')
def delete(id):
    database.delete_task(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
