from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from api.config import Config

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)
jwt = JWTManager(app)
cors = CORS(app, support_credentials=True)


def create_app(config_class=Config):
    app.config.from_object(config_class)
    app.config['CORS_HEADERS'] = 'Content-Type'

    from api import views
    from api import models
    db.init_app(app)
    migrate.init_app(app, db)
    return app
