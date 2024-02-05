from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_world():
    with open("scores.txt", "r") as f:
        return f"<p>{f.read()}</p>"
