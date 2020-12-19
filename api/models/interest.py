from api.app import db


class Interest(db.Model):
    __tablename__ = 'interests'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def serialize_short(self):
        return {
            'id': self.id,
            'title': self.title,
        }
