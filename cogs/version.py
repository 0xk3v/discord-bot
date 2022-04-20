from discord.ext import commands


class Version(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="version")
    async def version(self, ctx):
        """ Prints the bot version  """
        await ctx.message.channel.send("```version: 0.0.1```")


def setup(bot):
    bot.add_cog(Version(bot))
