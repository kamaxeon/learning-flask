#!/usr/bin/env python
# coding=utf-8
'Task API'

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, marshal, abort
from flask_jwt_extended import jwt_required
from app.tokens import blacklisted_tokens
from app.tasks import tasks, task_fields


taskapi_bp = Blueprint('tasks', __name__)
taskapi = Api(taskapi_bp)

class TaskAPI(Resource):
    'Task Api'

    def __init__(self):
        'Init'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    @staticmethod
    def get(id):  # pylint: disable=C0103,W0622
        'Return the task by id'
        return {'task': marshal(TaskAPI.find_task(id), task_fields)}

    @jwt_required
    def put(self, id):  # pylint: disable=C0103,W0622
        'Update a task'
        task = TaskAPI.find_task(id)
        args = self.reqparse.parse_args()
        for key, value in args.items():
            if value is not None:
                task[key] = value
        return {'task': marshal(task, task_fields)}

    @staticmethod
    def delete(id):  # pylint: disable=C0103,W0622
        'Delete a task'
        tasks.remove(TaskAPI.find_task(id))
        return ('', 204)

    @staticmethod
    def find_task(id):  # pylint: disable=C0103,W0622
        'Return the task by id, if not exist, return 404 code'
        try:
            return [task for task in tasks if task['id'] == id][0]
        except IndexError:
            abort(404, message='Task {} not found'.format(id))

taskapi.add_resource(TaskAPI, '/tasks/<int:id>')
