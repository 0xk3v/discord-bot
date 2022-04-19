# import discord
from discord.ext import commands
from dotenv import dotenv_values

banner = """
```
Help Menu:
------------
/help: To get available cmds
/hello: To Greet
```
"""


class Client(commands.Bot):
    """Main Class for The Discord Bot"""
    async def on_ready(self):
        print(f"Logged in as {self.user} ")

    async def on_message(self, message):
        self.ch = message.channel
        self.help = banner
        if message.author == self.user:
            return

        if message.content.lower() == "/help":
            await self.ch.send(self.help)

        if message.content.lower() == "/hello":
            await self.ch.send(f'Hello {message.author.mention},'
                               '\nHow can I help you?')


config = dotenv_values(".env")
client = Client(command_prefix="+")
client.run(config["TOKEN"])
