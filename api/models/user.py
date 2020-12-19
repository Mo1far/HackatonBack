from sqlalchemy.dialects.postgresql import BYTEA

from api.app import db

user_interests = db.Table('users_interests',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                          db.Column('interests_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
                          )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    password = db.Column(BYTEA)

    interests = db.relationship('Interest', secondary=user_interests)

    def serialize_short(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'interests': [interest.serialize_short() for interest in self.interests]
        }
