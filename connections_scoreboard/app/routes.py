from flask import Blueprint, render_template

from connections_scoreboard.app.db.models import Result


bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
def show_results():
    """Produce a table that shows a row for each day's puzzle (starting with most recent)
    and each column is an individual user. The cell contains the number of attempts for that user.
    """
    results = Result.query.all()

    # Create a list of dicts to store the puzzle results
    puzzle_numbers = sorted(
        set(result.puzzle_number for result in results), reverse=True
    )
    usernames = set(result.user.name for result in results)

    data = []

    for puzzle_number in puzzle_numbers:
        puzzle_results = dict(
            puzzle_number=puzzle_number, **{username: "" for username in usernames}
        )
        for result in results:
            if result.puzzle_number == puzzle_number:
                puzzle_results[result.user.name] = result.incorrect_count

        data.append(puzzle_results)

    return render_template("index.html", data=data)
