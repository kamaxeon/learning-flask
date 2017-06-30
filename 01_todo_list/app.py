#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify, abort, make_response

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
