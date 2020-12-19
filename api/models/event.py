from api.app import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    def serialize_short(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
