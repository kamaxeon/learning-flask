#!/usr/bin/env python
# coding=utf-8
'Register API'


from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from app.users import users, is_user
from app.tokens import blacklisted_tokens

registerapi_bp = Blueprint('registerapi', __name__)
registerapi = Api(registerapi_bp)

class RegisterAPI(Resource):
    'Register Class'

    def __init__(self):
        'Init'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('login', type=str, required=True,
                                   help='No login provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        super(RegisterAPI, self).__init__()

    def post(self):
        'Create a user'
        args = self.reqparse.parse_args()
        if is_user(args['login']):
            return {'message': 'User {} exists'.format(args['login'])}, 422
        user = {
            'login': args['login'],
            'password':  args['password']
        }
        users.append(user)
        return {'message': 'Successfully registered'}, 201

    @staticmethod
    def delete():
        'Remote all the tasks and tokens'
        blacklisted_tokens.clear()
        del users[:]

registerapi.add_resource(RegisterAPI, '/register')
