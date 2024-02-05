from flask import Blueprint, request
from tabulate import tabulate

from connections_scoreboard.app import db
from connections_scoreboard.app.models import Message


bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def show_messages():
    messages = Message.query.all()
    table = []
    for message in messages:
        table.append([message.id, message.content])
    return tabulate(table, headers=["ID", "Content"], tablefmt="ascii")


@bp.route("/submit_result", methods=["POST"])
def submit_result():
    if request.method == "POST":
        content = request.form.get("content")
        id = request.form.get("id")  # Add id parameter
        message = Message(content=content, id=id)  # Pass id to Message constructor
        db.session.add(message)
        db.session.commit()
        return "Message submitted!"
    else:
        return "Invalid request method!"
