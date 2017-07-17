#!/usr/bin/env python
# coding=utf-8
'Flask todo list api using flask-restful'
from datetime import timedelta
from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse, fields, marshal, abort
from flask_jwt_extended import JWTManager, jwt_required
from app.users import users, is_user, check_login
from app.tokens import blacklisted_tokens
from app.tasks import tasks, task_fields
from app.task_api import taskapi_bp
from app.task_list_api import tasklistapi_bp
from app.register_api import registerapi_bp
from app.logout_api import logoutapi_bp
from app.login_api import loginapi_bp
from app.status_api import statusapi_bp


app = Flask(__name__)  # pylint: disable=C0103

api = Api(app)  # pylint: disable=C0103
app.config['SECRET_KEY'] = "secret_key"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=3)
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
app.config['JWT_IDENTITY_CLAIM'] = 'sub'
jwt = JWTManager(app)  # pylint: disable=C0103


@jwt.expired_token_loader
def my_expired_token_callback():
    'Loader function used when an expired token accesses a protected endpoint'
    return make_response(
        jsonify(
            {'message': 'Signature expired. Please log in again.'}), 401)


@jwt.revoked_token_loader
def my_revoked_token_callback():
    'Loader function used when a revoked token accesses a protected endpoint'
    return make_response(jsonify({'message': 'Blacklisted tokens.'}), 401)


@jwt.invalid_token_loader
def my_invalid_token_callback(error):  # pylint: disable=W0613
    'Loader function used when an invalid token accesses a protected endpoint'
    return make_response(
        jsonify({'message': 'Invalid token. Please log in again.'}), 401)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    'Loader function to check when a token is blacklisted'
    jti = decrypted_token['jti']
    return jti in blacklisted_tokens


app.register_blueprint(tasklistapi_bp, url_prefix='/todo/api')
app.register_blueprint(taskapi_bp, url_prefix='/todo/api')
app.register_blueprint(loginapi_bp, url_prefix='/todo/api/auth')
app.register_blueprint(statusapi_bp, url_prefix='/todo/api/auth')
app.register_blueprint(logoutapi_bp, url_prefix='/todo/api/auth')
app.register_blueprint(registerapi_bp, url_prefix='/todo/api/auth')

if __name__ == '__main__':
    app.run(debug=True)
