from definições_avançado import estados, fatos
import discord
from discord.ext import commands
from random import choice
import random
from re import fullmatch
from os import getenv, path
from dotenv import load_dotenv
load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')

imagens = ['indignado.png']


@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message(msg):
    if msg.content.startswith('$'):    
        if msg.author.bot:
            return
        autor = msg.author.id
        if autor not in fatos:
            fatos[autor] = {
                'indignado': 20
                }

        if msg.content.startswith('$quao indignado vc esta?') and fatos[autor]['indignado'] in range(0, 11):
            flip = fatos[autor]['indignado']
            mais = flip + 2
            while fatos[autor]['indignado'] >= flip:
                flip = random.randint(1, mais)
            fatos[autor]['indignado'] = flip
            if fatos[autor]['indignado'] == 1:
                await msg.channel.send('tô um pouquinho indignado')
            if fatos[autor]['indignado'] == 2:
                await msg.channel.send('tô ficando indignado')
            if fatos[autor]['indignado'] == 3:
                await msg.channel.send('tô pouco indignado')
            if fatos[autor]['indignado'] == 4:
                await msg.channel.send('mais ou menos, pra menos')
            if fatos[autor]['indignado'] == 5:
                await msg.channel.send('tô meio indignado')
            if fatos[autor]['indignado'] == 6:
                await msg.channel.send('mais ou menos, pra mais')
            if fatos[autor]['indignado'] == 7:
                await msg.channel.send('tô bem indigando')
            if fatos[autor]['indignado'] == 8:
                await msg.channel.send('tô bem indigando, melhor não puchar a sua sorte')
            if fatos[autor]['indignado'] == 9:
                await msg.channel.send('mais um puche e eu juro que eu explodo')
            if fatos[autor]['indignado'] >= 10:
                await msg.channel.send('tô indignado pra caralho')
                fatos[autor]['indignado'] = 0
                await msg.reply(file= discord.File(path.join('imagens', random.choice(imagens))))
            return
        if msg.content.startswith('$quao indignado vc esta?') and fatos[autor]['indignado'] == 20:
            await msg.channel.send('Quem eu sou?')
        if msg.content.startswith('$crocodilo indignado') and fatos[autor]['indignado'] == 20:
            fatos[autor]['indignado'] = 0
            await msg.channel.send('O que foi?')
        if msg.content.startswith('$crocodilo indignado') and fatos[autor]['indignado'] in range(1, 10):
            await msg.channel.send('Me pergunta o quão indignado eu tô')


        
bot.run(getenv('DISCORD_TOKEN'))