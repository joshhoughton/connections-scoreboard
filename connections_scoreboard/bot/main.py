import os

import discord

from connections_scoreboard.app import create_app, db
from connections_scoreboard.app.db.models import Message, User


app = create_app()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
DISCORD_CHANNEL = os.getenv("DISCORD_CHANNEL")

if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set in the environment variables.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    with app.app_context():
        user_id = str(message.author.id)
        nick = (
            message.author.nick if isinstance(message.author, discord.Member) else None
        )
        global_name = message.author.name
        avatar_url = str(message.id)
        message_id = str(message.id)
        message_content = message.content
        message_timestamp = str(message.created_at)

        user = User.query.filter_by(id=user_id).first()

        if user:
            pass
        else:
            user = User(
                id=user_id, nick=nick, global_name=global_name, avatar_url=avatar_url
            )

        # Check if id already exists
        if Message.query.filter_by(id=message_id).first():
            return "ID already exists!"

        message = Message(
            id=message_id,
            content=message_content,
            created=message_timestamp,
            user_id=user.id,
        )

        db.session.add_all([user, message])
        db.session.commit()
    # logging.debug(f"Data to be sent: {data}")

    # # Send the POST request to your Flask server
    # response = requests.post("http://localhost:5000/submit_result", json=data)

    # # Check the response status code
    # if response.status_code == 200:
    #     print("Data sent successfully!")
    #     print(response.text)
    # else:
    #     print("Failed to send data.")


client.run(DISCORD_TOKEN)
