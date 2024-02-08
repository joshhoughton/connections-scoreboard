import os

import discord

from connections_scoreboard.app import create_app
from connections_scoreboard.bot._message_handler import handle_message


app = create_app()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_GUILD = os.getenv("DISCORD_GUILD")
DISCORD_CHANNEL = int(os.getenv("DISCORD_CHANNEL"))

if DISCORD_TOKEN is None:
    raise ValueError("DISCORD_TOKEN is not set in the environment variables.")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    channel = client.get_channel(DISCORD_CHANNEL)

    if channel is not None:
        async for message in channel.history(limit=500):
            handle_message(message)


@client.event
async def on_message(message: discord.Message):
    message_id = str(message.id)

    if message.author == client.user:
        app.logger.debug(f"{message_id}: ignoring message from self")
        return

    if not isinstance(message.channel, discord.TextChannel):
        app.logger.debug(f"{message_id}: ignoring message from non-text channel")
        return

    if message.channel.id != DISCORD_CHANNEL:
        app.logger.debug(f"{message_id}: ignoring message from non-scoreboard channel")
        return

    handle_message(message)


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
