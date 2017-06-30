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

    def test_empty_list_taks(self):
        """
        Test empty taks list
        """
        response = self.tester.get('todo/api/v1.0/tasks',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['error'], 'Empty list')


if __name__ == '__main__':
    unittest.main()
