from flask_restful import Resource
from flask import request
from auth import auth

from db.models import Admin


class LoginApi(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = Admin.query.filter_by(username=data['login']).first()
            if user and auth.get_password(data['login']) == auth.hash_password(data['login'], data['password']):
                token = auth.encode_auth_token(user.id)
                if token:
                    resp_obj = {
                        'ok': 'true',
                        'message': 'Logged in',
                        'auth_token': token.decode()
                    }
                    return resp_obj
            else:
                return {
                           'ok': 'false',
                           'message': 'Invalid credentials'
                       }, 403
        except Exception as e:
            print(e)
            return {
                       'ok': 'false',
                       'message': 'Internal error, try again later'
                   }, 500

    def get(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split()[1]
        else:
            token = ''
        if token:
            resp = auth.decode_auth_token(token)
            if not isinstance(resp, str):
                user = Admin.query.filter_by(id=resp).first()
                response_obj = {
                    'ok': 'true',
                    'data': {
                        'user_id': user.id,
                        'username': user.username
                    }
                }
                return response_obj
            return {
                       'ok': 'false',
                       'message': resp
                   }, 403
        else:
            return {
                       'ok': 'false',
                       'message': 'Invalid token.'
                   }, 403
