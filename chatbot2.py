from definições import estados, partidas, status_dos_jogadores
import discord
from discord.ext import commands
from random import choice
import random
from re import fullmatch
from os import getenv
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='')


@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.event
async def on_message(msg):
    autor = msg.author.id
    if autor == bot.application_id:
        return

    if autor not in partidas:
        partidas[autor] = 0
        status_dos_jogadores[autor] = {
            'Sanidade': 50,
            'Popularidade': 50,
            'Notas': 50,
            'Inteligência': 50
        }


    estado_do_jogador = estados[partidas[autor]]
    status_sanidade = status_dos_jogadores[autor]['Sanidade']
    status_popularidade = status_dos_jogadores[autor]['Popularidade']
    status_notas = status_dos_jogadores[autor]['Notas']
    status_inteligencia = status_dos_jogadores[autor]['Inteligência']

    for key, value in estado_do_jogador['positivo_proximos_estados'].items():

        if fullmatch(key, msg.content):
            
            await msg.channel.send(estado_do_jogador['frases_positivas'])

            status_dos_jogadores[autor]['Sanidade'] = status_sanidade + int(estado_do_jogador['positivos_sanidade'])
            status_dos_jogadores[autor]['Popularidade'] = status_popularidade + int(estado_do_jogador['positivos_popularidade'])
            status_dos_jogadores[autor]['Notas'] = status_notas + int(estado_do_jogador['positivos_notas'])
            status_dos_jogadores[autor]['Inteligência'] = status_inteligencia + int(estado_do_jogador['positivos_inteligência'])

            await msg.channel.send(status_dos_jogadores[autor])
            partidas[autor] = value
            if estados[partidas[autor]]['2_estapas'] == 0: #usar um diferente de 0 aqui para ser mais facil
                estado_do_jogador = estados[partidas[autor]]
            else:
                partidas[autor] = random.randint(0, 3)
                flip = random.randint(16, 17)#fazer ficar 1 à 25
                if flip == 17:
                    partidas[autor] = random.randint(2048, 2051)
            estado_do_jogador = estados[partidas[autor]]
            await msg.channel.send(partidas[autor])
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
    for key, value in estado_do_jogador['negativa_proximos_estados'].items():
        if fullmatch(key, msg.content):
            
            await msg.channel.send(estado_do_jogador['frases_negativas'])

            status_dos_jogadores[autor]['Sanidade'] = status_sanidade + int(estado_do_jogador['negativos_sanidade'])
            status_dos_jogadores[autor]['Popularidade'] = status_popularidade + int(estado_do_jogador['negativos_popularidade'])
            status_dos_jogadores[autor]['Notas'] = status_notas + int(estado_do_jogador['negativos_notas'])
            status_dos_jogadores[autor]['Inteligência'] = status_inteligencia + int(estado_do_jogador['negativos_inteligência'])

            await msg.channel.send(status_dos_jogadores[autor])
            partidas[autor] = value
            if estados[partidas[autor]]['2_estapas'] == 0: #usar um diferente de 0 aqui para ser mais facil
                estado_do_jogador = estados[partidas[autor]]
            else:
                partidas[autor] = random.randint(0, 3)
                flip = random.randint(16, 17)#fazer ficar 1 à 25
                if flip == 17:
                    partidas[autor] = random.randint(2048, 2051)
            estado_do_jogador = estados[partidas[autor]]
            await msg.channel.send(partidas[autor])
            await msg.channel.send(choice(estado_do_jogador['frases']))
            return
    if partidas[autor] == 0:
        await msg.channel.send(choice(estado_do_jogador['frases']))
    else:
        await msg.channel.send('I\'m sorry Dave, I\'m afraid I can\'t do that.')


bot.run(getenv('DISCORD_TOKEN'))