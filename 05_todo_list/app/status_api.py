#!/usr/bin/env python
# coding=utf-8
'Login API'


from flask import Blueprint
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required


statusapi_bp = Blueprint('statusapi', __name__)
statusapi = Api(statusapi_bp)


class StatusAPI(Resource):
    'Status Class'
    method_decorators = [jwt_required]

    @staticmethod
    def get():
        'Get function'
        return {'message': 'Successfully logged in'}

statusapi.add_resource(StatusAPI, '/status')