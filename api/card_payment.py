from flask_restful import Api, Resource, reqparse
from db import db
from db.models import CardPaymentModel


class CardPayment(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('cardNumber', type=str, required=True, location='json')
        self.reqparse.add_argument('expiration', type=str, required=True, location='json')
        self.reqparse.add_argument('cvc', type=int, required=True, location='json')
        self.reqparse.add_argument('sum', type=int, required=True, location='json')
        self.reqparse.add_argument('comment', type=str, required=False, location='json')
        self.reqparse.add_argument('email', type=str, required=True, location='json')
        super(CardPayment, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        payment = {
            'cardNumber': args['cardNumber'],
            'expiration': args['expiration'],
            'cvc': args['cvc'],
            'sum': args['sum'],
            'comment': args['comment'],
            'email': args['email']
        }
        print(payment)
        db.add_card_payment(args)
        return {'ok': 'true'}, 200

    def get(self):
        return {'ok': 'true', 'values': 'values will be here'}
