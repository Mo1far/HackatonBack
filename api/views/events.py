from flask import jsonify
from flask_jwt_extended import jwt_required

from api.models.event import Event
from api.views import events_bp as events_blueprint


@events_blueprint.route('/', methods=['GET'])
@jwt_required
def events_list():
    events = Event.query.all()
    return jsonify([event.serialize_short() for event in events])
