#!/usr/bin/env python
# coding=utf-8
'Task List API'

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal, abort
from flask_jwt_extended import jwt_required
from app.tokens import blacklisted_tokens
from app.tasks import tasks, task_fields


tasklistapi_bp = Blueprint('taskslistapi', __name__)
tasklistapi = Api(tasklistapi_bp)

class TaskListAPI(Resource):
    'Task List Api'

    def __init__(self):
        'Init'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', type=str, default="",
                                   location='json')
        super(TaskListAPI, self).__init__()

    @staticmethod
    def get():
        'Return the list of tasks'
        return {'tasks': [marshal(task, task_fields) for task in tasks]}

    @jwt_required
    def post(self):
        'Create a new task'
        args = self.reqparse.parse_args()
        if not tasks:
            new_id = 1
        else:
            new_id = tasks[-1]['id'] + 1
        task = {
            'id': new_id,
            'title': args['title'],
            'description': args['description'],
            'done': False
        }
        tasks.append(task)
        return {'task': marshal(task, task_fields)}, 201

    @staticmethod
    def delete():
        'Remote all the tasks'
        del tasks[:]
        return {'tasks': marshal(tasks, task_fields)}

tasklistapi.add_resource(TaskListAPI, '/tasks')
