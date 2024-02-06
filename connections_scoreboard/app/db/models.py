from sqlalchemy import Column, DateTime, ForeignKey, String

from connections_scoreboard.app.db import db


class Message(db.Model):
    __tablename__ = "messages"

    id = Column(String, primary_key=True)
    content = Column(String)
    created = Column(DateTime)
    user_id = Column(String, ForeignKey("users.id"))
    user = db.relationship("User", backref="messages")


class User(db.Model):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    nick = Column(String)
    global_name = Column(String)
    avatar_url = Column(String)


class Result(db.Model):
    __tablename__ = "results"

    id = Column(String, primary_key=True)
    content = Column(String)
    date = Column(DateTime)
    user_id = Column(String, db.ForeignKey("users.id"))
    user = db.relationship("User", backref="results")
