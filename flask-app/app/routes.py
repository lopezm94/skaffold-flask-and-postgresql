from flask import request, jsonify
from app import app, db
from app.models import Todo

@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'POST':
        data = request.get_json()
        new_todo = Todo(task=data['task'])
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({'message': 'Todo created'}), 201
    else:
        todos = Todo.query.all()
        return jsonify([{'id': todo.id, 'task': todo.task} for todo in todos])
