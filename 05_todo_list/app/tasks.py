#!/usr/bin/env python
# coding=utf-8
'Tasks model'

from flask_restful import fields


tasks = []  # pylint: disable=C0103
task_fields = {  # pylint: disable=C0103
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('tasks')
}
