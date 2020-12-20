from flask import Blueprint

from api.app import app

events_bp = Blueprint('events', __name__)
interests_bp = Blueprint('interests', __name__)
auth_bp = Blueprint('auth', __name__)


from . import events, auth, interests

app.register_blueprint(events_bp, url_prefix='/events')
app.register_blueprint(interests_bp, url_prefix='/interests')
app.register_blueprint(auth_bp, url_prefix='/auth')
