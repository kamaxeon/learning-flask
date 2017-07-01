#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

tasks = []

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [ task for task in tasks if task['id'] ]
    if not task:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/todo/api/tasks', methods=['POST'])
def create_task():
    if not request.get_json() or not 'title' in request.get_json():
        abort(400)

    if not tasks:
        id = 1
    else:
        id = tasks[-1]['id'] + 1
    task = {
        'id': id,
        'title': request.get_json()['title'],
        'description': request.get_json().get('description', ''),
        'done': False
    }

    tasks.append(task)
    return make_response(jsonify({'task': task}), 201)


@app.route('/todo/api/tasks', methods=['DELETE'])
def delete_tasks():
    [ tasks.remove(t) for t in tasks ]
    return jsonify({'tasks': tasks})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
