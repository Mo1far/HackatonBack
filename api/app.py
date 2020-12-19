from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)


def create_app(config_class=Config):
    app.config.from_object(config_class)

    from api import views

    db.init_app(app)
    migrate.init_app(app, db)
    return app
