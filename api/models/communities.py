from api.app import db


class Communities(db.Model):
    __tablename__ = 'communities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    userscount = db.Column(db.Integer)

    # Union between this table & interests name

    def serialize_short(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'userscount': self.userscount
        }
