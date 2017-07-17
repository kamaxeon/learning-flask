#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from app.test.base import BaseTestClass


class Login(BaseTestClass):
    'Test user login'

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/auth/register',
                           content_type='application/json')

    def test_valid_login(self):
        'Valid login'
        self.do_register()
        response = self.do_login()
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Successfully logged')
        self.assertTrue(data['auth_token'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_invalid_login(self):
        'Invalid user'

        # Unregister user
        response = self.do_login()
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Login failed')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 401)

        # Invalid password
        self.do_register()
        response = self.do_register()
        response = self.do_login(password='ard')
        data = json.loads(response.data.decode())
        self.assertEqual(data['message'], 'Login failed')
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
