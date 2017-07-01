#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json


from app import app


class BasicTestCase(unittest.TestCase):
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
        self.assertEqual(data['error'], 'Not found')

    def test_create_a_invalid_new_taks(self):
        """
        Create a taks without title
        """
        response = self.tester.post('/todo/api/tasks',
                                    data=json.dumps(dict(
                                        description='Description'
                                    )),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_create_a_valid_new_taks(self):
        """
        Create a valid task
        """

        response = self.tester.post('/todo/api/tasks',
                                    data=json.dumps(dict(
                                        title='Title',
                                        description='Description'
                                    )),
                                    content_type='application/json')
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
        self.tester.post('/todo/api/tasks',
                         data=json.dumps(dict(
                             title='foo',
                             description='bar'
                         )),
                         content_type='application/json')
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
        self.tester.post('/todo/api/tasks',
                         data=json.dumps(dict(
                             title='foo',
                             description='bar'
                         )),
                         content_type='application/json')

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
        self.tester.post('/todo/api/tasks',
                         data=json.dumps(dict(
                             title='foo',
                             description='bar'
                         )),
                         content_type='application/json')
        response = self.tester.delete('/todo/api/tasks/1',
                                      content_type='application/json')
        self.assertEqual(response.status_code, 204)
        # If it's deleted, we can't get it now :-)
        response = self.tester.get('/todo/api/tasks/1',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'Not found')


if __name__ == '__main__':
    unittest.main()
