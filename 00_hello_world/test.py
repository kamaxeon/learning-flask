#!/usr/bin/env python
# coding=utf-8
"Clase de Test"
import unittest

from app import app


class BasicTestCase(unittest.TestCase):
    "Clase básica de Test"

    def test_index(self):
        "Comprobando index"
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')


if __name__ == '__main__':
    unittest.main()
