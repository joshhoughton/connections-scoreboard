from flask import Blueprint
from tabulate import tabulate

from connections_scoreboard.app.db import Message


bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def show_messages():
    messages = Message.query.all()
    table = []
    for message in messages:
        table.append([message.id, message.content])
    return tabulate(table, headers=["ID", "Content"], tablefmt="html")
