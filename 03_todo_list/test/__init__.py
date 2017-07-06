#!/usr/bin/env python
# coding=utf-8
'Init'
import unittest
from . import test_login, test_todolist, test_registration  # NOQA
from . import test_logout, test_status  # NOQA

if __name__ == '__main__':
    unittest.main()
