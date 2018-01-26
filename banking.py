from api.card_payment import CardPayment
from api.payment_request import PaymentRequest
from api.login_api import LoginApi
from app import app, api, db
from db.models import *


def main():
    db.create_all()
    api.add_resource(CardPayment, '/card-payment', endpoint='card-payment')
    api.add_resource(CardPayment, '/card-payment<int:id>', endpoint='card-payment-id')
    api.add_resource(PaymentRequest, '/payment-request', endpoint='payment-request')
    api.add_resource(LoginApi, '/login', endpoint='login')
    app.run(port=3416, debug=True)


if __name__ == '__main__':
    main()

# фиксация сессии
