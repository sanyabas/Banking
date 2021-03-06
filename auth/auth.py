import datetime
import jwt
from hashlib import sha256
from app import app
from db import db


def auth_is_valid(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return False
    token = auth_header.split()[1]
    if not token:
        return False
    resp = decode_auth_token(token)
    if isinstance(resp, str):
        return False
    return True


def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    except Exception as e:
        print(e)
        return e


def decode_auth_token(token):
    try:
        payload = jwt.decode(token, app.config['SECRET_KEY'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'


def hash_password(username, password):
    salt = db.get_user_salt(username)
    admin_hash = sha256()
    admin_hash.update(salt.encode())
    admin_hash.update(password.encode())
    return admin_hash.hexdigest()


def get_password(username):
    admin_hash = db.get_user_hash(username)
    return admin_hash
