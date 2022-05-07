from discord.ext.commands import Bot as BotBase
from discord import Intents

PREFIX = "!"
OWNER_ID = [428994845403774978]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        super().__init__(
                        command_prefix=PREFIX,
                        owner_ids=OWNER_ID,
                        intents=Intents.all())

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

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
        else:
            print("Reconectando Bot")   

    async def on_message(self):
        pass
        
bot = Bot()