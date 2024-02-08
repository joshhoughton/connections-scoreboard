import discord

from connections_scoreboard.app import create_app, db
from connections_scoreboard.app.db.models import Result, User
from connections_scoreboard.bot._parsing import parse_result


app = create_app()


def handle_message(message: discord.Message):
    app.logger.info(f"Handling message {message.id}")

    message_id = str(message.id)
    puzzle_number, attempt_count = parse_result(message.content)

    if puzzle_number is None:
        app.logger.debug(f"{message_id}: unable to parse puzzle number")
        return

    if attempt_count < 4:
        app.logger.debug(f"{message_id}: less than 4 attempts")
        return

    user_id = str(message.author.id)
    nick = message.author.nick if isinstance(message.author, discord.Member) else None
    global_name = message.author.name
    avatar_url = str(message.id)
    message_timestamp = str(message.created_at)

    with app.app_context():
        # Check if id already exists
        if Result.query.filter_by(message_id=message_id).first():
            app.logger.debug(f"{message_id}: message already processed")
            return

        user = User.query.filter_by(id=user_id).first()

        if user:
            # Update user details
            user.global_name = global_name
            user.avatar_url = avatar_url
            if nick:
                user.nick = nick
        else:
            # Create new user
            user = User(
                id=user_id, nick=nick, global_name=global_name, avatar_url=avatar_url
            )

        result = Result(
            message_id=message_id,
            raw_content=message.content,
            created=message_timestamp,
            puzzle_number=puzzle_number,
            attempt_count=attempt_count,
            user_id=user_id,
        )

        db.session.add_all([user, result])
        db.session.commit()
