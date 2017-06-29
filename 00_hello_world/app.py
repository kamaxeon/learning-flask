#!/usr/bin/env python
# coding=utf-8
""" Aplicación inicial que sólo devuelve un hola mundo
"""

from flask import Flask, jsonify

app = Flask(__name__)  # pylint: disable=C0103


@app.route('/hello_world')
def hello_world():
    "Index"
    return 'Hello World!'


@app.route('/api/hello_world')
def hello_world_api():
    "Index json"
    return jsonify({'message': 'Hello World!'})


if __name__ == '__main__':
    app.run()
