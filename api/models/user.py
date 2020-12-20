from enum import Enum

from sqlalchemy import or_
from sqlalchemy.dialects.postgresql import BYTEA

from api.app import db


class FriendshipStatus(Enum):
    requested = 'requested'
    accepted = 'accepted'
    accepted_second_level = 'accepted_second_level'
    second_level = 'second_level'


user_interests = db.Table('users_interests',
                          db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                          db.Column('interests_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
                          )

user_friendship = db.Table('user_friendship',
                           db.Column('requester_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                           db.Column('target_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
                           db.Column('status', db.Enum(FriendshipStatus), default=FriendshipStatus.requested)
                           )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    password = db.Column(BYTEA)

    interests = db.relationship('Interest', secondary=user_interests)
    friends = db.relationship('User', secondary=user_friendship, primaryjoin=(
        or_(user_friendship.c.requester_id == id, user_friendship.c.target_id == id)),
                              secondaryjoin=(user_friendship.c.target_id == id))

    def serialize_short(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'interests': [interest.serialize_short() for interest in self.interests]
        }
