# bot.py
import os

import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

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

    print(message.author, message.content)

    with open("scores.txt", "a") as f:
        f.write(f"{message.author} {message.content}\n")

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')


client.run(TOKEN)
