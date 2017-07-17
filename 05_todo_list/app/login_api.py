#!/usr/bin/env python
# coding=utf-8
'Login API'


from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import create_access_token
from app.users import check_login


loginapi_bp = Blueprint('loginapi', __name__)  # pylint: disable=C0103
loginapi = Api(loginapi_bp)  # pylint: disable=C0103


class LoginAPI(Resource):
    'Login Class'

    def __init__(self):
        'Init'
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('login', type=str, required=True,
                                   help='No login provided', location='json')
        self.reqparse.add_argument('password', type=str, required=True,
                                   help='No password provided',
                                   location='json')
        super(LoginAPI, self).__init__()

    def post(self):
        'Post function'
        args = self.reqparse.parse_args()
        if check_login(args['login'], args['password']):
            auth_token = create_access_token(identity=args['login'])
            return {'message': 'Successfully logged',
                    'auth_token': auth_token}, 201
        return {'message': 'Login failed'}, 401


loginapi.add_resource(LoginAPI, '/login')
