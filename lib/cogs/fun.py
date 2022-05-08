from discord.ext.commands import Cog, command

## Cog fun para testes

class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @Cog.listener()
    async def on_ready(self):
        pass
    '''
    @Cog.command()
    async def hello(self, ctx, *, member:discord.Member= None):
        member = member or ctx.author
        if self._last_member is None or self._last_member != member.id:
            await ctx.send(f'Oioi {member.name}')
        else:
            await ctx.send(f'Oioi {member.name}, você me parece familiar.')

        self._last_member = member
    '''

def setup(bot):
    bot.add_cog(Fun(bot))