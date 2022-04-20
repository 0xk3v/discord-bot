from discord.ext import commands
from dotenv import dotenv_values


client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    """ Event to Check if The Bot is Active """
    print(f"Logged in as {client.user} ")


@client.event
async def on_message(message):
    """ Event Handler for messages """
    if message.author == client.user:
        return
    await client.process_commands(message)


@client.command(name="version", description="Get The bot Version")
async def version(ctx):
    """ Function to handle version command """
    await ctx.message.channel.send("```version: 0.0.1```")


@client.command(name="hello", description="Greet user :)")
async def hello(ctx):
    """ Function to handle hello command """
    ch = ctx.message.channel
    await ch.send(f"Hello {ctx.message.author.mention}"
                  "\nHow can I help you?")


config = dotenv_values(".env")
client.run(config["TOKEN"])
