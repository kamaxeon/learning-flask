#!/usr/bin/env python
# coding=utf-8
'Flask todo list api using flask-restful'
from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal, abort


app = Flask(__name__)  # pylint: disable=C0103

api = Api(app)  # pylint: disable=C0103
tasks = []  # pylint: disable=C0103
task_fields = {  # pylint: disable=C0103
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

users = []  # pylint: disable=C0103


def is_user(login):
    'Return if a user exists'
    for user in users:
        if user['login'] == login:
            return True
    return False


class RegisterAPI(Resource):
    'Register Class'

    def __init__(self):
        'Init'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('login', type=str, required=True,
                                   help='No login provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        super(RegisterAPI, self).__init__()

    def post(self):
        'Create a user'
        args = self.reqparse.parse_args()
        if is_user(args['login']):
            return {'message': 'User {} exists'.format(args['login'])}, 422
        user = {
            'login': args['login'],
            'password':  args['password']
        }
        users.append(user)
        return {'message': 'Successfully registered'}, 201


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


api.add_resource(TaskListAPI, '/todo/api/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/tasks/<int:id>', endpoint='task')
api.add_resource(RegisterAPI, '/todo/api/auth/register', endpoint='register')

if __name__ == '__main__':
    app.run(debug=True)