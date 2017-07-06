#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from app import app

DEFAULT_TITLE = 'Title'
DEFAULT_DESCRIPTION = 'Description'
DEFAULT_LOGIN = 'foo'
DEFAULT_PASSWD = 'bar'


class BaseTestClass(unittest.TestCase):
    'Base Test Class'

    def setUp(self):
        """
        Setup function
        """
        self.tester = app.test_client(self)

    @staticmethod
    def _do_headers(token):
        'Create Auth headers'
        return {'Authorization': 'Bearer {}'.format(token)}

    def create_task(self, token, data=None):
        'Helper: Create a new task'
        if not data:
            data = {
                'title': DEFAULT_TITLE,
                'description': DEFAULT_DESCRIPTION
            }
        return self.tester.post('/todo/api/tasks',
                                data=json.dumps(data),
                                headers=self._do_headers(token),
                                content_type='application/json')

    def update_task(self, task_id, token, data):
        'Update a task'
        return self.tester.put('/todo/api/tasks/{}'.format(task_id),
                               data=json.dumps(data),
                               headers=self._do_headers(token),
                               content_type='application/json')

    def do_register(self, login=DEFAULT_LOGIN, password=DEFAULT_PASSWD):
        'Helper: Do a register'
        return self.tester.post('/todo/api/auth/register',
                                data=json.dumps(dict(
                                    login=login,
                                    password=password)),
                                content_type='application/json')

    def do_login(self, login=DEFAULT_LOGIN, password=DEFAULT_PASSWD):
        'Helper: Do login'
        return self.tester.post('/todo/api/auth/login',
                                data=json.dumps(dict(
                                    login=login,
                                    password=password)),
                                content_type='application/json')

    def get_status(self, token):
        'Get user status'
        return self.tester.get('/todo/api/auth/status',
                               headers=dict(Authorization='Bearer ' + token))

    def register_login_and_token(self):
        'Helper Register Login and Get Token'
        self.do_register()
        response = self.do_login()
        return json.loads(response.data.decode())['auth_token']
