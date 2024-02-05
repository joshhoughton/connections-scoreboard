from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

from connections_scoreboard.app.models import db


class Message(db.Model):
    __tablename__ = "messages"

    id = Column(String, primary_key=True)
    content = Column(String)
