from discord.ext import commands
from dotenv import dotenv_values
import libs.config as config

client = commands.Bot(command_prefix="/")

extensions = config.get_config("cogs")

if len(extensions) > 0:
    print("[INFO] : Loading Cogs...")
    for ext in extensions:
        try:
            client.load_extension(ext)
            print(f"[SUCCESS] : {ext} Loaded.")
        except Exception as e:
            print(f"Error while loading {ext}\n{str(e)} ")


@client.event
async def on_ready():
    """Event to Check if The Bot is Active"""
    print(f"Logged in as {client.user} ")


@client.event
async def on_message(message):
    """Event Handler for messages"""
    if message.author == client.user:
        return
    await client.process_commands(message)


if __name__ == "__main__":
    config = dotenv_values(".env")
    client.run(config["TOKEN"])
