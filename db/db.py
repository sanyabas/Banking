from app import db
from .models import *


def add_card_payment(args):
    payment = CardPaymentModel(id=None,
                               cardNumber=args['cardNumber'],
                               expiration=args['expiration'],
                               cvc=args['cvc'],
                               sum=args['sum'],
                               comment=args['comment'],
                               email=args['email'],
                               notSafe=False)
    db.session.add(payment)
    db.session.commit()
    print(f'{payment} added')


def get_payments():
    return CardPaymentModel.query.all()


def toggle_safety(id):
    item = CardPaymentModel.query.filter_by(id=id).first()
    item.notSafe = not item.notSafe
    db.session.commit()


def add_payment_request(args):
    request=PaymentRequestModel(id=None,
                                to=args['to'],
                                bik=args['bik'],
                                account=args['account'],
                                goal=args['purpose'],
                                sum=args['sum'],
                                phone=args['phone'],
                                email=args['email'])
    db.session.add(request)
    db.session.commit()
    print(request)


def get_requests():
    return PaymentRequestModel.query.all()


def get_user_hash(username):
    admin = Admin.query.filter_by(username=username).first()
    return admin.password_hash


def get_user_salt(username):
    admin = Admin.query.filter_by(username=username).first()
    return admin.salt
