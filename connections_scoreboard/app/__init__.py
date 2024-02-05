from flask import Flask

from connections_scoreboard.app.config import Config
from connections_scoreboard.app.models import db


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

from .routes import bp as main_bp


app.register_blueprint(main_bp)
