from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}")

    @commands.command(name="greet")
    async def greet(self, ctx):
        """ Reply Hello """
        member = ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}")
        else:
            await ctx.send(":)")

    @commands.command(name="hello", description="Greet user :)")
    async def hello(self, ctx):
        """ Greets Users """
        ch = ctx.message.channel
        await ch.send(f"Hello {ctx.message.author.mention}"
                      "\nHow can I help you?")


def setup(bot):
    bot.add_cog(Greetings(bot))
