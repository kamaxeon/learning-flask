#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from app import app

DEFAULT_LOGIN = 'foo'
DEFAULT_PASSWD = 'bar'


class BaseTestClass(unittest.TestCase):
    'Base Test Class'

    def setUp(self):
        """
        Setup function
        """
        self.tester = app.test_client(self)

    def create_task(self, title=DEFAULT_LOGIN, description=DEFAULT_PASSWD):
        'Helper: Create a new task'
        return self.tester.post('/todo/api/tasks',
                                data=json.dumps(dict(
                                    title=title,
                                    description=description
                                )),
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
