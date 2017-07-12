#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from random import randint
from test.base import BaseTestClass, DEFAULT_TITLE, DEFAULT_DESCRIPTION


class TodoList(BaseTestClass):
    "Test Class"

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/tasks',
                           content_type='application/json')

    def test_empty_list_taks(self):
        """
        Test empty taks list
        """
        response = self.tester.get('/todo/api/tasks',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['tasks'], [])

    def test_get_a_non_existing_taks(self):
        """
        Get a non existing tasks
        """
        response = self.tester.get('/todo/api/tasks/99',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('Task 99 not found', data['message'])

    def test_create_a_invalid_new_task(self):
        """
        Create a taks without title
        """
        token = self.register_login_and_token()
        response = self.create_task(token=token,
                                    data={'description': 'Description'})
        self.assertEqual(response.status_code, 400)

    def test_create_a_valid_new_task(self):
        """
        Create a valid task
        """
        token = self.register_login_and_token()
        response = self.create_task(token=token)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], DEFAULT_TITLE)
        self.assertEqual(data['task']['description'], DEFAULT_DESCRIPTION)
        self.assertEqual(data['task']['done'], False)

    def test_get_a_valid_task(self):
        """
        Get an existing task
        """
        # We need create it before
        token = self.register_login_and_token()
        self.create_task(token=token)
        # Now we try get it
        response = self.tester.get('/todo/api/tasks/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], DEFAULT_TITLE)
        self.assertEqual(data['task']['description'], DEFAULT_DESCRIPTION)
        self.assertEqual(data['task']['done'], False)

    def test_update_an_existing_task(self):
        """
        Update a task
        """
        # We need create it before
        token = self.register_login_and_token()
        self.create_task(token=token)
        # Now we update it
        data = {
            'title': 'barñ',
            'description': 'foo',
            'done': True
        }
        response = self.update_task(task_id=1, token=token, data=data)

        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], 'barñ')
        self.assertEqual(data['task']['description'], 'foo')
        self.assertEqual(data['task']['done'], True)

    def test_delete_an_existing_task(self):
        """
        Delete a task
        """
        # We need create it before
        token = self.register_login_and_token()
        self.create_task(token=token)
        response = self.tester.delete('/todo/api/tasks/1',
                                      content_type='application/json')
        self.assertEqual(response.status_code, 204)
        # If it's deleted, we can't get it now :-)
        response = self.tester.get('/todo/api/tasks/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('Task 1 not found', data['message'])

    def test_get_all_tasks(self):
        """
        Get all tasks
        """
        # We are going to create some tasks
        token = self.register_login_and_token()
        number = len([self.create_task(token=token) in range(randint(2, 9))])
        response = self.tester.get('/todo/api/tasks',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['tasks']), number)

    def test_invalid_update(self):
        """
        Test all the invalid case for a invalid update
        """

        # Id not exists
        token = self.register_login_and_token()
        data = {
            'title': 'barñ',
            'description': 'foo',
            'done': True
        }
        response = self.update_task(task_id=99, token=token, data=data)
        self.assertEqual(response.status_code, 404)

        # Id exist but we don't send valid values
        self.create_task(token=token)
        data = {
            'foo': 'bar'
        }
        response = self.update_task(task_id=1, token=token, data=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], DEFAULT_TITLE)
        self.assertEqual(data['task']['description'], DEFAULT_DESCRIPTION)
        self.assertEqual(data['task']['uri'], '/todo/api/tasks/1')


if __name__ == '__main__':
    unittest.main()
