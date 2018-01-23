from api.card_payment import CardPayment
from app import app, api, db
from db.models import *


def main():
    db.create_all()
    api.add_resource(CardPayment, '/card-payment', endpoint='card-payment')
    app.run(port=3416, debug=True)


if __name__ == '__main__':
    main()
