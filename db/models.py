from app import db


class CardPaymentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardNumber = db.Column(db.String(16))
    expiration = db.Column(db.String(5))
    cvc = db.Column(db.Integer)
    sum = db.Column(db.Integer)
    comment = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f'<CardPayment {self.id} {self.cardNumber}>'
