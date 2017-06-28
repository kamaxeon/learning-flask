#!/usr/bin/env python
# coding=utf-8
""" Aplicación inicial que sólo devuelve un hola mundo
"""

from flask import Flask

app = Flask(__name__)  # pylint: disable=C0103


@app.route('/')
def index():
    "Index"
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
