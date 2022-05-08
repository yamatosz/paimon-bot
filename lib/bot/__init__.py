import discord
from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler  
from apscheduler.triggers.cron import CronTrigger    
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
from discord import Intents, Embed
from datetime import datetime
from glob import glob
from .. import db


PREFIX = "!"
OWNER_ID = 428994845403774978
ATIVIDADE = discord.Game(name='Lolzito')

## Cria uma lista com todos os arquivos cogs
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]
        

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
                        command_prefix=PREFIX,
                        owner_id=OWNER_ID,
                        intents=Intents.all(),
                        activity = ATIVIDADE)

    ## Funcao para inciar o carramento da lista com os cogs
    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f'{cog}(cog) carregado.')

        print('Setup completo')
        print('-------------------')

    def run(self, version):
        self.VERSION = version

        print('-------------------')
        print('Carregando setup...')
        self.setup()

        with open("./lib/bot/token.0", "r", encoding="utf-8") as r:
            self.TOKEN = r.read()

        print("Rodando bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            await ctx.reply("Comando invalido.")
        
        else:
            raise exc.original


    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Algo deu errado")

        channel = self.get_channel(928977970712965120)
        await channel.send("Um erro aconteceu.")
        raise

    async def on_connect(self):
        print("Iniciando")

    async def on_disconnect(self):
        print("Bot Desconectado")

    async def weblogin_reminder(self):
        channel = self.get_channel(928977970712965120)
        embed = Embed(
            title='Web-login', description='Lembre do web-login',
            colour=0xFFFF00,
            timestamp=datetime.utcnow(),
            link=''
        )
        fields = [
            ('Lembrete Diário', 'Web check-in da Miojo', False ),
            ('Pobre', 'Ei você que é pobre e não casha', False),
            ('Login', 'Vai fazer teu login na hoyolab e garanta recompensas incríveis', False),
            ('Link', 'https://www.encurtador.com.br/fiEM3', False)
        ]
        for field, value, inline, in fields:
            embed.add_field(name=field, value=value, inline=inline)
        embed.set_author(name=self.user.name, icon_url=self.user.avatar_url)
        embed.set_footer(text="tropa da ayaka testuda")
        embed.set_thumbnail(url=self.user.avatar_url)
        embed.set_image(url='https://cdn.discordapp.com/attachments/972704282954567730/972704477675147314/unknown.png')

        await channel.send(embed=embed)


    async def on_ready(self):
        if not self.ready:
            self.ready=True
            
            ## Iniciar os eventos de agendamento
            ##self.scheduler.start()
            ##self.scheduler.add_job(self.weblogin_reminder, CronTrigger(second=0))

            
            ## Embed de alerta ao ficar online
            autor = self.get_user(self.owner_id)
            channel = self.get_channel(928977970712965120)
            guild = self.get_guild(916664641009090590)
            embed = Embed(
                                title='Online',
                                description='Alerta ao ficar online',
                                colour=0xFFFF00,
                                timestamp=datetime.utcnow()
            )
            fields= [("Status: ", "Online", True),
                     ("Prefixo: ", f"`{PREFIX}`", True),
                     ("Qualquer duvida chamar: ", f"{autor.mention}", False)]
            for name, value, inline in fields:
               embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name=self.user.name, icon_url=self.user.avatar_url)
            embed.set_footer(text="tropa da ayaka testuda")
            embed.set_thumbnail(url=self.user.avatar_url)
            embed.set_image(url=guild.icon_url)

            ## Envia o embed e apaga apos 60 segundos
            await channel.send(embed=embed, delete_after=60)

            ##     
    
            print("Bot pronto")
            print('--------')
            print(f"|{self.user.name}|")
            print('--------')

            self.ready = True

        else:
            print("Reconectando Bot")   

    async def on_message(self, ctx):
        await self.process_commands(ctx)
        
bot = Bot()