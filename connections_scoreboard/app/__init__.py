import logging

from flask import Flask
from flask_bootstrap import Bootstrap5

from connections_scoreboard.app.config import Config
from connections_scoreboard.app.db import db
from connections_scoreboard.app.middleware import RealIPMiddleware


# from connections_scoreboard.app.db.models import Result, User


def create_app():
    app = Flask(__name__)

    app.wsgi_app = RealIPMiddleware(app.wsgi_app)

    bootstrap = Bootstrap5(app)
    app.logger.setLevel(logging.DEBUG)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
