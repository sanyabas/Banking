from flask_restful import Api, Resource, reqparse
from db import db
from auth.auth import auth_is_valid
from app import app
from db.models import CardPaymentModel
from app import auth
from flask import redirect, url_for, send_file, request


class CardPayment(Resource):
    # decorators = {'get': [auth.login_required]}

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
        # print(request.data)
        args = self.reqparse.parse_args()
        payment = {
            'cardNumber': args['cardNumber'],
            'expiration': args['expiration'],
            'cvc': args['cvc'],
            'sum': args['sum'],
            'comment': args['comment'],
            'email': args['email']
        }
        # with open('doc.json', 'w',encoding='utf-8') as file:
        #     file.write(str(payment))
        # return send_file('../db/app.db')
        # return redirect(url_for('static', 'doc.json'))
        # print(payment)
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
