#!/usr/bin/env python
# coding=utf-8
'Flask todo list api'
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)  # pylint: disable=C0103

tasks = []  # pylint: disable=C0103


@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    'Return the list of tasks'
    return jsonify({'tasks': tasks})


@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    'Return the task by id'
    task = [task for task in tasks if task['id'] == task_id]
    if not task:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/tasks', methods=['POST'])
def create_task():
    'Create a new task'
    if not request.get_json() or 'title' not in request.get_json():
        abort(400)

    if not tasks:
        new_id = 1
    else:
        new_id = tasks[-1]['id'] + 1
    task = {
        'id': new_id,
        'title': request.get_json()['title'],
        'description': request.get_json().get('description', ''),
        'done': False
    }

    tasks.append(task)
    return make_response(jsonify({'task': task}), 201)


@app.route('/todo/api/tasks', methods=['DELETE'])
def delete_tasks():
    'Remote all the tasks'
    del tasks[:]
    return jsonify({'tasks': tasks})


@app.route('/todo/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    'Update a task'
    task = [task for task in tasks if task['id'] == task_id]
    if not task:
        abort(404)
    request_update = request.get_json()
    if request_update is None:
        abort(404)

    if 'done' in request_update and \
            not isinstance(request_update['done'], bool):
        abort(404)

    task[0]['title'] = request_update.get('title', task[0]['title'])
    task[0]['description'] = request_update.get('description',
                                                task[0]['description'])
    task[0]['done'] = request_update.get('done', task[0]['done'])

    return jsonify({'task': task[0]})


@app.route('/todo/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    'Delete a task'
    task = [task for task in tasks if task['id'] == task_id]
    if not task:
        abort(404)
    tasks.remove(tasks[0])
    return ('', 204)


@app.errorhandler(404)
def not_found(error):  # pylint: disable=W0613
    'Handler for 404'
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
