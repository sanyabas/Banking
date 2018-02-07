import flask
from flask_restful import Resource, reqparse
from auth.auth import auth_is_valid
from db import db


class PaymentRequest(Resource):
    def __init__(self):
        self.error = {
            'ok': 'false',
            'message': 'Bad credentials'
        }
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('to', required=True, type=str, location='json')
        self.reqparser.add_argument('bik', type=str, required=True, location='json')
        self.reqparser.add_argument('account', type=str, required=True, location='json')
        self.reqparser.add_argument('purpose', type=str, required=True, location='json')
        self.reqparser.add_argument('sum', type=str, required=True, location='json')
        self.reqparser.add_argument('phone', type=str, required=True, location='json')
        self.reqparser.add_argument('email', type=str, required=True, location='json')
        super(PaymentRequest, self).__init__()

    def post(self):
        args = self.reqparser.parse_args()
        db.add_payment_request(args)
        return {'ok': 'true'}

    def get(self):
        if not auth_is_valid(flask.request):
            return self.error, 403
        fields=['id','to','bik','account','goal','sum','phone','email']
        requests = db.get_requests()
        result = []
        for request in requests:
            res_dict=dict()
            for field in fields:
                print(request.__dict__)
                res_dict[field]=request.__dict__[field]
            # request.__dict__.pop('_sa_instance_state')
            result.append(res_dict)
        print(result)
        return {'ok': 'true', 'values': result}
