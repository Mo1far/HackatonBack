from sqlalchemy.dialects.postgresql import BYTEA

from api.app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    password = db.Column(BYTEA)

    def serialize_short(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
