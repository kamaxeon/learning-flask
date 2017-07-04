#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json


from random import randint
from app import app


class TodoList(unittest.TestCase):
    "Test Class"

    def setUp(self):
        """
        Setup function
        """
        self.tester = app.test_client(self)

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/tasks',
                           content_type='application/json')

    def create_task(self, title='foo', description='bar'):
        'Helper: Create a new task'
        return self.tester.post('/todo/api/tasks',
                                data=json.dumps(dict(
                                    title=title,
                                    description=description
                                )),
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
        response = self.tester.post('/todo/api/tasks',
                                    data=json.dumps(dict(
                                        description='Description'
                                    )),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_a_valid_new_task(self):
        """
        Create a valid task
        """
        response = self.create_task(title='Title', description='Description')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], 'Title')
        self.assertEqual(data['task']['description'], 'Description')
        self.assertEqual(data['task']['done'], False)

    def test_get_a_valid_task(self):
        """
        Get an existing task
        """
        # We need create it before
        self.create_task()
        # Now we try get it
        response = self.tester.get('/todo/api/tasks/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], 'foo')
        self.assertEqual(data['task']['description'], 'bar')
        self.assertEqual(data['task']['done'], False)

    def test_update_an_existing_task(self):
        """
        Update a task
        """
        # We need create it before
        self.create_task()
        # Now we update it
        response = self.tester.put('/todo/api/tasks/1',
                                   data=json.dumps(dict(
                                       title='barñ',
                                       description='foo',
                                       done=True
                                   )),
                                   content_type='application/json')

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
        self.create_task()
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
        number = len([self.create_task() in range(randint(2, 9))])
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
        response = self.tester.put('/todo/api/tasks/99',
                                   data=json.dumps(dict(
                                       title='barñ',
                                       description='foo',
                                       done=True
                                   )),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

        # Id exist but we don't send valid values
        self.create_task()
        response = self.tester.put('/todo/api/tasks/1',
                                   data=json.dumps(dict(foo='bar')),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['task']['title'], 'foo')
        self.assertEqual(data['task']['description'], 'bar')
        self.assertEqual(data['task']['uri'], '/todo/api/tasks/1')

    def test_registration(self):
        'Test user registration'
        # Valid user
        response = self.tester.post('/todo/api/auth/register',
                                    data=json.dumps(dict(
                                        login='foo',
                                        password='bar')),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Successfully registered')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 201)

        # Exist user
        response = self.tester.post('/todo/api/auth/register',
                                    data=json.dumps(dict(
                                        login='foo',
                                        password='bar')),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertTrue(data['message'] == 'User foo exists')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 422)

        # Without password
        response = self.tester.post('/todo/api/auth/register',
                                    data=json.dumps(dict(login='foo')),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message']['password'], 'No password provided')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 400)

        # Without login
        response = self.tester.post('/todo/api/auth/register',
                                    data=json.dumps(dict(password='bar')),
                                    content_type='application/json')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message']['login'], 'No login provided')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
