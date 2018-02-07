from flask import request
from flask_restful import Resource, reqparse

from auth.auth import auth_is_valid
from db import db


class CardPayment(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('cardNumber', type=str, required=True, location='json')
        self.reqparse.add_argument('expiration', type=str, required=True, location='json')
        self.reqparse.add_argument('cvc', type=int, required=True, location='json')
        self.reqparse.add_argument('sum', type=int, required=True, location='json')
        self.reqparse.add_argument('comment', type=str, required=False, location='json')
        self.reqparse.add_argument('email', type=str, required=True, location='json')
        self.error = {
            'ok': 'false',
            'message': 'Bad credentials'
        }
        super(CardPayment, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        db.add_card_payment(args)
        return {'ok': 'true'}, 200

    def get(self):
        if not auth_is_valid(request):
            return self.error, 403
        payments = db.get_payments()
        result = []
        for payment in payments:
            payment.__dict__.pop('_sa_instance_state')
            result.append(payment.__dict__)
        return {'ok': 'true', 'values': result}

    def put(self, id):
        if not auth_is_valid(request):
            return self.error, 403
        try:
            db.toggle_safety(id)
        except Exception:
            return {'ok': 'false'}, 404
        else:
            return {'ok': 'true'}
