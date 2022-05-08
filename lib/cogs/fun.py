from discord.ext.commands import Cog, command
import discord

## Cog fun para testes

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @command(name='hello', aliases=['h'])
    async def hhello(self, ctx):
        await ctx.reply(f'Ola {ctx.author.mention}!')

    @Cog.listener()
    async def on_ready(self):
        pass
    @command()
    async def aahello(self, ctx, member:discord.Member= None):
        member = member or ctx.author
        if self._last_member is None or self._last_member != member.id:
            await ctx.send(f'Oioi {member.name}')
        else:
            await ctx.send(f'Oioi {member.name}, você me parece familiar.')

        self._last_member = member

def setup(bot):
    bot.add_cog(Fun(bot))