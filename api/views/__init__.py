from flask import Blueprint

from api.app import app

events_bp = Blueprint('events', __name__)

from . import events

app.register_blueprint(events_bp, url_prefix='/events')
