from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.card_payment import CardPayment


def main():
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    api.add_resource(CardPayment, '/card-payment', endpoint='card-payment')
    app.run(port=3416, debug=True)


if __name__ == '__main__':
    main()
