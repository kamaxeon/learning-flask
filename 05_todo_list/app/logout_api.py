#!/usr/bin/env python
# coding=utf-8
'Logout API'


from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_raw_jwt
from app.tokens import blacklisted_tokens


logoutapi_bp = Blueprint('logoutapi', __name__)
logoutapi = Api(logoutapi_bp)


class LogOutAPI(Resource):
    'LogOut Class'
    method_decorators = [jwt_required]

    @staticmethod
    def post():
        'Post function'
        jti = get_raw_jwt()['jti']
        blacklisted_tokens.add(jti)
        return {'message': 'Successfully logged out.'}


logoutapi.add_resource(LogOutAPI, '/logout')
