from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import math

app = Flask(__name__)
db_path = "todo.db"
tasks_per_page = 5

def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * tasks_per_page

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks LIMIT ? OFFSET ?', (tasks_per_page, offset))
    tasks = cursor.fetchall()
    
    cursor.execute('SELECT COUNT(*) FROM tasks')
    total_tasks = cursor.fetchone()[0]
    
    conn.close()

    total_pages = math.ceil(total_tasks / tasks_per_page)

    return render_template('index.html', tasks=tasks, current_page=page, total_pages=total_pages)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task'][:144]  # Limita o campo a 144 caracteres
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if request.method == 'POST':
        new_task = request.form['task'][:144]  # Limita o campo a 144 caracteres
        cursor.execute('UPDATE tasks SET task = ? WHERE id = ?', (new_task, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM tasks WHERE id = ?', (id,))
    task = cursor.fetchone()
    conn.close()
    return render_template('edit.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)