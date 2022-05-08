from datetime import datetime
import discord
from discord.ext.commands import Bot as BotBase
from discord import Intents, Embed


PREFIX = "!"
OWNER_ID = [428994845403774978]
ATIVIDADE = discord.Game(name='Lolzito')

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        super().__init__(
                        command_prefix=PREFIX,
                        owner_ids=OWNER_ID,
                        intents=Intents.all(),
                        activity = ATIVIDADE)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as r:
            self.TOKEN = r.read()

        print("Rodando bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Iniciando")

    async def on_disconnect(self):
        print("Bot Disconectado")

    async def on_ready(self):
        if not self.ready:
            self.ready=True
            print("Bot pronto")
            print(f"{self.user.name}")
            """
            channel = self.get_channel(928977970712965120)
            guild = self.get_guild(916664641009090590)
            embed = Embed(
                                title='Titulo',
                                descripition='Descrição',
                                colour=0xFFFF00,
                                timestamp=datetime.utcnow()
            )
            fields= [("Nome", "Valor", True),
                     ("Segundo campo", "Valor do segundo campo", True),
                     ("Terceiro campo", "Valor do segundo campo", False)]
            for name, value, inline in fields:
               embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name=self.user.name, icon_url=self.user.avatar_url)
            embed.set_footer(text="Rodapézito")
            embed.set_thumbnail(url=self.user.avatar_url)
            embed.set_image(url=guild.icon_url)
            await channel.send(embed=embed, delete_after=60)
            """

        else:
            print("Reconectando Bot")   

    async def on_message(self, message):
        pass
        
bot = Bot()