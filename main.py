import discord
from dotenv import dotenv_values


class Client(discord.Client):
    """Main Class for The Discord Bot"""
    async def on_ready(self):
        print(f"Logged in as {self.user} ")

    async def on_message(self, message):
        self.ch = message.channel
        self.help = """
Help Menu:\n
```
/help: To get available cmds \n
/hello: To Greet
```
"""
        if message.author == self.user:
            return

        if message.content.lower() == "/help":
            await self.ch.send(self.help)

        if message.content.lower() == "/hello":
            author = str(message.author)
            await self.ch.send(f'Hello {author.rsplit("#")[0]},'
                               '\nHow can I help you?')


config = dotenv_values(".env")
client = Client()
client.run(config["TOKEN"])
