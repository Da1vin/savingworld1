from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    todos = []

    if request.method == 'POST':
        name = request.form['name']
        task = request.form['task']
        action = request.form['action']
        
        if action == 'add':
            due_date_str = request.form['due_date']
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date()
            with open('data.txt', 'a') as file:
                file.write(f'{name} {task} {due_date}\n')
        elif action == 'finish':
            with open('data.txt', 'r') as file:
                lines = file.readlines()
            with open('data.txt', 'w') as file:
                for line in lines:
                    if task not in line:
                        file.write(line)

    with open('data.txt', 'r') as file:
        for line in file:
          fields = line.strip().split(' ')
          task = fields[1] if len(fields) > 1 else None
          due_date_str = fields[2] if len(fields) > 2 else None
          due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
          todos.append({'task': task, 'due_date': due_date})

    return render_template('index.html', todos=todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
