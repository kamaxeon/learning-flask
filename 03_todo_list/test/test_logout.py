#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest
import json

from test.base import BaseTestClass


class LogOut(BaseTestClass):
    'LogOut UnitTest'

    def tearDown(self):
        """
        TearDown
        """
        self.tester.delete('/todo/api/auth/register',
                           content_type='application/json')

    def test_logout(self):
        'Test Logout'

        # Register and login first
        auth_token = self.register_login_and_token()

        # LogOut
        response = self.tester.post('/todo/api/auth/logout',
                                    headers=dict(
                                        Authorization='Bearer ' + auth_token))
        data = json.loads(response.data.decode())
        self.assertIn('Successfully logged out.', data['message'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 200)
        # LogOut again
        response = self.tester.post('/todo/api/auth/logout',
                                    headers=dict(
                                        Authorization='Bearer ' + auth_token))
        data = json.loads(response.data.decode())
        self.assertIn('Blacklisted tokens.', data['message'])
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
