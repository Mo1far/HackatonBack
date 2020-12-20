from api.app import db

event_interests = db.Table('event_interests',
                           db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
                           db.Column('interests_id', db.Integer, db.ForeignKey('interests.id'), primary_key=True)
                           )


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    creator_id = db.Column(db.ForeignKey('user.id'))
    interests = db.relationship('Interest', secondary=event_interests)

    def serialize_short(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'interests': [interest.serialize_short() for interest in self.interests]
        }
