from api.app import db


class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def serialize_short(self):
        return {
            'id': self.id,
            'name': self.name
        }
