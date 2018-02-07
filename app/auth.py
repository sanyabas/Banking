from app import auth
from db import db
from hashlib import sha256


@auth.get_password
def get_password(username):
    admin_hash = db.get_user_hash(username)
    return admin_hash


@auth.hash_password
def hash_password(username, password):
    salt = db.get_user_salt(username)
    admin_hash = sha256(salt.encode())
    admin_hash = admin_hash.update(password.encode())
    return admin_hash.hexdigest()
