#!/usr/bin/env python
# coding=utf-8
'User model'


users = []  # pylint: disable=C0103


def is_user(login):
    'Return if a user exists'
    for user in users:
        if user['login'] == login:
            return True
    return False


def check_login(login, password):
    'Check user and passowrd'
    for user in users:
        if user['login'] == login and user['password'] == password:
            return True
    return False
