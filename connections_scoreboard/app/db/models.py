from sqlalchemy import Column, DateTime, Integer, String

from connections_scoreboard.app.db import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    nick = Column(String)
    global_name = Column(String)
    avatar_url = Column(String)

    @property
    def name(self):
        return self.nick or self.global_name


class Result(db.Model):
    __tablename__ = "results"

    message_id = Column(String, primary_key=True)
    raw_content = Column(String)
    created = Column(DateTime)
    puzzle_number = Column(Integer)
    attempt_count = Column(Integer)
    user_id = Column(String, db.ForeignKey("users.id"))
    user = db.relationship("User", backref="results")

    @property
    def incorrect_count(self):
        return self.attempt_count - 4
