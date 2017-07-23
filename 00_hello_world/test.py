#!/usr/bin/env python
# coding=utf-8

"""Clase de Test."""

import json
import unittest

from app import app


class BasicTestCase(unittest.TestCase):
    """Clase básica de Test."""

    def setUp(self):
        """Test setup function."""
        self.tester = app.test_client(self)

    def test_hello_world_html(self):
        """Comprobando hello world html."""
        response = self.tester.get('/hello_world', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

    def test_hello_world_json(self):
        """Comprobando index json."""
        response = self.tester.get('/api/hello_world',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], "Hello World!")


if __name__ == '__main__':
    unittest.main()
