from flask import Flask

from connections_scoreboard.app.config import Config
from connections_scoreboard.app.db import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # db.drop_all()
        db.create_all()

    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
