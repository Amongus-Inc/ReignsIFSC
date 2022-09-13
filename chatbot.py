from os import getenv
from dotenv import load_dotenv
import discord
load_dotenv()
import random
lista = ["melancia com mel", "the rock cocaina", "peitinhos falaciosos", "eita como eu to de boa", "eu falo tudo que penso"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!juca'):
            await message.reply(random.choice(lista), mention_author=True)




intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(getenv("DISCORD_TOKEN"))