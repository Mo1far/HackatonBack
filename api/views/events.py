from flask_jwt_extended import jwt_required

from api.models.event import Event
from api.views import events_bp as events_blueprint
from api.views.utils import success_response


@events_blueprint.route('/', methods=['GET'])
@jwt_required
def events_list():
    events = Event.query.all()
    return success_response({'events': [event.serialize_short() for event in events]})
