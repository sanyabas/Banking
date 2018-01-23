from app import db
from .models import CardPaymentModel


def add_card_payment(args):
    payment = CardPaymentModel(id=None,
                               cardNumber=args['cardNumber'],
                               expiration=args['expiration'],
                               cvc=args['cvc'],
                               sum=args['sum'],
                               comment=args['comment'],
                               email=args['email'])
    db.session.add(payment)
    db.session.commit()
    print(f'{payment} added')
