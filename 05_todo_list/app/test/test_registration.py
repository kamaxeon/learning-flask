#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from app.test.base import BaseTestClass


class Registration(BaseTestClass):
    'Test Class for Registration Process'

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/auth/register',
                           content_type='application/json')

    def test_valid_registration(self):
        'Test valid user registration'
        # Valid user
        response = self.do_register()
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Successfully registered')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_invalid_registration(self):
        'Test invalid user registration'
        # Exist user
        self.do_register()
        response = self.do_register()
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'User foo exists')
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
