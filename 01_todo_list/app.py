#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify

app = Flask(__name__)

tasks = []

@app.route('/todo/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
