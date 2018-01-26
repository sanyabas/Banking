from app import db


class CardPaymentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardNumber = db.Column(db.String(16))
    expiration = db.Column(db.String(5))
    cvc = db.Column(db.Integer)
    sum = db.Column(db.Integer)
    comment = db.Column(db.String(100))
    email = db.Column(db.String(100))
    notSafe = db.Column(db.Boolean)

    def __repr__(self):
        return f'<CardPayment {self.id} {self.cardNumber}>'


class PaymentRequestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String(20))
    bik = db.Column(db.String(20))
    account = db.Column(db.String(20))
    goal = db.Column(db.String(100))
    sum = db.Column(db.Integer)
    phone = db.Column(db.String(15))
    email = db.Column(db.String(30))

    def __repr__(self):
        return f'<Payment request {self.id} {self.to}'


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))

    salt = db.Column(db.String(20))
