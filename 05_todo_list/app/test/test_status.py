#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json
import time

from app.test.base import BaseTestClass


class Status(BaseTestClass):
    'Test user status'

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/auth/register',
                           content_type='application/json')

    def test_valid_status(self):
        'Valid login'
        self.do_register()
        response_login = self.do_login()
        response = self.tester.get('/todo/api/auth/status',
                                   headers=dict(
                                       Authorization='Bearer ' +
                                       json.loads(
                                           response_login.data.decode())
                                       ['auth_token']))

        data = json.loads(response.data.decode())
        self.assertEqual('Successfully logged in', data['message'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        'Invalid user'

        # Invalid token
        response = self.get_status(token='ffsf')

        data = json.loads(response.data.decode())
        self.assertIn('Invalid token', data['message'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 401)

        # Expired token
        self.do_register()
        response_login = self.do_login()
        time.sleep(4)
        response = self.get_status(token=json.loads(
            response_login.data.decode())['auth_token'])
        data = json.loads(response.data.decode())
        self.assertIn('Signature expired', data['message'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
